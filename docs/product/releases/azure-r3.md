---
release_file_id: "REL-AZURE-R3"
track: "azure"
track_tag: "track-azure"
release: "azure-r3"
release_tag: "azure-r3"
planned_git_tag: "product/azure-r3"
git_tag_status: "to be created after approval; not created"
status: "proposed"
document_status: "draft"
approver: "OPEN: O-09 (proposed Lena Varga, A-38)"
approval_date: ""
target_window: "1 Apr to 27 June 2027"
source_backlog_id: "BACKLOG-NW-001"
source_prd_id: "PRD-NW-001"
last_updated: "2026-11-15"
---

# Release `azure-r3`: Cutover and recovery proof

> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> Status: **Draft for review.** Release status: **Proposed, awaiting product-owner approval.** Nothing here is approved. **Nothing is deployed to Azure, and no Git tag or commit has been made** (ES-27, A-39).

## 1. Release header

| Field | Value |
|---|---|
| Track | Azure, track tag `track-azure` (business area BA-01) (source: ES-30) |
| Release tag | `azure-r3` (source: ES-31) |
| Planned Git tag | `product/azure-r3`. **To be created on approval; not created.** |
| Release status | **Proposed, awaiting product-owner approval** |
| Document status | Draft for review |
| Approver | **OPEN:** O-09, who is the named release approver for the Azure track? Owner: Marc Dubois. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner of the assumption: Marc Dubois. |
| Approval date | blank until a human approves (see section 11) |
| Source documents | `docs/product/backlog.md` (BACKLOG-NW-001), `docs/product/product-requirements.md` (PRD-NW-001), `docs/product/traceability.md`, `docs/product/experiments.md` (MVE-01) |
| Releases of this track | [azure-r1](azure-r1.md), [azure-r2](azure-r2.md), `azure-r3` (this file) |

**A release never waits for another track** (ES-31, A-45). A need from another track is an **OPEN:** row in section 6, with the way this release goes on without it.

For the business reader: an *Azure release* is a reviewed plan or design set, checked locally. It is never a deployment (ES-27). A *runbook* is a step-by-step procedure that a person follows. *Cutover* is the moment Order Desk starts running in Azure instead of in the Lyon data centre. *Rollback* is the way back to the old service if a step fails. *ESU* means paid Extended Security Updates for servers past end of support. *RPO* (recovery point objective) is how much recent data may be lost; *RTO* (recovery time objective) is how long recovery may take.

## 2. Objective and theme

**Theme (identical to the canonical release proposal, C1): Cutover and recovery proof.**

**Objective.** Give the team a reviewed database migration and rehearsal procedure and a reviewed cutover, rollback, recovery-test and decommission plan, so that Order Desk can move to Azure inside the Sunday maintenance window (06:00 to 12:00 CET) before the data-centre lease ends on 30 June 2027 (C-01), and so that availability and recovery can be proved against `NFR-01` and `NFR-06` (source: BR-13, NFR-01, NFR-03, NFR-06, C-01, C-02, SM-07, CS-07, CS-21, CS-23).

**What approval means (A-53).** The product owner approves `azure-r3` **before the first rehearsal Sunday, before 6 June 2027**. Approval covers the reviewed migration procedure, rehearsal plan, runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test are planned execution **after** that approval. They are not performed or claimed by this release (ES-27).

| Field | Value |
|---|---|
| Target window | **1 Apr to 27 June 2027.** This is the target period for the release: its content is complete and approved before the first rehearsal Sunday (before 6 June 2027), and the planned execution Sundays (6, 13, 20 and 27 June 2027) fall inside the window. It is a target, not a commitment (A-01, A-42). The window was extended from the first proposal so that these Sundays fall inside it (A-58). |
| Main epic | `EPIC-104` Cutover and recovery proof |
| Items in the release | 13 (1 epic, 4 features, 5 stories, 3 enablers) |

**In this release (IN).** The database migration and rehearsal (`FEAT-114`, `EA-16`): the steps that move `NorthwindOrders` to the chosen data tier, and the rehearsal plan, as procedures checked locally. It was added after the first review because no earlier item designed the database move (A-59). It is gated by MVE-01 through the data-tier option.

**OPEN:** O-27. The window ends on 27 June 2027, so the rehearsal Sundays (6 and 13 June 2027) and the live cutover and fallback Sundays (20 and 27 June 2027) are inside it, 3 days before the lease ends on 30 June 2027 (A-58, C-01). Approval is due before the first rehearsal Sunday, before 6 June 2027 (A-53). Marc Dubois is asked to confirm the extended window, the 3-day margin and the approval date. The release does not wait for the answer; the plan states the Sundays as proposed dates.

## 3. Items in the release

Every item below carries the track tag `track-azure` **and** the release tag `azure-r3`, and belongs to this release only (ES-31). Ids and titles are copied from the backlog item register (section 2.1) without change. Rank is the backlog rank (A-46); epics and features have no rank. *Enabler* is a story with a technical role (A-40).

**MVE gate.** MVE-01 asks: *can a platform-as-a-service (PaaS, managed) data tier carry `NorthwindOrders` and the nightly StockPilot exchange inside the cost cap?* It gates this release **through its inputs** (the chosen data tier and its backup and cost figures), not through any single item here. **Result: pending. The experiment has not been run** (source: `docs/product/experiments.md`).

| Id | Title | Type | Priority | Rank | Source ids (ES-02) | Tags | MVE gate |
|---|---|---|---|---|---|---|---|
| EPIC-104 | Cutover and recovery proof | epic | Must | — | BR-13, NFR-01, NFR-03, NFR-06, C-01, C-02, SM-07, CS-07, CS-21, CS-23 | `track-azure` `azure-r3` | **MVE-01**, through its inputs |
| FEAT-114 | Database migration and rehearsal | feature | Must | — | BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23 | `track-azure` `azure-r3` | **MVE-01** (through the data-tier option) |
| EA-16 | Migrate the NorthwindOrders database to the chosen data tier and rehearse the move | enabler | Must | 29 | BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23 | `track-azure` `azure-r3` | **MVE-01** (decision before commit) |
| FEAT-110 | Cutover and rollback runbooks | feature | Must | — | BR-13, C-01, C-02, CS-21, SM-07 | `track-azure` `azure-r3` | none directly |
| EA-13 | Write cutover, rollback and decommission runbooks | enabler | Must | 30 | CS-21, BR-13, C-02, SM-07 | `track-azure` `azure-r3` | none directly (depends on `EA-05`, `EA-08`, `EA-04`, `EA-15`, `EA-16`) |
| STORY-170 | Keep staff working through the cutover inside the Sunday window | story | Must | 31 | BR-13, C-01, CS-21 | `track-azure` `azure-r3` | none directly |
| STORY-171 | Define rollback and rehearsal for every cutover step | story | Must | 32 | BR-13, C-01, CS-21 | `track-azure` `azure-r3` | none directly |
| FEAT-111 | Recovery and availability proof | feature | Must | — | NFR-01, NFR-06, CS-22, CS-23, T-14 | `track-azure` `azure-r3` | none directly |
| EA-14 | Write the first recovery test plan and evidence template | enabler | Must | 33 | NFR-06, CS-23, T-14 | `track-azure` `azure-r3` | none directly (depends on `EA-08`) |
| STORY-172 | Prove recovery against RPO 1 hour and RTO 4 hours | story | Must | 34 | NFR-06, CS-07, CS-23 | `track-azure` `azure-r3` | none directly |
| STORY-173 | Plan the availability proof for the first weeks in Azure | story | Must | 35 | NFR-01, CS-22 | `track-azure` `azure-r3` | none directly |
| FEAT-112 | Decommission of the old servers | feature | Must | — | C-01, C-02, SM-07 | `track-azure` `azure-r3` | none directly |
| STORY-174 | Retire the old web and database servers before 30 June 2027 | story | Must | 36 | C-02, SM-07, C-01 | `track-azure` `azure-r3` | none directly |

Counts: epics 1, features 4, stories 5, enablers 3, **total 13**. These equal the backlog section 3 row for `azure-r3`. Enablers match the canonical enabler allocation (C4) plus `EA-16`, added after the first review (A-59): `EA-13`, `EA-14` and `EA-16`. `EA-14` is the first recovery test plan and evidence template, split from `EA-08` so that each item belongs to one release (C2, A-43).

### 3.1 What the MVE-01 decision does to this release

MVE-01 is owned by Ahmed Benali (IT Manager). Thresholds are **ASSUMPTION:** A-35 (owner Lena Varga).

| MVE-01 result | Effect on `azure-r3` |
|---|---|
| **Go** | The chosen PaaS option is the base for the migration steps (`EA-16`), the runbooks (`EA-13` depends on `EA-05`, `EA-08`, `EA-04`, `EA-15` and `EA-16`) and the recovery test plan (`EA-14`). Scope stays as in section 3. |
| **Adjust** | If the virtual-machine fallback is taken, the migration steps in `EA-16` and the cutover steps, the rollback path and the restore method in `EA-13`, `EA-14` and `STORY-172` follow the VM option; the item list does not change. Marc Dubois is informed. |
| **Stop** | Planning on the current cap stops (source: `docs/product/experiments.md` section 3.1.5). `EA-16`, `EA-13` and `EA-14` cannot be finished without a chosen data tier. Marc Dubois decides whether to relax C-04 or reduce scope (**OPEN:** O-21). Items do not move to another release. Whether `azure-r3` is approved without the affected items is **OPEN:** AZ3-O1. |
| **Not yet decided** | `EA-16`, `EA-13`, `EA-14` and the stories they serve are written against **ASSUMPTION:** A-21 (PaaS preferred, virtual machine fallback) and are re-checked when the result is recorded. |

## 4. Requirement identifiers covered (`BR-` and `NFR-`)

This section equals the canonical release table (C1), the coverage matrix (C3), the backlog and the traceability reverse view.

| Identifier | Part covered in `azure-r3` | Covering story | Where the rest is covered |
|---|---|---|---|
| `BR-13` (Order Desk staff keep working through the move to Azure; planned downtime stays inside the Sunday maintenance window) | **Whole requirement, as plans and procedures.** The covering stories deliver the cutover plan and the rollback and rehearsal plan. The design items `EA-15` (application hosting, `azure-r2`) and `EA-16` (database migration and rehearsal, this release) define how the application is hosted and how the database moves, validated locally. Applying them to a subscription, the rehearsals and the live cutover are planned execution after approval, which comes before 6 June 2027 (A-53, ES-27). | STORY-170, STORY-171 (supported by `EA-13`, `EA-15`, `EA-16`) | Not split. |
| `NFR-01` (Availability of 99.5 % during business hours, Monday to Saturday 06:00 to 20:00 CET) | **Proof** (the plan for the proof in the first weeks in Azure) | STORY-173 | `azure-r2`, design and alerting, `STORY-142` |
| `NFR-06` (RPO of 1 hour and RTO of 4 hours for order data) | **Proof** (recovery test plan and evidence) | STORY-172 (supported by `EA-14`) | `azure-r2`, design, `STORY-146` |

**Supports, but does not cover:** SM-07 (production servers past end of support: 2 today, 0 by 30 June 2027; `EA-13`, `STORY-174`), C-01 (lease ends 30 June 2027) and C-02 (servers past end of support, ESU payments). `STORY-174` is not the covering story of an identifier; it delivers the plan that makes SM-07 reachable.

## 5. What this release leaves out, and where it goes

| Left out (C1) | Where it goes | Items |
|---|---|---|
| Optimisation after the lease | **Unplanned.** It would be an unplanned item with only the `track-azure` tag. No item exists. It would need a new request and, if planned, a new release name (PRD section 6.2). | none |
| Carrying out the rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027), the recovery restore test and the retirement of the servers | Planned execution after approval, which comes before 6 June 2027 (A-53). Not claimed here. | `STORY-172/AC3` |
| Hosting runtime choice (rehost or `net10.0`) | The hosting definition is in `azure-r2` (`EA-15`). The choice stays **OPEN:** O-03, owner Ahmed Benali. | `EA-15` (`azure-r2`) |
| Application code changes, including a stateless session draft | Other track, `track-dotnet` (`EN-06`, `dotnet-r1`); see X-07 | not in this release |
| Anything after 27 June 2027 | Not planned. The lease ends on 30 June 2027 (C-01); the 3 days after the window are the margin (A-58). | none |
| Any deployment, apply or change in an Azure subscription | Never in this workshop (ES-27) | none |

## 6. Dependencies on other tracks (all **OPEN:**, none is a wait)

Rows are the canonical cross-track rows for `azure-r3` (C11): X-07 (single instance) and O-15 (post-lease locations). Full text is in `docs/product/product-requirements.md` section 10.1 and `docs/product/backlog.md` section 7.3.

| Id | **OPEN:** dependency | Direction | Owner to confirm | How `azure-r3` goes on without waiting | Items affected |
|---|---|---|---|---|---|
| X-07 | The in-process session order draft must be stateless before scale-out (single instance) | Azure needs .NET | Ahmed Benali | **Deferral and assumption:** the cutover and rollback runbooks plan for a **single application instance**; scale-out is not part of this release. **ASSUMPTION:** a single instance is enough for the cutover and for the first weeks in Azure (owner Ahmed Benali). Scale-out is picked up when the .NET track has replaced the session draft. | `EA-13`, `STORY-170`, `STORY-171` |
| O-15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Both (an unanswered business question, not a track) | Ahmed Benali, Julien Moreau | **Deferral:** no answer is assumed. Each affected step in the runbooks and in the decommission plan is marked **OPEN:** with its owner and is not designed as a fact. The release is not blocked (`EA-02/AC2`, `STORY-102/AC3`). | `EA-13`, `STORY-170`, `STORY-174` |

**Additional cross-track row cited by an item in this release (not in C11).**

| Id | **OPEN:** dependency | Direction | Owner to confirm | How `azure-r3` goes on | Items affected |
|---|---|---|---|---|---|
| X-03 | Database sign-in moves from Windows-integrated sign-in to Entra or a managed identity | Both | Ahmed Benali | **Stub:** Azure writes the migration steps for a managed identity (`EA-16`). The .NET track builds against a local SQL Server meanwhile. Neither track waits. | `EA-16` |

**Other open questions relied on (not tracks):** **OPEN:** O-03 (rehost .NET Framework 4.8 or wait for `net10.0`; the application-hosting step in the runbooks is marked **OPEN:** and no answer is assumed; **ASSUMPTION:** A-20, a Windows virtual-machine rehost is the contingency if .NET slips; owner Ahmed Benali), **OPEN:** O-27 (extended window, 3-day margin and approval before 6 June 2027, see section 2).

## 7. Entry conditions and exit criteria

### 7.1 Entry conditions

Entry conditions are about readiness to start. None waits for another track.

| Id | Condition | Status |
|---|---|---|
| EC-1 | Approval and funding to build. **OPEN:** O-21, owner Marc Dubois. | Open |
| EC-2 | The MVE-01 decision (go, adjust or stop) is recorded. Result pending. | Not run |
| EC-3 | Azure-track inputs from `azure-r1` and `azure-r2` are available: the data-tier record (`EA-05`), the backup and retention design (`EA-08`), the application hosting definition (`EA-15`) and the monitoring design (`EA-04`, `STORY-142`). This is one team's own sequence. | Open |
| EC-4 | The release counts, windows and placements are confirmed, including the extended window against the June rehearsal Sundays. **OPEN:** O-25 and O-27, owners Lena Varga and Marc Dubois. | Open |
| EC-5 | The release approver is named. **OPEN:** O-09, owner Marc Dubois. | Open |
| EC-6 | Which Sundays are available for rehearsal and for live cutover and fallback (6 and 13 June for rehearsal, 20 and 27 June for live and fallback, computed from CS-21), and that approval is given before 6 June 2027 (A-53, O-27). | Proposed |

### 7.2 Exit criteria (all testable, local validation only)

The release is ready for approval when every row passes. Each row names the story criteria (`<item id>/AC<n>`, Given / When / Then in the backlog) that prove it. Rows describe **plans and documents**, not carried-out operations (A-53).

| Id | Exit criterion | Proven by |
|---|---|---|
| XC-1 | Every cutover step has a stated longest duration and the steps add up to a planned downtime inside Sunday 06:00 to 12:00 CET. A step without a duration is not accepted; a step that would pass 12:00 is split across Sundays or given a rollback. | `EA-13/AC1`, `STORY-170/AC1`, `STORY-170/AC2`, `STORY-170/AC3` (`BR-13`) |
| XC-2 | Every cutover step has a rollback path that returns Order Desk to the previous service inside the same window. A step without a rollback path stops approval. | `EA-13/AC2`, `STORY-171/AC1`, `STORY-171/AC3` |
| XC-3 | The rehearsal plan names the Sundays for rehearsal (6 and 13 June 2027), live cutover and fallback (20 and 27 June 2027), all inside the window that ends on 27 June 2027 (A-58); it includes a template to record each result and carries **OPEN:** O-27. | `EA-13/AC4`, `STORY-171/AC2` |
| XC-4 | The decommission runbook and plan state how and when `NWWEB01` and `NWSQL01` are retired so that production servers past end of support are 0 by 30 June 2027 (SM-07), and state the date on which ESU payments stop. A retirement date after 30 June 2027 is not accepted. | `EA-13/AC3`, `STORY-174/AC1`, `STORY-174/AC2`, `STORY-174/AC3` |
| XC-5 | The recovery test template records the measured data loss in minutes and the restore time in hours next to the pass limits of 60 minutes and 4 hours; the plan states who restores, from which backup and when; it calls the first test the baseline and claims no earlier result. | `EA-14/AC1`, `EA-14/AC2`, `EA-14/AC3` |
| XC-6 | The recovery proof is defined as: data loss at most 60 minutes and restore time at most 4 hours is a pass; a worse result records `NFR-06` as **not met** and reopens `EA-08`. The restore test is carried out after approval and is not claimed in this release. | `STORY-172/AC1`, `STORY-172/AC2`, `STORY-172/AC3` (`NFR-06`, proof) |
| XC-7 | The availability-proof plan uses the synthetic-probe rule of `STORY-142` (hosting edge, local Central European time with summer time, Monday to Saturday 06:00 to 20:00), lists the weekly figure and every downtime event with start, end and cause, and flags a week below 99.5 % as `not met` instead of averaging it away. | `STORY-173/AC1`, `STORY-173/AC2`, `STORY-173/AC3` (`NFR-01`, proof) |
| XC-8 | The claim that a log-based restore fits the Sunday window stays marked **ASSUMPTION:** A-33 until the rehearsals prove it; the release does not present it as shown. | `STORY-122/AC3`, A-33 |
| XC-9 | Every item in section 3 has a source cite, the tags `track-azure` and `azure-r3`, and every unanswered question is **OPEN:** with an owner. | `docs/product/backlog.md` section 2.1 and section 4.1 |
| XC-10 | No document or file in the release claims that a rehearsal, cutover, restore or retirement has been done, or that anything was deployed, applied or created in a tenant or subscription, and none holds a secret. | ES-27, ES-17, A-53 |
| XC-11 | The database migration steps cover schema, data, sign-in and every job with no equivalent, each with a longest duration that fits the Sunday window; the rehearsal compares row counts and checksums with the source and fails on a difference; the target tier is in the EU; the moved copy is handed to the first restore test of `EA-14`; the rehearsals are planned execution after approval and not claimed as done. | `EA-16/AC1`, `EA-16/AC2`, `EA-16/AC3`, `EA-16/AC4`, `EA-16/AC5`, `EA-16/AC6` (`NFR-03`, `NFR-06`) |

## 8. ASSUMPTION and OPEN items for this release

Ids are those of the PRD and backlog registers and keep their numbers (full wording and owners: `docs/product/backlog.md` section 7, the register of record). `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

### 8.1 ASSUMPTION items

| Id | ASSUMPTION | Confirming owner |
|---|---|---|
| A-01 | Build starts December 2026 after approval; release approval dates are targets. | Marc Dubois |
| A-05 | `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. | Ahmed Benali |
| A-06 | Prioritisation is MoSCoW from the business case, then date and dependency risk. NFRs are Must. | Lena Varga |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | Ahmed Benali |
| A-21 | A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Ahmed Benali |
| A-35 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | Lena Varga |
| A-38 | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-40 | Enabler id families `EN-`, `EA-`, `EP-` and hundreds blocks per track for `EPIC-`, `FEAT-`, `STORY-` and `FR-`. | Lena Varga |
| A-42 | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-43 | Cross-cutting NFRs are split per track and, where design and proof differ, per release. The first recovery test plan is `EA-14`. | Ahmed Benali |
| A-45 | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | Backlog rank: enablers before the stories that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-53 | Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). | Ahmed Benali |
| A-49 | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must (A-06; `EA-14` protects `NFR-06`, `EA-16` protects `NFR-03` and `NFR-06`). An enabler that serves only another track's requirements is Should (so `EN-14` and `FR-240` are Should). | Lena Varga |
| A-58 | The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). | Marc Dubois |
| A-59 | `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. | Ahmed Benali |
| (this file) | A single application instance is enough for the cutover and the first weeks in Azure (see X-07). | Ahmed Benali |

### 8.2 OPEN items

| Id | **OPEN:** | Who can answer |
|---|---|---|
| O-03 | Rehost .NET Framework 4.8 or wait for `net10.0`; is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-06 | Which backlog tool and which ES-28 prefix? Item types and fields in the tool are not validated. | Lena Varga |
| O-09 | Who is the named release approver for the Azure track? | Marc Dubois |
| O-15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-21 | Approval and funding to build. | Marc Dubois |
| O-25 | Confirm the release counts, windows and placements. | Lena Varga, Marc Dubois |
| O-27 | Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. | Marc Dubois |
| AZ3-O1 | **OPEN (this file):** if MVE-01 ends in **stop**, does the product owner approve `azure-r3` without the affected items (`EA-16`, `EA-13`, `EA-14` and their stories), or hold it? Items do not move. | Lena Varga, Marc Dubois |

Id `AZ3-O1` is local to this file. This file is its register; it is not in the backlog register.

### 8.3 Inconsistency note

* **IN-4.** The canonical release table lists "optimisation after the lease (unplanned items)" as left out of `azure-r3`, but the backlog holds no unplanned `track-azure` item. This file records the line as stated and names no item.

### 8.4 Cross-track rows cited

X-07 and X-03 are registered with their owner in section 6 (Ahmed Benali).

## 9. Publication note (ES-39)

Nothing has been published to any tracker (O-06 names no tool; `tracker_published: false`). When the backlog is published, the track tag and the release tag travel with every item in section 3 so that the release stays identifiable in the tool.

| Tool | How `track-azure` and `azure-r3` appear |
|---|---|
| **Azure DevOps** | Work-item tags `track-azure` and `azure-r3` on every item in section 3. |
| **GitHub** | Issue labels `track-azure` and `azure-r3`, plus one milestone named `azure-r3`. |
| **Jira** | Labels `track-azure` and `azure-r3`, plus one fix version named `azure-r3`. |

In every tool, titles, descriptions and source identifiers follow ES-28 and ES-29: the published title is `<id> <title>` with the participant prefix (**OPEN:** O-06), and each description links back to its `BR-`, `NFR-` and other source ids.

## 10. Where this release sits in the Azure track

| Release | Theme | Window | Items | Git tag (planned text, not created) |
|---|---|---|---|---|
| [`azure-r1`](azure-r1.md) | Foundation, data platform decision and cost proof | 1 Dec 2026 to 29 Jan 2027 | 21 | `product/azure-r1` |
| [`azure-r2`](azure-r2.md) | Pilot environment, exchange and storage, observability | 1 Feb to 31 Mar 2027 | 20 | `product/azure-r2` |
| `azure-r3` (this file) | Cutover and recovery proof | 1 Apr to 27 June 2027 | 13 | `product/azure-r3` |

## 11. Approval and tagging procedure

Nothing in this procedure is carried out by this document. Nothing is deployed to Azure (ES-27). The approval is due before the first rehearsal Sunday, before 6 June 2027, and does not perform the rehearsals, the cutover or the recovery test, which are planned execution after it (A-53).

1. **Review.** The approver reviews section 3 (items), section 4 (identifiers) and section 7.2 (exit criteria) against the backlog and the local validation results.
2. **Confirm the approver.** **OPEN:** O-09. Until Marc Dubois names the approver, the product owner (Lena Varga, A-38) is the proposed approver and Marc Dubois the escalation.
3. **Record the approval** in the block below: name, date and decision.
4. **Commit.** After approval, the commit that holds this release file and the release content is made by a human (A-39).
5. **Tag.** Only then, tag that commit `product/azure-r3` (ES-31). **Do not create the tag before approval.**
6. **Publish (optional, later).** Apply section 9 when the backlog is published.

### Approval block

| Field | Value |
|---|---|
| Release | `azure-r3` |
| Track tag / release tag | `track-azure` / `azure-r3` |
| Planned Git tag | `product/azure-r3` — **to be created after approval; not created** |
| Approver | **OPEN:** O-09 (proposed: Lena Varga, A-38; escalation Marc Dubois) |
| Decision | ☐ Approved  ☐ Approved with changes  ☐ Not approved |
| Approval date | _(blank)_ |
| Commit id that holds the release | _(blank until approved and committed)_ |
| Git tag created on | _(blank, not created)_ |

<!-- end of azure-r3 -->
