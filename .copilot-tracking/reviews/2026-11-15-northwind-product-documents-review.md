<!-- markdownlint-disable-file -->
# Review: Northwind product documents (BRD, PRD, MVEs, backlog, traceability, per-track releases)

Verdict: Pass-With-Findings

## Executive Summary

* Assessment: Pass-With-Findings (proposed; the squad's "Approve-With-Fixes"). The document set is complete, internally consistent on its release plan, coverage ids, tags and track rules, and nothing was deployed, committed or tagged. Three High and two Medium findings must be fixed before the product owner approves any release. The assessed scope is the six product documents, the six release files and the plan contract C1 to C11 with checks RC-01 to RC-16. Scope is the full task NW-PRODUCT-DOCS-2026-11-15.
* Why this matters: the Azure and .NET teams will build from the release files. Two of the High findings change what a team would believe is in a release: the azure-r3 window ends before its own June cutover, and BR-13 (move Order Desk to Azure) is marked covered while the application hosting runtime and the database migration have no build item in any release.
* Review execution: Partial. The mechanical checks covered the whole set. A full line-by-line manual read of the prose was not done (see Risks, Blockers, and Residual Work).
* Assessed outcome: Defects found (proposed; not final until Parent Decision Record records decisions).
* Validation coverage: 9 analysis scripts run read-only over all deliverables and sources; git state checked. No build or test applies (documents only; ES-27). Scribe history entry not checked (squad state is read-only to this review).
* Confidence and limitations: high confidence in the mechanical results (id, tag, release, verbatim and arithmetic checks). Medium confidence in the prose-level judgments, which rest on targeted reads and sampling. No Critical finding was identified.

The assessment above is the reviewer's proposal. Parent Decision Record contains the final decisions and next actions, or states that decisions are pending.

## What You May Not Know

* The azure-r3 window (1 Apr to 31 May 2027) ends before the June Sundays that the same release plans for rehearsal and live cutover (6, 13, 20, 27 June 2027). The release says "Anything after 31 May 2027: Not planned". O-27 is open, but the canonical window and the exclusion are unchanged.
* BR-13 and BG-02 are "Covered" in the traceability table. The covering stories are cutover and rollback planning. The application runtime and the database migration are not built by any planned or unplanned item (azure-r1 IN-1). Design and planning are what ES-27 allows; the coverage wording still overstates what the releases deliver.
* The plan's canonical path for this review (`.copilot-tracking/reviews/logs/2026-11-15/northwind-product-documents-review.md`, plan C8 D7) differs from the path the caller requested. This record is written at the caller's path.
* The implementation changes record named in the plan (`.copilot-tracking/changes/2026-11-15/northwind-product-documents-changes.md`) does not exist. The directory `.copilot-tracking/changes/` is absent. This review therefore compared the plan to the deliverables directly.
* Critique was skipped by plan charter. No Squad Challenger or plan critique ran.

## Findings and Proposed Routes

Ordered by severity and impact. Severity uses the skill labels: High, Medium, Low. Mapping for the squad's scale: High and Medium are Major (blocking for approval until fixed); Low is Minor. No Critical finding was identified.

<!-- rpi:review id=RV-001 -->
### RV-001 [High]: azure-r3 target window excludes its own cutover and rehearsal dates

The canonical window for `azure-r3` ends 31 May 2027. The release plans its rehearsal and live cutover on Sundays in June, which fall after that window. The release also excludes everything after 31 May. A team reading the window would think the cutover is out of scope.

* Related scope: `azure-r3`; BR-13; NFR-01 and NFR-06 proof; SM-07; C-01; plan C1 and C2.
* Expected behavior: C1 window and each release's window, exit dates and "leaves out" text agree. The release's own content falls inside its window (plan C1; PRD section 6.2 and BRD section 10.2 must match C1).
* Observed behavior and evidence: `docs/product/releases/azure-r3.md` line 13 `target_window: "1 Apr to 31 May 2027"`; line 52 target window row; line 111 "Anything after 31 May 2027 | Not planned"; line 148 XC-3 plans rehearsal on 6 and 13 June and live cutover on 20 and 27 June; line 56 and line 189 record O-27 as open. The same window appears in `docs/product/product-requirements.md` section 6.2 (the canonical release table), `docs/product/business-requirements.md` section 10.2 and `docs/product/backlog.md` section 1.1. Checked with a calendar: 6, 13, 20 and 27 June 2027 are all Sundays; 30 June 2027 is a Wednesday.
* Impact: the window is the date a product owner approves against. Approving "by 31 May" would approve a release that cannot show its cutover. The fix is canonical (C1), so it must change in six documents at once.
* Resolution condition: one window value appears in C1 and in all four documents and the release frontmatter, and it covers the planned rehearsal and live Sundays (or the rehearsal Sundays move into May 2027, which is also consistent: 2, 9, 16, 23 and 30 May are Sundays). The "Anything after ..." row either disappears or names only true unplanned items. O-27 stays open only for the approval question.
* Proposed destination: rpi-plan (canonical contract C1 is a plan decision; change C1 first, then every document).
* Smallest useful next action: the coordinator changes C1 for `azure-r3` (for example, end 27 June 2027) and the six documents follow; Lena Varga and Marc Dubois confirm under O-25 and O-27.

<!-- rpi:review id=RV-002 -->
### RV-002 [High]: BR-13 and BG-02 are marked covered while the Azure runtime and database migration have no build item

Traceability row BR-13 says "Covered, OPEN remains" with covering stories STORY-170 and STORY-171. Those stories plan cutover and rollback. The application that must run in Azure (how Order Desk runs there) is "Unplanned. No backlog item exists for it in any Azure release" (azure-r1 section 5). The data migration is only decided and defined (STORY-120 and STORY-122). No item builds either. The release file records this itself as inconsistency note IN-1 and open item AZ1-O1.

* Related scope: BR-13; BG-02; SM-07; C-01; C-06; O-03; A-20 and A-21 (fallback and data tier); plan C1 "BR / NFR covered" column for `azure-r3`.
* Expected behavior: a covered requirement has a planned or unplanned story that delivers the behaviour it needs. Where delivery is out of scope under ES-27 (no deployment), the coverage row says so and names the open owner (ES-06 "Covered" must be true).
* Observed behavior and evidence: `docs/product/traceability.md` line 67 (BR-13 row); `docs/product/releases/azure-r1.md` line 115 (hosting runtime "Unplanned"), line 217 (AZ1-O1), line 224 (IN-1); `docs/product/backlog.md` items STORY-120 and STORY-122 define and decide, and there is no build item for runtime or migration; the `docs/product/backlog.md` section 2 register has no runtime or migration item.
* Impact: a reader of the traceability table would conclude that BR-13 and BG-02 are delivered by planned work. The releases deliver designs and runbooks. A product owner could approve a "covered" BR-13 that has no runtime or migration behind it.
* Resolution condition: either (a) the register gains a planned or unplanned item for the Azure runtime and the database migration build, with O-03 and A-21 cited as OPEN, or (b) the BR-13 and BG-02 coverage wording in traceability, backlog section 1.1, PRD section 4.2 and BRD section 7.1 says "design and runbook only; runtime and migration build unplanned (O-03, A-21)", so the row no longer reads as delivered. Either way, the status column changes from "Covered" to match.
* Proposed destination: rpi-plan (a scope decision: add the items or narrow the claim).
* Smallest useful next action: product owner (Lena Varga) with Ahmed Benali decide between (a) and (b) under O-03; the reviewer recommends (b) now, which needs no new scope.

<!-- rpi:review id=RV-003 -->
### RV-003 [High]: BRD front matter sets an 80 percent coverage threshold and its own section reports 0.0 percent as "not a defect"

The BRD header carries `fr_to_ac_coverage_threshold_pct: 80.0`. Decision DD-03 says the FR-to-acceptance-criteria coverage "is therefore reported as 0.0 % here and is not a defect". A reader or tool that reads the header sees a failing threshold that the text excuses. The PRD header carries a similar key (`fr_to_goal_coverage_threshold_pct: 100.0`), which the evidence meets (see below). The BRD header also carries template keys that do not fit this document (`business_goal_smart_status: "deferred"`, `diagram_format: "none"`, `requirement_id_prefixes` with `fr`, `ac`, `con`).

* Related scope: BRD headers and DD-03; PRD header; ES-06, PNFR-02, RC-02.
* Expected behavior: a metric in a document header is either measured and met, or marked not applicable with a reason. A document does not report a zero against its own threshold.
* Observed behavior and evidence: `docs/product/business-requirements.md` line 12 (threshold 80.0), line 67 (DD-03, 0.0 percent). Checked by script: all 57 PRD functional requirements (FR-101 to FR-330) map to at least one backlog item, and all 57 carry a business goal (BG-01 to BG-05). So the FR coverage is in fact 100 percent in the PRD and backlog; only the BRD statement is wrong.
* Impact: a reviewer or governance tool would read the BRD as failing its own threshold. The mislabelled template keys also suggest the metadata was not checked.
* Resolution condition: the BRD header either removes `fr_to_ac_coverage_threshold_pct` (and the other template keys that do not apply) or marks it "not applicable: no FR or AC items in this BRD". DD-03 says where FR coverage is measured (PRD section 16 and backlog) and gives the measured figure (57 of 57 FR mapped).
* Proposed destination: rpi-implement (document correction that fits the accepted plan).
* Smallest useful next action: edit the BRD header and DD-03 as stated; the product owner confirms that the template keys are not required.

<!-- rpi:review id=RV-004 -->
### RV-004 [Medium]: release files cite assumption and open ids that their own registers do not define

Plan PNFR-03 requires that every A-nn and O-nn in a document appears in that document's register with an owner, and ES-03 and ES-04 require the same. Checked by script, the release files cite these ids without a register row in that file:

* `azure-r1`: A-06, A-40, O-10
* `azure-r2`: A-06, A-40, A-46, O-06
* `azure-r3`: A-40, A-46, O-06
* `dotnet-r1`: A-38, O-07
* `dotnet-r2`: A-02, A-06, A-38, A-39, A-42, A-43, A-45, A-46, O-01, O-06, O-07, O-12, O-17
* `dotnet-r3`: A-02, A-25, A-38, A-39, A-42, A-45, A-46, O-02, O-07

The experiments document also cites A-14 at `docs/product/experiments.md` line 296 without a register row; O-10, O-11, O-13 and O-14 appear only in prose at line 385. The worst case is `dotnet-r2`, which cites the open API owner (O-01) and the pilot database (O-23 is defined; O-01 is not in that file).

* Related scope: each release file section 8 or 9 or 10 (its register); `docs/product/experiments.md` section 5.
* Expected behavior: every A or O id cited in a file has a row in that file's register with an owner, or the file states that a named register (backlog section 7) is the register of record for that id.
* Observed behavior and evidence: the cited ids above, from a script comparing cited ids with register rows in each file (outputs in `.copilot-tracking/reviews/probe-2026-11-15/`).
* Impact: an owner cannot tell from the release file who must confirm a cited assumption, which is the point of ES-03 and ES-04.
* Resolution condition: each listed id has a register row with its text and a named owner (copied from `docs/product/backlog.md` section 7), or each file names backlog section 7 as its register of record. A re-run of the same script returns no cited-but-undefined A or O id per file.
* Proposed destination: rpi-implement.
* Smallest useful next action: add the rows (or the register-of-record sentence) to each listed file and to experiments section 5.1.

<!-- rpi:review id=RV-005 -->
### RV-005 [Medium]: the registers are not consolidated and release-local ids are not registered

Plan P01-T01 requires the BRD to carry the consolidated ASSUMPTION and OPEN registers. The BRD register stops at A-48 and O-26; it omits A-49 to A-57 and O-27 to O-30. The PRD register omits A-55 to A-57 and O-28 to O-30. The complete set exists only in `docs/product/backlog.md` section 7, which `docs/product/traceability.md` section 9 names. Release-local ids (A-D1-01, A-D1-02, A-D2-01, A-D2-02, A-D3-01, A-D3-02, O-D2-01, O-D2-02, O-D3-01, O-D3-02, AZ1-O1, AZ1-O2, AZ2-O1, AZ3-O1) are labelled "to be registered by the coordinator" and appear in no consolidated register.

* Related scope: BRD sections 12 and 13; PRD sections 14 and 15; backlog section 7; C9 of the plan.
* Expected behavior: each document's register is the consolidated register for the ids it defines or cites, or it names the register of record. Release-local ids are registered in the consolidated register.
* Observed behavior and evidence: script comparison of register rows by document (outputs in the probe directory); `docs/product/business-requirements.md` section 12 and 13 headings; labels "to be registered by the coordinator" in `docs/product/releases/dotnet-r1.md` through `dotnet-r3.md` and `azure-r1.md` through `azure-r3.md`.
* Impact: a reader of the BRD cannot find the newest assumptions and open items, and the release-local ids can drop out of the squad's registers.
* Resolution condition: the BRD (sections 12 and 13) and the PRD (sections 14 and 15) either hold rows for A-49 to A-57 and O-27 to O-30, or each states that backlog section 7 is the register of record for ids added after the document was written. The release-local ids are added to backlog section 7 with owners.
* Proposed destination: rpi-implement (copy rows; the register-of-record choice is a coordinator decision).
* Smallest useful next action: coordinator confirms backlog section 7 as the register of record; the implementer adds the missing rows and the release-local ids.

<!-- rpi:review id=RV-006 -->
### RV-006 [Low]: PRD says dotnet-r2 "can start after" azure-r2, but the windows overlap

`docs/product/product-requirements.md` line 245 (section 6.2 table) says `azure-r2` "lands the pilot environment before the Q2 2027 pilot (so `dotnet-r2` can start after it, A-37)". The `dotnet-r2` window is 1 Mar to 30 Apr 2027. The `azure-r2` window is 1 Feb to 31 Mar 2027. The windows overlap by 31 days. A-37 is about which database the pilot reads, not when the release starts. The release file already records this as O-D2-01.

* Related scope: `dotnet-r2`; A-37; C2 wording.
* Expected behavior: a start-order statement matches the windows, or it states the approval order instead.
* Observed behavior and evidence: `docs/product/product-requirements.md` line 245; `docs/product/releases/dotnet-r2.md` line 252 (O-D2-01).
* Impact: a team may wait for the Azure window to close before starting, which the release is not allowed to require (ES-31).
* Resolution condition: the sentence states the dependency as the database read after `azure-r2` is approved (A-37), with the overlap explained, and does not say "start after".
* Proposed destination: rpi-implement.
* Smallest useful next action: reword the sentence in section 6.2 and in C2.

<!-- rpi:review id=RV-007 -->
### RV-007 [Low]: research and plan ids appear in product documents with no definition there

`RG-02`, `RG-03` and `RG-04` are cited in parentheses next to O-16, O-17 and O-19, but no product document defines the RG register. The plan ids `PNFR-05`, `RC-03` and `RC-05` are cited in the product documents as checks, but only the plan defines them.

* Related scope: `docs/product/business-requirements.md` lines 502, 503, 505 and 544; `docs/product/product-requirements.md` lines 75, 757, 758, 760 and 809; `docs/product/experiments.md` line 375; `docs/product/backlog.md` lines 1873, 1874 and 1876; `docs/product/traceability.md` line 214; `docs/product/releases/azure-r1.md` line 212; `docs/product/releases/dotnet-r1.md` line 169; `docs/product/releases/dotnet-r2.md` line 213; `docs/product/releases/dotnet-r3.md` line 157.
* Expected behavior: a product document cites only ids it defines or ids of a source it names.
* Observed behavior and evidence: script search of every product file for the RG, PNFR and RC families.
* Impact: a reader cannot resolve the citation, and the plan's internal check names leak into the product set.
* Resolution condition: the RG parentheses are removed (O-16, O-17 and O-19 already carry the question), and the PNFR and RC citations are replaced by the plain statement they support.
* Proposed destination: rpi-implement.
* Smallest useful next action: delete or rephrase the listed citations; re-run the id search.

<!-- rpi:review id=RV-008 -->
### RV-008 [Low]: BRD C-02 wording adds an expansion, so the quote is no longer verbatim

Plan and ES-02 require source ids and quotes verbatim. The business case C-02 says "we pay for Extended Security Updates". The BRD says "Extended Security Updates (ESU)".

* Related scope: BRD section 9, C-02.
* Expected behavior: quoted source text is unchanged; acronym expansions go in the glossary or in brackets outside the quote.
* Observed behavior and evidence: `docs/product/business-requirements.md` line 321 against `knowledge-docs/business-case.md` section 3.3 (C-02). All other BR, NFR, C and SM rows and the P rows match verbatim (script comparison).
* Impact: minor; the meaning is unchanged, but a verbatim check would fail.
* Resolution condition: the quoted text matches the source exactly; "ESU" is explained in the glossary.
* Proposed destination: rpi-implement.
* Smallest useful next action: remove "(ESU)" from C-02 and add ESU to the glossary.

<!-- rpi:review id=RV-009 -->
### RV-009 [Low]: some derived or estimated figures are not labelled as such

* Effort figures ("about 4 person-days"; step lengths of 0.5 day, 1.5 day and 1 day) appear in `docs/product/experiments.md` lines 108, 113 to 118, 195 and 279 and in `docs/product/releases/azure-r1.md` lines 153 and 202. They are labelled ASSUMPTION MVE-A-01, which satisfies ES-03. But `docs/product/product-requirements.md` line 208 (non-goals) says "Effort sizing and real prices. No basis for them exists in the sources", which the same set contradicts. The plan lists effort sizing as a non-goal.
* The EUR 300 headroom (1,500 less 1,200) is derived but unlabelled: `docs/product/experiments.md` line 97, `docs/product/releases/azure-r1.md` line 93 and `docs/product/backlog.md` line 468.
* The MVE-02 sample of "5 to 8 customers" appears at `docs/product/experiments.md` lines 46 and 155 without an ASSUMPTION label. It is a design choice, not a source fact (ES-03).
* The 56 GB and 136 GB projections assume 8 months of growth to 30 June 2027; from mid-November 2026 that is 7 to 7.5 months. The assumption MVE-A-03 is labelled, but the month count is not stated as an assumption of its own.
* Arithmetic checked and correct: 900 / 52 = 17.31 per user; 1,200 = 80 percent of 1,500; 410 - 250 = 160 fewer calls (39 percent); 1,900 / 1,150 = 1.65 orders per customer per week; 84 hours a week; 0.5 percent of 84 hours is about 25 minutes.

* Related scope: MVE effort and thresholds; C-04 headroom; C-08 per-user cost.
* Expected behavior: estimates are labelled as assumptions or derived values with their basis; the non-goals match what the set does.
* Observed behavior and evidence: the lines above.
* Impact: a reader could take an estimate as a sized plan, which the sources do not support.
* Resolution condition: the PRD non-goal is reworded to say that effort figures are assumptions (MVE-A-01), or the figures are removed; the EUR 300 headroom and the sample size carry "derived" or "ASSUMPTION" labels; the growth-month basis is stated.
* Proposed destination: rpi-implement.
* Smallest useful next action: edit the four labels and the non-goal sentence.

<!-- rpi:review id=RV-010 -->
### RV-010 [Low]: experiments document has long sentences and acronyms not explained at first use

ES-01 asks for short sentences and plain words, with acronyms explained at first use. Sampled by script: `docs/product/experiments.md` averages 19.2 words per prose sentence, with 19 sentences over 30 words (the other documents average 12 to 17). `WCAG` (line 171), `VM` (line 86) and `CSV` (line 47) are not expanded at first use in that file. `AC` in `docs/product/product-requirements.md` is not expanded at its first prose use.

* Related scope: ES-01 (PNFR-01).
* Expected behavior: a business reader can follow each acronym and sentence.
* Observed behavior and evidence: script sample; the manual 10-paragraph sample required by PNFR-01 was not done (see Missing or limited evidence).
* Impact: readability for the business reader; no effect on requirements.
* Resolution condition: the listed acronyms are expanded at first use; the longest experiment sentences are split.
* Proposed destination: rpi-implement.
* Smallest useful next action: expand the four acronyms and split the longest sentences in experiments section 3.

<!-- rpi:review id=RV-011 -->
### RV-011 [Low]: template licence and metadata lines appear in the product document headers

The BRD and PRD headers carry `license: "CC-BY 4.0 (Microsoft HVE-Core)"`, which is a template attribution. The BRD header also has `business_goal_smart_status: "deferred"` and `diagram_format: "none"`. These are not decisions the plan made.

* Related scope: BRD header line 24 and PRD header line 26; BRD header lines 11 and 13.
* Expected behavior: header values are either decided and stated, or removed.
* Observed behavior and evidence: the header lines named above.
* Impact: a licence statement on squad-authored documents is a claim that the owner has not confirmed. Metadata values with no basis add noise.
* Resolution condition: the owner confirms the licence line or removes it; unused template keys are removed (together with RV-003).
* Proposed destination: follow-up (owner: Lena Varga).
* Smallest useful next action: product owner confirms or removes the licence line.

## Parent Decision Record

<!-- Decisions live here. Append events; never rewrite the evidence body above to fit a decision. -->

### Current Disposition

* Based on events: RD-001, RD-002, RD-003, RD-004
* Review execution: Partial
* Final outcome: pending parent decision. Assessed proposal: Defects found (three High and two Medium findings that must be fixed before any release is approved; no finding is Critical; no evidence is missing for a credible verdict).
* Finding decisions and next actions: RV-001 to RV-011 pending. Proposed routes: RV-001, RV-002 to rpi-plan; RV-003 to RV-006, RV-007 to RV-010 to rpi-implement; RV-011 to follow-up. Owners are named in each finding.
* Decisions still needed: RV-001 (window), RV-002 (scope or narrowed claim), RV-005 (register of record), RV-003 and RV-011 (header metadata). Remaining findings are document corrections.

This summary is derived from Decision History, not a second decision record. The latest event for each subject governs; refresh this summary after appending decisions and on recovery.

### Decision History

Append events in order. Never rewrite or delete an earlier row. The latest event for a subject is current.

| Event  | Subject | Decision source | Status or value | Proposed destination | Final destination | Owner | More information needed | Smallest next action | Rationale |
|--------|---------|-----------------|-----------------|----------------------|-------------------|-------|-------------------------|----------------------|-----------|
| RD-001 | Participation | user | user-owned (standalone dispatch from the squad coordinator; no confirmed automatic RPI Agent mode) | none | none | Squad Coordinator | none | Coordinator runs the per-item walkthrough or confirms an agent-owned decision | The reviewer cannot ask the user questions from a dispatch; the user or coordinator owns decisions. |
| RD-002 | Walkthrough | user | pending: not started. No question channel in this dispatch. | none | none | Squad Coordinator | RV-001 to RV-011 undecided | Walk RV-001 first, then RV-002 | Each finding must be presented and answered one at a time before any decision is recorded. |
| RD-003 | Execution | agent | Partial: mechanical checks complete; full prose read and two checks not done | rpi-research or follow-up for the unread boundary | none | Squad Reviewer | Manual read of prose; ES-39 section; Scribe history entry | Coordinator decides whether a manual read is required before approval | The Partial status names the unassessed boundary (see Missing or limited evidence). |
| RD-004 | Outcome | agent | proposed: Defects found (pending parent decision) | none | none | Squad Coordinator | decisions on RV-001 and RV-002 | Coordinator records final outcome after RD-002 | Three High findings change release content and coverage claims; the set is credible and not blocked. |

## Validation Evidence

| Command | Scope | Status | Summary |
|---------|-------|--------|---------|
| `git tag -l 'product/*'` | repository tags | Passed | Empty. No `product/*` tag exists. |
| `git log --oneline -- docs/product` | commits touching the product documents | Passed | No commit touches `docs/product/`. The two existing commits predate the run. |
| `git status --short` | working tree | Passed | `docs/` is untracked. Squad state files show changes made by other stages, not by this review. |
| Analysis scripts in `.copilot-tracking/reviews/probe-2026-11-15/` (read-only; stdout only; output files `out_docs.txt` and `out_ids.txt`) | backlog, releases, traceability, C1 table, ids, figures, style, FR mapping, covers, final checks | Passed | 140 register items; 0 tag or release mismatches; 28 of 28 BR and NFR covered; 107 planned items in exactly one release file; 57 of 57 FR mapped; C1 identical in BRD, PRD and backlog; findings listed above. |
| Build or test (`az bicep build`, `dotnet test`) | none in scope | Skipped | Documents only. No IaC or code changed (ES-27, ES-37). |
| Scribe history entry | squad state | Unavailable | Squad state is read-only to this review; not checked. |

## Risks, Blockers, and Residual Work

* Blockers: none. The record is credible and not blocked.
* Remaining active work: none for the reviewer. Decisions on RV-001 and RV-002 are needed before the release files can be approved.
* Residual work: (1) manual line-by-line read of the BRD, PRD, experiments and backlog prose, and a manual 10-paragraph style sample per document (PNFR-01), owner Squad Coordinator. (2) Check of backlog section 6 (tool mapping, ES-39) and section 5 (unplanned list), owner Squad Coordinator. (3) Check of the Scribe history entry for this stage, owner Squad Coordinator. (4) The implementation changes record named in the plan is missing; the implementing role writes it, owner Squad Coordinator.

## Review Record

### Scope and Evidence

* Task ID: NW-PRODUCT-DOCS-2026-11-15
* Review date: 2026-11-15
* Review scope: full task (six product documents, six release files, plan C1 to C11 and checks RC-01 to RC-16).
* Assessed boundary: business case (`knowledge-docs/business-case.md`), current state (`knowledge-docs/current-state.md`), engineering standards (`knowledge-docs/engineering-standards.md`), plan `.copilot-tracking/plans/2026-11-15/northwind-product-documents-plan.md` (full, including C1 to C11 and RC-01 to RC-16), research `.copilot-tracking/research/2026-11-15/northwind-product-documents-research.md` (sections (a), (e) and (g) read; other sections not re-read), intake review `.copilot-tracking/reviews/2026-11-15-northwind-intake-review.md`, and the deliverables `docs/product/business-requirements.md`, `product-requirements.md`, `experiments.md`, `backlog.md`, `traceability.md` and `releases/azure-r1..r3.md` and `dotnet-r1..r3.md`.
* Review depth and provenance: standard; default (no explicit deep request).
* Candidate identity: task NW-PRODUCT-DOCS-2026-11-15; documents as on disk at review time (uncommitted; no commit exists).
* Review execution: Partial
* Helper use: none. No helper lane was dispatched; the comparison was done in one pass by the reviewer.
* Plan: .copilot-tracking/plans/2026-11-15/northwind-product-documents-plan.md
* Plan critique: skipped (plan charter; the Squad Challenger or council gate owns the independent challenge).
* Changes: .copilot-tracking/changes/2026-11-15/northwind-product-documents-changes.md is missing (directory absent). Recorded as a finding gap (see residual work).
* Record path: the caller requested this path. The plan's canonical path (`.copilot-tracking/reviews/logs/2026-11-15/northwind-product-documents-review.md`, plan C8 D7) was not used; the coordinator should confirm which path the Artifact Gate reads.
* Other evidence considered: git state; source documents above.
* Process note: the analysis scripts were created with shell heredocs for some files, not with the file-create tool. They are in the probe directory only and change nothing in the deliverables; disclosed for transparency.

### Opening Review State

* Interpreted review goal: decide whether the Northwind product document set satisfies the user's request and plan C1 to C11, and what must change before the product owner approves a release.
* Review scope: full task.
* Evidence readiness: all six product documents and six release files present; sources present; changes record absent.
* Acceptance basis: user request (BRD; PRD for planned releases; one MVE per business area; prioritised backlog with Given/When/Then and enablers; track tags; per-track releases with track and release tags; traceability table; source ids; ASSUMPTION and OPEN labels; cross-track dependencies as OPEN; nothing implemented, deployed, committed or tagged) and plan C1 to C11, RC-01 to RC-16.
* First comparison boundary: mechanical checks over the whole set, then targeted reads of the sources, plan contract, research sections (e) and (g), and the flagged lines.
* Active read-only boundaries: this record is the only file written. Deliverables, plan, research, intake review, knowledge documents and squad state were not modified.
* Authority: the review parent compares evidence and writes findings. Final outcome, routes and continuation are recorded in Parent Decision Record.
* Initial blockers: none.

### Acceptance and Change Coverage

| Requirement or scope | Implementation and validation evidence | Assessment | Finding or rationale |
|---|---|---|---|
| PFR-01 BRD exists at `docs/product/business-requirements.md` | file present; frontmatter `status: draft`; sections 1 to 15 | Met | RV-003, RV-005, RV-008, RV-011 for specific defects |
| PFR-02 PRD covers all planned releases | `product-requirements.md` section 6 and 7; 57 FR; all six releases | Met | RV-006 wording |
| PFR-03 one MVE per business area (MVE-01 BA-01, MVE-02 BA-02, MVE-03 BA-03) | `experiments.md` sections 2 and 3; three MVEs; each has riskiest assumption, decision triggers, safety statement | Met (structure); thresholds labelled A-35 | RV-004 (A-14, O-10 to O-14), RV-009 (sample size) |
| PFR-04 prioritised backlog, epics, features, stories, enablers with Given/When/Then | `backlog.md`: 140 items (12 epics, 37 features, 57 stories, 34 enablers); 57 stories with As a/I want/so that and at least two Given/When/Then each; 34 enablers with at least one | Met | none |
| PFR-05 traceability maps every BR and NFR to stories and lists uncovered and out-of-scope | `traceability.md`: 28 of 28 ids present; 39 rows; "not covered" none; out-of-scope none | Met for mapping; coverage wording overstated for BR-13 | RV-002 |
| PFR-06 six release files with track tag, release tag, stories, covered ids, leaves-out, OPEN dependencies | six files; items equal the register per release (ids, titles, priority, rank, tags); section 4 and section 5 present | Met | RV-001 (window), RV-004 (register), RV-006 |
| PFR-07 BA-03 documented, tagged `track-power-platform` only, release `unplanned`, dependencies OPEN, claims pilot OPEN | BA-03 items carry only the track tag (30 items); release column `unplanned`; no BA-03 release file; X-20 to X-27 OPEN; O-07 and A-25 cited | Met | none |
| PFR-08 reuse of A, O, G, OQ, X, T ids; no assumption presented as requirement | 175 ids defined; no meaning conflict found in owner or wording comparison; sampled 9 FR rows that carry ASSUMPTION or OPEN markers; each is labelled | Met (sampled for the second half) | RV-004, RV-005, RV-007 |
| PFR-09 documents follow C1 to C7 | C1 identical in BRD section 10.2, PRD section 6.2 and backlog section 1.1 (7 rows each); id families per C6; track tags per C7 | Met | RV-001 (window value) |
| PFR-10 ids follow C6 and C7; source ids verbatim | verbatim check of BR (19), NFR (9), C (8), SM (7); P (6) by script | Met except C-02 expansion | RV-008 |
| PFR-11 no Git tag, no commit, no deployment | `git tag -l 'product/*'` empty; no commit touches `docs/product/`; no deployment claim found by text scan | Met | none |
| RC-01 coverage of 19 BR and 9 NFR | all 28 present in traceability and backlog `Covers:` fields; 0 mismatches | Met | RV-002 (overstatement) |
| RC-02 source cites on every story and enabler | script check of `(source:` on 57 stories and 34 enablers | Met | none |
| RC-03 exactly one track tag per epic, feature, story and enabler; id block matches | script: 140 items each with one track tag; id blocks 1xx, 2xx, 3xx by track | Met | none |
| RC-04 release tags only on planned items; BA-03 and EPIC-204 untagged | register and detail blocks agree; no release tag on any unplanned item | Met | none |
| RC-05 one release per item; epic and feature tags equal children; covered ids equal C1 | 107 planned items in exactly one release file; 0 unplanned items in files; epic and feature tags equal child tags; section 4 of each file matches C1 (extra ids in azure-r1, azure-r2 and dotnet-r1 are labelled "supports, does not cover") | Met | RV-001 |
| RC-06 canonical consistency across documents | C1 identical; windows in release frontmatter equal C1; grep finds no other release name | Met (except window value) | RV-001 |
| RC-07 story quality (ES-05) | As a/I want/so that; at least two Given/When/Then; developer-readable text (sampled) | Met (structure); sampled readability | RV-010 (style) |
| RC-08 mandatory acceptance content | BR-01 isolation: STORY-230/AC2; BR-04 and BR-09 freshness: STORY-233/AC2, STORY-262/AC2; BR-15 no self-approval: STORY-321/AC2; BR-14 under 2 minutes and 5 photos: STORY-320/AC2 and AC3; NFR-01 probe in CET: STORY-142/AC1; NFR-02 p95 on server: STORY-243/AC1; NFR-06 RPO and RTO: STORY-146/AC1, STORY-172/AC1 | Met | none |
| RC-09 style (ES-01 to ES-04) | sampled by script; acronym and sentence-length sample | Partly met | RV-010, RV-009, RV-007 |
| RC-10 traceability table exists; scope BA-01 to BA-03; out-of-scope `none`; split ids list every story | sections 1 to 5 of `traceability.md` | Met | RV-002 |
| RC-11 release file content (ES-31) | each file: track, release tag, stories, covered ids, leaves-out, OPEN dependencies, "never waits" statement | Met | RV-001, RV-004 |
| RC-12 BA-03 handling | covered, track-only, `unplanned`, no placeholder release file, X-20 to X-27 OPEN, O-07 and A-25 on the claims pilot | Met | none |
| RC-13 no real deployment, no secrets, no personal data | text scan for deployment verbs, tenant changes, secrets patterns and e-mail addresses: none | Met | none |
| RC-14 location (ES-07) | all files at `docs/product/` and `docs/product/releases/` | Met | none |
| RC-15 Git state | `git tag -l 'product/*'` empty; no commit from this run; planned tags written as text, marked not created | Met | none |
| RC-16 MVE completeness | three MVEs, one per area; local; falsifiable; thresholds labelled A-35; owner and decision triggers present | Met | RV-009 (sample size label) |
| Business figures (business case C-04, C-08, SM targets, dates) | checked against `knowledge-docs/business-case.md` and `current-state.md`; derived arithmetic recomputed (see RV-009) | Met except labels | RV-001 (dates); RV-009 |
| OPEN items carry owners from the stakeholder list (ES-04) | every A, O and X table row names an owner who appears in business case section 5 | Met for table rows; prose-only OPEN not checked | none |
| Release dependencies: no release waits for another track (ES-31) | text scan for wait and dependency language; each dependency row is OPEN with a stated stub | Met | RV-006 (wording only) |
| Business sources and the plan's Canonical Contract C1 to C11 | read in full | Met | none |

### Critique and Follow-Up Assessment

* Latest critique dispositions: critique skipped by charter; not applicable. The plan records no independent challenge.
* Material revisions: the plan's C9 promised A-01 to A-48 and O-01 to O-25; the document set added A-49 to A-57 and O-26 to O-30 during drafting. These additions are not yet in the BRD register (RV-005) and their rationale is recorded in the PRD and backlog.
* Dependent-work pause assessment: no dependent work resumed early. The Azure and .NET release files each state that no release waits for another track.
* Justification assessment: the new ids A-49 to A-57 and O-26 to O-30 are labelled "New" with an owner; their rationale is stated in the register rows.

| Follow-up item | Why outside immediate scope | Owner or next action | Assessment and route |
|---|---|---|---|
| Missing implementation changes record `.copilot-tracking/changes/2026-11-15/northwind-product-documents-changes.md` | evidence artifact the plan names for the Artifact Gate | Squad Coordinator to assign the implementing role | Open; distinct follow-up |
| Manual prose read and 10-paragraph style sample (PNFR-01) | outside what this review could assess mechanically | Squad Coordinator | Open; distinct follow-up |
| Backlog section 5 and section 6 check (ES-39 mapping) | not read in this pass | Squad Coordinator | Open; distinct follow-up |
| Scribe history entry for this stage | squad state is read-only to this review | Squad Coordinator (Scribe) | Open; distinct follow-up |
| Release-path choice (plan C8 D7 path vs caller path) | two paths named in different sources | Squad Coordinator to confirm the Artifact Gate path | Open; distinct follow-up |

### Reviewer Self-Check

* [x] Every supplied requirement, acceptance criterion, in-scope marker, material update, critique disposition, validation result, blocker, remaining item and plan follow-up has an assessment or explicit gap (see Acceptance and Change Coverage and the follow-up table).
* [x] Findings are substantive, evidence-grounded, severity-graded, and use stable `RV-xxx` IDs with expected and observed behavior, a resolution condition, and one proposed route each.
* [x] Execution status (Partial), assessed outcome (Defects found, proposed), validation coverage, limitations and routes are consistent.
* [x] The summary is scoped and advisory; findings keep their supporting context together; coverage distinguishes demonstrated gaps from unassessed behavior.
* [ ] Standard review completely assessed the material boundary. Not fully met: the prose of the six product documents was checked by scripts and targeted reads, not read line by line. This is the reason for Partial.
* [x] No source, plan, critique, research, changes record or squad state was modified. Only this record was written. No validation was executed beyond read-only analysis. No helper was used.
* Checked boundary: all deliverable files by script; C1 table; registers; sources (business case, current state, engineering standards); plan contract; research sections (e) and (g); git state; targeted reads of cited lines.
* Missing or limited evidence: (1) manual line-by-line prose read of the six product documents and six release files; (2) backlog sections 5 and 6 (unplanned list and ES-39 mapping); (3) research sections (a) to (d) and (f) re-read; (4) Scribe history entry; (5) implementation changes record (absent); (6) manual ES-01 10-paragraph sample; (7) full manual check that every "ASSUMPTION" and "OPEN" in prose is in a register (sampled only).
