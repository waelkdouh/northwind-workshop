#!/usr/bin/env python3
"""Render ado-publish-preview.md from ado-publish-payload.json (and the backlog registers).

Read-only: it only reads the payload and writes one Markdown file next to itself.
Run build_ado_payload.py first, then:  python3 build_ado_preview.py
"""
import json
import os
import re
import sys
from collections import Counter, OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_ado_payload as B

HERE = os.path.dirname(os.path.abspath(__file__))
payload = json.load(open(os.path.join(HERE, "ado-publish-payload.json"), encoding="utf-8"))
items = payload["workItems"]
addon = payload["optionalAddOnUnplanned"]["workItems"]
reg = B.parse_registers(open(B.BACKLOG, encoding="utf-8").read().split("\n"))
by_id = {i["localId"]: i for i in items}
SHORT = {"brd": "BRD", "prd": "PRD", "exp": "EXP", "trace": "TRC", "release": "REL", "backlog": "BKL"}

out = []
w = out.append


def esc(t):
    return t.replace("|", "\\|")


def tcount(lst, rel, typ):
    return sum(1 for i in lst if i["release"] == rel and i["adoWorkItemType"] == typ)


def enablers(lst, rel):
    return sum(1 for i in lst if i["release"] == rel and i["backlogType"] == "enabler")


v = payload["verification"]
n_epic = payload["counts"]["plannedByAdoType"]["Epic"]
n_feat = payload["counts"]["plannedByAdoType"]["Feature"]
n_story = payload["counts"]["plannedByAdoType"]["User Story"]
n_links = payload["counts"]["hyperlinksPlanned"]
n_ac = sum(len(i["acceptanceCriteria"]) for i in items)
n_parent = sum(1 for i in items if i["parentLocalId"])
rels = ["azure-r1", "azure-r2", "azure-r3", "dotnet-r1", "dotnet-r2", "dotnet-r3"]

w("<!-- markdownlint-disable-file -->")
w("# Azure DevOps publication preview: Northwind Traders releases (READ-ONLY)\n")
w("> **Nothing has been created, updated or linked in Azure DevOps.** This is a preview. It needs your approval before any write (section I).")
w("> Source: `docs/product/backlog.md` (BACKLOG-NW-001 v0.1.0), the six release files and `traceability.md`, copied by `build_ado_payload.py`.")
w("> Machine-readable twin: `ado-publish-payload.json` (same folder). Date of this preview: 2026-11-17.\n")

# ------------------------------------------------------------------ A
w("## A. Target and scope summary\n")
w("| Field | Value |\n|---|---|")
w("| Organization / project | `waelconsulting` / `northwind-workshop` (**needs_review**: not verified, see section F) |")
w("| Participant prefix (ES-28) | `wael-01`. Every title starts with `wael-01 ` |")
w("| Tags on every item (ES-28, ES-30, ES-31, ES-39) | `nw-workshop`, exactly one track tag, and exactly one release tag when the item is planned in a release |")
w("| Scope | The %d items planned in the six releases: %d epics, %d features, %d user stories (of which %d are enablers `EA-`/`EN-`, published as User Story per backlog section 6.1) |" % (len(items), n_epic, n_feat, n_story, sum(1 for i in items if i['backlogType'] == 'enabler')))
w("| Out of scope (optional add-on, section G) | %d unplanned items: 30 Power Platform and 3 .NET (`EPIC-204`, `FEAT-215`, `STORY-280`) |" % len(addon))
w("| Acceptance criteria | %d criteria on %d stories and enablers. Epics and features have none in the backlog |" % (n_ac, n_story))
w("| Hyperlinks | %d link operations (average %.1f per item), section E |" % (n_links, n_links / len(items)))
w("| Git evidence | The six tags `product/azure-r1` to `product/dotnet-r3` exist on `origin` and point to commit `5ad7971`. `docs/` and `knowledge-docs/` have not changed since that commit. `origin/main` equals local `HEAD` (`e56447b`) |")
w("| Documentation base URL | `https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/<file>` |\n")
w("### Counts by track, release and type\n")
w("| Track | Release | Epics | Features | User Stories | of which enablers | Total |\n|---|---|---|---|---|---|---|")
tot = [0, 0, 0, 0]
for rel in rels:
    e, f, s, en = tcount(items, rel, "Epic"), tcount(items, rel, "Feature"), tcount(items, rel, "User Story"), enablers(items, rel)
    tot = [tot[0] + e, tot[1] + f, tot[2] + s, tot[3] + en]
    w("| %s | `%s` | %d | %d | %d | %d | %d |" % ("Azure" if rel.startswith("azure") else ".NET", rel, e, f, s, en, e + f + s))
    if rel in ("azure-r3", "dotnet-r3"):
        sub = [i for i in items if i["release"].startswith(rel.split("-")[0])]
        w("| **%s total** | | **%d** | **%d** | **%d** | **%d** | **%d** |" % (
            "Azure" if rel.startswith("azure") else ".NET",
            sum(1 for i in sub if i["adoWorkItemType"] == "Epic"), sum(1 for i in sub if i["adoWorkItemType"] == "Feature"),
            sum(1 for i in sub if i["adoWorkItemType"] == "User Story"), sum(1 for i in sub if i["backlogType"] == "enabler"), len(sub)))
w("| **All planned** | | **%d** | **%d** | **%d** | **%d** | **%d** |\n" % (tot[0], tot[1], tot[2], tot[3], tot[0] + tot[1] + tot[2]))
w("These counts equal backlog section 3 (Azure 54 = 21 + 20 + 13; .NET planned 57 = 23 + 21 + 13). The backlog has 144 items in total: 111 planned plus 33 unplanned.\n")
w("### Checks run on the payload by the script (all must pass)\n")
w("| Result | Check | Detail |\n|---|---|---|")
for r in v["results"]:
    w("| %s | %s | %s |" % ("PASS" if r["ok"] else "**FAIL**", esc(r["check"]), esc(r["detail"])[:300]))
w("")

# ------------------------------------------------------------------ B
w("## B. Proposed operations, in order\n")
w("Tool names below are the ones the Azure DevOps remote MCP server normally offers. **needs_review:** the server `ado-remote-mcp` is declared in `.mcp.json`, but none of its tools could be called in this session (section F), so names and parameters are not confirmed. No call below has been made.\n")
w("| Step | Operation | Tool (needs_review) | Calls | Notes |\n|---|---|---|---|---|")
w("| 0 | Read-only checks before any write: project, process, work item types, fields, duplicates, tag permission | `core_list_projects`, `wit_get_work_item_type`, `wit_query`, `search_workitem` | about 6 to 10 reads | Section F lists each check. Stop if one fails. |")
w("| 1 | Create the %d epics (type `Epic`) with title, tags, description, priority | `wit_create_work_item` | %d | Parents first. One call per item. No parent. Record each returned id against its `localId`. |" % (n_epic, n_epic))
w("| 2 | Create the %d features (type `Feature`) | `wit_create_work_item` | %d | Then link each feature to its epic (step 2b). |" % (n_feat, n_feat))
w("| 2b | Parent link feature to epic | `wit_work_items_link` (type `parent`) | %d link operations (1 call per batch if the tool accepts a list; else %d calls) | One hierarchical parent per item (ES-30 splits cross-track stories, so no feature needs a second parent). |" % (n_feat, n_feat))
w("| 3 | Create the %d user stories (backlog stories and enablers, type `User Story`) with `Microsoft.VSTS.Common.AcceptanceCriteria` | `wit_create_work_item` | %d | Then link each story to its feature (step 3b). |" % (n_story, n_story))
w("| 3b | Parent link story to feature | `wit_work_items_link` (type `parent`) | %d link operations (batched or one call each) | |" % n_story)
w("| 4 | Add the %d documentation hyperlinks (Hyperlink relation with a comment) | `wit_update_work_item` (add `/relations/-`, `rel: Hyperlink`) or `wit_update_work_items_batch` | %d (one per item) or fewer when batched | Section E gives the URL and comment per item. |" % (n_links, len(items)))
w("| 5 | Read back every created item and compare title, tags, parent and field text with the payload | `wit_get_work_items_batch_by_ids` | about 5 to 12 reads | Report any difference. Nothing is fixed without a new approval. |")
w("")
w("**Totals if nothing is batched:** %d creates + %d parent links + %d hyperlink updates = **%d write calls**, plus reads. Batching can lower the link and hyperlink calls. The order is fixed: epics, then features, then stories, then hyperlinks. A parent is always created before its child (checked: yes).\n" % (len(items), n_parent, len(items), len(items) + n_parent + len(items)))
w("Fields written per item (all **needs_review** until section F is done): `System.Title`, `System.Tags` (semicolon separated), `System.Description` (HTML), `Microsoft.VSTS.Common.Priority` (proposed Must=1, Should=2, Could=3), and for User Stories `Microsoft.VSTS.Common.AcceptanceCriteria` (HTML). If that field does not exist on the type, the criteria move into the description (payload field `descriptionWithAcceptanceCriteriaHtmlFallback`). `Microsoft.VSTS.Common.StackRank` is **not** proposed by default (see risk R5).\n")
w("Content guards (backlog-management skill) applied to every outbound text: no `.copilot-tracking/` paths, no planning reference ids (`WI001`), no `{{TEMP-n}}` placeholders, no `#nnn` references, `@` mentions, images or URLs inside descriptions, no secret indicators. The backlog ids (`EPIC-101`, `STORY-104`, `EA-01`) stay because you asked for them (ES-29). All checks passed (section A).\n")

# ------------------------------------------------------------------ C
w("## C. All %d items\n" % len(items))
w("Doc link codes: **BRD** business requirements, **PRD** product requirements, **EXP** experiments, **TRC** traceability, **REL** release file, **BKL** backlog entry (anchor). Full URLs are in section E.\n")
w("| # | localId | ADO type | Exact title | Tags | Parent | Release | Doc links |\n|---|---|---|---|---|---|---|---|")
for i in items:
    w("| %d | `%s` | %s%s | %s | `%s` | %s | `%s` | %s |" % (
        i["operationOrder"], i["localId"], i["adoWorkItemType"], " (enabler)" if i["backlogType"] == "enabler" else "",
        esc(i["title"]), i["tags"], ("`%s`" % i["parentLocalId"]) if i["parentLocalId"] else "none", i["release"],
        " ".join(SHORT[h["doc"]] for h in i["hyperlinks"])))
w("")

# ------------------------------------------------------------------ D
w("## D. Exact description and acceptance criteria of every item\n")
w("Text is copied by the script from the backlog and shown as Markdown. The payload holds the same text as HTML. Item order is the creation order. Each description starts with the item id and the source ids (ES-02, ES-29), then the story or goal, the ASSUMPTION and OPEN markers with their register text, and the gate.\n")
for i in items:
    w("### %d. %s\n" % (i["operationOrder"], i["title"]))
    w("* **Type:** %s (backlog type: %s) · **Tags:** `%s` · **Parent:** %s · **Priority:** %s (proposed ADO priority %s)%s\n" % (
        i["adoWorkItemType"], i["backlogType"], i["tags"], i["parentLocalId"] or "none", i["priority"], i["adoPriorityProposed"],
        (" · **Rank:** %d" % i["rank"]) if i["rank"] else ""))
    w("**Description**\n")
    w(i["descriptionMarkdown"] + "\n")
    if i["acceptanceCriteria"]:
        w("**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)\n")
        for a in i["acceptanceCriteria"]:
            w("* **%s** %s" % (a["id"], a["text"]))
        w("")
    else:
        w("**Acceptance criteria:** none in the backlog for %s %s.\n" % ("an" if i["backlogType"] == "epic" else "a", i["backlogType"]))

# ------------------------------------------------------------------ E
w("## E. Documentation links and why\n")
w("All URLs start with `%s`. They point at `main`. The six release tags point at the same commit, and the files have not changed since.\n" % payload["target"]["docBaseUrl"])
w("| Item level | Linked documents | Why |\n|---|---|---|")
w("| Epic | BRD, PRD, REL, BKL, and EXP when gated | The epic is the outcome, so it links the business case behind it (BRD), the product requirement (PRD) and the release that plans it. |")
w("| Feature | PRD, REL, BKL, and EXP when gated | A feature groups stories that implement product requirements. |")
w("| Story and enabler | PRD, TRC, REL, BKL, and EXP when gated; BRD when the source line cites a `BR-` or `NFR-` | The story implements an `FR-` (PRD), is proven covered in the traceability table (ES-06), and sits in a release. Enablers that cite only `CS-`, `ES-` or `C-` get no BRD link. |")
w("| Gated item (`Gate: MVE-nn`) | EXP | The experiment decision comes before the item is committed. No result exists yet. |")
w("| BKL | `backlog.md#<item heading>` | The anchor is built from the heading, so the link opens the item itself. |")
w("")
w("### Link counts by document\n")
cnt = Counter(h["doc"] for i in items for h in i["hyperlinks"])
w("| Document | Items linked | Link operations |\n|---|---|---|")
names = OrderedDict([("brd", "business-requirements.md"), ("prd", "product-requirements.md"), ("exp", "experiments.md"), ("trace", "traceability.md"), ("backlog", "backlog.md (with anchor)"), ("release", "releases/<release>.md")])
for k, n in names.items():
    w("| %s (%s) | %d | %d |" % (n, SHORT[k], sum(1 for i in items if any(h["doc"] == k for h in i["hyperlinks"])), cnt[k]))
w("| **Total** | | **%d** |\n" % sum(cnt.values()))
gated = [i for i in items if i["gated"]]
w("### Items that link `experiments.md` (%d)\n" % len(gated))
w(", ".join("`%s`" % i["localId"] for i in gated) + "\n")
w("Gates on the planned items are all `MVE-01` (Azure) and `MVE-02` (.NET). `MVE-03` gates only unplanned Power Platform items.\n")
w("### Items without a BRD link\n")
nb = [i["localId"] for i in items if not any(h["doc"] == "brd" for h in i["hyperlinks"])]
w("%d items: features (all %d) and stories or enablers with no `BR-` or `NFR-` in their source line: %s\n" % (len(nb), n_feat, ", ".join("`%s`" % x for x in nb if not x.startswith("FEAT-"))))
w("### Full link list per item (URL and comment)\n")
w("| localId | URL | Comment |\n|---|---|---|")
for i in items:
    for h in i["hyperlinks"]:
        w("| `%s` | %s | %s |" % (i["localId"], h["url"], esc(h["comment"])))
w("")

# ------------------------------------------------------------------ F
w("## F. Read-only Azure DevOps checks\n")
w("**Result: none of the checks could be run. All affected fields are `needs_review`.**\n")
w("| Check wanted | Attempt | Result |\n|---|---|---|")
for name, call in [("Project `northwind-workshop` exists in `waelconsulting`", "ado-remote-mcp-core_list_projects"),
                   ("Work item query for existing `nw-workshop` or `wael-01` items (duplicate risk)", "ado-remote-mcp-wit_query"),
                   ("Search for `wael-01` or the backlog ids in existing work items", "ado-remote-mcp-search_workitem"),
                   ("Read a work item to learn its type and fields", "ado-remote-mcp-wit_work_item"),
                   ("Project teams (area and iteration paths)", "ado-remote-mcp-core_list_project_teams")]:
    w("| %s | `%s` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |" % (name, call))
w("")
w("Cause (as far as I can see): `.mcp.json` declares the server `ado-remote-mcp` (type `http`), but its tools are not loaded in this session. I read `.mcp.json` only to list the server name; I did not print the URL or any header. I did not try any other route to Azure DevOps (no REST call, no CLI, no web fetch), because the scope was the MCP server.\n")
w("**Not validated, so `needs_review`:**\n")
w("* The project exists and my account can read it.")
w("* The process template. Agile has Epic, Feature, User Story. Scrum has Product Backlog Item instead of User Story. Basic has no Feature. CMMI has Requirement. The payload assumes Agile (`adoTypeNeedsReview: true` on every item).")
w("* The fields `Microsoft.VSTS.Common.AcceptanceCriteria`, `Microsoft.VSTS.Common.Priority`, `System.Tags` and `System.Description` exist on each of the three types. Epics and features in Agile have no acceptance criteria field, and the backlog gives none for them.")
w("* The backlog levels allow Epic > Feature > User Story for the target team.")
w("* Existing items already carrying `nw-workshop` or the `wael-01` prefix, or one of the 144 backlog ids in a title. **Duplicate risk is unknown.** Wanted query: `[System.TeamProject] = 'northwind-workshop' AND ([System.Tags] CONTAINS 'nw-workshop' OR [System.Title] CONTAINS 'wael-01')`.")
w("* Permission to create the new tags `nw-workshop`, `track-azure`, `track-dotnet`, `azure-r1` to `azure-r3`, `dotnet-r1` to `dotnet-r3` (9 new tag names: `nw-workshop`, 2 track tags and 6 release tags). Contributors can normally do this. Not verified.")
w("* Permission to add Hyperlink relations and hierarchy links.\n")
w("**Other evidence I could read (not Azure DevOps):** `git ls-remote --tags origin` lists the six `product/<track>-r<n>` tags, all on commit `5ad7971`. `git diff 5ad7971 HEAD -- docs knowledge-docs` shows no change. Only `.mcp.json` is untracked in the working tree.\n")

# ------------------------------------------------------------------ G
w("## G. Optional add-on: the %d unplanned items\n" % len(addon))
w("**Not in scope. Decision for you.** They carry only `nw-workshop` and their track tag, never a release tag (ES-31). They are not planned in any release (backlog section 5). Power Platform has no release and no team (G-08, O-07), and `EPIC-204` cannot take a release tag until O-01 is answered.\n")
ac = Counter((i["track"], i["adoWorkItemType"]) for i in addon)
w("| Track | Epics | Features | User Stories (enablers `EP-` included) |\n|---|---|---|---|")
for trk in ("track-power-platform", "track-dotnet"):
    w("| `%s` | %d | %d | %d |" % (trk, ac[(trk, "Epic")], ac[(trk, "Feature")], ac[(trk, "User Story")]))
w("")
a_parent = sum(1 for i in addon if i["parentLocalId"])
w("If you approve it: %d creates, %d parent links, %d hyperlink operations (same rules as section E). Title form `wael-01 <id> <title>`; the payload holds the full text under `optionalAddOnUnplanned`. Its checks passed in the same script run (one track tag, no release tag, parents exist).\n" % (len(addon), a_parent, payload["counts"]["hyperlinksUnplanned"]))
w("| localId | ADO type | Exact title | Tags | Parent |\n|---|---|---|---|---|")
for i in addon:
    w("| `%s` | %s%s | %s | `%s` | %s |" % (i["localId"], i["adoWorkItemType"], " (enabler)" if i["backlogType"] == "enabler" else "", esc(i["title"]), i["tags"], ("`%s`" % i["parentLocalId"]) if i["parentLocalId"] else "none"))
w("")
w("Points to decide for the add-on: `STORY-324` (spreadsheet claims migration) has **no priority** until O-14 is answered (Lena Varga, Julien Moreau). The Q1 2027 claims pilot cannot be committed (A-25). Publishing the Power Platform items would show work that has no team, which can mislead a reader of the board.\n")

# ------------------------------------------------------------------ H
w("## H. Risks, ASSUMPTION and OPEN items\n")
w("### Risks\n")
risks = [
    ("R1", "Azure DevOps could not be checked", "Project, process, types, fields, duplicates and tag rights are all `needs_review` (section F). A create could fail, or land in the wrong type.", "Load the `ado-remote-mcp` tools, run the section F checks, and regenerate this preview before approval."),
    ("R2", "Duplicate items", "If earlier workshop runs left items tagged `nw-workshop` or titled `wael-01 ...`, a second create would duplicate them (ES-28).", "Run the duplicate query. Classify matches as Match, Similar, Distinct or Uncertain. Do not create until that is done."),
    ("R3", "Documents still say draft and not approved", "Every release file says `status: proposed`, an empty `approval_date`, and approver `OPEN: O-09`. The Azure files also say the Git tag is *not created*, yet the tags now exist on `origin`. The business case says *Approved for discovery. Not yet approved for build* (O-21). The backlog is v0.1.0 draft. ADO items will link to files that still read as drafts.", "You told me the releases are approved. The documents do not record it. I changed nothing under `docs/`. The owner should record the approval (O-09, A-38, A-39) so the linked files match the board."),
    ("R4", "O-06 named no tool until now", "Backlog O-06 (owner Lena Varga) asked *which backlog tool and which ES-28 prefix*. `tracker_published: false` and section 6 say nothing is validated. Your request now names Azure DevOps `waelconsulting/northwind-workshop` and prefix `wael-01`.", "Treat this request as the answer to O-06. After a real publish, the owner updates O-06 and `tracker_published` in a separate, approved change. Not done here."),
    ("R5", "Rank and priority mapping", "The backlog rank is per track (Azure 1 to 36, .NET 1 to 40) and exists for stories and enablers only. `StackRank` is one number across a whole project, so two tracks would interleave. The backlog uses MoSCoW (Must, Should, Could), not ADO's 1 to 4.", "ASSUMPTION P-A1: Must=1, Should=2, Could=3 in `Microsoft.VSTS.Common.Priority`. Rank stays in the description and the creation order, and is not written to `StackRank` unless you ask. Owner: Lena Varga."),
    ("R6", "Enablers look like stories", "`EA-`/`EN-` enablers become User Story (backlog 6.1). Only the id and the title tell them apart, because you asked for exactly three kinds of tag.", "Accepted as asked. A tag such as `enabler` would break the tag rule (ES-31), so none is proposed."),
    ("R7", "Gated items look committed", "%d planned items sit behind experiment gates (all `pending`; no experiment has been run). Publishing them in a release can read as a commitment. Gate text is in each description." % len(gated), "Keep the Gate line and the EXP link on each item. Decisions go, adjust or stop are taken before commit (experiments.md)."),
    ("R8", "Link volume", "%d hyperlinks on %d items is a lot of repeated links. Four documents repeat on most stories." % (n_links, len(items)), "Option: epics and features only (about %d links), or drop TRC and BKL from stories. Your choice (question Q4)." % sum(len(i["hyperlinks"]) for i in items if i["backlogType"] in ("epic", "feature"))),
    ("R9", "Links point at `main`", "If the docs change later, the links show newer text than the tagged release.", "Option: link the release tag (`/blob/product/<track>-r<n>/...`) instead. Question Q5."),
    ("R10", "Title length", "The longest published title is %d characters. The backlog limit of 100 (BD-04) applies to the title without the prefix; ADO allows 255." % max(len(i["title"]) for i in items), "No action."),
    ("R11", "Cross-track needs are open, not waits", "X-nn rows are OPEN in the descriptions. A release never waits for another track (ES-31, A-45).", "No ADO predecessor links are proposed, so the board shows no false dependency."),
    ("R12", "`azure-r3` window", "A-58 stretches the window to 27 June 2027, leaving 3 days before the lease ends (C-01). O-27 (Marc Dubois) is unanswered.", "Shown as written. No date fields are set in ADO."),
    ("R13", "Power Platform has no release", "BA-03 has no team (O-07), so it has no release tag and is not in this scope (section G).", "Decision Q2."),
    ("R14", "Scope check by me", "Counts were checked by parsing the backlog, not by hand. The parse equals the register (144), section 3 counts and section 6.2 titles.", "Re-run `python3 build_ado_payload.py` after any backlog change."),
]
w("| Id | Risk | Detail | Handling |\n|---|---|---|---|")
for r in risks:
    w("| %s | **%s** | %s | %s |" % tuple(esc(x) for x in r))
w("")
w("### New ASSUMPTION items made by this preview (ES-03)\n")
w("| Id | ASSUMPTION | Owner who can confirm |\n|---|---|---|")
w("| P-A1 | Must, Should and Could map to ADO priority 1, 2 and 3. | Lena Varga |")
w("| P-A2 | Experiment links (EXP) go only to items whose gate is an MVE; BRD links go to epics and to stories whose source line cites a `BR-` or `NFR-`. | Lena Varga |")
w("| P-A3 | The target project uses the Agile process (Epic, Feature, User Story). Not verified. | Ahmed Benali |")
w("| P-A4 | Documentation links point at `main`, not at the release tags. | Lena Varga |")
w("")
w("These four are mine and are not in the backlog. They are not requirements.\n")
w("### ASSUMPTION and OPEN ids that the planned items cite\n")
w("Text and owner come from backlog section 7 (the register of record). \"Cited by\" is the number of planned items that cite the id.\n")
cited = Counter()
for i in items:
    for r in i["citedRegisterIds"]:
        cited[r] += 1
w("| Id | Cited by | Text | Owner |\n|---|---|---|---|")
for k in sorted(cited, key=lambda x: (re.sub(r"[\d-]+$", "", x), [int(n) for n in re.findall(r"\d+", x)])):
    r = reg.get(k, {"text": "(not found)", "owner": ""})
    w("| %s | %d | %s | %s |" % (k, cited[k], esc(r["text"]), esc(r["owner"])))
w("")
w("Items that rely on an OPEN question stay publishable: the OPEN marker is in the description, with its owner, so nobody reads it as a requirement (ES-04).\n")

# ------------------------------------------------------------------ I
w("## I. Nothing has been created. Approval needed.\n")
w("**Status: nothing has been created, updated, linked or deleted in Azure DevOps.** No file under `docs/` or `knowledge-docs/` was changed. No `git push`, commit or tag was run. Only four files in `.copilot-tracking/plans/2026-11-17/` were written: the two scripts, the payload and this preview.\n")
w("**What I need from you before any write:**\n")
w("1. Load the `ado-remote-mcp` tools (or confirm another read path) so I can run the section F checks. Then I regenerate this preview with the real types, fields and duplicate results.")
w("2. Approve the scope of %d items and the exact text in sections C and D, or tell me what to change." % len(items))
w("3. Approve the field mapping (section B) and answer the questions below.")
w("4. Say, in words, something like *\"Approved: create the %d items in Azure DevOps\"*. Without that, I stay read-only.\n" % len(items))
w("**Open questions (OPEN:, with who can answer):**\n")
w("* **Q1** Is the target process Agile? (Ahmed Benali, after the read checks.)")
w("* **Q2** Do you want the %d unplanned items (section G) published too, with track tag only? (Lena Varga.)" % len(addon))
w("* **Q3** Mapping Must/Should/Could to priority 1/2/3, and no `StackRank`: acceptable? (Lena Varga.)")
w("* **Q4** Keep all %d hyperlinks, or reduce them (risk R8)? (Lena Varga.)" % n_links)
w("* **Q5** Link `main` (as you asked) or the release tags (risk R9)? (Lena Varga.)")
w("* **Q6** Who records the release approval in the release files (R3, O-09)? (Marc Dubois.)")
w("* **Q7** Which area path and iteration path should items use? The backlog sets none; the default project root is assumed. (Ahmed Benali.)")

open(os.path.join(HERE, "ado-publish-preview.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote ado-publish-preview.md", len("\n".join(out)), "chars")
