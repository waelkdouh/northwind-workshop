import re
from collections import defaultdict
from pathlib import Path
P = Path("/Users/waelkdouh/Demos/northwind-workshop/docs/product")
bl = (P/"backlog.md").read_text(encoding="utf-8")
tr = (P/"traceability.md").read_text(encoding="utf-8")
blocks = re.split(r"^#{3,6} ", bl, flags=re.M)
backlog_cover = defaultdict(set)
for b in blocks:
    head = b.split("\n",1)[0]
    mm = re.match(r"((?:STORY|EA|EN|EP)-\d+)", head)
    if not mm: continue
    m = re.search(r"\*\*Covers:\*\*\s*([^·\n]+)", b)
    if m:
        for idc in re.findall(r"(BR-\d+|NFR-\d+)", m.group(1)):
            backlog_cover[idc].add(mm.group(1))
trace_cover = defaultdict(set)
for ln in tr.splitlines():
    if not ln.startswith("|"): continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    m = re.match(r"^(BR-\d+|NFR-\d+)\b", c[0]) if c else None
    if m and len(c) >= 5:
        colidx = 3 if m.group(1).startswith("NFR") else 4
        for s in re.findall(r"STORY-\d+", c[colidx]):
            trace_cover[m.group(1)].add(s)
diff = []
for k in sorted(set(backlog_cover)|set(trace_cover), key=lambda s:(s.split('-')[0], int(s.split('-')[1]))):
    a, b = backlog_cover.get(k,set()), trace_cover.get(k,set())
    if a != b:
        diff.append((k, sorted(a), sorted(b)))
print("ids where backlog 'Covers:' differs from traceability covering stories:", len(diff))
for d in diff: print("  ", d)
print("backlog covers map size:", len(backlog_cover), "traceability covers map size:", len(trace_cover))
# Release files section 4 covered ids vs C1 column
rel = {p.stem: p.read_text(encoding="utf-8") for p in (P/"releases").glob("*.md")}
for k, t in sorted(rel.items()):
    m = re.search(r"^## 4\. .*?$(.*?)^## 5\.", t, re.M|re.S)
    body = m.group(1) if m else "NO SECTION 4"
    ids = sorted(set(re.findall(r"\b(?:BR|NFR)-\d+\b", body)))
    print(f"{k}: section-4 ids = {ids}")
# PRD FR text containing assumption/open markers in requirement column
prd = (P/"product-requirements.md").read_text(encoding="utf-8")
for ln in prd.splitlines():
    if ln.startswith("| FR-"):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if re.search(r"ASSUMPTION|\bA-\d+\b|\bOPEN\b", c[1]):
            print("FR text carries assumption/open marker:", c[0], "::", c[1][:160])
# Backlog story text containing ASSUMPTION or OPEN inside the 'Story:' line
for b in blocks:
    head = b.split("\n",1)[0]
    mm = re.match(r"((?:STORY|EA|EN|EP)-\d+)", head)
    if not mm: continue
    s = re.search(r"\*\*Story:\*\*\s*(.*)", b)
    if s and re.search(r"ASSUMPTION", s.group(1)):
        print("story line has ASSUMPTION:", mm.group(1), s.group(1)[:160])
# contact data / secrets
for f in [P/"business-requirements.md", P/"product-requirements.md", P/"experiments.md", P/"backlog.md", P/"traceability.md"] + list((P/"releases").glob("*.md")):
    t = f.read_text(encoding="utf-8")
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", t)
    phones = re.findall(r"\+\d{2}[ \d]{8,}", t)
    secrets = re.findall(r"(?i)(password\s*[:=]\s*\S+|pwd=|Server=tcp:|AccountKey=|sk-[A-Za-z0-9]{10,})", t)
    if emails or phones or secrets:
        print("CONTACT/SECRET pattern in", f.name, emails[:3], phones[:3], secrets[:3])
print("contact/secret scan complete")
