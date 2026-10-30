# Northwind Traders — Product documents: index and master registers (BA-01 Azure and BA-02 .NET)

| Field | Value |
|---|---|
| Document | Index and master registers, deliverable D8 |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`, releases `azure-r1` to `azure-r3`) and **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`, releases `dotnet-r1` to `dotnet-r4`). **BA-03** Delivery claims and credit notes is out of scope. |
| Product owner (proposed) | Lena Varga, Head of Customer Operations, owns the product backlog and approves each release (A-29) |
| Sponsor | Marc Dubois, Chief Operating Officer (COO) |
| Builds on | The 12 other files in `docs/product/` (section 2). Every number, ID and tag below was read from those files on 2026-10-30. |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-07, ES-27 to ES-31, ES-39) |
| Boundary | **Nothing is deployed or published.** All seven releases were approved on 2026-10-30. The commit that holds the approved files and the Git tags in section 3 were created on 2026-10-30 (section 4.3, ES-31, A-29). This file changes no other file. |

## 1. Purpose and scope

### 1.1 Purpose

This folder holds the product documents that turn the Northwind business case into work a team can build. This file is the front page. It tells you what each document is for, which order to read them in, which release holds what, how the tags work, and which assumptions and open questions are still unanswered. It is the only place that lists **all** assumptions (`A-01` to `A-46`) and **all** open questions (`OPEN-01` to `OPEN-33`) in one table (sections 5 and 6).

Two business areas are planned:

* **BA-01 Platform and data-centre exit.** Run Order Desk and its database in Azure before the data-centre lease ends on 30 June 2027 (C-01), keep the nightly StockPilot file exchange working, and meet the availability, recovery and cost targets. Delivered by the **Azure track** (`track-azure`), in 3 releases.
* **BA-02 Ordering and customer self-service.** The Customer Portal and the Order Desk application that serves it: sign-in, orders, status, reorder, invoices, prices, and the upgrade of Order Desk that the portal depends on. Delivered by the **.NET track** (`track-dotnet`), in 4 releases.

The two tracks are delivered by different teams. **No release waits for a release of the other track** (ES-31). Where one track needs an answer from the other, it is written as an **OPEN:** item with what the release does without the answer (section 6).

### 1.2 Out of scope

* **BA-03 Delivery claims and credit notes** (Power Platform, `track-power-platform`) is out of scope: BR-14 to BR-19, NFR-09, C-07, C-08, SM-05, SM-06, OQ-04, OQ-05, CS-24 to CS-28 and ES-32 to ES-37. The tag `track-power-platform` is not used as an item tag. One informational item, OPEN-24, says BA-03 will later need an Order Desk programming interface (API). No release depends on it.
* The business case (section 6, "Out of scope for the first release") also excludes: online payment, a native mobile app, changes to StockPilot, replacing the finance system, and customers recording claims themselves in the portal.

### 1.3 Words used

* **BA-** business area. **BR-** business requirement. **NFR-** non-functional requirement (a quality target such as availability). **C-** constraint. **SM-** success measure. **P-** problem. **OQ-** open question in the business case. **CS-** a fact about today's system (`current-state.md`). **ES-** an engineering standard. All come from `knowledge-docs`.
* **BRD** business requirements document. **PRD** product requirements document. **MVE** minimum viable experiment: a small, cheap test of the riskiest assumption. **Epic**, **feature**, **story** and **enabler** are levels of the backlog; an enabler is preparation work that comes before the features that use it.
* **Order Desk** is the internal order application. **Portal** is the new customer web site. **StockPilot** is the warehouse system in Antwerp. **Entra ID** is Microsoft's sign-in service. **`tst`** and **`prd`** are the test and production environments.
* **ASSUMPTION:** marks anything not stated in `knowledge-docs`. Each has a person who can confirm it (ES-03). **OPEN:** marks an unanswered question. Each has a person who can answer it (ES-04). Neither is a requirement.
* Short names for documents in the registers: **BRD**, **PRD**, **EXP** (experiments), **BL** (backlog), **TR** (traceability), and **AZ1**, **AZ2**, **AZ3**, **DN1**, **DN2**, **DN3**, **DN4** for the release files `azure-r1` to `dotnet-r4`.

## 2. Index of documents

Read in this order. Each document reuses the IDs of the one before it. All 13 files are in `docs/product/` (ES-07). The seven release files were approved on 2026-10-30. The other six files are drafts for review. None is approved for build (A-16).

| # | Document | Path | What it is, in one line | Owner role (agent) | Status |
|---|---|---|---|---|---|
| 1 | Business requirements (BRD, D1) | `docs/product/business-requirements.md` | Why: needs, scope, stakeholders, current-state facts, requirements and risks for BA-01 and BA-02. | analyst (BRD Builder) | Draft - for review |
| 2 | Product requirements (PRD, D2) | `docs/product/product-requirements.md` | What: product vision per track, functional requirements, release roadmap (3 Azure and 4 .NET releases) and success measures by release. | analyst (PRD Builder) | Draft - for review |
| 3 | Experiments (D3) | `docs/product/experiments.md` | Two small tests designed, not run: `MVE-BA01` (StockPilot exchange) and `MVE-BA02` (nightly-fresh status). | experimenter (Experiment Designer) | Draft - for review |
| 4 | Backlog (D4) | `docs/product/backlog.md` | Epics, features, stories and enablers with Given / When / Then, tags, priority and sources. 133 items. Its section 11 is the item register. | product-owner (Functional Planner) | Draft - for review |
| 5 | Traceability (D5) | `docs/product/traceability.md` | Maps every BR-01 to BR-13 and NFR-01 to NFR-08 to stories, by track and release. Lists what is not covered (none) and BA-03 as out of scope. | product-owner (Functional Planner) | Draft - for review |
| 6 | Release `azure-r1` (D6) | `docs/product/releases/azure-r1.md` | Foundation and proof. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/azure-r1 |
| 7 | Release `azure-r2` (D6) | `docs/product/releases/azure-r2.md` | Production cutover. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/azure-r2 |
| 8 | Release `azure-r3` (D6) | `docs/product/releases/azure-r3.md` | Stabilise and decommission. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/azure-r3 |
| 9 | Release `dotnet-r1` (D7) | `docs/product/releases/dotnet-r1.md` | Modernised Order Desk (enabler release). | product-owner (Functional Planner) | Approved 2026-10-30; tag product/dotnet-r1 |
| 10 | Release `dotnet-r2` (D7) | `docs/product/releases/dotnet-r2.md` | Portal pilot: Must items. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/dotnet-r2 |
| 11 | Release `dotnet-r3` (D7) | `docs/product/releases/dotnet-r3.md` | Should items: invoices, customer administrator, French and English. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/dotnet-r3 |
| 12 | Release `dotnet-r4` (D7) | `docs/product/releases/dotnet-r4.md` | Could items and measures: shipped e-mail and success measures. | product-owner (Functional Planner) | Approved 2026-10-30; tag product/dotnet-r4 |
| 13 | Index and master registers (D8, this file) | `docs/product/README.md` | The front page and the master assumption and OPEN registers. | product-owner (Functional Planner) | Draft - for review |

The review report (D9, `.copilot-tracking/reviews/product-documents-review.md`, written by the tester) is outside `docs/product/` and is not one of the 13 files.

## 3. Tracks and releases

Item counts come from the register in `backlog.md` section 11 (133 rows). They agree with `backlog.md` section 3.1, `traceability.md` section 7 and the "Items in this release" line of each release file. A count includes the epic, its features, and the enablers and stories under them. An item has exactly one release tag, so nothing is counted twice.

| Track | Track tag | Release tag | Release file | Git tag (created 2026-10-30) | Items (epic / features / enablers / stories) | Target date (**ASSUMPTION:** A-07) | Status |
|---|---|---|---|---|---|---|---|
| Azure (BA-01) | `track-azure` | `azure-r1` | `docs/product/releases/azure-r1.md` | `product/azure-r1` | 17 (1 / 4 / 7 / 5) | End of January 2027 | Approved 2026-10-30; tag product/azure-r1 |
| Azure (BA-01) | `track-azure` | `azure-r2` | `docs/product/releases/azure-r2.md` | `product/azure-r2` | 22 (1 / 5 / 7 / 9) | Rehearsal complete by end of April 2027; cutover in a Sunday window in May 2027 | Approved 2026-10-30; tag product/azure-r2 |
| Azure (BA-01) | `track-azure` | `azure-r3` | `docs/product/releases/azure-r3.md` | `product/azure-r3` | 8 (1 / 2 / 0 / 5) | By 30 June 2027 (C-01) | Approved 2026-10-30; tag product/azure-r3 |
| .NET (BA-02) | `track-dotnet` | `dotnet-r1` | `docs/product/releases/dotnet-r1.md` | `product/dotnet-r1` | 15 (1 / 4 / 8 / 2) | End of February 2027 | Approved 2026-10-30; tag product/dotnet-r1 |
| .NET (BA-02) | `track-dotnet` | `dotnet-r2` | `docs/product/releases/dotnet-r2.md` | `product/dotnet-r2` | 41 (4 / 12 / 6 / 19) | Pilot start in April 2027, with 20 customers (OPEN-05) | Approved 2026-10-30; tag product/dotnet-r2 |
| .NET (BA-02) | `track-dotnet` | `dotnet-r3` | `docs/product/releases/dotnet-r3.md` | `product/dotnet-r3` | 10 (1 / 3 / 0 / 6) | Not dated | Approved 2026-10-30; tag product/dotnet-r3 |
| .NET (BA-02) | `track-dotnet` | `dotnet-r4` | `docs/product/releases/dotnet-r4.md` | `product/dotnet-r4` | 11 (1 / 3 / 1 / 6) | Not dated | Approved 2026-10-30; tag product/dotnet-r4 |
| .NET (BA-02) | `track-dotnet` | none (unplanned) | none (listed in `backlog.md` section 7, epic `EP-DN-08`, and in `dotnet-r4.md` Appendix A) | none | 9 (1 / 4 / 0 / 4): `EP-DN-08` and its children | none | Unplanned, track tag only |

Totals, checked against the backlog register: Azure 47 items (3 epics, 11 features, 14 enablers, 19 stories); .NET 86 items (8 epics, 26 features, 15 enablers, 37 stories); both tracks 133. Planned items: 124 (47 Azure and 77 .NET). Unplanned: 9, all .NET. The 9 unplanned items are held back by an open question: Dutch (OPEN-14), field-level audit (OPEN-17), an Order Desk API for reuse (OPEN-24), and status options that depend on the `MVE-BA02` result (A-35).

All target dates are **ASSUMPTION:** A-07 (owners: Marc Dubois and Lena Varga). They are targets, not commitments.

## 4. Tagging and publishing convention

### 4.1 Tags (ES-30, ES-31)

* Every epic, feature, story and enabler carries exactly **one track tag**: `track-azure` or `track-dotnet`.
* A **planned** item also carries exactly **one release tag of the same track**: `azure-r1`, `azure-r2` or `azure-r3` for `track-azure`; `dotnet-r1` to `dotnet-r4` for `track-dotnet`. An **unplanned** item carries the track tag only.
* A parent and its children share track and release. A story that needs both tracks is split into one story per track. NFR-03, NFR-04 and NFR-05 are handled this way (A-02).
* A release is described in `docs/product/releases/<track>-r<n>.md`: its items, the BR- and NFR- it covers, what it leaves out, and its dependencies on other tracks as **OPEN:** items. A release never waits for another track (ES-31).
* Item IDs: epic `EP-<AZ|DN>-nn`, feature `FT-<AZ|DN>-nn`, story `US-<AZ|DN>-nnn`, enabler `EN-<AZ|DN>-nn`, experiment `MVE-BA01` and `MVE-BA02`, assumption `A-nn`, open item `OPEN-nn`. Numbers are never reused or renumbered. A new entry takes the next free number and is added to the registers in this file in the same pass.

### 4.2 Publishing the tags (ES-39, ES-28, ES-29)

The publishing tool is **OPEN:** OPEN-11 (Lena Varga). Nothing is published now. In every tool the track tag and release tag travel with every item, so each release stays identifiable:

| Tool | Track and release tags | Release grouping | Extra rules |
|---|---|---|---|
| Azure DevOps | Work-item **tags**, for example `track-azure` and `azure-r1` on one item | A query on the release tag lists the release | Add the tag `nw-workshop` and the participant prefix agreed with the facilitator (ES-28). Put the source identifiers (`BR-`, `NFR-`) in the description (ES-29). |
| GitHub | Issue **labels**, for example `track-azure` and `azure-r1` | **One milestone per release**, named after it (for example `azure-r1`) | Titles, descriptions and source identifiers follow ES-28 and ES-29. |
| Jira | **Labels**, for example `track-azure` and `azure-r1` | **One fix version per release**, named after it | Titles, descriptions and source identifiers follow ES-28 and ES-29. |

Titles start with the item ID. The tool tags are separate from the Git tag in section 4.3.

### 4.3 Git tags

* Each release has one Git tag, `product/<track>-r<n>`, for example `product/azure-r1` (ES-31, A-08).
* **A Git tag is created only after the product owner approves the release and the commit that holds the approved files is made.** All seven releases were approved on 2026-10-30. The commit and the seven Git tags were created on 2026-10-30 (section 9).
* Lena Varga acts as product owner and approves each release (A-29). Marc Dubois confirms that arrangement.

## 5. Master register of assumptions (ES-03)

All 46 assumptions, `A-01` to `A-46`. Wording is identical in every document that repeats an ID (section 7 says how this was checked). Every assumption has a person who can confirm it. None is a requirement. "Used in" lists every document that cites the ID, using the short names in section 1.3.

| ID | Assumption | Owner who can confirm | Used in |
|---|---|---|---|
| A-01 | File names under `docs/product/` as pinned in `README.md` section 2 | Lena Varga | BRD, PRD |
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga | BRD, PRD, BL, TR, AZ1, AZ2, DN1, DN2 |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali | BRD, PRD, EXP, BL, AZ1, AZ2, DN1, DN2, DN4 |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga | BRD, PRD, EXP, BL, TR, DN2, DN4 |
| A-05 | Confirmed, Delivered and Cancelled are manual staff actions today | Order Desk team via Lena Varga | BRD, PRD, EXP, BL, DN2 |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali | BRD, PRD, EXP, BL, AZ1, DN2, DN4 |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga | BRD, PRD, EXP, BL, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga | BRD, PRD, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-09 | The cost model assumes SQL and private endpoints are the main spend | Ahmed Benali | BRD, PRD, EXP, BL, AZ1 |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali | BRD, PRD, EXP, BL, AZ1, AZ2 |
| A-11 | NFR-01 covers the Order Desk and the portal; availability is measured by a probe | Lena Varga | BRD, PRD, BL, AZ1, AZ2 |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga | BRD, PRD, BL, TR, AZ1, AZ2, AZ3, DN1, DN2 |
| A-13 | The portal is a responsive web site for current browsers (mobile via browser) | Sofie Peeters, Ahmed Benali | BRD, PRD, BL, DN2 |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois | BRD, PRD, BL, TR, AZ1, AZ2, AZ3, DN2, DN3, DN4 |
| A-15 | The BRD keeps the business-case identifiers `C-01`..`C-08` for constraints | Lena Varga | BRD, PRD |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga | BRD, PRD, EXP, BL, TR, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-17 | Move items without a BR or NFR (SMTP relay CS-12, invoice share CS-08/CS-11, monitoring CS-22, DR CS-23, pipeline CS-19) are enabler stories tagged by track | Lena Varga | BRD, PRD, BL, AZ2 |
| A-18 | BR-10 stories are small: show the channel, filter by it, and set the Portal channel on the server | Lena Varga | BRD, PRD, BL, DN1, DN2 |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali | BRD, PRD, EXP, BL, AZ1, AZ2, DN4 |
| A-20 | `ShippedAt` and `Carrier` must be stored for BR-09 | Ahmed Benali | BRD, PRD, BL, TR, DN4 |
| A-21 | Entra External ID pricing and limits, and .NET 10 on Azure App Service, are not verified | Ahmed Benali | BRD, PRD, BL, DN2 |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali | BRD, PRD, EXP, BL, AZ1, AZ2, DN1, DN2, DN3, DN4 |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali | BRD, PRD, EXP, BL, AZ1, AZ2 |
| A-24 | The people named as owners of OPEN items (BRD section 5) are proposals taken from the stakeholder list; Lena Varga, as backlog owner, confirms them | Lena Varga | BRD, PRD, EXP |
| A-25 | Risk likelihood and impact ratings in BRD section 13 are judgements for discussion and not figures from the business case | Lena Varga | BRD, PRD, EXP |
| A-26 | The feature IDs `FT-AZ-01`..`FT-AZ-11` and `FT-DN-01`..`FT-DN-25` in PRD section 5 are the baseline for `backlog.md`. The backlog reuses them, may add new numbers, and never renumbers. The unplanned parent epic `EP-DN-08` is a proposed name | Lena Varga | PRD, EXP, BL, DN4 |
| A-27 | The personas in section 2 are working descriptions built from the roles in the business case (section 1, section 5) and CS-03. They are not based on customer interviews | Lena Varga | PRD |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali | PRD, EXP, BL, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois | PRD, EXP, BL, TR, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-30 | The owner of `MVE-BA01` is Ahmed Benali and the owner of `MVE-BA02` is Lena Varga. The owner runs the test, records the result and proposes the decision. The product owner agrees any change to the backlog | Lena Varga | EXP, BL, AZ1 |
| A-31 | The elapsed times, effort in person-days, group size of about 10 customers, daily staff time of about 30 minutes and proposed run windows (late November to mid-December 2026 for `MVE-BA01`; January to February 2027 for `MVE-BA02`) are planning estimates. The owners set the real dates. The year-end is assumed to be a busy period for customers | Lena Varga, Ahmed Benali | EXP, AZ1 |
| A-32 | The format of the exchange files is taken from reading `database/003-stockpilot-exchange.sql` and from how the command-line tool normally behaves, not from a real file. Assumed: the order file uses `;` as separator, has no header row, does not put quotes around values, uses the database server's default character set, and has no defined row order. The shipment file has a header row and `;` as separator. Real files from Antwerp may differ | Ahmed Benali | EXP, BL, AZ1 |
| A-33 | "Where is my order?" calls are unevenly spread across customers, so a group of about 10 heavier callers gives a baseline that can be measured. Most of these calls ask whether an order was received, picked or shipped. The call reasons are not recorded in the business case | Lena Varga | EXP, BL, DN4 |
| A-34 | A status e-mail built by hand from the Order Desk screens at 08:00 is a fair stand-in for the portal status view for this test: the portal would show the same data with the same 02:00 freshness for Picking and Shipped | Lena Varga | EXP |
| A-35 | The two status options in `FT-DN-26` (show the time each status last changed; explain Picking and Shipped in plain words) come from the pivot outcome of `MVE-BA02`. They are unplanned until the result is known. If the product owner plans them, the feature and its stories take the same track tag and the same release tag together (for example `dotnet-r2`) | Lena Varga | BL, DN2, DN4 |
| A-36 | The priorities of unplanned items are provisional: Dutch (BR-11) Should, field-level audit Could, status options Should, Order Desk API Could. The epic `EP-DN-08` takes the highest of them | Lena Varga | BL, TR, DN4 |
| A-37 | Test figures not given in the business case. NFR-02 is tested with 60 users at once (the staff peak, CS-03), a test company with about 500 orders in 24 months, a test order with 100 lines, 20 orders per page, over 10 minutes. NFR-01 uses a probe about every 5 minutes, an alert after two failed checks in a row, and a calendar-week measurement (84 business hours, about 25 minutes of downtime allowed at 99.5 %) | Lena Varga, Ahmed Benali | BL, AZ1, AZ2, DN2 |
| A-38 | The cutover has a go/no-go point at 09:00 CET, the rollback must finish before 12:00 CET, the cutover and rollback leave at least 30 minutes spare, and the data check takes under 30 minutes. These are planning figures inside the Sunday window of 06:00 to 12:00 CET (CS-21) | Ahmed Benali | BL, AZ2 |
| A-39 | Resource abbreviations in names (for example `rg`, `kv`, `app`) follow the Microsoft Cloud Adoption Framework abbreviation list. ES-23 gives the pattern and one example, not a list | Ahmed Benali | BL, AZ1 |
| A-40 | ASP.NET MVC 5 does not run on .NET 10, so the `Web` project moves to ASP.NET Core MVC with the same routes, screens and behaviour. The project boundaries stay as they are (ES-13) | Ahmed Benali | BL, DN1 |
| A-41 | Until OPEN-16 is answered, the portal shows each customer's net unit price and the net line and order totals, and no discount breakdown | Lena Varga | BL, DN2 |
| A-42 | A reorder keeps the delivery address of the copied order. Changing the address in the portal is not part of the pilot | Lena Varga | BL, DN2 |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga | BL, AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 |
| A-44 | `MVE-BA02` compares the pilot group's calls with its own earlier 4 weeks, not the 2 weeks first planned. Call volume is low (about 0.36 calls per customer per week), so 2 weeks would give too few calls to compare | Lena Varga | EXP |
| A-45 | The cost "at risk" threshold is EUR 1,350 per month, 10 % under the EUR 1,500 ceiling (C-04). A full option above it is flagged "at risk" | Lena Varga, Ahmed Benali | EXP, BL, AZ1 |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga | BRD, PRD, EXP, TR, DN2, DN4 |

## 6. Master register of OPEN items (ES-04)

All 33 open items, `OPEN-01` to `OPEN-33`. None blocks the documents. "Releases that state it" lists the release files that have the ID in their own OPEN tables (sections 7.2 and 9 of each release file). "Other documents" lists the core documents that cite the ID.

| ID | Question or dependency | Person who can answer | Track(s) affected | Releases that state it | Other documents |
|---|---|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) | AZ1, AZ2, DN2, DN4 | BRD, PRD, EXP, BL, TR |
| OPEN-02 | Source of Confirmed, Delivered, Cancelled status | Lena Varga with the Order Desk team | .NET | DN2 | BRD, PRD, EXP, BL |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET | AZ1, AZ2, DN1, DN2 | BRD, PRD, EXP, BL, TR |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | AZ1, AZ2, AZ3, DN1, DN2 | BRD, PRD, EXP, BL, TR |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | AZ1, AZ2, DN2, DN3, DN4 | BRD, PRD, EXP, BL, TR |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET | AZ2, AZ3, DN1, DN3 | BRD, PRD, BL |
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | Azure | AZ1, AZ2 | BRD, PRD, EXP, BL |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET | AZ1, AZ2, DN2 | BRD, PRD, BL, TR |
| OPEN-09 | 24 months of orders exist; where `Orders.InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | .NET | DN1, DN2, DN3 | BRD, PRD, BL |
| OPEN-10 | Data-protection requirement for customer users (Ahmed Benali); mobile expectations (Sofie Peeters) | Ahmed Benali, Sofie Peeters | .NET | DN2 | BRD, PRD, EXP, BL |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | AZ1, AZ2, AZ3, DN1, DN2, DN3, DN4 | BRD, PRD, BL |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure | AZ1, AZ2, AZ3 | BRD, PRD, BL, TR |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET | AZ1, AZ2, DN1, DN2 | BRD, PRD, EXP, BL, TR |
| OPEN-14 | Dutch in the first release (business case OQ-02) | Sofie Peeters with Lena Varga | .NET | DN3, DN4 | BRD, PRD, BL, TR |
| OPEN-15 | Customer administrators for all customers or only large ones (business case OQ-03) | Lena Varga | .NET | DN3 | BRD, PRD, BL, TR |
| OPEN-16 | Show volume and Gold discounts to customers, or only the net price | Lena Varga | .NET | DN2 | BRD, PRD, BL |
| OPEN-17 | Is the free-text audit action enough for NFR-08 or are field-level changes needed | Lena Varga | .NET | DN2, DN4 | BRD, PRD, BL, TR |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET | AZ2, DN2, DN4 | BRD, PRD, EXP, BL, TR |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | AZ1, AZ2, DN1, DN2, DN3 | BRD, PRD, BL |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET | AZ1, AZ2, DN2, DN4 | BRD, PRD, EXP, BL |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Azure and .NET | AZ1, AZ2, DN1 | BRD, PRD, BL |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET | AZ2, AZ3, DN2 | BRD, PRD, BL, TR |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET | AZ1, AZ2, DN1, DN2 | BRD, PRD, EXP, BL |
| OPEN-24 | Informational, BA-03: BA-03 will need an Order Desk API. BA-03 is out of scope; no release depends on it | Ahmed Benali | Informational only (neither track) | DN4 | BRD, PRD, BL, TR |
| OPEN-25 | Verify Entra External ID pricing and .NET 10 on App Service | Ahmed Benali | .NET | DN2 | BRD, PRD, BL |
| OPEN-26 | Split `dotnet-r2` into a read-only slice and a reorder slice? | Lena Varga | .NET | DN2, DN4 | BRD, PRD, EXP, BL |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET | DN2, DN3 | PRD, EXP, BL, TR |
| OPEN-28 | Are "where is my order?" calls already counted by customer and by week (phone system or Order Desk records)? If not, who keeps the 4-week tally for `MVE-BA02`? | Lena Varga | .NET | DN4 | EXP, BL |
| OPEN-29 | Which about 10 customers take part in `MVE-BA02`, who approves contacting them, and is a data-protection or consent step needed before sending a trial status e-mail? | Lena Varga with Sofie Peeters; data-protection check by Ahmed Benali | .NET | DN4 | EXP, BL |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | Azure | AZ1, AZ2 | EXP, BL |
| OPEN-31 | Where do the numbers for SM-02, SM-03 and SM-04 come from (call tally, "order line corrected after entry", invoice requests handled by staff), and how is a correction defined? The business case gives baselines but no record | Lena Varga | .NET | DN4 | BL, TR |
| OPEN-32 | Which EU secondary region, if any, is used for disaster recovery and EU-resident copies (ES-20, NFR-03)? | Ahmed Benali | Azure | AZ1, AZ2 | BL |
| OPEN-33 | How do the first customer users get an account and a link to their company in `dotnet-r2`, before the customer administrator feature (`dotnet-r3`) exists? Option: Northwind staff or IT create and link the accounts for the 20 pilot customers | Lena Varga with Ahmed Benali | .NET | DN2, DN3 | BL |

## 7. Register consistency notes

Method: every table row whose ID is `A-nn` or `OPEN-nn`, in the "Assumptions" and "OPEN items" sections of all 12 other documents, was read. For each ID, the text, the owner or person, and the track column were compared across documents. A script then checked that every `A-` and `OPEN-` ID cited in a file has a row in that same file. No other document was changed by this check.

**Result.** All 46 assumptions and all 33 OPEN items are defined in at least one document and are in sections 5 and 6. No ID is missing and no ID outside `A-01` to `A-46` or `OPEN-01` to `OPEN-33` is used. Owner and person columns agree everywhere. Wording is identical in every document that repeats an ID, including A-25, and the section numbers inside A-01, A-24, A-25, A-26, A-28 and A-43 name the file they point to, so they are correct in every file that repeats them. The first-definition markers have been removed. Every ID cited in a file has a row in that file. PRD section 10 and the release files agree on which releases state each cross-track OPEN item, and the release status wording is the same in the PRD and in the release files. No difference is open. One note remains:

| # | Finding | IDs | Files | What to do |
|---|---|---|---|---|
| 1 | **IDs defined in one document only.** They are not used elsewhere, so no second wording exists. | A-27 (PRD only); A-34 (EXP only); A-44 (EXP only) | `product-requirements.md`, `experiments.md` | Nothing. The register here is complete. |

## 8. Cross-track dependencies: no release waits for another track

Every cross-track dependency is an **OPEN:** item (ES-31). The table shows which releases state each one in their section 7.2, and what each track does **without** the answer. That position is an **ASSUMPTION:** (A-28) until the person who can answer decides. The wording comes from `backlog.md` section 8 and the release files. A check of all 12 other documents found no sentence saying that a release "requires", is "blocked by" or "waits for" a release of the other track. Each such phrase appears only in a rule that forbids it.

| OPEN item | Who can answer | Azure releases that state it | .NET releases that state it | What the Azure track does without the answer | What the .NET track does without the answer |
|---|---|---|---|---|---|
| OPEN-01 Freshness of order status (BR-04) | Lena Varga | `azure-r1`, `azure-r2` | `dotnet-r2` | Keeps the nightly 02:00 cadence and builds no faster refresh. | Shows status "as of the 02:00 batch" (A-04). |
| OPEN-03 Who modernises Order Desk code | Ahmed Benali with Lena Varga | `azure-r1`, `azure-r2` | `dotnet-r1`, `dotnet-r2` | Plans the cutover for Order Desk as it exists on the day, lists each point that breaks on the new platform, and changes no application code. | Does the Order Desk code modernisation itself (A-03). |
| OPEN-04 Owner and split of the EUR 1,500 ceiling | Marc Dubois | `azure-r1`, `azure-r2`, `azure-r3` | `dotnet-r1`, `dotnet-r2` | Reports the cost of the whole platform and applies no split. | Reports the hosting cost of the portal and applies no split. |
| OPEN-05 Meaning of "portal launch"; pilot hosting; pilot order volume | Marc Dubois, Lena Varga | `azure-r1`, `azure-r2` | `dotnet-r2`, `dotnet-r4` | Delivers `tst` and `prd` only and plans no pilot environment. | Builds to run in any environment that meets ES-20 and ES-25, and takes the launch date as a setting. |
| OPEN-06 How finance invoice output reaches Azure | Julien Moreau | `azure-r2`, `azure-r3` | `dotnet-r1`, `dotnet-r3` | Moves the existing PDFs and changes nothing in the finance system. | Reads invoices through a storage setting and assumes nothing about where Finance writes. |
| OPEN-12 `NWFS01` and SM-07 (Azure only) | Ahmed Benali | `azure-r2`, `azure-r3` | none | Retires `NWWEB01` and `NWSQL01` and reports SM-07 with and without `NWFS01`. | none |
| OPEN-13 Customer identity provider; platform sign-in plumbing | Ahmed Benali | `azure-r1` | `dotnet-r2` | Builds no sign-in plumbing (A-02). | Compares the options in the decision record, checks price and limits (OPEN-25), and starts customer sign-in once the choice is recorded. Other features do not wait. |
| OPEN-18 SMTP relay replacement and BR-09 | Ahmed Benali | `azure-r2` | `dotnet-r2`, `dotnet-r4` | Replaces the relay for the e-mail that CS-12 describes today and covers no new e-mail. | Prepares the message content and the hand-off. BR-09 stays "partly covered" until a mail path is named. |
| OPEN-19 Hosting and database target | Ahmed Benali | `azure-r1`, `azure-r2` | `dotnet-r1`, `dotnet-r2`, `dotnet-r3` | Names the setup it assumes in the decision record. | Uses draft handling that works on one or several instances. |
| OPEN-20 StockPilot exchange redesign; any schema change | Lena Varga (freshness), Ahmed Benali (schema) | `azure-r1`, `azure-r2` | `dotnet-r2`, `dotnet-r4` | Keeps the exchange files, cadence and paths identical and assumes no schema change. | Plans no schema change. Any change goes through a migration-impact check and a decision record (ES-19). |
| OPEN-21 CI/CD ownership | Ahmed Benali | `azure-r1` | `dotnet-r1` | Covers the infrastructure pipeline only. | Covers the build and test pipeline only. |
| OPEN-22 7-year audit retention against RPO and RTO | Lena Varga, Ahmed Benali | `azure-r2`, `azure-r3` | `dotnet-r2` | Backs up audit data on the same schedule as other order data and sets no retrieval target. | Deletes no audit rows and sets no sizing or retrieval target. |
| OPEN-23 Time zone and clock | Ahmed Benali | `azure-r1`, `azure-r2` | `dotnet-r1` | Keeps CET meaning for batch times and states the time zone in each item (A-10). | Shows times in CET and states it. |

Notes:

* The plan fixed which cross-track items each release states (for example `azure-r3`: OPEN-04 and OPEN-12). Several release files add items that their own stories cite (for example `azure-r1` adds OPEN-01, OPEN-20 and OPEN-23). Each release file lists these extras in its section 11.
* **OPEN-24** is informational. BA-03 is out of scope and no release depends on it.
* Azure-only items (OPEN-07, OPEN-12, OPEN-30, OPEN-32) and .NET-only items (OPEN-02, 09, 10, 14 to 17, 25 to 29, 31, 33) do not cross tracks. The releases state them with the working position in the item text.
* The experiments keep the same rule: `MVE-BA01` (Azure) and `MVE-BA02` (.NET) each run on their own, and a result that touches the other track is written as OPEN-01 or OPEN-20.

## 9. Review points for the product owner and approval checklist

### 9.1 Decisions needed

These are distinct decisions for Lena Varga as product owner, with the person named where another person must answer. None blocks reading the documents. These decisions stay open after the approval of 2026-10-30 and do not block the approved releases (OPEN-26, OPEN-27, A-03, A-07 and NFR-04 below).

| # | Decision | Where it shows | What the product owner decides | Who answers |
|---|---|---|---|---|
| 1 | **Split `dotnet-r2`?** (OPEN-26) | PRD section 7.2; `dotnet-r2.md` | `dotnet-r2` is the largest release (41 items, 4 epics). Keep it as one release, or split it into a read-only slice and a reorder slice to deliver value earlier. A split changes the release count, the tags, the release files and the counts in section 3 together. | Lena Varga |
| 2 | **Pilot language** (OPEN-27) | `dotnet-r2.md`, `dotnet-r3.md` section 11; BL | French and English (BR-11) are planned for `dotnet-r3`, and only the scaffold (`EN-DN-12`) is in `dotnet-r2`. Pilot customers may see English only (A-22, C15). Keep as planned, or pull BR-11 into `dotnet-r2`. | Lena Varga with Sofie Peeters |
| 3 | **Who owns the Order Desk modernisation** (A-03, OPEN-03) | BRD, PRD, `azure-r1.md`, `dotnet-r1.md` | A-03 says the .NET track modernises the code and the Azure track owns hosting, data and the exchange. This is the assumption with the biggest effect: if it is false, the content of `azure-r2` and `dotnet-r1` changes. | Ahmed Benali with Lena Varga |
| 4 | **Release dates** (A-07) | Section 3; all release files | Confirm or replace the targets. `azure-r3` by 30 June 2027 is the lease end (C-01). The `dotnet-r2` pilot starts in April 2027, before the Azure cutover in May 2027, so where the pilot runs is OPEN-05. `dotnet-r3` and `dotnet-r4` have no date. The 35 % portal share (SM-01) is "6 months after portal launch", which is not defined, and, under assumption A-46, the 20 pilot customers are not expected to show it, which depends on their order volume (OPEN-05; `dotnet-r4.md` section 11, difference 2). | Marc Dubois, Lena Varga |
| 5 | **NFR-04 has no Azure story** (A-02) | `traceability.md` sections 3.3 and 4; `azure-r2.md` section 4 | Confirm that the Azure side of NFR-04 (sign-in plumbing) stays "OPEN-13, no Azure story". If OPEN-03 or OPEN-13 gives the plumbing to Azure, add an Azure story with the next free number (`US-AZ-020`) in `azure-r1` or `azure-r2`. Nothing waits for the answer. | Ahmed Benali (OPEN-13); Lena Varga |

Other points the documents already flag, for information:

* BR-09 (shipped e-mail) is "partly covered" until the mail path is named (OPEN-18). It is a Could item.
* Some measure and unplanned stories have a lower priority than the requirement they cite (`US-DN-030`, `US-DN-035` to `US-DN-037`). Unplanned priorities are provisional (A-36).
* `FT-DN-25` (Order Desk API for reuse, unplanned) is about BA-03 and cites OPEN-24 only, so no BA-03 identifier is used as a source. It is held back and has no stories (OPEN-24).
* `traceability.md` section 8.2 lists the one informational difference that remains: the supporting items for BR-13 are marked `†` because their own source lines do not cite it. None leaves a requirement uncovered.
* The consistency pass also corrected backlog sections 5 and 5.4, removed NFR-06 from `US-DN-019` and from the `azure-r1` coverage text, made criterion 3 of `US-AZ-008` stand inside `azure-r2`, and aligned the register notes in section 7.

### 9.2 Approval checklist per release (all seven approved on 2026-10-30)

**The commit and the Git tags are made only after approval, by the product owner, one release at a time.** All seven releases were approved on 2026-10-30 in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). The commit and the Git tags were created on 2026-10-30. Tool tags (section 4.2) are published later and only after OPEN-11 is answered. Each release file also has its own approval block (section 13), now completed.

Use this list for every release. Replace `<release>` and `<tag>` with the values below.

* [x] I have read the release file and its item list. The members match the backlog register (`backlog.md` section 11).
* [x] Each cross-track OPEN item in section 7.2 is visible to the person named, and I accept that the release starts without an answer (A-28).
* [x] The review points in section 9.1 that affect this release are decided or accepted as open.
* [x] The definition of done (section 12 of the release file) is accepted.
* [x] The approval is recorded in the release file, section 13 (approver, date, status).
* [x] The commit that holds the approved files is made.
* [x] The Git tag `<tag>` is created on that commit, and the date and person are recorded.

| Release | Items | Git tag | Review points to settle first | Approved |
|---|---|---|---|---|
| `azure-r1` | 17 | `product/azure-r1` | 3 (A-03), 4 (A-07), 5 (NFR-04 Azure story) | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `azure-r2` | 22 | `product/azure-r2` | 3 (A-03), 4 (A-07), 5 | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `azure-r3` | 8 | `product/azure-r3` | 4 (A-07, lease end) | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `dotnet-r1` | 15 | `product/dotnet-r1` | 3 (A-03), 4 (A-07) | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `dotnet-r2` | 41 | `product/dotnet-r2` | 1 (OPEN-26), 2 (OPEN-27), 4 (A-07, OPEN-05), 5 | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `dotnet-r3` | 10 | `product/dotnet-r3` | 2 (OPEN-27), 4 (not dated) | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |
| `dotnet-r4` | 11 | `product/dotnet-r4` | 4 (not dated, SM-01) | [x] Approved 2026-10-30. [x] Committed. [x] Tag created. |

Per-release checklist, to copy into the release record:

| Release | Release file read | OPEN items accepted | Review points decided | Done criteria accepted | Approval recorded | Commit made | Tag created |
|---|---|---|---|---|---|---|---|
| `azure-r1` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/azure-r1` |
| `azure-r2` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/azure-r2` |
| `azure-r3` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/azure-r3` |
| `dotnet-r1` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/dotnet-r1` |
| `dotnet-r2` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/dotnet-r2` |
| `dotnet-r3` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/dotnet-r3` |
| `dotnet-r4` | [x] | [x] | [x] | [x] | [x] | [x] | [x] `product/dotnet-r4` |

## 10. Document boundary and status

* The seven release files were approved on 2026-10-30; the commit and the Git tags were created on 2026-10-30. The other six files remain drafts for review. Nothing is implemented, deployed or published (ES-27, A-16).
* No secret, key, connection string, tenant ID or subscription ID appears in this file (NFR-05).
* The Git tags `product/azure-r<n>` and `product/dotnet-r<n>` are created only after the product owner approves each release (ES-31, A-08, A-29). All seven were approved on 2026-10-30 and the tags were created on the approval commit.
