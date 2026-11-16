import re
from collections import Counter
from pathlib import Path
P = Path("/Users/waelkdouh/Demos/northwind-workshop/docs/product")
prd = (P/"product-requirements.md").read_text(encoding="utf-8")
bl = (P/"backlog.md").read_text(encoding="utf-8")
brd = (P/"business-requirements.md").read_text(encoding="utf-8")
def sec(text, start, end):
    out=[]; on=False
    for ln in text.splitlines():
        if re.match(start, ln): on=True; continue
        if on and re.match(end, ln): break
        if on: out.append(ln)
    return out
def cells(l): return [re.sub(r"[`*]","",x).strip() for x in l.strip().strip("|").split("|")]
# ---- FR rows in PRD section 7
fr_rows = {}
for ln in sec(prd, r"^## 7\. Functional", r"^## 8\. "):
    if ln.startswith("| FR-"):
        c = cells(ln); fr_rows.setdefault(c[0], []).append(c)
print("PRD FR ids:", len(fr_rows), "dupes:", [k for k,v in fr_rows.items() if len(v)>1])
print("PRD FR ids (sorted):", sorted(fr_rows)[:3], "...", sorted(fr_rows)[-3:])
print("FR per block:", Counter(k[:4] for k in fr_rows))
# ---- backlog Implements/Serves
impl = {}
for ln in bl.splitlines():
    m = re.search(r"\*\*(Implements|Serves):\*\*\s*([^·\n]+)", ln)
    if m:
        cur_item = None
    # item detail headings
for m in re.finditer(r"^#{3,6} ((?:STORY|EA|EN|EP)-\d+) .*?$", bl, re.M):
    pass
blocks = re.split(r"^#{3,6} ", bl, flags=re.M)
for b in blocks:
    head = b.split("\n",1)[0]
    mm = re.match(r"((?:EPIC|FEAT|STORY|EA|EN|EP)-\d+)", head)
    if not mm: continue
    iid = mm.group(1)
    m = re.search(r"\*\*(Implements|Serves):\*\*\s*([^·\n]+)", b)
    if m:
        impl[iid] = re.findall(r"FR-\d+", m.group(2))
frs_by_backlog = Counter(f for v in impl.values() for f in v)
print("backlog items citing an FR:", len(impl), "| distinct FR cited:", len(frs_by_backlog))
no_story = sorted(set(fr_rows) - set(frs_by_backlog))
print("PRD FRs with NO backlog item:", no_story)
unknown = sorted(set(frs_by_backlog) - set(fr_rows))
print("backlog cites FR not in PRD §7:", unknown)
multi = {k:v for k,v in frs_by_backlog.items() if v>1}
print("FR cited by >1 backlog item:", multi)
# PRD FR priority/release vs backlog register
reg = {}
for ln in sec(bl, r"^## 2\. Item register", r"^## 3\. "):
    if ln.startswith("|"):
        c = cells(ln)
        if len(c)>=7 and re.match(r"^(EPIC|FEAT|STORY|EA|EN|EP)-\d+$", c[0]): reg[c[0]] = c
# Compare FR priority to any implementing backlog item's priority
mism=[]
for iid, frs in impl.items():
    if iid not in reg: continue
    for f in frs:
        if f in fr_rows:
            pr_prd = fr_rows[f][0][3] if len(fr_rows[f][0])>3 else "?"
            pr_bl = reg[iid][5]
            if pr_prd.split(" ")[0] != pr_bl.split(" ")[0]:
                mism.append((f, pr_prd, iid, pr_bl))
print("FR vs backlog priority mismatches:", mism[:20], len(mism))
print("sample FR row:", list(fr_rows.values())[0][0][:8])
# ---- C1 table restricted
def c1(text, start, end):
    return [re.sub(r"\s+"," ",l.strip()) for l in sec(text, start, end) if re.match(r"^\| (Azure|\.NET|Power Platform)", l.strip())]
a = c1(brd, r"^### 10\.2", r"^### 10\.3"); b = c1(prd, r"^### 6\.2", r"^### 6\.3"); c = c1(bl, r"^### 1\.1", r"^### 1\.2")
print("C1 rows BRD/PRD/BACKLOG:", len(a), len(b), len(c))
norm = lambda rows: [re.sub(r"[`*]","",r).replace("(track-azure)","").replace(" ","") for r in rows]
print("BRD == PRD (C1 rows, ignoring backticks):", norm(a)==norm(b))
print("BACKLOG == PRD (C1 rows, ignoring backticks):", norm(c)==norm(b))
for x,y,lab in [(a,b,"BRD"),(c,b,"BACKLOG")]:
    for r1,r2 in zip(x,y):
        if re.sub(r"[`*]","",r1)!=re.sub(r"[`*]","",r2):
            print(f"  {lab} differs:\n    {lab}: {r1[:300]}\n    PRD: {r2[:300]}")
