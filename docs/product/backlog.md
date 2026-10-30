# Northwind Traders — Backlog: Platform and data-centre exit (BA-01) and Ordering and customer self-service (BA-02)

| Field | Value |
|---|---|
| Document | Backlog, deliverable D4 |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`, releases `azure-r1` to `azure-r3`) and **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`, releases `dotnet-r1` to `dotnet-r4`). **BA-03** Delivery claims and credit notes is out of scope (section 1.3). |
| Product owner (proposed) | Lena Varga, Head of Customer Operations, owns the product backlog (A-29) |
| Builds on | `docs/product/business-requirements.md` (BRD, D1), `docs/product/product-requirements.md` (PRD, D2) and `docs/product/experiments.md` (D3). Feature IDs `FT-AZ-01` to `FT-AZ-11` and `FT-DN-01` to `FT-DN-25`, epics `EP-AZ-01` to `EP-AZ-03` and `EP-DN-01` to `EP-DN-07`, and enablers `EN-AZ-01` to `EN-AZ-14` and `EN-DN-01` to `EN-DN-15` are reused exactly as the PRD defines them (A-26). |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01 to ES-07, ES-13 to ES-31, ES-39). Findings from reading `src/` and `database/` are used only to explain risk and are marked **ASSUMPTION:** (A-22, A-23). |
| Boundary | This is a planning document. Nothing is published to Azure DevOps, GitHub or Jira (the tool is **OPEN:** OPEN-11). Nothing is deployed, committed or tagged in Git (ES-27). No code, database script or infrastructure file is changed. |

## 1. Purpose and how to read this document

### 1.1 Purpose

This backlog turns the product requirements into work a team can build. It is ordered by priority, per track. Each track is delivered by its own team and never waits for the other (ES-31). The backlog has four levels:

* **Epic** (`EP-`): a release theme. An epic belongs to exactly one release.
* **Feature** (`FT-`): a product capability inside an epic.
* **User story** (`US-`): one thing a user can do, written *As a ... I want ... so that ...* with *Given / When / Then* acceptance criteria (ES-05).
* **Enabler** (`EN-`): preparation work that must come before the features that use it. It is written in the same form as a story, has the type "Enabler", and names the features it enables (A-17).

Each story and enabler can be built by a developer who has not read the business case, from its own text. Where a story needs a fact from the business case or from the current system, the fact is written inside the story with its source. Acceptance criteria use *Given / When / Then*. Where a criterion states a rule that holds at all times, the "When" is the moment the rule is checked, for example "When I read it" or "When it is scanned".

### 1.2 Words used

* **BR-**, **NFR-**, **C-**, **SM-**, **P-**, **OQ-** are identifiers from the business case: business requirement, non-functional requirement (quality target), constraint, success measure, problem and open question. **CS-** are facts about today's system from `current-state.md`. **ES-** are engineering standards. **BA-** means business area.
* **MoSCoW** is the priority scale: **Must**, **Should**, **Could**. All BR items have a priority in the business case. The business case gives no priority for NFR items. They are treated as Must because each one gates a release that carries a Must outcome (A-12). A feature or enabler takes the priority of the requirement it serves.
* **Order Desk** is the internal web application that staff use to enter and manage orders. **Portal** is the new customer web site. **StockPilot** is the warehouse system in Antwerp. **SFTP** is a secure file-transfer service.
* **IaC** means infrastructure as code. **Bicep** is the language used for it. **`az bicep build`** is the local check that turns Bicep into a template and reports errors. Nothing is deployed (ES-27). **`tst`** is the test environment and **`prd`** the production environment (ES-23).
* **RPO** (recovery point objective) is how much data may be lost. **RTO** (recovery time objective) is how long recovery may take. **WCAG** is the Web Content Accessibility Guidelines. **ADR** is an architecture decision record: a short written decision with its options and reasons. **CET** is Central European Time.
* **ASSUMPTION:** marks anything not stated in `knowledge-docs`. All are in section 9, each with a person who can confirm it (ES-03). **OPEN:** marks an unanswered question. All are in section 10, each with the person who can answer (ES-04). Neither is a requirement.
* Every item cites its source in the form `(source: BR-05, CS-10)` (ES-02).

### 1.3 Out of scope

**BA-03 Delivery claims and credit notes (`track-power-platform`)** is out of scope: BR-14 to BR-19, NFR-09, C-07, C-08, SM-05, SM-06, OQ-04, OQ-05, CS-24 to CS-28 and ES-32 to ES-37. No story here covers them. Business-case section 6 exclusions also stay out: online payment, a native mobile app, changes to StockPilot, replacing the finance system, and customers recording claims themselves. **OPEN:** OPEN-24 (informational): BA-03 will need an Order Desk programming interface. No release depends on it. No story is written for it, and `FT-DN-25` is a feature without stories.

### 1.4 Ordering rules

1. Within a track, items are ranked by release, then Must before Should before Could, then enablers before the features that need them (ES-31).
2. Rank never depends on the other track. A dependency on the other track is written as an **OPEN:** item with what the item does without the answer (A-28). No item says "requires", "blocked by" or "waits for" for another track.
3. "Depends on" lines name items **of the same track** only.
4. Inside a release, the product owner may change the order without changing any tag (A-43).

## 2. Tag convention and how the tags are published

### 2.1 Tag convention (ES-30, ES-31)

Every item starts its description with a **Tags** line, for example `Tags: track-azure, azure-r2` (planned) or `Tags: track-dotnet` (not planned).

| Rule | Detail |
|---|---|
| One track tag | Every epic, feature, story and enabler carries exactly one of `track-azure` or `track-dotnet`. `track-power-platform` is not used as an item tag. |
| One release tag when planned | A planned item carries exactly one release tag of the **same** track: `azure-r1`, `azure-r2` or `azure-r3` for `track-azure`; `dotnet-r1`, `dotnet-r2`, `dotnet-r3` or `dotnet-r4` for `track-dotnet`. |
| Unplanned items | An unplanned item carries only the track tag. Its parent is also unplanned. |
| Parent and child | A parent and its children share the same track and release. Epics are release-scoped, so a parent never spans releases. |
| Two tracks needed | A story that needs two tracks is split into one story per track (ES-30). NFR-03, NFR-04 and NFR-05 are handled this way (section 5.3, A-02). |
| Required fields | ID, title, Tags, Type (Epic, Feature, Story, Enabler), Priority, source IDs, status (`Draft`). Stories and enablers add *As a ... I want ... so that ...* and *Given / When / Then* criteria. Enablers name what they enable. |

### 2.2 How the tags travel when the backlog is published (description only)

The tool is **OPEN:** OPEN-11. Nothing is published now. In every tool, the track and release tags travel with every item, and each release stays identifiable (ES-39). Titles start with the item ID. Descriptions hold the source identifiers as links back to the business documents (ES-29).

| Tool | Track and release tags | Release grouping | Extra rules (ES-28, ES-29) |
|---|---|---|---|
| Azure DevOps | Work-item **tags**: for example `track-azure` and `azure-r1` on one item | The release tag is the grouping. A query on the tag lists a release. | Add the tag `nw-workshop` and the participant prefix agreed with the facilitator (ES-28). Put the `(source: ...)` identifiers in the description (ES-29). Epic, Feature and User Story work-item types hold the epic, feature and story or enabler. |
| GitHub | Issue **labels**: `track-azure`, `azure-r1` | **One milestone per release**, named after it (`azure-r1`) | Source identifiers in the issue body. Parent and child through sub-issues. |
| Jira | **Labels**: `track-azure`, `azure-r1` | **One fix version per release**, named after it (`azure-r1`) | Source identifiers in the description. Parent and child through the epic link or parent field. |

No extra tag is added for the item type. An enabler is published as a story whose title starts with its `EN-` ID. Unplanned items get the track label or tag only, and no milestone or fix version.

## 3. Backlog overview

### 3.1 Counts

| Track | Release | Epics | Features | Enablers | Stories | Total items |
|---|---|---|---|---|---|---|
| `track-azure` | `azure-r1` | 1 | 4 | 7 | 5 | 17 |
| `track-azure` | `azure-r2` | 1 | 5 | 7 | 9 | 22 |
| `track-azure` | `azure-r3` | 1 | 2 | 0 | 5 | 8 |
| **`track-azure` total** | | **3** | **11** | **14** | **19** | **47** |
| `track-dotnet` | `dotnet-r1` | 1 | 4 | 8 | 2 | 15 |
| `track-dotnet` | `dotnet-r2` | 4 | 12 | 6 | 19 | 41 |
| `track-dotnet` | `dotnet-r3` | 1 | 3 | 0 | 6 | 10 |
| `track-dotnet` | `dotnet-r4` | 1 | 3 | 1 | 6 | 11 |
| `track-dotnet` | unplanned (track tag only) | 1 | 4 | 0 | 4 | 9 |
| **`track-dotnet` total** | | **8** | **26** | **15** | **37** | **86** |
| **Both tracks** | | **11** | **37** | **29** | **56** | **133** |

### 3.2 Epics and features (enablers and stories are in sections 6 and 7 and in the register in section 11)

Release `-` means unplanned. Priority of an epic is the highest priority of its children.

| ID | Type | Title | Track tag | Release tag | Priority | Sources |
|---|---|---|---|---|---|---|
| `EP-AZ-01` | Epic | Foundation and proof | `track-azure` | `azure-r1` | Must | C-01, C-03, C-04, NFR-01, NFR-03, NFR-05, CS-10 |
| `FT-AZ-01` | Feature | Azure foundation and network | `track-azure` | `azure-r1` | Must | C-01, NFR-03, CS-09, CS-19, ES-20, ES-22 to ES-25, ES-27 |
| `FT-AZ-02` | Feature | Hosting and data decision with a cost model | `track-azure` | `azure-r1` | Must | C-02, C-04, C-06, ES-21 |
| `FT-AZ-03` | Feature | Secrets and monitoring baseline on `tst` | `track-azure` | `azure-r1` | Must | NFR-05, NFR-01, CS-22, ES-17, ES-25, ES-26 |
| `FT-AZ-04` | Feature | StockPilot exchange proof | `track-azure` | `azure-r1` | Must | CS-10, C-03 |
| `EP-AZ-02` | Epic | Production cutover | `track-azure` | `azure-r2` | Must | BR-13, C-01, C-03, NFR-01, NFR-03, NFR-05, NFR-06 |
| `FT-AZ-05` | Feature | Production environment and Antwerp connection | `track-azure` | `azure-r2` | Must | BR-13, NFR-01, NFR-03, NFR-05, CS-09, CS-10 |
| `FT-AZ-06` | Feature | Backup, disaster recovery and tested restore | `track-azure` | `azure-r2` | Must | NFR-06, CS-07, CS-23 |
| `FT-AZ-07` | Feature | Data move: database and invoice files | `track-azure` | `azure-r2` | Must | BR-13, CS-07, CS-08, CS-11, CS-21 |
| `FT-AZ-08` | Feature | Nightly exchange and mail relay in Azure | `track-azure` | `azure-r2` | Must | CS-10, CS-12, C-03 |
| `FT-AZ-09` | Feature | Sunday-window cutover and rollback | `track-azure` | `azure-r2` | Must | BR-13, CS-21, C-01 |
| `EP-AZ-03` | Epic | Stabilise and decommission | `track-azure` | `azure-r3` | Must | SM-07, C-04, NFR-06 |
| `FT-AZ-10` | Feature | Retire the old servers | `track-azure` | `azure-r3` | Must | SM-07, C-01, C-02, CS-06, CS-07 |
| `FT-AZ-11` | Feature | Closing cost check, recovery test report and runbooks | `track-azure` | `azure-r3` | Must | C-04, NFR-06, CS-23, ES-09 |
| `EP-DN-01` | Epic | Modernised Order Desk | `track-dotnet` | `dotnet-r1` | Must | BR-10, NFR-05, CS-01, CS-02, CS-13 to CS-20, ES-13 to ES-19 |
| `FT-DN-01` | Feature | Current platform and safety net | `track-dotnet` | `dotnet-r1` | Must | CS-01, CS-02, CS-18, CS-19, CS-20, ES-13, ES-14, ES-18, ES-19 |
| `FT-DN-02` | Feature | Configuration, logging and no secrets | `track-dotnet` | `dotnet-r1` | Must | NFR-05, CS-13, CS-15, CS-17, ES-15, ES-16, ES-17 |
| `FT-DN-03` | Feature | Draft order and invoice storage free of one server | `track-dotnet` | `dotnet-r1` | Must | CS-14, CS-16 |
| `FT-DN-04` | Feature | Staff see the order channel | `track-dotnet` | `dotnet-r1` | Must | BR-10, CS-03 |
| `EP-DN-02` | Epic | Secure access and tenant isolation | `track-dotnet` | `dotnet-r2` | Must | BR-01, NFR-03, NFR-04, C-05, OQ-01 |
| `FT-DN-05` | Feature | Portal architecture decision | `track-dotnet` | `dotnet-r2` | Must | OQ-01, NFR-04, ES-13 |
| `FT-DN-06` | Feature | Customer data separation | `track-dotnet` | `dotnet-r2` | Must | BR-01, C-05 |
| `FT-DN-07` | Feature | Customer and staff sign-in | `track-dotnet` | `dotnet-r2` | Must | BR-01, NFR-04, CS-04, OQ-01 |
| `FT-DN-08` | Feature | Portal data stays in the EU | `track-dotnet` | `dotnet-r2` | Must | NFR-03, ES-20 |
| `EP-DN-03` | Epic | See my orders | `track-dotnet` | `dotnet-r2` | Must | BR-02, BR-03, BR-04, BR-12, NFR-02 |
| `FT-DN-09` | Feature | See my orders | `track-dotnet` | `dotnet-r2` | Must | BR-02, NFR-02, CS-05 |
| `FT-DN-10` | Feature | Order detail with my prices | `track-dotnet` | `dotnet-r2` | Must | BR-03, BR-12, NFR-02, CS-20, ES-18 |
| `FT-DN-11` | Feature | Order status as of the 02:00 batch | `track-dotnet` | `dotnet-r2` | Must | BR-04, CS-10, C-03 |
| `EP-DN-04` | Epic | Reorder and hand-off | `track-dotnet` | `dotnet-r2` | Must | BR-05, BR-06, BR-10, BR-12, NFR-08, C-05 |
| `FT-DN-12` | Feature | Reorder by copying | `track-dotnet` | `dotnet-r2` | Must | BR-05, BR-12, P-04, CS-16 |
| `FT-DN-13` | Feature | Portal order reaches Order Desk | `track-dotnet` | `dotnet-r2` | Must | BR-06, BR-10, C-05 |
| `FT-DN-14` | Feature | Order change audit | `track-dotnet` | `dotnet-r2` | Must | NFR-08, CS-05 |
| `EP-DN-05` | Epic | Portal quality | `track-dotnet` | `dotnet-r2` | Must | NFR-07, BR-11 |
| `FT-DN-15` | Feature | Language foundation | `track-dotnet` | `dotnet-r2` | Should | BR-11 |
| `FT-DN-16` | Feature | Accessibility baseline | `track-dotnet` | `dotnet-r2` | Must | NFR-07, BR-03 |
| `EP-DN-06` | Epic | Self-service extras | `track-dotnet` | `dotnet-r3` | Should | BR-07, BR-08, BR-11 |
| `FT-DN-17` | Feature | Invoice download | `track-dotnet` | `dotnet-r3` | Should | BR-07, P-05, CS-08, CS-11, CS-14 |
| `FT-DN-18` | Feature | Customer administrator | `track-dotnet` | `dotnet-r3` | Should | BR-08, OQ-03 |
| `FT-DN-19` | Feature | French and English | `track-dotnet` | `dotnet-r3` | Should | BR-11, OQ-02 |
| `EP-DN-07` | Epic | Notifications and measures | `track-dotnet` | `dotnet-r4` | Could | BR-09, SM-01, SM-02, SM-03, SM-04 |
| `FT-DN-20` | Feature | Keep shipment date and carrier | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10 |
| `FT-DN-21` | Feature | Shipped e-mail | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10, CS-12 |
| `FT-DN-22` | Feature | Measure the success measures | `track-dotnet` | `dotnet-r4` | Could | SM-01, SM-02, SM-03, SM-04 |
| `EP-DN-08` | Epic | Unplanned candidates (not in a release) | `track-dotnet` | - | Should (provisional, A-36) | BR-11, NFR-08, BR-04 |
| `FT-DN-23` | Feature | Dutch language | `track-dotnet` | - | Should (provisional, A-36) | BR-11, OQ-02 |
| `FT-DN-24` | Feature | Field-level order audit | `track-dotnet` | - | Could (provisional, A-36) | NFR-08 |
| `FT-DN-25` | Feature | Order Desk API for reuse | `track-dotnet` | - | Could (provisional, A-36) | none in knowledge-docs in scope; OPEN-24, informational |
| `FT-DN-26` | Feature | Status clarity options (only if `MVE-BA02` says pivot) | `track-dotnet` | - | Should (provisional, A-36) | BR-04, CS-10, SM-02 |

## 4. Ranked order per track

The number is the proposed build order inside the track (A-43). Epics and features are not ranked separately: a feature takes the rank of its first item. "Depends on" names items of the same track only. Cross-track questions are **OPEN:** items in each item's text.

### 4.1 `track-azure`

| Rank | ID | Type | Title | Release tag | Priority | Feature | Depends on (same track) |
|---|---|---|---|---|---|---|---|
| 1 | `US-AZ-001` | Story | Prove the nightly order file is identical | `azure-r1` | Must | `FT-AZ-04` | none |
| 2 | `US-AZ-002` | Story | Prove the shipment file gives the same result | `azure-r1` | Must | `FT-AZ-04` | none |
| 3 | `US-AZ-003` | Story | Confirm the Antwerp file-transfer details in writing | `azure-r1` | Must | `FT-AZ-04` | none |
| 4 | `US-AZ-004` | Story | Record which server features the proof needed | `azure-r1` | Must | `FT-AZ-04` | `US-AZ-001`, `US-AZ-002` |
| 5 | `US-AZ-005` | Story | Record the `MVE-BA01` outcome and its effect | `azure-r1` | Must | `FT-AZ-04` | `US-AZ-001` to `US-AZ-004` |
| 6 | `EN-AZ-01` | Enabler | Azure foundation: region, names, tags, Bicep, `tst` and `prd` | `azure-r1` | Must | `FT-AZ-01` | none |
| 7 | `EN-AZ-02` | Enabler | Network foundation and private endpoints | `azure-r1` | Must | `FT-AZ-01` | `EN-AZ-01` |
| 8 | `EN-AZ-07` | Enabler | Infrastructure pipeline | `azure-r1` | Must | `FT-AZ-01` | `EN-AZ-01` |
| 9 | `EN-AZ-03` | Enabler | Hosting and data decision record | `azure-r1` | Must | `FT-AZ-02` | `US-AZ-004`, `US-AZ-005` |
| 10 | `EN-AZ-12` | Enabler | Cost model | `azure-r1` | Must | `FT-AZ-02` | `EN-AZ-03` |
| 11 | `EN-AZ-04` | Enabler | Secrets and managed identity on `tst` | `azure-r1` | Must | `FT-AZ-03` | `EN-AZ-02`, `EN-AZ-03`, `EN-AZ-07` |
| 12 | `EN-AZ-05` | Enabler | Observability baseline on `tst` | `azure-r1` | Must | `FT-AZ-03` | `EN-AZ-01`, `EN-AZ-02` |
| 13 | `EN-AZ-14` | Enabler | Hybrid connectivity to Antwerp | `azure-r2` | Must | `FT-AZ-05` | `EN-AZ-02`, `EN-AZ-03` |
| 14 | `US-AZ-006` | Story | No secrets in production | `azure-r2` | Must | `FT-AZ-05` | `EN-AZ-04` |
| 15 | `US-AZ-007` | Story | Production monitoring and availability probe | `azure-r2` | Must | `FT-AZ-05` | `EN-AZ-05` |
| 16 | `US-AZ-008` | Story | Production data, backups and logs stay in the EU | `azure-r2` | Must | `FT-AZ-05` | `EN-AZ-01` |
| 17 | `EN-AZ-06` | Enabler | Backup, disaster recovery and restore method | `azure-r2` | Must | `FT-AZ-06` | `EN-AZ-03` |
| 18 | `EN-AZ-08` | Enabler | Database migration method and rehearsal | `azure-r2` | Must | `FT-AZ-07` | `EN-AZ-03`, `EN-AZ-06` |
| 19 | `EN-AZ-10` | Enabler | Invoice store migration | `azure-r2` | Must | `FT-AZ-07` | `EN-AZ-02`, `EN-AZ-03` |
| 20 | `EN-AZ-09` | Enabler | StockPilot exchange redesign | `azure-r2` | Must | `FT-AZ-08` | `US-AZ-005`, `EN-AZ-03`, `EN-AZ-14` |
| 21 | `EN-AZ-11` | Enabler | SMTP relay replacement | `azure-r2` | Must | `FT-AZ-08` | `EN-AZ-02` |
| 22 | `US-AZ-009` | Story | Tested restore meets RPO and RTO | `azure-r2` | Must | `FT-AZ-06` | `EN-AZ-06`, `EN-AZ-08` |
| 23 | `US-AZ-010` | Story | Order data is identical after the move | `azure-r2` | Must | `FT-AZ-07` | `EN-AZ-08` |
| 24 | `US-AZ-011` | Story | Invoice PDFs are available in Azure | `azure-r2` | Must | `FT-AZ-07` | `EN-AZ-10` |
| 25 | `US-AZ-012` | Story | The nightly exchange runs from Azure | `azure-r2` | Must | `FT-AZ-08` | `EN-AZ-09`, `EN-AZ-14` |
| 26 | `EN-AZ-13` | Enabler | Cutover runbook and rollback plan | `azure-r2` | Must | `FT-AZ-09` | `EN-AZ-08`, `EN-AZ-09`, `EN-AZ-10`, `EN-AZ-11`, `EN-AZ-14`, `US-AZ-009` |
| 27 | `US-AZ-013` | Story | Rehearse the cutover and rollback in the Sunday window | `azure-r2` | Must | `FT-AZ-09` | `EN-AZ-13`, `US-AZ-010`, `US-AZ-011`, `US-AZ-012` |
| 28 | `US-AZ-014` | Story | Cut over production inside the Sunday window | `azure-r2` | Must | `FT-AZ-09` | `US-AZ-013`, `US-AZ-006`, `US-AZ-007`, `US-AZ-008` |
| 29 | `US-AZ-018` | Story | Recovery test and report on production | `azure-r3` | Must | `FT-AZ-11` | `US-AZ-014` |
| 30 | `US-AZ-017` | Story | Closing cost check against the ceiling | `azure-r3` | Must | `FT-AZ-11` | `US-AZ-014` |
| 31 | `US-AZ-019` | Story | Runbooks the IT team can follow | `azure-r3` | Must | `FT-AZ-11` | `US-AZ-014` |
| 32 | `US-AZ-015` | Story | Retire the old web and database servers | `azure-r3` | Must | `FT-AZ-10` | `US-AZ-014`, `US-AZ-018` |
| 33 | `US-AZ-016` | Story | Decide whether the file server counts and report SM-07 | `azure-r3` | Must | `FT-AZ-10` | `US-AZ-011`, `US-AZ-015` |

Why this order. The StockPilot proof (`FT-AZ-04`) is the riskiest assumption and the cheapest to test, so it is first. Its result feeds the hosting decision (`EN-AZ-03`) and the cost model (`EN-AZ-12`). The foundation, network and pipeline come next, then secrets and monitoring. In `azure-r2`, connectivity, backup and the data move come before the exchange build and the cutover rehearsal. Decommissioning is last because it removes the rollback path (source: C-03, CS-10, C-01, SM-07, R-02).

### 4.2 `track-dotnet`

| Rank | ID | Type | Title | Release tag | Priority | Feature | Depends on (same track) |
|---|---|---|---|---|---|---|---|
| 1 | `EN-DN-01` | Enabler | SDK-style projects on `net10.0` | `dotnet-r1` | Must | `FT-DN-01` | none |
| 2 | `EN-DN-02` | Enabler | Tests pass on Windows, macOS and Linux | `dotnet-r1` | Must | `FT-DN-01` | `EN-DN-01` |
| 3 | `EN-DN-09` | Enabler | Build and test pipeline | `dotnet-r1` | Must | `FT-DN-01` | `EN-DN-02` |
| 4 | `EN-DN-03` | Enabler | Configuration through options | `dotnet-r1` | Must | `FT-DN-02` | `EN-DN-01` |
| 5 | `EN-DN-04` | Enabler | Logging through `ILogger<T>` | `dotnet-r1` | Must | `FT-DN-02` | `EN-DN-01` |
| 6 | `EN-DN-05` | Enabler | No secrets and no Windows-sign-in database connection | `dotnet-r1` | Must | `FT-DN-02` | `EN-DN-03` |
| 7 | `EN-DN-06` | Enabler | Draft order kept outside one server's memory | `dotnet-r1` | Must | `FT-DN-03` | `EN-DN-01` |
| 8 | `EN-DN-07` | Enabler | Invoice storage setting instead of a fixed network path | `dotnet-r1` | Must | `FT-DN-03` | `EN-DN-03` |
| 9 | `US-DN-001` | Story | Staff see the order channel | `dotnet-r1` | Must | `FT-DN-04` | `EN-DN-01` |
| 10 | `US-DN-002` | Story | Staff filter orders by channel | `dotnet-r1` | Must | `FT-DN-04` | `US-DN-001` |
| 11 | `EN-DN-11` | Enabler | Portal architecture and sign-in decision record | `dotnet-r2` | Must | `FT-DN-05` | `EN-DN-01` |
| 12 | `EN-DN-10` | Enabler | Customer data separation (tenant isolation) | `dotnet-r2` | Must | `FT-DN-06` | `EN-DN-11` |
| 13 | `EN-DN-08` | Enabler | Staff sign-in with Microsoft Entra ID | `dotnet-r2` | Must | `FT-DN-07` | `EN-DN-11`, `EN-DN-01` |
| 14 | `US-DN-004` | Story | Customer user signs in | `dotnet-r2` | Must | `FT-DN-07` | `EN-DN-11`, `EN-DN-10` |
| 15 | `US-DN-003` | Story | Customer user sees only their own company | `dotnet-r2` | Must | `FT-DN-06` | `EN-DN-10`, `US-DN-004` |
| 16 | `US-DN-005` | Story | Portal sign-in, mail and monitoring keep data in the EU | `dotnet-r2` | Must | `FT-DN-08` | `EN-DN-11`, `EN-DN-10` |
| 17 | `EN-DN-14` | Enabler | Accessibility baseline (WCAG 2.2 AA) | `dotnet-r2` | Must | `FT-DN-16` | `EN-DN-01` |
| 18 | `US-DN-006` | Story | See my company's orders from the last 24 months | `dotnet-r2` | Must | `FT-DN-09` | `EN-DN-10`, `EN-DN-14`, `US-DN-004` |
| 19 | `US-DN-007` | Story | The order list responds in under 2 seconds | `dotnet-r2` | Must | `FT-DN-09` | `US-DN-006`, `EN-DN-10` |
| 20 | `US-DN-008` | Story | Open an order and see its details | `dotnet-r2` | Must | `FT-DN-10` | `EN-DN-10`, `EN-DN-14`, `US-DN-006` |
| 21 | `US-DN-009` | Story | See my negotiated prices on an order | `dotnet-r2` | Must | `FT-DN-10` | `US-DN-008`, `EN-DN-10` |
| 22 | `US-DN-010` | Story | The order detail responds in under 2 seconds | `dotnet-r2` | Must | `FT-DN-10` | `US-DN-008`, `EN-DN-10` |
| 23 | `US-DN-011` | Story | See one of six statuses on an order | `dotnet-r2` | Must | `FT-DN-11` | `US-DN-008`, `EN-DN-10` |
| 24 | `US-DN-012` | Story | Understand how fresh the status is | `dotnet-r2` | Must | `FT-DN-11` | `US-DN-011`, `EN-DN-10` |
| 25 | `US-DN-013` | Story | Start a new order by copying a previous order | `dotnet-r2` | Must | `FT-DN-12` | `EN-DN-06`, `US-DN-008`, `EN-DN-10` |
| 26 | `US-DN-014` | Story | Change quantities and remove lines before submitting | `dotnet-r2` | Must | `FT-DN-12` | `US-DN-013`, `EN-DN-10` |
| 27 | `US-DN-015` | Story | See my prices on the draft order | `dotnet-r2` | Must | `FT-DN-12` | `US-DN-014`, `US-DN-009`, `EN-DN-10` |
| 28 | `EN-DN-13` | Enabler | Audit completeness | `dotnet-r2` | Must | `FT-DN-14` | `EN-DN-01` |
| 29 | `US-DN-016` | Story | Submit the order and see it in Order Desk as Received | `dotnet-r2` | Must | `FT-DN-13` | `US-DN-014`, `EN-DN-13`, `EN-DN-10` |
| 30 | `US-DN-017` | Story | The server marks portal orders with the Portal channel | `dotnet-r2` | Must | `FT-DN-13` | `US-DN-016`, `US-DN-001`, `EN-DN-10` |
| 31 | `US-DN-018` | Story | Every order change records who, what, when and channel | `dotnet-r2` | Must | `FT-DN-14` | `EN-DN-13`, `US-DN-016`, `EN-DN-10` |
| 32 | `US-DN-019` | Story | Audit records are kept for 7 years | `dotnet-r2` | Must | `FT-DN-14` | `EN-DN-13`, `EN-DN-10` |
| 33 | `US-DN-020` | Story | Use the portal with keyboard and screen reader | `dotnet-r2` | Must | `FT-DN-16` | `US-DN-006`, `US-DN-008`, `US-DN-014`, `EN-DN-10` |
| 34 | `US-DN-021` | Story | Read the portal with enough contrast, zoom and clear errors | `dotnet-r2` | Must | `FT-DN-16` | `US-DN-020`, `EN-DN-10` |
| 35 | `EN-DN-12` | Enabler | Localisation scaffold | `dotnet-r2` | Should | `FT-DN-15` | `EN-DN-01` |
| 36 | `US-DN-022` | Story | Download the PDF invoice of a delivered order | `dotnet-r3` | Should | `FT-DN-17` | `EN-DN-07`, `EN-DN-10`, `US-DN-008` |
| 37 | `US-DN-023` | Story | Clear message when an invoice is not available | `dotnet-r3` | Should | `FT-DN-17` | `US-DN-022`, `EN-DN-10` |
| 38 | `US-DN-024` | Story | Customer administrator invites a user | `dotnet-r3` | Should | `FT-DN-18` | `US-DN-004`, `EN-DN-10` |
| 39 | `US-DN-025` | Story | Customer administrator removes a user | `dotnet-r3` | Should | `FT-DN-18` | `US-DN-024`, `EN-DN-10` |
| 40 | `US-DN-026` | Story | Use the portal in French or English | `dotnet-r3` | Should | `FT-DN-19` | `EN-DN-12`, `EN-DN-10` |
| 41 | `US-DN-027` | Story | The portal remembers my language | `dotnet-r3` | Should | `FT-DN-19` | `US-DN-026`, `EN-DN-10` |
| 42 | `EN-DN-15` | Enabler | Store shipment date and carrier | `dotnet-r4` | Could | `FT-DN-20` | `EN-DN-01` |
| 43 | `US-DN-028` | Story | Receive an e-mail when my order is shipped | `dotnet-r4` | Could | `FT-DN-21` | `EN-DN-15`, `US-DN-011`, `EN-DN-10` |
| 44 | `US-DN-029` | Story | The shipped e-mail is sent once and only to my company | `dotnet-r4` | Could | `FT-DN-21` | `US-DN-028`, `EN-DN-10` |
| 45 | `US-DN-030` | Story | Measure SM-01: share of orders placed through the portal | `dotnet-r4` | Could | `FT-DN-22` | `US-DN-017`, `EN-DN-10` |
| 46 | `US-DN-031` | Story | Measure SM-02: "where is my order?" calls per week | `dotnet-r4` | Could | `FT-DN-22` | `US-DN-011`, `EN-DN-10` |
| 47 | `US-DN-032` | Story | Measure SM-03: order lines needing correction | `dotnet-r4` | Could | `FT-DN-22` | `US-DN-016`, `EN-DN-10` |
| 48 | `US-DN-033` | Story | Measure SM-04: invoice copy requests handled by staff | `dotnet-r4` | Could | `FT-DN-22` | `US-DN-022`, `EN-DN-10` |
| - | `US-DN-034` | Story | Use the portal in Dutch (unplanned) | none | Should (provisional) | `FT-DN-23` | `EN-DN-12`, `US-DN-026`, `EN-DN-10` |
| - | `US-DN-035` | Story | See which field changed in an order (unplanned) | none | Could (provisional) | `FT-DN-24` | `US-DN-018`, `EN-DN-10` |
| - | `US-DN-036` | Story | See when each status last changed (unplanned) | none | Should (provisional) | `FT-DN-26` | `US-DN-011`, `EN-DN-10` |
| - | `US-DN-037` | Story | Read Picking and Shipped in plain words (unplanned) | none | Should (provisional) | `FT-DN-26` | `US-DN-011`, `EN-DN-10` |

Why this order. Nothing for customers can be built safely on .NET Framework 4.8 with tests that run only in Visual Studio, so `dotnet-r1` goes first (source: CS-01, CS-18, ES-14, ES-18). `EN-DN-10` (customer data separation) comes before every portal story that shows data, and each such story cites it (A-22). `EN-DN-14` (accessibility) comes before the pages it shapes. `EN-DN-12` (language scaffold) is a Should item and is ranked in its priority block. It is cheaper to build before more screens exist, so the product owner may pull it forward inside `dotnet-r2` without changing any tag (A-43, OPEN-27).

## 5. Requirement coverage check

### 5.1 Business requirements (BR-01 to BR-13)

| ID | Priority | Track | Covered by (items) | Release tag(s) |
|---|---|---|---|---|
| BR-01 | Must | .NET | `EN-DN-10`, `US-DN-003`, `US-DN-004` | `dotnet-r2` |
| BR-02 | Must | .NET | `US-DN-006` | `dotnet-r2` |
| BR-03 | Must | .NET | `US-DN-008`, `US-DN-020` | `dotnet-r2` |
| BR-04 | Must | .NET | `US-DN-011`, `US-DN-012` (options `US-DN-036`, `US-DN-037` unplanned) | `dotnet-r2` |
| BR-05 | Must | .NET | `US-DN-013`, `US-DN-014` | `dotnet-r2` |
| BR-06 | Must | .NET | `US-DN-016` | `dotnet-r2` |
| BR-07 | Should | .NET | `US-DN-022`, `US-DN-023` | `dotnet-r3` |
| BR-08 | Should | .NET | `US-DN-024`, `US-DN-025` | `dotnet-r3` |
| BR-09 | Could | .NET | `EN-DN-15`, `US-DN-028`, `US-DN-029` (partly covered until a mail path is named, OPEN-18) | `dotnet-r4` |
| BR-10 | Must | .NET | `US-DN-001`, `US-DN-002` (`dotnet-r1`); `US-DN-017`, `US-DN-018`, `EN-DN-13` (`dotnet-r2`); `US-DN-030` (`dotnet-r4`) | `dotnet-r1`, `dotnet-r2`, `dotnet-r4` |
| BR-11 | Should | .NET | `EN-DN-12` (`dotnet-r2`); `US-DN-026`, `US-DN-027` (`dotnet-r3`); Dutch `US-DN-034` unplanned (OPEN-14) | `dotnet-r2`, `dotnet-r3` |
| BR-12 | Must | .NET | `US-DN-009`, `US-DN-015` | `dotnet-r2` |
| BR-13 | Must | Azure | `EN-AZ-08`, `EN-AZ-13`, `US-AZ-010`, `US-AZ-011`, `US-AZ-013`, `US-AZ-014`; supporting (†): `EN-AZ-09`†, `EN-AZ-10`†, `EN-AZ-14`†, `US-AZ-012`† | `azure-r2` |

In sections 5.1, 5.2 and 5.4, a row lists the stories and enablers whose own `(source: ...)` line cites the ID. `†` marks a supporting item that is named for the requirement but whose own source line does not cite it. Features and epics that cite an ID are shown in the traceability table (`traceability.md`).

### 5.2 Non-functional requirements (NFR-01 to NFR-08)

| ID | Track | Covered by (items) | Release tag(s) |
|---|---|---|---|
| NFR-01 | Azure | `EN-AZ-05`, `US-AZ-007` | `azure-r1`, `azure-r2` |
| NFR-02 | .NET | `US-DN-007`, `US-DN-010` | `dotnet-r2` |
| NFR-03 | Azure and .NET | Azure: `EN-AZ-01`, `US-AZ-008`, `EN-AZ-06`, `EN-AZ-08`, `EN-AZ-11`. .NET: `US-DN-005`, `EN-DN-11`, `US-DN-029` | `azure-r1`, `azure-r2`, `dotnet-r2`, `dotnet-r4` |
| NFR-04 | .NET (Azure side OPEN-13) | .NET: `EN-DN-08`, `US-DN-004`, `EN-DN-11`, `US-DN-024`. Azure: no story, see note | `dotnet-r2`, `dotnet-r3` |
| NFR-05 | Azure and .NET | Azure: `EN-AZ-04`, `US-AZ-006`, `EN-AZ-07`, `US-AZ-003`, `EN-AZ-11`. .NET: `EN-DN-05`, `EN-DN-09` | `azure-r1`, `azure-r2`, `dotnet-r1` |
| NFR-06 | Azure | `EN-AZ-06`, `US-AZ-009`, `US-AZ-018` | `azure-r2`, `azure-r3` |
| NFR-07 | .NET | `EN-DN-14`, `US-DN-020`, `US-DN-021` | `dotnet-r2` |
| NFR-08 | .NET (Azure retention side OPEN-22) | `EN-DN-13`, `US-DN-018`, `US-DN-019` (field-level `US-DN-035` unplanned, OPEN-17) | `dotnet-r2` |

### 5.3 Notes on the cross-cutting split (ES-30, A-02)

* **NFR-05:** one primary story per track: `EN-AZ-04` (platform) and `EN-DN-05` (application). Follow-on `US-AZ-006` covers `prd`.
* **NFR-03:** one primary story per track: `EN-AZ-01` (regions, backups and logs) and `US-DN-005` (the portal's sign-in, mail and monitoring). Follow-on `US-AZ-008` covers `prd`.
* **NFR-04:** the .NET track carries customer sign-in (`US-DN-004`) and staff Entra sign-in (`EN-DN-08`). **OPEN:** An Azure story exists only if OPEN-03 or OPEN-13 gives platform sign-in plumbing to the Azure track. Until then there is **no Azure story** for NFR-04, and the traceability table shows "OPEN-13, no Azure story" (A-02). If it is assigned, the Azure track adds a story with the next free `US-AZ-` number in `azure-r1` or `azure-r2`. Nothing in this backlog waits for that answer.
* **NFR-06 and NFR-08** are linked by OPEN-22 (7-year audit retention against RPO and RTO). Each is one track's story.

### 5.4 Constraints and success measures carried by the backlog

| ID | Carried by |
|---|---|
| C-01 (lease ends 30 June 2027) | Release order; `US-AZ-013`, `US-AZ-014` (a spare Sunday stays free) |
| C-02 (end-of-support servers) | `US-AZ-015`, `US-AZ-016` |
| C-03 (StockPilot does not change) | `US-AZ-001`, `US-AZ-002`, `US-AZ-003`, `US-AZ-005`, `EN-AZ-09`, `EN-AZ-14`, `US-AZ-012`; `US-DN-012`, `EN-DN-15` |
| C-04 (EUR 1,500 per month) | `EN-AZ-12`, `US-AZ-017` |
| C-05 (Order Desk is the single source of truth) | `EN-DN-10`, `US-DN-016` |
| C-06 (small IT team, no Kubernetes) | `EN-AZ-03`, `EN-AZ-12`, `US-AZ-019` |
| SM-07 (servers past end of support) | `US-AZ-015`, `US-AZ-016` |
| SM-01 to SM-04 | `US-DN-030` to `US-DN-033` |

## 6. Azure track backlog (`track-azure`)

Rules for every Azure item that touches infrastructure: it is written as Bicep with Azure Verified Modules where a module exists (ES-22), uses France Central (ES-20), is named `<resource-abbreviation>-nw-<workload>-<environment>-<region>` (for example `app-nw-orderdesk-prd-frc`; abbreviations follow A-39) and carries the four tags `workload`, `environment`, `owner` and `costCenter` (ES-23, ES-24). It is validated with `az bicep build` and reviewed. **Nothing is deployed** (ES-27). No secret, key, connection string, tenant ID or subscription ID appears in any file. Placeholders are used (NFR-05, ES-17).

### EP-AZ-01 Foundation and proof

* Tags: track-azure, azure-r1
* Type: Epic | Priority: Must | Status: Draft
* (source: C-01, C-03, C-04, NFR-01, NFR-03, NFR-05, CS-10)
* Goal: answer the biggest unknowns early (the nightly StockPilot exchange, the hosting target and cost), and prepare Azure for rehearsals.
* Contains: `FT-AZ-01`, `FT-AZ-02`, `FT-AZ-03`, `FT-AZ-04`.
* Cross-track **OPEN:** items stated for this release: OPEN-03, OPEN-04, OPEN-05, OPEN-13, OPEN-19, OPEN-21. Without the answers, this release builds only hosting, data and exchange work, makes no Order Desk code change, estimates the whole platform with no split of the ceiling, plans no pilot environment and no sign-in plumbing, names the hosting setup it assumes, and covers the infrastructure pipeline only (A-28, section 8).

#### FT-AZ-01 Azure foundation and network

* Tags: track-azure, azure-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-01`
* (source: C-01, NFR-03, CS-09, CS-19, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27)
* Description: a named Azure foundation exists for `tst` and `prd` in France Central, with a private network for data services and an automated pipeline for infrastructure code. It is checked locally with `az bicep build`. Nothing is deployed.
* Enablers: `EN-AZ-01`, `EN-AZ-02`, `EN-AZ-07`.

##### EN-AZ-01 Azure foundation: region, names, tags, Bicep, `tst` and `prd`

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-01`
* (source: C-01, NFR-03, ES-20, ES-22, ES-23, ES-24, ES-27, CS-09)
* Depends on (same track): none
* Enables: `FT-AZ-01` to `FT-AZ-11` (every Azure item lands in this foundation)
* ASSUMPTION / OPEN used: A-39, OPEN-32

**Story.** As an IT manager, I want a written foundation for the test (`tst`) and production (`prd`) environments in France Central, so that every later Azure resource lands in an agreed, EU-only, named and tagged place (NFR-03).

**Acceptance criteria**

1. Given an `infra/` folder (ES-10) with one `main.bicep` for each environment and a `.bicepparam` file for each (ES-22), When `az bicep build` runs for `tst` and for `prd`, Then both build with no error and nothing is deployed.
2. Given any resource in the templates, When I read its name and tags, Then the name follows `<resource-abbreviation>-nw-<workload>-<environment>-<region>` with environment `tst` or `prd`, and the tags `workload`, `environment`, `owner` and `costCenter` are all present. Tag values are placeholders where they are not yet known.
3. Given the primary region parameter, Then its value is France Central. Given a secondary region parameter, When it is set to a region outside the European Union, Then the build fails with a clear message (NFR-03, ES-20). Which secondary region, if any, is used is **OPEN:** OPEN-32.
4. Given backup storage and log workspace settings in the templates, When the templates are checked, Then every one is set to a region inside the European Union.
5. Given the repository, When it is scanned for tenant IDs, subscription IDs, keys and passwords, Then none is found.

##### EN-AZ-02 Network foundation and private endpoints

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-01`
* (source: CS-09, ES-25, ES-20, ES-27)
* Depends on (same track): `EN-AZ-01`
* Enables: `FT-AZ-03`, `FT-AZ-05`, `FT-AZ-07`, `FT-AZ-08`
* ASSUMPTION / OPEN used: none

**Story.** As an IT manager, I want a private network and private endpoints for data services, so that the database, storage and Key Vault are never open to the internet (ES-25).

**Acceptance criteria**

1. Given the `tst` and `prd` templates, When `az bicep build` runs, Then each environment has a virtual network with separate subnets for the application, for data and for private endpoints, and private DNS zones for the data services.
2. Given a database, a storage account or a Key Vault in the templates, When I read its settings, Then public network access is turned off and a private endpoint exists for it.
3. Given the network design, When it is reviewed, Then it contains no connection to Antwerp. That connection is `EN-AZ-14`.
4. Given the network design, When it is reviewed, Then each subnet and endpoint name follows ES-23 and carries the four tags (ES-24).

##### EN-AZ-07 Infrastructure pipeline

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-01`
* (source: CS-19, ES-22, ES-27, NFR-05)
* Depends on (same track): `EN-AZ-01`
* Enables: `FT-AZ-01`, `FT-AZ-03`, and the checks used by every later Azure enabler
* ASSUMPTION / OPEN used: OPEN-21

**Story.** As an IT manager, I want an automated pipeline that checks the infrastructure code on every change, so that nobody builds or copies infrastructure by hand as is done for Order Desk today (CS-19).

**Acceptance criteria**

1. Given a pull request that changes anything under `infra/`, When the pipeline runs, Then it runs `az bicep build` for `tst` and `prd` and fails the check if either has an error.
2. Given the pipeline definition and its variables, When they are scanned, Then no password, key or connection string is stored. The pipeline signs in with a managed or federated identity, shown as a placeholder.
3. Given the pipeline has a deployment step, When the pipeline definition is read, Then that step is switched off and needs a named human approval. It is not run from this workshop (ES-27).
4. Given the ownership of build and deployment pipelines is not yet agreed, When the pipeline is defined, Then this pipeline covers infrastructure only. **OPEN:** OPEN-21 (CI/CD ownership). Without the answer, this pipeline does not build or test application code.

#### FT-AZ-02 Hosting and data decision with a cost model

* Tags: track-azure, azure-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-01`
* (source: C-02, C-04, C-06, ES-21)
* Description: the product owner can read a recorded decision on where Order Desk and its database run, with a monthly cost estimate for production plus one test environment against the EUR 1,500 ceiling.
* Enablers: `EN-AZ-03`, `EN-AZ-12`.

##### EN-AZ-03 Hosting and data decision record

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-02`
* (source: C-02, C-04, C-06, ES-21, ES-08, A-23)
* Depends on (same track): `US-AZ-004`, `US-AZ-005`
* Enables: `FT-AZ-03`, `FT-AZ-05`, `FT-AZ-06`, `FT-AZ-07`, `FT-AZ-08`
* ASSUMPTION / OPEN used: A-09, A-23, OPEN-19, OPEN-04

**Story.** As an IT manager, I want a decision record for where the Order Desk web application and its database run in Azure, so that the move, the exchange and the cost are designed on one agreed target (C-06).

**Acceptance criteria**

1. Given the options for the web host (platform services only, no Kubernetes, ES-21) and for the database (for example a managed instance, a managed database or SQL Server on a virtual machine), When the record is written in `docs/architecture/` (ES-08), Then each option is described with its effect on the StockPilot exchange, on run cost, and on what a six-person .NET team can operate (C-06).
2. Given the result of `MVE-BA01` (`US-AZ-005`), When the record is written, Then the record states which database features the exchange needs and which option supports them.
3. Given the claim that Azure's managed database lacks the command-line call and local-disk bulk load (A-23), When the record is written, Then that claim is checked against the official Microsoft page and A-23 is confirmed or corrected. A search summary is not enough.
4. Given the record, When the record is written, Then it states the number of web instances and how the draft order is handled when there is more than one (OPEN-19). Without the answer, it names the setup it assumes.
5. Given the record, When the record is written, Then it has a status of "proposed" until a named person approves it. It states the approver (OPEN-04 for cost).

##### EN-AZ-12 Cost model

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-02`
* (source: C-04, C-06, ES-09, A-09, A-14)
* Depends on (same track): `EN-AZ-03`
* Enables: `FT-AZ-02`, `US-AZ-017`
* ASSUMPTION / OPEN used: A-09, A-14, A-45, OPEN-04

**Story.** As a sponsor, I want a monthly cost estimate for production plus one test environment, so that I know early whether the run cost stays at or under EUR 1,500 per month (C-04).

**Acceptance criteria**

1. Given each option in `EN-AZ-03`, When the estimate is written in `docs/migration/` (ES-09), Then it shows the monthly cost per service for `prd` and `tst`, with the price source and date.
2. Given the estimate, When it is read, Then it includes the hosting of the portal as well as Order Desk, because the ceiling is shared (A-14), and it shows the total against EUR 1,500.
3. Given any full option above EUR 1,350 per month (10 % under the ceiling, A-45), When the estimate is checked, Then it is flagged as "at risk".
4. Given a pivot from `US-AZ-005`, When the cost is re-run, Then the new result is added with the reason.
5. Given the owner of the ceiling is not agreed (OPEN-04), When the estimate is made, Then the estimate covers the whole platform and applies no split between tracks.

#### FT-AZ-03 Secrets and monitoring baseline on `tst`

* Tags: track-azure, azure-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-01`
* (source: NFR-05, NFR-01, CS-22, ES-17, ES-25, ES-26)
* Description: no password or key is kept in code or pipelines. Applications reach data services without passwords. Availability is measured by a probe, and logs from every resource go to one place per environment. This replaces ping checks and a weekly look at the Event Log.
* Enablers: `EN-AZ-04`, `EN-AZ-05`.

##### EN-AZ-04 Secrets and managed identity on `tst`

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-03`
* (source: NFR-05, ES-17, ES-25)
* Depends on (same track): `EN-AZ-02`, `EN-AZ-03`, `EN-AZ-07`
* Enables: `FT-AZ-03`, `FT-AZ-05`
* ASSUMPTION / OPEN used: none

**Story.** As an IT manager, I want secrets held in Azure Key Vault and applications to use managed identities on `tst`, so that no password, key or connection string with a password exists in code, templates or pipelines (NFR-05, platform side).

**Acceptance criteria**

1. Given the `tst` templates, When `az bicep build` runs, Then a Key Vault with a private endpoint exists, and the web application has a managed identity that is allowed to read only the secrets it needs.
2. Given the database connection for the application on `tst`, When it is configured, Then it uses the managed identity and holds no password (ES-25).
3. Given the templates, the parameter files and the pipeline (`EN-AZ-07`), When they are scanned for secrets, Then none is found, and the scan runs on every change.
4. Given a secret must exist, When the template is written, Then the template holds only the name of the secret, never its value.

##### EN-AZ-05 Observability baseline on `tst`

* Tags: track-azure, azure-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-03`
* (source: NFR-01, CS-22, ES-26, A-11)
* Depends on (same track): `EN-AZ-01`, `EN-AZ-02`
* Enables: `FT-AZ-03`, `US-AZ-007`
* ASSUMPTION / OPEN used: A-11, A-37, OPEN-08, OPEN-23

**Story.** As an IT manager, I want one log workspace per environment, application monitoring and an availability probe on `tst`, so that I can measure availability and see problems, instead of the ping checks and weekly Event Log look I have today (CS-22).

**Acceptance criteria**

1. Given the `tst` templates, When `az bicep build` runs, Then one Log Analytics workspace exists for `tst`, every resource sends its diagnostics to it, and Application Insights is set up for the web application (ES-26).
2. Given the probe definition, When the probe runs, Then it calls the Order Desk sign-in page about every 5 minutes (A-37) and records success or failure.
3. Given the probe fails for two checks in a row, When the second check fails, Then an alert goes to the IT team's alert group (a placeholder address).
4. Given the availability target of 99.5 % in business hours, Monday to Saturday 06:00 to 20:00 CET (NFR-01), When the probe data is queried, Then the probe data can be filtered to those hours and the time zone is stated in the query (OPEN-23).
5. Given the measurement period and scope are not agreed (OPEN-08), When the baseline is measured, Then the baseline measures Order Desk per calendar week (A-37, A-11).

#### FT-AZ-04 StockPilot exchange proof

* Tags: track-azure, azure-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-01`
* (source: CS-10, C-03, A-23, OPEN-07, OPEN-20)
* Description: the outcome of experiment `MVE-BA01` is recorded: the nightly exchange can be reproduced with the same files, the same 02:00 cadence and the same paths, and Antwerp's file-transfer details are known. The experiment is design and review only. No real Azure resource is created and no production data is moved (ES-27).
* Stories: `US-AZ-001` to `US-AZ-005`. No enabler is needed before them. They need only a local developer machine.

##### US-AZ-001 Prove the nightly order file is identical

* Tags: track-azure, azure-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-04`
* (source: CS-10, C-03, ES-27, A-23, A-32)
* Depends on (same track): none
* ASSUMPTION / OPEN used: A-06, A-23, A-32, OPEN-30

**Story.** As an IT manager, I want to reproduce the nightly order export so that it writes the same file as today without the database server's command-line call and without a local `D:\` drive, so that I know the StockPilot exchange can move to Azure with no change to StockPilot.

**Facts for the developer.** Today a job at 02:00 exports confirmed orders as a CSV file to an SFTP server for StockPilot, and imports shipment updates (CS-10). The export file is named `orders_YYYYMMDD.csv` and it lists orders in status Confirmed that were not yet exported (A-22). The file format (separator `;`, no header row, no quotes, default character set) is an assumption (A-32).

**Acceptance criteria**

1. Given a throw-away local developer SQL Server and made-up sample data in three sets, S1 (5 orders, about 12 lines), S2 (names with accents, a very long address, and one address that contains a semicolon) and S3 (about 300 orders and 2,000 lines, a normal day, CS-05), When the new export runs on each set, Then the file name is `orders_YYYYMMDD.csv` and its SHA-256 fingerprint equals the fingerprint of the legacy export on the same data, on 3 of 3 runs.
2. Given a fingerprint differs, When the files are compared, Then every differing byte position is listed and linked to a named setting (separator, line ending, character set, row order). The legacy behaviour is not fixed in this test, because identical files are the goal.
3. Given the proof runs, When I check what it touched, Then no real Azure resource is created, no production data is used and no secret is written down. A real sample file from the live exchange folder is taken only with Ahmed Benali's explicit approval, and it is made anonymous first (OPEN-30).
4. Given the result, When I read it, Then the SHA-256 value, size and row count of every legacy file and every new file are recorded.

##### US-AZ-002 Prove the shipment file gives the same result

* Tags: track-azure, azure-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-04`
* (source: CS-10, C-03, ES-19, ES-27, A-19, A-32)
* Depends on (same track): none
* ASSUMPTION / OPEN used: A-19, A-32, OPEN-20, OPEN-30

**Story.** As an IT manager, I want to ingest a sample shipment file with the new method and get the same order statuses and audit rows as the legacy procedure, so that shipment updates from Antwerp keep working after the move.

**Facts for the developer.** StockPilot puts `shipments.csv` on the SFTP server. It has a header row and the columns `OrderNumber;ShippedAt;Carrier` (A-32). Today the import moves orders from Picking to Shipped (A-22). The import writes a "Shipped" audit row for every shipment row, even a repeated one. That is believed to be unintended (A-19).

**Acceptance criteria**

1. Given a sample `shipments.csv` and orders in status Picking, When the new ingest runs without a command-line call or a local-disk bulk load, Then the final order statuses and the audit rows equal those from the legacy procedure on 3 of 3 runs.
2. Given a run shows different audit rows because of the repeated "Shipped" rows (A-19), When the difference is recorded, Then it comes with a proposed decision record to keep or fix the behaviour (ES-19). It is not changed silently.
3. Given an extra run with an empty file, a replayed file and a clock difference, When each run finishes, Then each result is recorded.
4. Given a schema change would be needed, When the proof reaches that point, Then it is not made. It goes to a migration-impact check (OPEN-20).

##### US-AZ-003 Confirm the Antwerp file-transfer details in writing

* Tags: track-azure, azure-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-04`
* (source: CS-10, CS-09, C-03, NFR-05)
* Depends on (same track): none
* ASSUMPTION / OPEN used: OPEN-07, OPEN-30

**Story.** As an IT manager, I want Antwerp IT to confirm the file-transfer host, the account type, the pick-up window and the empty-day rule in writing, so that the Azure path to Antwerp can be designed on facts.

**Acceptance criteria**

1. Given a 30-minute call with the StockPilot contact in Antwerp (Pieter Janssens or the person he names, OPEN-30), When the call ends, Then four things are confirmed in writing with the date and the name of the person who answered: where the SFTP host is (inside Antwerp or elsewhere), the account type, the time window in which StockPilot picks up and drops files, and what is expected on a day with no orders.
2. Given the answers, When I search the repository files, Then no user name, password or key is written in any repository file. They are marked "held by IT, not in this repository" (NFR-05).
3. Given Antwerp says the files must change, When the call is written up, Then the answer is recorded as a conflict with constraint C-03 and escalated to Marc Dubois and Lena Varga. It is not worked around.
4. Given the answers, When the call is written up, Then OPEN-07 is updated with what is now known.

##### US-AZ-004 Record which server features the proof needed

* Tags: track-azure, azure-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-04`
* (source: C-04, C-02, CS-10, A-23, ES-21)
* Depends on (same track): `US-AZ-001`, `US-AZ-002`
* ASSUMPTION / OPEN used: A-45, A-23, OPEN-04

**Story.** As an IT manager, I want to know which database-server features the proof needed, so that I choose the right hosting target and re-check the cost if SQL Server on a virtual machine is needed.

**Acceptance criteria**

1. Given the proof is done, When I write the result, Then it states for each of three features whether the proof needed it: the command-line call, a local-disk bulk load, and SQL Server on a virtual machine.
2. Given no feature was needed, When the result is written, Then it is "persevere" for this check.
3. Given a virtual machine is needed, When the cost model is re-run (`EN-AZ-12`), Then at least one complete option comes at or under EUR 1,350 per month for `prd` plus `tst` (A-45). Otherwise the result is "stop" for this check and the question goes to Marc Dubois (OPEN-04).

##### US-AZ-005 Record the `MVE-BA01` outcome and its effect

* Tags: track-azure, azure-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-04`
* (source: CS-10, C-03, A-23, A-06)
* Depends on (same track): `US-AZ-001`, `US-AZ-002`, `US-AZ-003`, `US-AZ-004`
* ASSUMPTION / OPEN used: A-06, A-23, A-30, OPEN-07, OPEN-20

**Story.** As a product owner, I want the outcome of `MVE-BA01` recorded as persevere, pivot or stop with its evidence, so that the content of `azure-r2` is decided on facts.

**Acceptance criteria**

1. Given the four checks (`US-AZ-001` to `US-AZ-004`), When the outcome is recorded, Then the overall result is the weakest of the four. Persevere only if all four persevere. Stop if any one says stop. Otherwise pivot.
2. Given **persevere**, When the outcome is recorded, Then `EN-AZ-09` is built from the proven design, `EN-AZ-14` uses the named Antwerp path, and A-23 is confirmed or corrected.
3. Given **pivot**, When the outcome is recorded, Then `EN-AZ-03` is reopened with the new constraint, `EN-AZ-12` is re-run, `EN-AZ-09` is resized, and each difference found is added as a story with the next free `US-AZ-` number in `azure-r2`. The product owner and the sponsor review the release dates (A-07).
4. Given **stop**, When the outcome is recorded, Then `azure-r2` is not approved until Lena Varga and Marc Dubois decide the next step. `azure-r1` continues with its other enablers (`EN-AZ-01`, `EN-AZ-02`, `EN-AZ-04`, `EN-AZ-05`, `EN-AZ-07`, `EN-AZ-12`).
5. Given a pass, When the outcome is recorded, Then the note says a pass does not prove that the Azure run works. The `azure-r2` rehearsal still has to prove it.
6. Given a result touches freshness of order status or a change to the Order Desk database, When the outcome is recorded, Then it is written under OPEN-01 and OPEN-20, and the Azure track keeps the 02:00 cadence and identical files until they are answered.

### EP-AZ-02 Production cutover

* Tags: track-azure, azure-r2
* Type: Epic | Priority: Must | Status: Draft
* (source: BR-13, C-01, C-03, NFR-01, NFR-03, NFR-05, NFR-06)
* Goal: Order Desk and its database run in Azure production. Staff keep working. The nightly exchange continues. Backups and recovery are tested. This is the Must outcome of the Azure track.
* Contains: `FT-AZ-05`, `FT-AZ-06`, `FT-AZ-07`, `FT-AZ-08`, `FT-AZ-09`.
* Cross-track **OPEN:** items stated for this release: OPEN-01, OPEN-03, OPEN-04, OPEN-05, OPEN-06, OPEN-18, OPEN-19, OPEN-20, OPEN-22, OPEN-23. Each item below says what it does without the answer (A-28).

#### FT-AZ-05 Production environment and Antwerp connection

* Tags: track-azure, azure-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-02`
* (source: BR-13, NFR-01, NFR-03, NFR-05, CS-09, CS-10, OPEN-07)
* Description: a production environment has secrets, monitoring and EU-resident data, and a connection path to the Antwerp file-transfer host.
* Enablers: `EN-AZ-14`. Follow-on stories: `US-AZ-006`, `US-AZ-007`, `US-AZ-008`.

##### EN-AZ-14 Hybrid connectivity to Antwerp

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-05`
* (source: CS-09, CS-10, C-03, ES-25)
* Depends on (same track): `EN-AZ-02`, `EN-AZ-03`
* Enables: `FT-AZ-05`, `FT-AZ-08`, `FT-AZ-09`
* ASSUMPTION / OPEN used: OPEN-07, OPEN-30

**Story.** As an IT manager, I want a defined and secured network path between the Azure network and the Antwerp file-transfer host, so that the nightly exchange can run from Azure (C-03).

**Facts for the developer.** Today Lyon has a site-to-site VPN to Antwerp (CS-09). The Antwerp host location and account type are being confirmed (`US-AZ-003`, OPEN-07).

**Acceptance criteria**

1. Given the host location and account type confirmed in `US-AZ-003`, When the path is written in Bicep, Then `az bicep build` passes for `prd` and the path reaches the Antwerp host and no other Antwerp system.
2. Given the answer is not yet known (OPEN-07), When the design is made, Then the story uses the most probable design, marks it as an assumption in the design note, and lists what must be confirmed. It does not wait for the answer to start.
3. Given a dummy test file, When the connectivity is tested, Then the test is part of the cutover rehearsal (`US-AZ-013`), and the test result is recorded there. Nothing is deployed from this workshop (ES-27).
4. Given the path, When the files are checked, Then no credential is written in any file (NFR-05).

##### US-AZ-006 No secrets in production

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-05`
* (source: NFR-05, ES-17, ES-25)
* Depends on (same track): `EN-AZ-04`
* ASSUMPTION / OPEN used: none

**Story.** As an IT manager, I want the production environment to hold no password or key in code, templates or pipelines, so that NFR-05 holds on `prd` as it does on `tst`.

**Acceptance criteria**

1. Given the `prd` templates, When `az bicep build` runs, Then a production Key Vault exists behind a private endpoint, and each application reaches data services through a managed identity with no password (ES-25).
2. Given the `prd` templates, parameter files and pipeline, When scanned, Then no secret is found, on every change.
3. Given a person needs a secret value, When the value is stored, Then it is entered into Key Vault by an authorised person and never appears in the repository.

##### US-AZ-007 Production monitoring and availability probe

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-05`
* (source: NFR-01, CS-22, CS-06, ES-26, A-11)
* Depends on (same track): `EN-AZ-05`
* ASSUMPTION / OPEN used: A-11, A-37, OPEN-08, OPEN-23

**Story.** As an IT manager, I want production monitoring with an availability probe and alerts, so that I can show 99.5 % availability in business hours and notice a problem before staff call me. Today there is one server and only ping checks (CS-06, CS-22).

**Acceptance criteria**

1. Given `prd`, When `az bicep build` runs, Then one Log Analytics workspace exists for `prd`, every resource sends diagnostics to it, and Application Insights is set up for the web application (ES-26).
2. Given the probe, When it is running, Then it checks Order Desk about every 5 minutes and alerts the IT team's alert group after two failed checks in a row, in business hours Monday to Saturday 06:00 to 20:00 CET (A-37).
3. Given one calendar week, When the report runs, Then it shows availability as a percentage for business hours, with the time zone stated (OPEN-23). In 84 business hours, 99.5 % allows about 25 minutes of downtime (A-37).
4. Given the measurement period is not agreed (OPEN-08), When the report runs, Then the report uses the calendar week and says so.

##### US-AZ-008 Production data, backups and logs stay in the EU

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-05`
* (source: NFR-03, CS-09, ES-20)
* Depends on (same track): `EN-AZ-01`
* ASSUMPTION / OPEN used: OPEN-32

**Story.** As an IT manager, I want to show that every production resource that holds data, backups or logs is in the European Union, so that NFR-03 holds on `prd`.

**Acceptance criteria**

1. Given the `prd` templates, When `az bicep build` runs, Then every resource location is France Central or an agreed EU secondary region (OPEN-32).
2. Given backup storage, log workspace and any copy of data, When I read their settings, Then each is set to an EU region.
3. Given this story is done, When I read its result, Then it holds a table of every `prd` resource that keeps data, backups or logs with its region, written as a draft section that the cutover runbook (`EN-AZ-13`) can reuse. The table is part of this story and needs nothing from a later release.

#### FT-AZ-06 Backup, disaster recovery and tested restore

* Tags: track-azure, azure-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-02`
* (source: NFR-06, CS-07, CS-23, OPEN-22)
* Description: order data can be recovered with at most 1 hour of lost data (RPO) and in at most 4 hours (RTO). A restore is tested and reported. The last disaster-recovery test was never done (CS-23).
* Enabler: `EN-AZ-06`. Story: `US-AZ-009`.

##### EN-AZ-06 Backup, disaster recovery and restore method

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-06`
* (source: NFR-06, CS-07, CS-23, NFR-03)
* Depends on (same track): `EN-AZ-03`
* Enables: `FT-AZ-06`, `FT-AZ-07`, `FT-AZ-09`
* ASSUMPTION / OPEN used: OPEN-22, OPEN-32

**Story.** As an IT manager, I want database backups and a written restore method that meet an RPO of 1 hour and an RTO of 4 hours, so that order data can be recovered (NFR-06).

**Facts for the developer.** Today the database is backed up fully every night and its log every 15 minutes, kept 35 days on a local backup appliance (CS-07).

**Acceptance criteria**

1. Given the `prd` database templates, When `az bicep build` runs, Then backups allow a restore to any point in time with at most 1 hour of lost data, and a full backup and a log backup schedule are shown (the legacy log backup is every 15 minutes, CS-07).
2. Given the backup settings, When they are checked, Then backups are kept at least 35 days, as today (CS-07), and stay in the EU (NFR-03).
3. Given the restore method, When it is written in `docs/migration/` (ES-09), Then it has numbered steps, the person who does each step, and the expected time of each, with a total of at most 4 hours.
4. Given 7 years of audit data must be kept (NFR-08), When the backup design is made, Then the backup design backs audit data up on the same schedule as other order data and sizes retention at today's volume. A retrieval target is not defined. **OPEN:** OPEN-22 (the owner of the retention rules is the .NET side of the same question).
5. Given a secondary region is used for recovery, When the region is chosen, Then it is in the EU (ES-20, OPEN-32).

##### US-AZ-009 Tested restore meets RPO and RTO

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-06`
* (source: NFR-06, CS-23, CS-07)
* Depends on (same track): `EN-AZ-06`, `EN-AZ-08`
* ASSUMPTION / OPEN used: OPEN-22

**Story.** As an IT manager, I want to restore the order database from backup into a rehearsal environment and measure it, so that I know the RPO of 1 hour and the RTO of 4 hours are met. Disaster recovery has never been tested (CS-23).

**Acceptance criteria**

1. Given backups are running on the rehearsal environment, When I restore to a point in time of my choice, Then the data lost between the chosen point and the last backup is at most 1 hour.
2. Given the restore, When I time it from the decision to restore until the database accepts queries, Then the total is at most 4 hours.
3. Given the test is finished, When I read the written report, Then it lists steps, start and end times, the result against RPO and RTO, and any gap. Each gap becomes a new story with the next free `US-AZ-` number.
4. Given a copy of production data is needed, When it is requested, Then it is used only with Ahmed Benali's explicit approval, stays in the EU, and is deleted after the test (ES-27, NFR-03).

#### FT-AZ-07 Data move: database and invoice files

* Tags: track-azure, azure-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-02`
* (source: BR-13, CS-07, CS-08, CS-11, CS-21, OPEN-06)
* Description: the 48 GB database (growing about 1 GB per month) is moved in a rehearsal inside the Sunday window. About 120 GB of invoice PDFs (growing about 2 GB per month) are moved to a store that Order Desk can read.
* Enablers: `EN-AZ-08`, `EN-AZ-10`. Stories: `US-AZ-010`, `US-AZ-011`.

##### EN-AZ-08 Database migration method and rehearsal

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-07`
* (source: BR-13, CS-07, CS-21, C-01, NFR-03)
* Depends on (same track): `EN-AZ-03`, `EN-AZ-06`
* Enables: `FT-AZ-06`, `FT-AZ-07`, `FT-AZ-09`
* ASSUMPTION / OPEN used: A-38, OPEN-23

**Story.** As an IT manager, I want a repeatable, scripted method to move the 48 GB order database to Azure, with timings from rehearsals, so that I know it can be moved, checked and rolled back inside the six-hour Sunday window (BR-13).

**Facts for the developer.** The database `NorthwindOrders` is about 48 GB and grows about 1 GB per month (CS-07). The window is Sunday 06:00 to 12:00 CET (CS-21).

**Acceptance criteria**

1. Given the method chosen in `EN-AZ-03`, When a rehearsal runs on a restored copy of the Lyon database, Then the time for each step (copy, restore, check, switch, rollback) is recorded.
2. Given the recorded times, When they are added up, Then the move, the data check and the rollback together fit inside the window with at least 30 minutes spare, and the go/no-go point is at 09:00 CET (A-38). If they do not fit, a new story is added with the next free `US-AZ-` number.
3. Given the method, When it is reviewed, Then every step is a script or a written step with an owner, so that it can be repeated without change.
4. Given the Lyon database is the source, When it runs, Then the method never writes to it.
5. Given the data is copied, When it moves, Then it moves only to EU regions and is encrypted in transit (NFR-03). A copy of production data is used only with Ahmed Benali's explicit approval (ES-27).
6. Given date columns differ in time zone between Lyon and Azure hosts (A-10), When the rehearsal runs, Then the rehearsal compares a sample of date values before and after and records any shift (OPEN-23).

##### EN-AZ-10 Invoice store migration

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-07`
* (source: CS-08, CS-11, CS-14, A-17, ES-25)
* Depends on (same track): `EN-AZ-02`, `EN-AZ-03`
* Enables: `FT-AZ-07`, `FT-AZ-09`
* ASSUMPTION / OPEN used: OPEN-06

**Story.** As an IT manager, I want the existing invoice PDF files moved to an Azure file store with the same folder layout, so that Order Desk can still read them after the move (CS-08).

**Facts for the developer.** About 120 GB of PDFs, growing about 2 GB per month. The finance system writes one PDF per invoice to `\\NWFS01\invoices\{year}\{invoiceNumber}.pdf` and Order Desk reads them (CS-08, CS-11).

**Acceptance criteria**

1. Given the store chosen in `EN-AZ-03`, When the copy runs, Then the folder layout `{year}\{invoiceNumber}.pdf` is kept and the file count and total size equal the source at the check.
2. Given files are added to the source until the cutover (about 2 GB per month), When a repeat copy runs, Then a repeat copy brings the new files across, and the last copy is part of the cutover runbook.
3. Given the store, When it is accessed, Then it is reached only through a private endpoint and a managed identity, with no shared key in any file (ES-25, NFR-05).
4. Given how the finance system will write new invoices after the move is not agreed, When the story is built, Then this story moves the existing files only and changes nothing in the finance system. **OPEN:** OPEN-06 (Julien Moreau).

##### US-AZ-010 Order data is identical after the move

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-07`
* (source: BR-13, CS-07, CS-21)
* Depends on (same track): `EN-AZ-08`
* ASSUMPTION / OPEN used: A-38

**Story.** As an Order Desk clerk, I want the orders in Azure to be exactly the orders that were in Lyon when the move started, so that no order is lost or changed (BR-13).

**Acceptance criteria**

1. Given a rehearsal copy of the Lyon database and the migrated database, When the checks run, Then the row count of every table is equal.
2. Given the same two databases, When the checks run, Then the highest order number and a checksum of the key columns of each table are equal.
3. Given any difference, When the checks run, Then the check fails, lists the table and the rows, and the go/no-go point in the runbook is "no-go" (A-38).
4. Given the check, When it is timed on the rehearsal data, Then it runs in under 30 minutes (A-38), so that it fits the window.

##### US-AZ-011 Invoice PDFs are available in Azure

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-07`
* (source: CS-08, CS-11, BR-13)
* Depends on (same track): `EN-AZ-10`
* ASSUMPTION / OPEN used: OPEN-06

**Story.** As an Order Desk clerk, I want existing invoice PDFs to be available in Azure under the same year and invoice number, so that attaching an invoice to an order keeps working after the move.

**Acceptance criteria**

1. Given the copied store and the source share, When the check runs, Then the file count and total bytes are equal.
2. Given a random sample of 100 files, When each is compared by fingerprint, Then all are equal, and each opens as a PDF.
3. Given the application's managed identity, When it reads a file by `{year}\{invoiceNumber}.pdf` through the private endpoint, Then it succeeds. A person without access cannot read it.
4. Given the finance system, When the move is done, Then nothing in it is changed (OPEN-06).

#### FT-AZ-08 Nightly exchange and mail relay in Azure

* Tags: track-azure, azure-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-02`
* (source: CS-10, CS-12, C-03, A-19, OPEN-18, OPEN-20, OPEN-23)
* Description: the nightly 02:00 StockPilot exchange runs from Azure with the same file formats and no change to StockPilot. A replacement for the internal mail relay exists.
* Enablers: `EN-AZ-09`, `EN-AZ-11`. Story: `US-AZ-012`.

##### EN-AZ-09 StockPilot exchange redesign

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-08`
* (source: CS-10, C-03, ES-19, ES-25, A-23)
* Depends on (same track): `US-AZ-005`, `EN-AZ-03`, `EN-AZ-14`
* Enables: `FT-AZ-08`, `FT-AZ-09`
* ASSUMPTION / OPEN used: A-19, A-23, A-10, OPEN-01, OPEN-20, OPEN-23, OPEN-30

**Story.** As an IT manager, I want the nightly StockPilot exchange rebuilt for Azure with the same files, the same 02:00 time and the same folder paths, so that StockPilot keeps working with no change (C-03).

**Acceptance criteria**

1. Given the design proven in `US-AZ-001` and `US-AZ-002`, When the job is built and checked with `az bicep build` and local tests, Then it creates `orders_YYYYMMDD.csv` in the outbound folder and ingests `shipments.csv` from the inbound folder, with no command-line call and no local-drive bulk load.
2. Given the job runs at 02:00 CET (not 02:00 UTC), When it selects and names the files, Then the file-name date and the "not yet exported" selection use the CET day. The rule is stated in the design (A-10, OPEN-23).
3. Given the Antwerp SFTP paths, file names and format, When the exchange is redesigned, Then none changes (C-03).
4. Given a day with no orders or no shipment file, When the job runs, Then the behaviour follows the rule confirmed in `US-AZ-003` (OPEN-30).
5. Given the legacy import writes repeated "Shipped" audit rows (A-19), When the exchange is redesigned, Then the redesign keeps or fixes that behaviour as recorded in a decision record (ES-19).
6. Given a run fails, When the failure is detected, Then an alert goes to the IT team and the next run does not create duplicate files or duplicate audit rows.
7. Given freshness or a faster refresh is asked for (OPEN-01, OPEN-20), When the story is built, Then this story keeps the nightly cadence and builds no faster refresh.

##### EN-AZ-11 SMTP relay replacement

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-08`
* (source: CS-12, NFR-05, NFR-03, A-17, A-22)
* Depends on (same track): `EN-AZ-02`
* Enables: `FT-AZ-08`, `FT-AZ-09`
* ASSUMPTION / OPEN used: OPEN-18

**Story.** As an IT manager, I want a mail path that works from Azure to replace the internal relay `smtp.northwind.local` on port 25 without sign-in, so that the e-mail described in CS-12 keeps being sent after the move.

**Facts for the developer.** Order confirmations go through the internal relay `smtp.northwind.local`, port 25, no authentication (CS-12). No mail-sending code was found in `src/` (A-22), so who sends today is not known (OPEN-18).

**Acceptance criteria**

1. Given the replacement, When `az bicep build` runs, Then a mail path exists that is reachable from the `prd` and `tst` networks and requires sign-in (not an open relay).
2. Given the mail path, When it is configured, Then it holds no password in any file and uses a managed identity or a Key Vault secret reference (NFR-05).
3. Given the service, When it sends a message, Then it keeps data in the EU (NFR-03).
4. Given a test message sent from `tst` to a test mailbox, When the mailbox is checked, Then it arrives, and the result is recorded.
5. Given who sends order e-mail today is not known, When the story is built, Then this story covers only the e-mail that CS-12 describes today. It covers no new e-mail (OPEN-18).

##### US-AZ-012 The nightly exchange runs from Azure

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-08`
* (source: CS-10, C-03, CS-21)
* Depends on (same track): `EN-AZ-09`, `EN-AZ-14`
* ASSUMPTION / OPEN used: A-10, OPEN-01, OPEN-20, OPEN-23, OPEN-30

**Story.** As a warehouse supervisor in Antwerp, I want the nightly exchange to keep working after Order Desk moves to Azure, with the same files at the same time, so that picking and shipping carry on as before (C-03).

**Acceptance criteria**

1. Given the rehearsal environment and a test set of confirmed orders, When the 02:00 CET run starts, Then `orders_YYYYMMDD.csv` for the orders in status Confirmed that were not yet exported is placed in the outbound folder, with the same format as the legacy file, and each exported order moves to Picking as it does today.
2. Given a test `shipments.csv` placed in the inbound folder by the Antwerp side, When the same run ingests it, Then the listed orders in status Picking move to Shipped and the audit rows match the decision in `EN-AZ-09`.
3. Given the Antwerp SFTP host, When the run finishes, Then the file names, folders and format are unchanged and StockPilot needs no change (C-03). A faster refresh is not built (OPEN-01, OPEN-20).
4. Given the run date, When the file is created, Then the date in the file name is the CET date, and the run time is 02:00 CET (A-10, OPEN-23).
5. Given the run fails, When the failure is detected, Then an alert goes to the IT team and the next run does not create duplicate files.
6. Given a day without orders or without a shipment file, When the run starts, Then the result follows the rule confirmed with Antwerp (OPEN-30).

#### FT-AZ-09 Sunday-window cutover and rollback

* Tags: track-azure, azure-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-02`
* (source: BR-13, CS-21, C-01)
* Description: production cutover happens inside the Sunday window, 06:00 to 12:00 CET, with a runbook and a rollback. Staff keep working.
* Enabler: `EN-AZ-13`. Stories: `US-AZ-013`, `US-AZ-014`.

##### EN-AZ-13 Cutover runbook and rollback plan

* Tags: track-azure, azure-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-AZ-09`
* (source: BR-13, CS-21, C-01, SM-07, ES-09)
* Depends on (same track): `EN-AZ-08`, `EN-AZ-09`, `EN-AZ-10`, `EN-AZ-11`, `EN-AZ-14`, `US-AZ-009`
* Enables: `FT-AZ-09`, `FT-AZ-10`
* ASSUMPTION / OPEN used: A-38, OPEN-03, OPEN-05

**Story.** As an IT manager, I want a written cutover runbook with a rollback plan and a decommissioning checklist, so that the move happens inside the Sunday window with a safe way back.

**Acceptance criteria**

1. Given the runbook in `docs/migration/` (ES-09), When I read it, Then it lists every step from freeze to first Monday sign-in, with owner, start time, expected duration and a check for each step, all between Sunday 06:00 and 12:00 CET.
2. Given the plan, When I read the timeline, Then a go/no-go point is set at 09:00 CET and a rollback finishes before 12:00 CET (A-38).
3. Given a no-go, When the rollback steps are followed, Then service returns to Lyon with the Lyon database unchanged, and a spare Sunday before 30 June 2027 is named (C-01).
4. Given the runbook, When it is read, Then it names how staff and Antwerp are told before and after.
5. Given the decommissioning checklist, When it is read, Then it lists `NWWEB01` and `NWSQL01`, and `NWFS01` marked "only if OPEN-12 says it counts".
6. Given Order Desk code changes may not be done by the Azure track (A-03, OPEN-03), When the runbook is written, Then the runbook plans the cutover for Order Desk as it exists on the day and lists each point where it breaks on the new platform. It changes no application code. A pilot environment for the portal is not planned (OPEN-05).

##### US-AZ-013 Rehearse the cutover and rollback in the Sunday window

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-09`
* (source: BR-13, CS-21, C-01, A-07)
* Depends on (same track): `EN-AZ-13`, `US-AZ-010`, `US-AZ-011`, `US-AZ-012`
* ASSUMPTION / OPEN used: A-07, A-38, OPEN-03, OPEN-07

**Story.** As an IT manager, I want to rehearse the whole cutover, including the rollback, inside a Sunday window by the end of April 2027 (A-07), so that the production move is predictable.

**Acceptance criteria**

1. Given the runbook and a Sunday window of 06:00 to 12:00 CET, When the rehearsal runs, Then every step has a recorded start and end time, and the cutover finishes with at least 30 minutes spare (A-38).
2. Given the rehearsal, When the rollback is run as well, Then it finishes before 12:00 CET.
3. Given a dummy file, When it is sent through the Antwerp path (`EN-AZ-14`), Then the test passes and is recorded.
4. Given the rehearsal, When I read the report, Then it lists every point where Order Desk as it is today breaks on the new platform. It changes no application code (OPEN-03).
5. Given any step overruns, When the rehearsal report is written, Then it becomes a new story with the next free `US-AZ-` number.

##### US-AZ-014 Cut over production inside the Sunday window

* Tags: track-azure, azure-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-09`
* (source: BR-13, CS-21, C-01, CS-10)
* Depends on (same track): `US-AZ-013`, `US-AZ-006`, `US-AZ-007`, `US-AZ-008`
* ASSUMPTION / OPEN used: A-38, OPEN-23

**Story.** As an Order Desk clerk, I want Order Desk to be ready in Azure when I start on Monday at 06:00 CET after a Sunday cutover, so that I keep working through the move (BR-13).

**Acceptance criteria**

1. Given the go decision at the 09:00 CET checkpoint (A-38), When the cutover runs, Then planned downtime starts no earlier than Sunday 06:00 and ends no later than Sunday 12:00 CET.
2. Given Monday 06:00 CET, When a clerk signs in and opens the order list, Then it shows the same orders as before the move (counts equal).
3. Given a no-go at the checkpoint, When the no-go is declared, Then the rollback restores service in Lyon before 12:00 CET, and a spare Sunday before 30 June 2027 is booked (C-01).
4. Given the first 02:00 CET run after the cutover, When it finishes, Then the nightly file is created with the same format and in the same folder as before (CS-10, OPEN-23).
5. Given production is live, When I read the probe on the first Monday, Then the probe (`US-AZ-007`) shows green during business hours.

### EP-AZ-03 Stabilise and decommission

* Tags: track-azure, azure-r3
* Type: Epic | Priority: Must | Status: Draft
* (source: SM-07, C-04, NFR-06)
* Goal: retire the old servers so that servers past end of support go from 2 to 0 by 30 June 2027. Confirm run cost is within the ceiling. Hand over a recovery test report and runbooks.
* Contains: `FT-AZ-10`, `FT-AZ-11`.
* Cross-track **OPEN:** items stated for this release: OPEN-04, OPEN-12.

#### FT-AZ-10 Retire the old servers

* Tags: track-azure, azure-r3
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-03`
* (source: SM-07, C-01, C-02, CS-06, CS-07, OPEN-12)
* Description: `NWWEB01` and `NWSQL01` are decommissioned. The file server `NWFS01` is decommissioned only if it counts (OPEN-12). SM-07 reaches 0.
* Stories: `US-AZ-015`, `US-AZ-016`.

##### US-AZ-015 Retire the old web and database servers

* Tags: track-azure, azure-r3
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-10`
* (source: SM-07, C-01, C-02, CS-06, CS-07)
* Depends on (same track): `US-AZ-014`, `US-AZ-018`
* ASSUMPTION / OPEN used: OPEN-04, OPEN-12

**Story.** As a sponsor, I want the old web server `NWWEB01` and database server `NWSQL01` switched off and removed, so that we stop paying for extended security updates and the number of production servers past end of support is 0 by 30 June 2027 (SM-07).

**Acceptance criteria**

1. Given production runs in Azure, and the recovery test report (`US-AZ-018`) is accepted by the product owner, When the decommissioning checklist from `EN-AZ-13` is completed for `NWWEB01` and `NWSQL01`, Then both are switched off and removed from service.
2. Given the decommissioning, When it is done, Then a final backup of the Lyon database is kept as the product owner agrees, and the date and place are recorded.
3. Given the measure SM-07 (2 at baseline), When it is reported, Then it shows the count of production servers past end of support, counting `NWWEB01` and `NWSQL01`, and the date.
4. Given the owner of the EUR 1,500 ceiling is not agreed (OPEN-04), When the cost is reported, Then this story reports whole-platform cost and applies no split.

##### US-AZ-016 Decide whether the file server counts and report SM-07

* Tags: track-azure, azure-r3
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-10`
* (source: SM-07, CS-08, CS-11, C-02)
* Depends on (same track): `US-AZ-011`, `US-AZ-015`
* ASSUMPTION / OPEN used: OPEN-06, OPEN-12

**Story.** As an IT manager, I want to know whether the file server `NWFS01` counts as a production server past end of support, and decommission it only if it does, so that SM-07 is reported truthfully.

**Acceptance criteria**

1. Given OPEN-12 is answered "it counts", When the invoice files are verified in Azure (`US-AZ-011`) and Finance confirms where it writes new invoices (OPEN-06), Then `NWFS01` is decommissioned by the checklist and SM-07 counts it.
2. Given OPEN-12 is answered "it does not count" or is not answered, When the SM-07 report is written, Then it states both numbers, with and without `NWFS01`, and `NWFS01` stays in service until the answer is given.
3. Given the report, When I read it, Then it states the operating system of `NWFS01` as confirmed by Ahmed Benali (OPEN-12).

#### FT-AZ-11 Closing cost check, recovery test report and runbooks

* Tags: track-azure, azure-r3
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-AZ-03`
* (source: C-04, NFR-06, CS-23, ES-09)
* Description: the run cost is checked against the EUR 1,500 ceiling. A recovery test report and runbooks exist.
* Stories: `US-AZ-017`, `US-AZ-018`, `US-AZ-019`.

##### US-AZ-017 Closing cost check against the ceiling

* Tags: track-azure, azure-r3
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-11`
* (source: C-04, A-14, ES-09)
* Depends on (same track): `US-AZ-014`
* ASSUMPTION / OPEN used: A-14, OPEN-04

**Story.** As a sponsor, I want the real monthly run cost of the Azure platform compared with the EUR 1,500 ceiling, so that I know constraint C-04 is met.

**Acceptance criteria**

1. Given one full month of cost data for `prd` and `tst`, When the report is written in `docs/migration/` (ES-09), Then it shows cost per service and the total against EUR 1,500, and says "met" or "not met".
2. Given the cost is not met, When I read the report, Then it lists options with their savings and the effect of each on availability and recovery.
3. Given the ceiling is shared by both tracks (A-14) and its owner is not agreed (OPEN-04), When the report is written, Then it covers the whole platform and applies no split.

##### US-AZ-018 Recovery test and report on production

* Tags: track-azure, azure-r3
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-11`
* (source: NFR-06, CS-23, ES-09)
* Depends on (same track): `US-AZ-014`
* ASSUMPTION / OPEN used: OPEN-22

**Story.** As an IT manager, I want a recovery test on the production setup and a written report, so that the RPO of 1 hour and the RTO of 4 hours are proven on the real platform (NFR-06).

**Acceptance criteria**

1. Given production runs in Azure, When a restore is run as in `US-AZ-009` against a production backup in an isolated place, Then data lost is at most 1 hour and the total time is at most 4 hours.
2. Given the test, When it is finished, Then the report in `docs/migration/` lists steps, times, result against targets and each gap. Each gap becomes a new story with the next free `US-AZ-` number.
3. Given the test uses production data, When the test runs, Then it stays in the EU and is deleted after the test, with Ahmed Benali's explicit approval (ES-27).

##### US-AZ-019 Runbooks the IT team can follow

* Tags: track-azure, azure-r3
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-AZ-11`
* (source: C-06, CS-22, CS-23, ES-09, ES-01)
* Depends on (same track): `US-AZ-014`
* ASSUMPTION / OPEN used: none

**Story.** As a member of the six-person IT team, I want runbooks for daily checks, restore, a failed nightly exchange and rollback, so that we can run the platform without the people who built it (C-06).

**Acceptance criteria**

1. Given the runbooks in `docs/migration/` (ES-09), When I read them, Then each has a trigger, numbered steps, an owner and a check that shows success, in plain language (ES-01).
2. Given each runbook, When a second team member who did not write it walks through it, Then they can follow it and any gap is fixed.
3. Given the data resources in `US-AZ-008`, When I read the runbooks, Then they list them with their regions.

## 7. .NET track backlog (`track-dotnet`)

Rules for every .NET item: keep one solution `src/Northwind.OrderDesk.sln` and the three projects `Core`, `Web` and `Tests`. Add a project only with a decision record (ES-13). Keep namespaces, domain types and behaviour unless a decision record explains a change (ES-19). **Pricing rules must not change** (CS-20). No secret appears in code or configuration files (NFR-05, ES-17). Findings about the current code are from reading `src/` and `database/` on 2026-10-30. They are not in `knowledge-docs` and are used here as **ASSUMPTION:** A-22.

Words used in the portal stories: a **customer user** is a person at a customer company who signs in to the portal. A **company** is one customer account in Order Desk. **Staff** are Order Desk employees. An order has one of six statuses: Received, Confirmed, Picking, Shipped, Delivered, Cancelled (BR-04). An order has a channel that says how it was placed: Phone, E-mail, Order form or Portal (A-22).

### EP-DN-01 Modernised Order Desk

* Tags: track-dotnet, dotnet-r1
* Type: Epic | Priority: Must | Status: Draft
* (source: BR-10, NFR-05, CS-01, CS-02, CS-13, CS-14, CS-15, CS-16, CS-17, CS-18, CS-19, CS-20, ES-13, ES-14, ES-15, ES-16, ES-17, ES-18, ES-19)
* Goal: Order Desk is on a current platform and behaves as before. Tests run everywhere and pricing is unchanged. Nothing in it ties it to one server. Staff see the order channel.
* Contains: `FT-DN-01`, `FT-DN-02`, `FT-DN-03`, `FT-DN-04`.
* Cross-track **OPEN:** items stated for this release: OPEN-03, OPEN-04, OPEN-19, OPEN-21, OPEN-23.

#### FT-DN-01 Current platform and safety net

* Tags: track-dotnet, dotnet-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-01`
* (source: CS-01, CS-02, CS-18, CS-19, CS-20, ES-13, ES-14, ES-18, ES-19)
* Description: Order Desk is on .NET 10 in SDK-style projects, with one solution and the same three projects. All tests run with `dotnet test` on Windows, macOS and Linux. Pricing results and test assertions do not change. A build and test pipeline exists.
* Enablers: `EN-DN-01`, `EN-DN-02`, `EN-DN-09`.

##### EN-DN-01 SDK-style projects on `net10.0`

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-01`
* (source: CS-01, CS-02, ES-13, ES-14, ES-19)
* Depends on (same track): none
* Enables: `FT-DN-01` to `FT-DN-22` (every .NET item builds on it)
* ASSUMPTION / OPEN used: A-40, OPEN-03

**Story.** As a developer, I want the solution moved to SDK-style projects on .NET 10 (`net10.0`), keeping one solution and the three project boundaries, so that every later change is built on a current, supported platform (ES-14).

**Facts for the developer.** Order Desk is an ASP.NET MVC 5 application on .NET Framework 4.8 built in 2013. All three projects use the old project format with `packages.config` (CS-01, CS-02). ASP.NET MVC 5 does not run on .NET 10, so the Web project moves to ASP.NET Core MVC with the same routes and screens (A-40).

**Acceptance criteria**

1. Given the solution `src/Northwind.OrderDesk.sln`, When I open it, Then it still contains exactly the projects `Core`, `Web` and `Tests`, each SDK-style, each targeting `net10.0`, and no `packages.config` remains (ES-13, ES-14).
2. Given the code, When it is compared with the code before the upgrade, Then namespaces and domain type names are unchanged (ES-19).
3. Given the Web project, When I browse the existing staff screens (order list, order detail, draft order, change status, invoice), Then each still works with the same inputs and results as before.
4. Given who modernises the Order Desk code is not yet agreed with the Azure track (OPEN-03), When the story is planned, Then this story is done by the .NET track (A-03) and does not wait for that answer.

##### EN-DN-02 Tests pass on Windows, macOS and Linux

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-01`
* (source: CS-18, CS-20, ES-18)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-01`, `FT-DN-02`, `FT-DN-03`, `FT-DN-10`, `FT-DN-12`
* ASSUMPTION / OPEN used: A-22

**Story.** As a developer, I want all existing tests to run with `dotnet test src/Northwind.OrderDesk.sln` on Windows, macOS and Linux, so that pricing and order rules are protected by a safety net that anyone can run (ES-18).

**Facts for the developer.** The tests use MSTest version 1 taken from the Visual Studio installation, so they run only inside Visual Studio on the build machine (CS-18). There are 28 tests: 15 for pricing, 9 for the order service and 4 for status rules (A-22).

**Acceptance criteria**

1. Given the solution after `EN-DN-01`, When I run `dotnet test src/Northwind.OrderDesk.sln` on Windows, macOS and Linux, Then every test is found and passes on all three.
2. Given the 28 existing tests, When they are adapted to the current test framework, Then the number of tests is not lower and no assertion is weakened or removed (ES-18).
3. Given the pricing tests, When they run on the upgraded code, Then the expected values are exactly the same as before, because pricing rules do not change (CS-20).
4. Given any later change in this track, When the tests run, Then `dotnet test src/Northwind.OrderDesk.sln` still passes.

##### EN-DN-09 Build and test pipeline

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-01`
* (source: CS-19, CS-18, ES-18, NFR-05)
* Depends on (same track): `EN-DN-02`
* Enables: `FT-DN-01`, and the checks for every later .NET story
* ASSUMPTION / OPEN used: OPEN-21

**Story.** As a developer, I want an automated pipeline that builds the solution and runs the tests on every change, so that nobody publishes by hand from Visual Studio as is done today (CS-19).

**Acceptance criteria**

1. Given a change to anything under `src/`, When the pipeline runs, Then it builds the solution and runs `dotnet test src/Northwind.OrderDesk.sln` on Windows, macOS and Linux.
2. Given a failing test or build, When the pipeline runs, Then the pipeline reports a failed check.
3. Given the pipeline definition and variables, When scanned, Then no password, key or connection string is stored (NFR-05).
4. Given deployment to a server, When the pipeline is defined, Then it is not part of this pipeline. Who owns the build and test pipeline and who owns the deployment pipeline is **OPEN:** OPEN-21. Without the answer, this pipeline builds and tests only.

#### FT-DN-02 Configuration, logging and no secrets

* Tags: track-dotnet, dotnet-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-01`
* (source: NFR-05, CS-13, CS-15, CS-17, ES-15, ES-16, ES-17)
* Description: configuration and logging use the current platform methods. No secret and no Windows-sign-in database connection remain in the application's configuration.
* Enablers: `EN-DN-03`, `EN-DN-04`, `EN-DN-05`.

##### EN-DN-03 Configuration through options

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-02`
* (source: CS-17, ES-15)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-02`, `FT-DN-03`
* ASSUMPTION / OPEN used: A-22

**Story.** As a developer, I want all settings read through `Microsoft.Extensions.Configuration` and the options pattern, so that settings can change per environment without code changes (ES-15).

**Facts for the developer.** Settings today are read with `ConfigurationManager` in several classes (CS-17). They include the order history length (24 months), the invoice location and the mail host (A-22).

**Acceptance criteria**

1. Given the code in `Core` and `Web`, When I search it, Then there is no call to `ConfigurationManager`.
2. Given each setting, When it is read, Then it is a typed option bound from configuration, and an environment variable or a user secret can override it locally (ES-17).
3. Given a required setting is missing, When the application starts, Then it stops with a message that names the missing setting.
4. Given the existing tests, When they run, Then all still pass (`EN-DN-02`).

##### EN-DN-04 Logging through `ILogger<T>`

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-02`
* (source: CS-15, ES-16)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-02`
* ASSUMPTION / OPEN used: none

**Story.** As a developer, I want errors and events logged through `ILogger<T>`, so that logs work on every operating system and can be collected by Azure monitoring (ES-16).

**Facts for the developer.** Errors are written to the Windows Event Log today (CS-15).

**Acceptance criteria**

1. Given the code, When I search it, Then no class writes to the Windows Event Log (`System.Diagnostics.EventLog`).
2. Given an unhandled error in a request, When it occurs, Then one log entry with level Error is written with the request path and the exception, and no password, secret or full connection string.
3. Given the application runs on macOS or Linux, When it writes a log entry, Then logging works there.

##### EN-DN-05 No secrets and no Windows-sign-in database connection

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-02`
* (source: NFR-05, CS-13, ES-17, ES-25)
* Depends on (same track): `EN-DN-03`
* Enables: `FT-DN-02`, and every portal story that reads data
* ASSUMPTION / OPEN used: OPEN-19

**Story.** As a developer, I want the application's database connection to hold no secret and no Windows sign-in (`Integrated Security=SSPI`) and no hard-coded server name `NWSQL01`, so that no secret is kept in source or configuration files (NFR-05, application side) and the application can run in Azure.

**Facts for the developer.** The connection today uses `Integrated Security=SSPI` and the server name `NWSQL01` in `Web.config` (CS-13). In Azure, applications use managed identities and never passwords (ES-25). Locally, developers use user secrets or environment variables (ES-17).

**Acceptance criteria**

1. Given the repository, When it is scanned for passwords, keys and connection strings with a password, Then none is found in any code or configuration file.
2. Given the connection settings, When the repository is checked, Then the server name and the sign-in method are configuration values. The default checked into the repository contains no server name that is real, no password and no `Integrated Security=SSPI`.
3. Given the application runs in Azure, When it connects to the database, Then it signs in to the database with a managed identity. Given it runs locally, When it connects to the database, Then it uses a user secret or an environment variable.
4. Given the hosting and database target is not yet decided (OPEN-19), When the story is built, Then this story does only what holds for any target. It does not wait for the answer.

##### FT-DN-03 Draft order and invoice storage free of one server

* Tags: track-dotnet, dotnet-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-01`
* (source: CS-14, CS-16, A-22, OPEN-19)
* Description: the order being entered no longer lives in one web server's memory. Invoice files are read through a storage setting, not a fixed network path.
* Enablers: `EN-DN-06`, `EN-DN-07`.

##### EN-DN-06 Draft order kept outside one server's memory

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-03`
* (source: CS-16, A-22, ES-19)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-03`, `FT-DN-12`
* ASSUMPTION / OPEN used: A-22, OPEN-19

**Story.** As a developer, I want the order that is being entered to be kept outside the memory of one web server, so that it is not lost when the application restarts or runs on more than one server instance.

**Facts for the developer.** The order being entered is held in session memory (`InProc`) with a 60-minute timeout, so with more than one instance a draft is lost (CS-16, A-22).

**Acceptance criteria**

1. Given a staff member has started an order, When the application restarts or the next request goes to another instance, Then the draft is still there with all its lines.
2. Given a draft is idle for 60 minutes (as today), When the 60 minutes have passed, Then it expires.
3. Given the draft store, When it is reviewed, Then it is one place behind a small interface, so that a different store can replace it by a decision record (ES-19).
4. Given the hosting target is not yet decided (OPEN-19), When the story is built, Then this story works on one or several instances, and does not wait for the answer.

##### EN-DN-07 Invoice storage setting instead of a fixed network path

* Tags: track-dotnet, dotnet-r1
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-03`
* (source: CS-14, CS-11, A-22)
* Depends on (same track): `EN-DN-03`
* Enables: `FT-DN-03`, `FT-DN-17`
* ASSUMPTION / OPEN used: A-22, OPEN-06, OPEN-09

**Story.** As a developer, I want invoice PDFs read through a storage setting instead of a fixed network path, so that Order Desk can read them wherever they are stored.

**Facts for the developer.** Invoices are read from `{InvoiceSharePath}\{year}\{invoiceNumber}.pdf`, where the path is a network share set in configuration (CS-14, CS-11). Today the year used is the order year, not the invoice year (A-22, OPEN-09).

**Acceptance criteria**

1. Given the invoice reader, When it reads an invoice, Then it reads through a small interface with an implementation for a file path and one for another store, chosen by configuration.
2. Given the same configuration as today, When a staff member opens the invoice of a Delivered order that has an invoice number, Then the same PDF is returned as before.
3. Given an order that is not Delivered or has no invoice number, When an invoice is requested, Then no file is served, as before.
4. Given the year rule and where the finance system writes are not agreed (OPEN-06, OPEN-09), When the invoice path is built, Then the year used stays as it is today and nothing is assumed about where Finance writes.

#### FT-DN-04 Staff see the order channel

* Tags: track-dotnet, dotnet-r1
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-01`
* (source: BR-10, CS-03, A-18)
* Description: Order Desk staff can see whether an order was placed through the portal or entered by staff, and can filter by it. The server sets the Portal channel in `dotnet-r2` (`US-DN-017`).
* Stories: `US-DN-001`, `US-DN-002`.

##### US-DN-001 Staff see the order channel

* Tags: track-dotnet, dotnet-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-04`
* (source: BR-10, CS-03, A-22)
* Depends on (same track): `EN-DN-01`
* ASSUMPTION / OPEN used: A-18, A-22

**Story.** As an Order Desk clerk, I want to see on each order whether it was placed by phone, by e-mail, by order form or through the portal, so that I know how the order reached us (BR-10).

**Facts for the developer.** The channel is stored on each order. The values are Phone, E-mail, Order form and Portal. It is shown in the order list and the order detail today, so this story keeps it and proves it after the platform change (A-22, A-18).

**Acceptance criteria**

1. Given orders placed by phone, e-mail and order form, When a clerk opens the order list, Then each row shows its channel in words.
2. Given an order with the channel Portal, When the clerk opens its detail, Then the detail shows "Portal".
3. Given an order has no channel stored, When the list is shown, Then the list shows a clear "unknown" label and does not fail.

##### US-DN-002 Staff filter orders by channel

* Tags: track-dotnet, dotnet-r1
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-04`
* (source: BR-10, CS-03, A-18)
* Depends on (same track): `US-DN-001`
* ASSUMPTION / OPEN used: A-18

**Story.** As an Order Desk clerk, I want to filter the order list by channel, so that I can find all portal orders or all phone orders quickly.

**Acceptance criteria**

1. Given the order list, When I choose the channel "Portal", Then only orders with that channel are shown, and the choice is visible on the page.
2. Given I choose "All channels", When the list reloads, Then every order is shown again.
3. Given the filter is combined with the existing customer or date filters, When the list is shown, Then all filters apply together.

### EP-DN-02 Secure access and tenant isolation

* Tags: track-dotnet, dotnet-r2
* Type: Epic | Priority: Must | Status: Draft
* (source: BR-01, NFR-03, NFR-04, C-05, OQ-01)
* Goal: a customer user signs in with an identity managed outside the application, is tied to one company, and sees only that company's data. Staff sign in with Microsoft Entra ID.
* Contains: `FT-DN-05`, `FT-DN-06`, `FT-DN-07`, `FT-DN-08`.
* Cross-track **OPEN:** items stated for this release: OPEN-01, OPEN-03, OPEN-04, OPEN-05, OPEN-13, OPEN-19, OPEN-20, OPEN-22. Each item says what it does without the answer (A-28).

#### FT-DN-05 Portal architecture decision

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-02`
* (source: OQ-01, NFR-04, ES-13, A-21, OPEN-13, OPEN-25)
* Description: a recorded decision says how the portal is added to Order Desk and which sign-in provider customers use. It checks cost and limits of the options.
* Enabler: `EN-DN-11`.

##### EN-DN-11 Portal architecture and sign-in decision record

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-05`
* (source: OQ-01, NFR-04, NFR-03, ES-13, ES-08, C-04, C-05)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-06`, `FT-DN-07`, `FT-DN-08`, `FT-DN-09` to `FT-DN-14`
* ASSUMPTION / OPEN used: A-21, OPEN-10, OPEN-13, OPEN-19, OPEN-25

**Story.** As an IT manager, I want a decision record for how the portal is added to Order Desk and which identity provider customers sign in with, so that the portal stories are built on an agreed design (OQ-01).

**Acceptance criteria**

1. Given the options, When the record is written in `docs/architecture/` (ES-08), Then it compares adding the portal to the `Web` project against adding a project (a new project needs a decision record, ES-13), and it shows how the portal reads and writes orders through Order Desk with no second order database (C-05).
2. Given the customer sign-in options (Microsoft Entra External ID and invitation into the company's own tenant are the two discussed, OQ-01), When the record is written, Then the record compares them on price, limits, EU data location (NFR-03) and the data-protection requirement (OPEN-10).
3. Given the price and limits of Microsoft Entra External ID and the use of .NET 10 on Azure App Service were never verified (A-21), When the record is written, Then the record checks them against the official Microsoft pages and cites them (OPEN-25).
4. Given the record, When it is read, Then it states the decision, who approved it and when. Until it is approved, its status is "proposed".
5. Given which identity provider is chosen is not yet answered (OPEN-13), When the work is planned, Then the features that do not need sign-in details are not held up by this story, and the customer sign-in story (`US-DN-004`) starts once the choice is recorded.
6. Given the hosting target is not yet decided (OPEN-19), When the record is written, Then the record builds on the draft handling from `EN-DN-06`, which works on one or several instances.

#### FT-DN-06 Customer data separation

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-02`
* (source: BR-01, C-05, A-22)
* Description: a signed-in customer user is tied to one company, and every data read is limited to that company.
* Enabler: `EN-DN-10`. Story: `US-DN-003`.

##### EN-DN-10 Customer data separation (tenant isolation)

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-06`
* (source: BR-01, C-05, CS-04, A-22)
* Depends on (same track): `EN-DN-11`
* Enables: `FT-DN-06`, `FT-DN-07`, `FT-DN-08`, `FT-DN-09`, `FT-DN-10`, `FT-DN-11`, `FT-DN-12`, `FT-DN-13`, `FT-DN-14`, `FT-DN-16`, `FT-DN-17`, `FT-DN-18`, `FT-DN-19`, `FT-DN-21`, `FT-DN-22`, `FT-DN-23`, `FT-DN-24`, `FT-DN-26`.
* Stories that depend on it: exactly 35 stories cite it in their own "Depends on" line: `US-DN-003` to `US-DN-037`, that is, every .NET story except `US-DN-001` and `US-DN-002`. Those two are staff-only changes in `dotnet-r1`, an earlier release than this enabler, so they cannot depend on it.
* ASSUMPTION / OPEN used: A-22, OPEN-33

**Story.** As an IT manager, I want every data read and write for a customer user limited to that user's own company, with the company taken from the signed-in identity and never from the request, so that one customer can never see another customer's data (BR-01).

**Facts for the developer.** Order Desk was built for staff. In the current code, the order list, order detail and invoice actions accept a customer or order number from the request and return data, and any signed-in user can open any customer (A-22). Customer data separation is therefore new, security-critical work. It must not trust any value sent by the browser.

**Acceptance criteria**

1. Given a signed-in customer user of company A, When any portal page or action reads or writes data (order list, order detail, draft, submit, invoice), Then the company used is the one tied to the signed-in identity and no company or customer number in the URL, the form or a header changes it.
2. Given a customer user of company A requests an order of company B by changing the order number, When the request is made, Then the response is "not found" and does not reveal that the order exists.
3. Given staff, When a staff member uses a staff screen, Then staff screens keep working as today (a staff member may open any customer).
4. Given a signed-in user who is tied to no company, When the user makes a portal data request, Then the request is refused with a clear message.
5. Given an automated test for every portal read and write path (list, detail, draft, submit, invoice), When the tests run, Then each test proves points 1 and 2 and runs in the pipeline (`EN-DN-09`).
6. Given the first customer users must be created and tied to a company before the customer administrator feature exists, When the first customer users are set up, Then how that is done is **OPEN:** OPEN-33. Without the answer, this story supports a user-to-company link that staff or IT can set.

##### US-DN-003 Customer user sees only their own company

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-06`
* (source: BR-01, C-05, A-22)
* Depends on (same track): `EN-DN-10`, `US-DN-004`
* ASSUMPTION / OPEN used: A-22

**Story.** As a customer user, I want to see only the orders of my own company, so that my company's data is private.

**Acceptance criteria**

1. Given I am signed in as a user of company A, When I open the order list, Then every order shown belongs to company A and none to any other company.
2. Given a customer user of company B has orders, When I (company A) type the number of one of those orders in the address bar, Then I see a "not found" page.
3. Given I am signed out, When I open any portal order page, Then I am asked to sign in and no order data is shown.

##### FT-DN-07 Customer and staff sign-in

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-02`
* (source: BR-01, NFR-04, CS-04, OQ-01, OPEN-13)
* Description: a customer user can sign in with an identity managed outside the application. Staff sign in with their Microsoft Entra ID accounts, not Windows Integrated Authentication.
* Enabler: `EN-DN-08`. Story: `US-DN-004`.

##### EN-DN-08 Staff sign-in with Microsoft Entra ID

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-07`
* (source: NFR-04, CS-04, CS-09)
* Depends on (same track): `EN-DN-11`, `EN-DN-01`
* Enables: `FT-DN-07`, `FT-DN-13`
* ASSUMPTION / OPEN used: OPEN-03, OPEN-13

**Story.** As an Order Desk clerk, I want to sign in to Order Desk with my Microsoft Entra ID account instead of Windows Integrated Authentication, so that I can sign in from Azure without the Lyon domain (NFR-04).

**Facts for the developer.** Staff sign in today with Windows Integrated Authentication against the on-premises domain `NORTHWIND` (CS-04). Entra ID is synchronised from that domain with Entra Connect (CS-09).

**Acceptance criteria**

1. Given a staff member with an Entra ID account, When they open Order Desk, Then they sign in with that account and reach the screens they could reach before.
2. Given a person who is not a staff member, When they try to open a staff screen, Then they cannot open any staff screen.
3. Given a customer user, When they try to open a staff screen, Then they cannot open any staff screen, and a staff member's account is not treated as a customer account.
4. Given the application, When a user signs in, Then Windows Integrated Authentication is no longer required to sign in.
5. Given who builds platform sign-in plumbing is not agreed (OPEN-03, OPEN-13), When the story is built, Then this story builds the application side only and does not wait for the answer.

##### US-DN-004 Customer user signs in

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-07`
* (source: BR-01, NFR-04, OQ-01, CS-04)
* Depends on (same track): `EN-DN-11`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-21, OPEN-13, OPEN-25, OPEN-33

**Story.** As a customer user, I want to sign in to the portal with an identity managed outside the application, so that I can reach my company's orders securely (NFR-04).

**Acceptance criteria**

1. Given I have an account tied to company A, When I open the portal and sign in with the provider chosen in `EN-DN-11`, Then I reach the portal home page for company A.
2. Given I enter wrong credentials, When I try to sign in, Then I see a clear message and no data is shown.
3. Given I sign out, When I press the browser's back button, Then no order data is shown without signing in again.
4. Given the application, When I inspect what it stores, Then it stores no customer password (NFR-04, NFR-05).
5. Given the provider is not yet chosen (OPEN-13), When this story is planned, Then this story starts once the choice is recorded in `EN-DN-11`. Other features in this release do not wait for it. The first accounts are created as in OPEN-33.

##### FT-DN-08 Portal data stays in the EU

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-02`
* (source: NFR-03, ES-20, A-02)
* Description: sign-in, mail and monitoring services used by the portal keep customer and order data in the European Union.
* Story: `US-DN-005`.

##### US-DN-005 Portal sign-in, mail and monitoring keep data in the EU

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-08`
* (source: NFR-03, ES-20, A-02)
* Depends on (same track): `EN-DN-11`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-02, OPEN-10

**Story.** As an IT manager, I want every external service the portal uses (customer sign-in, e-mail sending and monitoring) to keep customer and order data in the European Union, so that NFR-03 holds for the portal.

**Acceptance criteria**

1. Given each external service chosen for the portal, When I read its configuration and the decision record (`EN-DN-11`), Then its data location is in the European Union and is stated with a source.
2. Given a service that cannot keep data in the EU, When the services are chosen, Then it is not used, and the record says why.
3. Given the portal's logs, When I read them, Then they do not contain passwords or secrets, and customer data in logs stays in the EU workspace.
4. Given a data-protection requirement for customer users (OPEN-10), When one is added, Then any added requirement becomes a new story with the next free `US-DN-` number.

### EP-DN-03 See my orders

* Tags: track-dotnet, dotnet-r2
* Type: Epic | Priority: Must | Status: Draft
* (source: BR-02, BR-03, BR-04, BR-12, NFR-02)
* Goal: customer users see the list of their company's orders, the details with their own prices, and the status.
* Contains: `FT-DN-09`, `FT-DN-10`, `FT-DN-11`.

#### FT-DN-09 See my orders

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-03`
* (source: BR-02, NFR-02, CS-05, OPEN-08, OPEN-09)
* Description: a customer user sees the list of their company's orders from the last 24 months with order date, status and total. Order list pages respond in under 2 seconds for 95 % of requests.
* Stories: `US-DN-006`, `US-DN-007`.

##### US-DN-006 See my company's orders from the last 24 months

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-09`
* (source: BR-02, CS-05, P-03, A-22)
* Depends on (same track): `EN-DN-10`, `EN-DN-14`, `US-DN-004`
* ASSUMPTION / OPEN used: A-22, OPEN-09

**Story.** As a customer user, I want to see the list of my company's orders from the last 24 months with the order number, order date, status and total, so that I can find an order without phoning the Order Desk.

**Facts for the developer.** Order Desk already has an order history length of 24 months in configuration and an index on customer and order date (A-22). Whether 24 months of orders really exist in production is not confirmed (OPEN-09). Totals are the totals stored on the order.

**Acceptance criteria**

1. Given I am signed in as a user of company A who has orders over 30 months, When I open "My orders", Then I see only company A's orders dated within the last 24 months, newest first, each with order number, order date, status and total.
2. Given the list has more orders than fit on one page, When I open it, Then it is shown in pages and I can go to the next and previous page (the page size is in A-37).
3. Given company A has no orders in the last 24 months, When I open "My orders", Then I see a message saying so.
4. Given the page, When I check it, Then it uses only data of company A (`EN-DN-10`) and meets the accessibility baseline (`EN-DN-14`).

##### US-DN-007 The order list responds in under 2 seconds

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-09`
* (source: NFR-02, CS-03, CS-05, A-22)
* Depends on (same track): `US-DN-006`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-37, OPEN-08

**Story.** As a customer user, I want the order list to open quickly, so that I do not give up and phone the Order Desk (NFR-02).

**Acceptance criteria**

1. Given a test company with about 500 orders in 24 months and 60 users loading the list at the same time (A-37), When the page is requested repeatedly for 10 minutes, Then 95 % of responses take under 2 seconds.
2. Given the list query, When it runs, Then it loads one page of orders and does not load all orders.
3. Given the result, When the test is finished, Then it is recorded with the test load used. The measurement basis is **OPEN:** OPEN-08 and the load in A-37 stands in until it is answered.

##### FT-DN-10 Order detail with my prices

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-03`
* (source: BR-03, BR-12, NFR-02, CS-20, ES-18, OPEN-16)
* Description: a customer user opens an order and sees lines, quantities, delivery address, status and their own negotiated price. Pricing rules do not change.
* Stories: `US-DN-008`, `US-DN-009`, `US-DN-010`.

##### US-DN-008 Open an order and see its details

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-10`
* (source: BR-03, P-03, CS-05)
* Depends on (same track): `EN-DN-10`, `EN-DN-14`, `US-DN-006`
* ASSUMPTION / OPEN used: none

**Story.** As a customer user, I want to open one of my company's orders and see its lines, quantities, delivery address and status, so that I can check what was ordered and where it goes.

**Acceptance criteria**

1. Given I am on "My orders", When I select an order of my company, Then I see the order number, order date, status, delivery address, and every line with product name, quantity and line price.
2. Given an order has many lines, When I open it, Then all lines are shown and none is cut off.
3. Given I try to open an order of another company, When I request it, Then I see "not found" (`EN-DN-10`).
4. Given the page, When I check it, Then it meets the accessibility baseline (`EN-DN-14`).

##### US-DN-009 See my negotiated prices on an order

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-10`
* (source: BR-12, CS-20, ES-18, C-05)
* Depends on (same track): `US-DN-008`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-41, OPEN-16

**Story.** As a customer user, I want to see my company's negotiated price on each line, not the list price, so that the prices I see match what I agreed with Northwind.

**Facts for the developer.** Order Desk has one pricing service. A negotiated price replaces the list price. Volume discounts and a Gold tier discount may apply on top (CS-20, A-22). The pricing rules must not change, and the 15 pricing tests must pass unchanged (ES-18). The portal calls the same pricing service and does not copy its rules (C-05).

**Acceptance criteria**

1. Given company A has a negotiated price of 8.50 for a product whose list price is 10.00, When I open an order with that product, Then the line shows 8.50 and the list price is not shown.
2. Given a line has no negotiated price, When I open the order, Then the line shows the standard price for that company as the pricing service returns it.
3. Given discounts apply, When I open the order, Then the portal shows the net unit price and the net line and order totals, and no discount breakdown (A-41, **OPEN:** OPEN-16).
4. Given the pricing tests, When they run, Then all pass with the same expected values as before (`EN-DN-02`).

##### US-DN-010 The order detail responds in under 2 seconds

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-10`
* (source: NFR-02, CS-03)
* Depends on (same track): `US-DN-008`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-37, OPEN-08

**Story.** As a customer user, I want an order to open quickly, so that checking an order is faster than phoning (NFR-02).

**Acceptance criteria**

1. Given a test order with 100 lines and 60 users opening orders at the same time (A-37), When pages are requested repeatedly for 10 minutes, Then 95 % of detail responses take under 2 seconds.
2. Given the result, When the test is finished, Then it is recorded with the load used. The measurement basis is **OPEN:** OPEN-08.

##### FT-DN-11 Order status as of the 02:00 batch

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-03`
* (source: BR-04, CS-10, C-03, A-04, A-05, OPEN-01, OPEN-02)
* Description: a customer user sees one of: Received, Confirmed, Picking, Shipped, Delivered, Cancelled. The status is as of the 02:00 batch (A-04). Experiment `MVE-BA02` tests whether this is enough. Its change options are in `FT-DN-26` (unplanned).
* Stories: `US-DN-011`, `US-DN-012`.

##### US-DN-011 See one of six statuses on an order

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-11`
* (source: BR-04, P-03, CS-10, A-05)
* Depends on (same track): `US-DN-008`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-04, A-05, OPEN-01, OPEN-02

**Story.** As a customer user, I want to see the status of each of my orders as one of Received, Confirmed, Picking, Shipped, Delivered or Cancelled, so that I know where my order is without phoning.

**Facts for the developer.** Picking and Shipped are updated once per night by a 02:00 batch with the warehouse system. StockPilot cannot change (CS-10, C-03). Confirmed, Delivered and Cancelled are assumed to be entered by staff by hand (A-05, OPEN-02).

**Acceptance criteria**

1. Given orders in each of the six statuses, When I open "My orders" and an order, Then the status shown is exactly one of the six words, matching the status stored in Order Desk.
2. Given staff change an order to Confirmed during the day, When I reload the page, Then it shows Confirmed.
3. Given an order has no status or an unknown code, When the page is shown, Then the page shows a neutral "unknown" label and does not fail.
4. Given the list and the detail, When a customer opens each, Then the status is shown in both.

##### US-DN-012 Understand how fresh the status is

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-11`
* (source: BR-04, CS-10, C-03, SM-02)
* Depends on (same track): `US-DN-011`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-04, A-05, OPEN-01

**Story.** As a customer user, I want to be told how fresh the status is, so that I do not expect "always up to date" when the warehouse updates only once per night.

**Acceptance criteria**

1. Given I open the status in the list or the detail, When the page is shown, Then a short note says that Picking and Shipped are updated once per night (as of the 02:00 batch, CET), and other statuses change when Northwind staff enter them.
2. Given the note, When a screen reader reads the page, Then the note is read in plain words and is not hidden by a tooltip only.
3. Given the freshness question is not answered (OPEN-01), When the status is shown, Then the note states "as of the 02:00 batch" as agreed in A-04.
4. Given the time zone, When I read the note, Then the note says CET and not UTC.

### EP-DN-04 Reorder and hand-off

* Tags: track-dotnet, dotnet-r2
* Type: Epic | Priority: Must | Status: Draft
* (source: BR-05, BR-06, BR-10, BR-12, NFR-08, C-05)
* Goal: a customer user creates a new order by copying a previous one, and the submitted order reaches Order Desk without re-keying, with every change recorded.
* Contains: `FT-DN-12`, `FT-DN-13`, `FT-DN-14`.

#### FT-DN-12 Reorder by copying

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-04`
* (source: BR-05, BR-12, P-04, CS-16)
* Description: a customer user creates a new order by copying a previous order, changing quantities or removing lines, then submitting. 70 % of orders repeat a previous order with small changes (P-04).
* Stories: `US-DN-013`, `US-DN-014`, `US-DN-015`.

##### US-DN-013 Start a new order by copying a previous order

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-12`
* (source: BR-05, P-04, CS-16)
* Depends on (same track): `EN-DN-06`, `US-DN-008`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-42

**Story.** As a customer user, I want to start a new order by copying one of my company's previous orders, so that I do not have to type the whole list again.

**Facts for the developer.** Copying an existing order copies its lines and quantities, and not prices. Prices are worked out when the order is submitted (A-22). The new order keeps the delivery address of the copied order (A-42).

**Acceptance criteria**

1. Given I am viewing an order of my company, When I choose "Order again", Then a draft order opens with the same products and quantities, and with the delivery address of the copied order.
2. Given I try to copy an order of another company, When I choose "Order again", Then I see "not found" (`EN-DN-10`).
3. Given the draft is open, When I reload the page or my session continues on another server instance, Then the draft is still there (`EN-DN-06`).
4. Given a product in the copied order is no longer sold, When the draft opens, Then that line is shown with a clear note and is not submitted unless I remove it.

##### US-DN-014 Change quantities and remove lines before submitting

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-12`
* (source: BR-05, P-02, P-04)
* Depends on (same track): `US-DN-013`, `EN-DN-10`
* ASSUMPTION / OPEN used: none

**Story.** As a customer user, I want to change quantities and remove lines on the draft order before I submit it, so that the order matches what I need this time.

**Acceptance criteria**

1. Given a draft with 5 lines, When I change a quantity to 12 and save, Then the draft shows 12 for that line.
2. Given I enter a quantity that is zero, negative or not a whole number, When I save, Then I see an error message next to the field and the draft is not changed.
3. Given a draft with several lines, When I remove one, Then it disappears from the draft, and the other lines are unchanged.
4. Given I have removed every line, When I view the draft, Then the submit button is disabled and a message explains that an order needs at least one line.

##### US-DN-015 See my prices on the draft order

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-12`
* (source: BR-12, CS-20, C-05, ES-18)
* Depends on (same track): `US-DN-014`, `US-DN-009`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-22, A-41, OPEN-16

**Story.** As a customer user, I want to see my negotiated prices and the order total on the draft before I submit, so that I know what I am agreeing to.

**Facts for the developer.** Today the draft screen shows no prices. Prices are worked out only when the order is submitted (A-22). The portal shows prices by calling the same pricing service. Pricing rules do not change (CS-20).

**Acceptance criteria**

1. Given a draft, When I view it, Then each line shows my company's net unit price and net line price, and the draft shows the order total, all worked out by the existing pricing service.
2. Given I change a quantity, When the change is saved, Then the line and the total update to the values the pricing service returns for that quantity.
3. Given the price shown on the draft and the price stored when I submit, When I compare them, Then they are equal for the same lines and quantities.
4. Given discounts apply, When I view the draft, Then only net prices are shown (A-41, **OPEN:** OPEN-16).

##### FT-DN-13 Portal order reaches Order Desk

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-04`
* (source: BR-06, BR-10, C-05, A-18)
* Description: a submitted portal order appears in Order Desk as Received, without re-keying. The channel is set to Portal by the server.
* Stories: `US-DN-016`, `US-DN-017`.

##### US-DN-016 Submit the order and see it in Order Desk as Received

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-13`
* (source: BR-06, C-05, P-01, P-02, A-22)
* Depends on (same track): `US-DN-014`, `EN-DN-13`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-22, A-42, OPEN-18, OPEN-20

**Story.** As a customer user, I want to submit my draft order and have it appear in Order Desk as Received, so that Northwind staff do not have to re-key it (BR-06).

**Facts for the developer.** Orders get a number from one sequence, formatted `NW-` plus a seven-digit number. The portal uses the same sequence and the same order tables, with no second order database (C-05, A-22). The same order number is the key StockPilot uses.

**Acceptance criteria**

1. Given a draft with at least one line, When I press "Submit order" once, Then one order is created for my company with status Received, a new order number from the Order Desk sequence, the lines and quantities of the draft, my company's prices worked out by the pricing service, and the delivery address of the draft.
2. Given I press the button twice quickly, When both requests arrive, Then only one order is created.
3. Given I submit, When the order is saved, Then I see a confirmation page with the order number, and the order shows in "My orders".
4. Given an Order Desk clerk opens the order list, When the list loads, Then the new order is there with status Received, with no key-in by staff.
5. Given the submission fails, When the error is returned, Then no partial order is saved, and I see a clear message and my draft is kept.
6. Given a confirmation e-mail is not part of this story (the mail path is **OPEN:** OPEN-18), When I submit, Then the confirmation is on screen only. Given the nightly export, When it runs, Then nothing changes there and no schema change is made (OPEN-20).

##### US-DN-017 The server marks portal orders with the Portal channel

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-13`
* (source: BR-10, A-18, A-22)
* Depends on (same track): `US-DN-016`, `US-DN-001`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-18, A-22

**Story.** As an Order Desk clerk, I want every portal order to carry the channel Portal, set by the server, so that I can trust the channel and filter by it (BR-10).

**Facts for the developer.** The submit action today takes the channel as a parameter, and the order form posts it from a dropdown (A-22). The portal must never accept a channel from the browser.

**Acceptance criteria**

1. Given a customer user submits an order, When the order is saved, Then the stored channel is Portal.
2. Given a request that includes a channel value (for example Phone), When it is sent to the portal submit action, Then the value is ignored and the stored channel is still Portal.
3. Given an order entered by staff, When it is saved, Then its channel is the one the clerk chose, as today.
4. Given the clerk filters by Portal (`US-DN-002`), When the list loads, Then the order is listed.

##### FT-DN-14 Order change audit

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-04`
* (source: NFR-08, CS-05, A-22, OPEN-17, OPEN-22)
* Description: every change to an order records who, what, when and channel, and is kept 7 years.
* Enabler: `EN-DN-13`. Stories: `US-DN-018`, `US-DN-019`.

##### EN-DN-13 Audit completeness

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-14`
* (source: NFR-08, BR-10, CS-05, A-22)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-13`, `FT-DN-14`
* ASSUMPTION / OPEN used: A-22, OPEN-17, OPEN-22

**Story.** As a Customer Operations auditor, I want the audit record of an order to hold the channel on every change and the signed-in user's identity, so that "who, what, when and channel" is complete (NFR-08).

**Facts for the developer.** The audit table has an action, a changed-by value of up to 100 characters, a channel and a time in UTC. The channel is empty on status changes today, and "what" is a free-text action (A-22). There is no retention or delete protection in the application.

**Acceptance criteria**

1. Given any order is created or its status is changed, When the audit row is written, Then it holds the user, the action, the channel of the order and the time in UTC.
2. Given a portal user, When an audit row is written, Then the stored user identity fits in the 100-character field and identifies the user (not only the company).
3. Given the application, When it runs, Then no code deletes or edits audit rows.
4. Given no schema change is needed for points 1 to 3, When the story is built, Then none is made. If one is needed, it goes through a migration-impact check and a decision record (ES-19, OPEN-20).
5. Given field-level detail and 7-year retention sizing are not decided (OPEN-17, OPEN-22), When the story is built, Then this story keeps the free-text action and deletes no rows.

##### US-DN-018 Every order change records who, what, when and channel

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-14`
* (source: NFR-08, BR-10, CS-05)
* Depends on (same track): `EN-DN-13`, `US-DN-016`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-17

**Story.** As a Customer Operations auditor, I want every change to an order recorded with who made it, what changed, when and through which channel, so that I can answer an audit question about any order (NFR-08).

**Acceptance criteria**

1. Given a customer user submits an order, When I read its audit, Then there is a "Created" entry with the customer user, the time and the channel Portal.
2. Given a clerk changes the status from Received to Confirmed, When the change is saved, Then a new entry shows the clerk, the time, "Received to Confirmed" in the action, and the order's channel.
3. Given the nightly job moves an order to Picking or Shipped, When the job finishes, Then an entry shows the system user, the time and the order's channel.
4. Given the audit of an order, When I read it, Then the entries are in time order.
5. Given field-level detail is not decided (OPEN-17), When an entry is written, Then the "what" is the free-text action.

##### US-DN-019 Audit records are kept for 7 years

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-14`
* (source: NFR-08, CS-05)
* Depends on (same track): `EN-DN-13`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-08, OPEN-22

**Story.** As a Customer Operations auditor, I want order audit records kept for 7 years and not deleted by the application, so that I can answer an audit question about an order placed years ago (NFR-08).

**Acceptance criteria**

1. Given the application, When I search its code and scripts, Then nothing deletes or archives audit rows before 7 years.
2. Given an order older than one year, When I read its audit, Then all its entries are present.
3. Given the 7-year size and the retrieval target against RPO and RTO are not defined (OPEN-22), When this story is built, Then this story deletes no audit row and sets no sizing or retrieval target.

### EP-DN-05 Portal quality

* Tags: track-dotnet, dotnet-r2
* Type: Epic | Priority: Must | Status: Draft
* (source: NFR-07, BR-11)
* Goal: the portal meets WCAG 2.2 level AA from the start and is ready to show more than one language.
* Contains: `FT-DN-15`, `FT-DN-16`.

#### FT-DN-15 Language foundation

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Should | Status: Draft | Parent: `EP-DN-05`
* (source: BR-11, A-22, OPEN-27)
* Description: the portal is ready to show more than one language. The pilot language is **OPEN:** OPEN-27 (which language do pilot customers see in `dotnet-r2`, because French and English are planned for `dotnet-r3`).
* Enabler: `EN-DN-12`.

##### EN-DN-12 Localisation scaffold

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Should | Status: Draft | Parent: `FT-DN-15`
* (source: BR-11, A-22)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-15`, `FT-DN-19`, `FT-DN-23`
* ASSUMPTION / OPEN used: A-22, OPEN-27

**Story.** As a developer, I want all portal text read from language resource files, so that adding French, English or Dutch later means adding a file and not changing screens (BR-11).

**Facts for the developer.** There are no language files today. View text is written directly in English (A-22).

**Acceptance criteria**

1. Given a new portal page, When I search it for visible text, Then no text is written directly in the page. It is read from a resource file by key.
2. Given a second resource file with a test language, When I switch to it in a test, Then every portal page shows the test language and none shows missing keys.
3. Given a key is missing in a language, When the page is shown, Then the page falls back to the default language and logs the missing key.
4. Given the pilot language is not decided (OPEN-27), When the portal starts, Then the default language is a setting.

#### FT-DN-16 Accessibility baseline

* Tags: track-dotnet, dotnet-r2
* Type: Feature | Priority: Must | Status: Draft | Parent: `EP-DN-05`
* (source: NFR-07, BR-03, A-13)
* Description: portal pages meet WCAG 2.2 level AA (Web Content Accessibility Guidelines) from the start. The portal is a responsive web site for current browsers (A-13).
* Enabler: `EN-DN-14`. Stories: `US-DN-020`, `US-DN-021`.

##### EN-DN-14 Accessibility baseline (WCAG 2.2 AA)

* Tags: track-dotnet, dotnet-r2
* Type: Enabler | Priority: Must | Status: Draft | Parent: `FT-DN-16`
* (source: NFR-07, A-13)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-09`, `FT-DN-10`, `FT-DN-11`, `FT-DN-12`, `FT-DN-13`, `FT-DN-16`
* ASSUMPTION / OPEN used: A-13, OPEN-10

**Story.** As a developer, I want a shared portal layout and form components that already meet WCAG 2.2 level AA, so that each new page is accessible by default (NFR-07).

**Acceptance criteria**

1. Given the shared layout, When I open any portal page, Then it has page landmarks (header, navigation, main content, footer), a "skip to content" link, a page title and a visible focus marker.
2. Given a form component, When I read its markup, Then each field has a label tied to it, and error messages are tied to the field they describe.
3. Given the pipeline, When it runs on a change to a portal page, Then an automated accessibility check runs on every portal page and fails the build on an error at level AA.
4. Given the pages, When the pages are viewed in a narrow browser window, Then they adapt to it without horizontal scrolling at 320 px width (A-13). Mobile expectations are **OPEN:** OPEN-10.

##### US-DN-020 Use the portal with keyboard and screen reader

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-16`
* (source: NFR-07, BR-03)
* Depends on (same track): `US-DN-006`, `US-DN-008`, `US-DN-014`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-13

**Story.** As a customer user who cannot use a mouse or who uses a screen reader, I want to sign in, find an order, copy it and submit it with only the keyboard, so that I can use the portal like anyone else (NFR-07).

**Acceptance criteria**

1. Given only a keyboard, When I go through sign-in, the order list, an order, "Order again", editing the draft and submit, Then every control can be reached and used, in a logical order, and the focus is always visible.
2. Given a screen reader, When I open the order list, Then each order's number, date, status and total are read in a sensible order, and the table has headers.
3. Given an error or a confirmation message, When it appears, Then a screen reader announces it without moving the focus unexpectedly.

##### US-DN-021 Read the portal with enough contrast, zoom and clear errors

* Tags: track-dotnet, dotnet-r2
* Type: Story | Priority: Must | Status: Draft | Parent: `FT-DN-16`
* (source: NFR-07)
* Depends on (same track): `US-DN-020`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-13

**Story.** As a customer user with low vision, I want enough colour contrast, text that can be enlarged, and clear error messages, so that I can read and use every portal page (NFR-07).

**Acceptance criteria**

1. Given any portal page, When checked for contrast, Then normal text has a contrast ratio of at least 4.5 to 1 against its background (WCAG 2.2 level AA).
2. Given the browser zoom is 200 %, When I use any page, Then all content and functions are still available with no loss and no overlap.
3. Given a status is shown with colour, When I read it, Then it is also shown in words.
4. Given the WCAG 2.2 level AA checklist, When the manual check is done on the list, detail, draft and submit pages, Then each item passes, and any failure is recorded as a new story with the next free `US-DN-` number.

### EP-DN-06 Self-service extras

* Tags: track-dotnet, dotnet-r3
* Type: Epic | Priority: Should | Status: Draft
* (source: BR-07, BR-08, BR-11)
* Goal: customers can download invoices, customer administrators can manage their own users, and the portal speaks French and English.
* Contains: `FT-DN-17`, `FT-DN-18`, `FT-DN-19`.
* Cross-track **OPEN:** items stated for this release: OPEN-06, OPEN-19.

#### FT-DN-17 Invoice download

* Tags: track-dotnet, dotnet-r3
* Type: Feature | Priority: Should | Status: Draft | Parent: `EP-DN-06`
* (source: BR-07, P-05, CS-08, CS-11, CS-14, OPEN-06, OPEN-09)
* Description: a customer user can download the PDF invoice of a delivered order. Staff handle about 120 invoice copy requests per week today (P-05).
* Stories: `US-DN-022`, `US-DN-023`.

##### US-DN-022 Download the PDF invoice of a delivered order

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-17`
* (source: BR-07, P-05, CS-11, CS-14, A-22)
* Depends on (same track): `EN-DN-07`, `EN-DN-10`, `US-DN-008`
* ASSUMPTION / OPEN used: A-22, OPEN-06, OPEN-09

**Story.** As a customer user, I want to download the PDF invoice of a delivered order of my company, so that I do not have to ask Northwind staff for a copy (BR-07).

**Facts for the developer.** Invoice files are named `{invoiceNumber}.pdf` in a folder per year. The order record has an invoice number field that may be empty. The year used for the folder is the order year today, which may differ from the invoice year (CS-11, A-22, OPEN-09). Invoices are read through the storage setting from `EN-DN-07`.

**Acceptance criteria**

1. Given a Delivered order of my company that has an invoice number and a file in the store, When I choose "Download invoice", Then the PDF downloads, and its file name includes the invoice number.
2. Given an order of another company, When I request its invoice by changing the address, Then I see "not found" and no file is sent (`EN-DN-10`).
3. Given the order is not Delivered or has no invoice number, When I open its detail, Then there is no download button (see `US-DN-023`).
4. Given where the finance system writes new invoices and the year rule are not agreed (OPEN-06, OPEN-09), When invoices are read, Then this story reads through the storage setting and assumes nothing about where Finance writes.

##### US-DN-023 Clear message when an invoice is not available

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-17`
* (source: BR-07, P-05)
* Depends on (same track): `US-DN-022`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-09

**Story.** As a customer user, I want a clear message when an invoice is not available yet, so that I know whether to wait or to ask Northwind.

**Acceptance criteria**

1. Given an order that is not Delivered, When I open its detail, Then a note says an invoice is available once the order is delivered.
2. Given a Delivered order whose invoice file cannot be found, When I open its detail, Then I see a message that the invoice is not available and how to ask for a copy, and the problem is logged for staff.
3. Given the message, When I read it, Then it is in plain words and does not show file paths or system names.

#### FT-DN-18 Customer administrator

* Tags: track-dotnet, dotnet-r3
* Type: Feature | Priority: Should | Status: Draft | Parent: `EP-DN-06`
* (source: BR-08, OQ-03, OPEN-15)
* Description: a customer administrator can invite and remove users of their own company. Whether administrators exist for all customers or only large ones is **OPEN:** OPEN-15.
* Stories: `US-DN-024`, `US-DN-025`.

##### US-DN-024 Customer administrator invites a user

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-18`
* (source: BR-08, OQ-03, NFR-04)
* Depends on (same track): `US-DN-004`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-15, OPEN-33

**Story.** As a customer administrator, I want to invite a colleague by e-mail to use the portal for my company, so that they can see our orders without calling Northwind.

**Acceptance criteria**

1. Given I am signed in as an administrator of company A, When I enter a colleague's e-mail address and send the invitation, Then the colleague receives an invitation, and when they accept, they have an account tied to company A only.
2. Given I am not an administrator, When I open the portal, Then I do not see the invitation page, and a direct request is refused.
3. Given an invalid e-mail address, When I send the invitation, Then I see a clear error and no invitation is sent.
4. Given the invited user signs in, When the sign-in starts, Then they use the same customer sign-in as every other user (NFR-04).
5. Given the invitation is for another company, When I try to create it, Then it cannot be created (`EN-DN-10`).
6. Given which customers have administrators is not decided (OPEN-15), When an administrator is set, Then administrators are set by Northwind staff for any customer, and no rule limits it to large customers.

##### US-DN-025 Customer administrator removes a user

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-18`
* (source: BR-08, OQ-03)
* Depends on (same track): `US-DN-024`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-15

**Story.** As a customer administrator, I want to remove a user of my company, so that a person who has left no longer sees our orders.

**Acceptance criteria**

1. Given a user of company A, When I remove them, Then they can no longer sign in to company A's data, and their active session ends at the next request.
2. Given a user of another company, When I look for them, Then I cannot see or remove them.
3. Given I try to remove the last administrator of my company, When I confirm, Then I see a message and it is not removed.
4. Given a user is removed, When I read the audit history of orders they placed, Then it stays unchanged (NFR-08).

#### FT-DN-19 French and English

* Tags: track-dotnet, dotnet-r3
* Type: Feature | Priority: Should | Status: Draft | Parent: `EP-DN-06`
* (source: BR-11, OQ-02, OPEN-14)
* Description: the portal is available in French and English. Dutch is unplanned (OPEN-14, `FT-DN-23`).
* Stories: `US-DN-026`, `US-DN-027`.

##### US-DN-026 Use the portal in French or English

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-19`
* (source: BR-11, OQ-02)
* Depends on (same track): `EN-DN-12`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-14

**Story.** As a customer user in France or Belgium, I want to use the portal in French or in English, so that I can work in the language of my business.

**Acceptance criteria**

1. Given I choose French, When I open any portal page, Then all text, dates and numbers appear in French, including the status words, buttons and error messages.
2. Given I choose English, When the page reloads, Then everything appears in English.
3. Given a resource key is missing in French, When the page is shown, Then the page shows the English text and the missing key is logged.
4. Given the translations, When the release is prepared, Then they are reviewed by a French-speaking Northwind employee before release.

##### US-DN-027 The portal remembers my language

* Tags: track-dotnet, dotnet-r3
* Type: Story | Priority: Should | Status: Draft | Parent: `FT-DN-19`
* (source: BR-11, OQ-02)
* Depends on (same track): `US-DN-026`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-14

**Story.** As a customer user, I want the portal to remember my language, so that I do not choose it at every visit.

**Acceptance criteria**

1. Given I have never chosen a language, When I first open the portal, Then it uses French if my browser language is French and English otherwise.
2. Given I choose a language, When I sign in again later, Then the portal shows that language.
3. Given I change the language, When the change is saved, Then the page I am on reloads in the new language and I am not signed out.

### EP-DN-07 Notifications and measures

* Tags: track-dotnet, dotnet-r4
* Type: Epic | Priority: Could | Status: Draft
* (source: BR-09, SM-01, SM-02, SM-03, SM-04)
* Goal: customers receive an e-mail when an order is shipped, and the success measures SM-01 to SM-04 are measured against their baselines.
* Contains: `FT-DN-20`, `FT-DN-21`, `FT-DN-22`.
* Cross-track **OPEN:** items stated for this release: OPEN-18, OPEN-20. Other: OPEN-05.

#### FT-DN-20 Keep shipment date and carrier

* Tags: track-dotnet, dotnet-r4
* Type: Feature | Priority: Could | Status: Draft | Parent: `EP-DN-07`
* (source: BR-09, CS-10, A-20, OPEN-20)
* Description: the shipment date and carrier that StockPilot sends are stored, so they can be shown and used.
* Enabler: `EN-DN-15`.

##### EN-DN-15 Store shipment date and carrier

* Tags: track-dotnet, dotnet-r4
* Type: Enabler | Priority: Could | Status: Draft | Parent: `FT-DN-20`
* (source: BR-09, CS-10, C-03, ES-19, A-20, A-22)
* Depends on (same track): `EN-DN-01`
* Enables: `FT-DN-20`, `FT-DN-21`
* ASSUMPTION / OPEN used: A-20, A-22, OPEN-20

**Story.** As a developer, I want the shipment date and carrier from the shipment update to be stored on the order, so that the shipped e-mail can show them (BR-09).

**Facts for the developer.** StockPilot sends `OrderNumber;ShippedAt;Carrier` in a shipment file. The import reads `ShippedAt` and `Carrier` but does not keep them (A-22, A-20).

**Acceptance criteria**

1. Given sample shipment rows with a shipped date and a carrier, When the new store method processes them in a test, Then both values are stored on the matching order and can be read back.
2. Given existing orders, When the new fields are added, Then their stored values stay empty and nothing fails.
3. Given a change to the database is needed, When the change is planned, Then a migration-impact check and a decision record are written first (ES-19).
4. Given the exchange files, When the new fields are stored, Then their format does not change (C-03).
5. Given how the nightly job passes these values is a question for the exchange owner (OPEN-20), When the story is built, Then this story adds the storage and a tested method, and assumes the exchange files stay as they are.

#### FT-DN-21 Shipped e-mail

* Tags: track-dotnet, dotnet-r4
* Type: Feature | Priority: Could | Status: Draft | Parent: `EP-DN-07`
* (source: BR-09, CS-10, CS-12, OPEN-18)
* Description: a customer user receives an e-mail when an order changes to Shipped.
* Stories: `US-DN-028`, `US-DN-029`.

##### US-DN-028 Receive an e-mail when my order is shipped

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-21`
* (source: BR-09, CS-10, CS-12, A-20)
* Depends on (same track): `EN-DN-15`, `US-DN-011`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-20, OPEN-18

**Story.** As a customer user, I want to receive an e-mail when one of my orders changes to Shipped, so that I know it is on its way without checking the portal.

**Acceptance criteria**

1. Given an order of company A changes to Shipped, When the change is saved, Then a message is prepared with the order number, the shipped date and the carrier, in the user's chosen language (or the default language).
2. Given the message, When it is sent, Then it is handed to the mail sending service, and the result (sent or failed) is logged.
3. Given no mail path is named yet (OPEN-18), When the story is built, Then this story prepares the content and the hand-off and BR-09 is recorded as partly covered until a mail path exists.
4. Given the message, When I read it, Then it contains no price, no address and no invoice data.

##### US-DN-029 The shipped e-mail is sent once and only to my company

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-21`
* (source: BR-09, NFR-03, A-22)
* Depends on (same track): `US-DN-028`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-19, A-22, OPEN-18

**Story.** As a customer user, I want the shipped e-mail sent once per order and only to the users of my company, so that I am not sent duplicates and nobody outside my company gets my order data.

**Facts for the developer.** The nightly import can write repeated "Shipped" rows for the same order (A-19, A-22). The e-mail must not repeat because of that.

**Acceptance criteria**

1. Given an order changes to Shipped, and the same shipment row is processed again, When the second row is processed, Then only one e-mail has been sent for that order.
2. Given the order belongs to company A, When the e-mail is sent, Then it goes only to users of company A who are set to receive it.
3. Given the mail service, When the message is sent, Then it keeps data in the EU (NFR-03).
4. Given the e-mail fails to send, When the failure is detected, Then it is retried a limited number of times and then logged as failed, and the order status is not affected.

#### FT-DN-22 Measure the success measures

* Tags: track-dotnet, dotnet-r4
* Type: Feature | Priority: Could | Status: Draft | Parent: `EP-DN-07`
* (source: SM-01, SM-02, SM-03, SM-04, OPEN-05)
* Description: SM-01 to SM-04 are measured against their baselines. "Portal launch" is not defined (OPEN-05).
* Stories: `US-DN-030`, `US-DN-031`, `US-DN-032`, `US-DN-033`.

##### US-DN-030 Measure SM-01: share of orders placed through the portal

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-22`
* (source: SM-01, BR-10)
* Depends on (same track): `US-DN-017`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-05, OPEN-31

**Story.** As a Customer Operations manager, I want to see the share of orders placed through the portal each week, so that I can compare it with the target of 35 % six months after portal launch (baseline 0 %).

**Acceptance criteria**

1. Given a chosen week, When I run the report, Then it shows orders with the channel Portal, all orders, and the share as a percentage, from Order Desk data.
2. Given the report, When I read it, Then it shows the baseline (0 %) and the target (35 %, 6 months after portal launch) next to the result.
3. Given "portal launch" is not defined (OPEN-05), When the report runs, Then the report takes the launch date as a setting.

##### US-DN-031 Measure SM-02: "where is my order?" calls per week

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-22`
* (source: SM-02, P-03)
* Depends on (same track): `US-DN-011`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-33, OPEN-28, OPEN-31

**Story.** As a Customer Operations manager, I want to see the number of "where is my order?" calls per week against the baseline of 410 and the target of 250 or fewer, so that I know whether the portal status view works.

**Acceptance criteria**

1. Given a week, When I run the report, Then it shows the number of such calls, the baseline (410) and the target (250 or fewer, 6 months after portal launch).
2. Given a call is counted when a customer phones or e-mails to ask for the status or timing of an existing order (A-33), When I read the report, Then the report states this definition.
3. Given where the call numbers come from is not yet agreed (OPEN-28, OPEN-31), When the report runs, Then the report names its data source in the result.

##### US-DN-032 Measure SM-03: order lines needing correction

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-22`
* (source: SM-03, P-02)
* Depends on (same track): `US-DN-016`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-31

**Story.** As a Customer Operations manager, I want to see the share of order lines needing correction after entry against the baseline of 4.1 % and the target of 2.5 % or fewer, so that I know whether portal orders reduce re-keying errors.

**Acceptance criteria**

1. Given a period, When I run the report, Then it shows the share of order lines that were corrected after entry, split by channel (portal and staff-entered), with the baseline (4.1 %) and target (2.5 % or fewer, 6 months after portal launch).
2. Given no record of "corrected after entry" exists in the documents, When the report runs, Then the report names the data it uses and the definition of a correction (**OPEN:** OPEN-31).

##### US-DN-033 Measure SM-04: invoice copy requests handled by staff

* Tags: track-dotnet, dotnet-r4
* Type: Story | Priority: Could | Status: Draft | Parent: `FT-DN-22`
* (source: SM-04, P-05)
* Depends on (same track): `US-DN-022`, `EN-DN-10`
* ASSUMPTION / OPEN used: OPEN-05, OPEN-31

**Story.** As a Customer Operations manager, I want to see invoice copy requests handled by staff per week against the baseline of 120 and the target of 40 or fewer, so that I know whether invoice download works.

**Acceptance criteria**

1. Given a week, When I run the report, Then it shows the number of invoice copy requests handled by staff, the number of portal invoice downloads, the baseline (120) and the target (40 or fewer, 6 months after portal launch).
2. Given where the count of staff-handled requests comes from is not yet agreed (OPEN-31), When the report runs, Then the report names its source.
3. Given "portal launch" is not defined (OPEN-05), When the report runs, Then the launch date is a setting.

### EP-DN-08 Unplanned candidates (not in a release)

* Tags: track-dotnet
* Type: Epic | Priority: Should (provisional, A-36) | Status: Draft
* (source: BR-11, NFR-08, BR-04, OQ-02)
* Goal: hold candidate items that are not planned because a decision or a result is missing. Each has only the track tag. If the product owner plans one, the epic or feature, its children and their tags change together (A-35). The name `EP-DN-08` is a proposal (A-26).
* Contains: `FT-DN-23`, `FT-DN-24`, `FT-DN-25`, `FT-DN-26`.

#### FT-DN-23 Dutch language

* Tags: track-dotnet
* Type: Feature | Priority: Should (provisional, A-36) | Status: Draft | Parent: `EP-DN-08`
* (source: BR-11, OQ-02, OPEN-14)
* Description: Dutch text in the portal. Not planned because **OPEN:** OPEN-14 asks whether Dutch is needed in the first release.
* Story: `US-DN-034`.

##### US-DN-034 Use the portal in Dutch

* Tags: track-dotnet
* Type: Story | Priority: Should (provisional, A-36) | Status: Draft | Parent: `FT-DN-23`
* (source: BR-11, OQ-02)
* Depends on (same track): `EN-DN-12`, `US-DN-026`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-36, OPEN-14

**Story.** As a customer user in Belgium, I want to use the portal in Dutch, so that I can work in my own language.

**Acceptance criteria**

1. Given I choose Dutch, When I open any portal page, Then all text, dates and numbers appear in Dutch, including statuses, buttons and error messages.
2. Given a key is missing in Dutch, When the page is shown, Then the page shows the default language and the missing key is logged.
3. Given the translations, When the release is prepared, Then a Dutch-speaking Northwind employee reviews them before release.

#### FT-DN-24 Field-level order audit

* Tags: track-dotnet
* Type: Feature | Priority: Could (provisional, A-36) | Status: Draft | Parent: `EP-DN-08`
* (source: NFR-08, A-22, OPEN-17)
* Description: record which field changed in an order. Not planned because **OPEN:** OPEN-17 asks whether the free-text audit action is enough for NFR-08.
* Story: `US-DN-035`.

##### US-DN-035 See which field changed in an order

* Tags: track-dotnet
* Type: Story | Priority: Could (provisional, A-36) | Status: Draft | Parent: `FT-DN-24`
* (source: NFR-08, A-22)
* Depends on (same track): `US-DN-018`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-36, OPEN-17

**Story.** As a Customer Operations auditor, I want the audit record to show which field of an order changed, with the old and new value, so that I can answer detailed audit questions (NFR-08).

**Acceptance criteria**

1. Given a staff member changes the quantity of a line from 10 to 12 (once order editing exists), When I read the audit, Then it shows the field "quantity", the old value 10, the new value 12, who, when and the channel.
2. Given a change to an order's status, When I read the audit, Then the audit shows the field "status" with old and new values.
3. Given any schema change is needed, When the change is planned, Then a migration-impact check and a decision record come first (ES-19, OPEN-20).

#### FT-DN-25 Order Desk API for reuse

* Tags: track-dotnet
* Type: Feature | Priority: Could (provisional, A-36) | Status: Draft | Parent: `EP-DN-08`
* (source: none in knowledge-docs in scope; OPEN-24, informational)
* Description: a programming interface that other systems could use. Informational only: BA-03 will need one, and BA-03 is out of scope. **No story is written** and no release depends on it (OPEN-24).

#### FT-DN-26 Status clarity options (only if `MVE-BA02` says pivot)

* Tags: track-dotnet
* Type: Feature | Priority: Should (provisional, A-36) | Status: Draft | Parent: `EP-DN-08`
* (source: BR-04, CS-10, SM-02, A-04)
* Description: if the result of experiment `MVE-BA02` is **pivot**, `FT-DN-11` stays and these stories are added: show the time each status last changed, and explain Picking and Shipped in plain words. Until the result is known they are unplanned (A-35). If it is **persevere**, they are dropped or kept unplanned. If it is **stop**, Lena Varga and Marc Dubois decide whether the portal pilot leads with status or with reorder, and the question goes to OPEN-01 and OPEN-20.
* Stories: `US-DN-036`, `US-DN-037`.

##### US-DN-036 See when each status last changed

* Tags: track-dotnet
* Type: Story | Priority: Should (provisional, A-36) | Status: Draft | Parent: `FT-DN-26`
* (source: BR-04, CS-10, SM-02, A-04)
* Depends on (same track): `US-DN-011`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-04, A-35, A-36, OPEN-01, OPEN-26

**Story.** As a customer user, I want to see the date and time each status of my order last changed, so that I can judge how current the status is.

**Acceptance criteria**

1. Given an order has moved from Received to Confirmed to Picking, When I open its detail, Then I see each status reached with its date and time in CET.
2. Given an order whose status history is incomplete, When I open its detail, Then the entries that exist are shown and no entry is invented.
3. Given the times, When I read them, Then they come from the order's audit record and are shown in CET, not UTC.
4. Given Picking and Shipped are updated only by the nightly 02:00 batch (A-04), When I read the status history, Then the page states that these two statuses are as of the 02:00 batch.

##### US-DN-037 Read Picking and Shipped in plain words

* Tags: track-dotnet
* Type: Story | Priority: Should (provisional, A-36) | Status: Draft | Parent: `FT-DN-26`
* (source: BR-04, CS-10, SM-02)
* Depends on (same track): `US-DN-011`, `EN-DN-10`
* ASSUMPTION / OPEN used: A-04, A-35, A-36, OPEN-01

**Story.** As a customer user, I want a short plain-word explanation next to Picking and Shipped, so that I understand what each means for my delivery.

**Acceptance criteria**

1. Given an order is in Picking, When I see its status, Then a short sentence explains that the warehouse is preparing the order.
2. Given an order is Shipped, When I open its detail, Then a short sentence explains that the order has left the warehouse.
3. Given the sentences, When I read them, Then they are in the chosen language, can be read by a screen reader, and are approved by Lena Varga before release.
4. Given Picking and Shipped are updated only by the nightly 02:00 batch (A-04), When I read the explanation, Then the page states that these two statuses are as of the 02:00 batch.

## 8. Cross-track dependencies (all OPEN, none a prerequisite)

No item and no release waits for the other track (ES-31). Each cross-track **OPEN:** item is stated in the releases that touch it. For every one, the table says what each track does **without** the answer. That position is an **ASSUMPTION:** (A-28). The items named are the ones whose text states the position.

| OPEN item | `track-azure` items | What the Azure track does without the answer | `track-dotnet` items | What the .NET track does without the answer |
|---|---|---|---|---|
| OPEN-01 Acceptable freshness for BR-04 (nightly?) | `US-AZ-005`, `EN-AZ-09`, `US-AZ-012` | Keeps the nightly 02:00 cadence and builds no faster refresh. | `US-DN-011`, `US-DN-012`, `US-DN-036`, `US-DN-037` | Shows status "as of the 02:00 batch" (A-04). |
| OPEN-03 Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | `EN-AZ-13`, `US-AZ-013` | Plans the cutover for Order Desk as it exists on the day, lists each point that breaks on the new platform, and changes no application code. | `EN-DN-01`, `EN-DN-08` | Does the Order Desk code modernisation itself (A-03). |
| OPEN-04 Accountable owner and split of the EUR 1,500 ceiling | `EN-AZ-03`, `EN-AZ-12`, `US-AZ-004`, `US-AZ-015`, `US-AZ-017` | Reports the cost of the whole platform and applies no split. | `EP-DN-01`, `EP-DN-02` | Reports the hosting cost of the portal and applies no split. |
| OPEN-05 Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | `EN-AZ-13` | Delivers `tst` and `prd` only and plans no pilot environment. | `US-DN-030`, `US-DN-033` | Builds to run in any environment that meets ES-20 and ES-25, and takes the launch date as a setting. |
| OPEN-06 How finance invoice output reaches Azure; where Order Desk reads it | `EN-AZ-10`, `US-AZ-011`, `US-AZ-016` | Moves the existing PDFs and changes nothing in the finance system. | `EN-DN-07`, `US-DN-022` | Reads invoices through a storage setting and assumes nothing about where Finance writes. |
| OPEN-12 NWFS01 operating system and whether it counts in SM-07 | `EN-AZ-13`, `US-AZ-015`, `US-AZ-016` | Retires `NWWEB01` and `NWSQL01` and reports SM-07 with and without `NWFS01`. | none | none |
| OPEN-13 Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | none (no Azure story for NFR-04, A-02) | Builds no sign-in plumbing. | `EN-DN-11`, `EN-DN-08`, `US-DN-004` | Compares the options in the decision record (`EN-DN-11`), checks price and limits (OPEN-25), and starts customer sign-in once the choice is recorded. Other features do not wait. |
| OPEN-18 SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | `EN-AZ-11` | Replaces the relay for the e-mail that CS-12 describes today and covers no new e-mail. | `US-DN-016`, `US-DN-028`, `US-DN-029` | Prepares the message content and the hand-off. BR-09 stays "partly covered" until a mail path is named. |
| OPEN-19 Hosting and database target the portal and modernised app run on (instance count, session state) | `EN-AZ-03` | Names the setup it assumes in the decision record. | `EN-DN-05`, `EN-DN-06`, `EN-DN-11` | Uses draft handling that works on one or several instances. |
| OPEN-20 StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | `US-AZ-002`, `US-AZ-005`, `EN-AZ-09`, `US-AZ-012` | Keeps the exchange files, cadence and paths identical and assumes no schema change. | `US-DN-016`, `EN-DN-13`, `EN-DN-15`, `US-DN-035` | Plans no schema change. Any change goes through a migration-impact check and a decision record (ES-19). |
| OPEN-21 CI/CD ownership: build and test pipeline vs deployment pipeline | `EN-AZ-07` | Covers the infrastructure pipeline only. | `EN-DN-09` | Covers the build and test pipeline only. |
| OPEN-22 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | `EN-AZ-06`, `US-AZ-009`, `US-AZ-018` | Backs up audit data on the same schedule as other order data and sets no retrieval target. | `EN-DN-13`, `US-DN-019` | Deletes no audit rows and sets no sizing or retrieval target. |
| OPEN-23 Time zone and clock for batch times, order dates, audit | `EN-AZ-05`, `US-AZ-007`, `EN-AZ-08`, `EN-AZ-09`, `US-AZ-012`, `US-AZ-014` | Keeps CET meaning for batch times and states the time zone in each item (A-10). | `US-DN-012`, `US-DN-036` | Shows times in CET and states it. |

Releases and the cross-track OPEN items each states (from the plan): `azure-r1` OPEN-03, 04, 05, 13, 19, 21; `azure-r2` OPEN-01, 03, 04, 05, 06, 18, 19, 20, 22, 23; `azure-r3` OPEN-04, 12; `dotnet-r1` OPEN-03, 04, 19, 21, 23; `dotnet-r2` OPEN-01, 03, 04, 05, 13, 19, 20, 22; `dotnet-r3` OPEN-06, 19; `dotnet-r4` OPEN-18, 20.

## 9. Assumptions (ES-03)

Every assumption has a person who can confirm it. Wording is identical in every product document. The master register is in `docs/product/README.md`. Only the assumptions used in this document are listed.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-05 | Confirmed, Delivered and Cancelled are manual staff actions today | Order Desk team via Lena Varga |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-09 | The cost model assumes SQL and private endpoints are the main spend | Ahmed Benali |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali |
| A-11 | NFR-01 covers the Order Desk and the portal; availability is measured by a probe | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-13 | The portal is a responsive web site for current browsers (mobile via browser) | Sofie Peeters, Ahmed Benali |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-17 | Move items without a BR or NFR (SMTP relay CS-12, invoice share CS-08/CS-11, monitoring CS-22, DR CS-23, pipeline CS-19) are enabler stories tagged by track | Lena Varga |
| A-18 | BR-10 stories are small: show the channel, filter by it, and set the Portal channel on the server | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-20 | `ShippedAt` and `Carrier` must be stored for BR-09 | Ahmed Benali |
| A-21 | Entra External ID pricing and limits, and .NET 10 on Azure App Service, are not verified | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali |
| A-26 | The feature IDs `FT-AZ-01`..`FT-AZ-11` and `FT-DN-01`..`FT-DN-25` in PRD section 5 are the baseline for `backlog.md`. The backlog reuses them, may add new numbers, and never renumbers. The unplanned parent epic `EP-DN-08` is a proposed name | Lena Varga |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-30 | The owner of `MVE-BA01` is Ahmed Benali and the owner of `MVE-BA02` is Lena Varga. The owner runs the test, records the result and proposes the decision. The product owner agrees any change to the backlog | Lena Varga |
| A-32 | The format of the exchange files is taken from reading `database/003-stockpilot-exchange.sql` and from how the command-line tool normally behaves, not from a real file. Assumed: the order file uses `;` as separator, has no header row, does not put quotes around values, uses the database server's default character set, and has no defined row order. The shipment file has a header row and `;` as separator. Real files from Antwerp may differ | Ahmed Benali |
| A-33 | "Where is my order?" calls are unevenly spread across customers, so a group of about 10 heavier callers gives a baseline that can be measured. Most of these calls ask whether an order was received, picked or shipped. The call reasons are not recorded in the business case | Lena Varga |
| A-35 | The two status options in `FT-DN-26` (show the time each status last changed; explain Picking and Shipped in plain words) come from the pivot outcome of `MVE-BA02`. They are unplanned until the result is known. If the product owner plans them, the feature and its stories take the same track tag and the same release tag together (for example `dotnet-r2`) | Lena Varga |
| A-36 | The priorities of unplanned items are provisional: Dutch (BR-11) Should, field-level audit Could, status options Should, Order Desk API Could. The epic `EP-DN-08` takes the highest of them | Lena Varga |
| A-37 | Test figures not given in the business case. NFR-02 is tested with 60 users at once (the staff peak, CS-03), a test company with about 500 orders in 24 months, a test order with 100 lines, 20 orders per page, over 10 minutes. NFR-01 uses a probe about every 5 minutes, an alert after two failed checks in a row, and a calendar-week measurement (84 business hours, about 25 minutes of downtime allowed at 99.5 %) | Lena Varga, Ahmed Benali |
| A-38 | The cutover has a go/no-go point at 09:00 CET, the rollback must finish before 12:00 CET, the cutover and rollback leave at least 30 minutes spare, and the data check takes under 30 minutes. These are planning figures inside the Sunday window of 06:00 to 12:00 CET (CS-21) | Ahmed Benali |
| A-39 | Resource abbreviations in names (for example `rg`, `kv`, `app`) follow the Microsoft Cloud Adoption Framework abbreviation list. ES-23 gives the pattern and one example, not a list | Ahmed Benali |
| A-40 | ASP.NET MVC 5 does not run on .NET 10, so the `Web` project moves to ASP.NET Core MVC with the same routes, screens and behaviour. The project boundaries stay as they are (ES-13) | Ahmed Benali |
| A-41 | Until OPEN-16 is answered, the portal shows each customer's net unit price and the net line and order totals, and no discount breakdown | Lena Varga |
| A-42 | A reorder keeps the delivery address of the copied order. Changing the address in the portal is not part of the pilot | Lena Varga |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |
| A-45 | The cost "at risk" threshold is EUR 1,350 per month, 10 % under the EUR 1,500 ceiling (C-04). A full option above it is flagged "at risk" | Lena Varga, Ahmed Benali |

## 10. OPEN items (ES-04)

Wording is identical in every product document. None blocks this document. Only the OPEN items used in this document are listed.

| ID | OPEN question or dependency | Person who can answer | Track(s) affected |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) |
| OPEN-02 | Source of Confirmed, Delivered, Cancelled status | Lena Varga with the Order Desk team | .NET |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET |
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | Azure |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET |
| OPEN-09 | 24 months of orders exist; where `Orders.InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | .NET |
| OPEN-10 | Data-protection requirement for customer users (Ahmed Benali); mobile expectations (Sofie Peeters) | Ahmed Benali, Sofie Peeters | .NET |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET |
| OPEN-14 | Dutch in the first release (business case OQ-02) | Sofie Peeters with Lena Varga | .NET |
| OPEN-15 | Customer administrators for all customers or only large ones (business case OQ-03) | Lena Varga | .NET |
| OPEN-16 | Show volume and Gold discounts to customers, or only the net price | Lena Varga | .NET |
| OPEN-17 | Is the free-text audit action enough for NFR-08 or are field-level changes needed | Lena Varga | .NET |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Azure and .NET |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET |
| OPEN-24 | Informational, BA-03: BA-03 will need an Order Desk API. BA-03 is out of scope; no release depends on it | Ahmed Benali | Informational only (neither track) |
| OPEN-25 | Verify Entra External ID pricing and .NET 10 on App Service | Ahmed Benali | .NET |
| OPEN-26 | Split `dotnet-r2` into a read-only slice and a reorder slice? | Lena Varga | .NET |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET |
| OPEN-28 | Are "where is my order?" calls already counted by customer and by week (phone system or Order Desk records)? If not, who keeps the 4-week tally for `MVE-BA02`? | Lena Varga | .NET |
| OPEN-29 | Which about 10 customers take part in `MVE-BA02`, who approves contacting them, and is a data-protection or consent step needed before sending a trial status e-mail? | Lena Varga with Sofie Peeters; data-protection check by Ahmed Benali | .NET |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | Azure |
| OPEN-31 | Where do the numbers for SM-02, SM-03 and SM-04 come from (call tally, "order line corrected after entry", invoice requests handled by staff), and how is a correction defined? The business case gives baselines but no record | Lena Varga | .NET |
| OPEN-32 | Which EU secondary region, if any, is used for disaster recovery and EU-resident copies (ES-20, NFR-03)? | Ahmed Benali | Azure |
| OPEN-33 | How do the first customer users get an account and a link to their company in `dotnet-r2`, before the customer administrator feature (`dotnet-r3`) exists? Option: Northwind staff or IT create and link the accounts for the 20 pilot customers | Lena Varga with Ahmed Benali | .NET |

## 11. Machine-friendly register

This register lists every item once, for the traceability and release documents to be generated from it. It follows these rules:

* One row per item: 133 rows (47 Azure and 86 .NET). Columns are exactly `ID | Type | Parent | Title | Track tag | Release tag | Priority | Sources`.
* Rows are grouped by track. Inside a track, epics come first, then features, then enablers and stories in the ranked order of section 4. The `Parent` column gives the hierarchy. A release tag of `-` means unplanned (track tag only).
* `Priority` is Must, Should or Could. The priorities of the unplanned items are provisional (A-36).
* `Sources` lists the knowledge-docs identifiers (`BR-`, `NFR-`, `C-`, `CS-`, `ES-`, `SM-`, `P-`, `OQ-`) from each item's `(source: ...)` line. The assumptions and OPEN items an item uses are in the item itself.

| ID | Type | Parent | Title | Track tag | Release tag | Priority | Sources |
|---|---|---|---|---|---|---|---|
| `EP-AZ-01` | Epic | - | Foundation and proof | `track-azure` | `azure-r1` | Must | C-01, C-03, C-04, NFR-01, NFR-03, NFR-05, CS-10 |
| `EP-AZ-02` | Epic | - | Production cutover | `track-azure` | `azure-r2` | Must | BR-13, C-01, C-03, NFR-01, NFR-03, NFR-05, NFR-06 |
| `EP-AZ-03` | Epic | - | Stabilise and decommission | `track-azure` | `azure-r3` | Must | SM-07, C-04, NFR-06 |
| `FT-AZ-01` | Feature | `EP-AZ-01` | Azure foundation and network | `track-azure` | `azure-r1` | Must | C-01, NFR-03, CS-09, CS-19, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27 |
| `FT-AZ-02` | Feature | `EP-AZ-01` | Hosting and data decision with a cost model | `track-azure` | `azure-r1` | Must | C-02, C-04, C-06, ES-21 |
| `FT-AZ-03` | Feature | `EP-AZ-01` | Secrets and monitoring baseline on `tst` | `track-azure` | `azure-r1` | Must | NFR-05, NFR-01, CS-22, ES-17, ES-25, ES-26 |
| `FT-AZ-04` | Feature | `EP-AZ-01` | StockPilot exchange proof | `track-azure` | `azure-r1` | Must | CS-10, C-03 |
| `FT-AZ-05` | Feature | `EP-AZ-02` | Production environment and Antwerp connection | `track-azure` | `azure-r2` | Must | BR-13, NFR-01, NFR-03, NFR-05, CS-09, CS-10 |
| `FT-AZ-06` | Feature | `EP-AZ-02` | Backup, disaster recovery and tested restore | `track-azure` | `azure-r2` | Must | NFR-06, CS-07, CS-23 |
| `FT-AZ-07` | Feature | `EP-AZ-02` | Data move: database and invoice files | `track-azure` | `azure-r2` | Must | BR-13, CS-07, CS-08, CS-11, CS-21 |
| `FT-AZ-08` | Feature | `EP-AZ-02` | Nightly exchange and mail relay in Azure | `track-azure` | `azure-r2` | Must | CS-10, CS-12, C-03 |
| `FT-AZ-09` | Feature | `EP-AZ-02` | Sunday-window cutover and rollback | `track-azure` | `azure-r2` | Must | BR-13, CS-21, C-01 |
| `FT-AZ-10` | Feature | `EP-AZ-03` | Retire the old servers | `track-azure` | `azure-r3` | Must | SM-07, C-01, C-02, CS-06, CS-07 |
| `FT-AZ-11` | Feature | `EP-AZ-03` | Closing cost check, recovery test report and runbooks | `track-azure` | `azure-r3` | Must | C-04, NFR-06, CS-23, ES-09 |
| `US-AZ-001` | Story | `FT-AZ-04` | Prove the nightly order file is identical | `track-azure` | `azure-r1` | Must | CS-10, C-03, ES-27 |
| `US-AZ-002` | Story | `FT-AZ-04` | Prove the shipment file gives the same result | `track-azure` | `azure-r1` | Must | CS-10, C-03, ES-19, ES-27 |
| `US-AZ-003` | Story | `FT-AZ-04` | Confirm the Antwerp file-transfer details in writing | `track-azure` | `azure-r1` | Must | CS-10, CS-09, C-03, NFR-05 |
| `US-AZ-004` | Story | `FT-AZ-04` | Record which server features the proof needed | `track-azure` | `azure-r1` | Must | C-04, C-02, CS-10, ES-21 |
| `US-AZ-005` | Story | `FT-AZ-04` | Record the `MVE-BA01` outcome and its effect | `track-azure` | `azure-r1` | Must | CS-10, C-03 |
| `EN-AZ-01` | Enabler | `FT-AZ-01` | Azure foundation: region, names, tags, Bicep, `tst` and `prd` | `track-azure` | `azure-r1` | Must | C-01, NFR-03, ES-20, ES-22, ES-23, ES-24, ES-27, CS-09 |
| `EN-AZ-02` | Enabler | `FT-AZ-01` | Network foundation and private endpoints | `track-azure` | `azure-r1` | Must | CS-09, ES-25, ES-20, ES-27 |
| `EN-AZ-07` | Enabler | `FT-AZ-01` | Infrastructure pipeline | `track-azure` | `azure-r1` | Must | CS-19, ES-22, ES-27, NFR-05 |
| `EN-AZ-03` | Enabler | `FT-AZ-02` | Hosting and data decision record | `track-azure` | `azure-r1` | Must | C-02, C-04, C-06, ES-21, ES-08 |
| `EN-AZ-12` | Enabler | `FT-AZ-02` | Cost model | `track-azure` | `azure-r1` | Must | C-04, C-06, ES-09 |
| `EN-AZ-04` | Enabler | `FT-AZ-03` | Secrets and managed identity on `tst` | `track-azure` | `azure-r1` | Must | NFR-05, ES-17, ES-25 |
| `EN-AZ-05` | Enabler | `FT-AZ-03` | Observability baseline on `tst` | `track-azure` | `azure-r1` | Must | NFR-01, CS-22, ES-26 |
| `EN-AZ-14` | Enabler | `FT-AZ-05` | Hybrid connectivity to Antwerp | `track-azure` | `azure-r2` | Must | CS-09, CS-10, C-03, ES-25 |
| `US-AZ-006` | Story | `FT-AZ-05` | No secrets in production | `track-azure` | `azure-r2` | Must | NFR-05, ES-17, ES-25 |
| `US-AZ-007` | Story | `FT-AZ-05` | Production monitoring and availability probe | `track-azure` | `azure-r2` | Must | NFR-01, CS-22, CS-06, ES-26 |
| `US-AZ-008` | Story | `FT-AZ-05` | Production data, backups and logs stay in the EU | `track-azure` | `azure-r2` | Must | NFR-03, CS-09, ES-20 |
| `EN-AZ-06` | Enabler | `FT-AZ-06` | Backup, disaster recovery and restore method | `track-azure` | `azure-r2` | Must | NFR-06, CS-07, CS-23, NFR-03 |
| `EN-AZ-08` | Enabler | `FT-AZ-07` | Database migration method and rehearsal | `track-azure` | `azure-r2` | Must | BR-13, CS-07, CS-21, C-01, NFR-03 |
| `EN-AZ-10` | Enabler | `FT-AZ-07` | Invoice store migration | `track-azure` | `azure-r2` | Must | CS-08, CS-11, CS-14, ES-25 |
| `EN-AZ-09` | Enabler | `FT-AZ-08` | StockPilot exchange redesign | `track-azure` | `azure-r2` | Must | CS-10, C-03, ES-19, ES-25 |
| `EN-AZ-11` | Enabler | `FT-AZ-08` | SMTP relay replacement | `track-azure` | `azure-r2` | Must | CS-12, NFR-05, NFR-03 |
| `US-AZ-009` | Story | `FT-AZ-06` | Tested restore meets RPO and RTO | `track-azure` | `azure-r2` | Must | NFR-06, CS-23, CS-07 |
| `US-AZ-010` | Story | `FT-AZ-07` | Order data is identical after the move | `track-azure` | `azure-r2` | Must | BR-13, CS-07, CS-21 |
| `US-AZ-011` | Story | `FT-AZ-07` | Invoice PDFs are available in Azure | `track-azure` | `azure-r2` | Must | CS-08, CS-11, BR-13 |
| `US-AZ-012` | Story | `FT-AZ-08` | The nightly exchange runs from Azure | `track-azure` | `azure-r2` | Must | CS-10, C-03, CS-21 |
| `EN-AZ-13` | Enabler | `FT-AZ-09` | Cutover runbook and rollback plan | `track-azure` | `azure-r2` | Must | BR-13, CS-21, C-01, SM-07, ES-09 |
| `US-AZ-013` | Story | `FT-AZ-09` | Rehearse the cutover and rollback in the Sunday window | `track-azure` | `azure-r2` | Must | BR-13, CS-21, C-01 |
| `US-AZ-014` | Story | `FT-AZ-09` | Cut over production inside the Sunday window | `track-azure` | `azure-r2` | Must | BR-13, CS-21, C-01, CS-10 |
| `US-AZ-018` | Story | `FT-AZ-11` | Recovery test and report on production | `track-azure` | `azure-r3` | Must | NFR-06, CS-23, ES-09 |
| `US-AZ-017` | Story | `FT-AZ-11` | Closing cost check against the ceiling | `track-azure` | `azure-r3` | Must | C-04, ES-09 |
| `US-AZ-019` | Story | `FT-AZ-11` | Runbooks the IT team can follow | `track-azure` | `azure-r3` | Must | C-06, CS-22, CS-23, ES-09, ES-01 |
| `US-AZ-015` | Story | `FT-AZ-10` | Retire the old web and database servers | `track-azure` | `azure-r3` | Must | SM-07, C-01, C-02, CS-06, CS-07 |
| `US-AZ-016` | Story | `FT-AZ-10` | Decide whether the file server counts and report SM-07 | `track-azure` | `azure-r3` | Must | SM-07, CS-08, CS-11, C-02 |
| `EP-DN-01` | Epic | - | Modernised Order Desk | `track-dotnet` | `dotnet-r1` | Must | BR-10, NFR-05, CS-01, CS-02, CS-13, CS-14, CS-15, CS-16, CS-17, CS-18, CS-19, CS-20, ES-13, ES-14, ES-15, ES-16, ES-17, ES-18, ES-19 |
| `EP-DN-02` | Epic | - | Secure access and tenant isolation | `track-dotnet` | `dotnet-r2` | Must | BR-01, NFR-03, NFR-04, C-05, OQ-01 |
| `EP-DN-03` | Epic | - | See my orders | `track-dotnet` | `dotnet-r2` | Must | BR-02, BR-03, BR-04, BR-12, NFR-02 |
| `EP-DN-04` | Epic | - | Reorder and hand-off | `track-dotnet` | `dotnet-r2` | Must | BR-05, BR-06, BR-10, BR-12, NFR-08, C-05 |
| `EP-DN-05` | Epic | - | Portal quality | `track-dotnet` | `dotnet-r2` | Must | NFR-07, BR-11 |
| `EP-DN-06` | Epic | - | Self-service extras | `track-dotnet` | `dotnet-r3` | Should | BR-07, BR-08, BR-11 |
| `EP-DN-07` | Epic | - | Notifications and measures | `track-dotnet` | `dotnet-r4` | Could | BR-09, SM-01, SM-02, SM-03, SM-04 |
| `EP-DN-08` | Epic | - | Unplanned candidates (not in a release) | `track-dotnet` | - | Should | BR-11, NFR-08, BR-04, OQ-02 |
| `FT-DN-01` | Feature | `EP-DN-01` | Current platform and safety net | `track-dotnet` | `dotnet-r1` | Must | CS-01, CS-02, CS-18, CS-19, CS-20, ES-13, ES-14, ES-18, ES-19 |
| `FT-DN-02` | Feature | `EP-DN-01` | Configuration, logging and no secrets | `track-dotnet` | `dotnet-r1` | Must | NFR-05, CS-13, CS-15, CS-17, ES-15, ES-16, ES-17 |
| `FT-DN-03` | Feature | `EP-DN-01` | Draft order and invoice storage free of one server | `track-dotnet` | `dotnet-r1` | Must | CS-14, CS-16 |
| `FT-DN-04` | Feature | `EP-DN-01` | Staff see the order channel | `track-dotnet` | `dotnet-r1` | Must | BR-10, CS-03 |
| `FT-DN-05` | Feature | `EP-DN-02` | Portal architecture decision | `track-dotnet` | `dotnet-r2` | Must | OQ-01, NFR-04, ES-13 |
| `FT-DN-06` | Feature | `EP-DN-02` | Customer data separation | `track-dotnet` | `dotnet-r2` | Must | BR-01, C-05 |
| `FT-DN-07` | Feature | `EP-DN-02` | Customer and staff sign-in | `track-dotnet` | `dotnet-r2` | Must | BR-01, NFR-04, CS-04, OQ-01 |
| `FT-DN-08` | Feature | `EP-DN-02` | Portal data stays in the EU | `track-dotnet` | `dotnet-r2` | Must | NFR-03, ES-20 |
| `FT-DN-09` | Feature | `EP-DN-03` | See my orders | `track-dotnet` | `dotnet-r2` | Must | BR-02, NFR-02, CS-05 |
| `FT-DN-10` | Feature | `EP-DN-03` | Order detail with my prices | `track-dotnet` | `dotnet-r2` | Must | BR-03, BR-12, NFR-02, CS-20, ES-18 |
| `FT-DN-11` | Feature | `EP-DN-03` | Order status as of the 02:00 batch | `track-dotnet` | `dotnet-r2` | Must | BR-04, CS-10, C-03 |
| `FT-DN-12` | Feature | `EP-DN-04` | Reorder by copying | `track-dotnet` | `dotnet-r2` | Must | BR-05, BR-12, P-04, CS-16 |
| `FT-DN-13` | Feature | `EP-DN-04` | Portal order reaches Order Desk | `track-dotnet` | `dotnet-r2` | Must | BR-06, BR-10, C-05 |
| `FT-DN-14` | Feature | `EP-DN-04` | Order change audit | `track-dotnet` | `dotnet-r2` | Must | NFR-08, CS-05 |
| `FT-DN-15` | Feature | `EP-DN-05` | Language foundation | `track-dotnet` | `dotnet-r2` | Should | BR-11 |
| `FT-DN-16` | Feature | `EP-DN-05` | Accessibility baseline | `track-dotnet` | `dotnet-r2` | Must | NFR-07, BR-03 |
| `FT-DN-17` | Feature | `EP-DN-06` | Invoice download | `track-dotnet` | `dotnet-r3` | Should | BR-07, P-05, CS-08, CS-11, CS-14 |
| `FT-DN-18` | Feature | `EP-DN-06` | Customer administrator | `track-dotnet` | `dotnet-r3` | Should | BR-08, OQ-03 |
| `FT-DN-19` | Feature | `EP-DN-06` | French and English | `track-dotnet` | `dotnet-r3` | Should | BR-11, OQ-02 |
| `FT-DN-20` | Feature | `EP-DN-07` | Keep shipment date and carrier | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10 |
| `FT-DN-21` | Feature | `EP-DN-07` | Shipped e-mail | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10, CS-12 |
| `FT-DN-22` | Feature | `EP-DN-07` | Measure the success measures | `track-dotnet` | `dotnet-r4` | Could | SM-01, SM-02, SM-03, SM-04 |
| `FT-DN-23` | Feature | `EP-DN-08` | Dutch language | `track-dotnet` | - | Should | BR-11, OQ-02 |
| `FT-DN-24` | Feature | `EP-DN-08` | Field-level order audit | `track-dotnet` | - | Could | NFR-08 |
| `FT-DN-25` | Feature | `EP-DN-08` | Order Desk API for reuse | `track-dotnet` | - | Could | none in knowledge-docs in scope; OPEN-24, informational |
| `FT-DN-26` | Feature | `EP-DN-08` | Status clarity options (only if `MVE-BA02` says pivot) | `track-dotnet` | - | Should | BR-04, CS-10, SM-02 |
| `EN-DN-01` | Enabler | `FT-DN-01` | SDK-style projects on `net10.0` | `track-dotnet` | `dotnet-r1` | Must | CS-01, CS-02, ES-13, ES-14, ES-19 |
| `EN-DN-02` | Enabler | `FT-DN-01` | Tests pass on Windows, macOS and Linux | `track-dotnet` | `dotnet-r1` | Must | CS-18, CS-20, ES-18 |
| `EN-DN-09` | Enabler | `FT-DN-01` | Build and test pipeline | `track-dotnet` | `dotnet-r1` | Must | CS-19, CS-18, ES-18, NFR-05 |
| `EN-DN-03` | Enabler | `FT-DN-02` | Configuration through options | `track-dotnet` | `dotnet-r1` | Must | CS-17, ES-15 |
| `EN-DN-04` | Enabler | `FT-DN-02` | Logging through `ILogger<T>` | `track-dotnet` | `dotnet-r1` | Must | CS-15, ES-16 |
| `EN-DN-05` | Enabler | `FT-DN-02` | No secrets and no Windows-sign-in database connection | `track-dotnet` | `dotnet-r1` | Must | NFR-05, CS-13, ES-17, ES-25 |
| `EN-DN-06` | Enabler | `FT-DN-03` | Draft order kept outside one server's memory | `track-dotnet` | `dotnet-r1` | Must | CS-16, ES-19 |
| `EN-DN-07` | Enabler | `FT-DN-03` | Invoice storage setting instead of a fixed network path | `track-dotnet` | `dotnet-r1` | Must | CS-14, CS-11 |
| `US-DN-001` | Story | `FT-DN-04` | Staff see the order channel | `track-dotnet` | `dotnet-r1` | Must | BR-10, CS-03 |
| `US-DN-002` | Story | `FT-DN-04` | Staff filter orders by channel | `track-dotnet` | `dotnet-r1` | Must | BR-10, CS-03 |
| `EN-DN-11` | Enabler | `FT-DN-05` | Portal architecture and sign-in decision record | `track-dotnet` | `dotnet-r2` | Must | OQ-01, NFR-04, NFR-03, ES-13, ES-08, C-04, C-05 |
| `EN-DN-10` | Enabler | `FT-DN-06` | Customer data separation (tenant isolation) | `track-dotnet` | `dotnet-r2` | Must | BR-01, C-05, CS-04 |
| `EN-DN-08` | Enabler | `FT-DN-07` | Staff sign-in with Microsoft Entra ID | `track-dotnet` | `dotnet-r2` | Must | NFR-04, CS-04, CS-09 |
| `US-DN-004` | Story | `FT-DN-07` | Customer user signs in | `track-dotnet` | `dotnet-r2` | Must | BR-01, NFR-04, OQ-01, CS-04 |
| `US-DN-003` | Story | `FT-DN-06` | Customer user sees only their own company | `track-dotnet` | `dotnet-r2` | Must | BR-01, C-05 |
| `US-DN-005` | Story | `FT-DN-08` | Portal sign-in, mail and monitoring keep data in the EU | `track-dotnet` | `dotnet-r2` | Must | NFR-03, ES-20 |
| `EN-DN-14` | Enabler | `FT-DN-16` | Accessibility baseline (WCAG 2.2 AA) | `track-dotnet` | `dotnet-r2` | Must | NFR-07 |
| `US-DN-006` | Story | `FT-DN-09` | See my company's orders from the last 24 months | `track-dotnet` | `dotnet-r2` | Must | BR-02, CS-05, P-03 |
| `US-DN-007` | Story | `FT-DN-09` | The order list responds in under 2 seconds | `track-dotnet` | `dotnet-r2` | Must | NFR-02, CS-03, CS-05 |
| `US-DN-008` | Story | `FT-DN-10` | Open an order and see its details | `track-dotnet` | `dotnet-r2` | Must | BR-03, P-03, CS-05 |
| `US-DN-009` | Story | `FT-DN-10` | See my negotiated prices on an order | `track-dotnet` | `dotnet-r2` | Must | BR-12, CS-20, ES-18, C-05 |
| `US-DN-010` | Story | `FT-DN-10` | The order detail responds in under 2 seconds | `track-dotnet` | `dotnet-r2` | Must | NFR-02, CS-03 |
| `US-DN-011` | Story | `FT-DN-11` | See one of six statuses on an order | `track-dotnet` | `dotnet-r2` | Must | BR-04, P-03, CS-10 |
| `US-DN-012` | Story | `FT-DN-11` | Understand how fresh the status is | `track-dotnet` | `dotnet-r2` | Must | BR-04, CS-10, C-03, SM-02 |
| `US-DN-013` | Story | `FT-DN-12` | Start a new order by copying a previous order | `track-dotnet` | `dotnet-r2` | Must | BR-05, P-04, CS-16 |
| `US-DN-014` | Story | `FT-DN-12` | Change quantities and remove lines before submitting | `track-dotnet` | `dotnet-r2` | Must | BR-05, P-02, P-04 |
| `US-DN-015` | Story | `FT-DN-12` | See my prices on the draft order | `track-dotnet` | `dotnet-r2` | Must | BR-12, CS-20, C-05, ES-18 |
| `EN-DN-13` | Enabler | `FT-DN-14` | Audit completeness | `track-dotnet` | `dotnet-r2` | Must | NFR-08, BR-10, CS-05 |
| `US-DN-016` | Story | `FT-DN-13` | Submit the order and see it in Order Desk as Received | `track-dotnet` | `dotnet-r2` | Must | BR-06, C-05, P-01, P-02 |
| `US-DN-017` | Story | `FT-DN-13` | The server marks portal orders with the Portal channel | `track-dotnet` | `dotnet-r2` | Must | BR-10 |
| `US-DN-018` | Story | `FT-DN-14` | Every order change records who, what, when and channel | `track-dotnet` | `dotnet-r2` | Must | NFR-08, BR-10, CS-05 |
| `US-DN-019` | Story | `FT-DN-14` | Audit records are kept for 7 years | `track-dotnet` | `dotnet-r2` | Must | NFR-08, CS-05 |
| `US-DN-020` | Story | `FT-DN-16` | Use the portal with keyboard and screen reader | `track-dotnet` | `dotnet-r2` | Must | NFR-07, BR-03 |
| `US-DN-021` | Story | `FT-DN-16` | Read the portal with enough contrast, zoom and clear errors | `track-dotnet` | `dotnet-r2` | Must | NFR-07 |
| `EN-DN-12` | Enabler | `FT-DN-15` | Localisation scaffold | `track-dotnet` | `dotnet-r2` | Should | BR-11 |
| `US-DN-022` | Story | `FT-DN-17` | Download the PDF invoice of a delivered order | `track-dotnet` | `dotnet-r3` | Should | BR-07, P-05, CS-11, CS-14 |
| `US-DN-023` | Story | `FT-DN-17` | Clear message when an invoice is not available | `track-dotnet` | `dotnet-r3` | Should | BR-07, P-05 |
| `US-DN-024` | Story | `FT-DN-18` | Customer administrator invites a user | `track-dotnet` | `dotnet-r3` | Should | BR-08, OQ-03, NFR-04 |
| `US-DN-025` | Story | `FT-DN-18` | Customer administrator removes a user | `track-dotnet` | `dotnet-r3` | Should | BR-08, OQ-03 |
| `US-DN-026` | Story | `FT-DN-19` | Use the portal in French or English | `track-dotnet` | `dotnet-r3` | Should | BR-11, OQ-02 |
| `US-DN-027` | Story | `FT-DN-19` | The portal remembers my language | `track-dotnet` | `dotnet-r3` | Should | BR-11, OQ-02 |
| `EN-DN-15` | Enabler | `FT-DN-20` | Store shipment date and carrier | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10, C-03, ES-19 |
| `US-DN-028` | Story | `FT-DN-21` | Receive an e-mail when my order is shipped | `track-dotnet` | `dotnet-r4` | Could | BR-09, CS-10, CS-12 |
| `US-DN-029` | Story | `FT-DN-21` | The shipped e-mail is sent once and only to my company | `track-dotnet` | `dotnet-r4` | Could | BR-09, NFR-03 |
| `US-DN-030` | Story | `FT-DN-22` | Measure SM-01: share of orders placed through the portal | `track-dotnet` | `dotnet-r4` | Could | SM-01, BR-10 |
| `US-DN-031` | Story | `FT-DN-22` | Measure SM-02: "where is my order?" calls per week | `track-dotnet` | `dotnet-r4` | Could | SM-02, P-03 |
| `US-DN-032` | Story | `FT-DN-22` | Measure SM-03: order lines needing correction | `track-dotnet` | `dotnet-r4` | Could | SM-03, P-02 |
| `US-DN-033` | Story | `FT-DN-22` | Measure SM-04: invoice copy requests handled by staff | `track-dotnet` | `dotnet-r4` | Could | SM-04, P-05 |
| `US-DN-034` | Story | `FT-DN-23` | Use the portal in Dutch | `track-dotnet` | - | Should | BR-11, OQ-02 |
| `US-DN-035` | Story | `FT-DN-24` | See which field changed in an order | `track-dotnet` | - | Could | NFR-08 |
| `US-DN-036` | Story | `FT-DN-26` | See when each status last changed | `track-dotnet` | - | Should | BR-04, CS-10, SM-02 |
| `US-DN-037` | Story | `FT-DN-26` | Read Picking and Shipped in plain words | `track-dotnet` | - | Should | BR-04, CS-10, SM-02 |
