import os, re
ROOT = r'C:\demos\northwind-workshop\docs\product'
files = ['backlog.md','traceability.md','README.md','product-requirements.md','business-requirements.md','experiments.md'] + ['releases/%s.md' % r for r in ['azure-r1','azure-r2','azure-r3','dotnet-r1','dotnet-r2','dotnet-r3','dotnet-r4']]
OOS = re.compile(r'\b(BR-1[4-9]|NFR-09|C-07|C-08|SM-05|SM-06|OQ-04|OQ-05|CS-2[4-8]|ES-3[2-7])\b')
ctx = re.compile(r'out of scope|out-of-scope|Out of scope|informational|Informational|Constraints|Success measures|Open questions|Current-state facts|Standards for Power Platform|BA-03|belong to|are out of|section 6|Not in scope|no release', re.I)
n_all = 0; rem = []
for f in files:
    lines = open(os.path.join(ROOT, f), encoding='utf-8').read().splitlines()
    for i, l in enumerate(lines, 1):
        if OOS.search(l):
            n_all += 1
            if not ctx.search(l):
                rem.append((f, i, l.strip()[:220]))
print('OOS mentions total=%d ; lines without out-of-scope context=%d' % (n_all, len(rem)))
for x in rem:
    print('  %s:%d %s' % x)
mves = set()
for f in files:
    mves |= set(re.findall(r'MVE-[A-Z0-9]+', open(os.path.join(ROOT, f), encoding='utf-8').read()))
print('MVE identifiers used:', sorted(mves))
