# Release azure-r2: Production cutover (Azure track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D6 (ES-31) |
| Track | Azure, business area BA-01 Platform and data-centre exit |
| Release name | Production cutover |
| Release tag | `azure-r2` |
| Track tag | `track-azure` |
| Git tag | `product/azure-r2`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r2 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | Rehearsal complete by end of April 2027. Cutover in a Sunday window in May 2027. At least one spare Sunday stays free before 30 June 2027 (C-01). **ASSUMPTION:** A-07 (targets, not commitments). |
| Date of this file | 2026-10-30 |
| Items in this release | 22: 1 epic, 5 features, 7 enablers, 9 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.2), `docs/product/business-requirements.md`, `docs/product/experiments.md`, `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is deployed, published, committed or tagged (ES-27). |

## 1. Words used

* **BA-01** is the business area "Platform and data-centre exit". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **Order Desk** is the internal web application staff use to enter and manage orders. **StockPilot** is the warehouse system in Antwerp. The **nightly exchange** is the 02:00 job that sends confirmed orders to StockPilot and reads shipment updates back (CS-10). **SFTP** is a secure file-transfer service. **SMTP** is the standard way to send e-mail; the **mail relay** is the internal server that forwards it (CS-12).
* **`tst`** is the test environment and **`prd`** the production environment (ES-23). **IaC** is infrastructure as code. **Bicep** is the language used for it. **`az bicep build`** is a local check that turns Bicep into a template and reports errors. Nothing is deployed (ES-27).
* **RPO** (recovery point objective) is how much data may be lost. **RTO** (recovery time objective) is how long recovery may take. **CET** is Central European Time. **The Sunday window** is Sunday 06:00 to 12:00 CET, the only planned downtime (CS-21). **Lyon** is today's data centre.
* **Cutover** is the move of Order Desk and its database from Lyon to Azure. **Rollback** is the way back to Lyon if the cutover is stopped.
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Order Desk and its database run in Azure production. Staff keep working through the move, and planned downtime stays inside the Sunday window. The nightly StockPilot exchange continues with the same files, time and paths. The existing invoice PDFs are available in Azure. Backups exist and a restore is tested against an RPO of 1 hour and an RTO of 4 hours. This is the Must outcome of the Azure track (source: BR-13, C-01, C-03, NFR-06).

The release builds on the foundation, network, secrets, monitoring, hosting decision, cost model and exchange proof of `azure-r1` (inside the Azure track, section 7.1).

## 3. Items planned in this release

The list below is every item that carries the tags `track-azure` and `azure-r2`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `azure-r2`: 22 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-AZ-02` | Epic | - | Production cutover | Must | `track-azure`, `azure-r2` | BR-13, C-01, C-03, NFR-01, NFR-03, NFR-05, NFR-06 |
| `FT-AZ-05` | Feature | `EP-AZ-02` | Production environment and Antwerp connection | Must | `track-azure`, `azure-r2` | BR-13, NFR-01, NFR-03, NFR-05, CS-09, CS-10 |
| `FT-AZ-06` | Feature | `EP-AZ-02` | Backup, disaster recovery and tested restore | Must | `track-azure`, `azure-r2` | NFR-06, CS-07, CS-23 |
| `FT-AZ-07` | Feature | `EP-AZ-02` | Data move: database and invoice files | Must | `track-azure`, `azure-r2` | BR-13, CS-07, CS-08, CS-11, CS-21 |
| `FT-AZ-08` | Feature | `EP-AZ-02` | Nightly exchange and mail relay in Azure | Must | `track-azure`, `azure-r2` | CS-10, CS-12, C-03 |
| `FT-AZ-09` | Feature | `EP-AZ-02` | Sunday-window cutover and rollback | Must | `track-azure`, `azure-r2` | BR-13, CS-21, C-01 |
| `EN-AZ-14` | Enabler | `FT-AZ-05` | Hybrid connectivity to Antwerp | Must | `track-azure`, `azure-r2` | CS-09, CS-10, C-03, ES-25 |
| `US-AZ-006` | Story | `FT-AZ-05` | No secrets in production | Must | `track-azure`, `azure-r2` | NFR-05, ES-17, ES-25 |
| `US-AZ-007` | Story | `FT-AZ-05` | Production monitoring and availability probe | Must | `track-azure`, `azure-r2` | NFR-01, CS-22, CS-06, ES-26 |
| `US-AZ-008` | Story | `FT-AZ-05` | Production data, backups and logs stay in the EU | Must | `track-azure`, `azure-r2` | NFR-03, CS-09, ES-20 |
| `EN-AZ-06` | Enabler | `FT-AZ-06` | Backup, disaster recovery and restore method | Must | `track-azure`, `azure-r2` | NFR-06, CS-07, CS-23, NFR-03 |
| `EN-AZ-08` | Enabler | `FT-AZ-07` | Database migration method and rehearsal | Must | `track-azure`, `azure-r2` | BR-13, CS-07, CS-21, C-01, NFR-03 |
| `EN-AZ-10` | Enabler | `FT-AZ-07` | Invoice store migration | Must | `track-azure`, `azure-r2` | CS-08, CS-11, CS-14, ES-25 |
| `EN-AZ-09` | Enabler | `FT-AZ-08` | StockPilot exchange redesign | Must | `track-azure`, `azure-r2` | CS-10, C-03, ES-19, ES-25 |
| `EN-AZ-11` | Enabler | `FT-AZ-08` | SMTP relay replacement | Must | `track-azure`, `azure-r2` | CS-12, NFR-05, NFR-03 |
| `US-AZ-009` | Story | `FT-AZ-06` | Tested restore meets RPO and RTO | Must | `track-azure`, `azure-r2` | NFR-06, CS-23, CS-07 |
| `US-AZ-010` | Story | `FT-AZ-07` | Order data is identical after the move | Must | `track-azure`, `azure-r2` | BR-13, CS-07, CS-21 |
| `US-AZ-011` | Story | `FT-AZ-07` | Invoice PDFs are available in Azure | Must | `track-azure`, `azure-r2` | CS-08, CS-11, BR-13 |
| `US-AZ-012` | Story | `FT-AZ-08` | The nightly exchange runs from Azure | Must | `track-azure`, `azure-r2` | CS-10, C-03, CS-21 |
| `EN-AZ-13` | Enabler | `FT-AZ-09` | Cutover runbook and rollback plan | Must | `track-azure`, `azure-r2` | BR-13, CS-21, C-01, SM-07, ES-09 |
| `US-AZ-013` | Story | `FT-AZ-09` | Rehearse the cutover and rollback in the Sunday window | Must | `track-azure`, `azure-r2` | BR-13, CS-21, C-01 |
| `US-AZ-014` | Story | `FT-AZ-09` | Cut over production inside the Sunday window | Must | `track-azure`, `azure-r2` | BR-13, CS-21, C-01, CS-10 |

Counts: 1 epic, 5 features, 7 enablers (`EN-AZ-06`, `-08`, `-09`, `-10`, `-11`, `-13`, `-14`) and 9 stories (`US-AZ-006` to `US-AZ-014`). Total 22. All are priority Must.

## 4. Requirements covered

**Business requirement (BR-).**

| ID | What it says (short) | Priority | Source | Carried in this release by |
|---|---|---|---|---|
| BR-13 | Order Desk staff keep working through the move to Azure. Planned downtime stays inside the Sunday window (Sunday 06:00 to 12:00 CET). | Must | BR-13, CS-21, CS-07, CS-10, C-01 | `US-AZ-010`, `US-AZ-011`, `US-AZ-013`, `US-AZ-014`, `EN-AZ-08`, `EN-AZ-13`, `FT-AZ-05`, `FT-AZ-07`, `FT-AZ-09`, `EP-AZ-02`. Supporting items (†): `EN-AZ-09`†, `EN-AZ-10`†, `EN-AZ-14`† and `US-AZ-012`†. The backlog counts them toward BR-13, although their own source lines do not cite it (section 11, difference 1). |

**Quality targets (NFR-).** An NFR has no priority in the business case. It is treated as Must because it gates a release that carries a Must outcome (A-12).

| ID | What it says (short) | Source | Carried in this release by | Note |
|---|---|---|---|---|
| NFR-01 | Availability of 99.5 % in business hours, Monday to Saturday 06:00 to 20:00 CET | NFR-01, CS-06, CS-22 | `US-AZ-007` (production log workspace, probe, alert and weekly availability report), `FT-AZ-05` | Measured by a probe on `prd`. Measurement basis is OPEN-08 (A-11, A-37). |
| NFR-03 | Customer and order data stay in the European Union | NFR-03, CS-09, ES-20 | `US-AZ-008` (production follow-on), `EN-AZ-06`, `EN-AZ-08`, `EN-AZ-11`, `FT-AZ-05` | Backups, logs, data copies and the mail path stay in the EU. |
| NFR-05 | No secret in code or in configuration files in the repository | NFR-05, ES-17, ES-25 | `US-AZ-006` (production follow-on), `EN-AZ-11`, `FT-AZ-05` | Key Vault behind a private endpoint, managed identities, no passwords. |
| NFR-06 | Recovery point of 1 hour and recovery time of 4 hours for order data | NFR-06, CS-07, CS-23 | `EN-AZ-06` (backup and restore method), `US-AZ-009` (tested restore), `FT-AZ-06` | The restore is tested in a rehearsal environment here. The test and report on production are in `azure-r3`. |
| NFR-04 | Customer sign-in and staff Entra ID sign-in | NFR-04 | **No Azure story.** | **ASSUMPTION:** A-02. See OPEN-13 and OPEN-03. |

**Constraints (C-) carried.**

| ID | What it says (short) | Carried by |
|---|---|---|
| C-01 | The data-centre lease ends on 30 June 2027 | `EN-AZ-08`, `EN-AZ-13`, `US-AZ-013`, `US-AZ-014`, `FT-AZ-09`, `EP-AZ-02`; one spare Sunday stays free |
| C-03 | StockPilot stays on premises and does not change | `EN-AZ-09`, `EN-AZ-14`, `US-AZ-012`, `FT-AZ-08`, `EP-AZ-02` |
| C-04 | Azure run cost of at most EUR 1,500 per month (shared by both tracks, A-14) | Applies as cost grows with `prd`. No item in this release cites C-04. The closing check is in `azure-r3` (`US-AZ-017`). |

**Success measures (SM-) moved.** SM-07 (production servers past end of support: 2 now, 0 by 30 June 2027) is prepared here by `EN-AZ-13`, which writes the decommissioning checklist. The old servers still run until `azure-r3` retires them, so the measure itself moves in `azure-r3` (source: SM-07).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Decommissioning `NWWEB01` (web server) and `NWSQL01` (database server), and `NWFS01` (file server) if it counts | `azure-r3` |
| The closing cost check against EUR 1,500, the recovery test and report on production, and the runbooks the IT team follows | `azure-r3` |
| The foundation, network, hosting decision, cost model, secrets and monitoring on `tst`, and the exchange proof | `azure-r1` (already planned there) |
| Order Desk code modernisation and portal features (BR-01 to BR-12, NFR-02, NFR-07, NFR-08) | The .NET track (BA-02). See OPEN-03 in section 7.2. |
| The "Shipped" e-mail (BR-09) and any other new e-mail | The .NET track (BA-02). See OPEN-18. This release replaces only the relay for the e-mail described in CS-12. |
| A faster refresh of order status than the nightly 02:00 exchange | Not planned. See OPEN-01 and OPEN-20. |
| A pilot environment for the customer portal | Not planned. See OPEN-05. |
| Any change to StockPilot (C-03) and any change to the finance system | Out of scope. |
| A build and test pipeline for application code | Not planned in this release. See OPEN-21 and `azure-r1` (infrastructure pipeline only). |
| Customer sign-in and staff sign-in plumbing (NFR-04, Azure side) | Unplanned. See A-02 and OPEN-13. |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Business case section 6 exclusions: online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope. |
| Deploying anything to Azure | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: reviewed infrastructure code for production, a written backup and restore method with a measured restore, a scripted database move with timed rehearsals, an invoice file move with a count and fingerprint check, a rebuilt nightly exchange that keeps the same files, a replacement for the mail relay, a Sunday-window cutover runbook with a rollback plan, and a rehearsal report. From those, the IT team can run the cutover in its own controlled change process.

## 7. Dependencies

### 7.1 Order inside the Azure track

Inside the Azure track, this release uses the output of `azure-r1`: the foundation and network (`EN-AZ-01`, `EN-AZ-02`), secrets on `tst` (`EN-AZ-04`), monitoring on `tst` (`EN-AZ-05`), the hosting and data decision (`EN-AZ-03`), the cost model, and the recorded `MVE-BA01` outcome (`US-AZ-005`). If that outcome is "stop", this release is not approved until Lena Varga and Marc Dubois decide the next step. If it is "pivot", stories may be added to this release with the next free `US-AZ-` number (the next free number today is `US-AZ-020`) and this file is updated.

Inside the release, the proposed build order is below (A-43). The product owner may change the order inside a release without changing any tag. The "Depends on" column names items of the Azure track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 13 | `EN-AZ-14` | Hybrid connectivity to Antwerp | `EN-AZ-02`, `EN-AZ-03` |
| 14 | `US-AZ-006` | No secrets in production | `EN-AZ-04` |
| 15 | `US-AZ-007` | Production monitoring and availability probe | `EN-AZ-05` |
| 16 | `US-AZ-008` | Production data, backups and logs stay in the EU | `EN-AZ-01` |
| 17 | `EN-AZ-06` | Backup, disaster recovery and restore method | `EN-AZ-03` |
| 18 | `EN-AZ-08` | Database migration method and rehearsal | `EN-AZ-03`, `EN-AZ-06` |
| 19 | `EN-AZ-10` | Invoice store migration | `EN-AZ-02`, `EN-AZ-03` |
| 20 | `EN-AZ-09` | StockPilot exchange redesign | `US-AZ-005`, `EN-AZ-03`, `EN-AZ-14` |
| 21 | `EN-AZ-11` | SMTP relay replacement | `EN-AZ-02` |
| 22 | `US-AZ-009` | Tested restore meets RPO and RTO | `EN-AZ-06`, `EN-AZ-08` |
| 23 | `US-AZ-010` | Order data is identical after the move | `EN-AZ-08` |
| 24 | `US-AZ-011` | Invoice PDFs are available in Azure | `EN-AZ-10` |
| 25 | `US-AZ-012` | The nightly exchange runs from Azure | `EN-AZ-09`, `EN-AZ-14` |
| 26 | `EN-AZ-13` | Cutover runbook and rollback plan | `EN-AZ-08`, `EN-AZ-09`, `EN-AZ-10`, `EN-AZ-11`, `EN-AZ-14`, `US-AZ-009` |
| 27 | `US-AZ-013` | Rehearse the cutover and rollback in the Sunday window | `EN-AZ-13`, `US-AZ-010`, `US-AZ-011`, `US-AZ-012` |
| 28 | `US-AZ-014` | Cut over production inside the Sunday window | `US-AZ-013`, `US-AZ-006`, `US-AZ-007`, `US-AZ-008` |

The ranks continue from `azure-r1` (ranks 1 to 12). Why this order: connectivity, backup and the data move come before the exchange build and the cutover rehearsal. Decommissioning is last, in `azure-r3`, because it removes the rollback path (source: C-03, CS-10, C-01, SM-07, backlog section 4.1).

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | Keeps the nightly 02:00 cadence (CS-10, C-03). Builds no faster refresh (`EN-AZ-09`, `US-AZ-012`). |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Plans the cutover for Order Desk as it exists on the day. Records in the rehearsal report each point that breaks on the new platform, and does not change application code (A-03; `EN-AZ-13`, `US-AZ-013`). |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports cost for the whole platform against the ceiling. Applies no split. |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Delivers `prd` and `tst` only. Plans no pilot environment (`EN-AZ-13`). |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Moves the existing PDFs to a store Order Desk can read. Leaves the write target of the finance system as Finance defines it. Changes nothing in the finance system (`EN-AZ-10`, `US-AZ-011`). |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Delivers a replacement for the relay for the e-mail that CS-12 describes today. Covers no new e-mail (BR-09) (`EN-AZ-11`). |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the decision record from `azure-r1`. Assumes the setup that record names. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Keeps the exchange files, cadence and paths identical. Assumes no schema change. Any change reported later goes through a migration-impact check (`EN-AZ-09`, `US-AZ-012`). |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Backs up audit data on the same schedule as other order data. Sizes retention at today's volume. Defines no retrieval target (`EN-AZ-06`, `US-AZ-009`). |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Keeps CET meaning for batch times and states the time zone in each story (A-10). Proves it in the rehearsal (`EN-AZ-08`, `EN-AZ-09`, `US-AZ-012`, `US-AZ-014`). |

OPEN items that concern the Azure track only, and what the release does without the answer:

| ID | OPEN question | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | `EN-AZ-14` uses the most probable design, marks it as an assumption in the design note and lists what must be confirmed. |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | `EN-AZ-09` follows the rule confirmed in `azure-r1` (`US-AZ-003`). Anything still unconfirmed is marked as an assumption. |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | `EN-AZ-13` lists `NWWEB01` and `NWSQL01` for decommissioning and marks `NWFS01` "only if OPEN-12 says it counts". |

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali |
| A-11 | NFR-01 covers the Order Desk and the portal; availability is measured by a probe | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-17 | Move items without a BR or NFR (SMTP relay CS-12, invoice share CS-08/CS-11, monitoring CS-22, DR CS-23, pipeline CS-19) are enabler stories tagged by track | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-37 | Test figures not given in the business case. NFR-02 is tested with 60 users at once (the staff peak, CS-03), a test company with about 500 orders in 24 months, a test order with 100 lines, 20 orders per page, over 10 minutes. NFR-01 uses a probe about every 5 minutes, an alert after two failed checks in a row, and a calendar-week measurement (84 business hours, about 25 minutes of downtime allowed at 99.5 %) | Lena Varga, Ahmed Benali |
| A-38 | The cutover has a go/no-go point at 09:00 CET, the rollback must finish before 12:00 CET, the cutover and rollback leave at least 30 minutes spare, and the data check takes under 30 minutes. These are planning figures inside the Sunday window of 06:00 to 12:00 CET (CS-21) | Ahmed Benali |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) | `EP-AZ-02`, `EN-AZ-09`, `US-AZ-012` |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET | `EP-AZ-02`, `EN-AZ-13`, `US-AZ-013` |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | `EP-AZ-02` |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | `EP-AZ-02`, `EN-AZ-13` |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET | `EP-AZ-02`, `FT-AZ-07`, `EN-AZ-10`, `US-AZ-011` |
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | Azure | `FT-AZ-05`, `EN-AZ-14`, `US-AZ-013` |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET | `US-AZ-007` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure | `EN-AZ-13` |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET | No Azure story for NFR-04 (A-02, sections 4 and 5) |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET | `EP-AZ-02`, `FT-AZ-08`, `EN-AZ-11` |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | `EP-AZ-02` |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET | `EP-AZ-02`, `FT-AZ-08`, `EN-AZ-09`, `US-AZ-012` |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Azure and .NET | No item; the build and test pipeline for application code is left out (section 5) |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET | `EP-AZ-02`, `FT-AZ-06`, `EN-AZ-06`, `US-AZ-009` |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET | `EP-AZ-02`, `FT-AZ-08`, `US-AZ-007`, `EN-AZ-08`, `EN-AZ-09`, `US-AZ-012`, `US-AZ-014` |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | Azure | `EN-AZ-14`, `EN-AZ-09`, `US-AZ-012` |
| OPEN-32 | Which EU secondary region, if any, is used for disaster recovery and EU-resident copies (ES-20, NFR-03)? | Ahmed Benali | Azure | `US-AZ-008`, `EN-AZ-06` |

OPEN-08: without the answer, the availability report uses the calendar week and says so (`US-AZ-007`). OPEN-32: without the answer, every `prd` resource location is France Central, and any secondary region used for recovery must be in the European Union.

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 22 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-azure` and `azure-r2` on every item. A query on the tag `azure-r2` lists the release. |
| GitHub | Issue labels `track-azure` and `azure-r2`, and the milestone `azure-r2`. |
| Jira | Labels `track-azure` and `azure-r2`, and the fix version `azure-r2`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). The Git tag `product/azure-r2` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | Backlog section 5.1 marks these items with a dagger as supporting BR-13, because their own source lines do not cite BR-13. The traceability file marks them the same way. | `EN-AZ-09`, `EN-AZ-10`, `EN-AZ-14`, `US-AZ-012` |
| 2 | The plan lists C-01 and C-03 for this release, and the product requirements document lists C-04 as applying. No item here cites C-04, so it is carried by `azure-r1` (estimate) and `azure-r3` (closing check). | C-04 |
| 3 | The product requirements document lists OPEN-07, OPEN-08 and OPEN-12 as "other OPEN items used". Items here cite them, and OPEN-30 and OPEN-32 as well. All are in sections 7.2 and 9. | OPEN-07, OPEN-08, OPEN-12, OPEN-30, OPEN-32 |
## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. The `azure-r1` outcome for `MVE-BA01` is recorded as persevere, or as pivot with the changes accepted by the product owner (inside the Azure track). Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer.

**Definition of done.** The release is done when the acceptance criteria of its 22 items are met by tests and validation only (ES-27):

* *Production foundation.* `az bicep build` passes for `prd`. Production has a Key Vault behind a private endpoint and managed identities with no passwords. A scan of templates, parameter files and pipeline finds no secret. Every resource that holds data, backups or logs is in France Central or an agreed EU region.
* *Monitoring.* Production has one log workspace, a probe about every 5 minutes, an alert after two failed checks, and a weekly availability report for business hours with the time zone stated (A-37).
* *Backup and restore.* Backups allow a restore with at most 1 hour of lost data and are kept at least 35 days. A written restore method with a total of at most 4 hours is reviewed. A restore into a rehearsal environment is measured and meets the RPO and RTO (NFR-06).
* *Data move.* The database move is scripted and timed. Row counts, highest order number and key-column checksums are equal between a rehearsal copy and the migrated database, and the check runs in under 30 minutes (A-38). The invoice PDFs match by file count, total size and a 100-file fingerprint sample.
* *Exchange and mail.* The rebuilt nightly exchange writes `orders_YYYYMMDD.csv` and reads `shipments.csv` with the same names, format and paths, at 02:00 CET, with no duplicate files or audit rows when a run fails. A mail path replaces the internal relay for the e-mail that CS-12 describes. Antwerp paths, file names and format do not change (C-03).
* *Cutover plan and rehearsal.* The runbook lists every step from freeze to the first Monday sign-in inside the Sunday window, with a go/no-go point at 09:00 CET and a rollback that finishes before 12:00 CET, leaving at least 30 minutes spare (A-38). The rehearsal report records every step's start and end and every point where Order Desk, as it is today, breaks on the new platform (OPEN-03).
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop. Infrastructure code is validated locally and reviewed, not applied (ES-27).** The restore test, the rehearsal and the cutover are carried out by the IT team in its own controlled environment and change process, not from this workshop. This file does not start or authorise any deployment.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/azure-r2` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/azure-r2` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/azure-r2`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/azure-r2` is created on the commit that holds this file.**
