# Read-only regression probe for docs/product, review 3 (final state after remediation cycle 2).
# Writes nothing. Prints findings to stdout only. Scratch file inside the authorised probe directory.
import os
import re
from collections import defaultdict

ROOT = r'C:\demos\northwind-workshop\docs\product'
FILES = ['README.md', 'backlog.md', 'traceability.md', 'product-requirements.md',
         'business-requirements.md', 'experiments.md',
         'releases/azure-r1.md', 'releases/azure-r2.md', 'releases/azure-r3.md',
         'releases/dotnet-r1.md', 'releases/dotnet-r2.md', 'releases/dotnet-r3.md', 'releases/dotnet-r4.md']

def raw(rel):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        return f.read()

# ---------- A. Encoding and mojibake ----------
print('== A. ENCODING')
texts = {}
for f in FILES:
    b = raw(f)
    crlf = b.count(b'\r\n')
    try:
        t = b.decode('utf-8')
    except UnicodeDecodeError as e:
        print('  DECODE FAIL', f, e)
        continue
    texts[f] = t
    moj = [m for m in ['\ufffd', '\u00e2\u20ac', '\u00c3', '\u00c2'] if m in t]
    print('  %-30s bytes=%-7d lines=%-5d CRLF=%-5d emdash=%-4d mojibake=%s' % (
        f, len(b), t.count('\n'), crlf, t.count('\u2014'), moj or 'none'))

# ---------- B. Table column integrity ----------
print('== B. TABLE COLUMN COUNTS')
def cells(line):
    s = line.strip().replace('\\|', '\x00')
    return len(s.strip('|').split('|'))

bad_tables = 0
tables_total = 0
for f, t in texts.items():
    lines = t.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith('|'):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith('|'):
                j += 1
            block = lines[i:j]
            tables_total += 1
            hdr_n = cells(block[0])
            sep = block[1] if len(block) > 1 else ''
            if not re.match(r'^\s*\|?\s*:?-{2,}', sep):
                print('  NO SEPARATOR %s:%d' % (f, i + 1))
                bad_tables += 1
            else:
                for k, row in enumerate(block[2:], start=i + 3):
                    if cells(row) != hdr_n:
                        print('  COLCOUNT %s:%d header=%d row=%d | %s' % (f, k, hdr_n, cells(row), row.strip()[:140]))
                        bad_tables += 1
            i = j
        else:
            i += 1
print('  tables=%d, column/separator problems=%d' % (tables_total, bad_tables))

# ---------- C. Links and anchors ----------
print('== C. LINKS AND ANCHORS')
def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[`*_]', '', h)
    h = re.sub(r'[^\w\- ]', '', h, flags=re.UNICODE)
    return h.replace(' ', '-')
anchors = {}
for f, t in texts.items():
    anchors[f] = set()
    seen = defaultdict(int)
    for l in t.splitlines():
        m = re.match(r'^#{1,6}\s+(.*)$', l)
        if m:
            s = slug(m.group(1))
            n = seen[s]
            anchors[f].add(s if n == 0 else '%s-%d' % (s, n))
            seen[s] += 1
link_rx = re.compile(r'\]\(([^)\s]+)\)')
links = 0
link_bad = 0
for f, t in texts.items():
    base = os.path.dirname(os.path.join(ROOT, f))
    for n, l in enumerate(t.splitlines(), 1):
        for m in link_rx.finditer(l):
            tgt = m.group(1)
            links += 1
            if tgt.startswith(('http://', 'https://', 'mailto:')):
                continue
            path, _, anc = tgt.partition('#')
            if path == '':
                tf = f
            else:
                full = os.path.normpath(os.path.join(base, path))
                if not os.path.exists(full):
                    print('  MISSING FILE %s:%d -> %s' % (f, n, tgt)); link_bad += 1
                    continue
                tf = os.path.relpath(full, ROOT).replace('\\', '/')
            if anc and tf in anchors and anc not in anchors[tf]:
                print('  MISSING ANCHOR %s:%d -> %s' % (f, n, tgt)); link_bad += 1
print('  links=%d problems=%d' % (links, link_bad))

# ---------- D. Independent A- and OPEN- wording comparison against README ----------
print('== D. A-/OPEN- WORDING vs README')
def row_map(t):
    out = {}
    for l in t.splitlines():
        m = re.match(r'^\|\s*((?:A|OPEN)-\d{2})\s*\|', l)
        if m:
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            out.setdefault(c[0], []).append(c[1])
    return out
def norm(s):
    return re.sub(r'\s+', ' ', s.replace('`', '')).strip()
ref = row_map(texts['README.md'])
print('  README IDs: A/OPEN =', sum(1 for k in ref if k.startswith('A-')), '/', sum(1 for k in ref if k.startswith('OPEN-')))
cmp_rows = 0
diffs = 0
per_file = {}
for f, t in texts.items():
    if f == 'README.md':
        continue
    rm = row_map(t)
    cnt = 0
    for k, vals in rm.items():
        if k not in ref:
            print('  UNDEFINED %s in %s' % (k, f)); diffs += 1; continue
        for v in vals:
            cnt += 1
            cmp_rows += 1
            if norm(v) != norm(ref[k][0]):
                diffs += 1
                print('  DIFF %s in %s: "%s" != README "%s"' % (k, f, norm(v)[:90], norm(ref[k][0])[:90]))
    per_file[f] = cnt
print('  compared rows=%d differences=%d' % (cmp_rows, diffs))
print('  rows per file:', per_file)
# README section 7 claim
m7 = re.search(r'identical in every (document|file)[^\n]*', texts['README.md'])
print('  README claim sentence:', m7.group(0)[:200] if m7 else 'not found')

# ---------- E. Cross-track wording in context ----------
print('== E. CROSS-TRACK WORDING (context)')
pat = re.compile(r'\b(requires?|blocked by|waits? for|after)\b', re.I)
neg = re.compile(r"\b(not|never|no|nothing|none|without|does not|do not|must not)\b", re.I)
hits = 0
for f, t in texts.items():
    for n, l in enumerate(t.splitlines(), 1):
        if pat.search(l) and not neg.search(l) and not l.lstrip().startswith('|') is False:
            pass
        if pat.search(l) and not neg.search(l):
            hits += 1
            mm = pat.search(l)
            s = max(0, mm.start() - 70)
            print('  %s:%d ...%s...' % (f, n, l[s:mm.end() + 60].strip()))
print('  positive hits=%d' % hits)

# ---------- F. Status, claims and boundary wording ----------
print('== F. STATUS AND CLAIM WORDING')
claim = re.compile(r'\b(has been implemented|is implemented|was deployed|has been deployed|is deployed|now live|went live|has been tagged|tag created|was tagged)\b', re.I)
for f, t in texts.items():
    for n, l in enumerate(t.splitlines(), 1):
        if claim.search(l):
            print('  CLAIM? %s:%d %s' % (f, n, l.strip()[:160]))
status_items = defaultdict(int)
for f, t in texts.items():
    for l in t.splitlines():
        m = re.search(r'Status: (\w+)', l)
        if m:
            status_items[m.group(1)] += 1
print('  item Status values:', dict(status_items))
print('== DONE')
