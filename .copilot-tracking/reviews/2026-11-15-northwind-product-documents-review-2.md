<!-- markdownlint-disable-file -->
# Review 2: Northwind product documents (verification of fixes)

Verdict: Pass-With-Findings

Requested verdict scale: **Approve-With-Fixes**. The product owner should not approve any release until RV2-01 has a coordinator decision and RV2-02 to RV2-04 are fixed. No Critical finding was found.

Task: NW-PRODUCT-DOCS-2026-11-15. Record date: 2026-11-15 (review 2 of the same task). Reviewed on disk; nothing committed, tagged or deployed.

## Executive Summary

* Most first-review fixes are in place. The window value (RV-001), the BR-13 build items (RV-002), the registers (RV-004 and RV-005 in part), the PRD start-order wording (RV-006), the RG, PNFR and RC citations (RV-007), the C-02 quote (RV-008) and the figure labels (RV-009) are fixed or mostly fixed. RV-010 is resolved. RV-011 is carried as O-31, as the coordinator decided.
* The rework added four Major findings. Three come from the new items and decisions, and one is an old conflicting definition that the first review did not catch.
  * **RV2-01 (Major, decision):** the azure-r3 window now ends 27 June 2027. That window contains the 6 and 13 June rehearsal Sundays, but A-53 says rehearsals and live cutover follow approval. The window therefore allows rehearsals before approval.
  * **RV2-02 (Major):** the PRD gives EA-15 the wrong "serves" mapping (FR-106, FR-116). The backlog and the coordinator say FR-112, FR-116. FR-112 does not list EA-15, and FR-106 does.
  * **RV2-03 (Major):** the azure-r2 "Stop" rule says EA-15 does not depend on the data tier. The backlog says EA-15 takes its database settings from EA-05, which waits on the MVE-01 decision.
  * **RV2-04 (Major):** O-26 means different things in the backlog register of record and in the BRD, PRD and experiments copies.
* Counts hold everywhere I checked: 144 items = 12 epics, 39 features, 57 stories, 36 enablers; Azure 54; azure-r2 20; azure-r3 13; per-release counts match backlog section 3.
* The C1 release table is identical in BRD 10.2, PRD 6.2, backlog 1.1 and the release headers, with azure-r3 ending 27 June 2027. No "31 May" survives in any product document. The plan's own C1 (plan line 513) still says 31 May, so the plan contract has not been amended.
* Git state is clean: no `product/*` tag, no commit touches `docs/product/`, and the product documents are untracked.
* Review execution: **Partial**. Mechanical checks cover all deliverables. Manual line-by-line prose reading was not done, and the Scribe history entry was not checked (see Checks Run and Unverified).

## What You May Not Know

* **The sequencing conflict (RV2-01) comes from the D1 decision, not from a document error.** The coordinator extended the window to include the cutover Sundays. A-53 and EA-16/AC6 still say those Sundays follow approval. The two cannot both hold unless approval is due before 6 June 2027. The coordinator needs to choose how to resolve it; this review does not change the decision.
* **The plan has not been updated for D1 and D2.** The plan's preamble says a changed canonical value changes the plan first. Plan C1 (line 513) still says "1 Apr to 31 May 2027", plan C2 (line 525) still says `dotnet-r2` "can start after" `azure-r2`, and C5 and C9 do not list FEAT-113, FEAT-114, EA-15, EA-16, A-58 or A-59. Deliverables are correct against the coordinator's decisions; the contract is not.
* **Two first-review findings in the review-1 script were false positives.** The enabler stories for EN-13 and EP-04 use "As the …", which is an accepted form. They are not defects.
* **The mechanical copy comparison flagged 99 token differences** between register copies and the backlog register of record. Most are pointer or wording differences (section numbers, "BRD" against "PRD" as a source). I read the coordinator-named ids and every new id in the BRD, PRD and backlog, and listed the two that differ in meaning. I did not read the rest one by one.
* **The changes record named in the plan is still missing.** `.copilot-tracking/changes/` does not exist. The plan's canonical review path (`.copilot-tracking/reviews/logs/2026-11-15/...`) does not exist either; this record is at the caller's path.
* **Model identity:** this session does not expose the model name, so I cannot verify it and I do not state one.

## Findings and Proposed Routes

Ordered by severity. Severity uses Critical, Major and Minor. Each finding gives the smallest fix I can see. Owners follow the squad roles in the plan. Line numbers are as on disk.

| ID | Severity | File and section | Evidence | Smallest fix | Route and owner |
|----|----------|------------------|----------|--------------|-----------------|
| RV2-01 | Major | `releases/azure-r3.md` §2 (L52), §4 (L48, L112), §11; `backlog.md` A-53 (L1899), EA-16/AC6 (L704), A-58 (L1904), O-27 (L1939); BRD A-53 (L484), PRD A-53 (L719) | The window "1 Apr to 27 June 2027" is the period by which content is complete and ready to approve (A-42). The same release says "the rehearsals, the live cutover and the recovery test follow approval" (A-53, L48, L112). The rehearsal Sundays, 6 and 13 June 2027, fall inside the window. The window therefore allows approval after the first rehearsal. | Coordinator decides. Option A (recommended): set the approval-due date before 6 June 2027 (the first rehearsal Sunday), so the window ends there. Keep the 6, 13, 20 and 27 June dates in the rehearsal plan as planned execution after approval, and restate A-58 as a schedule margin check. Option B: keep 27 June and delete "follow approval" from A-53, EA-16/AC6, azure-r3 L48 and L112, and O-27. Option B moves execution before approval, which the release says it does not claim. | rpi-plan (change C1 first), then six documents. Owner: Lena Varga (approver), Marc Dubois (A-58, O-27). |
| RV2-02 | Major | `product-requirements.md` §9.1 EA-15 (L500), §7 FR-112 (L354) and FR-106 (L343) | Backlog EA-15 "Serves: FR-112, FR-116" (`backlog.md` L506). PRD §9.1 EA-15 says "FR-106, FR-116". PRD FR-112 items are "EA-10; X-01, X-02; A-37", so EA-15 is missing there. PRD FR-106 items include "EA-15", which should not be there. EA-16 is consistent in both (PRD L501, backlog L695: FR-106, FR-116). | PRD L500: serves `FR-112`, `FR-116`. FR-112 items: add `EA-15`. FR-106 items: remove `EA-15`. | rpi-implement (PRD). Owner: analyst (PRD Builder). |
| RV2-03 | Major | `releases/azure-r2.md` "Stop" row (L95) against backlog EA-15 Dependencies (`backlog.md` L515) and azure-r1 L159 | The Stop row says "`EA-04`, `EA-07`, `EA-12` and `EA-15` do not depend on the data tier". EA-15 says it "takes its database settings from the data-tier record `EA-05` once that is decided". EA-05 waits on the MVE-01 decision (azure-r1 L159). EA-15 has gate "none", so the Stop rule as written lets EA-15 continue while the data tier is stopped. | Either remove EA-15 from the "do not depend" list and add it to the items that pause, or state that EA-15 uses EA-05 only at finalisation and can proceed on the hosting definition alone. Pick one and make the backlog gate match. | rpi-implement (azure-r2 §5 and backlog EA-15 gate). Owner: Ahmed Benali. |
| RV2-04 | Major | O-26 register rows: `backlog.md` §7 (L1938) against BRD §13 (L525), PRD §15 (L774), `experiments.md` (L382, L155) | Backlog §7 (register of record): "Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07)." BRD and PRD add "confirm the proposed goal owners" and "name who speaks for customer users". Experiments L155 relies on O-26 for the customer representative. One id, two questions. | Put the BRD/PRD wording into backlog §7 (the register of record), or split the customer-representative question into a new O-id and cite that in experiments L155. | rpi-implement (backlog §7, BRD, PRD, experiments). Owner: Lena Varga. |
| RV2-05 | Medium (carried from RV-005, partly resolved; RV-005 was Medium in review 1) | `backlog.md` §7 (register of record) against release files §8 | Eleven release-local ids are in release files but not in backlog §7: A-D1-02, A-D2-01, A-D2-02, A-D3-01, A-D3-02, O-D2-02, O-D3-01, O-D3-02, AZ1-O2, AZ2-O1, AZ3-O1. Three release-local ids are registered: A-D1-01, O-D2-01, AZ1-O1. | Add the eleven rows to backlog §7 with the owner printed in each release file's §8. Keep the same text. | rpi-implement. Owner: Squad Coordinator (confirm register of record). |
| RV2-06 | Minor | `.copilot-tracking/plans/2026-11-15/northwind-product-documents-plan.md` C1 (L513), C2 (L525), C5, C9 | C1 still says azure-r3 "1 Apr to 31 May 2027". C2 still says `dotnet-r2` "can start after" `azure-r2`. C5 ranges and C9 do not list FEAT-113, FEAT-114, EA-15, EA-16, A-58, A-59, O-27 or O-31. The plan says a changed canonical value changes the plan first. RC-06 compares deliverables to C1, so it fails if the plan is the reference. | Coordinator amends the plan for D1 and D2 (C1 window, C2 wording, C4 and C5 items, C9 ids). Do not edit the deliverables again for this. | Squad Coordinator. |
| RV2-07 | Minor | A-37 in backlog §7 (L1883), BRD (L468), PRD (L703), `releases/azure-r2.md` (L200), `dotnet-r2.md` (L179, L236); PRD §6.2 (L245) | Register and copies say "after `azure-r2`". PRD §6.2 and C2 say "once `azure-r2` is approved", which is the RV-006 wording. The meaning is the same, but the register should match the fix. | Change A-37 to "after `azure-r2` is approved" in every copy. | rpi-implement. Owner: Ahmed Benali. |
| RV2-08 | Minor | A-58 in backlog (L1904), BRD (L489), PRD (L724), `releases/azure-r1.md` (L205), `azure-r2.md` (L211), `azure-r3.md` (L193); O-27 in BRD (L526) | A-58 says "the cutover Sunday fall inside it" (singular). The live cutover and fallback Sundays are two (20 and 27 June). BRD O-27 drops the Sunday dates that the other copies list (backlog L1939, PRD L775, azure-r3 L207). | Change "the cutover Sunday" to "the cutover and fallback Sundays (20 and 27 June 2027)" in A-58, and make BRD O-27 match the other copies. | rpi-implement. Owner: Marc Dubois. |
| RV2-09 | Minor | `backlog.md` EA-16 Dependencies line (L705) against `releases/azure-r3.md` §8 (L93) | Release says EA-16 "is written against ASSUMPTION: A-21 (PaaS preferred, VM fallback)". The backlog "Relies on" for EA-16 is "A-30, A-33, A-53, A-59". A-21 is missing. | Add A-21 to the backlog "Relies on" for EA-16. | rpi-implement. Owner: Ahmed Benali. |
| RV2-10 | Minor | `traceability.md` EA-15 and EA-16 rows (L141, L144) | The traceability rows name STORY-143 and STORY-170 as covering EA-15, and STORY-170 and STORY-120 for EA-16. Neither story's backlog block refers to EA-15 or EA-16 (STORY-143 at L629, STORY-170 at L724). STORY-170 is in azure-r3, after EA-15 (azure-r2). | Either add EA-15 and EA-16 to those stories' "Relies on" or "Covers" fields, or change the traceability rows to name only the items that refer to them (EA-10 for STORY-143 is already the enabler link). | rpi-implement. Owner: Functional Planner. |
| RV2-11 | Minor | PRD §7 FR-201 items (L379) against PRD §9.2 EN-13 (L519) and backlog EN-13 | FR-201 items list "EN-01, EN-03, EN-05, EN-08; X-14; O-20", but EN-13 serves FR-201 in the enabler table and the backlog. Pre-existing from the first review. | Add `EN-13` to the FR-201 items cell. | rpi-implement. Owner: analyst (PRD Builder). |
| RV2-12 | Minor | EA-12 priority (backlog register and azure-r2) against rule A-49 | A-49 says "an enabler that serves only another track's requirements is Should". EA-12 is Azure and serves only BR-09 (.NET track, Could). EA-12 is Could. The rule and the item disagree. | Set EA-12 to Should, or amend A-49 and record the reason. Coordinator decides. | Coordinator decision, then rpi-implement. Owner: Lena Varga. |
| RV2-13 | Minor (RV-003 and RV-011 residual) | BRD header lines 11, 12, 19; PRD header lines 11, 14 | BRD: `business_goal_smart_status: "deferred"` (L11), `diagram_format: "none"` (L12), and `requirement_id_prefixes` with `ac: "AC"` (L19) although the BRD has no AC items. PRD: `product_goal_smart_status: "deferred"` (L11) and `diagram_format` (L14). The FR-to-AC threshold has been removed from the BRD (DD-03, L66, says not applicable), which resolves RV-003's failing metric. | Remove the unused template keys from both headers, or mark them not applicable. The licence line stays under O-31. | rpi-implement. Owner: Lena Varga (O-31 for licence). |
| RV2-14 | Minor (RV-009 residual) | `releases/azure-r1.md` L93; `backlog.md` L474 | The EUR 300 headroom is labelled "derived" in `experiments.md` L97 only. The two other copies state "EUR 300" without the label. | Add "(derived: EUR 1,500 less EUR 1,200)" to both, as in experiments L97. | rpi-implement. |
| RV2-15 | Minor (RV-004 and RV-007 residual) | `releases/azure-r1.md` §8 row at L207 and EC-3 (L154); `releases/dotnet-r1..r3.md` and `azure-r1..r3.md` (G-, T-, OQ- citations); `backlog.md` §7 and `experiments.md` §5 named as register of record | The row at L207 groups MVE-A-01, MVE-A-03 and MVE-A-04 in one cell; MVE-A-01 is cited at L154 without its own row. Release files cite G-01, G-03, G-05, G-08, G-10 (defined only in the intake review, which the product set does not name) and T-03, T-08, T-10, T-13, T-14, T-17 (defined in PRD §11) without a local row. Backlog §7 names itself as the register of record, but it does not define G-, T- or OQ- ids. | Split the L207 row into one row per id. Name the intake review as the register of record for G-ids, and PRD §11 for T-ids, in each file that cites them. | rpi-implement. Owner: Squad Coordinator. |
| RV2-16 | Minor | BRD §13 note (L532); PRD §15 note (L745) | Text addressed to the coordinator: "The coordinator must add O-26 to O-31 and A-49 to A-59 to the plan's register where it keeps one." The rows now exist, so the note is stale and does not belong in a product document. | Delete the sentence, or replace it with a status note that the rows exist. | rpi-implement. |
| RV2-17 | Minor | `traceability.md` §9 (L236) | "ASSUMPTION ids used: A-01 to A-06, A-10 to A-25, A-27, A-29 to A-59" leaves out A-07, A-08 and A-09, which the BRD, PRD, experiments and backlog cite. | Change the list to "A-01 to A-25, A-27, A-29 to A-59" (A-26 and A-28 unused). | rpi-implement. |
| RV2-18 | Minor | Register copies: A-49 (BRD L480, PRD L715 against backlog §7 L1895); A-51 (backlog §7 against BRD and PRD) | A-49: the BRD and PRD add "(so `EN-14` and `FR-240` are Should)". A-51: backlog §7 omits the "Picking means exported" and "Delivered is set only by a staff action" facts that the BRD and PRD copies carry. ES-03 and plan C9 require verbatim copies. | Copy the register-of-record text into each copy (or move the extra text into backlog §7 first). | rpi-implement. |
| RV2-19 | Minor | `backlog.md` §2 (L128, L148); plan C5 (feature ranges) | FEAT-113 sits under EPIC-103 and FEAT-114 under EPIC-104, outside the C5 feature ranges (FEAT-106 to FEAT-109 and FEAT-110 to FEAT-112). Ids are not reused, so the numbers are valid. The exception is not explained in C5 or in the backlog "How to read" section. | Add a one-line note to backlog §1 and the C5 amendment (RV2-06). | rpi-implement and Squad Coordinator. |
| RV2-20 | Minor (RV-002 residual wording) | BRD §5 BR-13 row (L212); PRD §16.1 BR-13 row (L842); `releases/azure-r3.md` L101 against `traceability.md` L111 | BRD and PRD say "build items" for EA-15 and EA-16. The traceability note says "covered by designs, procedures and runbooks only", and ES-27 allows validated design only. | Use "design items" (or "design and infrastructure code validated locally") in BRD and PRD where "build items" appears. | rpi-implement. |

## First-Review Findings: Status

| First-review ID | Status now | Evidence | Remaining gap |
|-----------------|------------|----------|----------------|
| RV-001 (window) | Fixed in the deliverables; reopened in part by RV2-01 | C1 identical in BRD 10.2 (L347), PRD 6.2 (L231), backlog 1.1 (L47), azure-r3 frontmatter (L13) and §2 (L52); "Anything after 27 June 2027" (azure-r3 L115). Zero "31 May" hits across the 11 product files. | Sequencing (RV2-01); plan C1 (RV2-06). |
| RV-002 (BR-13 build) | Fixed by option (a): the register gained EA-15 and EA-16 | EA-15 backlog L129 (register), L504 to L515 (detail); EA-16 L149, L693 to L705; PRD §9.1 L500 and L501; azure-r2 L66; azure-r3 L70; traceability BR-13 row L67 and note L111. | EA-16 "Relies on" omits A-21 (RV2-09); "build" wording (RV2-20); covering-story links (RV2-10). |
| RV-003 (BRD threshold) | Partly fixed | Threshold key gone from the BRD header; DD-03 (L66) says not applicable. | Template keys remain (RV2-13). |
| RV-004 (release ids) | Fixed for A and O ids | Script: every A and O id cited in each release file has a local row. EXP A-14 and O-10 to O-14 covered by backlog §7, which EXP names as register of record. | MVE-A grouping and G, T and OQ citations (RV2-15). |
| RV-005 (registers) | Partly fixed | BRD §12 and §13 and PRD §14 and §15 contain A-49 to A-59 and O-26 to O-31 (script: none missing). | Eleven release-local ids not in backlog §7 (RV2-05); O-26 meaning (RV2-04). |
| RV-006 (start order) | Fixed | "start after" absent from every product document; PRD §6.2 L245 now says "once `azure-r2` is approved (A-37)". | A-37 register wording (RV2-07). |
| RV-007 (RG, PNFR, RC) | Fixed for the named families | Grep for RG-0n, PNFR-, RC-0n and PFR- across `docs/product/` returns no hits. | G-, T- and OQ- citations (RV2-15). |
| RV-008 (C-02 quote) | Fixed | BRD L320 equals `knowledge-docs/business-case.md` L95 (verbatim, "(ESU)" removed); ESU defined in the BRD glossary (L583). | None. |
| RV-009 (labels) | Partly fixed | PRD L208 non-goal reworded; "5 to 8" sample labelled ASSUMPTION MVE-A-05 (EXP L46, L155, L183, L191, L359); growth month count stated as an assumption in MVE-A-03 (EXP L357); EUR 300 labelled derived in EXP L97. | EUR 300 unlabelled in azure-r1 L93 and backlog L474 (RV2-14). |
| RV-010 (readability) | Fixed | WCAG expanded at EXP L171 (first use), VM at L86, CSV at L47; AC first used at PRD L675 with its expansion, and defined in the PRD glossary (L887). Experiments prose averages 16.8 words per sentence with 7 sentences over 30 words. Different method from review 1 (19.2 and 19), so indicative only. | None. |
| RV-011 (licence, template keys) | Carried OPEN as O-31 (as decided) | O-31 in BRD §13 (L530) and PRD §15 (L779). Licence line unchanged (BRD header L23, PRD header L26). | Template keys (RV2-13). |

## New Items: EA-15 and EA-16

| Check | EA-15 | EA-16 | Result |
|-------|-------|-------|--------|
| Id and type | enabler | enabler | Consistent: backlog §2, §4, PRD §9.1, release, traceability. |
| Title | "Host the Order Desk web application in the test and production environments" | "Migrate the NorthwindOrders database to the chosen data tier and rehearse the move" | Identical across backlog, PRD, release file. |
| Track tag (one) | `track-azure` | `track-azure` | Pass. |
| Release tag | `azure-r2` (release file row, register) | `azure-r3` | Pass; release tables equal the register. |
| Parent and epic | FEAT-113, EPIC-103 | FEAT-114, EPIC-104 | Pass; ids outside C5 ranges (RV2-19). |
| Priority and rank | Must, rank 15 | Must, rank 29 | Pass; rank unique in Azure 1 to 36. |
| Sources | BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25 (backlog, PRD, traceability, release: same set) | BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23 (same in all four) | Pass. All source ids exist in `knowledge-docs`. |
| Gate | none (O-03 for runtime) | MVE-01 (decision before commit) | Pass in backlog, PRD, release. Stop-rule conflict for EA-15 (RV2-03). |
| "Serves" (FR) | Backlog: FR-112, FR-116. PRD §9.1: FR-106, FR-116. | Backlog: FR-106, FR-116. PRD §9.1: FR-106, FR-116. | **Mismatch for EA-15 (RV2-02).** EA-16 consistent. |
| PRD FR rows | FR-112 items do not list EA-15; FR-106 items do. | FR-106 and FR-116 items list EA-16. | Mismatch for EA-15 only (RV2-02). |
| Dependencies | EA-01, EA-03, EA-05 (settings), X-02, X-07, O-03 | EA-05, EA-08, EA-15, X-03, A-30, A-33, A-53, A-59, O-03, O-15, O-27 (no A-21) | EA-15 vs Stop rule (RV2-03). EA-16 missing A-21 (RV2-09). |
| Acceptance criteria | 5 (Given/When/Then, each `EA-15/AC<n>`) | 6 (each `EA-16/AC<n>`) | Pass. |
| Covering stories (traceability) | STORY-143, STORY-170 | STORY-170, STORY-120 | Neither story refers to the item (RV2-10). |

## Counts and Release Tables

| Count | Expected | Found | Result |
|-------|----------|-------|--------|
| Register total | 144 | 144 | Pass |
| Epics, features, stories, enablers | 12, 39, 57, 36 | 12, 39, 57, 36 | Pass |
| Azure items | 54 | 54 (4 epics, 14 features, 20 stories, 16 enablers) | Pass |
| azure-r2 | 20 | 20 (1 epic, 5 features, 7 stories, 7 enablers) | Pass |
| azure-r3 | 13 | 13 (1 epic, 4 features, 5 stories, 3 enablers) | Pass |
| All releases | r1 21, r2 20, r3 13; .NET r1 23, r2 21, r3 13; unplanned 33 | 21, 20, 13; 23, 21, 13; 33 (30 BA-03 and 3 `EPIC-204`) | Pass |
| Planned items in release files | 111, each in one file | 111 | Pass |
| Traceability reverse table and release headers | 21, 20, 13 | 21, 20, 13 | Pass |
| Enabler split in PRD §9 and traceability | 16 Azure, 14 .NET, 6 Power Platform | 16, 14, 6 | Pass |
| Stale totals | none | none ("140", "37 features", "34 enablers" absent) | Pass |

## Checks Run and Unverified

| Check | Method | Result |
|-------|--------|--------|
| (1) RV-001 to RV-010 fixed, RV-011 OPEN | Targeted greps and line reads (see status table) | RV-001 to RV-010 checked; RV-011 OPEN as O-31. Four Major and nine Minor findings (above). |
| (2) New items consistent | Register and detail blocks compared to PRD §7 and §9, release files, traceability (`r2_checks.py`) | EA-15 "Serves" mismatch (RV2-02); other fields pass. |
| (3) C1 table identical | Parsed the C1 rows from BRD 10.2, PRD 6.2, backlog 1.1, plan C1 and release headers (`r2_checks_b.py`) | Identical in deliverables; plan C1 differs (RV2-06). |
| (4) Mechanical re-run of review-1 checks | `check_backlog.py` (review 1) and `r2_checks.py` | 28 of 28 BR and NFR covered; 39 traceability rows; one track tag per item (144); release tags only on 111 planned items; release tables equal the register on id, title, priority, rank and tags; 57 stories with As a / I want / so that and at least two Given/When/Then; 36 enablers with at least one Given/When/Then; all 121 cited source ids exist in `knowledge-docs`. Two flags (EN-13, EP-04) are false positives. |
| (4) Cited ids defined | Table first-cell scan per file, with backlog §7 as fallback and register-of-record sentences | Undefined cites are covered by the findings above (RV2-05, RV2-15, RV2-17). A-26 and A-28 are stated as unused (BRD L430); X-16 to X-19 are stated as an unused range (BRD L406, PRD L537); no finding. |
| (4) Conflicting definitions | Numeric, date and id token comparison of each copy against backlog §7; manual read of A-37, A-49, A-51, A-53, A-54, A-58, A-59, O-26 to O-31 and O-27 | Meaning conflicts: O-26 (RV2-04). Drift: A-37 (RV2-07), A-58 and O-27 (RV2-08), A-49 and A-51 (RV2-18). |
| (4) Calendar | Python `datetime` | 6, 13, 20 and 27 June 2027 are Sundays; 30 June 2027 is a Wednesday; 31 May 2027 is a Monday. |
| (5) Nothing deployed, tagged or committed | `git tag -l 'product/*'`; `git log -- docs/product`; `git status`; text scan for deployment and tenant claims | No tag. No commit touches `docs/product/` (HEAD is the squad tracking commit `2a7ff5a`). `docs/` untracked. Every "deployed" or "applied" statement is a negation (ES-27). |
| (6) BA-03 unplanned, no waits | Register and release files; "wait" scan of the six release files | 30 BA-03 items: track tag only, release `unplanned`, no release tag, no BA-03 release file. "Wait" appears only as "none is a wait", "never waits", or the MVE-01 gate (azure-r1 L159). No release waits on another track. |
| Re-run of the C10 checks RC-01 to RC-16 | Summary below | See table |
| Manual prose read of all product documents | Not done | **Unverified.** |
| Backlog §5 and §6 (unplanned list, ES-39 mapping) | Not re-read | **Unverified.** |
| Scribe history entry for this stage | `.copilot-tracking/squad/history/Squad Reviewer.md` exists; not read or checked | **Unverified** (squad state is read-only to this review). |
| Implementation changes record | `.copilot-tracking/changes/` absent | Still missing. |
| Denied probes | None. No runtime probe was attempted and none was denied. | Not applicable. |

### C10 checks, re-run status

| Check | Status in this pass |
|-------|---------------------|
| RC-01 coverage | Pass (28 of 28; not-covered table "none") |
| RC-02 source cites | Pass (every story and enabler has a source line; ids verbatim) |
| RC-03 one track tag | Pass |
| RC-04 release tags only on planned items | Pass |
| RC-05 one release per item; epic and feature tags equal children | Pass; covered ids vs C1 checked by table, not by line-by-line read |
| RC-06 canonical consistency | Pass for deliverables; plan C1 still differs (RV2-06) |
| RC-07 story quality | Pass for structure; readability not re-read |
| RC-08 mandatory acceptance content | **Unverified** (not re-read; EA-15 and EA-16 acceptance criteria read and present) |
| RC-09 style | Partly: RV-010 fixed; RV-009 label residual |
| RC-10 traceability table | Pass for structure; §9 id list (RV2-17) |
| RC-11 release file content | Partly: EA-15 Stop row (RV2-03); other sections not re-read |
| RC-12 BA-03 handling | Pass (X-20 to X-27 defined in PRD; no placeholder release file) |
| RC-13 no deployment, secrets or personal data | Pass for deployment wording; secrets and personal-data scan not repeated in this pass (**unverified** for this pass) |
| RC-14 location | Pass (11 files at C8 paths) |
| RC-15 git state | Pass |
| RC-16 MVE completeness | **Unverified** beyond id presence (MVE-01 to MVE-03 and MVE-A-01 to MVE-A-05 present) |

## Plan Deviations

* **Planned, not done:** the plan's canonical review path (C8 D7) is not used; this record is at the caller's path. The changes record is missing. Release-local ids are not all in backlog §7 (RV2-05).
* **Done, not planned:** D1 and D2 are applied to the deliverables but not to the plan (RV2-06). New ids A-58, A-59, O-27 and O-31 are recorded in the deliverables.
* **Done differently:** the "serves" mapping for EA-15 in the PRD differs from the backlog (RV2-02). The Stop rule for azure-r2 differs from the backlog dependency (RV2-03).

## Conditions Honored

Not applicable. No council condition was supplied with this dispatch.

## Review Record

* Task ID: NW-PRODUCT-DOCS-2026-11-15 (review 2).
* Scope reviewed: BRD, PRD, experiments, backlog, traceability, six release files; plan C1 to C11 and RC-01 to RC-16; review 1 (RV-001 to RV-011); knowledge documents (business case C-02 quote and source-id existence); git state.
* Review execution: **Partial** (mechanical and targeted reads; no manual full prose read).
* Read-only: this record and the probe scripts in `.copilot-tracking/reviews/probe-2026-11-15/` (`r2_checks.py`, `r2_checks_b.py`, outputs `r2_out.txt` and `r2_out_b.txt`) are the only files written. No deliverable, plan, research, squad state or knowledge document was changed.
* Tool calls: about 50 in this session (estimate; calls were not logged individually).
* Model identity: not exposed to this session; not verified.
* Record path: `.copilot-tracking/reviews/2026-11-15-northwind-product-documents-review-2.md` (the caller's path).

### Reviewer Self-Check

* [x] Every first-review finding RV-001 to RV-011 has a status with evidence.
* [x] Every new id (EA-15, EA-16, FEAT-113, FEAT-114, A-58, A-59, O-27, O-31) was compared across the documents that cite it.
* [x] Each finding has a severity, a file and section, evidence and the smallest fix.
* [x] Checks run and unverified items are listed separately.
* [ ] Full manual prose read of the product documents: not done (unverified).
* [ ] Scribe history entry: not checked (unverified).
* [x] Only this record and the probe scripts were written.
