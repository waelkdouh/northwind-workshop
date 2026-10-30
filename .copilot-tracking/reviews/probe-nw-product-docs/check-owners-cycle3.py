# Read-only owner comparison for OPEN- rows, review 3. Writes nothing. Output to stdout only.
import os
import re

ROOT = r'C:\demos\northwind-workshop\docs\product'
FILES = ['business-requirements.md', 'product-requirements.md', 'experiments.md', 'backlog.md',
         'traceability.md', 'releases/azure-r1.md', 'releases/azure-r2.md', 'releases/azure-r3.md',
         'releases/dotnet-r1.md', 'releases/dotnet-r2.md', 'releases/dotnet-r3.md', 'releases/dotnet-r4.md']
PEOPLE = ['Ahmed Benali', 'Lena Varga', 'Marc Dubois', 'Julien Moreau', 'Sofie Peeters', 'Pieter Janssens']

def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()

def people(s):
    return frozenset(p for p in PEOPLE if p in s)

ref = {}
for l in rd('README.md').splitlines():
    m = re.match(r'^\| (OPEN-\d{2}) \|', l)
    if m:
        ref[m.group(1)] = (people(l), l)

checked = 0
mism = 0
for f in FILES:
    for n, l in enumerate(rd(f).splitlines(), 1):
        m = re.match(r'^\| (OPEN-\d{2}) \|', l)
        if not m:
            continue
        k = m.group(1)
        if k not in ref:
            print('UNDEFINED', k, f, n); mism += 1; continue
        ppl = people(l)
        # only compare rows that carry a person (owner) column
        if not ppl:
            continue
        checked += 1
        if ppl != ref[k][0]:
            mism += 1
            print('OWNER MISMATCH %s %s:%d file=%s readme=%s' % (k, f, n, sorted(ppl), sorted(ref[k][0])))
print('OWNER rows with person names checked=%d mismatches=%d' % (checked, mism))
