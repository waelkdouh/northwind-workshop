# Review 3: Northwind product documents (BA-01 Azure, BA-02 .NET), final verification after remediation cycle 2

| Field | Value |
|---|---|
| Stage | Review, final verification (Squad Reviewer). Third pass after `product-documents-review.md` (Fail) and `product-documents-review-2.md` (Fail, M-1 only at Medium) |
| Date | 2026-10-30 |
| Under review | 13 files in `docs/product/`: `business-requirements.md`, `product-requirements.md`, `experiments.md`, `backlog.md`, `traceability.md`, `README.md`, `releases/azure-r1..r3.md`, `releases/dotnet-r1..r4.md` |
| Checked against | `knowledge-docs/business-case.md`, `current-state.md`, `engineering-standards.md`; plan criteria Q-01..Q-17 (`.copilot-tracking/plans/2026-10-30-northwind-product-documents-plan.md`, section 9); review 1 and review 2 findings |
| Implementation state | Read-only. No product document, earlier review or source file was changed. `git status --short -- src database knowledge-docs` is empty; `git diff --stat HEAD -- src database knowledge-docs` is empty; the only tag is `starter`; `main` has one commit (`f6e3874`); `docs/` contains only `product/` (13 files); `infra/` does not exist |
| Method | Re-ran the four existing scratch probes (`check-final.py`, `check-final-2.py`, `check-oos.py`, `check-enables.py`). Added two read-only scratch probes in the authorised directory: `check-cycle3.py` (encoding, table column counts, links and anchors, independent A-/OPEN- wording comparison, cross-track wording in context, claim wording, item status values) and `check-owners-cycle3.py` (owner cells of every OPEN row against README). Targeted reads of every cycle-2 edit site. Targeted greps for pre-remediation strings, secrets, and source IDs against knowledge-docs |
| Model identity | Not known to the reviewer |
| Tool calls | About 55 (approximate) |
| Paths written | This report: `C:\demos\northwind-workshop\.copilot-tracking\reviews\product-documents-review-3.md`. Scratch only, inside the authorised probe directory: `check-cycle3.py`, `check-owners-cycle3.py`, `cycle3-out.txt` (output of `check-cycle3.py`). Nothing else. The harness saved some long tool output to the user temp folder; this review did not write those spill files |

## Verdict

Verdict: Pass

No Critical, High, Medium or Low finding remains. The Medium finding from review 2 (M-1, OPEN wording) and all four Low findings (L-A to L-D) are resolved in the final files, and the cycle-2 edits introduced no regression that the suite can detect. Plan criteria Q-01..Q-17 pass on the final files. Three observations in section 5 are probe notes or harness facts, not defects in the documents.

Scope limit. Q-14 (plain language and acronym wording) was spot-checked again, not re-read line by line. The regression scan covers tables, encoding, links and cycle-2 edit sites, not every sentence.

## 1. Resolution of review-2 findings

| Review-2 ID | Status now | Evidence in the final files |
|---|---|---|
| M-1 (Medium) OPEN wording differs from README | **Resolved** | Independent comparison (`check-cycle3.py`, section D): 546 table rows with an A- or OPEN- ID compared against README §6 after whitespace and backtick normalisation only. **0 differences.** Rows per file: BRD 64, PRD 105, EXP 40, BL 69, TR 24, AZ1 47, AZ2 49, AZ3 17, DN1 27, DN2 52, DN3 19, DN4 33. OPEN-30 in `azure-r2` is now complete. The README §7 sentence ("identical in every document that repeats an ID") is now true |
| L-A (Low) `US-DN-037` lacks "as of the 02:00 batch" (A-04) | **Resolved** | `backlog.md` US-DN-037 (line ~2229): criterion 4 now reads "Given Picking and Shipped are updated only by the nightly 02:00 batch (A-04), When I read the explanation, Then the page states that these two statuses are as of the 02:00 batch." The "ASSUMPTION / OPEN used" line now includes A-04. The A-04 probe no longer flags US-DN-037. Criterion count rose from 346 to 347, which accounts for the new criterion |
| L-B (Low) EN-DN-10 "Enables" line contains prose | **Resolved** | `backlog.md` EN-DN-10 block (line ~1313): the Enables line lists enabled items only (18 features). The sentence is now its own bullet, "Stories that depend on it: exactly 35 stories ... `US-DN-003` to `US-DN-037` ...". Review 2 counted 160 Enables targets; this pass counts 123. The difference is 37, which is exactly the 35 stories plus the 2 exclusions (`US-DN-001`, `US-DN-002`) that were in the old line. The 123 targets have 0 problems (no enabler in a later release, no cross-track target) |
| L-C (Low) `track-power-platform` "is not used here" | **Resolved** | `backlog.md` §2.1 (line 56): "`track-power-platform` is not used as an item tag." Same wording as README §1.2 |
| L-D (Low) `FT-DN-25` source is only OPEN-24 | **Resolved** | `backlog.md` FT-DN-25 block: "(source: none in knowledge-docs in scope; OPEN-24, informational)". Register row (§11) and item block agree on the source set (no knowledge-docs ID). Appendix A, `dotnet-r4.md` §11 item 4 and README §9 describe the same thing. No BA-03 identifier is used as a source |

## 2. Structural suite on the final files

| Check | Result |
|---|---|
| Register (backlog §11) | 133 rows, 133 unique. Azure: 3 epics, 11 features, 14 enablers, 19 stories (47). .NET: 8 epics, 26 features, 15 enablers, 37 stories (86). Planned release counts: azure-r1 17, azure-r2 22, azure-r3 8, dotnet-r1 15, dotnet-r2 41, dotnet-r3 10, dotnet-r4 11. Unplanned 9 (EP-DN-08, FT-DN-23, FT-DN-24, FT-DN-25, FT-DN-26, US-DN-034, US-DN-035, US-DN-036, US-DN-037), confirmed by direct grep of the register rows |
| Item blocks vs register | 133 blocks, one per register row, none missing and none extra. Track, release, type, priority, parent, title and source set agree for all 133 |
| One track tag per item; at most one same-track release tag | 0 problems. All 133 items have exactly one track tag; no item has two release tags; no item has a release tag from the other track; no unexpected tag |
| Parent and child consistency | 0 problems. Track and release of every child equal its parent; every child is listed in its parent's Contains or Enablers line |
| Dependencies | 0 cross-track; 0 to a later release; 0 planned-on-unplanned; 0 self-dependencies. Probe covers all planned items |
| Rank tables (backlog §4) vs item "Depends on" | 33 Azure and 52 .NET rows. Rank release equals register. Dependency sets equal item blocks. EN-DN-11 is ranked 11, before EN-DN-10 at 12. The four probe flags "rank order goes back a release" are for US-DN-034..037 (see section 5, P-1) |
| Release file §3 tables and §7.1 tables | Row counts and sets equal the register for all seven releases; §7.1 dependency sets equal the backlog rank tables |
| Release headers, README §3 and traceability §7 counts | Equal the register by track, type and release. Azure 17 (1/4/7/5), 22 (1/5/7/9), 8 (1/2/0/5); .NET 15 (1/4/8/2), 41 (4/12/6/19), 10 (1/3/0/6), 11 (1/3/1/6); unplanned 9 (1/4/0/4). Track totals 47 and 86 |
| Coverage of BR-01..BR-13 and NFR-01..NFR-08 | 21 of 21 covered by at least one planned item. Counts from the register range from 3 to 14 items per ID. Traceability §3.1 and §3.2 agree with the register. The only table-versus-register difference is the BR-13 supporting items marked `†` (`EN-AZ-09`, `EN-AZ-10`, `EN-AZ-14`, `US-AZ-012`), which traceability §2 and §8.2 and backlog §5.1 disclose |
| Source IDs | 81 distinct source IDs in item source lines. All resolve to a knowledge-docs ID or the product `P-01..P-06` problem table. **No BA-03 identifier** (BR-14..19, NFR-09, C-07, C-08, SM-05, SM-06, OQ-04, OQ-05, CS-24..28, ES-32..37) appears as a source in any item, register row or Appendix A row |
| Out-of-scope identifiers in prose | 35 mentions, each in an out-of-scope list, an out-of-scope note or the informational OPEN-24 text. The six mentions in table rows without nearby prose are rows of out-of-scope tables (traceability §6, and the out-of-scope sections of the BRD and PRD) |
| Story form | 56 stories and 29 enablers have "As a / I want / so that" (0 missing) |
| Given / When / Then | 347 criteria; 0 out of Given, When, Then order |
| Appendix A (traceability) | 85 rows = 56 stories + 29 enablers. Track, release, priority, title and covers equal the register |
| A-nn and OPEN-nn definitions | README defines A-01..A-46 and OPEN-01..OPEN-33. Every ID used is defined and every defined ID is used. Declared "used in" codes equal actual occurrences (probe reports no difference). Owner cells: 287 OPEN rows with names checked against README (`check-owners-cycle3.py`): 0 mismatches |
| Draft status wording | All 133 items `Status: Draft`. Six non-release documents: "Draft - for review. Not approved for build. (A-16)". Seven release files and PRD §8 and README §2 and §3: "Draft — awaiting product owner approval; not yet tagged". 0 "Proposed" status wording |
| MVE identifiers | Only `MVE-BA01` and `MVE-BA02` |
| Secrets | 0 hits for the earlier probe patterns (GUID, `AccountKey`, `SharedAccessSignature`, private-key markers, IPv4, e-mail, `Server=`, `Data Source=`, token prefixes). Second sweep with keyword-assignment, `password`, `secret`, `api key`, `bearer`, GUID and AWS or GitHub token prefixes: 0 hits |

## 3. Plan criteria Q-01..Q-17 on the final files

| Criterion | Result | Evidence |
|---|---|---|
| Q-01 Files at pinned paths; nothing written elsewhere | Pass | 13 files; `docs/` contains only `product/`; no `infra/` |
| Q-02 BA-03 only in out-of-scope lists (and OPEN-24 as informational) | Pass | No BA-03 ID as a source (section 2). OPEN-24 is informational |
| Q-03 Every BR-01..13 and NFR-01..08 covered; uncovered listed | Pass | 21 of 21 covered; "Not covered: none" is correct |
| Q-04 NFR-03, NFR-05 per track; NFR-04 .NET only; no two-track item | Pass | Register and item tags; no item has two track tags |
| Q-05 Tags (ES-30, ES-31) | Pass | Section 2 |
| Q-06 Release membership equal across backlog, traceability, release file, PRD | Pass | Section 2; PRD §8 names every planned EP/FT/EN ID for each release (probe: missing=[], extra=[] for seven releases) |
| Q-07 Release counts 3 Azure and 4 .NET; Git tags planned only | Pass | Seven release files. Only tag `starter`. `main` has one commit |
| Q-08 No release waits on another track | Pass | 0 cross-track dependencies. Cross-track wording search: 0 hits. The 57 "after" hits are time phrases ("after portal launch", "after the move") or intra-track, reviewed in context |
| Q-09 Stories and enablers: As a / I want / so that; Given / When / Then | Pass | Section 2 |
| Q-10 Sources cite knowledge-docs IDs or labelled findings | Pass | All 81 distinct source IDs resolve. FT-DN-25 cites OPEN-24 only, with the form gap disclosed (L-D resolved) |
| Q-11 A- and OPEN- IDs identical in meaning and wording; README master register | **Pass** | 546 rows, 0 differences (review 2 had 28) |
| Q-12 Enablers before features; dependencies earlier in own track | Pass | Rank tables non-decreasing by release; 0 dependency ranked after its dependent; release §7.1 tables equal rank tables |
| Q-13 Exactly two MVEs; nothing run | Pass | `MVE-BA01`, `MVE-BA02` only; experiments §7 records "not run" |
| Q-14 Plain language, acronyms, file locations, `az bicep build` wording | Pass (spot-check, not re-read in full) | Acronym and location wording unchanged in cycle 2 |
| Q-15 No secrets or real tenant, subscription or connection values | Pass | Section 2 |
| Q-16 Documents say "for review"; no change to `src/`, `database/`, `infra/` | Pass | Section 4 (git) |
| Q-17 Every file marked draft; each release awaits product-owner approval | Pass | Section 2 |

## 4. Regression check on the cycle-2 edits

| Check | Result |
|---|---|
| Table integrity (every table in the 13 files) | 211 tables. Each has a separator row and every row has the header's column count. **0 problems.** The rewritten OPEN cells did not break any table |
| Encoding | All 13 files decode as strict UTF-8. No U+FFFD and no mojibake sequences. Em dashes present where expected |
| Links and anchors | The product documents contain **0 markdown links**, so there are no anchors to break. File references are backtick paths |
| Counts 17 / 22 / 8 and 15 / 41 / 10 / 11, plus 9 unplanned | Equal across register, release headers, release §3 tables, README §3, traceability §7, PRD §8 (section 2) |
| Rewritten cells: OPEN wording (28 cells) | Identical to README (section 1, M-1) |
| Rewritten prose: US-DN-037 criterion 4 and used-line; EN-DN-10 Enables and new bullet; backlog §2.1 row; FT-DN-25 source | Each correct; each consistent with its register row, item block, Appendix A and release text (section 1) |
| Pre-remediation strings | Not present: "listed once here"; "not reachable with 20 of"; "arithmetic"; "track-power-platform is not used here"; "Proposed … awaiting"; "CS-27", "ES-36", "CS-26", "CS-28" in a source context; "2 weeks" baseline; a BA-02 NFR-06 row; the old Enables sentence |
| Git | `git status --short -- src database knowledge-docs`: empty. `git diff --stat HEAD -- src database knowledge-docs`: empty. No `product/*` tag. No product-document commit. `main` = `f6e3874` = `starter` |

## 5. Findings and observations (ordered by severity)

There are no Critical, High, Medium or Low findings in this pass. The three items below are observations. None requires an edit to a product document.

| ID | Type | Where | Observation | Why it does not change the verdict | Suggested action |
|---|---|---|---|---|---|
| P-1 | Probe note | `check-final.py` rank check (line ~190) | Reports "rank order goes back a release" for US-DN-034..037. These unplanned rows sit after `dotnet-r4` with release `none`, and the probe maps `none` to release 0. No planned item depends on them, and the rank table is correct | The document is correct. The probe logic is not | Treat `none` as unplanned and skip the order test for those rows |
| P-2 | Probe note | `check-final-2.py` OWNER-OPEN lines | Reads the track column of the BRD §12 pointer table (which has no owner column) as if it were the owner. The real owner comparison (BRD §17, all other tables, 287 rows) passes in `check-owners-cycle3.py` | The owner cells match README | Compare owner cells only in tables that have an owner column |
| P-3 | Harness fact | Git refs `refs/agents/<session>/checkpoints/turn/*` (4 commits, 09:39–09:48) | The agent host created checkpoint commits under `refs/agents/`. They are not on `main`, carry no tag, contain no `docs/` file, and their `src`, `database` and `knowledge-docs` trees equal the starter commit. They are not product-document commits | Q-07 and the "no commit of product docs" rule are met | None for the documents. The coordinator may decide whether those harness refs should stay in the repository |

## 6. Plan deviations (charter response format)

* Planned, not done: none. All 13 files exist at the pinned paths. No extra file under `docs/`. No `infra/` folder.
* Done differently, already recorded and unchanged in this pass: release status wording "awaiting product owner approval; not yet tagged"; four-week baseline recorded as A-44; NFR-04 attribution through A-02 and BRD §4.
* Done, not planned, disclosed: `EN-AZ-14` and `EN-DN-15` (plan J-1, J-2); A-27..A-46; OPEN-27..OPEN-33; `FT-DN-26` and `EP-DN-08` (A-35, A-36); `US-AZ-020` as the next free number.
* Done, not planned, not disclosed: none found in this pass.

## 7. Conditions honored

Not applicable. No council conditions were supplied with this dispatch.

## 8. Review record

This file: `C:\demos\northwind-workshop\.copilot-tracking\reviews\product-documents-review-3.md`.

Scratch artefacts (not product documents), all in `C:\demos\northwind-workshop\.copilot-tracking\reviews\probe-nw-product-docs\`: `check-cycle3.py` (new: encoding, table columns, links and anchors, independent A-/OPEN- wording, cross-track wording, claim wording, item status), `check-owners-cycle3.py` (new: OPEN owner cells vs README), `cycle3-out.txt` (output of `check-cycle3.py`). Re-run without modification: `check-final.py`, `check-final-2.py`, `check-oos.py`, `check-enables.py`. The earlier probes and the first-review CSV files were not modified.

## 9. Return to coordinator

| Item | Value |
|---|---|
| Verdict | **Pass** |
| Findings open | None at Critical, High, Medium or Low. Three observations (P-1 to P-3) |
| Review-2 items | M-1 and L-A to L-D resolved and verified |
| Next step | Product-owner approval of each release, per the document status. Approval and tagging remain outside this review. Optional: fix the two probe logic notes (P-1, P-2) before any later re-run |
| Release approval | Not affected by this review. No tag or commit was created or proposed |
