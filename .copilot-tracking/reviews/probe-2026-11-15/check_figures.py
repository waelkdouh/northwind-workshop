import re
from pathlib import Path
R = Path("/Users/waelkdouh/Demos/northwind-workshop")
src_files = [R/"knowledge-docs"/f for f in ["business-case.md","current-state.md","engineering-standards.md"]]
src_files += [R/".copilot-tracking/research/2026-11-15/northwind-product-documents-research.md",
              R/".copilot-tracking/plans/2026-11-15/northwind-product-documents-plan.md",
              R/".copilot-tracking/reviews/2026-11-15-northwind-intake-review.md"]
corpus = " ".join(p.read_text(encoding="utf-8") for p in src_files)
srcnums = set(re.findall(r"\d[\d,\.]*", corpus))
srcnums |= {n.replace(",", "") for n in srcnums}
docs = [R/"docs/product"/f for f in ["business-requirements.md","product-requirements.md","experiments.md","backlog.md","traceability.md"]]
docs += sorted((R/"docs/product/releases").glob("*.md"))
NUM = re.compile(r"(?<![A-Za-z0-9.#-])(\d[\d,]*(?:\.\d+)?)(?![\d])\s*(%|EUR|GB|hours?|minutes?|days?|seconds?|users?|customers?|calls?|claims?|orders?|rows?|photos?|months?|years?|weeks?|lines?|customers|USD)?")
seen = {}
for d in docs:
    lines = d.read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith(("|---", "```")):
            continue
        for m in NUM.finditer(ln):
            raw = m.group(1)
            n = raw.replace(",", "")
            if n in ("1","2","3","4","5","6","0","7","8") and not m.group(2):
                continue  # small counts (ids, numbering) are too noisy to check here
            if raw in srcnums or n in srcnums:
                continue
            if re.match(r"^(19|20)\d\d$", n):
                continue  # years
            ctx = ln.strip()
            key = (d.name, raw, m.group(2) or "")
            seen.setdefault(key, (i, ctx[max(0,m.start()-70):m.end()+60]))
for (fn, raw, unit), (i, ctx) in sorted(seen.items()):
    print(f"{fn}:{i} [{raw} {unit}] ...{ctx}...")
print("TOTAL distinct not-in-source figures:", len(seen))
