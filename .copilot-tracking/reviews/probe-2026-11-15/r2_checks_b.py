#!/usr/bin/env python3
"""Second-pass review, part B (read-only, stdout only).

  B1 C1 release table: BRD 10.2, PRD 6.2, backlog 1.1, release frontmatter and section 2, plan C1
  B2 cited A/O/X/T ids that have no local row in a release file (ES-03/ES-04 local register check)
  B3 stale text: '31 May 2027' as window end, old totals, sentences addressed to the coordinator
"""
import re
from pathlib import Path

ROOT = Path("/Users/waelkdouh/Demos/northwind-workshop")
PROD = ROOT / "docs" / "product"
REL = PROD / "releases"
PLAN = ROOT / ".copilot-tracking" / "plans" / "2026-11-15" / "northwind-product-documents-plan.md"

REG_FAMILY = r"(?:MVE-A-\d{2}|MVE-O-\d{2}|A-\d{2}|O-\d{2}|X-\d{2}|T-\d{2}|G-\d{2}|OQ-\d{2}|RG-\d{2})"
CITE_RE = re.compile(r"(?<![\w-])(" + REG_FAMILY + r")(?![\w-])")


def clean(s):
    return re.sub(r"[*`]", "", s).strip()


def cells(line):
    return [p.strip() for p in line.strip().strip("|").split("|")]


def c1_rows(text):
    """Rows of a C1-style table: cell0 track, cell1 release (or none)."""
    rows = {}
    for ln in text.splitlines():
        if not ln.startswith("|"):
            continue
        c = cells(ln)
        if len(c) < 6:
            continue
        rel = clean(c[1])
        if re.fullmatch(r"(azure|dotnet)-r\d", rel):
            rows[rel] = [clean(x) for x in c]
    return rows


def section(text, start, end):
    out, on = [], False
    for ln in text.splitlines():
        if re.match(start, ln):
            on = True
            continue
        if on and re.match(end, ln):
            break
        if on:
            out.append(ln)
    return "\n".join(out)


brd = (PROD / "business-requirements.md").read_text(encoding="utf-8")
prd = (PROD / "product-requirements.md").read_text(encoding="utf-8")
bl = (PROD / "backlog.md").read_text(encoding="utf-8")
plan = PLAN.read_text(encoding="utf-8")

print("=== B1. C1 release table ===")
sources = {
    "BRD 10.2": c1_rows(section(brd, r"^## 10\. ", r"^## 11\. ")),
    "PRD 6.2": c1_rows(section(prd, r"^## 6\. ", r"^## 7\. ")),
    "BL 1.1": c1_rows(section(bl, r"^## 1\. ", r"^## 2\. ")),
    "PLAN C1": c1_rows(section(plan, r"^### C1\. ", r"^### C2\. ")),
}
for src, rows in sources.items():
    print(f"  {src}: releases found {sorted(rows)}")

# columns: 0 track, 1 release, 2 theme, 3 window, 4 main epics, 5 BR/NFR covered, 6 leaves out
keys = ["azure-r1", "azure-r2", "azure-r3", "dotnet-r1", "dotnet-r2", "dotnet-r3"]
for rel in keys:
    print(f"  -- {rel}")
    base = None
    for src, rows in sources.items():
        if rel not in rows:
            print(f"     {src}: MISSING ROW")
            continue
        r = rows[rel]
        win = r[3] if len(r) > 3 else "?"
        print(f"     {src:9s} window='{win}' | epics='{r[4] if len(r) > 4 else '?'}' | covered-len={len(r[5]) if len(r) > 5 else '?'} | left-out-len={len(r[6]) if len(r) > 6 else '?'}")
        if base is None:
            base = (src, r)
        else:
            for idx, name in [(2, "theme"), (3, "window"), (4, "epics"), (5, "covered"), (6, "leaves out")]:
                if idx < len(r) and idx < len(base[1]) and r[idx] != base[1][idx]:
                    print(f"       DIFF {name} {src} vs {base[0]}:")
                    print(f"         {src}: {r[idx][:220]}")
                    print(f"         {base[0]}: {base[1][idx][:220]}")

# frontmatter + section 2 window in each release file
print("  -- release file headers:")
for f in sorted(REL.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    fm = re.search(r'target_window:\s*"([^"]+)"', t)
    row = re.search(r"\|\s*Target window\s*\|([^|]*)\|", t)
    dates_fm = fm.group(1) if fm else None
    dates_row = clean(row.group(1)) if row else None
    print(f"     {f.name}: frontmatter='{dates_fm}' | section2 row='{dates_row[:120] if dates_row else None}'")
    stale = re.findall(r"31 May 2027", t)
    if stale:
        print(f"       contains '31 May 2027' x{len(stale)} (check each is not a window end)")

print("\n=== B2. release files: cited ids without a local row ===")
for f in sorted(REL.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    local = set()
    for ln in t.splitlines():
        if ln.startswith("|"):
            c = cells(ln)
            if c and re.fullmatch(REG_FAMILY, clean(c[0])):
                local.add(clean(c[0]))
    cited = set(CITE_RE.findall(t))
    miss = sorted(cited - local)
    print(f"  {f.name}: cited {len(cited)}, local rows {len(local)}, cited without local row: {miss}")
    for ln_no, ln in enumerate(t.splitlines(), 1):
        for m in miss[:12]:
            if m in ln and ln.startswith("|") and ln_no < 400:
                print(f"      L{ln_no}: {cells(ln)[0][:40]} ... cites {m}")
                break

print("\n=== B3. stale or coordinator-addressed text in product docs ===")
for name, t in [("BRD", brd), ("PRD", prd), ("BL", bl)]:
    for pat in [r"must add", r"coordinator must", r"O-26 to O-31", r"register of record", r"31 May", r"140 items", r"34 enabler", r"37 feature", r"107 planned", r"Azure 14", r"start after", r"can start after", r"RG-0", r"PNFR-", r"RC-0\d", r"license:", r"business_goal_smart_status", r"diagram_format", r"fr_to_ac_coverage_threshold", r"fr_to_goal_coverage_threshold"]:
        hits = [i for i, ln in enumerate(t.splitlines(), 1) if re.search(pat, ln)]
        if hits:
            print(f"  {name} /{pat}/ lines {hits[:12]}{' ...' if len(hits) > 12 else ''}")
