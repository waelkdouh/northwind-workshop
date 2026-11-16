import re
from pathlib import Path
from collections import defaultdict
P = Path("/Users/waelkdouh/Demos/northwind-workshop/docs/product")
K = Path("/Users/waelkdouh/Demos/northwind-workshop/knowledge-docs")
bl = (P/"backlog.md").read_text(encoding="utf-8")
blocks = re.split(r"^#{3,6} ", bl, flags=re.M)
info = {}
for b in blocks:
    head = b.split("\n",1)[0]
    mm = re.match(r"((?:EPIC|FEAT|STORY|EA|EN|EP)-\d+)", head)
    if not mm: continue
    t = re.search(r"\*\*Tags:\*\*\s*(.*)", b); p = re.search(r"\*\*Parent:\*\*\s*((?:EPIC|FEAT)-\d+)", b)
    tags = re.findall(r"`([^`]+)`", t.group(1)) if t else []
    info[mm.group(1)] = {"tags": tags, "parent": p.group(1) if p else None}
# child release tag must equal parent release tag; child track must equal parent track
bad = []
children = defaultdict(list)
for k,v in info.items():
    if v["parent"]: children[v["parent"]].append(k)
for par, kids in children.items():
    if par not in info: bad.append(("missing parent", par)); continue
    ptags = set(info[par]["tags"])
    for kid in kids:
        if set(info[kid]["tags"]) != ptags and not (info[kid]["tags"] and set(info[kid]["tags"]).issubset(ptags) is False and False):
            # allow child unplanned (track only) if parent also unplanned
            if set(info[kid]["tags"]) != ptags:
                bad.append((par, sorted(ptags), kid, info[kid]["tags"]))
print("epic/feature vs child tag mismatches:", bad[:10], len(bad))
# SM and P verbatim
bc = (K/"business-case.md").read_text(encoding="utf-8")
brd = (P/"business-requirements.md").read_text(encoding="utf-8")
def rows(text):
    out={}
    for ln in text.splitlines():
        if ln.startswith("|"):
            c=[re.sub(r"[`*]","",x).strip() for x in ln.strip().strip("|").split("|")]
            if c and re.match(r"^(SM|P|C)-\d\d$", c[0]): out.setdefault(c[0], c)
    return out
s, b = rows(bc), rows(brd)
for k in sorted(s):
    if k not in b: print("not in BRD:", k); continue
    src_t = [x for x in s[k][1:]]; brd_t = [x for x in b[k][1:]]
    if k.startswith("SM"):
        # business case: measure | baseline | target ; BRD: measure | baseline | target | BG | BA | note
        if src_t[:3] != brd_t[:3]:
            print("SM DIFF", k, src_t[:3], brd_t[:3])
    elif k.startswith("P-"):
        if src_t[0] != brd_t[0]: print("P DIFF", k, src_t[0][:120], "|", brd_t[0][:120])
print("SM/P verbatim check done")
# BRD register intros
for head in ["## 12. ASSUMPTION register", "## 13. OPEN register"]:
    i = brd.find(head); print(brd[i:i+420].replace("\n"," / ")[:420]); print("--")
# release-local ids: owners
for f in sorted((P/"releases").glob("*.md")):
    for ln in f.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| (A-D\d-\d+|O-D\d-\d+|AZ\d-O\d+) ", ln):
            print(f.name, ln[:90], "... owner cell:", ln.strip().strip("|").split("|")[-1].strip()[:60])
