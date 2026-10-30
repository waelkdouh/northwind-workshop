# Release azure-r1: Foundation and proof (Azure track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D6 (ES-31) |
| Track | Azure, business area BA-01 Platform and data-centre exit |
| Release name | Foundation and proof |
| Release tag | `azure-r1` |
| Track tag | `track-azure` |
| Git tag | `product/azure-r1`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r1 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | End of January 2027. **ASSUMPTION:** A-07 (a target, not a commitment). |
| Date of this file | 2026-10-30 |
| Items in this release | 17: 1 epic, 4 features, 7 enablers, 5 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.1), `docs/product/business-requirements.md`, `docs/product/experiments.md` (`MVE-BA01`), `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is deployed, published, committed or tagged (ES-27). |

## 1. Words used

* **BA-01** is the business area "Platform and data-centre exit". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **Order Desk** is the internal web application staff use to enter and manage orders. **StockPilot** is the warehouse system in Antwerp. The **nightly exchange** is the 02:00 job that sends confirmed orders to StockPilot and reads shipment updates back (CS-10). **SFTP** is a secure file-transfer service.
* **`tst`** is the test environment and **`prd`** the production environment (ES-23). **IaC** is infrastructure as code. **Bicep** is the language used for it. **`az bicep build`** is a local check that turns Bicep into a template and reports errors. Nothing is deployed (ES-27).
* **MVE** is a Minimum Viable Experiment: a small, cheap test of the riskiest idea. **`MVE-BA01`** is the Azure experiment (`docs/product/experiments.md`).
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Answer the biggest Azure unknowns early and prepare Azure for rehearsals. Show that the nightly StockPilot exchange can keep its files, its 02:00 time and its paths with no change to StockPilot. Settle where Order Desk and its database will run, and estimate the monthly run cost against the EUR 1,500 ceiling. Put in place the named, tagged, EU-only foundation, the private network, the secrets baseline, the monitoring baseline and an infrastructure pipeline on `tst` and `prd` (source: C-03, C-04, CS-10, NFR-01, NFR-03, NFR-05, A-23).

This release moves no production system. It produces written decisions, local proofs, and infrastructure code that is checked locally and reviewed (ES-27).

## 3. Items planned in this release

The list below is every item that carries the tags `track-azure` and `azure-r1`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `azure-r1`: 17 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-AZ-01` | Epic | - | Foundation and proof | Must | `track-azure`, `azure-r1` | C-01, C-03, C-04, NFR-01, NFR-03, NFR-05, CS-10 |
| `FT-AZ-01` | Feature | `EP-AZ-01` | Azure foundation and network | Must | `track-azure`, `azure-r1` | C-01, NFR-03, CS-09, CS-19, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27 |
| `FT-AZ-02` | Feature | `EP-AZ-01` | Hosting and data decision with a cost model | Must | `track-azure`, `azure-r1` | C-02, C-04, C-06, ES-21 |
| `FT-AZ-03` | Feature | `EP-AZ-01` | Secrets and monitoring baseline on `tst` | Must | `track-azure`, `azure-r1` | NFR-05, NFR-01, CS-22, ES-17, ES-25, ES-26 |
| `FT-AZ-04` | Feature | `EP-AZ-01` | StockPilot exchange proof | Must | `track-azure`, `azure-r1` | CS-10, C-03 |
| `US-AZ-001` | Story | `FT-AZ-04` | Prove the nightly order file is identical | Must | `track-azure`, `azure-r1` | CS-10, C-03, ES-27 |
| `US-AZ-002` | Story | `FT-AZ-04` | Prove the shipment file gives the same result | Must | `track-azure`, `azure-r1` | CS-10, C-03, ES-19, ES-27 |
| `US-AZ-003` | Story | `FT-AZ-04` | Confirm the Antwerp file-transfer details in writing | Must | `track-azure`, `azure-r1` | CS-10, CS-09, C-03, NFR-05 |
| `US-AZ-004` | Story | `FT-AZ-04` | Record which server features the proof needed | Must | `track-azure`, `azure-r1` | C-04, C-02, CS-10, ES-21 |
| `US-AZ-005` | Story | `FT-AZ-04` | Record the `MVE-BA01` outcome and its effect | Must | `track-azure`, `azure-r1` | CS-10, C-03 |
| `EN-AZ-01` | Enabler | `FT-AZ-01` | Azure foundation: region, names, tags, Bicep, `tst` and `prd` | Must | `track-azure`, `azure-r1` | C-01, NFR-03, ES-20, ES-22, ES-23, ES-24, ES-27, CS-09 |
| `EN-AZ-02` | Enabler | `FT-AZ-01` | Network foundation and private endpoints | Must | `track-azure`, `azure-r1` | CS-09, ES-25, ES-20, ES-27 |
| `EN-AZ-07` | Enabler | `FT-AZ-01` | Infrastructure pipeline | Must | `track-azure`, `azure-r1` | CS-19, ES-22, ES-27, NFR-05 |
| `EN-AZ-03` | Enabler | `FT-AZ-02` | Hosting and data decision record | Must | `track-azure`, `azure-r1` | C-02, C-04, C-06, ES-21, ES-08 |
| `EN-AZ-12` | Enabler | `FT-AZ-02` | Cost model | Must | `track-azure`, `azure-r1` | C-04, C-06, ES-09 |
| `EN-AZ-04` | Enabler | `FT-AZ-03` | Secrets and managed identity on `tst` | Must | `track-azure`, `azure-r1` | NFR-05, ES-17, ES-25 |
| `EN-AZ-05` | Enabler | `FT-AZ-03` | Observability baseline on `tst` | Must | `track-azure`, `azure-r1` | NFR-01, CS-22, ES-26 |

Counts: 1 epic, 4 features, 7 enablers (`EN-AZ-01`, `-02`, `-03`, `-04`, `-05`, `-07`, `-12`) and 5 stories (`US-AZ-001` to `US-AZ-005`). Total 17. All are priority Must.

## 4. Requirements covered

**Business requirements (BR-):** none. The only Azure business requirement, BR-13 (staff keep working through the move), is carried by `azure-r2`. This release prepares the ground for it.

**Quality targets (NFR-).** An NFR has no priority in the business case. It is treated as Must because it gates a release that carries a Must outcome (A-12).

| ID | What it says (short) | Source | Carried in this release by | Note |
|---|---|---|---|---|
| NFR-03 | Customer and order data stay in the European Union | NFR-03, CS-09, C-01 | `EN-AZ-01` (primary Azure story: regions, backups and logs in the EU), `FT-AZ-01`, `EP-AZ-01` | Platform side only. The production follow-on is in `azure-r2`. |
| NFR-05 | No secret in code or in configuration files in the repository | NFR-05, CS-13, CS-17, ES-17 | `EN-AZ-04` (primary Azure story: Key Vault and managed identity on `tst`), `EN-AZ-07`, `US-AZ-003`, `FT-AZ-03` | Platform side only. The production follow-on is in `azure-r2`. |
| NFR-01 | Availability of 99.5 % in business hours, Monday to Saturday 06:00 to 20:00 CET | NFR-01, CS-06, CS-22 | `EN-AZ-05` (log workspace, probe and alert on `tst`), `FT-AZ-03` | Design and first measurement on `tst`. The production probe is in `azure-r2`. The measurement basis is OPEN-08 (A-11, A-37). |
| NFR-04 | Customer sign-in and staff Entra ID sign-in | NFR-04 | **No Azure story.** | **ASSUMPTION:** A-02. An Azure story exists only if OPEN-03 or OPEN-13 gives sign-in plumbing to the Azure track. Until then the traceability table shows "OPEN-13, no Azure story". |

**Constraints (C-) carried.**

| ID | What it says (short) | Carried by |
|---|---|---|
| C-01 | The data-centre lease ends on 30 June 2027 | `EN-AZ-01`, `FT-AZ-01`, `EP-AZ-01`; it sets every target date |
| C-02 | The web and database servers are past end of support | `EN-AZ-03`, `US-AZ-004`, `FT-AZ-02` |
| C-03 | StockPilot stays on premises and does not change | `US-AZ-001`, `US-AZ-002`, `US-AZ-003`, `US-AZ-005`, `FT-AZ-04`, `EP-AZ-01` |
| C-04 | Azure run cost of at most EUR 1,500 per month (shared by both tracks, A-14) | `EN-AZ-12` (cost model), `EN-AZ-03`, `US-AZ-004`; this is the estimate. The closing check is in `azure-r3`. |
| C-06 | Small IT team, no Kubernetes | `EN-AZ-03`, `EN-AZ-12`, `FT-AZ-02` |

**Success measures (SM-) moved.** None directly. This release lowers the risk to SM-07 (production servers past end of support: 2 now, 0 by 30 June 2027) by settling the hosting target and the exchange early (source: SM-07, C-02).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Production cutover: BR-13, database move rehearsal, invoice store move, nightly exchange build in Azure, SMTP relay replacement, backup and tested restore, Antwerp connection, production secrets, monitoring and EU residency on `prd` | `azure-r2` |
| Decommissioning `NWWEB01` and `NWSQL01`, the closing cost check, the recovery test report and the runbooks | `azure-r3` |
| Any Order Desk code change | Not planned in this release. See OPEN-03 (section 7.2). |
| A pilot environment for the customer portal | Not planned in this release. See OPEN-05 (section 7.2). |
| A build and test pipeline for application code | Not planned in this release. This release has the infrastructure pipeline only. See OPEN-21 (section 7.2). |
| Customer sign-in and staff sign-in plumbing (NFR-04, Azure side) | Unplanned. See A-02 and OPEN-13. |
| Portal and ordering features (BR-01 to BR-12), NFR-02, NFR-07 and NFR-08 | The .NET track (BA-02). They are not part of this release. |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Business case section 6 exclusions: online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope. |
| Deploying anything to Azure | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a recorded answer on whether the nightly StockPilot exchange can move with identical files; written confirmation of Antwerp's file-transfer details; a hosting and data decision with a monthly cost estimate for `prd` plus one `tst`; and reviewed infrastructure code for a named, tagged, EU-only foundation with a private network, secrets handling, monitoring and a checking pipeline.

## 7. Dependencies

### 7.1 Order inside the Azure track

`azure-r1` is the first Azure release. It has no dependency on an earlier release. Inside the release, the proposed build order is below (A-43). The product owner may change the order inside a release without changing any tag. The "Depends on" column names items of the Azure track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 1 | `US-AZ-001` | Prove the nightly order file is identical | none |
| 2 | `US-AZ-002` | Prove the shipment file gives the same result | none |
| 3 | `US-AZ-003` | Confirm the Antwerp file-transfer details in writing | none |
| 4 | `US-AZ-004` | Record which server features the proof needed | `US-AZ-001`, `US-AZ-002` |
| 5 | `US-AZ-005` | Record the `MVE-BA01` outcome and its effect | `US-AZ-001` to `US-AZ-004` |
| 6 | `EN-AZ-01` | Azure foundation: region, names, tags, Bicep, `tst` and `prd` | none |
| 7 | `EN-AZ-02` | Network foundation and private endpoints | `EN-AZ-01` |
| 8 | `EN-AZ-07` | Infrastructure pipeline | `EN-AZ-01` |
| 9 | `EN-AZ-03` | Hosting and data decision record | `US-AZ-004`, `US-AZ-005` |
| 10 | `EN-AZ-12` | Cost model | `EN-AZ-03` |
| 11 | `EN-AZ-04` | Secrets and managed identity on `tst` | `EN-AZ-02`, `EN-AZ-03`, `EN-AZ-07` |
| 12 | `EN-AZ-05` | Observability baseline on `tst` | `EN-AZ-01`, `EN-AZ-02` |

Why this order: the StockPilot proof (`FT-AZ-04`) is the riskiest assumption and the cheapest to test, so it is first. Its result feeds the hosting decision and the cost model. The foundation, network and pipeline come next, then secrets and monitoring (source: C-03, CS-10, backlog section 4.1).

**What the outcome of `MVE-BA01` does to the plan (inside the Azure track, `US-AZ-005`).** The overall result is the weakest of four checks. *Persevere:* the exchange redesign in `azure-r2` is built from the proven design. *Pivot:* the hosting decision is reopened, the cost model is re-run, the exchange redesign is resized, each difference found becomes a story with the next free `US-AZ-` number in `azure-r2` (the next free number today is `US-AZ-020`), and the product owner and the sponsor review the dates (A-07). *Stop:* `azure-r2` is not approved until Lena Varga and Marc Dubois decide the next step, and `azure-r1` carries on with its other enablers. A pass does not prove that the Azure run works. The `azure-r2` rehearsal still has to prove it. If a pivot adds stories, the member list of `azure-r2` changes and its release file is updated (A-06, A-30).

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Builds only hosting, data and exchange work (A-03). Makes no Order Desk code change. Lists, read-only, the points where the current application would break on the new platform. |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Estimates the whole platform (Order Desk and portal, `prd` and one `tst`) against the ceiling. Applies no split (`EN-AZ-03`, `EN-AZ-12`, `US-AZ-004`). |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Plans `tst` and `prd` only. Plans no separate pilot environment. |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Writes no sign-in story (A-02). Shows "OPEN-13, no Azure story". |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Decides in `EN-AZ-03`. Costs a single-instance case and a multi-instance case, because session state sits in one server's memory today (CS-16). Names the setup it assumes. |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Delivers only the infrastructure pipeline (`EN-AZ-07`). Delivers no build or test pipeline for application code. |
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | Used by `US-AZ-005`. Keeps the nightly 02:00 cadence and builds no faster refresh. A proof result that touches freshness is written under OPEN-01. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Used by `FT-AZ-04`, `US-AZ-002`, `US-AZ-005`. Keeps the exchange files, cadence and paths identical and assumes no schema change. A needed schema change is not made; it goes to a migration-impact check. |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Used by `EN-AZ-05`. Keeps CET meaning for batch times and states the time zone in the query (A-10). |

Items OPEN-01, OPEN-20 and OPEN-23 are used by items in this release but are not in the plan's list of cross-track items for `azure-r1`. They are shown here because the items cite them (section 11, difference 1).

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-09 | The cost model assumes SQL and private endpoints are the main spend | Ahmed Benali |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali |
| A-11 | NFR-01 covers the Order Desk and the portal; availability is measured by a probe | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-30 | The owner of `MVE-BA01` is Ahmed Benali and the owner of `MVE-BA02` is Lena Varga. The owner runs the test, records the result and proposes the decision. The product owner agrees any change to the backlog | Lena Varga |
| A-31 | The elapsed times, effort in person-days, group size of about 10 customers, daily staff time of about 30 minutes and proposed run windows (late November to mid-December 2026 for `MVE-BA01`; January to February 2027 for `MVE-BA02`) are planning estimates. The owners set the real dates. The year-end is assumed to be a busy period for customers | Lena Varga, Ahmed Benali |
| A-32 | The format of the exchange files is taken from reading `database/003-stockpilot-exchange.sql` and from how the command-line tool normally behaves, not from a real file. Assumed: the order file uses `;` as separator, has no header row, does not put quotes around values, uses the database server's default character set, and has no defined row order. The shipment file has a header row and `;` as separator. Real files from Antwerp may differ | Ahmed Benali |
| A-37 | Test figures not given in the business case. NFR-02 is tested with 60 users at once (the staff peak, CS-03), a test company with about 500 orders in 24 months, a test order with 100 lines, 20 orders per page, over 10 minutes. NFR-01 uses a probe about every 5 minutes, an alert after two failed checks in a row, and a calendar-week measurement (84 business hours, about 25 minutes of downtime allowed at 99.5 %) | Lena Varga, Ahmed Benali |
| A-39 | Resource abbreviations in names (for example `rg`, `kv`, `app`) follow the Microsoft Cloud Adoption Framework abbreviation list. ES-23 gives the pattern and one example, not a list | Ahmed Benali |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |
| A-45 | The cost "at risk" threshold is EUR 1,350 per month, 10 % under the EUR 1,500 ceiling (C-04). A full option above it is flagged "at risk" | Lena Varga, Ahmed Benali |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) | `US-AZ-005` |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET | `EP-AZ-01` |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | `EP-AZ-01`, `EN-AZ-03`, `EN-AZ-12`, `US-AZ-004` |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | `EP-AZ-01` |
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | Azure | `FT-AZ-04`, `US-AZ-003`, `US-AZ-005` |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET | `EN-AZ-05` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure | No item in this release (section 11, difference 2). It is used by `azure-r2` and `azure-r3`. |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET | `EP-AZ-01` |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | `EP-AZ-01`, `EN-AZ-03` |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET | `FT-AZ-04`, `US-AZ-002`, `US-AZ-005` |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Azure and .NET | `EP-AZ-01`, `EN-AZ-07` |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET | `EN-AZ-05` |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | Azure | `US-AZ-001`, `US-AZ-002`, `US-AZ-003` |
| OPEN-32 | Which EU secondary region, if any, is used for disaster recovery and EU-resident copies (ES-20, NFR-03)? | Ahmed Benali | Azure | `EN-AZ-01` |

OPEN-32: without the answer, `EN-AZ-01` names France Central as the primary region and no secondary region, and the build fails for any secondary region outside the European Union.

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 17 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-azure` and `azure-r1` on every item. A query on the tag `azure-r1` lists the release. |
| GitHub | Issue labels `track-azure` and `azure-r1`, and the milestone `azure-r1`. |
| Jira | Labels `track-azure` and `azure-r1`, and the fix version `azure-r1`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). The Git tag `product/azure-r1` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | Items in this release cite OPEN-01, OPEN-20 and OPEN-23, which are not in the plan's list of cross-track items for `azure-r1`. They are shown in section 7.2 with what the release does without the answer. | `US-AZ-005`, `US-AZ-002`, `FT-AZ-04`, `EN-AZ-05` |
| 2 | The product requirements document lists OPEN-12 (NWFS01) for `azure-r1`. No item in this release cites it. It is shown in section 9 for completeness. It is used by `azure-r2` and `azure-r3`. | OPEN-12 |

## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can start without an answer. Nothing else has to be done first.

**Definition of done.** The release is done when the acceptance criteria of its 17 items are met by tests and validation only (ES-27):

* *Proof.* The nightly order file written by the new method has the same SHA-256 fingerprint as the legacy file on 3 of 3 runs, on a throw-away local SQL Server with made-up data. The shipment file gives the same order statuses and audit rows. Antwerp's file-transfer details are confirmed in writing. The result of `MVE-BA01` is recorded as persevere, pivot or stop, with its evidence.
* *Decision and cost.* The hosting and data decision record is written, names its approver and is marked "proposed" until that person approves it. The cost model shows the monthly cost per service for `prd` and `tst` against EUR 1,500 and flags any full option above EUR 1,350 as "at risk" (A-45).
* *Infrastructure code.* `az bicep build` passes for `tst` and `prd`. Names follow ES-23 and every resource carries the four tags (ES-24). Public network access is off for data services. A scan of templates, parameter files and pipeline finds no secret. Monitoring, probe and alert are defined for `tst`.
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop. Infrastructure code is validated locally and reviewed, not applied (ES-27).** No real Azure resource is created, and no production data is used.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/azure-r1` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/azure-r1` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/azure-r1`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/azure-r1` is created on the commit that holds this file.**
