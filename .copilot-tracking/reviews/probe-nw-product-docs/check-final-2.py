# Second read-only probe for docs/product (final state): cross-document consistency.
# Writes nothing. Prints to stdout only.
import os
import re
from collections import defaultdict

ROOT = r'C:\demos\northwind-workshop\docs\product'

def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()

RELS = ['azure-r1', 'azure-r2', 'azure-r3', 'dotnet-r1', 'dotnet-r2', 'dotnet-r3', 'dotnet-r4']
ID_RX = r'(?:EP|FT|EN|US)-(?:AZ|DN)-\d{2,3}'
SRC_RX = r'\b(?:BR|NFR|C|CS|ES|SM|P|OQ)-\d{2,3}\b'
B = rd('backlog.md'); BL = B.splitlines()
RM = rd('README.md')
PRD = rd('product-requirements.md')

def section(lines, prefix):
    # collect body lines of the heading that starts with prefix, until the next heading of any level
    out = []; on = False
    for l in lines:
        if l.startswith('#'):
            if on:
                break
            on = l.startswith(prefix)
            continue
        if on:
            out.append(l)
    return out

# ---------- register and item sources (independent light parse) ----------
i11 = next(i for i, l in enumerate(BL) if l.startswith('## 11.'))
reg = {}
for l in BL[i11:]:
    if re.match(r'^\| `' + ID_RX + r'` \|', l):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        reg[c[0].strip('`')] = dict(type=c[1], track=c[4].strip('`'), rel=c[5].strip('`'), src=set(re.findall(SRC_RX, c[7])))

# ---------- 1. strict Given / When / Then order ----------
hdr = re.compile(r'^(#{2,6}) (' + ID_RX + r')\b')
heads = [i for i, l in enumerate(BL[:i11]) if l.startswith('#')]
bad_gwt = []; ncrit = 0; bodies = {}
for k, h in enumerate(heads):
    m = hdr.match(BL[h])
    if not m:
        continue
    end = heads[k + 1] if k + 1 < len(heads) else i11
    body = BL[h + 1:end]
    bodies[m.group(2)] = body
    for l in body:
        mm = re.match(r'^\d+\. (.*)$', l)
        if mm:
            ncrit += 1
            c = mm.group(1)
            if not re.match(r'^Given .+?, When .+?, Then .+$', c):
                bad_gwt.append((m.group(2), c[:110]))
print('STRICT GWT: criteria=%d not in "Given ..., When ..., Then ..." order=%d' % (ncrit, len(bad_gwt)))
for x in bad_gwt:
    print('   ', x)

# ---------- 2. owner and track columns: README master vs backlog sections 9 and 10 ----------
def rows_of(text, idrx):
    out = {}
    for l in text.splitlines():
        m = re.match(r'^\| (' + idrx + r') \|(.*)$', l)
        if m:
            cells = [x.strip() for x in l.strip().strip('|').split('|')]
            out.setdefault(cells[0], cells)
    return out
bl_A = rows_of(B, r'A-\d{2}')
bl_O = rows_of(B, r'OPEN-\d{2}')
rm_A = rows_of(RM, r'A-\d{2}')
rm_O = rows_of(RM, r'OPEN-\d{2}')
own_diff = []
for k, c in bl_A.items():
    if k in rm_A and c[2] != rm_A[k][2]:
        own_diff.append(('A', k, 'backlog=' + c[2], 'README=' + rm_A[k][2]))
for k, c in bl_O.items():
    if k in rm_O and c[2] != rm_O[k][2]:
        own_diff.append(('OPEN', k, 'backlog=' + c[2], 'README=' + rm_O[k][2]))
print('OWNER diffs (backlog vs README):', len(own_diff))
for x in own_diff:
    print('   ', x)
# owner columns in other files
for f in ['business-requirements.md', 'product-requirements.md', 'experiments.md', 'traceability.md'] + ['releases/%s.md' % r for r in RELS]:
    t = rd(f)
    for k, cells in rows_of(t, r'A-\d{2}').items():
        if k in rm_A and len(cells) >= 3 and cells[2] != rm_A[k][2]:
            print('   OWNER-A %s in %s: %s vs README %s' % (k, f, cells[2], rm_A[k][2]))
    for k, cells in rows_of(t, r'OPEN-\d{2}').items():
        if k in rm_O and len(cells) >= 3 and cells[2] != rm_O[k][2]:
            print('   OWNER-OPEN %s in %s: %s vs README %s' % (k, f, cells[2], rm_O[k][2]))

# ---------- 3. Release section 7.1 table vs backlog rank table ----------
rank = {'track-azure': [], 'track-dotnet': []}
i41 = BL.index('### 4.1 `track-azure`'); i42 = BL.index('### 4.2 `track-dotnet`'); i5 = next(i for i, l in enumerate(BL) if l.startswith('## 5.'))
for l in BL[i41:i42]:
    if re.match(r'^\| \d+ \|', l):
        rank['track-azure'].append([x.strip() for x in l.strip().strip('|').split('|')])
for l in BL[i42:i5]:
    if re.match(r'^\| (\d+|-) \|', l):
        rank['track-dotnet'].append([x.strip() for x in l.strip().strip('|').split('|')])
for r in RELS:
    t = rd('releases/%s.md' % r).splitlines()
    sec = section(t, '### 7.1')
    rows = []
    for l in sec:
        if re.match(r'^\| \d+ \|', l):
            rows.append([x.strip() for x in l.strip().strip('|').split('|')])
    track = 'track-azure' if r.startswith('azure') else 'track-dotnet'
    exp = [c for c in rank[track] if c[4].strip('`') == r]
    exp_ids = [(c[0], c[1].strip('`'), set() if c[7].strip().lower() == 'none' else set(re.findall(ID_RX, c[7]))) for c in exp]
    got_ids = [(c[0], c[1].strip('`'), set(re.findall(ID_RX, c[3]))) for c in rows]
    flag = 'OK' if [(a, b) for a, b, _ in exp_ids] == [(a, b) for a, b, _ in got_ids] else 'MISMATCH'
    dflag = 'OK' if [x[2] for x in exp_ids] == [x[2] for x in got_ids] else 'DEP-MISMATCH'
    print('REL-7.1 %-10s rows=%d expected=%d order %s deps %s' % (r, len(rows), len(exp_ids), flag, dflag))
    if flag != 'OK':
        print('    release:', [(a, b) for a, b, _ in got_ids][:30])
        print('    backlog:', [(a, b) for a, b, _ in exp_ids][:30])
    if dflag != 'OK':
        for x, y in zip(exp_ids, got_ids):
            if x[2] != y[2]:
                print('    dep diff', y[1], 'release=', sorted(y[2]), 'backlog=', sorted(x[2]))

# ---------- 4. PRD section 8 (release subsections) vs register ----------
prd_lines = PRD.splitlines()
for r in RELS:
    name = r
    sub = []; on = False
    for l in prd_lines:
        if l.startswith('### 8.'):
            on = name in l
            continue
        if l.startswith('## ') or (l.startswith('### ') and not l.startswith('### 8.')):
            on = False
        if on:
            sub.append(l)
    ids = set(re.findall(ID_RX, '\n'.join(sub)))
    planned = {k for k, v in reg.items() if v['rel'] == r and v['type'] in ('Epic', 'Feature', 'Enabler')}
    us = {x for x in ids if x.startswith('US-')}
    print('PRD-8 %-10s IDs=%d planned(EP/FT/EN)=%d missing=%s extra=%s US-named=%s' % (
        r, len(ids), len(planned), sorted(planned - ids), sorted(x for x in ids if x not in planned), sorted(us)))

# ---------- 8. Traceability sections 3.1 and 3.2 vs register ----------
TR_all = rd('traceability.md').splitlines()
j1 = next(i for i, l in enumerate(TR_all) if l.startswith('### 3.1'))
j3 = next(i for i, l in enumerate(TR_all) if l.startswith('### 3.3'))
TR = TR_all[j1:j3]
trace_rows = {}
for l in TR:
    m = re.match(r'^\| `((?:BR|NFR)-\d{2})` \|', l)
    if m:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) >= 9:
            trace_rows.setdefault(m.group(1), []).append(c)
tr_problems = []
for req, rows in sorted(trace_rows.items()):
    cited = {k for k, v in reg.items() if req in v['src']}
    for c in rows:
        table_ids = {}
        for seg in c[5].split(';') + c[6].split(';'):
            m = re.search(r'\((`?[a-z0-9-]+`?|unplanned)[,)]', seg)
            rel = m.group(1).strip('`') if m else '?'
            for x in re.findall(ID_RX, seg):
                table_ids[x] = rel
        # compare: IDs in table vs register items citing this requirement and in the same track
        track_rows = c[3].strip('`')
        expected = {k for k in cited if reg[k]['track'] == track_rows and reg[k]['type'] in ('Story', 'Enabler')}
        if set(table_ids) != expected:
            tr_problems.append('%s (%s): table-only=%s register-only=%s' % (
                req, track_rows, sorted(set(table_ids) - expected), sorted(expected - set(table_ids))))
        for k, rel in table_ids.items():
            if k in reg:
                want = reg[k]['rel'] if reg[k]['rel'] != '-' else 'unplanned'
                if rel != want:
                    tr_problems.append('%s lists %s as %s, register says %s' % (req, k, rel, want))
print('TRACEABILITY 3.1/3.2 rows=%d problems=%d' % (sum(len(v) for v in trace_rows.values()), len(tr_problems)))
for p in tr_problems:
    print('   ', p)

for rid in ['US-DN-016', 'US-DN-006', 'US-DN-008', 'US-DN-011', 'US-DN-012', 'US-DN-031', 'US-DN-030', 'US-DN-036', 'US-DN-037', 'FT-DN-25', 'EP-DN-08']:
    if rid in reg:
        print('SRC %-10s %s' % (rid, sorted(reg[rid]['src'])))

# ---------- 6. Positive uses of forbidden cross-track wording ----------
pat = re.compile(r'\b(requires|require|blocked by|waits for|wait for|after the)\b', re.I)
neg = re.compile(r"\b(not|never|no|nothing|none|without|does not|do not|must not|forbid|forbidden)\b", re.I)
files = ['backlog.md', 'product-requirements.md', 'business-requirements.md', 'experiments.md', 'traceability.md', 'README.md'] + ['releases/%s.md' % r for r in RELS]
hits = []
for f in files:
    for n, l in enumerate(rd(f).splitlines(), 1):
        if pat.search(l) and not neg.search(l):
            hits.append((f, n, l.strip()[:200]))
print('FORBIDDEN-WORDING positive hits (no negation on line): %d' % len(hits))
for h in hits[:40]:
    print('   %s:%d %s' % h)

# ---------- 7. Release files status line ----------
for r in RELS:
    t = rd('releases/%s.md' % r)
    print('STATUS-REL %-10s %s' % (r, 'Draft' in t and 'awaiting product owner approval' in t and 'not yet tagged' in t))
print('PRD status phrase count:', PRD.count('Draft — awaiting product owner approval; not yet tagged'))
print('Proposed-as-status occurrences:', len(re.findall(r'Status\W.{0,20}Proposed', B + RM + PRD + ''.join(rd('releases/%s.md' % r) for r in RELS))))
