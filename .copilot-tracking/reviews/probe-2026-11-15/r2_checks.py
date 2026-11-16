#!/usr/bin/env python3
"""Second-pass (review 2) read-only checks over docs/product and knowledge-docs.

Writes nothing. Prints results to stdout only.
Checks:
  1  counts (register, sections, release "Counts:" lines, traceability)
  2  release tables vs backlog register (ids, titles, priority, rank, tags)
  3  track tag exactly one; release tag only on planned items; tag track == track tag
  4  stories: As a / I want / so that and >= 2 Given/When/Then; enablers >= 1 GWT
  5  cited A/O/X/T/MVE/G/OQ/RG ids defined in same file or in named register of record
  6  conflicting definitions of the same id across files (text cell)
  7  C1 release table identical across BRD 10.2, PRD 6.2, backlog 1.1, release headers
  8  serves mapping: backlog Serves vs PRD section 9 Serves vs PRD FR item cells
  9  cited source ids (BR/NFR/C/SM/CS/ES/P/BA/OQ) exist in knowledge-docs
 10  calendar: Sundays in June 2027; window dates
"""
import re
import datetime
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/waelkdouh/Demos/northwind-workshop")
PROD = ROOT / "docs" / "product"
REL = PROD / "releases"
KD = ROOT / "knowledge-docs"

BL = PROD / "backlog.md"
TR = PROD / "traceability.md"
BRD = PROD / "business-requirements.md"
PRD = PROD / "product-requirements.md"
EXP = PROD / "experiments.md"
REL_FILES = sorted(REL.glob("*.md"))

ITEM_RE = re.compile(r"^(EPIC|FEAT|STORY|EA|EN|EP)-\d+$")
TRACK_TAGS = {"track-azure", "track-dotnet", "track-power-platform"}
REL_TAGS = {"azure-r1", "azure-r2", "azure-r3", "dotnet-r1", "dotnet-r2", "dotnet-r3"}
REG_FAMILY = r"(?:MVE-A-\d{2}|MVE-O-\d{2}|A-\d{2}|O-\d{2}|X-\d{2}|T-\d{2}|G-\d{2}|OQ-\d{2}|RG-\d{2})"
CITE_RE = re.compile(r"(?<![\w-])(" + REG_FAMILY + r")(?![\w-])")
SRC_RE = re.compile(r"(?<![\w-])((?:BR|NFR|C|SM|CS|ES|P|BA|OQ)-\d{2})(?![\w-])")

findings = []


def out(sev, where, msg):
    findings.append((sev, where, msg))
    print(f"[{sev}] {where}: {msg}")


def cells(line):
    return [p.strip() for p in line.strip().strip("|").split("|")]


def clean(s):
    return s.replace("`", "").replace("*", "").strip()


def table_rows(text):
    """Yield (line_no, cells) for markdown table rows, skipping separators."""
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.startswith("|") and not re.match(r"^\|\s*:?-{3,}", ln):
            yield i, cells(ln)


def section_text(text, start_pat, end_pat):
    out_lines, on = [], False
    for ln in text.splitlines():
        if re.match(start_pat, ln):
            on = True
            continue
        if on and re.match(end_pat, ln):
            break
        if on:
            out_lines.append(ln)
    return "\n".join(out_lines)


bl_text = BL.read_text(encoding="utf-8")
tr_text = TR.read_text(encoding="utf-8")
brd_text = BRD.read_text(encoding="utf-8")
prd_text = PRD.read_text(encoding="utf-8")
exp_text = EXP.read_text(encoding="utf-8")
rel_texts = {f.name: f.read_text(encoding="utf-8") for f in REL_FILES}

# ---------------------------------------------------------------- 1. register
print("=== 1. COUNTS ===")
register = {}
for ln_no, c in table_rows(section_text(bl_text, r"^## 2\. ", r"^## 3\. ")):
    if len(c) < 7 or not ITEM_RE.match(clean(c[0])):
        continue
    iid = clean(c[0])
    if iid in register:
        out("Major", "backlog §2", f"{iid} duplicated in register")
    register[iid] = dict(type=clean(c[1]), title=clean(c[2]), track=clean(c[3]),
                         release=clean(c[4]), priority=clean(c[5]), rank=clean(c[6]), line=ln_no)
types = Counter(v["type"] for v in register.values())
tracks = Counter(v["track"] for v in register.values())
rels = Counter(v["release"] for v in register.values())
print("register total:", len(register), "| types:", dict(types))
print("tracks:", dict(tracks))
print("releases:", dict(rels))
exp_totals = {"total": 144, "epic": 12, "feature": 39, "story": 57, "enabler": 36,
              "track-azure": 54, "azure-r2": 20, "azure-r3": 13}
got = {"total": len(register), "epic": types["epic"], "feature": types["feature"],
       "story": types["story"], "enabler": types["enabler"], "track-azure": tracks["track-azure"],
       "azure-r2": rels["azure-r2"], "azure-r3": rels["azure-r3"]}
for k, v in exp_totals.items():
    status = "OK" if got[k] == v else "MISMATCH"
    print(f"  expect {k}={v} got {got[k]} {status}")
    if got[k] != v:
        out("Major", "backlog §2", f"count {k} expected {v} got {got[k]}")

# backlog section 3 table
sec3 = section_text(bl_text, r"^## 3\. ", r"^## 4\. ")
print("--- backlog §3 rows:")
for ln_no, c in table_rows(sec3):
    print("   ", ln_no, " | ".join(clean(x) for x in c)[:260])

# release file Counts lines
print("--- release 'Counts' lines:")
for name, t in rel_texts.items():
    m = re.search(r"[Cc]ounts?:[^\n]*", t)
    print("   ", name, "->", m.group(0)[:220] if m else "NO COUNTS LINE")

# compute per release composition
def comp(relname):
    ids = [k for k, v in register.items() if v["release"] == relname]
    t = Counter(register[k]["type"] for k in ids)
    return dict(epic=t["epic"], feature=t["feature"], story=t["story"], enabler=t["enabler"], total=len(ids))

for r in ["azure-r1", "azure-r2", "azure-r3", "dotnet-r1", "dotnet-r2", "dotnet-r3"]:
    print("   computed", r, comp(r))

# ---------------------------------------------------------------- 2. release tables
print("\n=== 2/3. RELEASE TABLES vs REGISTER; TAGS ===")
rel_items = {}
for name, t in rel_texts.items():
    sec = section_text(t, r"^## 3\. ", r"^## 4\. ")
    rows = {}
    for ln_no, c in table_rows(sec):
        if len(c) < 5 or not ITEM_RE.match(clean(c[0])):
            continue
        iid = clean(c[0])
        tagtxt = " ".join(c[5:])
        rtags = [x for x in re.findall(r"`([^`]+)`", tagtxt) if x in TRACK_TAGS or x in REL_TAGS]
        rows[iid] = dict(title=clean(c[1]), priority=clean(c[3]) if len(c) > 3 else "",
                         rank=clean(c[4]) if len(c) > 4 else "", tags=rtags, line=ln_no)
    rel_items[name] = rows
    print(f"{name}: {len(rows)} item rows (section 3)")
    for iid, row in rows.items():
        reg = register.get(iid)
        if not reg:
            out("Critical", f"releases/{name}", f"{iid} not in register")
            continue
        exp_tags = {reg["track"]} | ({reg["release"]} if reg["release"] in REL_TAGS else set())
        if set(row["tags"]) != exp_tags:
            out("Major", f"releases/{name} {iid}", f"tags {row['tags']} != register {sorted(exp_tags)}")
        if row["title"] != reg["title"]:
            out("Minor", f"releases/{name} {iid}", f"title '{row['title']}' != register '{reg['title']}'")
        if row["priority"] and row["priority"] != reg["priority"]:
            out("Minor", f"releases/{name} {iid}", f"priority '{row['priority']}' != register '{reg['priority']}'")
        if row["rank"] and row["rank"] != reg["rank"]:
            out("Minor", f"releases/{name} {iid}", f"rank '{row['rank']}' != register '{reg['rank']}'")
    stem = name[:-3]
    expected = {k for k, v in register.items() if v["release"] == stem}
    if set(rows) != expected:
        out("Critical", f"releases/{name}",
            f"set differs: missing={sorted(expected - set(rows))} extra={sorted(set(rows) - expected)}")

seen = Counter(i for rows in rel_items.values() for i in rows)
multi = [i for i, n in seen.items() if n > 1]
if multi:
    out("Critical", "releases", f"ids in >1 release file: {multi}")
planned = {k for k, v in register.items() if v["release"] in REL_TAGS}
print("planned in register:", len(planned), "| in release files:", len(planned & set(seen)),
      "| unplanned in release files:", sorted(i for i in seen if register[i]["release"] not in REL_TAGS))

# detail blocks
HEAD = re.compile(r"^(#{3,6}) ((?:EPIC|FEAT|STORY|EA|EN|EP)-\d+) (.+)$")
details = {}
cur = None
bl_lines = bl_text.splitlines()
for idx, ln in enumerate(bl_lines):
    m = HEAD.match(ln)
    if m:
        cur = m.group(2)
        if cur in details:
            out("Major", f"backlog detail {cur}", "duplicate detail heading")
        details[cur] = dict(title=m.group(3).strip(), line=idx + 1, lines=[])
        continue
    if re.match(r"^#{1,2} ", ln):
        cur = None
        continue
    if cur:
        details[cur]["lines"].append((idx + 1, ln))
print("detail blocks:", len(details), "| register without detail:", sorted(set(register) - set(details)),
      "| detail without register:", sorted(set(details) - set(register)))

TAGS_RE = re.compile(r"\*\*Tags:\*\*\s*(.*)")
SERVES_RE = re.compile(r"\*\*Serves:\*\*\s*([^·\n]*)")
PARENT_RE = re.compile(r"\*\*Parent:\*\*\s*([A-Z]+-\d+)")
STORY_RE = re.compile(r"\*\*Story:\*\*\s*(.*)")
SOURCE_RE = re.compile(r"\*\*Source:\*\*\s*(.*)")
AC_RE = re.compile(r"^\s*\*\s+`([^`]+)`\s*(.*)$")

detail_info = {}
for iid, d in details.items():
    tagline = story = source = None
    serves = parent = None
    acs = []
    in_ac = False
    for ln_no, ln in d["lines"]:
        m = TAGS_RE.search(ln)
        if m:
            tagline = m.group(1)
        m = SERVES_RE.search(ln)
        if m:
            serves = m.group(1).strip()
        m = PARENT_RE.search(ln)
        if m:
            parent = m.group(1)
        m = STORY_RE.search(ln)
        if m:
            story = m.group(1)
        m = SOURCE_RE.search(ln)
        if m:
            source = m.group(1)
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
    trk = [t for t in tags if t in TRACK_TAGS]
    rl = [t for t in tags if t in REL_TAGS]
    detail_info[iid] = dict(tags=tags, tracks=trk, rels=rl, story=story, source=source,
                            serves=serves, parent=parent, acs=acs, line=d["line"], title=d["title"])
    reg = register.get(iid)
    if len(trk) != 1:
        out("Critical", f"backlog {iid} (L{d['line']})", f"track tags {trk} (need exactly one)")
    if reg:
        if reg["track"] not in trk:
            out("Major", f"backlog {iid}", f"register track {reg['track']} not in tags {trk}")
        if reg["release"] in REL_TAGS and rl != [reg["release"]]:
            out("Major", f"backlog {iid}", f"release tags {rl} != register {reg['release']}")
        if reg["release"] not in REL_TAGS and rl:
            out("Critical", f"backlog {iid}", f"unplanned item carries release tags {rl}")
        if reg["title"] != d["title"]:
            out("Minor", f"backlog {iid}", f"title differs register vs detail")
    if reg and reg["type"] == "story":
        ok_story = bool(story) and re.search(r"\bAs (a|an|the) ", story) and "I want" in story and "so that" in story
        if not ok_story:
            out("Major", f"backlog {iid} (L{d['line']})", "story lacks As a / I want / so that")
        gwt = [a for a in acs if all(w in a[2] for w in ("Given", "When", "Then"))]
        if len(gwt) < 2:
            out("Major", f"backlog {iid} (L{d['line']})", f"{len(gwt)} Given/When/Then (need >= 2)")
    if reg and reg["type"] == "enabler":
        gwt = [a for a in acs if all(w in a[2] for w in ("Given", "When", "Then"))]
        if len(gwt) < 1:
            out("Major", f"backlog {iid}", "enabler has no Given/When/Then")
        if not story or not all(w in story for w in ("As a", "I want", "so that")):
            out("Minor", f"backlog {iid} (L{d['line']})", "enabler story text not in As a / I want / so that form")
        if not d["lines"] or not any("**Source:**" in l for _, l in d["lines"]):
            out("Major", f"backlog {iid}", "enabler has no Source line")
    if reg and reg["type"] in ("story", "enabler", "feature", "epic"):
        if not any("**Source:**" in l for _, l in d["lines"]):
            out("Major", f"backlog {iid}", "no Source line")
    for ln_no, acid, _ in acs:
        if not acid.startswith(iid + "/AC"):
            out("Minor", f"backlog {iid} L{ln_no}", f"AC id '{acid}' not '{iid}/AC<n>'")

# parent / release consistency for epics and features
for iid, info in detail_info.items():
    reg = register.get(iid)
    if not reg or reg["type"] not in ("feature", "enabler", "story"):
        continue
    par = info["parent"]
    if par and par in register:
        if register[par]["release"] != reg["release"] or register[par]["track"] != reg["track"]:
            out("Major", f"backlog {iid}", f"parent {par} release/track differs")

# epic/feature release equals children
for iid, reg in register.items():
    if reg["type"] in ("epic", "feature"):
        kids = [k for k, v in detail_info.items() if v["parent"] == iid]
        bad = [k for k in kids if register[k]["release"] != reg["release"]]
        if bad:
            out("Major", f"backlog {iid}", f"children with other release: {bad}")

# ---------------------------------------------------------------- 4. serves / FR mapping
print("\n=== 8. SERVES MAPPING ===")
bl_serves = {k: v["serves"] for k, v in detail_info.items() if register.get(k, {}).get("type") == "enabler"}
prd_rows = {}
for ln_no, c in table_rows(prd_text):
    if not c:
        continue
    first = clean(c[0])
    if re.match(r"^(EA|EN|EP)-\d+$", first) and len(c) >= 6:
        prd_rows.setdefault(first, []).append((ln_no, c))
for iid in sorted(bl_serves):
    b = bl_serves[iid]
    prd_list = prd_rows.get(iid, [])
    p_serves = clean(prd_list[0][1][5]) if prd_list and len(prd_list[0][1]) > 5 else None
    bset = set(re.findall(r"FR-\d{3}", b or ""))
    pset = set(re.findall(r"FR-\d{3}", p_serves or ""))
    flag = "" if bset == pset else "  <-- MISMATCH"
    if flag or iid in ("EA-15", "EA-16"):
        print(f"  {iid}: backlog Serves={sorted(bset)} | PRD §9 Serves={sorted(pset)} (PRD rows: {[r[0] for r in prd_list]}){flag}")
    if flag:
        out("Major", f"PRD §9 vs backlog {iid}", f"Serves backlog {sorted(bset)} != PRD {sorted(pset)}")
    if len(prd_list) != 1:
        out("Major", f"PRD §9 {iid}", f"appears {len(prd_list)} times in PRD enabler tables")

# FR rows in PRD §7: cell index 7 lists items
fr_items = {}
for ln_no, c in table_rows(prd_text):
    if c and re.match(r"^FR-\d{3}$", clean(c[0])) and len(c) >= 8:
        fr_items[clean(c[0])] = (ln_no, set(re.findall(r"(?:EA|EN|EP)-\d+", c[7])))
print("FR rows parsed:", len(fr_items))
for iid in sorted(bl_serves):
    b = set(re.findall(r"FR-\d{3}", bl_serves[iid] or ""))
    for fr in sorted(b):
        if fr not in fr_items:
            out("Major", f"backlog {iid}", f"serves {fr} not in PRD §7")
        elif iid not in fr_items[fr][1]:
            out("Major", f"PRD §7 {fr}", f"row items cell lacks {iid} (backlog says {iid} serves {fr})")
for fr, (ln_no, ids) in sorted(fr_items.items()):
    for e in sorted(ids):
        if e in bl_serves and fr not in set(re.findall(r"FR-\d{3}", bl_serves[e] or "")):
            print(f"  note: PRD §7 {fr} (L{ln_no}) lists {e}, backlog Serves for {e} = {bl_serves[e]}")

# ---------------------------------------------------------------- 5/6. id definitions
print("\n=== 5/6. ID DEFINITIONS AND CONFLICTS ===")
DOCS = {"BRD": (BRD, brd_text), "PRD": (PRD, prd_text), "EXP": (EXP, exp_text),
        "BL": (BL, bl_text), "TR": (TR, tr_text)}
for n, t in rel_texts.items():
    DOCS["REL:" + n] = (REL / n, t)


def defined_in(text):
    """Ids in first cell of table rows (definitions)."""
    d = {}
    for ln_no, c in table_rows(text):
        if not c:
            continue
        first = clean(c[0])
        m = re.fullmatch(REG_FAMILY, first)
        if m:
            body = c[1:-1] if len(c) > 2 else c[1:]
            text_cell = clean(max(body, key=len)) if body else ""
            d.setdefault(first, []).append((ln_no, text_cell, clean(c[-1]) if len(c) > 2 else ""))
    return d


defs = {k: defined_in(t) for k, (_, t) in DOCS.items()}
cited = {k: Counter(CITE_RE.findall(t)) for k, (_, t) in DOCS.items()}
bl_defs = set(defs["BL"])
for k in DOCS:
    und = sorted(i for i in cited[k] if i not in defs[k])
    if not und:
        print(f"  {k}: all {len(cited[k])} cited A/O/X/T/MVE/G/OQ/RG ids defined in file")
        continue
    ror = "register of record" in DOCS[k][1]
    resolved_by_bl = [i for i in und if i in bl_defs]
    unresolved = [i for i in und if i not in bl_defs]
    print(f"  {k}: {len(und)} cited-not-defined locally; register-of-record sentence={ror}; "
          f"defined in backlog §7={len(resolved_by_bl)}; not defined anywhere={unresolved}")
    if unresolved:
        out("Major" if k.startswith("REL") or k in ("BRD", "PRD", "EXP") else "Minor", f"{k}",
            f"ids cited but defined nowhere: {unresolved}")

# conflicting definitions
print("\n  -- definition text comparisons (text cell, normalised):")
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[*`]", "", s)).strip().rstrip(".")
allids = defaultdict(list)
for k in DOCS:
    for iid, rows in defs[k].items():
        for ln_no, txt, owner in rows:
            allids[iid].append((k, ln_no, norm(txt), norm(owner)))
TOK_RE = re.compile(
    r"\d+(?:[.,]\d+)?|January|February|March|April|May|June|July|August|September|October|November|December"
    r"|azure-r\d|dotnet-r\d|\b(?:BR|NFR|C|SM|CS|ES|P|BA|FR|EA|EN|EP|STORY|EPIC|FEAT|MVE|OPEN|ASSUMPTION)-?[\w-]*")
TOK_IDS = ("A-", "O-", "X-", "T-", "MVE-", "G-", "OQ-")
conflicts = 0
for iid in sorted(allids, key=lambda x: (x.split("-")[0], int(x.split("-")[-1]))):
    rows = allids[iid]
    # compare the numeric, date and id tokens of each copy against the register of record (backlog section 7)
    ref = [r for r in rows if r[0] == "BL"]
    if not ref:
        continue
    ref_t = set(TOK_RE.findall(ref[0][2]))
    for k, ln_no, txt, owner in rows:
        if k == "BL":
            continue
        t = set(TOK_RE.findall(txt))
        diff = (ref_t ^ t)
        diff = {d for d in diff if not d.startswith(("ASSUMPTION", "OPEN", "BR-", "NFR-", "C-", "SM-", "CS-", "ES-", "P-", "BA-", "FR-", "STORY", "EPIC", "FEAT", "EA-", "EN-", "EP-"))}
        if diff:
            conflicts += 1
            print(f"  NUM/DATE/ID DIFF {iid} in {k} L{ln_no}: only-in-register={sorted(ref_t - t)} only-in-copy={sorted(t - ref_t)}")
    owners = {o for _, _, _, o in rows}
    if len(owners) > 1 and iid.startswith(("A-", "O-")):
        print(f"  note owner variants {iid}: {sorted(owners)}")
print("  copies whose numbers/dates/ids differ from register of record:", conflicts)

# ids defined in backlog §7 and missing elsewhere that should be registers: report counts
print("  backlog §7 defines:", len(bl_defs), "ids:", sorted(bl_defs)[:5], "...")
for k in ["BRD", "PRD", "EXP", "TR"] + [x for x in DOCS if x.startswith("REL:")]:
    got_ids = set(defs[k])
    missing_new = sorted(i for i in ["A-49", "A-50", "A-51", "A-52", "A-53", "A-54", "A-55", "A-56", "A-57", "A-58", "A-59",
                                      "O-26", "O-27", "O-28", "O-29", "O-30", "O-31"] if i in cited[k] and i not in got_ids)
    if missing_new:
        print(f"  {k}: cites but no register row for {missing_new}")

# ---------------------------------------------------------------- 9. source ids exist
print("\n=== 9. SOURCE IDS EXIST IN KNOWLEDGE-DOCS ===")
kd_text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(KD.glob("*.md")))
kd_defined = set(re.findall(r"(?<![\w-])((?:BR|NFR|C|SM|CS|ES|P|BA|OQ|G)-\d{2})(?![\w-])", kd_text))
print("knowledge-docs defines:", len(kd_defined), "ids; families:",
      dict(Counter(i.split('-')[0] for i in kd_defined)))
cited_src = Counter()
for k, (_, t) in DOCS.items():
    for s in SRC_RE.findall(t):
        cited_src[s] += 1
missing_src = sorted(s for s in cited_src if s not in kd_defined)
print("cited source ids:", len(cited_src), "| not found in knowledge-docs:", missing_src)
for s in missing_src:
    out("Minor", "source ids", f"{s} cited ({cited_src[s]}x) but not found in knowledge-docs")

# ---------------------------------------------------------------- 10. calendar
print("\n=== 10. CALENDAR ===")
for d in [6, 13, 20, 27]:
    dt = datetime.date(2027, 6, d)
    print(f"  {dt.isoformat()} weekday={dt.strftime('%A')}")
print("  2027-06-30 weekday:", datetime.date(2027, 6, 30).strftime("%A"))
print("  2027-05-31 weekday:", datetime.date(2027, 5, 31).strftime("%A"))

print("\nFINDINGS:", len(findings), dict(Counter(f[0] for f in findings)))
