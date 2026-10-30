# Review: Northwind product documents (BA-01 Azure, BA-02 .NET)

| Field | Value |
|---|---|
| Stage | Review (closing stage), Squad Reviewer. Plan deliverable D9 |
| Date | 2026-10-30 |
| Under review | 13 files in `docs/product/`: `business-requirements.md`, `product-requirements.md`, `experiments.md`, `backlog.md`, `traceability.md`, `README.md`, `releases/azure-r1..r3.md`, `releases/dotnet-r1..r4.md` |
| Checked against | `knowledge-docs/business-case.md`, `current-state.md`, `engineering-standards.md`; plan `.copilot-tracking/plans/2026-10-30-northwind-product-documents-plan.md` (criteria Q-01..Q-17); research and intake review; facts spot-checked in `src/` and `database/` |
| Implementation state | Read-only. No product document was modified. Git status shows only untracked `docs/` and `.copilot-tracking/`; no tracked file in `src/`, `database/` or `knowledge-docs/` changed; no `product/*` tag exists |
| Method | Script checks (read-only, scratch directory `.copilot-tracking/reviews/probe-nw-product-docs/`) over all 133 register rows, all 133 item blocks, all 7 release tables, the PRD release sections, the traceability tables and the cross-document ID set. Targeted reads of the source-of-truth, plan, BRD, traceability, README, experiments, and the register. Facts checked against source files |
| Model identity | Not known to the reviewer |
| Tool calls | About 125 (approximate) |
| Paths written | This review file. Scratch only, inside the authorised probe directory: `check-backlog.ps1`, `check-crossdoc.ps1`, `backlog-register.csv`, `backlog-items.csv`. Nothing else |

Verdict: Fail

Basis for the verdict. The plan (section 9) says the review "passes only if all are true". Q-02 and Q-17 are not literally met (findings M-2 and L-1). Finding H-1 is High and the plan (section 9) requires return to the owner before release approval. The fixes are bounded: local edits to named lines or item blocks, with no change to counts, release membership, tags or release structure. A re-review of the touched items is enough after the fixes. Nothing found blocks the plan's approach itself.

## 1. Findings (ordered by severity)

| ID | Severity | File and location | Finding | Why it matters | Smallest fix |
|---|---|---|---|---|---|
| H-1 | High | `backlog.md` §7, EN-DN-10 block (line 1315 claims "every portal story that shows or changes data cites it"). Affected stories: `US-DN-005, 007, 009, 010, 011, 012, 014, 015, 017, 018, 019, 020, 021, 023, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037` | 27 of 37 .NET stories do not cite `EN-DN-10` in their own "Depends on" line or in their criteria. Thirteen of them are in `dotnet-r2`. The plan (P04, section 7) requires that `EN-DN-10` "precedes every portal data story and is cited by it". The enabler's own text overstates coverage. Of the 27, 22 reach `EN-DN-10` through chains of "Depends on" lines (for example `US-DN-007` to `US-DN-006`), checked by script. Five do not: `US-DN-005, 019, 026, 027, 034`. None of the five reads customer order data. `US-DN-019` (audit history) should also depend on `EN-DN-10` if audit records can be viewed | Tenant isolation is the top portal risk (BRD R-03, High/High; per A-22 the code has no check that a request belongs to the signed-in customer's company). A developer who builds `US-DN-007` or `US-DN-009` from its text alone is not told that company isolation comes first (ES-05) | Add `Depends on (same track): EN-DN-10` to each listed story that reads or shows customer data (the five above are excluded, except `US-DN-019` if audit history is viewable). The source-ID lines need no change, because `EN-DN-10` is not a source ID. Or, at minimum, reword line 1315 to "reached through Depends-on chains, except as noted". Re-run the dependency check |
| M-1 | Medium | `backlog.md` §6 and §7: all 29 enabler blocks (`EN-AZ-01..14`, `EN-DN-01..15`) | 84 of 345 acceptance criteria are "Given ... Then ..." with no "When". Every story (`US-`) criterion is full Given/When/Then. ES-05 requires "acceptance criteria in Given / When / Then form". §1.1 of the backlog itself says rule-style criteria need a "When" | Each enabler still has at least one full Given/When/Then, so Q-09 holds literally. The gap is form, and it weakens testability of the preparation work | Insert "When <the check runs>" in each of the 84 criteria (for example "Given the templates, When `az bicep build` runs, Then ..."). Lines found by the probe (`check-backlog.ps1`, criteria check) |
| M-2 | Medium | `backlog.md` lines 142, 145, 2196-2200 (FT-DN-25, EP-DN-08), 2412, 2437. `business-requirements.md` line 115. `product-requirements.md` line 184. `releases/dotnet-r4.md` Appendix A and §11 item 4. `experiments.md` line 111 (cites CS-28) and line 266 (cites CS-26). `traceability.md` line 213 (check 8) | BA-03 identifiers are cited as sources in planned-tracking content. `CS-27` and `ES-36` (FT-DN-25, EP-DN-08, OPEN-24) and `CS-26` and `CS-28` (experiments) are all in the out-of-scope list (`CS-24` to `CS-28`, `ES-32` to `ES-37`) in BRD §3.2, PRD §3.2, traceability §6 and README §1.2. `traceability.md` check 8 says no out-of-scope identifier is cited by any item. That statement is false | Q-02 says BA-03 appears "only in out-of-scope lists (and OPEN-24 as informational)". The traceability check overstates the result. Readers would find a source ID that the scope section says is out of scope | Remove `CS-27, ES-36` from the source line of FT-DN-25 and EP-DN-08 (keep the OPEN-24 text, without source IDs). Replace `CS-26` and `CS-28` in experiments with in-scope sources (for example `ES-20` and `NFR-03` for the EU data row; `CS-10` for the Antwerp contact row). Correct traceability check 8 to name what is actually cited. Register and Appendix A "Other" columns do not list CS-IDs, so no count changes |
| M-3 | Medium | `business-requirements.md` line 72 (§2.2 note) and R-11 (line 302). `product-requirements.md` line 470 (`releases/dotnet-r2` section §8.5). `traceability.md` line 125 (SM-01 row). `experiments.md` line 317 (B4: "This is arithmetic"). `releases/dotnet-r4.md` §11 item 2. Origin: intake G-08 | The statement "a 35 % share is not reachable with 20 of 1,150 customers" is presented as arithmetic. It is not. The share depends on the order volume of the 20 pilot customers, which no source gives. The statement drives risk R-11 (High/Medium) and experiment B4. It appears in six places | Overclaimed inference presented as fact. ES-03 requires an assumption to be labelled | Reword each occurrence as a labelled assumption, for example "ASSUMPTION: the 20 pilot customers place far fewer orders than the 35 % target needs; their order volume is not in knowledge-docs (see OPEN-05)". Add the pilot's order share to OPEN-05. Keep the risk rating as a judgement under A-25 |
| L-1 | Low (gate Q-17 not literally met) | Status rows in all seven release files (line 11 of each, and the "Status now" line at the end). `product-requirements.md` §8 status rows (lines 289, 331, 378 and later). `README.md` §2 and §3 tables | Release files say "Proposed — awaiting product owner approval; not yet tagged". Plan Q-17 and D6 require each file to be marked "Draft" and to say it awaits approval. The BRD, PRD, backlog and traceability headers say "Draft - for review" correctly | Q-17 says "every file is marked draft". The status is consistent across files, so the defect is wording only | Change the status text in the seven release files, the PRD §8 rows and the README tables to "Draft - awaiting product-owner approval - not tagged" (plan wording) |
| L-2 | Low | `releases/dotnet-r4.md` line 15 and Appendix A (from about line 222) | The release file lists 9 unplanned items (track tag only) in an appendix. Membership is correct: the 11 planned items match the register exactly. The appendix says "listed once here", but the same items also appear in the backlog and traceability | Q-06 requires release-file membership to equal the register. A reader could take the appendix for release content | Move Appendix A to README §3 or to the backlog, or keep it and remove "listed once here". No count changes |
| L-3 | Low (plan deviation, not recorded) | `experiments.md` §1 table (line 32), §3.6, §3.7 M1, §3.8, step 6 (line 217) | Plan P03 specifies comparing pilot calls with "their own earlier 2 weeks". The experiment uses 4 baseline weeks throughout and gives an 8-week elapsed time. The change is reasonable, but nothing records it as a difference | Q-13 is met. The plan and the experiment disagree without a note | Add a short "difference from plan" row to the experiment (section 3.6), or align to 2 weeks and recompute A-31 |
| L-4 | Low | `backlog.md` §7, `US-DN-036` block (line 2211 area) | `US-DN-036` cites BR-04 but does not state the "as of the 02:00 batch" freshness that A-04 and plan §8 require for BR-04 stories. `US-DN-011` and `US-DN-012` do state it | The unplanned story could be built with live-status wording that the source system cannot support | Add the 02:00 freshness sentence to the criteria of `US-DN-036` |
| L-5 | Low | `README.md` §1.2, line 30 | "The tag `track-power-platform` is not used in any document." The string appears in BRD §3.2, traceability §6, backlog §1.3 and this README. The intent is that no item carries it as a tag | Self-contradictory wording in the master file | Change to "is not used as a tag on any item" |
| L-6 | Low | `backlog.md` lines 424 and 550 (cost-model criteria); `releases/azure-r1.md` line 226 (§12 "Decision and cost"); `experiments.md` line 125 (M4) and line 313 (A3) | The EUR 1,350 "at risk" threshold (10 % under the ceiling) is cited to A-06. A-06 is defined as "experiment success thresholds and pivots". A cost threshold is not an experiment threshold | Labelling is weak. The number drives a go or stop decision (OPEN-04 escalation) | Add a separate ASSUMPTION row for the 10 % cost margin (owner Marc Dubois, with Ahmed Benali), or extend A-06's wording in the register and in each file |
| L-7 | Low | `traceability.md` §3.2, NFR-06 row with Area BA-02 (line 86); NFR-04 row with Area BA-01 | Business case §4 lists NFR-06 under BA-01 only. The BA-02 row therefore shows a .NET requirement with "no .NET story" when none is expected. NFR-04 under BA-01 is defensible, because §4 says NFR-03, NFR-04 and NFR-05 apply "wherever relevant", but the BRD §4 BA-01 list does not include it | Attribution check (business case §4) fails for NFR-06 and is ambiguous for NFR-04 | Delete the NFR-06 BA-02 row and keep a note that NFR-06 is BA-01 only. Add "cross-cutting per business case §4" to the NFR-04 BA-01 row, and mention it in BRD §4 |

## 2. Plan criteria Q-01..Q-17

| Criterion | Result | Evidence |
|---|---|---|
| Q-01 Files at pinned paths; nothing written elsewhere | Pass | 13 files present at the pinned paths. `docs/` contains only `docs/product/` and `releases/`. Git: only untracked `docs/` and `.copilot-tracking/` |
| Q-02 BA-03 only in out-of-scope lists (and OPEN-24) | **Fail (partial)** | M-2. No BR-14..BR-19, NFR-09, C-07, C-08, SM-05, SM-06 appears as a source. CS-26, CS-27, CS-28 and ES-36 do appear as sources (outside the out-of-scope lists) |
| Q-03 Every BR-01..13 and NFR-01..08 mapped; uncovered listed | Pass | Derived from the register. Every in-scope BR and NFR has at least one planned story or enabler (for example BR-13: 10 citing items; NFR-06: 7). Traceability §3 story references agree with the register on release (77 references checked; the two apparent mismatches are a parser artefact of the §3.3 layout, and the corrected pairing agrees). "Not covered: none" is correct |
| Q-04 NFR-03, NFR-04 (when in scope), NFR-05 per track; no two-track story | Pass | NFR-03: `EN-AZ-01`, `US-AZ-008` (Azure) and `US-DN-005`, `EN-DN-11` (.NET). NFR-05: `EN-AZ-04`, `US-AZ-006` and `EN-DN-05` (both tracks). NFR-04: .NET stories; Azure side is OPEN-13 per A-02. No item carries two track tags |
| Q-05 Tags (ES-30, ES-31) | Pass | 133 items: 133 have exactly one track tag; 124 planned have one release tag of their own track; 9 unplanned have none; no item lists two releases; parent and child share track and release (0 violations). Item tags, priority, parent and source lines agree with the register for all 133 |
| Q-06 Release membership equals backlog register across backlog, traceability, release file and PRD | Pass (note L-2) | Release tables match the register for all seven releases (17, 22, 8, 15, 41, 10, 11 planned). Header counts match (for example azure-r2 "22: 1 epic, 5 features, 7 enablers, 9 stories"). PRD §8 lists every planned epic, feature and enabler in its release section. PRD names no US- story, as stated in traceability §8.1 |
| Q-07 Release counts 3 Azure and 4 .NET; Git tags planned only | Pass | 3 and 4 release files. Tag names appear only as planned text. `git tag --list "product/*"` is empty. No commit made |
| Q-08 No release waits on another track | Pass | 207 "Depends on / Enables" references checked: 0 cross-track, 0 later-release. Cross-track items are OPEN-items with "without the answer" positions in every release file and README §8. The phrase search found only negations and the forbidden-phrase rule itself |
| Q-09 Stories have As a / I want / so that and at least one testable Given/When/Then | Pass (see M-1) | All 56 stories and all 29 enablers have "As a ... I want ... so that". All 56 stories have full Given/When/Then criteria. Every enabler has at least one full block. The remaining enabler criteria lack "When" (M-1) |
| Q-10 Sources cite identifiers that exist in knowledge-docs | Pass | 114 distinct BR, NFR, C, CS, ES, SM, P and OQ identifiers cited across the set. All exist in knowledge-docs (P-01..P-06 are bullets in business case §2). Research labels C1..C17, W1 and G-/X- are labelled ASSUMPTION (A-22, A-23) |
| Q-11 ASSUMPTION and OPEN in tables with owners; IDs identical | Pass | README defines A-01..A-43 and OPEN-01..OPEN-33. Every A- and OPEN- ID cited in any file is defined in the README; every defined ID is used somewhere. Owners and track columns agree in the spot-checked rows. Wording spot-checked for A-02, A-22, A-23 and OPEN-03: identical in each file read |
| Q-12 Enablers before features (ranked) | Pass | Backlog §4: 81 ranked enablers and stories (33 Azure, 48 .NET). Release order is non-decreasing. Every "Depends on" item ranks earlier in its own track (0 violations) |
| Q-13 Exactly two MVEs, each with riskiest assumption, test, thresholds and backlog links; nothing run | Pass (note L-3) | `MVE-BA01` (StockPilot exchange, `track-azure`) and `MVE-BA02` (status "as of 02:00", `track-dotnet`). Each has hypothesis, test, owner, effort, M-metrics with persevere/pivot/stop, and an "Informs" list. The not-chosen list (A2, A3, A4, B2, B3, B4) is not a third MVE. §7 records "Not run" |
| Q-14 Plain language, acronyms explained, file locations, IaC wording | Pass (spot-check) | Acronyms are explained in the "words used" sections of the files read. IaC is described as checked with `az bicep build`; nothing deployed (ES-27). Plain-language quality was spot-checked, not read line by line |
| Q-15 No secrets or real tenant, subscription or connection values | Pass | Regex scan over `docs/product/`: no GUID, no `Password=` / `AccountKey` / `SharedAccessSignature`, no private key marker, no IP address, no e-mail address. Server names (`NWSQL01`, `NWFS01`) and file-share paths are business facts from knowledge-docs, not credentials |
| Q-16 Documents say "for review"; no change to `src/`, `database/`, `infra/` | Pass | All headers read "Draft - for review" or "Proposed". Git: no tracked file changed |
| Q-17 Every file marked draft; each release awaits product-owner approval | **Fail (literal)** | Release files say "Proposed", not "Draft" (L-1). Approval wording is present in every release file (§13, approval block) |

## 3. Facts spot-checked against source

Verified (the document statement matches the source):

| Statement in product documents | Source checked | Result |
|---|---|---|
| Nightly job at 02:00 on `NWSQL01` runs the export and import | `database/003-stockpilot-exchange.sql` header (SQL Agent job "NW - StockPilot nightly") | Match |
| Export uses `xp_cmdshell` and `bcp`; import uses `BULK INSERT` from `D:\` | `003` procedures | Match |
| Export sets orders to Picking (status 2); import sets Shipped (status 3) | `003` UPDATE statements | Match |
| `ShippedAt` and `Carrier` are read but not stored (C3) | `003`: `#Shipments` temp table only; no `Orders` column for either | Match. `Orders` has no such columns in `001-schema.sql` |
| Repeated "Shipped" audit rows (C4) | `003`: audit INSERT joins all shipments without filtering status | Match |
| Orders.Channel 3 = Portal; `InvoiceNumber` nullable | `001-schema.sql` lines 40–43 | Match |
| Connection uses Integrated Security to `NWSQL01` (CS-13) | `src/.../Web.config` | Match |
| Session is `InProc`, timeout 60 minutes (CS-16); used by `EN-DN-06` "idle for 60 minutes" | `Web.config` `sessionState` | Match |
| Invoice share `\\NWFS01\invoices`; order history 24 months (CS-14, BR-02) | `Web.config` appSettings | Match |
| Controllers take `customerId` from the request; no user-to-company check (C5) | `OrdersController.cs` `Index(int customerId)`, `Copy(int id, int customerId)` | Match. `OrderService.CopyOrder` checks only the passed customerId, which is itself from the request |
| Draft screen offers no Portal channel (C16) | `Views/Orders/Draft.cshtml`: options Phone, E-mail, Order form | Match |
| No mail-sending code in `src/` (C14, CS-12) | Search for `SmtpClient`, `System.Net.Mail`, `MailMessage` | None found. Match |
| Invoice folder year follows the order date (C7) | `InvoiceStore.GetInvoicePath` uses `invoiceDate.Year`; `OpenInvoice` is called with `order.OrderDate` | Match |
| Business-case numbers: 1,900 orders/week; 4.1 %; 410 calls/week; 35 %; 62 %; 70 %; 120 requests/week; 1,150 customers; 38 staff; 48 GB; 120 GB; 1 GB and 2 GB growth; 99.5 %; RPO 1 h; RTO 4 h; 30 June 2027; EUR 1,500; 06:00–12:00 CET; 2 servers; SM-07 | `business-case.md`, `current-state.md` | Match in every spot-checked occurrence |

Not verified in this review, and labelled correctly:

* External claim (research W1, A-23) that Azure SQL Managed Instance does not offer `xp_cmdshell` and reads `BULK INSERT` only from Blob storage. The product documents label it as a search summary that must be confirmed before a hosting decision. No web check was run.
* "All text is in English" (C15, A-22). No resource files exist in `src/`, and the views are English. Not exhaustively checked; labelled.

## 4. Requirement coverage and attribution (ES-06, business case §4)

| Requirement | BA (business case §4) | Stories and enablers (planned, with release) | Result |
|---|---|---|---|
| BR-01 | BA-02 | `EN-DN-10`, `US-DN-003`, `US-DN-004` (dotnet-r2) | Covered |
| BR-02 to BR-06 | BA-02 | `US-DN-006`; `US-DN-008`, `US-DN-020`; `US-DN-011`, `US-DN-012`; `US-DN-013`, `US-DN-014`; `US-DN-016` (dotnet-r2) | Covered |
| BR-07, BR-08 | BA-02 | `US-DN-022`, `US-DN-023`; `US-DN-024`, `US-DN-025` (dotnet-r3, Should) | Covered |
| BR-09 | BA-02 | `EN-DN-15`, `US-DN-028`, `US-DN-029` (dotnet-r4, Could) | Covered; "partly" until OPEN-18, stated |
| BR-10 | BA-02 | `US-DN-001`, `US-DN-002` (dotnet-r1); `US-DN-017`, `US-DN-018`, `EN-DN-13` (dotnet-r2); `US-DN-030` (dotnet-r4, Could) | Covered. Priority note on `US-DN-030` disclosed |
| BR-11 | BA-02 | `EN-DN-12` (r2, Should); `US-DN-026`, `US-DN-027` (r3); `US-DN-034` unplanned | Covered; Dutch unplanned, disclosed |
| BR-12 | BA-02 | `US-DN-009`, `US-DN-015` (dotnet-r2) | Covered; OPEN-16 stated |
| BR-13 | BA-01 | `US-AZ-010`, `US-AZ-011`, `US-AZ-013`, `US-AZ-014`, `EN-AZ-08`, `EN-AZ-13` (azure-r2) | Covered |
| NFR-01 | BA-01 | `EN-AZ-05` (r1), `US-AZ-007` (r2) | Covered |
| NFR-02 | BA-02 | `US-DN-007`, `US-DN-010` (dotnet-r2) | Covered |
| NFR-03 | BA-01 (also applied to BA-02, per A-02) | `EN-AZ-01` (r1), `US-AZ-008`, `EN-AZ-06`, `EN-AZ-08`, `EN-AZ-11` (r2); `US-DN-005`, `EN-DN-11` (r2), `US-DN-029` (r4) | Covered |
| NFR-04 | BA-02 (cross-cutting, A-02) | `US-DN-004`, `EN-DN-08` (r2); `US-DN-024` (r3). Azure side: OPEN-13 | Covered on .NET; see L-7 |
| NFR-05 | Both (cross-cutting) | `EN-AZ-04`, `US-AZ-003`, `EN-AZ-07`, `US-AZ-006`, `EN-AZ-11` (Azure); `EN-DN-05`, `EN-DN-09` (.NET) | Covered per track |
| NFR-06 | BA-01 | `EN-AZ-06`, `US-AZ-009` (r2); `US-AZ-018` (r3) | Covered. The BA-02 row is an attribution error (L-7) |
| NFR-07 | BA-02 | `EN-DN-14`, `US-DN-020`, `US-DN-021` (dotnet-r2) | Covered |
| NFR-08 | BA-02 | `EN-DN-13`, `US-DN-018`, `US-DN-019` (dotnet-r2); `US-DN-035` unplanned | Covered; field-level detail unplanned (OPEN-17) |
| BA-03 items (BR-14..19, NFR-09, C-07, C-08, SM-05, SM-06) | Out of scope | No item cites them as a source, apart from CS/ES items in M-2 | Not planned (correct) |

Coverage results were derived from the register's Sources column and match the traceability tables for every requirement above. Traceability §4 "Not covered: none" is correct.

## 5. Plan deviations (charter response format)

* Planned, not done: none. All 13 files exist. All release names, Git tag names (planned only) and counts match.
* Done differently: release status wording (L-1); MVE-BA02 baseline 4 weeks, not 2 (L-3).
* Done, not planned, but disclosed: `EN-AZ-14`, `EN-DN-15` (plan J-1, J-2); assumptions A-27..A-43; OPEN-27..OPEN-33 (new numbers, added to the master registers, as §5.3 allows); `FT-DN-26` status options and `EP-DN-08` (A-35, A-36); "US-AZ-020" as the next free number (conditional on OPEN-03 or OPEN-13).
* Done, not planned, not disclosed: the citations listed in M-2.

## 6. Conditions honored

Not applicable. No council conditions were supplied with this dispatch.

## 7. Review record

This file: `C:\demos\northwind-workshop\.copilot-tracking\reviews\product-documents-review.md`.

Scratch artefacts (not product documents): `.copilot-tracking\reviews\probe-nw-product-docs\check-backlog.ps1`, `check-crossdoc.ps1`, `backlog-register.csv`, `backlog-items.csv`.

## 8. What to fix before re-review

Order of work for the owner (Functional Planner for backlog and traceability; Analyst for BRD and PRD; Experiment Designer for experiments; the release files):

1. H-1: add `Depends on: EN-DN-10` to each listed story that reads or shows customer data (see H-1; `US-DN-019` included if audit history is viewable), or reword line 1315. Re-run the dependency check.
2. M-2: remove the BA-03 source IDs from FT-DN-25 and EP-DN-08; replace CS-26 and CS-28 in experiments; correct traceability check 8.
3. M-3: reword the 35 % statement in six places as a labelled assumption.
4. M-1: add "When" to the 84 enabler criteria.
5. L-1: change the release status wording (plan wording).
6. L-2 to L-7: as listed.

After these fixes, the expected result is Pass-With-Findings (Low items only), or Pass if the owner accepts L-items as noted.
