#!/usr/bin/env python3
"""Read-only mechanical checks over docs/product backlog, releases and traceability.

Writes nothing. Prints findings to stdout only.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/Users/waelkdouh/Demos/northwind-workshop")
PROD = ROOT / "docs" / "product"
ID_RE = re.compile(r"^(EPIC|FEAT|STORY|EA|EN|EP)-\d+$")
TRACK_TAGS = {"track-azure", "track-dotnet", "track-power-platform"}
REL_TAGS = {"azure-r1", "azure-r2", "azure-r3", "dotnet-r1", "dotnet-r2", "dotnet-r3"}
problems = []


def flag(sev, where, msg):
    problems.append((sev, where, msg))
    print(f"[{sev}] {where}: {msg}")


def cells(line):
    parts = line.strip().strip("|").split("|")
    return [p.strip() for p in parts]


def clean(s):
    return s.replace("`", "").replace("*", "").strip()


def section(lines, start_pat, end_pat):
    out = []
    on = False
    for ln in lines:
        if re.match(start_pat, ln):
            on = True
            continue
        if on and re.match(end_pat, ln):
            break
        if on:
            out.append(ln)
    return out


# ---------- 1. Backlog item register (section 2) ----------
bl = (PROD / "backlog.md").read_text(encoding="utf-8").splitlines()
reg_lines = section(bl, r"^## 2\. Item register", r"^## 3\. ")
register = {}
for ln in reg_lines:
    if not ln.startswith("|"):
        continue
    c = cells(ln)
    if len(c) < 7 or not ID_RE.match(clean(c[0])):
        continue
    iid = clean(c[0])
    if iid in register:
        flag("Major", "backlog §2", f"{iid} appears twice in register")
    register[iid] = {
        "type": clean(c[1]),
        "title": clean(c[2]),
        "track": clean(c[3]),
        "release": clean(c[4]),
        "priority": clean(c[5]),
        "rank": clean(c[6]),
    }
print(f"REGISTER rows: {len(register)}")
from collections import Counter
print("  types:", dict(Counter(v["type"] for v in register.values())))
print("  releases:", dict(Counter(v["release"] for v in register.values())))
print("  tracks:", dict(Counter(v["track"] for v in register.values())))

# ---------- 2. Backlog detail blocks (section 4 and 5 headings) ----------
HEAD_RE = re.compile(r"^(#{3,6}) ((?:EPIC|FEAT|STORY|EA|EN|EP)-\d+) (.+)$")
details = {}
dup_detail = Counter()
cur = None
for idx, ln in enumerate(bl):
    m = HEAD_RE.match(ln)
    if m:
        iid = m.group(2)
        dup_detail[iid] += 1
        cur = iid
        details.setdefault(iid, {"title": m.group(3).strip(), "lines": [], "line": idx + 1})
        continue
    if re.match(r"^#{1,2} ", ln):
        cur = None
        continue
    if cur:
        details[cur]["lines"].append((idx + 1, ln))
dups = [k for k, v in dup_detail.items() if v > 1]
print(f"DETAIL headings: {len(details)} unique; duplicated headings: {dups}")
# Each heading occurrence counted; check whether section 5 repeats items
for k in dups:
    flag("Minor", "backlog §4/§5", f"{k} heading appears {dup_detail[k]} times")

missing_detail = set(register) - set(details)
extra_detail = set(details) - set(register)
if missing_detail:
    flag("Critical", "backlog", f"register items with no detail block: {sorted(missing_detail)}")
if extra_detail:
    flag("Major", "backlog", f"detail blocks not in register: {sorted(extra_detail)}")

TAGS_RE = re.compile(r"\*\*Tags:\*\*\s*(.*)")
PRI_RE = re.compile(r"\*\*Priority:\*\*\s*([A-Za-z0-9]+)")
RANK_RE = re.compile(r"\*\*Rank:\*\*\s*([0-9—-]+)")
STORY_RE = re.compile(r"\*\*Story:\*\*\s*(.*)")
SOURCE_RE = re.compile(r"\*\*Source:\*\*\s*(.*)")
AC_RE = re.compile(r"^\s*\*\s+`([^`]+)`\s*(.*)$")

story_stats = {}
for iid, d in details.items():
    tagline = None
    story_line = None
    source_line = None
    acs = []
    in_ac = False
    for ln_no, ln in d["lines"]:
        m = TAGS_RE.search(ln)
        if m:
            tagline = m.group(1)
        m = STORY_RE.search(ln)
        if m:
            story_line = m.group(1)
        m = SOURCE_RE.search(ln)
        if m:
            source_line = m.group(1)
        if re.search(r"\*\*Acceptance criteria:\*\*", ln):
            in_ac = True
            continue
        if in_ac:
            am = AC_RE.match(ln)
            if am:
                acs.append((ln_no, am.group(1), am.group(2)))
            elif ln.strip() and not ln.startswith("  "):
                in_ac = False
    tags = re.findall(r"`([^`]+)`", tagline or "")
    tracks = [t for t in tags if t in TRACK_TAGS]
    rels = [t for t in tags if t in REL_TAGS]
    kind = register.get(iid, {}).get("type", "?")
    story_stats[iid] = dict(kind=kind, tracks=tracks, rels=rels)
    if len(tracks) != 1:
        flag("Critical", f"backlog {iid} (line {d['line']})", f"track tags = {tracks} (need exactly 1)")
    reg = register.get(iid)
    if reg:
        if reg["track"] not in tracks:
            flag("Major", f"backlog {iid}", f"register track {reg['track']} not in detail tags {tracks}")
        reg_rel = reg["release"]
        if reg_rel in REL_TAGS:
            if rels != [reg_rel]:
                flag("Major", f"backlog {iid}", f"register release {reg_rel} vs detail tags {rels}")
        else:
            if rels:
                flag("Critical", f"backlog {iid}", f"unplanned in register but detail carries release tags {rels}")
        if reg["title"] != d["title"]:
            flag("Minor", f"backlog {iid}", f"title differs: register='{reg['title']}' detail='{d['title']}'")
    if kind == "story":
        if not story_line or not (re.search(r"\bAs (a|an|the) ", story_line) and "I want" in story_line and "so that" in story_line):
            flag("Major", f"backlog {iid} (line {d['line']})", "story text lacks 'As a / I want / so that'")
        gwt = [a for a in acs if all(w in a[2] for w in ("Given", "When", "Then"))]
        if len(gwt) < 2:
            flag("Major", f"backlog {iid} (line {d['line']})", f"only {len(gwt)} Given/When/Then criteria (need >=2 per user brief)")
        if not source_line or "source:" not in source_line.lower() and "(source" not in source_line.lower():
            flag("Major", f"backlog {iid}", "no source cite line")
    if kind == "enabler":
        if not source_line:
            flag("Major", f"backlog {iid}", "enabler has no source cite")
        gwt = [a for a in acs if all(w in a[2] for w in ("Given", "When", "Then"))]
        if len(gwt) < 1:
            flag("Major", f"backlog {iid}", "enabler has no Given/When/Then criterion")
        if not story_line or not all(w in story_line for w in ("As a", "I want", "so that")):
            flag("Minor", f"backlog {iid}", "enabler not in 'As a / I want / so that' form")
    # AC id must be prefixed by the item id
    for ln_no, acid, _ in acs:
        if not acid.startswith(iid + "/AC"):
            flag("Minor", f"backlog {iid} line {ln_no}", f"AC id '{acid}' does not use '{iid}/AC<n>'")

# Story / enabler coverage of FR-
print("STORIES:", sum(1 for v in story_stats.values() if v["kind"] == "story"),
      "ENABLERS:", sum(1 for v in story_stats.values() if v["kind"] == "enabler"))

# ---------- 3. Release files ----------
rel_items = {}  # release -> {id: row}
rel_dir = PROD / "releases"
for f in sorted(rel_dir.glob("*.md")):
    lines = f.read_text(encoding="utf-8").splitlines()
    rel_name = f.stem.replace("azure-", "azure-").replace("dotnet-", "dotnet-")
    rows = {}
    sec = section(lines, r"^## 3\. Items", r"^## 4\. ")
    for ln in sec:
        if not ln.startswith("|"):
            continue
        c = cells(ln)
        if len(c) < 7 or not ID_RE.match(clean(c[0])):
            continue
        iid = clean(c[0])
        tags_cell = " ".join(c[6:])
        rtags = [t for t in re.findall(r"`([^`]+)`", tags_cell) if t in TRACK_TAGS or t in REL_TAGS]
        if iid in rows:
            flag("Major", f"releases/{f.name}", f"{iid} listed twice")
        rows[iid] = {"title": clean(c[1]), "type": clean(c[2]), "priority": clean(c[3]),
                     "rank": clean(c[4]), "tags": rtags}
    rel_items[f.name] = rows
    print(f"RELEASE {f.name}: {len(rows)} item rows")
    for iid, row in rows.items():
        reg = register.get(iid)
        if reg is None:
            flag("Critical", f"releases/{f.name}", f"{iid} not in backlog register")
            continue
        # tags must match the register
        expected = {reg["track"]}
        if reg["release"] in REL_TAGS:
            expected.add(reg["release"])
        if set(row["tags"]) != expected:
            flag("Major", f"releases/{f.name} {iid}", f"tags {row['tags']} != register {sorted(expected)}")
        if row["title"] != reg["title"]:
            flag("Minor", f"releases/{f.name} {iid}", f"title differs from register")
        if row["priority"] != reg["priority"]:
            flag("Minor", f"releases/{f.name} {iid}", f"priority '{row['priority']}' vs register '{reg['priority']}'")
        if row["rank"] != reg["rank"]:
            flag("Minor", f"releases/{f.name} {iid}", f"rank '{row['rank']}' vs register '{reg['rank']}'")
        if reg["release"] not in REL_TAGS and f.name.startswith(("azure", "dotnet")):
            pass
    # release-expected set
    rel_tag = f.stem
    expected_ids = {k for k, v in register.items() if v["release"] == rel_tag}
    if set(rows) != expected_ids:
        flag("Critical", f"releases/{f.name}", f"items differ from register: missing={sorted(expected_ids - set(rows))} extra={sorted(set(rows) - expected_ids)}")

# one release per item
seen = Counter()
for fn, rows in rel_items.items():
    for iid in rows:
        seen[iid] += 1
for iid, n in seen.items():
    if n > 1:
        flag("Critical", "releases", f"{iid} appears in {n} release files")

# unplanned items in any release file
for iid, reg in register.items():
    if reg["release"] not in REL_TAGS and iid in seen:
        flag("Critical", "releases", f"unplanned item {iid} appears in a release file")

# planned items missing from release files
planned = {k for k, v in register.items() if v["release"] in REL_TAGS}
not_in_any = planned - set(seen)
if not_in_any:
    flag("Critical", "releases", f"planned items not in any release file: {sorted(not_in_any)}")
print("PLANNED in register:", len(planned), "| listed in release files:", len(set(seen) & planned))

# ---------- 4. Traceability ----------
tr = (PROD / "traceability.md").read_text(encoding="utf-8").splitlines()
cov = {}
for ln in tr:
    if not ln.startswith("|"):
        continue
    c = cells(ln)
    if not c:
        continue
    m = re.match(r"^(BR-\d\d|NFR-\d\d)\b", clean(c[0]))
    if not m or len(c) < 7:
        continue
    cov.setdefault(m.group(1), []).append(c)
ids_expected = [f"BR-{i:02d}" for i in range(1, 20)] + [f"NFR-{i:02d}" for i in range(1, 10)]
missing_tr = [i for i in ids_expected if i not in cov]
print("TRACE ids present:", len(cov), "of", len(ids_expected), "| missing:", missing_tr)
print("TRACE rows:", sum(len(v) for v in cov.values()))
for iid, rows in cov.items():
    for r in rows:
        stories = re.findall(r"(?:STORY|EA|EN|EP)-\d+", r[4])
        for s in stories:
            if s.startswith("STORY"):
                if s not in details:
                    flag("Critical", f"traceability {iid}", f"cites {s} which has no backlog detail")
                elif iid not in details[s]["lines"][0][1] and not any(iid in l for _, l in details[s]["lines"]):
                    flag("Major", f"traceability {iid}", f"{s} does not mention {iid} in its backlog block")
        relcell = r[5]
        for rt in re.findall(r"[a-z]+-r\d", relcell):
            if rt not in REL_TAGS:
                flag("Major", f"traceability {iid}", f"unknown release '{rt}'")
    # compare release cited in traceability row against backlog covering story
    for r in rows:
        for s in re.findall(r"STORY-\d+", r[4]):
            if s in register and register[s]["release"] not in r[5] and "unplanned" not in r[5].lower():
                flag("Major", f"traceability {iid}", f"{s} release '{register[s]['release']}' not shown in release cell '{r[5]}'")

# Not covered section
nc = section(tr, r"^## 4\. ", r"^## 5\. ")
print("TRACE §4 'not covered' text:", " ".join(clean(x) for x in nc if x.strip())[:400])
oos = section(tr, r"^## 5\. ", r"^## 6\. ")
print("TRACE §5 'out of scope' text:", " ".join(clean(x) for x in oos if x.strip())[:300])

# Summaries
print("\nPROBLEM COUNT:", len(problems), "| by severity:", dict(Counter(p[0] for p in problems)))
