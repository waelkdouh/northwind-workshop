#!/usr/bin/env python3
"""Build the read-only Azure DevOps publication payload from docs/product/backlog.md.

Input : docs/product/backlog.md (BACKLOG-NW-001), docs/product/releases/*.md
Output: ado-publish-payload.json (next to this script)

Nothing here talks to Azure DevOps. The text of every item is copied from the
backlog; nothing is retyped. Run:  python3 build_ado_payload.py
Exit code 0 only when every verification check passes.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BACKLOG = os.path.join(ROOT, "docs", "product", "backlog.md")
REL_DIR = os.path.join(ROOT, "docs", "product", "releases")
OUT = os.path.join(HERE, "ado-publish-payload.json")

ORG = "waelconsulting"
PROJECT = "northwind-workshop"
PREFIX = "wael-01"
BASE_TAG = "nw-workshop"
DOC_BASE = "https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/"
DOCS = {
    "brd": ("business-requirements.md", "Business requirements (BRD-NW-001)"),
    "prd": ("product-requirements.md", "Product requirements (PRD-NW-001)"),
    "exp": ("experiments.md", "Experiment designs (MVE-01 to MVE-03)"),
    "backlog": ("backlog.md", "Backlog (BACKLOG-NW-001)"),
    "trace": ("traceability.md", "Traceability (TRACE-NW-001)"),
}

ITEM_ID = r"(?:EPIC|FEAT|STORY)-\d+|E[ANP]-\d+"
HEAD_RE = re.compile(r"^(#{4,6}) (%s) (.+?)\s*$" % ITEM_ID)
AC_RE = re.compile(r"^\s+\* `([A-Z0-9-]+/AC\d+)` (.+?)\s*$")
BULLET_RE = re.compile(r"^\* (.*)$")
SEG_RE = re.compile(r"(?:^|\s·\s)\*\*([^*]+?):\*\*\s*")
SRC_TOKEN_RE = re.compile(r"\b(?:BR|NFR|C|SM|CS|ES|FR|OQ)-\d+\b")
REF_RE = re.compile(r"(?<![-\w])(?:[AOXTG]-\d+|MVE-[AO]-\d+|[AO]-D\d-\d+|AZ\d-O\d+)\b")
REG_KEY_RE = re.compile(r"^(?:[AOXTG]-\d+|MVE-[AO]-\d+|[AO]-D\d-\d+|AZ\d-O\d+)$")


def slug(text):
    """GitHub heading anchor."""
    s = re.sub(r"[^a-z0-9 _-]", "", text.strip().lower())
    return s.replace(" ", "-")


def md2html(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)


def split_segments(rest):
    marks = list(SEG_RE.finditer(rest))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(rest)
        out.append((m.group(1).strip(), rest[m.end():end].strip()))
    return out


def parse_registers(lines):
    reg = {}
    in7 = False
    for ln in lines:
        if ln.startswith("## 7."):
            in7 = True
        if not in7 or not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        keys = [k.strip() for k in cells[0].replace("*", "").split(",")]
        if not all(REG_KEY_RE.match(k) for k in keys):
            continue
        if len(cells) >= 4:
            text = "%s (%s)" % (cells[1], cells[2]) if cells[0].startswith("X-") else cells[2]
            owner = cells[3]
        else:
            text, owner = cells[1], cells[2]
        text = re.sub(r"^\*\*New\.\*\*\s*", "", text)
        for k in keys:
            reg[k] = {"text": text, "owner": owner}
    return reg


def table_rows(lines, start, end):
    rows, on = [], False
    for ln in lines:
        if ln.startswith(start):
            on = True
            continue
        if on and ln.startswith(end):
            break
        if on and ln.startswith("| ") and not ln.startswith(("| Id", "| Item id")):
            rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
    return rows


def parse_items(lines):
    s = next(i for i, l in enumerate(lines) if l.startswith("## 4. Items by track"))
    e = next(i for i, l in enumerate(lines) if l.startswith("## 5. Unplanned items"))
    heads = [(i, HEAD_RE.match(lines[i])) for i in range(s, e) if HEAD_RE.match(lines[i])]
    items, unclassified = [], []
    for n, (i, m) in enumerate(heads):
        stop = heads[n + 1][0] if n + 1 < len(heads) else e
        it = {"localId": m.group(2), "heading": m.group(3), "fields": {}, "ac": [], "tags": []}
        for ln in lines[i + 1:stop]:
            if not ln.strip() or ln.strip() == "---":
                continue
            if ln.startswith("### 4."):  # track heading and its intro sentence end the previous block
                break
            a = AC_RE.match(ln)
            if a:
                it["ac"].append({"id": a.group(1), "text": a.group(2)})
                continue
            b = BULLET_RE.match(ln)
            segs = split_segments(b.group(1)) if b else []
            if not segs:
                unclassified.append((it["localId"], ln))
                continue
            for k, v in segs:
                if k == "Tags":
                    it["tags"] = re.findall(r"`([^`]+)`", v)
                else:
                    it["fields"][k] = v
        items.append(it)
    return items, unclassified


def build():
    lines = open(BACKLOG, encoding="utf-8").read().split("\n")
    reg = parse_registers(lines)
    items, unclassified = parse_items(lines)
    reg2 = {}
    for r in table_rows(lines, "## 2. Item register", "## 3. Counts"):
        if len(r) >= 7 and re.match("^(%s)$" % ITEM_ID, r[0]):
            reg2[r[0]] = {"type": r[1], "title": r[2], "track": r[3].strip("`"),
                          "release": r[4].strip("`"), "priority": r[5], "rank": r[6]}
    pub = {}
    for r in table_rows(lines, "### 6.2 Published titles", "## 7."):
        if len(r) >= 3 and re.match("^(%s)$" % ITEM_ID, r[0]):
            pub[r[0]] = {"title": r[1], "tags": [t.strip().strip("`") for t in r[2].split(",")]}
    rel_ids = {}
    for fn in sorted(os.listdir(REL_DIR)):
        if fn.endswith(".md"):
            txt = open(os.path.join(REL_DIR, fn), encoding="utf-8").read()
            rel_ids[fn[:-3]] = set(re.findall(r"\b(?:%s)\b" % ITEM_ID, txt))

    records = []
    for it in items:
        iid, f, tags = it["localId"], it["fields"], it["tags"]
        track = next((t for t in tags if t.startswith("track-")), None)
        release = next((t for t in tags if re.match(r"^(azure|dotnet)-r\d+$", t)), None)
        if iid.startswith("EPIC-"):
            btype, ado_type = "epic", "Epic"
        elif iid.startswith("FEAT-"):
            btype, ado_type = "feature", "Feature"
        elif iid.startswith("STORY-"):
            btype, ado_type = "story", "User Story"
        else:
            btype, ado_type = "enabler", "User Story"
        parent = f.get("Parent")
        prio_raw = f.get("Priority", "")
        prio = prio_raw.split()[0].strip("(),.") if prio_raw else ""
        rank = int(f["Rank"]) if f.get("Rank", "").strip().isdigit() else None
        source_md, gate_md = f.get("Source", ""), f.get("Gate", "")
        story_md, goal_md = f.get("Story", ""), f.get("Goal", "")
        dep_md, cross_md = f.get("Dependencies", ""), f.get("Cross-track (OPEN)", "")
        contains = f.get("Contains") or f.get("Features") or ""
        serves = f.get("Serves") or f.get("Implements") or ""
        covers = f.get("Covers", "")
        all_src = sorted(set(SRC_TOKEN_RE.findall(source_md) + SRC_TOKEN_RE.findall(serves) + SRC_TOKEN_RE.findall(covers)))
        ref_text = " ".join([source_md, gate_md, dep_md, cross_md, story_md, goal_md] + [a["text"] for a in it["ac"]])
        refs = sorted(set(REF_RE.findall(ref_text)), key=lambda x: (re.sub(r"[\d-]+$", "", x), [int(n) for n in re.findall(r"\d+", x)]))
        refs_ok = [(r, reg[r]) for r in refs if r in reg]
        refs_bad = [r for r in refs if r not in reg]

        # description as a list of blocks: ("p", text) or ("ul", [text, ...])
        blocks = [("p", "**%s** (BACKLOG-NW-001) · **Source ids:** %s" % (iid, ", ".join(all_src) if all_src else "none")),
                  ("p", "**Source:** %s" % source_md)]
        if serves or covers:
            parts = []
            if serves:
                parts.append("**%s:** %s" % ("Serves" if iid[:2] in ("EA", "EN", "EP") else "Implements", serves))
            if covers:
                parts.append("**Covers:** %s" % covers)
            blocks.append(("p", " · ".join(parts)))
        if story_md:
            blocks.append(("p", "**Story:** %s" % story_md))
        if goal_md:
            blocks.append(("p", "**Goal:** %s" % goal_md))
        if contains:
            blocks.append(("p", "**%s:** %s" % ("Features" if btype == "epic" else "Contains", contains)))
        marks = []
        if dep_md:
            marks.append("**Dependencies:** %s" % dep_md)
        if cross_md:
            marks.append("**Cross-track (OPEN):** %s" % cross_md)
        if marks:
            blocks.append(("p", "**ASSUMPTION / OPEN markers (as written in the backlog):**"))
            blocks.append(("ul", marks))
        if refs_ok:
            blocks.append(("p", "**Register text for the ids cited in this item (backlog section 7):**"))
            blocks.append(("ul", ["**%s** %s (owner: %s)" % (r, v["text"], v["owner"]) for r, v in refs_ok]))
        blocks.append(("p", "**Gate:** %s" % (gate_md if gate_md else "none")))
        meta = ["**Track tag:** %s" % track, "**Release tag:** %s" % (release or "none (unplanned)"),
                "**Type:** %s" % btype, "**Priority:** %s" % (prio_raw or "not set")]
        if rank is not None:
            meta.append("**Rank:** %d" % rank)
        meta.append("**Parent:** %s" % (parent or "none"))
        blocks.append(("p", " · ".join(meta)))

        md_parts, html_parts = [], []
        for kind, val in blocks:
            if kind == "p":
                md_parts.append(val)
                html_parts.append("<p>%s</p>" % md2html(val))
            else:
                md_parts.append("\n".join("* " + x for x in val))
                html_parts.append("<ul>%s</ul>" % "".join("<li>%s</li>" % md2html(x) for x in val))
        desc_md, desc_html = "\n\n".join(md_parts), "".join(html_parts)
        ac_html = ("<ul>%s</ul>" % "".join("<li><b>%s</b> %s</li>" % (html.escape(a["id"]), md2html(a["text"])) for a in it["ac"])) if it["ac"] else ""
        fallback = desc_html + ("<h3>Acceptance criteria</h3>" + ac_html if ac_html else "")

        gated = bool(re.search(r"MVE-0\d", gate_md))
        anchor = slug("%s %s" % (iid, it["heading"]))
        links = []

        def add(key, why, frag=""):
            fn, label = DOCS[key]
            links.append({"url": DOC_BASE + fn + frag, "comment": "%s: %s" % (label, why), "doc": key})
        br_nfr = [x for x in all_src if x.startswith(("BR-", "NFR-"))]
        if btype == "epic":
            add("brd", "business requirements, goals and constraints behind this epic")
            add("prd", "product requirements, journeys and release placement")
        elif btype == "feature":
            add("prd", "product requirements covered by this feature")
        else:
            add("prd", "product functional requirement %s" % (serves or "implemented here"))
            if br_nfr:
                add("brd", "business and quality requirements cited in the source line (%s)" % ", ".join(br_nfr))
            add("trace", "requirement-to-story traceability (ES-06)")
        if release:
            links.append({"url": DOC_BASE + "releases/%s.md" % release,
                          "comment": "Release file %s: scope, exit criteria and OPEN dependencies" % release, "doc": "release"})
        if gated:
            add("exp", "experiment gate %s: decision before this item is committed; no result yet" % re.search(r"MVE-0\d", gate_md).group(0))
        add("backlog", "this item with its full text", "#" + anchor)

        tag_list = [BASE_TAG] + ([track] if track else []) + ([release] if release else [])
        records.append({
            "localId": iid, "backlogType": btype, "adoWorkItemType": ado_type, "adoTypeNeedsReview": True,
            "title": "%s %s %s" % (PREFIX, iid, it["heading"]),
            "tags": "; ".join(tag_list), "tagList": tag_list, "track": track, "release": release,
            "parentLocalId": parent, "priority": prio or None, "priorityRaw": prio_raw or None,
            "adoPriorityProposed": {"Must": 1, "Should": 2, "Could": 3}.get(prio), "rank": rank,
            "sourceIds": all_src, "serves": serves or None, "covers": covers or None,
            "gate": gate_md or None, "gated": gated, "contains": contains or None,
            "descriptionMarkdown": desc_md, "descriptionHtml": desc_html,
            "acceptanceCriteria": it["ac"], "acceptanceCriteriaHtml": ac_html,
            "descriptionWithAcceptanceCriteriaHtmlFallback": fallback,
            "hyperlinks": links, "citedRegisterIds": refs, "unresolvedRegisterIds": refs_bad,
            "needsReview": ["work item type, fields and parent link not validated in the project (ADO read tools unavailable)"],
            "_heading": it["heading"],
        })

    planned = [r for r in records if r["release"]]
    unplanned = [r for r in records if not r["release"]]
    rank_of_type = {"epic": 0, "feature": 1, "story": 2, "enabler": 2}
    for lst in (planned, unplanned):
        for pos, r in enumerate(lst):
            r["_doc"] = pos
        lst.sort(key=lambda r: (rank_of_type[r["backlogType"]], r["_doc"]))
        for pos, r in enumerate(lst, 1):
            r["operationOrder"] = pos
            del r["_doc"]

    v = {"results": [], "failures": []}

    def check(name, ok, detail=""):
        v["results"].append({"check": name, "ok": bool(ok), "detail": detail})
        if not ok:
            v["failures"].append("%s: %s" % (name, detail))

    by_id = {r["localId"]: r for r in records}
    check("no id is duplicated", len(by_id) == len(records), "%d records, %d unique ids" % (len(records), len(by_id)))
    check("every line of every item block was recognised by the parser", not unclassified, "%d unrecognised: %s" % (len(unclassified), unclassified[:3]))
    check("144 items parsed and equal to the item register (section 2)", len(records) == 144 == len(reg2) and set(by_id) == set(reg2), "parsed %d, register %d" % (len(records), len(reg2)))
    expected = {("azure-r1", "track-azure"): (2, 5, 8, 6), ("azure-r2", "track-azure"): (1, 5, 7, 7), ("azure-r3", "track-azure"): (1, 4, 5, 3),
                ("dotnet-r1", "track-dotnet"): (1, 5, 6, 11), ("dotnet-r2", "track-dotnet"): (1, 5, 14, 1), ("dotnet-r3", "track-dotnet"): (1, 4, 6, 2),
                ("unplanned", "track-dotnet"): (1, 1, 1, 0), ("unplanned", "track-power-platform"): (4, 10, 10, 6)}
    ok, det = True, []
    for (rel, trk), exp in expected.items():
        got = tuple(sum(1 for r in records if (r["release"] or "unplanned") == rel and r["track"] == trk and r["backlogType"] == t) for t in ("epic", "feature", "story", "enabler"))
        det.append("%s/%s epics,features,stories,enablers=%s" % (rel, trk, got))
        ok = ok and got == exp
    check("counts per track/release/type equal backlog section 3", ok, "; ".join(det))
    check("planned = 111 (azure 54, dotnet 57)", len(planned) == 111 and sum(r["track"] == "track-azure" for r in planned) == 54 and sum(r["track"] == "track-dotnet" for r in planned) == 57, "planned %d" % len(planned))
    check("unplanned = 33 (power platform 30, .NET 3 incl. EPIC-204)", len(unplanned) == 33 and sum(r["track"] == "track-power-platform" for r in unplanned) == 30 and sum(r["track"] == "track-dotnet" for r in unplanned) == 3 and "EPIC-204" in {r["localId"] for r in unplanned}, "unplanned %d" % len(unplanned))
    for lst, name in ((planned, "planned"), (unplanned, "unplanned")):
        bad = []
        for r in lst:
            tl = r["tagList"]
            nt = [t for t in tl if t.startswith("track-")]
            nr = [t for t in tl if re.match(r"^(azure|dotnet)-r\d+$", t)]
            if tl[0] != BASE_TAG or len(nt) != 1 or len(nr) > 1 or (name == "planned") != (len(nr) == 1) or len(tl) != 1 + len(nt) + len(nr):
                bad.append(r["localId"])
            if nr and nr[0].split("-")[0] != nt[0].split("-")[1]:
                bad.append(r["localId"] + " release/track mismatch")
        check("%s: nw-workshop + exactly one track tag + %s" % (name, "exactly one release tag" if name == "planned" else "no release tag"), not bad, str(bad))
    check("every title starts with 'wael-01 '", all(r["title"].startswith(PREFIX + " ") for r in records))
    check("title lengths", max(len(r["title"]) for r in records) <= 255, "longest published title %d chars (ADO limit 255); longest backlog title %d (BD-04 limit 100)" % (max(len(r["title"]) for r in records), max(len(r["_heading"]) for r in records)))
    check("title = 'wael-01 ' + published title of backlog section 6.2", all(r["title"] == PREFIX + " " + pub.get(r["localId"], {}).get("title", "<missing>") for r in records))
    check("tags = nw-workshop + tags of backlog section 6.2", all(pub.get(r["localId"], {}).get("tags") == r["tagList"][1:] for r in records))
    bad = []
    for r in records:
        g = reg2[r["localId"]]
        if g["track"] != r["track"] or g["release"] != (r["release"] or "unplanned"):
            bad.append(r["localId"] + " tags %s/%s" % (g["track"], g["release"]))
        if g["title"] != r["_heading"]:
            bad.append(r["localId"] + " title")
        if g["priority"].split()[0] != (r["priority"] or ""):
            bad.append(r["localId"] + " priority %s vs %s" % (g["priority"], r["priority"]))
        if (r["rank"] is None) != (g["rank"] in ("—", "-", "")) or (r["rank"] is not None and str(r["rank"]) != g["rank"]):
            bad.append(r["localId"] + " rank")
    check("block fields (title, tags, priority, rank) equal item register of section 2", not bad, str(bad[:8]))
    check("every description begins with the item id and contains source ids", all(r["sourceIds"] and r["descriptionMarkdown"].startswith("**%s** " % r["localId"]) for r in records), str([r["localId"] for r in records if not r["sourceIds"]]))
    check("every description carries the '(source: ...)' cite (ES-02, ES-29)", all("**Source:** (source:" in r["descriptionMarkdown"] for r in records))
    short = [r["localId"] for r in records if r["backlogType"] in ("story", "enabler") and len(r["acceptanceCriteria"]) < 2]
    check("every story and enabler has >= 2 acceptance criteria", not short, str(short))
    badac = []
    for r in records:
        for n, a in enumerate(r["acceptanceCriteria"], 1):
            if a["id"] != "%s/AC%d" % (r["localId"], n) or not re.search(r"Given .+ When .+ Then ", a["text"].replace("**", "")):
                badac.append(a["id"])
    check("every criterion id is '<item id>/AC<n>' (contiguous) and in Given/When/Then form", not badac, str(badac[:10]))
    check("epics and features carry no acceptance criteria in the backlog", all(not r["acceptanceCriteria"] for r in records if r["backlogType"] in ("epic", "feature")))
    bad = []
    for r in records:
        p = r["parentLocalId"]
        if r["backlogType"] == "epic":
            if p:
                bad.append(r["localId"] + " epic has a parent")
            continue
        if p not in by_id:
            bad.append("%s parent %s missing" % (r["localId"], p))
            continue
        pt = by_id[p]["backlogType"]
        if (r["backlogType"] == "feature") != (pt == "epic") or (r["backlogType"] in ("story", "enabler") and pt != "feature"):
            bad.append(r["localId"] + " wrong parent type")
        if by_id[p]["release"] != r["release"] or by_id[p]["track"] != r["track"]:
            bad.append(r["localId"] + " parent differs in track or release")
    check("every parent exists, has the right level, and shares track and release", not bad, str(bad))
    bad = []
    for r in records:
        if r["contains"]:
            kids = set(re.findall(r"\b(?:%s)\b" % ITEM_ID, r["contains"]))
            actual = {k["localId"] for k in records if k["parentLocalId"] == r["localId"]}
            if kids != actual:
                bad.append("%s differs by %s" % (r["localId"], sorted(kids ^ actual)))
    check("Contains/Features lists equal the children found by Parent", not bad, str(bad))
    miss = [r["localId"] for r in planned if r["localId"] not in rel_ids.get(r["release"], set())]
    check("every planned item id is named in its release file", not miss, "missing: %s" % miss)
    pos = {r["localId"]: r["operationOrder"] for r in planned}
    check("operation order creates every parent before its children", all(pos[r["parentLocalId"]] < pos[r["localId"]] for r in planned if r["parentLocalId"]))
    bad = []
    for r in records:
        blob = r["descriptionMarkdown"] + " " + " ".join(a["text"] for a in r["acceptanceCriteria"])
        if re.search(r"(?<![\w&])#\d+\b|(?<![\w.])@\w+|!\[|https?://", blob):
            bad.append(r["localId"] + " markup")
        if ".copilot-tracking" in blob or re.search(r"\bWI-?\d{3}\b|\{\{[A-Z-]*TEMP", blob):
            bad.append(r["localId"] + " local path or planning id")
    check("Guards 1, 2, 3, 5: no #nnn references, @mentions, images or URLs, .copilot-tracking paths, planning ids or template placeholders in outbound text", not bad, str(bad))
    bad = []
    for r in records:
        blob = r["descriptionMarkdown"] + " " + " ".join(a["text"] for a in r["acceptanceCriteria"])
        if re.search(r"(?i)\b(password|passwd|pwd|secret|token|api[_-]?key|client_secret|connectionstring)\s*[=:]\s*\S", blob) or re.search(r"BEGIN [A-Z ]*PRIVATE KEY|AccountKey=|Authorization:|sig=[A-Za-z0-9%]{8,}|://[^/\s:@]+:[^/\s@]+@", blob):
            bad.append(r["localId"])
    check("Guard 6: no secret or credential indicator in outbound text", not bad, str(bad))
    check("every cited A-/O-/X-/T-/G- id resolves in backlog section 7", all(not r["unresolvedRegisterIds"] for r in records), str({r["localId"]: r["unresolvedRegisterIds"] for r in records if r["unresolvedRegisterIds"]}))
    for r in records:
        del r["_heading"]

    payload = {
        "payloadId": "ADO-PUBLISH-PREVIEW-NW-001",
        "generatedFrom": "docs/product/backlog.md (BACKLOG-NW-001, version 0.1.0, status draft)",
        "generator": "build_ado_payload.py",
        "mode": "READ-ONLY PREVIEW. Nothing has been created in Azure DevOps.",
        "target": {"organization": ORG, "project": PROJECT, "participantPrefix": PREFIX, "baseTag": BASE_TAG,
                   "docBaseUrl": DOC_BASE, "validated": False,
                   "validationNote": "The ado-remote-mcp tools could not be called in this session. Project, process, work item types and fields are needs_review."},
        "fieldMapping": {
            "title": "System.Title", "tags": "System.Tags (semicolon separated)",
            "description": "System.Description (HTML, descriptionHtml)",
            "acceptanceCriteria": "Microsoft.VSTS.Common.AcceptanceCriteria (HTML, acceptanceCriteriaHtml; User Story only). If the field is not available, use descriptionWithAcceptanceCriteriaHtmlFallback as System.Description.",
            "priority": "Microsoft.VSTS.Common.Priority (proposed Must=1, Should=2, Could=3; needs_review)",
            "rank": "Microsoft.VSTS.Common.StackRank (optional; rank is per track in the backlog; needs_review). Rank is also in the description.",
            "parent": "System.LinkTypes.Hierarchy-Reverse, added after both items exist",
            "hyperlinks": "Hyperlink relation, url + comment"},
        "verification": v,
        "counts": {
            "planned": len(planned), "unplanned": len(unplanned),
            "plannedByAdoType": {t: sum(1 for r in planned if r["adoWorkItemType"] == t) for t in ("Epic", "Feature", "User Story")},
            "hyperlinksPlanned": sum(len(r["hyperlinks"]) for r in planned),
            "hyperlinksUnplanned": sum(len(r["hyperlinks"]) for r in unplanned)},
        "workItems": planned,
        "optionalAddOnUnplanned": {"inScope": False, "note": "Decision for the user. These items would carry only nw-workshop and the track tag, no release tag.", "workItems": unplanned},
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", OUT)
    for r in v["results"]:
        print(("PASS " if r["ok"] else "FAIL ") + r["check"] + ((" | " + r["detail"]) if r["detail"] and len(r["detail"]) < 400 else ""))
    return 0 if not v["failures"] else 1


if __name__ == "__main__":
    sys.exit(build())
