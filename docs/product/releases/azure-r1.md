---
release_file_id: "REL-AZURE-R1"
track: "azure"
track_tag: "track-azure"
release: "azure-r1"
release_tag: "azure-r1"
planned_git_tag: "product/azure-r1"
git_tag_status: "to be created after approval; not created"
status: "proposed"
document_status: "draft"
approver: "OPEN: O-09 (proposed Lena Varga, A-38)"
approval_date: ""
target_window: "1 Dec 2026 to 29 Jan 2027"
source_backlog_id: "BACKLOG-NW-001"
source_prd_id: "PRD-NW-001"
last_updated: "2026-11-15"
---

# Release `azure-r1`: Foundation, data platform decision and cost proof

> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> Status: **Draft for review.** Release status: **Proposed, awaiting product-owner approval.** Nothing here is approved. **Nothing is deployed to Azure, and no Git tag or commit has been made** (ES-27, A-39).

## 1. Release header

| Field | Value |
|---|---|
| Track | Azure, track tag `track-azure` (business area BA-01) (source: ES-30) |
| Release tag | `azure-r1` (source: ES-31) |
| Planned Git tag | `product/azure-r1`. **To be created on approval; not created.** |
| Release status | **Proposed, awaiting product-owner approval** |
| Document status | Draft for review |
| Approver | **OPEN:** O-09, who is the named release approver for the Azure track? Owner: Marc Dubois. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner of the assumption: Marc Dubois. |
| Approval date | blank until a human approves (see section 11) |
| Source documents | `docs/product/backlog.md` (BACKLOG-NW-001), `docs/product/product-requirements.md` (PRD-NW-001), `docs/product/traceability.md`, `docs/product/experiments.md` (MVE-01) |
| Releases of this track | `azure-r1` (this file), [azure-r2](azure-r2.md), [azure-r3](azure-r3.md) |

**A release never waits for another track** (ES-31, A-45). A need from another track is an **OPEN:** row in section 6, with the way this release goes on without it.

For the business reader: an *Azure release* is a reviewed design set, checked on a laptop (for example with `az bicep build`, a command that turns a Bicep file into a deployment template without applying it). It is never a deployment (ES-27). *Bicep* is the language used to describe Azure resources as code (ES-22). *IaC* means infrastructure as code. *MVE* means minimum viable experiment, the smallest test that can prove an assumption wrong.

## 2. Objective and theme

**Theme (identical to the canonical release proposal, C1): Foundation, data platform decision and cost proof.**

**Objective.** Give the Azure team one reviewed foundation (naming, tags, EU region, connectivity, secrets, private access), a written decision on where the order database will run, and a cost model that shows whether Order Desk and the portal fit the EUR 1,500 monthly cap (C-04). This release needs no .NET change, and it settles the data tier early so that `azure-r2` and `azure-r3` build on a chosen option (source: NFR-03, NFR-05, C-01, C-02, C-04, C-06).

| Field | Value |
|---|---|
| Target window | **1 Dec 2026 to 29 Jan 2027.** This is the period by which the release content is expected to be complete and ready for the product owner to approve. It is a target, not a commitment (A-01, A-42). |
| Main epics | `EPIC-101` Azure foundation and security baseline; `EPIC-102` Data platform decision, cost and migration approach |
| Items in the release | 21 (2 epics, 5 features, 8 stories, 6 enablers) |

## 3. Items in the release

Every item below carries the track tag `track-azure` **and** the release tag `azure-r1`, and belongs to this release only (ES-31). Ids and titles are copied from the backlog item register (section 2.1) without change. Rank is the backlog rank (A-46): enablers come before the stories they serve; epics and features have no rank. *Enabler* is a story with a technical role (A-40). Priority follows A-06 and A-49.

**MVE gate.** MVE-01 asks: *can a platform-as-a-service (PaaS, managed) data tier carry `NorthwindOrders` and the nightly StockPilot exchange inside the cost cap?* Its decision (go, adjust or stop) is taken **before** a gated item is committed. A gate is a decision point, not a wait for another track. **Result: pending. The experiment has not been run** (source: `docs/product/experiments.md`).

| Id | Title | Type | Priority | Rank | Source ids (ES-02) | Tags | MVE gate |
|---|---|---|---|---|---|---|---|
| EPIC-101 | Azure foundation and security baseline | epic | Must | — | NFR-03, NFR-05, C-01, CS-09, CS-13, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27 | `track-azure` `azure-r1` | none |
| FEAT-101 | Environment foundation as code and validation | feature | Must | — | CS-09, CS-19, NFR-03, ES-20 to ES-24, ES-27 | `track-azure` `azure-r1` | none |
| EA-01 | Build the Azure foundation as code (naming, tags, region, modules) | enabler | Must | 1 | CS-09, NFR-03, ES-20, ES-21, ES-22, ES-23, ES-24, ES-27 | `track-azure` `azure-r1` | none |
| EA-11 | Build the infrastructure validation and deployment pipeline design | enabler | Must | 2 | CS-19, ES-22, ES-27 | `track-azure` `azure-r1` | none |
| STORY-101 | Review a test and production environment design set | story | Must | 3 | C-01, CS-09, ES-20, ES-22, ES-23, ES-24, ES-27 | `track-azure` `azure-r1` | none |
| STORY-104 | Keep every Azure resource in an EU region | story | Must | 4 | NFR-03, ES-20 | `track-azure` `azure-r1` | none |
| STORY-105 | Validate every infrastructure definition locally before release | story | Must | 5 | CS-19, ES-22, ES-27 | `track-azure` `azure-r1` | none |
| FEAT-102 | Hybrid connectivity design | feature | Must | — | CS-09, C-01, C-03 | `track-azure` `azure-r1` | none |
| EA-02 | Design hybrid connectivity between Lyon, Azure and Antwerp | enabler | Must | 6 | CS-09, C-01, C-03, O-15 | `track-azure` `azure-r1` | none |
| STORY-102 | Agree the connection design for the move and after the lease | story | Must | 7 | CS-09, C-01, C-03 | `track-azure` `azure-r1` | none |
| FEAT-103 | Secrets, identity and private access | feature | Must | — | NFR-05, CS-13, ES-17, ES-25 | `track-azure` `azure-r1` | none |
| EA-03 | Design secrets, managed identities and private endpoints | enabler | Must | 8 | CS-13, NFR-05, ES-17, ES-25 | `track-azure` `azure-r1` | none |
| STORY-103 | Keep secrets out of Azure-hosted code and configuration | story | Must | 9 | NFR-05, CS-13, ES-17, ES-25 | `track-azure` `azure-r1` | none |
| EPIC-102 | Data platform decision, cost and migration approach | epic | Must | — | C-02, C-04, C-06, BR-13, CS-07, CS-08, CS-21, ES-21, ES-25 | `track-azure` `azure-r1` | **MVE-01** (applies to `EA-05` and `EA-09`) |
| FEAT-104 | Data tier decision | feature | Must | — | C-02, C-06, CS-07, ES-21 | `track-azure` `azure-r1` | **MVE-01** |
| EA-05 | Record the data-tier decision and migration approach | enabler | Must | 10 | CS-07, CS-21, C-02, ES-21 | `track-azure` `azure-r1` | **MVE-01** (decision before commit) |
| STORY-120 | Decide the data tier for the order database | story | Must | 11 | C-02, C-06, CS-07, BR-13, ES-21 | `track-azure` `azure-r1` | **MVE-01** |
| FEAT-105 | Cost model and migration approach | feature | Must | — | C-04, BR-13, CS-07, CS-08, CS-21 | `track-azure` `azure-r1` | **MVE-01** |
| EA-09 | Build the Azure cost model against the monthly cap | enabler | Must | 12 | C-04, X-12, CS-03, CS-06 | `track-azure` `azure-r1` | **MVE-01** |
| STORY-121 | Show the monthly cost against the EUR 1,500 cap | story | Must | 13 | C-04, X-12, T-03 | `track-azure` `azure-r1` | **MVE-01** |
| STORY-122 | Define the database and invoice migration approach | story | Must | 14 | BR-13, CS-07, CS-08, CS-21 | `track-azure` `azure-r1` | **MVE-01** (through the data-tier option) |

Counts: epics 2, features 5, stories 8, enablers 6, **total 21**. These equal the backlog section 3 row for `azure-r1`. Enablers match the canonical enabler allocation (C4): `EA-01`, `EA-02`, `EA-03`, `EA-05`, `EA-09`, `EA-11`.

### 3.1 What the MVE-01 decision does to this release

MVE-01 is owned by Ahmed Benali (IT Manager). Its starting thresholds are **ASSUMPTION:** A-35 (owner Lena Varga, who sets the final numbers). The three checks must pass on the same option: `M1a` zero unmapped constructs, `M1b` indicative cost at or below EUR 1,200 a month (80 % of C-04), `M1c` backup frequency of 60 minutes or less.

| MVE-01 result | Effect on `azure-r1` |
|---|---|
| **Go** | `EA-05` records the chosen option. `EA-09` takes the estimate as its baseline. Release scope stays as listed in section 3. |
| **Adjust** | Either only the virtual-machine option passes (`STORY-120/AC4`: choose it, with a decision record that explains why it departs from ES-21), or a PaaS option passes `M1a` and `M1c` but costs between EUR 1,200 and EUR 1,500 (`STORY-121/AC2`: record it and tell the sponsor that headroom for the portal is below EUR 300 (derived: EUR 1,500 less EUR 1,200)). Scope in section 3 stays, but `EA-05`, `EA-09` and their stories change wording. Marc Dubois is informed. |
| **Stop** | No option stays within EUR 1,500 while meeting `M1a` and `M1c` (`STORY-121/AC3`). `EA-05` and `EA-09` stay uncommitted. Items marked gate *none* (`EA-01` to `EA-03`, `EA-11` and their stories) continue, because they do not depend on the data tier. Marc Dubois decides whether to relax C-04 or reduce scope (**OPEN:** O-21). Items do not move to another release because of the result; whether the product owner approves `azure-r1` without the gated items is **OPEN:** AZ1-O2 (section 8). |
| **Not yet decided** | `EA-05` and `EA-09` stay uncommitted (`EA-05/AC2`). The release cannot be approved with those items complete until the result is recorded. |

## 4. Requirement identifiers covered (`BR-` and `NFR-`)

This section equals the canonical release table (C1), the coverage matrix (C3), the backlog and the traceability reverse view.

| Identifier | Part covered in `azure-r1` | Covering story | Other releases or tracks that cover the rest |
|---|---|---|---|
| `NFR-03` (Customer data and order data stay in the European Union) | **Azure side** | STORY-104 | `dotnet-r2` (.NET side, `STORY-239`); BA-03 side unplanned (`STORY-301`) |
| `NFR-05` (No secret in source code or configuration files in the repository) | **Azure side** | STORY-103 | `dotnet-r1` (.NET side, `STORY-205`) |

**Supports, but does not cover:** C-01 (lease ends 30 June 2027), C-02 (servers past end of support), C-04 (cost cap, proof by `EA-09` and `STORY-121`), C-06 (a six-person team that knows .NET and SQL Server; platform services it can operate). Stories `STORY-120`, `STORY-122` and `EA-05` cite `BR-13` as a source, but `BR-13` is **covered in `azure-r3`** (`STORY-170`, `STORY-171`); the design work here is enabler work for it (C3). The two design items for it, `EA-15` (application hosting, `azure-r2`) and `EA-16` (database migration and rehearsal, `azure-r3`), were added after the first review (A-59) and are not in this release.

No `BR-` identifier is covered in this release. Not covered here and not claimed: `BR-13`, `NFR-01`, `NFR-06`, `NFR-08` (see section 5).

## 5. What this release leaves out, and where it goes

| Left out (C1) | Where it goes | Items |
|---|---|---|
| Exchange redesign (StockPilot nightly exchange) | `azure-r2` | `EA-06`, `STORY-140` |
| Hosting runtime (how the application runs on Azure: rehost .NET Framework 4.8 or wait for `net10.0`) | `azure-r2`. The hosting definition is `EA-15`. The runtime choice stays **OPEN:** O-03, owner Ahmed Benali (see AZ1-O1 in section 8). | `EA-15` |
| Pilot environment (`tst`) | `azure-r2` | `EA-10`, `STORY-143` |
| Monitoring and alerting | `azure-r2` | `EA-04`, `STORY-142` |
| Recovery: backup, retention and recovery design | `azure-r2` | `EA-08`, `STORY-145`, `STORY-146` |
| Recovery: first test plan and proof | `azure-r3` | `EA-14`, `STORY-172` |
| Cutover, rollback, decommission | `azure-r3` | `EA-13`, `STORY-170`, `STORY-171`, `STORY-174` |
| Database migration and rehearsal (moving `NorthwindOrders` to the chosen data tier) | `azure-r3`. The migration approach is decided here (`STORY-122`); the migration and rehearsal design is `EA-16`. | `EA-16` |
| `BR-13` (staff keep working through the move) | `azure-r3` | `STORY-170`, `STORY-171` (with the design items `EA-15`, `EA-16`) |
| Invoice storage and outbound mail designs | `azure-r2` | `EA-07`, `STORY-141`, `EA-12`, `STORY-144` |
| Any deployment, apply or change in an Azure subscription | Never in this workshop (ES-27) | none |

## 6. Dependencies on other tracks (all **OPEN:**, none is a wait)

Rows are the canonical cross-track rows for `azure-r1` (C11): X-02, X-03, X-11, X-12, X-14. Full text is in `docs/product/product-requirements.md` section 10.1 and `docs/product/backlog.md` section 7.3. *Entra ID* is Microsoft's cloud identity service. *Managed identity* is an Azure identity that an application uses instead of a password.

| Id | **OPEN:** dependency | Direction | Owner to confirm | How `azure-r1` goes on without waiting | Items affected |
|---|---|---|---|---|---|
| X-02 | A `net10.0` application that follows a documented configuration and identity contract | Azure needs .NET | Ahmed Benali | **Stub:** Azure writes infrastructure around a configuration contract it states itself and validates locally. The foundation does not depend on how the application is built. **ASSUMPTION:** the contract can be agreed later without changing the foundation (owner Ahmed Benali). | `EA-01`, `EA-03`, `STORY-101`, `STORY-103` |
| X-03 | Database sign-in moves from Windows-integrated sign-in to Entra or a managed identity | Both | Ahmed Benali | **Stub:** Azure designs the managed identity. The .NET track builds against a local SQL Server meanwhile. Neither track waits. | `EA-03`, `STORY-103` |
| X-11 | Build and test pipeline (.NET) and deployment pipeline (Azure) | Both | Ahmed Benali | **Assumption:** each track keeps its own pipeline. The Azure pipeline definition is tool-neutral until O-19 (which pipeline tool) is answered. | `EA-11`, `STORY-105` |
| X-12 | The shared monthly cap C-04 covers Order Desk and the portal | Azure needs .NET sizing inputs | Ahmed Benali | **Assumption:** Azure sizes from today's load (CS-03, CS-06) and refines when the portal and API sizes are known. The cost model includes the portal and the Order Desk API host as labelled estimates. | `EA-09`, `STORY-121` |
| X-14 | One solution and three projects versus a portal area and an API: a decision record is needed (T-10, `EN-13`) | Both | Ahmed Benali | **Assumption:** the Azure design set does not fix the application project shape and stays neutral. Owner Ahmed Benali. | `STORY-101` |

**Additional cross-track rows cited by items in this release (not in C11):**

| Id | **OPEN:** dependency | Owner | How `azure-r1` goes on | Items |
|---|---|---|---|---|
| X-04 | Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (O-10). The Azure side stays **OPEN:** | Ahmed Benali | `NFR-04` is split by track (C3). Azure keeps this as an **OPEN:** row and covers `NFR-03` and `NFR-05` only. The identity and mail services of the portal are covered by `STORY-239` in `dotnet-r2` (cost question O-24). | `STORY-104` |

## 7. Entry conditions and exit criteria

### 7.1 Entry conditions

Entry conditions are about readiness to start this release. None of them waits for another track.

| Id | Condition | Status |
|---|---|---|
| EC-1 | Approval and funding to build. The business case says the work is "not yet approved for build". **OPEN:** O-21, owner Marc Dubois. | Open |
| EC-2 | Build start December 2026 after approval. **ASSUMPTION:** A-01, owner Marc Dubois. Dates are targets. | Assumption |
| EC-3 | MVE-01 can start. It is local, needs no subscription, takes 5 working days and about 4 person-days (**ASSUMPTION:** MVE-A-01), and needs a local SQL Server (**ASSUMPTION:** MVE-A-04, owner Ahmed Benali). The engineer who runs it is **OPEN:** MVE-O-01. | Not run |
| EC-4 | The backlog items in section 3 are reviewed by the product owner (`BACKLOG-NW-001` is draft). | Open |
| EC-5 | The release approver is named. **OPEN:** O-09, owner Marc Dubois. | Open |
| EC-6 | The release counts, windows and placements are confirmed. **OPEN:** O-25, owners Lena Varga and Marc Dubois. | Open |

`EA-01` to `EA-03` and `EA-11` can start on entry without waiting for MVE-01 (gate none). `EA-05` and `EA-09` wait for the MVE-01 **decision** only, which is a gate and not another track.

### 7.2 Exit criteria (all testable, local validation only)

The release is ready for approval when every row passes. Each row names the story criteria (`<item id>/AC<n>`, Given / When / Then in the backlog) that prove it.

| Id | Exit criterion | Proven by |
|---|---|---|
| XC-1 | `az bicep build` run locally on the `main.bicep` of `tst` and of `prd` finishes with no error, each with a matching `.bicepparam` file, and nothing is applied to a subscription. | `EA-01/AC1`, `EA-11/AC1`, `EA-11/AC2`, `STORY-101/AC2`, `STORY-105/AC1`, `STORY-105/AC2` |
| XC-2 | Every resource name follows `<resource-abbreviation>-nw-<workload>-<environment>-<region>` and carries the tags `workload`, `environment`, `owner`, `costCenter`. A name or tag break stops approval. | `EA-01/AC2`, `EA-01/AC3`, `STORY-101/AC1`, `STORY-101/AC3` |
| XC-3 | Every resource is listed with its region; each is in France Central, or a secondary region in the EU. A resource outside the EU stops approval. | `STORY-104/AC1`, `STORY-104/AC2`, `STORY-104/AC3` (`NFR-03`) |
| XC-4 | A scan of source and configuration files finds no password, key or connection string with a password; applications use the managed secret store and managed identities; data services use private endpoints. | `STORY-103/AC1`, `STORY-103/AC2`, `STORY-103/AC3`, `EA-03/AC1`, `EA-03/AC2`, `EA-03/AC3` (`NFR-05`) |
| XC-5 | The pipeline definition has no step that applies anything to a subscription, and every deploy stage is marked as needing human approval. | `EA-11/AC3`, `STORY-105/AC3` |
| XC-6 | The connection design covers two periods (during the move and after the lease) and keeps the nightly 02:00 StockPilot exchange reachable in both. Each path that depends on O-15 is marked **OPEN:** with an owner and does not block the release. | `EA-02/AC1`, `EA-02/AC2`, `STORY-102/AC1`, `STORY-102/AC2`, `STORY-102/AC3` |
| XC-7 | The MVE-01 result (go, adjust or stop) is recorded before `EA-05` and `EA-09` are committed, with the check against `M1a`, `M1b` and `M1c`. | `EA-05/AC1`, `EA-05/AC2`, `EA-05/AC3` |
| XC-8 | A written data-tier decision names the chosen tier, states that PaaS is preferred and a virtual machine the fallback (A-21), introduces no Kubernetes, and says how the old servers leave support. | `STORY-120/AC1`, `STORY-120/AC2`, `STORY-120/AC3`, `STORY-120/AC4` |
| XC-9 | The cost model covers Order Desk, the portal and the Order Desk API host in production and one test environment, shows the monthly total, the EUR 1,500 cap and the headroom, and labels every price as dated and indicative. | `EA-09/AC1`, `EA-09/AC2`, `EA-09/AC3`, `STORY-121/AC1`, `STORY-121/AC2`, `STORY-121/AC3` (C-04) |
| XC-10 | The migration approach states steps, expected downtime and fallback for the 48 GB database and the 120 GB of invoice files; if the steps exceed Sunday 06:00 to 12:00 CET, it is split across Sundays or has a fallback. The claim that a log-based restore fits the window stays marked **ASSUMPTION:** A-33. | `STORY-122/AC1`, `STORY-122/AC2`, `STORY-122/AC3` |
| XC-11 | Every item in section 3 has a source cite, the tags `track-azure` and `azure-r1`, and every unanswered question in it is **OPEN:** with an owner. | `docs/product/backlog.md` section 2.1 and section 4.1 |
| XC-12 | No document or file in the release claims that anything was deployed, applied or created in a tenant or subscription, and holds no secret. | ES-27, ES-17 |

## 8. ASSUMPTION and OPEN items for this release

Ids are those of the PRD and backlog registers and keep their numbers (full wording and owners: `docs/product/backlog.md` section 7, the register of record). `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

### 8.1 ASSUMPTION items

| Id | ASSUMPTION | Confirming owner |
|---|---|---|
| A-01 | Build starts December 2026 after approval; release approval dates are targets. | Marc Dubois |
| A-02 | .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. | Ahmed Benali |
| A-06 | Prioritisation is MoSCoW from the business case, then date and dependency risk. NFRs are Must. | Lena Varga |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | Ahmed Benali |
| A-21 | A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | Ahmed Benali |
| A-32 | Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Ahmed Benali |
| A-35 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | Lena Varga |
| A-38 | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-40 | Enabler id families `EN-`, `EA-`, `EP-` and hundreds blocks per track for `EPIC-`, `FEAT-`, `STORY-` and `FR-`. | Lena Varga |
| A-42 | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-45 | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | Backlog rank: enablers before the stories that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-49 | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must (A-06). An enabler that serves only another track's requirements is Should (so `EN-14` and `FR-240` are Should). | Lena Varga |
| A-54 | Measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. | Ahmed Benali, Lena Varga |
| A-58 | The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). | Marc Dubois |
| A-59 | `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. | Ahmed Benali |
| MVE-A-01 | The effort (about 4 person-days each) and elapsed times are planning estimates; the inputs give no sizing basis. | Ahmed Benali |
| MVE-A-03 | Growth stays linear. From mid-November 2026 to 30 June 2027 is 7 to 7.5 months, so the database reaches about 56 GB (48 GB plus 7.5 months at 1 GB) and invoices about 135 GB (120 GB plus 7.5 months at 2 GB). The month count is itself an assumption. | Ahmed Benali |
| MVE-A-04 | A local SQL Server (Developer edition or container) is available to run the database scripts. | Ahmed Benali |

### 8.2 OPEN items

| Id | **OPEN:** | Who can answer |
|---|---|---|
| O-03 | Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-06 | Which backlog tool and which ES-28 prefix? Item types and fields in the tool are not validated. | Lena Varga |
| O-09 | Who is the named release approver for the Azure track? | Marc Dubois |
| O-10 | Which identity provider do customer users use (OQ-01)? | Ahmed Benali |
| O-15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-19 | Which build and deployment pipeline tool? | Ahmed Benali |
| O-21 | Approval and funding to build. | Marc Dubois |
| O-24 | What does the customer identity service cost, and does it count toward C-04? | Ahmed Benali |
| O-25 | Confirm the release counts, windows and the three placement changes. | Lena Varga, Marc Dubois |
| MVE-O-01 | Name the engineer who runs MVE-01. | Ahmed Benali |
| AZ1-O1 | **OPEN (this file):** the hosting runtime choice (rehost the unchanged application on a Windows virtual machine, or wait for `net10.0`) is not made. `EA-15` in `azure-r2` defines the hosting and names the runtime it describes. Confirm the runtime before `EA-15` is committed (O-03, A-20). | Ahmed Benali (O-03), Lena Varga (commitment) |
| AZ1-O2 | **OPEN (this file):** if MVE-01 ends in **stop**, does the product owner approve `azure-r1` without `EA-05`, `EA-09` and their stories, or hold the release? Items do not move. | Lena Varga, Marc Dubois |

Ids `AZ1-O1` and `AZ1-O2` are local to this file. This file is their register; they are not in the backlog register.

### 8.3 Inconsistency note

* **IN-1 (resolved).** The canonical release table lists "hosting runtime" as left out of `azure-r1`. At first no backlog item designed it. `EA-15` (`azure-r2`) now does, and `EA-16` (`azure-r3`) designs the database migration (A-59). Neither is in this release.

## 9. Publication note (ES-39)

Nothing has been published to any tracker (O-06 names no tool; `tracker_published: false`). When the backlog is published, the track tag and the release tag travel with every item in section 3 so that the release stays identifiable in the tool.

| Tool | How `track-azure` and `azure-r1` appear |
|---|---|
| **Azure DevOps** | Work-item tags `track-azure` and `azure-r1` on every item in section 3. |
| **GitHub** | Issue labels `track-azure` and `azure-r1`, plus one milestone named `azure-r1`. |
| **Jira** | Labels `track-azure` and `azure-r1`, plus one fix version named `azure-r1`. |

In every tool, titles, descriptions and source identifiers follow ES-28 and ES-29: the published title is `<id> <title>` with the participant prefix (**OPEN:** O-06), and each description links back to its `BR-`, `NFR-` and other source ids.

## 10. Where this release sits in the Azure track

| Release | Theme | Window | Items | Git tag (planned text, not created) |
|---|---|---|---|---|
| `azure-r1` (this file) | Foundation, data platform decision and cost proof | 1 Dec 2026 to 29 Jan 2027 | 21 | `product/azure-r1` |
| [`azure-r2`](azure-r2.md) | Pilot environment, exchange and storage, observability | 1 Feb to 31 Mar 2027 | 20 | `product/azure-r2` |
| [`azure-r3`](azure-r3.md) | Cutover and recovery proof | 1 Apr to 27 June 2027 (A-58) | 13 | `product/azure-r3` |

Within the Azure track, later items depend on earlier ones (for example `EA-05` feeds `EA-06`, `EA-08` and `EA-13`). That is the order of one team's own work, not a wait for another track.

## 11. Approval and tagging procedure

Nothing in this procedure is carried out by this document. Nothing is deployed to Azure (ES-27).

1. **Review.** The approver reviews section 3 (items), section 4 (identifiers) and section 7.2 (exit criteria) against the backlog and the local validation results.
2. **Confirm the approver.** **OPEN:** O-09. Until Marc Dubois names the approver, the product owner (Lena Varga, A-38) is the proposed approver and Marc Dubois the escalation.
3. **Record the approval** in the block below: name, date and decision.
4. **Commit.** After approval, the commit that holds this release file and the release content is made by a human (A-39).
5. **Tag.** Only then, tag that commit `product/azure-r1` (ES-31). **Do not create the tag before approval.**
6. **Publish (optional, later).** Apply section 9 when the backlog is published.

### Approval block

| Field | Value |
|---|---|
| Release | `azure-r1` |
| Track tag / release tag | `track-azure` / `azure-r1` |
| Planned Git tag | `product/azure-r1` — **to be created after approval; not created** |
| Approver | **OPEN:** O-09 (proposed: Lena Varga, A-38; escalation Marc Dubois) |
| Decision | ☐ Approved  ☐ Approved with changes  ☐ Not approved |
| Approval date | _(blank)_ |
| Commit id that holds the release | _(blank until approved and committed)_ |
| Git tag created on | _(blank, not created)_ |

<!-- end of azure-r1 -->
