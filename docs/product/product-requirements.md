# Northwind Traders — Product requirements: Platform and data-centre exit (BA-01) and Ordering and customer self-service (BA-02)

| Field | Value |
|---|---|
| Document | Product requirements document (PRD), deliverable D2 |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`, releases `azure-r1` to `azure-r3`) and **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`, releases `dotnet-r1` to `dotnet-r4`). **BA-03** is out of scope (section 3.2). |
| Product owner (proposed) | Lena Varga, Head of Customer Operations, owns the product backlog (A-29) |
| Sponsor | Marc Dubois, Chief Operating Officer (COO) |
| Builds on | `docs/product/business-requirements.md` (the business requirements document, BRD, deliverable D1). Its IDs and wording are reused. |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01 to ES-07, ES-13 to ES-27, ES-30, ES-31, ES-39). Findings from reading `src/` and `database/` are used only to explain risk and are marked **ASSUMPTION:** (A-22, A-23). |
| Boundary | This document describes the product at product level. It has no solution design and no code. Nothing is deployed, committed or tagged in Git (ES-27). |

How to read this document:

* **PRD** means product requirements document. It says *what* the product must do and *in which release*. The BRD says *why*.
* IDs such as `BR-05`, `NFR-02`, `C-01`, `SM-01`, `P-01` and `OQ-01` come from the business case. `CS-` IDs come from `current-state.md`. `ES-` IDs come from the engineering standards. `BA-` means business area.
* Priorities use MoSCoW: **Must**, **Should**, **Could**. NFR means non-functional requirement. A feature or enabler takes the priority of the business requirement it serves.
* Every requirement cites its source in the form `(source: BR-05, CS-10)` (ES-02).
* **ASSUMPTION:** marks anything not stated in `knowledge-docs`. All are listed in section 14 with a person who can confirm them (ES-03).
* **OPEN:** marks an unanswered question. All are listed in section 15 with the person who can answer them (ES-04).
* Item IDs follow the plan: epic `EP-<AZ|DN>-nn`, feature `FT-<AZ|DN>-nn`, enabler story `EN-<AZ|DN>-nn`. `AZ` is the Azure track and `DN` the .NET track. User stories (`US-`) are written in `backlog.md`, not here.

## 1. Product vision and problem

### 1.1 Vision

Northwind Traders is a business-to-business (B2B) distributor of specialty food products. It is based in Lyon, with a second warehouse in Antwerp. It supplies about 1,150 active business customers in France, Belgium and Luxembourg. 38 of its 240 employees work in Customer Operations, called the "Order Desk" (source: business-case §1, CS-03, CS-05).

*Order Desk* is also the name of the internal web application that staff use to enter and manage orders. It was built in 2013 on ASP.NET MVC 5 and .NET Framework 4.8 and runs in the company's own data centre in Lyon (source: CS-01, CS-06, CS-07).

The product vision has two parts, one for each delivery track:

* **Azure track (BA-01).** Order Desk and its database run in Microsoft Azure before the data-centre lease ends on 30 June 2027. Staff keep working through the move. The nightly exchange with the warehouse system StockPilot keeps working. Availability, recovery and cost targets are met (source: C-01, BR-13, C-03, NFR-01, NFR-06, C-04, business-case §3, §4).
* **.NET track (BA-02).** Business customers have a secure web Customer Portal. They sign in, see their own orders and the status, reorder, and later get invoices. Order Desk is upgraded so the portal can safely use it, and it stays the single source of truth for orders (source: business-case §3, §4, BR-01 to BR-12, C-05).

### 1.2 Problems the product solves

| ID | Problem | Track | Source |
|---|---|---|---|
| P-01 | About 1,900 orders per week are entered by hand. 62 % arrive by phone or e-mail. | .NET | (source: P-01, CS-05) |
| P-02 | 4.1 % of order lines need a correction after entry because of re-keying. | .NET | (source: P-02, SM-03) |
| P-03 | Customers cannot see order status. About 410 "where is my order?" calls per week, about 35 % of inbound calls. | .NET | (source: P-03, SM-02) |
| P-04 | Reordering is slow. 70 % of orders repeat a previous order with small changes. | .NET | (source: P-04, BR-05) |
| P-05 | Staff search a file share and e-mail invoice copies by hand, about 120 requests per week. | .NET | (source: P-05, SM-04, CS-08, CS-11) |
| (none) | The platform has to leave the data centre. Both servers are past end of support, and Northwind pays extra to keep them secure. The platform need is not a numbered problem in the business case. | Azure | (source: C-01, C-02, SM-07) |

P-06 (delivery claims) belongs to BA-03 and is out of scope (section 3.2).

## 2. Users and personas

Personas are working descriptions built from the roles in the business case. They are not based on interviews (A-27).

| Persona | Who they are | What they need from the product | Track | Source |
|---|---|---|---|---|
| Order Desk clerk | One of 38 Customer Operations staff. Enters and manages orders in Order Desk every day. About 60 staff and others work at the Monday 08:00 to 11:00 peak. | Keep working through the move. See whether an order came from the portal or from staff. Stop re-keying portal orders. | Azure, .NET | (source: CS-03, BR-10, BR-13, BR-06) |
| Customer purchasing user | A grocer, chef or purchasing staff member at one of about 1,150 customers. | Sign in. See own orders and status. Reorder fast. Get invoices. See own negotiated prices. | .NET | (source: business-case §5, BR-01 to BR-07, BR-12) |
| Customer administrator | A person at a customer who manages the users of that customer. | Invite and remove users of their own company. | .NET | (source: BR-08, OQ-03) |
| Belgian customer and account manager | Customers in Belgium, supported by Sofie Peeters, Key Account Manager. | Dutch language. Use on mobile devices through the browser. | .NET | (source: business-case §5, BR-11, OQ-02, A-13) |
| Head of Customer Operations (Lena Varga) | Business owner. Wants fewer calls and fewer errors. Owns the backlog. | Releases ordered by value. Clear measures. | Both | (source: business-case §5) |
| Sponsor (Marc Dubois, COO) | Wants to exit the data centre on time and within budget. | A date-safe move, a cost ceiling, a closing measure (SM-07). | Azure | (source: business-case §5, C-01, C-04) |
| IT Manager and team (Ahmed Benali, 6 people) | Run the platform. Know .NET and SQL Server well, with limited container skills. | Platforms the team can operate. Secure, low-cost and recoverable. | Both | (source: business-case §5, C-06, ES-21) |
| Finance (Julien Moreau) | Finance system writes invoices and credit notes. Other applications only show them. | A clear hand-off for invoice files. No change to the finance system. | Azure, .NET | (source: business-case §5, CS-11, business-case §6) |
| Warehouse supervisor, Antwerp (Pieter Janssens) | Uses StockPilot, which exchanges files with Order Desk. | The nightly exchange keeps working with no change to StockPilot. | Azure | (source: business-case §5, CS-10, C-03) |

## 3. Scope

### 3.1 In scope

| Area | Name | Delivery track | Track tag | Releases |
|---|---|---|---|---|
| BA-01 | Platform and data-centre exit | Azure | `track-azure` | `azure-r1`, `azure-r2`, `azure-r3` |
| BA-02 | Ordering and customer self-service | .NET | `track-dotnet` | `dotnet-r1`, `dotnet-r2`, `dotnet-r3`, `dotnet-r4` |

In scope: BR-01 to BR-13, NFR-01 to NFR-08, C-01 to C-06, SM-01 to SM-04, SM-07, OQ-01 to OQ-03 (source: business-case §4; BRD section 3.1).

Each area is delivered by its own team on its own track and in its own numbered releases. Every epic, feature and story carries exactly one track tag. A story that would need both tracks is split into one story per track (ES-30). A release never waits for another track. A dependency between tracks is written as an **OPEN:** item (ES-31) (source: business-case §4, ES-30, ES-31).

### 3.2 Out of scope

**BA-03 Delivery claims and credit notes (Power Platform track, `track-power-platform`)** is out of scope. These identifiers are listed only so that nothing is lost (ES-06):

| Out-of-scope item | Identifiers |
|---|---|
| Business requirements | BR-14, BR-15, BR-16, BR-17, BR-18, BR-19 |
| Non-functional requirement | NFR-09 |
| Constraints | C-07, C-08 |
| Success measures | SM-05, SM-06 |
| Problem | P-06 |
| Open questions | OQ-04, OQ-05 (no release in this scope waits for them) |
| Current-state facts | CS-24 to CS-28 |
| Standards for Power Platform | ES-32 to ES-37 |
| Timeline item | Delivery claims pilot in Q1 2027 |

NFR-03 and NFR-04 are shared with BA-03. They are in scope here only for BA-01 and BA-02.

**Exclusions in business case section 6** (first release):

* Online payment. Customers continue to pay by bank transfer on invoice.
* A native mobile app. A responsive web portal is enough for now (A-13).
* Changes to StockPilot, the warehouse system in Antwerp.
* Replacing the finance system that produces invoices and credit notes.
* Customers recording claims themselves in the portal. (Claims belong to BA-03.)

(source: business-case §6, C-03)

**OPEN:** OPEN-24 (informational). BA-03 will need an Order Desk programming interface (API). This is noted here only so that it is not lost. No release in this scope depends on it. No story is written for it.

## 4. The two business areas as product capabilities

| Capability | Business area | What the product does for the user | Features (section 5) | Releases | Source |
|---|---|---|---|---|---|
| **Order Desk in Azure** | BA-01 (`track-azure`) | Order Desk and its database run in Azure. Staff are not stopped by the move. The warehouse exchange continues. Old servers are retired. | FT-AZ-01 to FT-AZ-11 | `azure-r1` to `azure-r3` | (source: business-case §4, BR-13, C-01, C-03, SM-07) |
| **Modernised Order Desk** | BA-02 (`track-dotnet`) | Order Desk moves to a current platform with the same behaviour, so the portal can safely build on it. Staff see the order channel. | FT-DN-01 to FT-DN-04 | `dotnet-r1` | (source: business-case §4, BR-10, CS-01, CS-02, CS-13 to CS-20, ES-13 to ES-19) |
| **Customer Portal** | BA-02 (`track-dotnet`) | Customers sign in, see their own orders and status with their own prices, reorder, and submit orders that reach Order Desk. Later: invoices, customer administrators, French and English, a shipped e-mail and measures. | FT-DN-05 to FT-DN-22 | `dotnet-r2` to `dotnet-r4` | (source: BR-01 to BR-12, NFR-02, NFR-04, NFR-07, NFR-08, C-05) |

**ASSUMPTION:** The .NET track owns the modernisation of the Order Desk code. The Azure track owns hosting, data and the StockPilot exchange (A-03). **OPEN:** The two business-case descriptions overlap on "the upgrade of Order Desk" (OPEN-03).

## 5. Functional requirements per capability

### 5.1 How feature IDs work

* Features are the product-level functional requirements. Each feature has one track tag and at most one release tag (ES-30, ES-31).
* The feature IDs below are the baseline for `backlog.md`. The backlog reuses them. It may add features with new numbers. It never renumbers (A-26).
* Enabler stories (`EN-`) are preparation work that must come before the features that use them. They are named in the "Enablers" column (ES-31).
* Priority of an enabler follows the feature it unblocks (A-12, A-17).
* The detailed stories, with As a / I want / so that and Given / When / Then, are in `backlog.md`. Nothing here is a design.

### 5.2 Capability: Order Desk in Azure (`track-azure`)

| Feature | Requirement at product level | Enablers | Priority | Release | Source |
|---|---|---|---|---|---|
| `FT-AZ-01` Azure foundation and network | A named Azure foundation exists for a test environment (`tst`) and a production environment (`prd`) in France Central. It has a private network for data services and an automated pipeline for infrastructure code. It is checked locally with `az bicep build`. Nothing is deployed. | `EN-AZ-01`, `EN-AZ-02`, `EN-AZ-07` | Must | `azure-r1` | (source: C-01, NFR-03, CS-09, CS-19, ES-20, ES-22 to ES-25, ES-27) |
| `FT-AZ-02` Hosting and data decision with a cost model | The product owner can read a recorded decision on where Order Desk and its database run, with a monthly cost estimate for production plus one test environment against the EUR 1,500 ceiling. | `EN-AZ-03`, `EN-AZ-12` | Must | `azure-r1` | (source: C-02, C-04, C-06, ES-21, A-09, OPEN-04, OPEN-19) |
| `FT-AZ-03` Secrets and monitoring baseline on `tst` | No password or key is kept in code or pipelines. Applications reach data services without passwords. Availability is measured by a probe, and logs from every resource go to one place per environment. This replaces ping checks and a weekly look at the Event Log. | `EN-AZ-04`, `EN-AZ-05` | Must | `azure-r1` | (source: NFR-05, NFR-01, CS-22, ES-17, ES-25, ES-26, A-11) |
| `FT-AZ-04` StockPilot exchange proof | The outcome of experiment `MVE-BA01` is recorded: the nightly exchange can be reproduced with the same files, the same 02:00 cadence and the same paths, and Antwerp's file-transfer (SFTP) details are known. | (feature stories) | Must | `azure-r1` | (source: CS-10, C-03, A-23, OPEN-07, OPEN-20) |
| `FT-AZ-05` Production environment and Antwerp connection | A production environment has secrets, monitoring and EU-resident data, and a connection path to the Antwerp file-transfer host. | `EN-AZ-14` (plus follow-on stories for NFR-05, NFR-01 and NFR-03 on `prd`) | Must | `azure-r2` | (source: BR-13, NFR-01, NFR-03, NFR-05, CS-09, CS-10, OPEN-07) |
| `FT-AZ-06` Backup, disaster recovery and tested restore | Order data can be recovered with at most 1 hour of lost data (RPO) and in at most 4 hours (RTO). A restore is tested and reported. Today the last disaster-recovery test was never. | `EN-AZ-06` | Must | `azure-r2` | (source: NFR-06, CS-07, CS-23, OPEN-22) |
| `FT-AZ-07` Data move: database and invoice files | The 48 GB database (growing about 1 GB per month) is moved in a rehearsal inside the Sunday window. About 120 GB of invoice PDFs (growing about 2 GB per month) are moved to a store Order Desk can read. | `EN-AZ-08`, `EN-AZ-10` | Must | `azure-r2` | (source: BR-13, CS-07, CS-08, CS-11, CS-21, OPEN-06) |
| `FT-AZ-08` Nightly exchange and mail relay in Azure | The nightly 02:00 StockPilot exchange runs from Azure with the same file formats and no change to StockPilot. A replacement for the internal mail relay exists. | `EN-AZ-09`, `EN-AZ-11` | Must | `azure-r2` | (source: CS-10, CS-12, C-03, A-19, OPEN-18, OPEN-20, OPEN-23) |
| `FT-AZ-09` Sunday-window cutover and rollback | Production cutover happens inside the Sunday window, 06:00 to 12:00 CET, with a runbook and a rollback. Staff keep working. | `EN-AZ-13` (plus cutover feature stories) | Must | `azure-r2` | (source: BR-13, CS-21, C-01) |
| `FT-AZ-10` Retire the old servers | `NWWEB01` and `NWSQL01` are decommissioned. The file server `NWFS01` is decommissioned only if it counts (OPEN-12). SM-07 reaches 0. | (none) | Must | `azure-r3` | (source: SM-07, C-01, C-02, CS-06, CS-07, OPEN-12) |
| `FT-AZ-11` Closing cost check, recovery test report and runbooks | The run cost is checked against the EUR 1,500 ceiling. A disaster-recovery test report and runbooks exist. | (none) | Must | `azure-r3` | (source: C-04, NFR-06, CS-23, ES-09) |

### 5.3 Capability: Modernised Order Desk (`track-dotnet`)

| Feature | Requirement at product level | Enablers | Priority | Release | Source |
|---|---|---|---|---|---|
| `FT-DN-01` Current platform and safety net | Order Desk is on .NET 10 in SDK-style projects, with one solution and the same three projects. All tests run with `dotnet test` on Windows, macOS and Linux. Pricing results and test assertions do not change. A build and test pipeline exists. | `EN-DN-01`, `EN-DN-02`, `EN-DN-09` | Must | `dotnet-r1` | (source: CS-01, CS-02, CS-18, CS-19, CS-20, ES-13, ES-14, ES-18, ES-19) |
| `FT-DN-02` Configuration, logging and no secrets | Configuration and logging use the current platform methods. No secret and no Windows-sign-in database connection remain in the application's configuration. | `EN-DN-03`, `EN-DN-04`, `EN-DN-05` | Must | `dotnet-r1` | (source: NFR-05, CS-13, CS-15, CS-17, ES-15, ES-16, ES-17) |
| `FT-DN-03` Draft order and invoice storage free of one server | The order being entered no longer lives in one web server's memory. Invoice files are read through a storage setting, not a fixed network path. | `EN-DN-06`, `EN-DN-07` | Must | `dotnet-r1` | (source: CS-14, CS-16, A-22, OPEN-19) |
| `FT-DN-04` Staff see the order channel | Order Desk staff can see whether an order was placed through the portal or entered by staff, and can filter by it. | (none) | Must | `dotnet-r1` | (source: BR-10, CS-03, A-18) |

### 5.4 Capability: Customer Portal (`track-dotnet`)

| Feature | Requirement at product level | Enablers | Priority | Release | Source |
|---|---|---|---|---|---|
| `FT-DN-05` Portal architecture decision | A recorded decision says how the portal is added to Order Desk and which sign-in provider customers use. It checks cost and limits of the options. | `EN-DN-11` | Must | `dotnet-r2` | (source: OQ-01, NFR-04, ES-13, A-21, OPEN-13, OPEN-25) |
| `FT-DN-06` Customer data separation | A signed-in customer user is tied to one company, and every data read is limited to that company. | `EN-DN-10` | Must | `dotnet-r2` | (source: BR-01, C-05, A-22) |
| `FT-DN-07` Customer and staff sign-in | A customer user can sign in with an identity managed outside the application. Staff sign in with their Microsoft Entra ID accounts, not Windows Integrated Authentication. | `EN-DN-08` | Must | `dotnet-r2` | (source: BR-01, NFR-04, CS-04, OQ-01, OPEN-13) |
| `FT-DN-08` Portal data stays in the EU | Sign-in, mail and monitoring services used by the portal keep customer and order data in the European Union. | (none) | Must | `dotnet-r2` | (source: NFR-03, ES-20, A-02) |
| `FT-DN-09` See my orders | A customer user sees the list of their company's orders from the last 24 months with order date, status and total. Order list pages respond in under 2 seconds for 95 % of requests. | (none) | Must | `dotnet-r2` | (source: BR-02, NFR-02, CS-05, OPEN-08, OPEN-09) |
| `FT-DN-10` Order detail with my prices | A customer user opens an order and sees lines, quantities, delivery address, status and their own negotiated price. Pricing rules do not change. | (none) | Must | `dotnet-r2` | (source: BR-03, BR-12, CS-20, ES-18, OPEN-16) |
| `FT-DN-11` Order status as of the 02:00 batch | A customer user sees one of: Received, Confirmed, Picking, Shipped, Delivered, Cancelled. The status is as of the 02:00 batch (A-04). | (none) | Must | `dotnet-r2` | (source: BR-04, CS-10, C-03, A-04, A-05, OPEN-01, OPEN-02) |
| `FT-DN-12` Reorder by copying | A customer user creates a new order by copying a previous order, changing quantities or removing lines, then submitting. | (none) | Must | `dotnet-r2` | (source: BR-05, P-04, CS-16) |
| `FT-DN-13` Portal order reaches Order Desk | A submitted portal order appears in Order Desk as Received, without re-keying. The channel is set to Portal by the server. | (none) | Must | `dotnet-r2` | (source: BR-06, BR-10, C-05, A-18) |
| `FT-DN-14` Order change audit | Every change to an order records who, what, when and channel, and is kept 7 years. | `EN-DN-13` | Must | `dotnet-r2` | (source: NFR-08, CS-05, A-22, OPEN-17, OPEN-22) |
| `FT-DN-15` Language foundation | The portal is ready to show more than one language. | `EN-DN-12` | Should | `dotnet-r2` | (source: BR-11, A-22, OPEN-27) |
| `FT-DN-16` Accessibility baseline | Portal pages meet WCAG 2.2 level AA (Web Content Accessibility Guidelines) from the start. | `EN-DN-14` | Must | `dotnet-r2` | (source: NFR-07, BR-03, A-13) |
| `FT-DN-17` Invoice download | A customer user can download the PDF invoice of a delivered order. | (none) | Should | `dotnet-r3` | (source: BR-07, P-05, CS-08, CS-11, CS-14, OPEN-06, OPEN-09) |
| `FT-DN-18` Customer administrator | A customer administrator can invite and remove users of their own company. | (none) | Should | `dotnet-r3` | (source: BR-08, OQ-03, OPEN-15) |
| `FT-DN-19` French and English | The portal is available in French and English. | (none) | Should | `dotnet-r3` | (source: BR-11, OQ-02, OPEN-14) |
| `FT-DN-20` Keep shipment date and carrier | The shipment date and carrier that StockPilot sends are stored, so they can be shown and used. | `EN-DN-15` | Could | `dotnet-r4` | (source: BR-09, CS-10, A-20, OPEN-20) |
| `FT-DN-21` Shipped e-mail | A customer user receives an e-mail when an order changes to Shipped. | (none) | Could | `dotnet-r4` | (source: BR-09, CS-10, CS-12, OPEN-18) |
| `FT-DN-22` Measure the success measures | SM-01 to SM-04 are measured against their baselines. | (none) | Could | `dotnet-r4` | (source: SM-01, SM-02, SM-03, SM-04, OPEN-05) |

Unplanned candidates (track tag only, no release tag, no date). Their parent is an unplanned epic, which the backlog may call `EP-DN-08` (A-26):

| Feature | What it would add | Why it is not planned | Source |
|---|---|---|---|
| `FT-DN-23` Dutch language | Dutch text in the portal. | **OPEN:** Is Dutch needed in the first release? (OPEN-14) | (source: BR-11, OQ-02) |
| `FT-DN-24` Field-level order audit | Record which field changed in an order. | **OPEN:** Is the free-text audit action enough for NFR-08? (OPEN-17) | (source: NFR-08, A-22) |
| `FT-DN-25` Order Desk API for reuse | A programming interface that other systems could use. | Informational only. No story is written for BA-03. (OPEN-24) | (source: none in knowledge-docs in scope; OPEN-24, informational) |

## 6. Non-functional requirements, constraints and standards

### 6.1 Cross-cutting NFRs: one story per track (ES-30)

The business case gives no priority for NFR items. **ASSUMPTION:** All are treated as "Must" because each one gates a release that carries a Must outcome (A-12). Where the business case gives no way to measure an NFR, the measurement basis is **OPEN:** OPEN-08.

NFR-03, NFR-04 and NFR-05 apply wherever they are relevant. One story can carry only one track tag. Each therefore gets at least one story per track (A-02).

| NFR | Requirement (business case wording) | Azure track (platform side) | .NET track (application side) | Gates | Source |
|---|---|---|---|---|---|
| NFR-05 | No secret (password, connection string with password, key) in source code or configuration files in the repository. | `EN-AZ-04` in `azure-r1` (on `tst`). Follow-on on `prd` in `azure-r2`. No secret in infrastructure code or pipelines. | `EN-DN-05` in `dotnet-r1`. No password or secret in application configuration. | `azure-r1`, `dotnet-r1` | (source: NFR-05, CS-13, CS-17, ES-17, ES-25) |
| NFR-03 | Customer data and order data stay in the European Union. | `EN-AZ-01` in `azure-r1`: France Central, EU-only secondary region, EU-resident backups and logs. Follow-on on `prd` in `azure-r2`. | `FT-DN-08` in `dotnet-r2`: the portal's sign-in, mail and monitoring services keep customer data in the EU. NFR-03 is not listed for BA-02 in the business case (A-02). | `azure-r1`, `dotnet-r2` | (source: NFR-03, CS-09, ES-20, A-02) |
| NFR-04 | Customers sign in with an identity managed outside the application. Staff use Microsoft Entra ID. | **OPEN:** No Azure story, unless OPEN-03 or OPEN-13 gives platform sign-in plumbing to the Azure track. Traceability shows "OPEN-13, no Azure story" (A-02). | `FT-DN-07` and `EN-DN-08` in `dotnet-r2`: customer sign-in and staff Entra sign-in. | `dotnet-r2` | (source: NFR-04, CS-04, OQ-01, A-02) |
| NFR-06 | RPO 1 hour and RTO 4 hours for order data. (RPO is how much data may be lost. RTO is how long recovery may take.) | `FT-AZ-06` (`EN-AZ-06`) in `azure-r2`. Test report in `azure-r3`. Log backups every 15 minutes today (CS-07). | None. Linked to NFR-08 by OPEN-22. | `azure-r2` | (source: NFR-06, CS-07, CS-23, OPEN-22) |
| NFR-08 | Every change to an order (who, what, when, channel) is recorded for 7 years. | Backup, size and retrieval of 7 years of audit data (OPEN-22). | `FT-DN-14` (`EN-DN-13`) in `dotnet-r2`: audit content. | `dotnet-r2` | (source: NFR-08, BR-10, CS-05, OPEN-17, OPEN-22) |

### 6.2 Other NFRs

| NFR | Requirement | Track | Measure and basis | Gates | Source |
|---|---|---|---|---|---|
| NFR-01 | Availability of 99.5 % during business hours, Monday to Saturday 06:00 to 20:00 CET. | Azure | **ASSUMPTION:** It covers Order Desk and the portal and is measured by a probe (A-11). Business hours are 84 hours per week. If measured weekly, 99.5 % allows about 25 minutes of downtime. The measurement period is **OPEN:** OPEN-08. Today there is one server and ping checks only (CS-06, CS-22). | `azure-r2` | (source: NFR-01, CS-06, CS-22, A-11, OPEN-08) |
| NFR-02 | Order list and order detail pages respond in under 2 seconds for 95 % of requests. | .NET | **OPEN:** Load basis. Staff load is about 60 concurrent users at peak (CS-03). Portal load is unknown (OPEN-08). | `dotnet-r2` | (source: NFR-02, CS-03, OPEN-08) |
| NFR-07 | The portal meets WCAG 2.2 level AA. | .NET | **ASSUMPTION:** Responsive web site for current browsers (A-13). **OPEN:** Mobile expectations (OPEN-10). | `dotnet-r2` | (source: NFR-07, A-13, OPEN-10) |

### 6.3 Constraints

The business case `C-` IDs are kept as they are (A-15).

| ID | Constraint | Releases it shapes | How the product respects it | Source |
|---|---|---|---|---|
| C-01 | The data-centre lease ends on **30 June 2027**. Order Desk must run in Azure before that date. | `azure-r1`, `azure-r2`, `azure-r3` | Release order is fixed by this date. At least one spare Sunday window stays free before it. Target dates are **ASSUMPTION:** (A-07). | (source: C-01, CS-21, A-07) |
| C-02 | Windows Server 2012 R2 and SQL Server 2014 are past end of support. | `azure-r2`, `azure-r3` | Old servers are retired in `azure-r3`. This is measure SM-07. | (source: C-02, SM-07) |
| C-03 | StockPilot stays on premises in Antwerp until at least 2028. It does not change. | `azure-r1`, `azure-r2`, `dotnet-r2`, `dotnet-r4` | File formats, cadence and paths of the exchange stay as they are. | (source: C-03, CS-10, business-case §6) |
| C-04 | Target run cost of the Azure platform (Order Desk and portal, production and one test environment) is at most **EUR 1,500 per month**. | `azure-r1` (estimate), `azure-r3` (check), and any release that adds hosting cost | **ASSUMPTION:** Shared by both tracks (A-14). The estimate is in `azure-r1`. The closing check is in `azure-r3`. **OPEN:** Who is accountable (OPEN-04). | (source: C-04, A-09, A-14, OPEN-04) |
| C-05 | The portal reuses Order Desk as the single source of truth for orders. No second order database. | `dotnet-r2` | Portal orders use Order Desk data and numbering. | (source: C-05, CS-01, BR-06) |
| C-06 | The IT team (6 people) knows .NET and SQL Server well. It has limited experience with containers and Kubernetes. | All | Use platform services the team can operate. No Kubernetes (ES-21). | (source: C-06, ES-21) |

### 6.4 Engineering standards that shape every release

These are not business requirements. They limit how the work is delivered.

| Standards | What they mean here | Tracks | Source |
|---|---|---|---|
| ES-13 to ES-19 | One solution with `Core`, `Web` and `Tests`. SDK-style projects on .NET 10 (`net10.0`). Current configuration and logging methods. No secrets in code. `dotnet test src/Northwind.OrderDesk.sln` passes on Windows, macOS and Linux with no weakened assertions. Modernise in place and keep names and behaviour unless a decision record says otherwise. | .NET | (source: ES-13 to ES-19, CS-20) |
| ES-20 to ES-27 | France Central. Platform services, no Kubernetes. Infrastructure as code (IaC) in Bicep with Azure Verified Modules. Names `<resource-abbreviation>-nw-<workload>-<environment>-<region>` with environments `tst` and `prd`. Four tags on every resource: `workload`, `environment`, `owner`, `costCenter`. Data services reached through private endpoints with managed identities. One Log Analytics workspace per environment and Application Insights. Nothing is deployed. IaC is checked locally, for example with `az bicep build`. | Azure (and .NET where it uses the platform) | (source: ES-20 to ES-27) |
| ES-30, ES-31, ES-39 | One track tag per item. Release names `<track>-r<n>`. At most one release per item. No release waits for another track. Tags travel with every item when the backlog is published. | Both | (source: ES-30, ES-31, ES-39, OPEN-11) |
| ES-01 to ES-07 | Plain language, sources, assumptions, open items, stories, traceability and file locations. | Both | (source: ES-01 to ES-07) |

## 7. Release roadmap

### 7.1 Ordering rule

Releases follow priority. Must comes before Should, and Should before Could. Preparation work (enablers) comes before the features that need it. Within one track the order never depends on the other track (source: ES-31, business-case §4).

**Why enablers come first.**

* *Azure.* The StockPilot exchange and the database move are the biggest unknowns. They are proved early (`azure-r1`) so that rehearsals can run before cutover. The foundation, network, secrets and monitoring must exist before data moves (source: C-03, CS-10, CS-07, ES-25).
* *.NET.* Nothing for customers can be built safely on .NET Framework 4.8 with tests that only run in Visual Studio (source: CS-01, CS-18, ES-14, ES-18). **ASSUMPTION:** Order Desk does not limit data to the signed-in customer's company, so customer data separation (`EN-DN-10`) comes before every portal story that shows data (A-22).

### 7.2 Roadmap

Target dates are **ASSUMPTION:** and are targets, not commitments. Owners: Marc Dubois and Lena Varga (A-07).

| Track | Release | Theme | Target (A-07) | Business outcome |
|---|---|---|---|---|
| Azure | `azure-r1` | Foundation and proof | End of January 2027 | Biggest unknowns answered early. A cost estimate exists. |
| Azure | `azure-r2` | Production cutover | Rehearsal complete by end of April 2027. Cutover in a Sunday window in May 2027. | Order Desk runs in Azure. Staff keep working. |
| Azure | `azure-r3` | Stabilise and decommission | By 30 June 2027 | Old servers retired. SM-07 is 0. |
| .NET | `dotnet-r1` | Modernised Order Desk | End of February 2027 | Order Desk on a current platform with the same behaviour. Staff see the order channel. |
| .NET | `dotnet-r2` | Portal pilot: Must items | Pilot start in April 2027 | 20 pilot customers use the portal for the Must items. |
| .NET | `dotnet-r3` | Should items | Not dated | Invoices, customer administrators, French and English. |
| .NET | `dotnet-r4` | Could items and measures | Not dated | Shipped e-mail. SM-01 to SM-04 measured. |

(source: business-case §8, C-01, A-07)

Notes:

* The portal pilot (Q2 2027) and the lease end (30 June 2027) fall in the same quarter. **OPEN:** Whether the pilot runs on Azure before 30 June 2027 is OPEN-05.
* **OPEN:** OPEN-26. The product owner may split `dotnet-r2` into a read-only slice and a reorder slice if value is needed earlier. This PRD keeps one release.
* Discovery and planning run October to November 2026 (source: business-case §8). The delivery claims pilot in Q1 2027 is BA-03 and out of scope.

### 7.3 Release tag and Git tag convention

| Track | Track tag | Release tag | Git tag | Release file |
|---|---|---|---|---|
| Azure | `track-azure` | `azure-r<n>` (n = 1 to 3) | `product/azure-r<n>` | `docs/product/releases/azure-r<n>.md` |
| .NET | `track-dotnet` | `dotnet-r<n>` (n = 1 to 4) | `product/dotnet-r<n>` | `docs/product/releases/dotnet-r<n>.md` |

* Every planned item carries its track tag and exactly one release tag of the **same** track, for example `Tags: track-azure, azure-r2`. An unplanned item carries only the track tag, for example `Tags: track-dotnet`.
* A `track-azure` item may carry only `azure-r1` to `azure-r3`. A `track-dotnet` item may carry only `dotnet-r1` to `dotnet-r4`. A parent and its children share track and release (ES-30, ES-31).
* The Git tag `product/<track>-r<n>` is created **only after the product owner approves the release** and the commit that holds it is made (ES-31). All seven releases were approved on 2026-10-30, and the tags were created on the approval commit (A-08, A-29).
* The publishing tool (Azure DevOps, GitHub or Jira) is **OPEN:** OPEN-11. In any tool the tags travel with every item (ES-39).

## 8. Planned releases

Each release section follows the same order: goal, scope, requirements covered, constraints that apply, success measures moved, what is left out, and cross-track **OPEN:** items. For every cross-track item, the release says what it does without the answer. That is an **ASSUMPTION:** (A-28). No release waits for another track.

### 8.1 `azure-r1` — Foundation and proof (`track-azure`)

| Field | Value |
|---|---|
| Git tag | `product/azure-r1` (approved 2026-10-30; created on the approval commit) |
| Target | End of January 2027 (A-07) |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r1 |

**Goal.** Answer the biggest unknowns early, and prepare Azure for rehearsals. Show that the nightly StockPilot exchange can keep its files. Produce a cost estimate against EUR 1,500 per month (source: C-03, C-04, CS-10, A-23).

**Scope.** Epic `EP-AZ-01` Foundation and proof (`track-azure`, `azure-r1`):

| Feature | Enablers |
|---|---|
| `FT-AZ-01` Azure foundation and network | `EN-AZ-01` foundation (France Central, naming, tags, Bicep with Azure Verified Modules, `tst` and `prd` skeleton); `EN-AZ-02` network foundation and private endpoints; `EN-AZ-07` infrastructure pipeline |
| `FT-AZ-02` Hosting and data decision with a cost model | `EN-AZ-03` hosting and data decision record; `EN-AZ-12` cost model |
| `FT-AZ-03` Secrets and monitoring baseline on `tst` | `EN-AZ-04` secrets and managed identity; `EN-AZ-05` observability baseline |
| `FT-AZ-04` StockPilot exchange proof | Feature stories that record the `MVE-BA01` outcome |

**Requirements covered.** NFR-05 (platform), NFR-03 (platform), NFR-01 (design and measure), C-04 (estimate).

**Constraints and standards that apply.** C-01 (the date drives all targets), C-02, C-03 (the proof must keep the exchange files), C-04, C-06; NFR-01, NFR-03, NFR-05, NFR-06; ES-20 to ES-27. IaC is validated with `az bicep build`. Nothing is deployed (ES-27).

**Success measures moved.** None directly. This release lowers the risk to SM-07 (source: SM-07, R-02, R-05).

**Left out.** Production cutover, database move rehearsal, exchange build, invoice store, mail relay, backup and tested restore, and the Antwerp connection (all `azure-r2`). Decommissioning (`azure-r3`). Any Order Desk code change (OPEN-03). Any commitment to a portal pilot environment (OPEN-05).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Builds only hosting, data and exchange work (A-03). Makes no Order Desk code change. Lists, read-only, the points where the current application would break on the new platform. |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Estimates the whole platform (Order Desk and portal, `prd` and one `tst`) against the ceiling. Applies no split. |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Plans `tst` and `prd` only. Plans no separate pilot environment. |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Writes no sign-in story (A-02). Shows "OPEN-13, no Azure story". |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Decides in `EN-AZ-03`. Costs a single-instance case and a multi-instance case, because session state sits in one server's memory today (CS-16). |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Delivers only the infrastructure pipeline (`EN-AZ-07`). Delivers no build or test pipeline. |

**Other OPEN items used.** OPEN-07 (Antwerp path, Ahmed Benali with Pieter Janssens), OPEN-08 (measurement bases, Lena Varga), OPEN-12 (NWFS01, Ahmed Benali).

**Dependencies inside the track.** None. This is the first Azure release.

### 8.2 `azure-r2` — Production cutover (`track-azure`)

| Field | Value |
|---|---|
| Git tag | `product/azure-r2` (approved 2026-10-30; created on the approval commit) |
| Target | Rehearsal complete by end of April 2027. Cutover in a Sunday window in May 2027. At least one spare Sunday stays free before 30 June 2027 (A-07, C-01). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r2 |

**Goal.** Order Desk and its database run in Azure production. Staff keep working. The nightly exchange continues. Backups and recovery are tested. This is the Must outcome of the Azure track (source: BR-13, C-01, C-03, NFR-06).

**Scope.** Epic `EP-AZ-02` Production cutover (`track-azure`, `azure-r2`):

| Feature | Enablers and stories |
|---|---|
| `FT-AZ-05` Production environment and Antwerp connection | `EN-AZ-14` hybrid connectivity to Antwerp; follow-on stories for secrets (NFR-05), monitoring (NFR-01) and EU residency (NFR-03) on `prd` |
| `FT-AZ-06` Backup, disaster recovery and tested restore | `EN-AZ-06` |
| `FT-AZ-07` Data move: database and invoice files | `EN-AZ-08` database migration rehearsal; `EN-AZ-10` invoice store migration |
| `FT-AZ-08` Nightly exchange and mail relay in Azure | `EN-AZ-09` StockPilot exchange redesign; `EN-AZ-11` SMTP relay replacement |
| `FT-AZ-09` Sunday-window cutover and rollback | `EN-AZ-13` cutover runbook and rollback; cutover feature stories |

**Requirements covered.** BR-13, NFR-01, NFR-03, NFR-05, NFR-06, C-01, C-03.

**Constraints and standards that apply.** C-01 (date), C-02, C-03 (no StockPilot change), C-04 (cost grows with `prd`; the closing check is in `azure-r3`), C-06; NFR-01 (99.5 % in business hours, measured by a probe on `prd`), NFR-03, NFR-05, NFR-06 (RPO 1 hour, RTO 4 hours); ES-20 to ES-27. Planned downtime stays in the Sunday window, 06:00 to 12:00 CET (CS-21).

**Success measures moved.** Enables SM-07. The old servers are still running until `azure-r3` retires them (source: SM-07).

**Left out.** Decommissioning, the closing cost check and the disaster-recovery test report (`azure-r3`). Portal features and Order Desk code modernisation (BA-02; OPEN-03). The "Shipped" e-mail (BR-09), which belongs to BA-02. Any change to StockPilot (C-03). Any change to the finance system.

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | Keeps the nightly 02:00 cadence (CS-10, C-03). Builds no faster refresh. |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Plans the cutover for Order Desk as it exists on the day. Records in the rehearsal report each point that breaks on the new platform, and does not change application code (A-03). |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports cost for the whole platform against the ceiling. Applies no split. |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Delivers `prd` and `tst` only. Plans no pilot environment. |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Moves the existing PDFs to a store Order Desk can read. Leaves the write target of the finance system as Finance defines it. Changes nothing in the finance system. |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Delivers a replacement for the relay for the e-mail that CS-12 describes today. Covers no new e-mail (BR-09). |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the decision record from `azure-r1`. Assumes the setup that record names. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Keeps the exchange files, cadence and paths identical. Assumes no schema change. Any change reported later goes through a migration-impact check. |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Backs up audit data on the same schedule as other order data. Sizes retention at today's volume. Defines no retrieval target. |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Keeps CET meaning for batch times and states the time zone in each story (A-10). Proves it in the rehearsal. |

**Other OPEN items used.** OPEN-07 (Antwerp path, Ahmed Benali with Pieter Janssens), OPEN-08 (measurement bases, Lena Varga), OPEN-12 (NWFS01, Ahmed Benali).

**Dependencies inside the track.** Uses the foundation, network, secrets, monitoring, hosting decision, cost model and exchange proof from `azure-r1`.

### 8.3 `azure-r3` — Stabilise and decommission (`track-azure`)

| Field | Value |
|---|---|
| Git tag | `product/azure-r3` (approved 2026-10-30; created on the approval commit) |
| Target | By 30 June 2027 (A-07, C-01) |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r3 |

**Goal.** Retire the old servers so that servers past end of support go from 2 to 0. Confirm that run cost is within the ceiling. Hand over a disaster-recovery test report and runbooks (source: SM-07, C-04, NFR-06).

**Scope.** Epic `EP-AZ-03` Stabilise and decommission (`track-azure`, `azure-r3`):

| Feature | Content |
|---|---|
| `FT-AZ-10` Retire the old servers | Decommission `NWWEB01` and `NWSQL01`. Decommission `NWFS01` only if OPEN-12 says it counts. |
| `FT-AZ-11` Closing cost check, recovery test report and runbooks | Cost check against C-04. Disaster-recovery test report. Runbooks. |

**Requirements covered.** SM-07, C-04, NFR-06 (tested). **ASSUMPTION:** Runbooks are stored under `docs/migration/` (source: ES-09).

**Constraints and standards that apply.** C-01 (date), C-02, C-04 (EUR 1,500 per month), NFR-06; ES-20 to ES-27.

**Success measures moved.** **SM-07: production servers past end of support, 2 now, 0 by 30 June 2027.** Counting `NWFS01` is OPEN-12 (source: SM-07, CS-06, CS-07, CS-08).

**Left out.** New functions. Portal features (BA-02). Anything that changes StockPilot (C-03).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports the whole-platform cost against the ceiling. Applies no split. |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Retires `NWWEB01` and `NWSQL01`. Reports SM-07 with and without `NWFS01`. |

**Dependencies inside the track.** Uses the production environment, data move and cutover from `azure-r2`.

### 8.4 `dotnet-r1` — Modernised Order Desk (`track-dotnet`)

| Field | Value |
|---|---|
| Git tag | `product/dotnet-r1` (approved 2026-10-30; created on the approval commit) |
| Target | End of February 2027 (A-07) |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r1 |

**Goal.** Order Desk is on a current platform and behaves as before. Tests run everywhere and pricing is unchanged. Nothing in it ties it to one server. Staff see the order channel (source: CS-01, CS-02, CS-18, CS-20, BR-10, ES-14, ES-18).

**Scope.** Epic `EP-DN-01` Modernised Order Desk (`track-dotnet`, `dotnet-r1`):

| Feature | Enablers |
|---|---|
| `FT-DN-01` Current platform and safety net | `EN-DN-01` SDK-style projects on `net10.0`; `EN-DN-02` tests pass on Windows, macOS and Linux; `EN-DN-09` build and test pipeline |
| `FT-DN-02` Configuration, logging and no secrets | `EN-DN-03` configuration; `EN-DN-04` logging; `EN-DN-05` no secrets or Integrated Security (application side) |
| `FT-DN-03` Draft order and invoice storage free of one server | `EN-DN-06` draft order session; `EN-DN-07` invoice storage abstraction |
| `FT-DN-04` Staff see the order channel | Feature stories (BR-10 staff view) |

**Requirements covered.** NFR-05 (application), BR-10 (staff view), ES-14 to ES-19.

**Constraints and standards that apply.** C-05 (Order Desk stays the single source of truth), C-06; NFR-05; ES-13 to ES-19. Pricing tests and results do not change (CS-20, ES-18). **ASSUMPTION:** The 28 existing tests are the baseline and none may lose an assertion (A-22).

**Success measures moved.** None directly. It protects pricing and makes the later measures possible (source: CS-20, R-17).

**Left out.** Customer sign-in, customer data separation, staff Entra sign-in, the language scaffold and the audit work (`dotnet-r2`). The portal "Portal" channel stamp (`dotnet-r2`). Invoice download, customer administrators and French and English (`dotnet-r3`). Shipped e-mail and shipment storage (`dotnet-r4`). Any deployment pipeline for Azure (OPEN-21).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Modernises the Order Desk code in place (A-03). Does not wait for hosting work. |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports any change that adds hosting cost. Applies no split. |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Makes the draft order and invoice reading independent of any one server, so any hosting target works. |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Delivers the build and test pipeline for the solution (`EN-DN-09`). Includes no deployment steps. |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Keeps today's behaviour (local time for order dates, UTC for audit) and documents it. Changes it only with a decision record (ES-19). |

**Dependencies inside the track.** None. This is the first .NET release.

### 8.5 `dotnet-r2` — Portal pilot: Must items (`track-dotnet`)

| Field | Value |
|---|---|
| Git tag | `product/dotnet-r2` (approved 2026-10-30; created on the approval commit) |
| Target | Pilot start in April 2027 (A-07). The pilot is with 20 customers (source: business-case §8). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r2 |

**Goal.** 20 pilot customers use the portal for all Must items. They sign in, see only their own orders, see status and their own prices, reorder by copying, and submit orders that reach Order Desk. Staff see which orders came from the portal (source: BR-01 to BR-06, BR-10, BR-12, business-case §8).

**Scope.** Four epics (`track-dotnet`, `dotnet-r2`):

| Epic | Features | Enablers |
|---|---|---|
| `EP-DN-02` Secure access and tenant isolation | `FT-DN-05`, `FT-DN-06`, `FT-DN-07`, `FT-DN-08` | `EN-DN-11` portal decision record; `EN-DN-10` tenant isolation; `EN-DN-08` staff Entra sign-in |
| `EP-DN-03` See my orders | `FT-DN-09`, `FT-DN-10`, `FT-DN-11` | (none) |
| `EP-DN-04` Reorder and hand-off | `FT-DN-12`, `FT-DN-13`, `FT-DN-14` | `EN-DN-13` audit completeness |
| `EP-DN-05` Portal quality | `FT-DN-15`, `FT-DN-16` | `EN-DN-12` localisation scaffold; `EN-DN-14` accessibility baseline |

`EN-DN-10` (customer data separation) comes before every portal story that shows data, and each such story cites it (A-22).

**Requirements covered.** BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-10 (portal stamp), BR-12, NFR-02, NFR-03 (application), NFR-04, NFR-07, NFR-08.

**Constraints and standards that apply.** C-03 (status freshness is bounded by the nightly exchange), C-04 (hosting cost), C-05, C-06; NFR-02, NFR-03, NFR-04, NFR-07, NFR-08; ES-13 to ES-19, ES-20, ES-25. BR-04 stories say "as of the 02:00 batch" (A-04). BR-12 stories include OPEN-16. Pricing rules do not change (CS-20).

**Success measures moved.** This release starts the clock for SM-01 (portal share of orders), SM-02 ("where is my order?" calls) and SM-03 (order lines needing correction). The targets are "6 months after portal launch". "Portal launch" is **OPEN:** OPEN-05. **ASSUMPTION:** A-46: a 35 % share is not expected to be reached with 20 of about 1,150 customers. It depends on the order volume of the pilot customers (OPEN-05) (source: SM-01, SM-02, SM-03, business-case §8, R-11, A-46).

**Left out.**

* Invoice download (BR-07), customer administrator (BR-08) and French and English text (BR-11): `dotnet-r3`. Only the language foundation (`FT-DN-15`) is in this release.
* Shipped e-mail (BR-09) and storing shipment date and carrier: `dotnet-r4`.
* Measuring SM-01 to SM-04: `dotnet-r4`.
* Dutch (unplanned, OPEN-14). Field-level audit (unplanned, OPEN-17). Order Desk API (unplanned, OPEN-24).
* Online payment, native mobile app, changes to StockPilot, replacing the finance system (business-case §6).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | Shows status "as of the 02:00 batch" (A-04). |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Builds on the modernised Order Desk from its own track (A-03). |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports the hosting cost of the portal. Applies no split. |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Builds so that it can run in any environment that meets ES-20 and ES-25. Does not assume a pilot environment. |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Compares the options in the decision record (`EN-DN-11`) and checks price and limits (OPEN-25). Starts the customer sign-in feature once the choice is recorded. Other features in this release do not wait. |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the modernised draft order handling from `dotnet-r1`, which works on one or several instances. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Plans no schema change. Any change goes through a migration-impact check and a decision record (ES-19). |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Deletes no audit rows. Defines no sizing or retrieval target. |

**Other OPEN items used.** OPEN-02 (status source, Lena Varga with the Order Desk team), OPEN-08 (NFR measurement, Lena Varga), OPEN-09 (24 months of orders, Julien Moreau and Ahmed Benali), OPEN-10 (data protection and mobile, Ahmed Benali and Sofie Peeters), OPEN-14, OPEN-16, OPEN-17, OPEN-25, OPEN-26, and **OPEN-27** (the pilot language, Lena Varga with Sofie Peeters). Experiment `MVE-BA02` tests whether status "as of the 02:00 batch" is enough (see `experiments.md`).

**Dependencies inside the track.** Uses the modernised Order Desk, tests, configuration and draft order handling from `dotnet-r1`.

### 8.6 `dotnet-r3` — Should items (`track-dotnet`)

| Field | Value |
|---|---|
| Git tag | `product/dotnet-r3` (approved 2026-10-30; created on the approval commit) |
| Target | Not dated (A-07) |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r3 |

**Goal.** Customers can download invoices, customer administrators can manage their own users, and the portal speaks French and English (source: BR-07, BR-08, BR-11, P-05).

**Scope.** Epic `EP-DN-06` Self-service extras (`track-dotnet`, `dotnet-r3`): `FT-DN-17` Invoice download, `FT-DN-18` Customer administrator, `FT-DN-19` French and English. No enablers in this release.

**Requirements covered.** BR-07, BR-08, BR-11.

**Constraints and standards that apply.** C-04 (storage and hosting cost), C-05; NFR-03, NFR-04 (administrator invitations use the customer sign-in), NFR-07 (new pages stay WCAG 2.2 AA); ES-13 to ES-19.

**Success measures moved.** SM-04 (invoice copy requests handled by staff, 120 per week now, 40 or fewer, 6 months after portal launch). Measured in `dotnet-r4` (source: SM-04, P-05, OPEN-05).

**Left out.** Shipped e-mail (`dotnet-r4`). Dutch (unplanned, OPEN-14). Any change to how the finance system writes invoices (out of scope).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Reads invoices through a storage setting, not a fixed path. Assumes nothing about where finance writes. |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the hosting-independent invoice and draft handling from `dotnet-r1`. |

**Other OPEN items used.** OPEN-09 (order-to-invoice link and invoice year rule, Julien Moreau and Ahmed Benali), OPEN-14 (Dutch, Sofie Peeters with Lena Varga), OPEN-15 (customer administrators for all or only large customers, Lena Varga).

**Dependencies inside the track.** Uses customer data separation, sign-in and the language foundation from `dotnet-r2`, and the invoice storage setting from `dotnet-r1`.

### 8.7 `dotnet-r4` — Could items and measures (`track-dotnet`)

| Field | Value |
|---|---|
| Git tag | `product/dotnet-r4` (approved 2026-10-30; created on the approval commit) |
| Target | Not dated (A-07) |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r4 |

**Goal.** Customers receive an e-mail when an order is shipped. The success measures SM-01 to SM-04 are measured (source: BR-09, SM-01 to SM-04).

**Scope.** Epic `EP-DN-07` Notifications and measures (`track-dotnet`, `dotnet-r4`): `FT-DN-20` Keep shipment date and carrier (`EN-DN-15`), `FT-DN-21` Shipped e-mail, `FT-DN-22` Measure the success measures.

**Requirements covered.** BR-09, SM-01 to SM-04.

**Constraints and standards that apply.** C-03 (StockPilot sends the shipment data and does not change), C-04 (mail service cost), C-05; NFR-03 (mail service keeps data in the EU); ES-19 (a schema change needs a decision record).

**Success measures moved.** SM-01 (35 % of orders through the portal), SM-02 (410 to 250 or fewer calls per week), SM-03 (4.1 % to 2.5 % or fewer corrections), SM-04 (120 to 40 or fewer invoice requests per week), each 6 months after portal launch. **OPEN:** "Portal launch" is not defined (OPEN-05).

**Left out.** Online payment, native mobile app, any change to StockPilot (business-case §6). Dutch (unplanned, OPEN-14).

**Cross-track OPEN items (ES-31).**

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer (A-28) |
|---|---|---|---|
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Stores the shipment data and prepares the message content. Records BR-09 as partly covered until a mail path is named. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Assumes the exchange files stay as they are. Runs a migration-impact check before storing the new fields. |

**Other OPEN items used.** OPEN-05 (portal launch, Marc Dubois and Lena Varga).

**Dependencies inside the track.** Uses the portal order and status features from `dotnet-r2`.

## 9. Success measures by release

| Measure | Baseline | Target | Moved or measured by | Source |
|---|---|---|---|---|
| SM-01 Share of orders through the portal | 0 % | 35 %, 6 months after portal launch | Started in `dotnet-r2`. Measured in `dotnet-r4`. **OPEN:** OPEN-05. | (source: SM-01, business-case §8) |
| SM-02 "Where is my order?" calls per week | 410 | 250 or fewer, 6 months after portal launch | Started in `dotnet-r2`. Measured in `dotnet-r4`. | (source: SM-02, P-03) |
| SM-03 Order lines needing correction | 4.1 % | 2.5 % or fewer, 6 months after portal launch | Started in `dotnet-r2`. Measured in `dotnet-r4`. | (source: SM-03, P-02) |
| SM-04 Invoice copy requests handled by staff per week | 120 | 40 or fewer, 6 months after portal launch | Started in `dotnet-r3`. Measured in `dotnet-r4`. | (source: SM-04, P-05) |
| SM-07 Production servers past end of support | 2 | 0 by 30 June 2027 | Reached in `azure-r3`. Enabled by `azure-r2`. **OPEN:** OPEN-12. | (source: SM-07, C-01, C-02) |

## 10. Cross-track dependencies (all OPEN, none a prerequisite)

No release waits for another track (ES-31). The table shows where each cross-track **OPEN:** item is stated. Each release section above says what the release does without the answer (A-28).

| OPEN item | Topic | Stated in releases |
|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | `azure-r1`, `azure-r2`, `dotnet-r2` |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | `azure-r1`, `azure-r2`, `dotnet-r1`, `dotnet-r2` |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | `azure-r1`, `azure-r2`, `azure-r3`, `dotnet-r1`, `dotnet-r2` |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | `azure-r1`, `azure-r2`, `dotnet-r2`, `dotnet-r4` |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | `azure-r2`, `azure-r3`, `dotnet-r1`, `dotnet-r3` |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | `azure-r2`, `azure-r3` |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | `azure-r1`, `dotnet-r2` |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | `azure-r2`, `dotnet-r2`, `dotnet-r4` |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | `azure-r1`, `azure-r2`, `dotnet-r1`, `dotnet-r2`, `dotnet-r3` |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | `azure-r1`, `azure-r2`, `dotnet-r2`, `dotnet-r4` |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | `azure-r1`, `dotnet-r1` |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | `azure-r2`, `azure-r3`, `dotnet-r2` |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | `azure-r1`, `azure-r2`, `dotnet-r1` |

The table lists the releases that state the item in their section 7.2.

(source: ES-30, ES-31, business-case §4)

## 11. Risks

Ratings are an **ASSUMPTION:** judgement for discussion (A-25). The IDs are the BRD risk IDs. The wording is shortened. Risks that rely on code or database findings use A-22 and A-23.

| ID | Risk | Likelihood | Impact | Releases | Product-level response | Owner | Source |
|---|---|---|---|---|---|---|---|
| R-01 | The move is late and misses the lease end of 30 June 2027. | Medium | High | `azure-r2`, `azure-r3` | Keep a spare Sunday window. Dates are targets (A-07). | Marc Dubois | (source: C-01, BR-13, CS-21, A-07) |
| R-02 | The nightly StockPilot exchange cannot move in the same form. It depends on database-server features that Azure's managed database does not offer. StockPilot cannot change. | High | High | `azure-r1`, `azure-r2` | Prove the exchange early with identical files (`FT-AZ-04`). | Ahmed Benali | (source: CS-10, C-03, A-23) |
| R-03 | Order Desk code does not limit a signed-in user to their own company's data. | High | High | `dotnet-r2` | Customer data separation (`EN-DN-10`) comes first. | Ahmed Benali | (source: BR-01, CS-04, A-22) |
| R-04 | "Always up to date" (BR-04) cannot be met. Customers may keep phoning. | Medium | Medium | `dotnet-r2` | Test "as of the 02:00 batch" with pilot customers (`MVE-BA02`). | Lena Varga | (source: BR-04, CS-10, SM-02, A-04) |
| R-05 | The shared cost ceiling of EUR 1,500 per month is exceeded. | Medium | High | `azure-r1`, `azure-r3` | Estimate early (`FT-AZ-02`). Check at the end (`FT-AZ-11`). | Marc Dubois | (source: C-04, CS-08, A-09, A-14) |
| R-06 | Ownership of the Order Desk upgrade is unclear. | Medium | High | `azure-r2`, `dotnet-r1` | Confirm the split (A-03). Neither track waits. | Ahmed Benali | (source: CS-13 to CS-17, A-03, OPEN-03) |
| R-07 | The 48 GB database cannot be moved, checked and rolled back inside the six-hour Sunday window. | Medium | High | `azure-r2` | Measure transfer time and rehearse (`EN-AZ-08`). | Ahmed Benali | (source: CS-07, CS-21, BR-13) |
| R-08 | Recovery targets (RPO 1 hour, RTO 4 hours) are not met because recovery was never tested. | Medium | High | `azure-r2`, `azure-r3` | Tested restore with a report (`FT-AZ-06`, `FT-AZ-11`). | Ahmed Benali | (source: NFR-06, CS-23) |
| R-09 | The six-person IT team is stretched by two tracks and has limited container skills. | Medium | Medium | All | Prefer platforms the team can run (ES-13, ES-21). | Ahmed Benali | (source: C-06, ES-13, ES-21) |
| R-10 | Invoice delivery depends on the finance system, which is out of scope. The invoice folder year may follow the order year, not the invoice year. | Medium | Medium | `azure-r2`, `dotnet-r3` | Agree the hand-off with Finance. Confirm the year rule. | Julien Moreau | (source: CS-08, CS-11, BR-07, A-22, OPEN-06, OPEN-09) |
| R-11 | The pilot of 20 customers may not show the 35 % share in SM-01, if the pilot customers place too few orders (**ASSUMPTION:** A-46; their order volume is part of OPEN-05). The result would be judged a failure. | High | Medium | `dotnet-r2`, `dotnet-r4` | Define "portal launch" and read the pilot customers' order volume before measuring. | Lena Varga | (source: SM-01, business-case §8, OPEN-05, A-46) |
| R-12 | New hosting uses a different clock from Lyon (UTC against CET). Batch times, order dates and audit shift. | Medium | Medium | `azure-r2`, `dotnet-r1` | Decide one time rule. | Ahmed Benali | (source: CS-10, CS-21, A-10, OPEN-23) |
| R-13 | 7 years of audit history grow the database and complicate recovery. | Low | Medium | `azure-r2`, `dotnet-r2` | Size retention and recovery together. | Ahmed Benali | (source: NFR-08, NFR-06, OPEN-22) |
| R-14 | The e-mail path may not work from Azure, and no sending code was found in `src/`. | Medium | Medium | `azure-r2`, `dotnet-r4` | Find out who sends e-mail today and agree a path. | Ahmed Benali | (source: CS-12, BR-09, A-22, OPEN-18) |
| R-15 | Customer sign-in options cost more or have limits not yet checked. | Medium | Medium | `dotnet-r2` | Check price and limits before choosing. | Ahmed Benali | (source: NFR-04, OQ-01, A-21, OPEN-25) |
| R-16 | The portal has no French, English or Dutch text support today. All text is English. Pilot customers in `dotnet-r2` may see one language only. | High | Low | `dotnet-r2`, `dotnet-r3` | Lay a language foundation early (`FT-DN-15`). Decide the pilot language (OPEN-27). | Ahmed Benali | (source: BR-11, A-22, OPEN-27) |
| R-17 | Pricing changes by accident during the upgrade. | Low | High | `dotnet-r1`, `dotnet-r2` | Keep pricing tests and their assertions unchanged (CS-20, ES-18). | Ahmed Benali | (source: CS-20, BR-12, ES-18) |

## 12. Companion documents

| Document | Path | What it holds |
|---|---|---|
| Business requirements (BRD) | `docs/product/business-requirements.md` | Why: needs, sources, stakeholders, current-state facts. |
| Experiments | `docs/product/experiments.md` | Two Minimum Viable Experiments (MVEs): `MVE-BA01` StockPilot exchange (Azure) and `MVE-BA02` nightly-fresh status (.NET). Success thresholds are in A-06. |
| Backlog | `docs/product/backlog.md` | Epics, features, stories and enablers with Given / When / Then, tags, priority and sources. Reuses the IDs in section 5. |
| Traceability | `docs/product/traceability.md` | Maps every BR-01 to BR-13 and NFR-01 to NFR-08 to stories by track and release. Lists anything not covered. Lists BA-03 as out of scope (ES-06). |
| Releases | `docs/product/releases/azure-r1.md`, `azure-r2.md`, `azure-r3.md`, `dotnet-r1.md`, `dotnet-r2.md`, `dotnet-r3.md`, `dotnet-r4.md` | One file per release (ES-31). Section 8 is the summary of each. |
| Index and master registers | `docs/product/README.md` | Reading order. Master assumption and OPEN registers. |

These files are written in later steps of the plan. At the time of writing, no story exists yet. This document claims no story-level coverage (A-01).

## 13. Document boundary and status

* Every statement is a draft for review. Nothing is implemented, deployed, committed or tagged (ES-27, A-16).
* No secret, key, connection string, tenant ID or subscription ID appears in this document (NFR-05).
* The Git tags `product/azure-r<n>` and `product/dotnet-r<n>` are created only after the product owner approves each release (ES-31, A-08, A-29). All seven releases were approved on 2026-10-30.

## 14. Assumptions (ES-03)

Every assumption has a person who can confirm it. Wording is identical in every product document. The master register is in `docs/product/README.md`.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-01 | File names under `docs/product/` as pinned in `README.md` section 2 | Lena Varga |
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-05 | Confirmed, Delivered and Cancelled are manual staff actions today | Order Desk team via Lena Varga |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-09 | The cost model assumes SQL and private endpoints are the main spend | Ahmed Benali |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali |
| A-11 | NFR-01 covers the Order Desk and the portal; availability is measured by a probe | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-13 | The portal is a responsive web site for current browsers (mobile via browser) | Sofie Peeters, Ahmed Benali |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-15 | The BRD keeps the business-case identifiers `C-01`..`C-08` for constraints | Lena Varga |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-17 | Move items without a BR or NFR (SMTP relay CS-12, invoice share CS-08/CS-11, monitoring CS-22, DR CS-23, pipeline CS-19) are enabler stories tagged by track | Lena Varga |
| A-18 | BR-10 stories are small: show the channel, filter by it, and set the Portal channel on the server | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-20 | `ShippedAt` and `Carrier` must be stored for BR-09 | Ahmed Benali |
| A-21 | Entra External ID pricing and limits, and .NET 10 on Azure App Service, are not verified | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali |
| A-24 | The people named as owners of OPEN items (BRD section 5) are proposals taken from the stakeholder list; Lena Varga, as backlog owner, confirms them | Lena Varga |
| A-25 | Risk likelihood and impact ratings in BRD section 13 are judgements for discussion and not figures from the business case | Lena Varga |
| A-26 | The feature IDs `FT-AZ-01`..`FT-AZ-11` and `FT-DN-01`..`FT-DN-25` in PRD section 5 are the baseline for `backlog.md`. The backlog reuses them, may add new numbers, and never renumbers. The unplanned parent epic `EP-DN-08` is a proposed name | Lena Varga |
| A-27 | The personas in section 2 are working descriptions built from the roles in the business case (section 1, section 5) and CS-03. They are not based on customer interviews | Lena Varga |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 15. OPEN items (ES-04)

Wording is identical in every product document. Items marked "Azure and .NET" are cross-track. None is a blocker for this document.

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

Business-case open questions kept in scope: OQ-01 is OPEN-13, OQ-02 is OPEN-14 and OQ-03 is OPEN-15. OQ-04 and OQ-05 belong to BA-03 and are out of scope (section 3.2).
