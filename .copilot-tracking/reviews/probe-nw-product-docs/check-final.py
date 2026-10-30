# Read-only structural probe for docs/product (second review, final state).
# Writes nothing. Prints findings to stdout only.
import os
import re
from collections import defaultdict

ROOT = r'C:\demos\northwind-workshop\docs\product'

def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()

RELS = ['azure-r1', 'azure-r2', 'azure-r3', 'dotnet-r1', 'dotnet-r2', 'dotnet-r3', 'dotnet-r4']
RELIDX = {'azure-r1': 1, 'azure-r2': 2, 'azure-r3': 3, 'dotnet-r1': 1, 'dotnet-r2': 2, 'dotnet-r3': 3, 'dotnet-r4': 4}
RELTRACK = {r: ('track-azure' if r.startswith('azure') else 'track-dotnet') for r in RELS}
FILES = ['backlog.md', 'traceability.md', 'README.md', 'product-requirements.md',
         'business-requirements.md', 'experiments.md'] + ['releases/%s.md' % r for r in RELS]
DOCS = {f: rd(f) for f in FILES}
ID_RX = r'(?:EP|FT|EN|US)-(?:AZ|DN)-\d{2,3}'
SRC_RX = r'\b(?:BR|NFR|C|CS|ES|SM|P|OQ)-\d{2,3}\b'
OOS_RX = re.compile(r'\b(BR-1[4-9]|NFR-09|C-07|C-08|SM-05|SM-06|OQ-04|OQ-05|CS-2[4-8]|ES-3[2-7])\b|\bBA-03\b')
TRACKS = ['track-azure', 'track-dotnet']

problems = defaultdict(list)   # check name -> list of messages
def bad(check, msg):
    problems[check].append(msg)

def expand(s):
    out = set()
    rng = re.compile(r'`?(' + ID_RX + r')`?\s+to\s+`?(' + ID_RX + r')`?')
    for m in rng.finditer(s):
        pa, na = m.group(1).rsplit('-', 1)
        pb, nb = m.group(2).rsplit('-', 1)
        if pa == pb:
            for n in range(int(na), int(nb) + 1):
                out.add('%s-%0*d' % (pa, len(na), n))
    out |= set(re.findall(ID_RX, rng.sub(' ', s)))
    return out

# ---------- 1. Register (backlog section 11) ----------
bl = DOCS['backlog.md'].splitlines()
i11 = next(i for i, l in enumerate(bl) if l.startswith('## 11.'))
reg = {}
reg_rows = 0
for l in bl[i11:]:
    if not re.match(r'^\| `' + ID_RX + r'` \|', l):
        continue
    reg_rows += 1
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    rid, typ, parent, title, track, rel, prio, src = c[:8]
    rid = rid.strip('`')
    if rid in reg:
        bad('register', 'duplicate register row %s' % rid)
    reg[rid] = dict(type=typ, parent=None if parent == '-' else parent.strip('`'),
                    title=title, track=track.strip('`'), rel=rel.strip('`'), prio=prio,
                    src=set(re.findall(SRC_RX, src)))
print('REGISTER rows=%d unique=%d' % (reg_rows, len(reg)))
cnt = defaultdict(int)
for k, v in reg.items():
    cnt[(v['track'], v['type'])] += 1
print('REGISTER by track/type:', dict(cnt))
print('REGISTER release counts:', {r: sum(1 for v in reg.values() if v['rel'] == r) for r in RELS},
      'unplanned=', sum(1 for v in reg.values() if v['rel'] == '-'))

# ---------- 2. Item blocks ----------
hdr = re.compile(r'^(#{2,6}) (' + ID_RX + r')\b\s*(.*)$')
heads = [i for i, l in enumerate(bl[:i11]) if l.startswith('#')]
items = {}
for k, h in enumerate(heads):
    m = hdr.match(bl[h])
    if not m:
        continue
    end = heads[k + 1] if k + 1 < len(heads) else i11
    body = '\n'.join(bl[h + 1:end])
    rid = m.group(2)
    if rid in items:
        bad('items', 'duplicate item block %s' % rid)
    def first(rx):
        mm = re.search(rx, body, re.M)
        return mm.group(1).strip() if mm else None
    tags = first(r'^\* Tags: (.+)$') or ''
    tagl = [t.strip().strip('`') for t in tags.split(',') if t.strip()]
    tl = re.search(r'^\* Type: (\w+) \| Priority: (.+?) \| Status: (\w+)(?: \| Parent: `([^`]+)`)?\s*$', body, re.M)
    src_line = first(r'^\* \(source: (.+)\)\s*$')
    dep = first(r'^\* Depends on \(same track\): (.+)$')
    items[rid] = dict(
        head=m.group(3), tags=tagl, raw_tags=tags,
        type=tl.group(1) if tl else None, prio=tl.group(2) if tl else None,
        status=tl.group(3) if tl else None, parent=(tl.group(4) if tl and tl.group(4) else None),
        src_line=src_line, src=set(re.findall(SRC_RX, src_line or '')),
        deps=set() if (dep is None or dep.lower().startswith('none')) else expand(dep),
        dep_raw=dep, enables=first(r'^\* Enables: (.+)$'),
        contains=first(r'^\* (?:Contains|Enablers): (.+)$'),
        used=first(r'^\* ASSUMPTION / OPEN used: (.+)$'),
        story=first(r'\*\*Story\.\*\* (.+)'),
        crit=re.findall(r'^\d+\. (.+)$', body, re.M), body=body)
print('ITEM blocks=%d ; register-only=%s ; item-only=%s' % (
    len(items), sorted(set(reg) - set(items)), sorted(set(items) - set(reg))))

# ---------- 3. Tags, parent/child, dependencies ----------
for rid, it in items.items():
    tr = [t for t in it['tags'] if t in TRACKS]
    rl = [t for t in it['tags'] if t.startswith(('azure-r', 'dotnet-r'))]
    other = [t for t in it['tags'] if t not in TRACKS and t not in RELIDX]
    if len(tr) != 1:
        bad('tags', '%s track tags=%s' % (rid, tr))
    if len(rl) > 1:
        bad('tags', '%s two release tags=%s' % (rid, rl))
    if other:
        bad('tags', '%s unexpected tags=%s' % (rid, other))
    if rl and tr and not all(RELTRACK.get(r) == tr[0] for r in rl):
        bad('tags', '%s release/track mismatch %s %s' % (rid, rl, tr))
    if not rl and it['status'] is not None and rid[:2] == 'US' or (not rl and it['type'] == 'Story' and False):
        pass
    r = reg.get(rid)
    if r:
        exp_rel = rl[0] if rl else '-'
        if r['rel'] != exp_rel:
            bad('register-vs-item', '%s release reg=%s item=%s' % (rid, r['rel'], exp_rel))
        exp_track = tr[0] if tr else None
        if r['track'] != exp_track:
            bad('register-vs-item', '%s track reg=%s item=%s' % (rid, r['track'], exp_track))
        if r['type'] != it['type']:
            bad('register-vs-item', '%s type reg=%s item=%s' % (rid, r['type'], it['type']))
        rp = r['prio'].split(' ')[0]
        ip = (it['prio'] or '').split(' ')[0]
        if rp != ip:
            bad('register-vs-item', '%s priority reg=%s item=%s' % (rid, r['prio'], it['prio']))
        if r['parent'] != it['parent']:
            bad('register-vs-item', '%s parent reg=%s item=%s' % (rid, r['parent'], it['parent']))
        if set(r['src']) != it['src']:
            bad('register-vs-item', '%s sources reg-only=%s item-only=%s' % (
                rid, sorted(r['src'] - it['src']), sorted(it['src'] - r['src'])))
        if r['title'].strip() != it['head'].strip():
            bad('register-vs-item', '%s title reg="%s" item="%s"' % (rid, r['title'], it['head']))
    if it['parent']:
        p = items.get(it['parent'])
        if not p:
            bad('parent-child', '%s parent %s has no block' % (rid, it['parent']))
        else:
            ptr = [t for t in p['tags'] if t in TRACKS]
            prl = [t for t in p['tags'] if t.startswith(('azure-r', 'dotnet-r'))]
            if ptr != tr:
                bad('parent-child', '%s track differs from parent %s' % (rid, it['parent']))
            if prl != rl:
                bad('parent-child', '%s release %s differs from parent %s %s' % (rid, rl, it['parent'], prl))
            if p['contains'] and rid not in p['contains'] and rid[:2] == 'US' or (p['contains'] and rid[:2] == 'EN' and rid not in p['contains']):
                bad('parent-child', '%s not listed in parent %s Contains/Enablers' % (rid, it['parent']))
    # dependencies: same track, not later release, no unplanned prerequisite for planned item
    for d in sorted(it['deps']):
        di = items.get(d)
        if di is None:
            bad('deps', '%s depends on unknown %s' % (rid, d)); continue
        dtr = [t for t in di['tags'] if t in TRACKS]
        drl = [t for t in di['tags'] if t.startswith(('azure-r', 'dotnet-r'))]
        if dtr != tr:
            bad('deps', '%s depends on other track %s' % (rid, d))
        if rl and drl and RELIDX[drl[0]] > RELIDX[rl[0]]:
            bad('deps', '%s (%s) depends on later release %s (%s)' % (rid, rl[0], d, drl[0]))
        if rl and not drl:
            bad('deps', '%s planned depends on unplanned %s' % (rid, d))
        if d == rid:
            bad('deps', '%s self dependency' % rid)

# ---------- 4. Rank tables (section 4) ----------
i41 = bl.index('### 4.1 `track-azure`')
i42 = bl.index('### 4.2 `track-dotnet`')
i5 = next(i for i, l in enumerate(bl) if l.startswith('## 5.'))
rank = {'track-azure': [], 'track-dotnet': []}
for l in bl[i41:i42]:
    if re.match(r'^\| \d+ \|', l):
        rank['track-azure'].append([x.strip() for x in l.strip().strip('|').split('|')])
for l in bl[i42:i5]:
    if re.match(r'^\| (\d+|-) \|', l):
        rank['track-dotnet'].append([x.strip() for x in l.strip().strip('|').split('|')])
for tr, rows in rank.items():
    print('RANK %s rows=%d' % (tr, len(rows)))
    pos = {}
    last_rel = 0
    for n, c in enumerate(rows):
        rid = c[1].strip('`')
        pos[rid] = n
        rr = c[4].strip('`')
        if rid not in items:
            bad('rank', 'rank row %s not an item' % rid); continue
        r = reg.get(rid, {})
        if r.get('rel') != rr and not (rr == 'none' and r.get('rel') == '-'):
            bad('rank', '%s rank release %s vs register %s' % (rid, rr, r.get('rel')))
        if RELIDX.get(rr, 0) < last_rel:
            bad('rank', '%s rank order goes back a release' % rid)
        last_rel = max(last_rel, RELIDX.get(rr, 0))
        rdeps = set() if c[7].strip().lower() == 'none' else expand(c[7])
        idep = items[rid]['deps']
        if rdeps != idep:
            bad('rank-vs-item-deps', '%s rank deps=%s item deps=%s' % (rid, sorted(rdeps), sorted(idep)))
    planned = {k for k, v in reg.items() if v['track'] == tr and v['rel'] != '-' and v['type'] in ('Story', 'Enabler')}
    ranked = set(pos)
    unpl = {k for k, v in reg.items() if v['track'] == tr and v['rel'] == '-' and v['type'] in ('Story', 'Enabler')}
    if (planned | unpl) - ranked:
        bad('rank', '%s stories/enablers missing from rank table: %s' % (tr, sorted((planned | unpl) - ranked)))
    for rid in ranked:
        for d in items[rid]['deps']:
            if d in pos and pos[d] > pos[rid]:
                bad('rank', '%s ranked before its dependency %s' % (rid, d))
    print('RANK %s story+enabler planned=%d unplanned=%d' % (tr, len(planned), len(unpl)))

# ---------- 5. Per-item story and criteria form (ES-05, M-1) ----------
noform = []; nowhen = []; nogwt = []
for rid, it in items.items():
    if it['type'] in ('Story', 'Enabler'):
        s = it['story'] or ''
        if not (re.search(r'\bAs an? .+?, I want\b', s) and 'so that' in s):
            noform.append(rid)
        if not it['crit']:
            nogwt.append(rid)
        for c in it['crit']:
            if 'Given' not in c or 'When' not in c or 'Then' not in c:
                nowhen.append((rid, c[:90]))
print('STORY FORM missing As a/I want/so that:', noform)
print('CRITERIA with no criteria list:', nogwt)
print('CRITERIA not full Given/When/Then: %d (items %d)' % (len(nowhen), len({a for a, _ in nowhen})))
for rid, c in nowhen[:12]:
    print('   ', rid, '|', c)

# ---------- 6. A-04 freshness wording ----------
for rid, it in items.items():
    if 'BR-04' in it['src'] and '02:00 batch' not in it['body']:
        bad('A-04', '%s cites BR-04 but lacks "as of the 02:00 batch" wording' % rid)
    if rid.startswith('US-DN') and 'BR-04' in it['body'] and '02:00 batch' not in it['body']:
        pass

# ---------- 7. EN-DN-10 coverage for .NET stories (H-1) ----------
def reach(start, graph):
    seen = set(); st = [start]
    while st:
        x = st.pop()
        for y in graph.get(x, ()):
            if y not in seen:
                seen.add(y); st.append(y)
    return seen
graph = {k: v['deps'] for k, v in items.items()}
noten = []; direct = []
for rid, it in items.items():
    if not rid.startswith('US-DN') or rid == 'EN-DN-10':
        continue
    if 'EN-DN-10' in it['deps']:
        direct.append(rid)
    elif 'EN-DN-10' not in reach(rid, graph):
        noten.append(rid)
print('US-DN stories with direct EN-DN-10 dependency: %d' % len(direct))
print('US-DN stories NOT reaching EN-DN-10 (direct or chain):', noten)
for rid in noten:
    print('   %s | src=%s | deps=%s' % (rid, sorted(items[rid]['src']), sorted(items[rid]['deps'])))
print('EN-DN-10 block dependency line:', items['EN-DN-10']['dep_raw'])
m10 = re.search(r'EN-DN-10.*', DOCS['backlog.md'][DOCS['backlog.md'].find('##### EN-DN-10'):][:0] or '')

# ---------- 8. Out-of-scope identifiers (Q-02) ----------
for rid, it in items.items():
    hits = OOS_RX.findall(it['src_line'] or '')
    if hits:
        bad('oos-source', '%s source line cites out-of-scope %s' % (rid, hits))
    if OOS_RX.search(it['body']):
        for m in OOS_RX.finditer(it['body']):
            pass
oos_lines = []
for f, t in DOCS.items():
    for n, l in enumerate(t.splitlines(), 1):
        for m in OOS_RX.finditer(l):
            oos_lines.append((f, n, m.group(0), l.strip()[:150]))
print('OUT-OF-SCOPE ID mentions across files: %d' % len(oos_lines))
for x in oos_lines:
    print('   %s:%d [%s] %s' % x)

# ---------- 9. Coverage of BR/NFR (Q-03, Q-04) ----------
planned_src = defaultdict(set)
for rid, v in reg.items():
    if v['rel'] != '-':
        for s in v['src']:
            planned_src[s].add(rid)
for br in ['BR-%02d' % i for i in range(1, 14)] + ['NFR-%02d' % i for i in range(1, 9)]:
    if not planned_src.get(br):
        bad('coverage', '%s has no planned item' % br)
for nf in ['NFR-03', 'NFR-04', 'NFR-05']:
    for tr in TRACKS:
        ids = [k for k in planned_src.get(nf, ()) if reg[k]['track'] == tr]
        if nf == 'NFR-04' and tr == 'track-azure':
            if ids:
                print('NFR-04 Azure-tagged planned items:', ids)
            continue
        if not ids:
            bad('coverage', '%s has no planned %s item' % (nf, tr))
print('COVERAGE NFR-04 sources(planned .NET):', sorted(k for k in planned_src.get('NFR-04', ()) ))
print('COVERAGE BR-04 items:', sorted(planned_src.get('BR-04', ())))

# ---------- 10. Release files section 3 vs register ----------
def section(t, prefix):
    out = []; on = False
    for l in t.splitlines():
        if l.startswith('## '):
            if on:
                break
            on = l.startswith(prefix)
            continue
        if on:
            out.append(l)
    return out

for r in RELS:
    t = DOCS['releases/%s.md' % r]
    rows = {}
    for l in section(t, '## 3.'):
        m = re.match(r'^\| `(' + ID_RX + r')` \|', l)
        if m:
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            rows[m.group(1)] = c
    regset = {k for k, v in reg.items() if v['rel'] == r}
    if set(rows) != regset:
        bad('release-vs-register', '%s rows-only=%s reg-only=%s' % (r, sorted(set(rows) - regset), sorted(regset - set(rows))))
    for k, c in rows.items():
        if k in reg:
            if reg[k]['title'] != c[3]:
                bad('release-vs-register', '%s %s title differs' % (r, k))
            if c[4].strip('`') != reg[k]['prio'].split(' ')[0] and c[4].split(' ')[0] != reg[k]['prio'].split(' ')[0]:
                bad('release-vs-register', '%s %s priority %s vs %s' % (r, k, c[4], reg[k]['prio']))
            if RELTRACK[r] not in c[5] or r not in c[5]:
                bad('release-vs-register', '%s %s tags %s' % (r, k, c[5]))
            if set(re.findall(SRC_RX, c[6])) != reg[k]['src']:
                bad('release-vs-register', '%s %s sources differ' % (r, k))
    m = re.search(r'\| Items in this release \| (\d+): ([^|]+?) \(section 3\)', t)
    if m:
        total = int(m.group(1))
        if total != len(regset):
            bad('release-header', '%s header total %d vs register %d' % (r, total, len(regset)))
        print('RELEASE %s header=%s | register=%d | rows=%d' % (r, m.group(2), len(regset), len(rows)))
    else:
        bad('release-header', '%s no items header line found' % r)
    # any non-member item ID listed in section 3?
    ids3 = set(re.findall(ID_RX, '\n'.join(section(t, '## 3.'))))
    if ids3 - regset:
        bad('release-section3', '%s section 3 mentions non-member IDs %s' % (r, sorted(ids3 - regset)))

# ---------- 11. Traceability Appendix A vs register ----------
tr_t = DOCS['traceability.md']
app = {}
for l in tr_t[tr_t.find('## Appendix A'):].splitlines():
    m = re.match(r'^\| `(' + ID_RX + r')` \|', l)
    if m:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        app[m.group(1)] = c
regSL = {k for k, v in reg.items() if v['type'] in ('Story', 'Enabler')}
print('APPENDIX A rows=%d ; register stories+enablers=%d' % (len(app), len(regSL)))
if set(app) != regSL:
    bad('appendix-A', 'rows-only=%s reg-only=%s' % (sorted(set(app) - regSL), sorted(regSL - set(app))))
for k, c in app.items():
    if k not in reg:
        continue
    r = reg[k]
    # columns: 0 ID | 1 Type | 2 Title | 3 Feature | 4 Track | 5 Release | 6 Priority | 7 Covers | 8 Other
    if c[4].strip('`') != r['track'] or c[5].strip('`') != r['rel']:
        bad('appendix-A', '%s tags doc=%s/%s reg=%s/%s' % (k, c[4], c[5], r['track'], r['rel']))
    if c[6] != r['prio'] and c[6].split(' ')[0] != r['prio'].split(' ')[0]:
        bad('appendix-A', '%s priority doc=%s reg=%s' % (k, c[6], r['prio']))
    covBR = set(re.findall(r'\b(?:BR|NFR)-\d{2}\b', c[7]))
    covOther = set(re.findall(r'\b(?:C|SM|OQ)-\d{2}\b', c[8]))
    srcBR = {s for s in r['src'] if s.startswith(('BR-', 'NFR-'))}
    srcOther = {s for s in r['src'] if s.startswith(('C-', 'SM-', 'OQ-'))}
    if covBR != srcBR:
        bad('appendix-A', '%s covers doc=%s reg=%s' % (k, sorted(covBR), sorted(srcBR)))
    if covOther != srcOther:
        bad('appendix-A', '%s other doc=%s reg=%s' % (k, sorted(covOther), sorted(srcOther)))
    if c[2].strip() != r['title'].strip():
        bad('appendix-A', '%s title differs' % k)

# ---------- 12. Secrets and forbidden strings across all docs ----------
SECRET = re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}|AccountKey|SharedAccessSignature|Password\s*=|pwd\s*=|-----BEGIN|\b\d{1,3}(?:\.\d{1,3}){3}\b|[\w.+-]+@[\w-]+\.[\w.]+|Server=|Data Source=|\bsk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{10,}|\bxox[bp]-')
hits = []
for f, t in list(DOCS.items()):
    for n, l in enumerate(t.splitlines(), 1):
        for m in SECRET.finditer(l):
            hits.append((f, n, m.group(0)))
print('SECRET-PATTERN hits: %d' % len(hits))
for h in hits[:40]:
    print('   ', h)

# track-power-platform as a tag
for f, t in DOCS.items():
    for n, l in enumerate(t.splitlines(), 1):
        if 'track-power-platform' in l:
            print('track-power-platform at %s:%d: %s' % (f, n, l.strip()[:160]))

# ---------- 13. Status wording ----------
for f in FILES:
    t = DOCS[f]
    st = re.search(r'^\| (?:Status|Status now)[^|]*\|\s*(.+?)\s*\|$', t, re.M)
    sn = re.search(r'Status now: \*\*(.+?)\*\*', t)
    print('STATUS %-32s %s' % (f, (st.group(1)[:110] if st else '-')), '|', (sn.group(1) if sn else ''))

# ---------- 14. Master registers (README) vs wording in each file ----------
rd_ = DOCS['README.md']
A_def = {}; O_def = {}
for l in rd_.splitlines():
    m = re.match(r'^\| (A-\d{2}) \|(.*)$', l)
    if m:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        A_def[c[0]] = dict(text=c[1], owner=c[2], used=c[3])
    m = re.match(r'^\| (OPEN-\d{2}) \|(.*)$', l)
    if m:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        O_def[c[0]] = dict(text=c[1], owner=c[2], track=c[3], rels=c[4], other=c[5])
print('README A defined=%d (%s..%s) ; OPEN defined=%d (%s..%s)' % (
    len(A_def), min(A_def), max(A_def), len(O_def), min(O_def), max(O_def)))
exp_a = {'A-%02d' % i for i in range(1, 47)}
exp_o = {'OPEN-%02d' % i for i in range(1, 34)}
if set(A_def) != exp_a: bad('master', 'A set differs: missing=%s extra=%s' % (sorted(exp_a - set(A_def)), sorted(set(A_def) - exp_a)))
if set(O_def) != exp_o: bad('master', 'OPEN set differs: missing=%s extra=%s' % (sorted(exp_o - set(O_def)), sorted(set(O_def) - exp_o)))

def norm(s):
    return re.sub(r'\s+', ' ', s.replace('`', '')).strip()
code = {'business-requirements.md': 'BRD', 'product-requirements.md': 'PRD', 'experiments.md': 'EXP',
        'backlog.md': 'BL', 'traceability.md': 'TR', 'azure-r1.md': 'AZ1', 'azure-r2.md': 'AZ2', 'azure-r3.md': 'AZ3',
        'dotnet-r1.md': 'DN1', 'dotnet-r2.md': 'DN2', 'dotnet-r3.md': 'DN3', 'dotnet-r4.md': 'DN4'}
occ = defaultdict(set)     # ID -> set of codes where it occurs in a table row or body
wording = defaultdict(list)
for f, t in DOCS.items():
    if f == 'README.md':
        continue
    base = f.replace('releases/', '')
    for l in t.splitlines():
        m = re.match(r'^\| (A-\d{2}|OPEN-\d{2}) \|(.*)$', l)
        if m:
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            wording[m.group(1)].append((base, c[1]))
    for x in set(re.findall(r'\b(A-\d{2}|OPEN-\d{2})\b', t)):
        occ[x].add(code[base])
for k, lst in wording.items():
    ref = A_def.get(k, O_def.get(k, {})).get('text')
    if ref is None:
        bad('wording', '%s used in tables but not defined in README' % k); continue
    for base, txt in lst:
        if norm(txt) != norm(ref):
            bad('wording', '%s differs in %s: "%s" vs README "%s"' % (k, base, norm(txt)[:120], norm(ref)[:120]))
# used-in codes in README vs actual occurrence
for k in sorted(list(A_def) + list(O_def)):
    if k in A_def:
        declared = set(x.strip() for x in A_def[k]['used'].split(','))
    else:
        declared = set(x.strip() for x in (O_def[k]['rels'] + ',' + O_def[k]['other']).split(','))
    actual = occ.get(k, set())
    if not actual:
        bad('unused', '%s not used in any file' % k)
    dec_nonrel = {d for d in declared if d}
    if dec_nonrel != actual:
        if k in O_def:
            # releases column only lists releases; compare with the release and other-doc codes
            pass
        bad('used-in', '%s README-declared=%s actual=%s' % (k, sorted(dec_nonrel), sorted(actual)))
# plan 5.3 release OPEN lists
plan_rel_open = {'AZ1': ['OPEN-03', 'OPEN-04', 'OPEN-05', 'OPEN-13', 'OPEN-19', 'OPEN-21'],
                 'AZ2': ['OPEN-01', 'OPEN-03', 'OPEN-04', 'OPEN-05', 'OPEN-06', 'OPEN-18', 'OPEN-19', 'OPEN-20', 'OPEN-22', 'OPEN-23'],
                 'AZ3': ['OPEN-04', 'OPEN-12'],
                 'DN1': ['OPEN-03', 'OPEN-04', 'OPEN-19', 'OPEN-21', 'OPEN-23'],
                 'DN2': ['OPEN-01', 'OPEN-03', 'OPEN-04', 'OPEN-05', 'OPEN-13', 'OPEN-19', 'OPEN-20', 'OPEN-22'],
                 'DN3': ['OPEN-06', 'OPEN-19'],
                 'DN4': ['OPEN-18', 'OPEN-20']}
rel_by_code = {v: k for k, v in code.items() if k.startswith(('azure', 'dotnet'))}
for cd, lst in plan_rel_open.items():
    f = rel_by_code[cd]
    t = DOCS['releases/' + f]
    for o in lst:
        if o not in t:
            bad('plan-5.3-open', '%s does not state %s' % (f, o))

# ---------- 15. Git and boundary (informational) ----------

print()
print('=== PROBLEMS BY CHECK ===')
for k in sorted(problems):
    print('## %s : %d' % (k, len(problems[k])))
    for m in problems[k][:120]:
        print('   -', m)
