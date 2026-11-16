---
release_file_id: "REL-AZURE-R2"
track: "azure"
track_tag: "track-azure"
release: "azure-r2"
release_tag: "azure-r2"
planned_git_tag: "product/azure-r2"
git_tag_status: "to be created after approval; not created"
status: "proposed"
document_status: "draft"
approver: "OPEN: O-09 (proposed Lena Varga, A-38)"
approval_date: ""
target_window: "1 Feb to 31 Mar 2027"
source_backlog_id: "BACKLOG-NW-001"
source_prd_id: "PRD-NW-001"
last_updated: "2026-11-15"
---

# Release `azure-r2`: Pilot environment, exchange and storage, observability

> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> Status: **Draft for review.** Release status: **Proposed, awaiting product-owner approval.** Nothing here is approved. **Nothing is deployed to Azure, and no Git tag or commit has been made** (ES-27, A-39).

## 1. Release header

| Field | Value |
|---|---|
| Track | Azure, track tag `track-azure` (business area BA-01) (source: ES-30) |
| Release tag | `azure-r2` (source: ES-31) |
| Planned Git tag | `product/azure-r2`. **To be created on approval; not created.** |
| Release status | **Proposed, awaiting product-owner approval** |
| Document status | Draft for review |
| Approver | **OPEN:** O-09, who is the named release approver for the Azure track? Owner: Marc Dubois. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner of the assumption: Marc Dubois. |
| Approval date | blank until a human approves (see section 11) |
| Source documents | `docs/product/backlog.md` (BACKLOG-NW-001), `docs/product/product-requirements.md` (PRD-NW-001), `docs/product/traceability.md`, `docs/product/experiments.md` (MVE-01) |
| Releases of this track | [azure-r1](azure-r1.md), `azure-r2` (this file), [azure-r3](azure-r3.md) |

**A release never waits for another track** (ES-31, A-45). A need from another track is an **OPEN:** row in section 6, with the way this release goes on without it.

For the business reader: an *Azure release* is a reviewed design set, checked on a laptop (for example with `az bicep build`, which turns a Bicep file into a deployment template without applying it). It is never a deployment (ES-27). *RPO* (recovery point objective) is how much recent data may be lost; *RTO* (recovery time objective) is how long recovery may take. *SFTP* is a secure file-transfer service. *CSV* is a plain comma-separated file. *StockPilot* is the warehouse system in Antwerp that stays on premises (C-03).

## 2. Objective and theme

**Theme (identical to the canonical release proposal, C1): Pilot environment, exchange and storage, observability.**

**Objective.** Land, as a reviewed and locally validated design, everything the Q2 2027 customer-portal pilot and the move to Azure need around the application: the hosting of the Order Desk web application in `tst` and `prd`, the nightly StockPilot exchange working without changing its file contract, a plan for invoice files and outbound mail after the lease, monitoring with alerts, a test environment (`tst`) where the pilot can run, and the backup, 7-year retention and recovery design (source: BR-13, C-01, C-02, C-03, C-04, C-06, NFR-01, NFR-06, NFR-08, CS-10, CS-12, CS-13, CS-15, CS-16, CS-22, CS-23).

| Field | Value |
|---|---|
| Target window | **1 Feb to 31 Mar 2027.** This is the period by which the release content is expected to be complete and ready for the product owner to approve. It is a target, not a commitment (A-01, A-42). |
| Main epic | `EPIC-103` Pilot environment, exchange, storage and observability |
| Items in the release | 20 (1 epic, 5 features, 7 stories, 7 enablers) |

**In this release (IN).** The application hosting (`FEAT-113`, `EA-15`): the design of where the Order Desk web application runs in `tst` and `prd`, as infrastructure code checked locally. It was added after the first review because no earlier item designed the hosting runtime (A-59). The runtime choice (rehost on a Windows virtual machine, or wait for `net10.0`) stays **OPEN:** O-03 (see AZ2-O2 in section 8.2). The production database settings of `EA-15` wait for the MVE-01 decision; test hosting does not.

## 3. Items in the release

Every item below carries the track tag `track-azure` **and** the release tag `azure-r2`, and belongs to this release only (ES-31). Ids and titles are copied from the backlog item register (section 2.1) without change. Rank is the backlog rank (A-46); epics and features have no rank. *Enabler* is a story with a technical role (A-40). Priority follows A-06 and A-49: an enabler that serves only another track's requirements is Should.

**MVE gate.** MVE-01 asks: *can a platform-as-a-service (PaaS, managed) data tier carry `NorthwindOrders` and the nightly StockPilot exchange inside the cost cap?* Its decision (go, adjust or stop) is taken **before** a gated item is committed. A gate is a decision point, not a wait for another track. **Result: pending. The experiment has not been run** (source: `docs/product/experiments.md`).

| Id | Title | Type | Priority | Rank | Source ids (ES-02) | Tags | MVE gate |
|---|---|---|---|---|---|---|---|
| EPIC-103 | Pilot environment, exchange, storage and observability | epic | Must | — | BR-13, C-01, C-02, C-03, C-04, C-06, NFR-01, NFR-06, NFR-08, CS-06, CS-08, CS-10, CS-12, CS-13, CS-15, CS-16, CS-22, CS-23, ES-21, ES-23, ES-25, ES-26 | `track-azure` `azure-r2` | **MVE-01** for `EA-06` and `EA-08` and the stories they serve, and for the production database settings of `EA-15` |
| FEAT-113 | Application hosting | feature | Must | — | BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25 | `track-azure` `azure-r2` | **MVE-01** for the production database settings of `EA-15` only |
| EA-15 | Host the Order Desk web application in the test and production environments | enabler | Must | 15 | BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25 | `track-azure` `azure-r2` | **MVE-01** for the production database settings only (test hosting does not wait; the runtime choice is O-03) |
| FEAT-106 | StockPilot exchange, invoice storage and outbound mail | feature | Must | — | C-03, CS-08, CS-10, CS-11, CS-12, BR-09 | `track-azure` `azure-r2` | **MVE-01** (`EA-06`, `STORY-140`) |
| EA-06 | Redesign the StockPilot exchange without changing the file contract | enabler | Must | 16 | CS-10, C-03 | `track-azure` `azure-r2` | **MVE-01** |
| EA-07 | Design invoice storage and synchronisation | enabler | Should | 17 | CS-08, CS-11, CS-14 | `track-azure` `azure-r2` | none |
| EA-12 | Design outbound mail to replace the on-premises relay | enabler | Should | 18 | CS-12, A-29, BR-09 | `track-azure` `azure-r2` | none |
| STORY-140 | Keep the nightly StockPilot exchange working after the database moves | story | Must | 19 | C-03, CS-10, BR-13 | `track-azure` `azure-r2` | **MVE-01** |
| STORY-141 | Decide where invoice files live after the lease | story | Should | 20 | CS-08, CS-11, CS-14 | `track-azure` `azure-r2` | none |
| STORY-144 | Replace the on-premises mail relay for outbound e-mail | story | Could | 21 | CS-12, BR-09 | `track-azure` `azure-r2` | none |
| FEAT-107 | Observability and alerting | feature | Must | — | NFR-01, CS-15, CS-22, ES-26 | `track-azure` `azure-r2` | none |
| EA-04 | Build observability: log workspace, application monitoring and alerts | enabler | Must | 22 | CS-15, CS-22, ES-26, NFR-01 | `track-azure` `azure-r2` | none |
| STORY-142 | Monitor availability with a synthetic probe and alerts | story | Must | 23 | NFR-01, CS-15, CS-22, ES-26 | `track-azure` `azure-r2` | none |
| FEAT-108 | Test environment for the portal pilot | feature | Must | — | ES-23, C-04, business-case section 8 | `track-azure` `azure-r2` | none |
| EA-10 | Define the tst environment | enabler | Must | 24 | ES-23, business-case section 8 | `track-azure` `azure-r2` | none (see IN-2, section 8.3) |
| STORY-143 | Define a test environment where the portal pilot can run | story | Must | 25 | ES-23, C-04, business-case section 8 | `track-azure` `azure-r2` | none (see IN-2, section 8.3) |
| FEAT-109 | Backup, retention and recovery design | feature | Must | — | NFR-06, NFR-08, CS-07, CS-23 | `track-azure` `azure-r2` | **MVE-01** (`EA-08`, `STORY-146`) |
| EA-08 | Design backup, long-term retention and recovery | enabler | Must | 26 | CS-07, CS-23, NFR-06, NFR-08 | `track-azure` `azure-r2` | **MVE-01** |
| STORY-145 | Keep order-change records for 7 years in Azure | story | Must | 27 | NFR-08, CS-07 | `track-azure` `azure-r2` | through `EA-08` (**MVE-01**) |
| STORY-146 | Design backup and recovery for RPO 1 hour and RTO 4 hours | story | Must | 28 | NFR-06, CS-07, CS-23 | `track-azure` `azure-r2` | **MVE-01** |

Counts: epics 1, features 5, stories 7, enablers 7, **total 20**. These equal the backlog section 3 row for `azure-r2`. Enablers match the canonical enabler allocation (C4) plus `EA-15`, added after the first review (A-59): `EA-04`, `EA-06`, `EA-07`, `EA-08`, `EA-10`, `EA-12`, `EA-15`. `EA-08` holds the backup and retention design only; the first recovery test plan was split into `EA-14`, which sits in `azure-r3` (C2, A-43).

### 3.1 What the MVE-01 decision does to this release

MVE-01 is owned by Ahmed Benali (IT Manager). Thresholds are **ASSUMPTION:** A-35 (owner Lena Varga). The decision is taken in `azure-r1` time, before `azure-r2` content for `EA-06` and `EA-08` is committed.

| MVE-01 result | Effect on `azure-r2` |
|---|---|
| **Go** | `EA-06` starts from the documented replacements of the unsupported constructs; `EA-08` designs backup for the chosen option; the production database settings of `EA-15` take the chosen option from `EA-05`. Release scope stays as in section 3. |
| **Adjust** | If the virtual-machine fallback is taken, `EA-06` is re-scoped (the exchange may keep Windows-only steps, recorded in a decision record that departs from ES-21), `EA-08` follows the VM backup options, and the production database settings of `EA-15` follow the VM option. If a PaaS option is taken with reduced cost headroom, `EA-09` and `X-12` carry it. The scope list in section 3 does not change; the wording of the gated items does. Marc Dubois is informed. |
| **Stop** | Planning of `azure-r2` scope on the current cap stops: `EA-06`, `EA-08` and `EA-10` are paused (source: `docs/product/experiments.md` section 3.1.5), and the production database settings of `EA-15` are delayed. `EA-04`, `EA-07` and `EA-12` do not depend on the data tier. Test hosting in `EA-15` proceeds with a placeholder connection setting from user secrets or a managed identity and no password (ES-17, ES-25; `EA-15/AC6`). Marc Dubois decides whether to relax C-04 or reduce scope (**OPEN:** O-21). Items do not move to another release. Whether `azure-r2` is approved without the paused items and settings is **OPEN:** AZ2-O1. |
| **Not yet decided** | `EA-06`, `EA-08` and the stories they serve stay uncommitted. |

## 4. Requirement identifiers covered (`BR-` and `NFR-`)

This section equals the canonical release table (C1), the coverage matrix (C3), the backlog and the traceability reverse view.

| Identifier | Part covered in `azure-r2` | Covering story | Other releases that cover the rest |
|---|---|---|---|
| `NFR-01` (Availability of 99.5 % during business hours, Monday to Saturday 06:00 to 20:00 CET) | **Design and alerting** | STORY-142 (supported by `EA-04`) | `azure-r3`, proof plan, `STORY-173` |
| `NFR-06` (RPO of 1 hour and RTO of 4 hours for order data) | **Design** | STORY-146 (supported by `EA-08`) | `azure-r3`, recovery proof, `STORY-172` with `EA-14` |
| `NFR-08` (Every change to an order is recorded for 7 years) | **Retention design** (Azure side) | STORY-145 (supported by `EA-08`) | `dotnet-r2`, content side, `STORY-241` |

**Supports, but does not cover:** C-03 (StockPilot stays on premises; exchange file contract unchanged, `EA-06`, `STORY-140`) and C-04 (cost cap; `tst` is part of the model, `STORY-143/AC3`). `EA-15` (application hosting) is a design item for `BR-13` (and supports C-01, C-02, C-06 and `NFR-01`), but it covers no `BR-` identifier by itself. `STORY-140` cites `BR-13` as a source, and `STORY-144` and `EA-12` cite `BR-09`, but neither requirement is covered here: `BR-13` is covered in `azure-r3` (`STORY-170`, `STORY-171`, with the design items `EA-15` and `EA-16`) and `BR-09` by `STORY-262` in `dotnet-r3` (C3). No `BR-` identifier is covered in this release.

## 5. What this release leaves out, and where it goes

| Left out (C1) | Where it goes | Items |
|---|---|---|
| Cutover rehearsal and runbooks | `azure-r3` | `EA-13`, `STORY-170`, `STORY-171` |
| Recovery proof (first recovery test plan, restore test, availability proof) | `azure-r3` | `EA-14`, `STORY-172`, `STORY-173` |
| Database migration and rehearsal (moving `NorthwindOrders` to the chosen data tier) | `azure-r3` | `EA-16` |
| `BR-13` (staff keep working through the move) | `azure-r3` | `STORY-170`, `STORY-171` (with the design items `EA-15`, `EA-16`) |
| Decommission of the old servers | `azure-r3` | `STORY-174` |
| Hosting runtime choice (rehost or `net10.0`) | The hosting definition is **in this release** (`EA-15`). The runtime choice stays **OPEN:** O-03, owner Ahmed Benali (AZ2-O2). | `EA-15` |
| The application code and the pilot itself (portal, `dotnet-r2`) | Other track, `track-dotnet` | not in this release |
| Any deployment, apply or change in an Azure subscription | Never in this workshop (ES-27) | none |

## 6. Dependencies on other tracks (all **OPEN:**, none is a wait)

Rows are the canonical cross-track rows for `azure-r2` (C11): X-02, X-07, X-09, X-10. Full text is in `docs/product/product-requirements.md` section 10.1 and `docs/product/backlog.md` section 7.3.

| Id | **OPEN:** dependency | Direction | Owner to confirm | How `azure-r2` goes on without waiting | Items affected |
|---|---|---|---|---|---|
| X-02 | A `net10.0` application that follows a documented configuration and identity contract | Azure needs .NET | Ahmed Benali | **Stub:** the `tst` definition does not depend on how the application is built, so the Azure track is not blocked by .NET and .NET is not blocked by Azure (`EA-10/AC2`, `STORY-143/AC2`). For `EA-15`, the Order Desk build arrives from the .NET track or as the unchanged application rehosted under A-20; Azure writes the hosting definition for either shape and validates it locally, and the release does not wait (`EA-15/AC2`). | `EA-10`, `STORY-143`, `EA-15` |
| X-07 | The in-process session order draft must be stateless before scale-out | Azure needs .NET | Ahmed Benali | **Deferral and assumption:** the pilot environment is designed for a **single web instance**; scale-out is deferred until the .NET track replaces the session draft (`EN-06`). **ASSUMPTION:** a single instance is enough for a 20-customer pilot (A-17, owner Ahmed Benali). | `EPIC-103` (hosting design in `EA-10`, `STORY-143`, `EA-15/AC4`) |
| X-09 | Invoice files move from a network path to Azure storage | Both | Julien Moreau, Ahmed Benali | **Assumption:** the finance system stays the writer (`EA-07/AC1`, `STORY-141/AC1`). The location after the lease is marked **OPEN:** and the story still completes as a design (`STORY-141/AC2`, O-15). **ASSUMPTION:** A-15, invoice number and folder year (owner Julien Moreau). | `EA-07`, `STORY-141` |
| X-10 | Outbound mail replaces the on-premises relay | Both | Ahmed Benali | **Stub:** the .NET track uses a mail abstraction and a local mail catcher meanwhile. Azure designs the replacement path and does not assume what sends order confirmations today (`EA-12/AC2`, `STORY-144/AC2`, O-17). | `EA-12`, `STORY-144` |

**Additional cross-track rows cited by items in this release (not in C11).** These rows are things the .NET track needs from Azure; the Azure track provides them in its own items and does not wait.

| Id | **OPEN:** dependency | Owner | How `azure-r2` goes on | Items |
|---|---|---|---|---|
| X-01 | Hosting target and pilot test environment for the modernised application (.NET needs Azure) | Ahmed Benali | Azure provides the `tst` definition. .NET builds and tests locally until pilot hosting is answered. The pilot database is **OPEN:** O-23, **ASSUMPTION:** A-37 (the pilot reads the Azure-hosted database after `azure-r2` is approved; owner Ahmed Benali). | `EA-10`, `STORY-143` |
| X-05 | StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) | Ahmed Benali | Azure owns the exchange end to end; .NET only reads the status results. **ASSUMPTION:** A-27, the CSV contract and pick-up stay as they are. Where the Agent job and the Antwerp transfer task are defined is **OPEN:** MVE-O-05. | `EA-06`, `STORY-140` |
| X-08 | Logging moves to Application Insights and Log Analytics (.NET needs Azure) | Ahmed Benali | .NET logs through the standard logger to the console meanwhile. | `EA-04`, `STORY-142` |
| X-12 | The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) | Ahmed Benali | Azure sizes the host from today's load (CS-06), lists it in the cost model of `EA-09` and refines it when the portal size is known. | `EA-15` |
| X-15 | Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) | Ahmed Benali | .NET defines the audit content (T-13); Azure sets the retention period. **ASSUMPTION:** A-31, backup and long-term retention can cover 7 years. | `EA-08`, `STORY-145` |

Also relied on: **OPEN:** O-15 (post-lease locations), O-16 (how Delivered is set; StockPilot pick-up cadence), O-17 (what sends order confirmations), O-23 (pilot database). Each is marked **OPEN:** inside the item that uses it and does not block the release.

## 7. Entry conditions and exit criteria

### 7.1 Entry conditions

Entry conditions are about readiness to start. None waits for another track.

| Id | Condition | Status |
|---|---|---|
| EC-1 | Approval and funding to build. **OPEN:** O-21, owner Marc Dubois. | Open |
| EC-2 | MVE-01 decision (go, adjust or stop) is recorded before `EA-06` and `EA-08` are committed. Result pending. | Not run |
| EC-3 | Azure-track inputs from `azure-r1` are available: the validated foundation (`EA-01`, as the base for `EA-04`, `EA-07`, `EA-10`) and the data-tier record (`EA-05`, which `EA-06` and `EA-08` depend on). This is one team's own sequence. If `azure-r1` is not approved by 29 Jan 2027, `azure-r2` work on items without those inputs proceeds and the rest is held. | Open |
| EC-4 | The release counts, windows and placements are confirmed. **OPEN:** O-25, owners Lena Varga and Marc Dubois. | Open |
| EC-5 | The release approver is named. **OPEN:** O-09, owner Marc Dubois. | Open |
| EC-6 | Pilot database decision. **OPEN:** O-23, owner Ahmed Benali. Not a start condition: until it is answered, `EA-10/AC3` states **ASSUMPTION:** A-37. | Open |

### 7.2 Exit criteria (all testable, local validation only)

The release is ready for approval when every row passes. Each row names the story criteria (`<item id>/AC<n>`, Given / When / Then in the backlog) that prove it.

| Id | Exit criterion | Proven by |
|---|---|---|
| XC-1 | The redesigned StockPilot exchange keeps the file format, file names and pick-up point of today's baseline, has no step that depends on `xp_cmdshell` or another Windows-only tool, and a produced file that differs in a column, a name or a location fails the comparison and is not handed to StockPilot. StockPilot is not changed. | `EA-06/AC1`, `EA-06/AC2`, `STORY-140/AC1`, `STORY-140/AC2`, `STORY-140/AC3` (C-03) |
| XC-2 | The SFTP route after the lease is marked **OPEN:** with its owner, not stated as a fact. | `EA-06/AC3`, `EA-02/AC2` |
| XC-3 | The invoice-storage design covers about 120 GB today and about 135 GB by 30 June 2027 with continued growth, keeps the finance system as the writer, and marks the post-lease location **OPEN:** while still completing as a design. | `EA-07/AC1`, `EA-07/AC2`, `EA-07/AC3`, `STORY-141/AC1`, `STORY-141/AC2` |
| XC-4 | The outbound mail design names a replacement path in the EU that requires authentication, and lists "what sends order confirmations today" as **OPEN:** without assuming an answer. | `EA-12/AC1`, `EA-12/AC2`, `STORY-144/AC1`, `STORY-144/AC2` |
| XC-5 | Each of `tst` and `prd` has exactly one log workspace receiving the diagnostics of every resource; applications report to application monitoring; an availability alert and an application-error alert replace today's ping checks and weekly Event Log look. | `EA-04/AC1`, `EA-04/AC2`, `EA-04/AC3` |
| XC-6 | Availability is measured by a synthetic probe at the hosting edge, per week, in local Central European time with summer time, over Monday to Saturday 06:00 to 20:00 (84 hours); a week below 99.5 % raises an alert; Sunday 06:00 to 12:00 downtime is not counted. | `STORY-142/AC1`, `STORY-142/AC2`, `STORY-142/AC3`, `STORY-142/AC4` (`NFR-01`, A-05, T-17) |
| XC-7 | `az bicep build` on the `tst` entry point passes locally; names follow ES-23 and tags follow ES-24; the definition lists every resource the pilot needs, does not depend on how the application is built, states which database the pilot reads (**ASSUMPTION:** A-37 until O-23 is answered), and appears in the cost model. Nothing is applied. | `EA-10/AC1`, `EA-10/AC2`, `EA-10/AC3`, `STORY-143/AC1`, `STORY-143/AC2`, `STORY-143/AC3` |
| XC-8 | The backup design states a frequency of 60 minutes or less, the restore method and who runs a restore, and shows how RPO 1 hour and RTO 4 hours are reached **on paper**; it does not claim that the target is met, because a recovery has never been tested. A documented frequency longer than 60 minutes returns the design for rework. | `EA-08/AC1`, `EA-08/AC3`, `STORY-146/AC1`, `STORY-146/AC2`, `STORY-146/AC3` (`NFR-06`, design) |
| XC-9 | The retention design shows 7 years for order-change records and how backup and long-term retention achieve it; a tier that keeps backups for less than 7 years is rejected or sent to the product owner as an exception; limits not verified stay marked **ASSUMPTION:** A-31. | `EA-08/AC2`, `STORY-145/AC1`, `STORY-145/AC2`, `STORY-145/AC3` (`NFR-08`, retention design) |
| XC-10 | Every item in section 3 has a source cite, the tags `track-azure` and `azure-r2`, and every unanswered question is **OPEN:** with an owner. | `docs/product/backlog.md` section 2.1 and section 4.1 |
| XC-11 | No document or file in the release claims that anything was deployed, applied or created in a tenant or subscription, and none holds a secret. | ES-27, ES-17 |
| XC-12 | `az bicep build` on the hosting definition of `tst` and of `prd` passes locally; the definition states which runtime it describes and marks the other as **OPEN:** O-03; the application reaches data services by managed identity and private endpoint with no password; one instance runs until the session draft is stateless; the host size appears in the cost model; `tst` hosting is complete with a placeholder connection setting that holds no password, and the production database settings wait for the MVE-01 decision. Nothing is applied. | `EA-15/AC1`, `EA-15/AC2`, `EA-15/AC3`, `EA-15/AC4`, `EA-15/AC5`, `EA-15/AC6` |

## 8. ASSUMPTION and OPEN items for this release

Ids are those of the PRD and backlog registers and keep their numbers (full wording and owners: `docs/product/backlog.md` section 7, the register of record). `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

### 8.1 ASSUMPTION items

| Id | ASSUMPTION | Confirming owner |
|---|---|---|
| A-01 | Build starts December 2026 after approval; release approval dates are targets. | Marc Dubois |
| A-05 | `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. | Ahmed Benali |
| A-06 | Prioritisation is MoSCoW from the business case, then date and dependency risk. NFRs are Must. | Lena Varga |
| A-15 | The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. | Julien Moreau |
| A-17 | Pilot customer concurrency is small (20 customers). No customer load figure exists. | Ahmed Benali |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | Ahmed Benali |
| A-27 | The StockPilot CSV contract and file pick-up stay as they are. | Ahmed Benali |
| A-29 | The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | Ahmed Benali |
| A-31 | Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Ahmed Benali |
| A-35 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | Lena Varga |
| A-37 | The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. | Ahmed Benali |
| A-38 | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-40 | Enabler id families `EN-`, `EA-`, `EP-` and hundreds blocks per track for `EPIC-`, `FEAT-`, `STORY-` and `FR-`. | Lena Varga |
| A-42 | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-43 | Cross-cutting NFRs are split per track and, where design and proof differ, per release. The first recovery test plan is `EA-14`. | Ahmed Benali |
| A-45 | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | Backlog rank: enablers before the stories that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-49 | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must (A-06). An enabler that serves only another track's requirements is Should (so `EN-14` and `FR-240` are Should). | Lena Varga |
| A-51 | Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. | Ahmed Benali |
| A-54 | Measurement rules for `NFR-03` to `NFR-09` are the author's proposals. | Ahmed Benali, Lena Varga |
| A-58 | The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). | Marc Dubois |
| A-59 | `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. | Ahmed Benali |

### 8.2 OPEN items

| Id | **OPEN:** | Who can answer |
|---|---|---|
| O-03 | Rehost .NET Framework 4.8 or wait for `net10.0`; is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-06 | Which backlog tool and which ES-28 prefix? Item types and fields in the tool are not validated. | Lena Varga |
| O-09 | Who is the named release approver for the Azure track? | Marc Dubois |
| O-15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-16 | How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? | Ahmed Benali, Pieter Janssens |
| O-17 | What sends order confirmations today? | Ahmed Benali |
| O-21 | Approval and funding to build. | Marc Dubois |
| O-23 | Which database does the Q2 2027 portal pilot read (T-08)? | Ahmed Benali |
| O-24 | What does the customer identity service cost, and does it count toward C-04? | Ahmed Benali |
| O-25 | Confirm the release counts, windows and placements. | Lena Varga, Marc Dubois |
| MVE-O-05 | Where are the SQL Server Agent job and the Windows scheduled task for the Antwerp transfer defined? | Ahmed Benali |
| AZ2-O1 | **OPEN (this file):** if MVE-01 ends in **stop**, does the product owner approve `azure-r2` without the paused items (`EA-06`, `EA-08`, `EA-10` and their stories) and without the production database settings of `EA-15`, or hold it? Items do not move. | Lena Varga, Marc Dubois |
| AZ2-O2 | **OPEN (this file):** which runtime does `EA-15` describe first: the unchanged application rehosted on a Windows virtual machine (A-20), or a managed web service for `net10.0`? Confirm before `EA-15` is committed (O-03). | Ahmed Benali |

Ids `AZ2-O1` and `AZ2-O2` are local to this file. This file is their register; they are not in the backlog register.

### 8.3 Inconsistency notes

* **IN-2.** `docs/product/experiments.md` (stop result) pauses `EA-10` together with `EA-06` and `EA-08`, but the backlog shows gate *none* for `EA-10` and `STORY-143`. This file shows the backlog value and flags the difference. Owner: Lena Varga.
* **IN-3.** The dependency of `dotnet-r2` on this release is the database the pilot reads after `azure-r2` is approved (A-37), not a start order. The `azure-r2` window (1 Feb to 31 Mar 2027) overlaps the `dotnet-r2` window (1 Mar to 30 Apr 2027) by 31 days. Because a release never waits for another track, `dotnet-r2` builds and tests locally until the `tst` definition exists (X-01). Owner: Ahmed Benali.

## 9. Publication note (ES-39)

Nothing has been published to any tracker (O-06 names no tool; `tracker_published: false`). When the backlog is published, the track tag and the release tag travel with every item in section 3 so that the release stays identifiable in the tool.

| Tool | How `track-azure` and `azure-r2` appear |
|---|---|
| **Azure DevOps** | Work-item tags `track-azure` and `azure-r2` on every item in section 3. |
| **GitHub** | Issue labels `track-azure` and `azure-r2`, plus one milestone named `azure-r2`. |
| **Jira** | Labels `track-azure` and `azure-r2`, plus one fix version named `azure-r2`. |

In every tool, titles, descriptions and source identifiers follow ES-28 and ES-29: the published title is `<id> <title>` with the participant prefix (**OPEN:** O-06), and each description links back to its `BR-`, `NFR-` and other source ids.

## 10. Where this release sits in the Azure track

| Release | Theme | Window | Items | Git tag (planned text, not created) |
|---|---|---|---|---|
| [`azure-r1`](azure-r1.md) | Foundation, data platform decision and cost proof | 1 Dec 2026 to 29 Jan 2027 | 21 | `product/azure-r1` |
| `azure-r2` (this file) | Pilot environment, exchange and storage, observability | 1 Feb to 31 Mar 2027 | 20 | `product/azure-r2` |
| [`azure-r3`](azure-r3.md) | Cutover and recovery proof | 1 Apr to 27 June 2027 (A-58) | 13 | `product/azure-r3` |

## 11. Approval and tagging procedure

Nothing in this procedure is carried out by this document. Nothing is deployed to Azure (ES-27).

1. **Review.** The approver reviews section 3 (items), section 4 (identifiers) and section 7.2 (exit criteria) against the backlog and the local validation results.
2. **Confirm the approver.** **OPEN:** O-09. Until Marc Dubois names the approver, the product owner (Lena Varga, A-38) is the proposed approver and Marc Dubois the escalation.
3. **Record the approval** in the block below: name, date and decision.
4. **Commit.** After approval, the commit that holds this release file and the release content is made by a human (A-39).
5. **Tag.** Only then, tag that commit `product/azure-r2` (ES-31). **Do not create the tag before approval.**
6. **Publish (optional, later).** Apply section 9 when the backlog is published.

### Approval block

| Field | Value |
|---|---|
| Release | `azure-r2` |
| Track tag / release tag | `track-azure` / `azure-r2` |
| Planned Git tag | `product/azure-r2` — **to be created after approval; not created** |
| Approver | **OPEN:** O-09 (proposed: Lena Varga, A-38; escalation Marc Dubois) |
| Decision | ☐ Approved  ☐ Approved with changes  ☐ Not approved |
| Approval date | _(blank)_ |
| Commit id that holds the release | _(blank until approved and committed)_ |
| Git tag created on | _(blank, not created)_ |

<!-- end of azure-r2 -->
