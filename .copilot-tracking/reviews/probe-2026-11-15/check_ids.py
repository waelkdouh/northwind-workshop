#!/usr/bin/env python3
"""Read-only id meaning and location checks. Writes nothing; prints to stdout."""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/waelkdouh/Demos/northwind-workshop")
PROD = ROOT / "docs" / "product"
DOCS = {
    "BRD": PROD / "business-requirements.md",
    "PRD": PROD / "product-requirements.md",
    "EXP": PROD / "experiments.md",
    "BACKLOG": PROD / "backlog.md",
    "TRACE": PROD / "traceability.md",
}
for p in sorted((PROD / "releases").glob("*.md")):
    DOCS["REL " + p.name] = p
TEXT = {k: v.read_text(encoding="utf-8") for k, v in DOCS.items()}
OWNERS = ["Lena Varga", "Marc Dubois", "Ahmed Benali", "Sofie Peeters", "Julien Moreau", "Pieter Janssens"]
FAM = r"(A|O|G|OQ|X|T|RG|MVE|BG|PFR|PNFR|RC)"


def cells(line):
    return [re.sub(r"[`*]", "", x).strip() for x in line.strip().strip("|").split("|")]


defs = defaultdict(list)
for dn, text in TEXT.items():
    for ln in text.splitlines():
        if not ln.startswith("|"):
            continue
        c = cells(ln)
        if c and re.match(rf"^{FAM}-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?$", c[0]) and len(c) >= 3:
            defs[c[0]].append((dn, c))

print("== ids defined in exactly one register row (new or local ids) ==")
single = [k for k, v in defs.items() if len(v) == 1]
for k in sorted(single):
    if re.match(r"^(A-(4[89]|5\d)|O-(2[5-9]|30)|MVE-|AZ|A-D|O-D|X-1[69]|RG|T-1[0-9])", k):
        dn, c = defs[k][0]
        print(f"  {k} [{dn}] {' | '.join(c[1:])[:200]}")

print("\n== ids whose named owner or opening words differ across docs ==")
for k in sorted(defs):
    rows = defs[k]
    if len(rows) < 2:
        continue
    owners = {}
    for dn, c in rows:
        o = [x for x in OWNERS if x in " | ".join(c)]
        owners[dn] = tuple(o)
    distinct_owner_sets = {v for v in owners.values() if v}
    heads = {}
    for dn, c in rows:
        words = re.findall(r"[A-Za-z]+", " ".join(c[1:2]))[:4]
        heads[dn] = " ".join(words).lower()
    if len(set(heads.values())) > 1 or len(distinct_owner_sets) > 1:
        print(f"  {k}:")
        for dn, c in rows:
            print(f"     [{dn}] owner={owners[dn]} :: {' | '.join(c[1:])[:170]}")

print("\n== where undefined/unusual ids are cited ==")
for k in ["A-26", "A-28", "RG-02", "RG-03", "RG-04", "X-16", "X-19", "PNFR-05", "RC-03", "RC-05"]:
    hits = []
    for dn, text in TEXT.items():
        for i, ln in enumerate(text.splitlines(), 1):
            if re.search(rf"(?<![A-Za-z0-9-]){re.escape(k)}(?![0-9])", ln):
                hits.append(f"{dn}:{i}")
    print(f"  {k}: {hits[:12]}")
    for dn, text in TEXT.items():
        for i, ln in enumerate(text.splitlines(), 1):
            if re.search(rf"(?<![A-Za-z0-9-]){re.escape(k)}(?![0-9])", ln) and dn in ("BRD", "PRD", "BACKLOG"):
                print(f"      > [{dn}:{i}] {ln.strip()[:240]}")
                break
        else:
            continue
        break
