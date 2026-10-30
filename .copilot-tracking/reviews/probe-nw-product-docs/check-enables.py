import os
import re

ROOT = r'C:\demos\northwind-workshop\docs\product'
RELIDX = {'azure-r1': 1, 'azure-r2': 2, 'azure-r3': 3, 'dotnet-r1': 1, 'dotnet-r2': 2, 'dotnet-r3': 3, 'dotnet-r4': 4}
ID_RX = r'(?:EP|FT|EN|US)-(?:AZ|DN)-\d{2,3}'

def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()

BL = rd('backlog.md').splitlines()
i11 = next(i for i, l in enumerate(BL) if l.startswith('## 11.'))
reg = {}
for l in BL[i11:]:
    if re.match(r'^\| `' + ID_RX + r'` \|', l):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        reg[c[0].strip('`')] = dict(type=c[1], parent=c[2].strip('`'), track=c[4].strip('`'), rel=c[5].strip('`'))

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

heads = [i for i, l in enumerate(BL[:i11]) if l.startswith('#')]
hdr = re.compile(r'^(#{2,6}) (' + ID_RX + r')\b')
problems = []
n_enables = 0
for k, h in enumerate(heads):
    m = hdr.match(BL[h])
    if not m:
        continue
    rid = m.group(2)
    end = heads[k + 1] if k + 1 < len(heads) else i11
    body = '\n'.join(BL[h + 1:end])
    em = re.search(r'^\* Enables: (.+)$', body, re.M)
    if not em:
        continue
    targets = expand(em.group(1))
    for t in sorted(targets):
        n_enables += 1
        if t not in reg:
            problems.append('%s enables unknown %s' % (rid, t)); continue
        a, b = reg[rid], reg[t]
        if a['rel'] == '-' or b['rel'] == '-':
            continue
        if RELIDX[a['rel']] > RELIDX[b['rel']]:
            problems.append('%s (%s) enables %s (%s): enabler is in a LATER release' % (rid, a['rel'], t, b['rel']))
        if a['track'] != b['track']:
            problems.append('%s enables other-track %s' % (rid, t))
print('ENABLES targets checked=%d problems=%d' % (n_enables, len(problems)))
for p in problems:
    print('   ', p)

n6 = rd('backlog.md')
us19 = re.search(r'^\* \(source: (.+)\)$', n6[n6.find('##### US-DN-019'):], re.M)
print('US-DN-019 source line:', us19.group(1) if us19 else None)
print('NFR-06 mentions in azure-r1 release file:', rd('releases/azure-r1.md').count('NFR-06'))
for n, l in enumerate(rd('releases/azure-r1.md').splitlines(), 1):
    if 'NFR-06' in l:
        print('   azure-r1:%d %s' % (n, l.strip()[:200]))
