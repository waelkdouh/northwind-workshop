#!/usr/bin/env python3
"""Read-only document checks: verbatim quotes, C1 release table, id definitions, source ids,
owners, deployment claims and figure provenance. Writes nothing; prints to stdout only."""
import re
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path("/Users/waelkdouh/Demos/northwind-workshop")
KD = ROOT / "knowledge-docs"
PROD = ROOT / "docs" / "product"
RES = ROOT / ".copilot-tracking" / "research" / "2026-11-15" / "northwind-product-documents-research.md"
PLAN = ROOT / ".copilot-tracking" / "plans" / "2026-11-15" / "northwind-product-documents-plan.md"
INTAKE = ROOT / ".copilot-tracking" / "reviews" / "2026-11-15-northwind-intake-review.md"


def rd(p):
    return p.read_text(encoding="utf-8")


def norm(s):
    s = s.replace("\u00a0", " ").replace("`", "").replace("**", "").replace("\\", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def cells(line):
    return [norm(x) for x in line.strip().strip("|").split("|")]


def table_rows(text):
    for ln in text.splitlines():
        if ln.startswith("|") and not re.match(r"^\|[\s\-|:]+\|$", ln.strip()):
            yield ln


bc = rd(KD / "business-case.md")
cs = rd(KD / "current-state.md")
es = rd(KD / "engineering-standards.md")
brd = rd(PROD / "business-requirements.md")
prd = rd(PROD / "product-requirements.md")
exp = rd(PROD / "experiments.md")
bl = rd(PROD / "backlog.md")
tr = rd(PROD / "traceability.md")
rel_files = {p.name: rd(p) for p in sorted((PROD / "releases").glob("*.md"))}
intake = rd(INTAKE)
research = rd(RES)
plan = rd(PLAN)

print("=" * 30, "A. VERBATIM QUOTES: business-case vs BRD", "=" * 30)
src = {}
for row in table_rows(bc):
    c = cells(row)
    if len(c) >= 2 and re.match(r"^(BR|NFR|C|SM|P|BA|OQ)-\d\d$", c[0]):
        src[c[0]] = c
brd_rows = {}
_brd_sec = []
_on = False
for _ln in brd.splitlines():
    if re.match(r"^## (3|7|8|9)\. ", _ln):
        _on = True
    elif re.match(r"^## ", _ln):
        _on = False
    if _on:
        _brd_sec.append(_ln)
for row in table_rows("\n".join(_brd_sec)):
    c = cells(row)
    if c and re.match(r"^(BR|NFR|C|SM|P)-\d\d$", c[0]):
        brd_rows.setdefault(c[0], []).append(c)
mismatch = 0
for iid, c in sorted(src.items()):
    if iid not in brd_rows:
        if iid.startswith(("BR", "NFR", "C-", "SM")):
            print(f"  MISSING in BRD sections 3/7/8/9: {iid}")
            mismatch += 1
        continue
    if len(brd_rows[iid]) > 1:
        print(f"  {iid} appears {len(brd_rows[iid])} times in BRD sections 3/7/8/9")
    b = brd_rows[iid][0]
    if iid.startswith(("BR-", "NFR-", "C-")):
        if c[1] != b[1]:
            print(f"  TEXT DIFF {iid}:\n    source: {c[1]}\n    brd   : {b[1]}")
            mismatch += 1
        if iid.startswith("BR-") and c[2] != b[2]:
            print(f"  PRIORITY DIFF {iid}: source={c[2]} brd={b[2]}")
            mismatch += 1
print("  verbatim mismatches:", mismatch)
# C-xx constraints and SM measure rows in BRD may use different column order: show raw for SM
for sm in ["SM-01", "SM-05", "SM-07"]:
    print("  BRD row", sm, "->", [r for r in table_rows(brd) if r.startswith(f"| {sm}")][:1])

print("\n" + "=" * 30, "B. C1 RELEASE TABLE IDENTITY", "=" * 30)
rel_rows = {}
for name, text in [("BRD 10.2", brd), ("PRD 6.2", prd), ("BACKLOG 1.1", bl)]:
    rows = [norm(r) for r in table_rows(text) if re.match(r"^\| (Azure|\.NET|Power Platform)", r)]
    rel_rows[name] = rows
    print(f"  {name}: {len(rows)} release-table rows")
ref = rel_rows["PRD 6.2"]
for name, rows in rel_rows.items():
    if rows != ref:
        print(f"  DIFF {name} vs PRD 6.2:")
        for a, b in zip(rows, ref):
            if a != b:
                print("    doc :", a[:260])
                print("    prd :", b[:260])
        if len(rows) != len(ref):
            print("    row counts differ", len(rows), len(ref))
    else:
        print(f"  {name} identical to PRD 6.2")
# frontmatter windows of release files
for fn, t in rel_files.items():
    fm = re.search(r"target_window: \"([^\"]+)\"", t)
    rel = re.search(r"^release: \"?([^\"\n]+)\"?", t, re.M)
    print(f"  {fn}: window={fm.group(1) if fm else 'NONE'}; release={rel.group(1) if rel else '?'}")

print("\n" + "=" * 30, "C. ID DEFINITIONS ACROSS DOCS", "=" * 30)
FAM = r"(A|O|G|OQ|X|T|RG|MVE|BG|PFR|PNFR|RC)"
defs = defaultdict(list)  # id -> [(doc, text)]
DOCS = {"BRD": brd, "PRD": prd, "EXP": exp, "BACKLOG": bl, "TRACE": tr}
for n, t in rel_files.items():
    DOCS["REL " + n] = t
for dn, text in DOCS.items():
    for row in table_rows(text):
        c = cells(row)
        if not c:
            continue
        m = re.match(rf"^({FAM}-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?)$", c[0])
        if m and len(c) >= 2:
            defs[m.group(1)].append((dn, " | ".join(c[1:])[:200]))
ids_defined = set(defs)
print("  distinct ids defined in register rows:", len(ids_defined))
# Cited anywhere
cited = defaultdict(set)
for dn, text in DOCS.items():
    for m in re.finditer(r"(?<![A-Za-z0-9-])((?:A|O|G|OQ|X|T|RG|MVE|BG)-\d+)(?![0-9])", text):
        cited[m.group(1)].add(dn)
undef = sorted(k for k in cited if k not in ids_defined)
print("  cited but NOT in any register row:", undef)
print("  ids for release-local or new families present:",
      sorted(set(re.findall(r"\b(?:AZ\d-O\d+|A-D\d-\d+|O-D\d-\d+|MVE-A-\w+)\b", " ".join(DOCS.values())))))
for iid in sorted(ids_defined, key=lambda x: (x.split("-")[0], int(re.search(r"\d+", x).group()) if re.search(r"\d+", x) else 0)):
    texts = {t[:90] for _, t in defs[iid]}
    if len(defs[iid]) > 1:
        docs_def = sorted({d for d, _ in defs[iid]})
        print(f"  {iid} defined in {docs_def}:")
        for d, t in defs[iid]:
            print(f"     [{d}] {t[:150]}")
print("\n  ids the plan promised (C9): A-01..A-48 and O-01..O-25; checking presence in register rows:")
promised = [f"A-{i:02d}" for i in range(1, 58) if i not in (26, 28)] + [f"O-{i:02d}" for i in range(1, 31)]
absent = [p for p in promised if p not in ids_defined]
print("  absent from every register:", absent)

print("\n" + "=" * 30, "D. OWNERS ON A-/O-/X- REGISTER ROWS", "=" * 30)
OWNERS = ["Lena Varga", "Marc Dubois", "Ahmed Benali", "Sofie Peeters", "Julien Moreau", "Pieter Janssens"]
for dn, text in DOCS.items():
    for row in table_rows(text):
        c = cells(row)
        if c and re.match(r"^(A|O|X)-\d+$", c[0]) and len(c) >= 3:
            if not any(o in " | ".join(c) for o in OWNERS):
                print(f"  [{dn}] no named owner: {' | '.join(c)[:160]}")

print("\n" + "=" * 30, "E. SOURCE IDS CITED THAT DO NOT EXIST", "=" * 30)
known = set()
for t in (bc, cs, es):
    known.update(re.findall(r"\b(BR-\d+|NFR-\d+|C-\d+|SM-\d+|P-\d+|BA-\d+|OQ-\d+|CS-\d+|ES-\d+)\b", t))
known_bc = {k for k in known}
cites = Counter()
for dn, text in DOCS.items():
    for m in re.finditer(r"\b(BR-\d+|NFR-\d+|C-\d+|SM-\d+|P-\d+|BA-\d+|OQ-\d+|CS-\d+|ES-\d+)\b", text):
        cites[m.group(1)] += 1
bad = sorted(k for k in cites if k not in known and not re.match(r"^(BA)-0[1-3]$", k))
print("  source-family ids cited but not in knowledge-docs:", bad)
# Verify ES ids referenced exist in engineering standards list
es_defined = set(re.findall(r"^\| (ES-\d+) \|", es, re.M))
es_cited = {k for k in cites if k.startswith("ES-")}
print("  ES ids cited but not defined in engineering-standards:", sorted(es_cited - es_defined))
cs_defined = set(re.findall(r"^\| (CS-\d+) \|", cs, re.M))
cs_cited = {k for k in cites if k.startswith("CS-")}
print("  CS ids cited but not defined in current-state:", sorted(cs_cited - cs_defined))
print("  CS ids in current-state not cited anywhere:", sorted(cs_defined - cs_cited))
br_cited = {k for k in cites if k.startswith("BR-")}
print("  BR ids cited:", len(br_cited), "| BR not cited:", sorted({f'BR-{i:02d}' for i in range(1,20)} - br_cited))

print("\n" + "=" * 30, "F. PLAN-LOCAL IDs (PFR/PNFR/RC) AND OTHER FAMILIES", "=" * 30)
for fam in ["PFR", "PNFR", "RC", "BG", "G", "OQ", "RG", "T", "X"]:
    found = Counter()
    for dn, text in DOCS.items():
        for m in re.finditer(rf"(?<![A-Za-z0-9-]){fam}-\d+", text):
            found[m.group(0)] += 1
    print(f"  {fam}: {len(found)} distinct ids cited; e.g. {sorted(found)[:6]} ...")

print("\n" + "=" * 30, "G. CLAIM WORDING (deployment, tenant, tags, commits)", "=" * 30)
pat = re.compile(r"\b(deployed|has been deployed|was deployed|published to|created in|imported|tenant changed|committed|git tag|tagged|approved by|approved on|approved:|status: approved|Approved)\b", re.I)
for dn, text in DOCS.items():
    for i, ln in enumerate(text.splitlines(), 1):
        if pat.search(ln):
            s = ln.strip()
            print(f"  [{dn}:{i}] {s[:230]}")
