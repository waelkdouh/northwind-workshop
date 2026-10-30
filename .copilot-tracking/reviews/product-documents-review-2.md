# Review 2: Northwind product documents (BA-01 Azure, BA-02 .NET), closing re-review after remediation cycle 1

| Field | Value |
|---|---|
| Stage | Review, closing re-review (Squad Reviewer). Second pass after the remediation of `product-documents-review.md` (verdict Fail: H-1, M-1..M-3, L-1..L-7) |
| Date | 2026-10-30 |
| Under review | 13 files in `docs/product/`: `business-requirements.md`, `product-requirements.md`, `experiments.md`, `backlog.md`, `traceability.md`, `README.md`, `releases/azure-r1..r3.md`, `releases/dotnet-r1..r4.md` |
| Checked against | `knowledge-docs/business-case.md`, `current-state.md`, `engineering-standards.md` (ES-02, ES-07, ES-09, ES-31); plan criteria Q-01..Q-17 (`.copilot-tracking/plans/2026-10-30-northwind-product-documents-plan.md`, section 9); first review `product-documents-review.md` |
| Implementation state | Read-only. No product document, no earlier review and no source file was changed by this review. `git status` shows only untracked `docs/` and `.copilot-tracking/`; `git status --short -- src database knowledge-docs` is empty; `git diff --stat` is empty; the only tag is `starter`; `git rev-list --count HEAD` is 1 |
| Method | Four read-only Python probes in the authorised scratch directory `.copilot-tracking/reviews/probe-nw-product-docs/`: register vs item blocks vs rank tables vs release tables vs Appendix A vs traceability §3 vs PRD §8 vs README master registers; strict Given/When/Then order on all criteria; transitive dependency reach to EN-DN-10; out-of-scope identifier context; A-/OPEN- wording and owner comparison; secret patterns. Targeted reads of the changed sentences |
| Model identity | Not known to the reviewer |
| Tool calls | About 100 (approximate) |
| Paths written | This report: `C:\demos\northwind-workshop\.copilot-tracking\reviews\product-documents-review-2.md`. Scratch only, inside the authorised probe directory: `check-final.py`, `check-final-2.py`, `check-oos.py`, `check-enables.py`. The harness also saved long tool output to the user temp folder; those spill files were not written by this review's scripts. Nothing else |

## Verdict

**Verdict: Fail**

Basis. No Critical or High finding remains. The plan (section 9) says the review "passes only if all [criteria] are true". One criterion is still not met literally: **Q-11** (A- and OPEN- IDs "identical in meaning and wording in every file and in the README master register"). The A- wording is identical everywhere. The OPEN- wording differs in 28 table cells across the BRD, the PRD and three release files, and the README §7 statement that wording is "identical in every document" is therefore false. This is a bounded text fix (Medium, M-1). The other findings are Low (L-A to L-D). After M-1 is fixed, the expected result is Pass-With-Findings (Low only), or Pass if the owner accepts the Low items.

## 1. Resolution of the first-review findings

| First-review ID | Status now | Evidence in the final files |
|---|---|---|
| H-1 (High) EN-DN-10 coverage | **Resolved** | Probe: 35 of 37 `US-DN` stories list `EN-DN-10` directly in "Depends on (same track)". The two without it, `US-DN-001` and `US-DN-002`, are staff-only stories in `dotnet-r1`, an earlier release, so they cannot depend on an enabler in `dotnet-r2`. The EN-DN-10 block (backlog line 1315) now states that exact count. The five stories the first review named (`US-DN-005, 019, 026, 027, 034`) all cite it. No dependency is on a later release. |
| M-1 (Medium) Given/When/Then "When" missing in 84 enabler criteria | **Resolved** | Probe: 346 of 346 criteria match the ordered pattern `Given ..., When ..., Then ...`. |
| M-2 (Medium) BA-03 identifiers cited as sources | **Resolved** | Probe: no out-of-scope ID appears in any item source line, register row or Appendix A row. `CS-27`/`ES-36` are gone from FT-DN-25 and EP-DN-08; `CS-26`/`CS-28` are gone from experiments. Traceability §8.1 check 8 now describes the result accurately: 35 out-of-scope mentions in the repository, each in an out-of-scope list or in the informational OPEN-24 text. |
| M-3 (Medium) "35 % not reachable with 20 of 1,150" stated as fact | **Resolved** | "arithmetic" is gone. The statement is labelled `ASSUMPTION: A-46` and points to OPEN-05 at BRD §2.2 note and R-11, PRD R-11, experiments B4, traceability SM-01, and `dotnet-r4` §11 item 2. A-46 is defined in README and used in exactly the files the README declares (BRD, PRD, EXP, TR, DN2, DN4). |
| L-1 Release status wording (Q-17) | **Resolved** | All seven release files, the PRD §8 status rows and the README §2 and §3 tables read "Draft — awaiting product owner approval; not yet tagged". No "Proposed — awaiting" status remains. |
| L-2 Unplanned items in `dotnet-r4` Appendix A | **Resolved** | Appendix A is framed as "not part of this release or any release". "listed once here" is gone. Membership unchanged (11 planned). |
| L-3 Four-week baseline not recorded as a difference from plan | **Resolved** | A-44 (EXP) records the difference ("4 weeks, not the 2 weeks first planned"). Experiments §1, §2.7 and §3.6 cite it consistently. The arithmetic (4 weeks baseline, 2 weeks test, about 8 weeks elapsed) is consistent. |
| L-4 `US-DN-036` lacks "as of the 02:00 batch" | **Resolved** for `US-DN-036`. The same gap remains in `US-DN-037`; see L-A below. |
| L-5 "The tag `track-power-platform` is not used in any document" | **Partly resolved.** README §1.2 now reads "is not used as an item tag". The same self-contradictory wording remains in the backlog §2.1 table; see L-C. |
| L-6 EUR 1,350 cited to A-06 | **Resolved.** EUR 1,350 now cites A-45 in backlog (cost criteria), `azure-r1` (§3 row and §12) and experiments (§2.7, M4, A-45 row). Nothing cites A-06 for the cost threshold. |
| L-7 NFR-06 attribution (BA-02 row) and NFR-04 BA-01 note | **Resolved in substance.** The NFR-06 BA-02 row is gone; traceability §3.2 lists NFR-06 once, under BA-01. The NFR-04 BA-01 row states "No Azure story, by assumption A-02". The suggested words "cross-cutting per business case §4" were not added verbatim. This is accepted, because BRD §4 and A-02 record the cross-cutting basis and no attribution is wrong. |

## 2. Plan criteria Q-01..Q-17 on the final files

| Criterion | Result | Evidence |
|---|---|---|
| Q-01 Files at pinned paths; nothing written elsewhere | Pass | The 13 files are present. `docs/` contains only `product/` and `product/releases/`. No other file under `docs/`. |
| Q-02 BA-03 only in out-of-scope lists (and OPEN-24 as informational) | Pass | No BR-14..19, NFR-09, C-07, C-08, SM-05, SM-06, OQ-04, OQ-05, CS-24..28, ES-32..37 in any item source line. Of 35 mentions in the product documents, every one sits in an out-of-scope list, an out-of-scope note, or the informational OPEN-24 text. FT-DN-25 cites only OPEN-24 as its source (see L-D, a source-form gap, not a BA-03 citation). |
| Q-03 Every BR-01..13 and NFR-01..08 covered; uncovered listed | Pass | Probe: each has at least one planned story or enabler. Traceability §3.1 and §3.2 story and enabler lists equal the register for all 24 BR/NFR rows, with release tags matching. The only difference is the BR-13 supporting items marked `†` (`EN-AZ-09`, `EN-AZ-10`, `EN-AZ-14`, `US-AZ-012`), which traceability §2 and §8.2 and backlog §5.1 explain. "Not covered: none" is correct. |
| Q-04 NFR-03, NFR-05 per track; NFR-04 .NET only; no two-track item | Pass | NFR-03 and NFR-05 have items on both tracks. NFR-04 has no Azure-tagged planned item (OPEN-13, A-02). No item has two track tags. |
| Q-05 Tags (ES-30, ES-31) | Pass | 133 items: exactly one track tag each; at most one release tag, same track; 124 planned, 9 unplanned with none; parent and child share track and release; register agrees with item tags, type, priority, parent, title and sources for all 133. |
| Q-06 Release membership equal across backlog, traceability, release file, PRD | Pass | Release file §3 rows equal the register for all seven releases (17, 22, 8, 15, 41, 10, 11). Header totals match. Traceability §7 counts match. README §3 counts match. PRD §8 names every planned EP, FT and EN of each release (12, 13, 3, 13, 22, 4, 5 IDs, zero missing, zero extra) and no US story. |
| Q-07 Release counts 3 Azure and 4 .NET; Git tags planned only | Pass | Seven release files. `git tag --list` shows only `starter`. One commit. |
| Q-08 No release waits on another track | Pass | Probe: 0 cross-track dependencies and 0 dependencies on a later release. Positive "requires", "blocked by", "waits for" uses on a line without negation are intra-track ("after the move", "requires sign-in"). |
| Q-09 Stories have As a / I want / so that and Given/When/Then | Pass | 56 stories and 29 enablers have "As a ... I want ... so that". All 346 criteria are in ordered Given/When/Then form. |
| Q-10 Sources cite knowledge-docs IDs (or labelled research findings) | Pass with note | Every source identifier in items is a knowledge-docs ID or a labelled assumption. FT-DN-25 cites only OPEN-24 (L-D). |
| Q-11 A- and OPEN- IDs identical in meaning and wording; README master register | **Fail (literal)** | A-01..A-46: all table cells identical to README (0 differences). OPEN-01..OPEN-33: 28 cell differences (M-1). README §7 says wording is identical; that is false. Owners agree in all backlog and README rows checked. |
| Q-12 Enablers before features; dependencies earlier in own track | Pass | Rank tables (33 Azure, 48 planned and 4 unplanned .NET) are non-decreasing by release; no dependency is ranked after its dependent (0 violations). The release §7.1 table in each of the seven release files equals the backlog rank table (rank, ID, dependencies), 0 mismatches. "Enables" lines: 160 targets checked, no enabler in a later release than what it enables (see the EN-DN-10 note, L-B). |
| Q-13 Exactly two MVEs; nothing run | Pass | Only `MVE-BA01` and `MVE-BA02` appear anywhere in the product documents. §7 of experiments records "not run". |
| Q-14 Plain language, acronyms, file locations, `az bicep build` wording | Pass (spot-check) | Not re-read line by line in this pass. Sampled sections show the acronym lists and the `az bicep build` wording. Locations follow ES-07 and ES-09 (`docs/migration/` for the migration report). |
| Q-15 No secrets or real tenant, subscription or connection values | Pass | Secret-pattern probe over all 13 files: 0 hits (GUID, `AccountKey`, `SharedAccessSignature`, `Password=`, `pwd=`, private-key marker, IPv4 address, e-mail address, `Server=`, `Data Source=`, token prefixes). |
| Q-16 Documents say "for review"; no change to `src/`, `database/`, `infra/` | Pass | All headers say "Draft - for review" or "Draft — awaiting product owner approval". Git: no tracked change under `src/`, `database/` or `knowledge-docs/`. No `infra/` folder exists. |
| Q-17 Every file marked draft; each release awaits product-owner approval | Pass | All 13 files are marked draft. All seven release files, the PRD §8 status rows and the README §2 and §3 tables say "awaiting product owner approval; not yet tagged". |

## 3. Structural checks on the final files

| Check | Result |
|---|---|
| Register rows (backlog §11) | 133, unique. By track and type: Azure 3 epics, 11 features, 14 enablers, 19 stories (47); .NET 8 epics, 26 features, 15 enablers, 37 stories (86). Planned by release: 17, 22, 8, 15, 41, 10, 11. Unplanned 9. |
| Item blocks | 133, one per register row, no duplicates, none missing either way |
| Register vs item text | Track, release, type, priority, parent, title and source set agree for all 133 |
| Rank tables (§4) vs item "Depends on" | 33 Azure and 52 .NET rows; rank release equals register; "to" range notation expanded; dependency sets equal for every row |
| Dependencies | 0 cross-track, 0 later-release, 0 planned-on-unplanned. US-AZ-005 identical to its item block (see the ruling in section 5) |
| Parent and child | Track and release identical for all 133; children listed in parent Contains or Enablers for all |
| Appendix A (traceability) | 85 rows = 56 stories + 29 enablers; track, release, priority, title, BR/NFR and C/SM/OQ covers equal the register. The "- (unplanned)" cell is a presentation form of "-", not a difference |
| Release file §3 tables | Row sets, titles, priorities, tags and sources equal the register for all seven releases; no non-member ID in §3 |
| Release header counts | "Items in this release" totals equal the register for all seven |
| Traceability §7 and README §3 counts | Equal the register by track, type and release |
| Story form and criteria | 0 missing "As a / I want / so that"; 0 criteria out of Given/When/Then order |
| A-04 "as of the 02:00 batch" | Missing in `US-DN-037` (L-A). `US-DN-036`, `FT-DN-11`, `US-DN-011`, `US-DN-012` carry it. Epics and features that cite BR-04 (`EP-DN-03`, `EP-DN-08`, `FT-DN-26`) are not stories; A-04 applies to stories (plan P04) |
| Out-of-scope IDs | None in sources; see Q-02 |
| A- and OPEN- definitions | README defines exactly A-01..A-46 and OPEN-01..OPEN-33. Every ID used somewhere is defined; every defined ID is used somewhere. Declared "used in" codes equal the actual occurrences for all IDs |
| A- wording | Identical in every file (0 differences) |
| OPEN- wording | 28 differences (M-1) |
| Plan §5.3 release OPEN lists | Every release file states each OPEN ID the plan lists for it |
| Secrets | 0 hits |
| `track-power-platform` as a tag | Not used as an item tag. Appears as a label in out-of-scope text only (backlog §2.1 wording: L-C) |
| Git | No `product/*` tag. One commit. `src/`, `database/`, `knowledge-docs/` unchanged |

## 4. Remediation edits: contradictions introduced

| Edit | Result |
|---|---|
| EN-DN-10 dependencies (H-1) | No contradiction. Rank table, item blocks and release `dotnet-r2` §7.1 agree for all 35 stories. The explanatory sentence sits in the Enables line, which a reader or script can misread (L-B). |
| A-44 (4-week baseline) | Consistent in experiments §1, §2.7, §3.6 and README. No residual "2 weeks" baseline. |
| A-45 (EUR 1,350 threshold) | Consistent. Cited to A-45 wherever the figure appears. README "used in" codes (EXP, BL, AZ1) equal the actual occurrences. |
| A-46 (35 % judgement) | Consistent. Labelled ASSUMPTION everywhere it appears. Declared "used in" codes (BRD, PRD, EXP, TR, DN2, DN4) equal the actual occurrences. |
| README §7 statement on wording | **Contradicted** by the final files (M-1). |
| US-AZ-005 and the rank range | No contradiction (see ruling below). |

## 5. Findings (ordered by severity)

| ID | Severity | File and location | Finding | Why it matters | Smallest fix |
|---|---|---|---|---|---|
| M-1 | Medium | OPEN labels in: `business-requirements.md` §17 (11 cells: OPEN-01, 03, 04, 06, 13, 18, 19, 20, 21, 22, 23); `product-requirements.md` §15 and the cross-track table in §10 (14 cells: OPEN-01, 03, 04, 06, 12, 13 (three variants), 18, 19, 20, 21, 22, 23); `releases/azure-r1.md` §9 (OPEN-13); `releases/azure-r2.md` §9 (OPEN-30, truncated); `releases/dotnet-r2.md` §9 (OPEN-13). README §7 "Result" paragraph (false statement) | 28 OPEN- wording cells differ from the README §6 master register. Examples: BRD OPEN-01 "Freshness of order status (also affects the exchange)" vs README "Acceptable freshness for BR-04 (nightly?)"; PRD OPEN-13 "Customer identity provider and platform sign-in plumbing" vs README "... (business case OQ-01)"; `dotnet-r2` OPEN-13 drops "(business case OQ-01)"; `azure-r2` OPEN-30 is cut short. README §7 says wording is identical in every document. | Plan Q-11 requires identical wording so an owner reading any file sees the same question. The README master is the reference a reader will use. The §7 claim is a check result that the files do not support, so the register misstates its own state. | Replace the text column of each of the 28 cells with the README §6 wording verbatim (for OPEN-30 in `azure-r2`, the full README text). Leave the owner and track columns. Then README §7 is true as written. No ID, count or release changes. Owners: Analyst (BRD, PRD), Product owner (release files) |
| L-A | Low | `backlog.md` §7, `US-DN-037` block (heading near line 2228; "ASSUMPTION / OPEN used" line 2234; criteria lines 2240–2242) | The story explains Picking and Shipped, which are set by the nightly 02:00 batch (BR-04, CS-10), but no criterion states "as of the 02:00 batch" (A-04). A-04 is also missing from its "ASSUMPTION / OPEN used" line. | Same risk as the first-review L-4: a status explanation without the freshness statement can read as live. Plan P04 requires BR-04 stories to state the freshness. The story is unplanned, so this has no release effect. | Add criterion 4: "Given Picking or Shipped is explained, When I read the sentence, Then the page states that the status is as of the 02:00 batch (A-04)." Add A-04 to the "ASSUMPTION / OPEN used" line. |
| L-B | Low | `backlog.md` §7, `EN-DN-10` block, "Enables:" line (line 1315) | The Enables field contains a prose sentence ("Exactly 35 stories cite it ... every .NET story except `US-DN-001` and `US-DN-002`"). A reader or script takes both IDs as items this enabler enables. Read mechanically, a `dotnet-r2` enabler enables `dotnet-r1` items, which breaks traceability §8.1 check 6 as written. | The content is correct; the field is ambiguous. Traceability §8.1 check 6 says "no enabler enables an item in an earlier release". The probe reports exactly these two lines and no other. | Move the sentence beginning "Exactly 35 stories cite it" into its own bullet line (for example "* Stories that depend on it: ..."). Leave the Enables line listing enabled items only. |
| L-C | Low | `backlog.md` §2.1 table, row "One track tag" (line 56) | "`track-power-platform` is not used here." The same string appears in §1.3 of the same file, so "here" does not separate the tag from the label. The first review's L-5 fix was applied to README §1.2 only. | Same self-contradiction the first review recorded (L-5), now in the backlog. | Change to "`track-power-platform` is not used as an item tag." (same wording as README §1.2). |
| L-D | Low | `backlog.md` §7, `FT-DN-25` block (source line 2200) | The only source is "(source: OPEN-24)". OPEN-24 is not a knowledge-docs identifier, and no in-scope knowledge-docs ID applies. ES-02 and plan §5.2 require source identifiers on every item. | Literal gap against ES-02. The gap is already disclosed in traceability §8.1 check 8, README §9 ("other points") and `dotnet-r4` §11 item 4, so this is a form gap, not a hidden one. | Keep the source line and say so: "(source: none in knowledge-docs in scope; OPEN-24, informational)". No BA-03 identifier is added. |

### Rulings on the leftovers the coordinator asked about

| Leftover | Ruling | Reason and smallest fix |
|---|---|---|
| **US-DN-037 lacks the "as of the 02:00 batch" wording (A-04)** | **Defect, Low (L-A).** | The story is about Picking and Shipped, which the nightly batch sets, and A-04 (plan P04) requires that every BR-04 story says so. The fix is the criterion and used-line edit in L-A. |
| **BRD and PRD short OPEN labels differ from README wording** | **Defect, Medium (M-1).** | Plan Q-11 requires identical wording in every file. 28 cells differ, and README §7 wrongly says they are identical. Smallest fix: copy the README §6 wording into those 28 cells (M-1). A shorter label is acceptable only if the README text is also changed, which would move the register rather than the files; that is not the smaller change. |
| **US-AZ-005 dependency differs: rank table versus item block** | **Not a defect.** | The rank row reads "`US-AZ-001` to `US-AZ-004`", a range that expands to 001, 002, 003, 004. The item block lists "`US-AZ-001`, `US-AZ-002`, `US-AZ-003`, `US-AZ-004`". The probe compares the expanded sets: identical. The "(US-AZ-001, US-AZ-004)" form does not appear in the final files. No fix required. If the team wants grep-friendly rank rows, the explicit list would be the same set. |

Notes that are not findings:

* `US-DN-001` and `US-DN-002` do not depend on EN-DN-10. They are staff-only stories in `dotnet-r1`, which is earlier than the enabler. This is correct under the no-later-release rule, and the EN-DN-10 block says so.
* `EP-DN-03`, `EP-DN-08` and `FT-DN-26` cite BR-04 without the freshness sentence. A-04 applies to stories, and the features are not stories. `FT-DN-11` and `US-DN-036` carry the sentence.
* The rank-table sentence "each such story cites it (A-22)" is the plan's ordering rule with A-22 as the stated basis (C5 tenant-isolation finding). It is consistent across backlog, PRD and `dotnet-r2`.
* `azure-r3` §7 says "The report in `docs/migration/` lists ...". That is the ES-09 location for a future report. It describes an acceptance criterion, not an existing file.
* Q-08 wording was re-checked in this pass: no positive cross-track "requires", "blocked by" or "waits for" wording in any file.

## 6. Plan deviations (charter response format)

* Planned, not done: none. All 13 files exist; no extra file under `docs/`.
* Done differently, now recorded: release status wording uses "awaiting product owner approval; not yet tagged" (plan: "awaiting approval - not tagged"); four-week baseline recorded as A-44; NFR-04 attribution recorded through A-02 and BRD §4 (not the verbatim words suggested in L-7).
* Done, not planned, disclosed: `EN-AZ-14`, `EN-DN-15` (plan J-1, J-2); A-27..A-46; OPEN-27..OPEN-33; `FT-DN-26`, `EP-DN-08` (A-35, A-36); `US-AZ-020` as next free number.
* Done, not planned, not disclosed: none found in this pass.

## 7. Conditions honored

Not applicable. No council conditions were supplied with this dispatch.

## 8. Review record

This file: `C:\demos\northwind-workshop\.copilot-tracking\reviews\product-documents-review-2.md`.

Scratch artefacts (not product documents), all in `.copilot-tracking\reviews\probe-nw-product-docs\`: `check-final.py` (register, items, rank, Appendix A, A-/OPEN- wording, secrets, coverage), `check-final-2.py` (strict criteria order, owners, release §7.1 vs rank, PRD §8, traceability §3.1/§3.2, forbidden wording, status), `check-oos.py` (out-of-scope context, MVE identifiers), `check-enables.py` (Enables order, NFR-06 removal). The earlier `check-backlog.ps1`, `check-crossdoc.ps1` and CSV files from the first review were not modified.

## 9. Return to coordinator

| Item | Value |
|---|---|
| Verdict | Fail (single literal criterion: Q-11, finding M-1; no Critical or High) |
| Next step | Owners apply M-1 (28 cells), then L-A to L-D. Re-review only the touched lines and re-run `check-final.py` and `check-final-2.py` |
| Expected after fixes | Pass-With-Findings if no Low item is accepted as a waiver; Pass if the owner accepts the Low items |
| Release approval | Not affected by these findings beyond the above. The approval step and the tagging remain outside this review |
