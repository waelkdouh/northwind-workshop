# Northwind Traders — Business requirements: Platform and data-centre exit (BA-01) and Ordering and customer self-service (BA-02)

| Field | Value |
|---|---|
| Document | Business requirements document (BRD), deliverable D1 |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`) and **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`). **BA-03** is out of scope (section 3). |
| Business owner | Lena Varga, Head of Customer Operations (owns the product backlog) |
| Sponsor | Marc Dubois, Chief Operating Officer (COO) |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01 to ES-07, ES-30, ES-31). Code and database findings from the research file are used only to explain risk and are marked **ASSUMPTION:** (A-22). |
| Boundary | This document describes business needs. It contains no solution design and no implementation. Nothing is deployed, committed or tagged (ES-27). |

How to read this document:

* IDs such as `BR-05`, `NFR-02`, `C-01`, `SM-01`, `P-01` and `OQ-01` come from the business case. `CS-` IDs come from `current-state.md`. `ES-` IDs come from the engineering standards. `BA-` means business area.
* Priorities use MoSCoW: **Must**, **Should**, **Could** (Won't is not used here). A requirement is a business need that is testable. NFR means non-functional requirement.
* Every requirement cites its source in the form `(source: BR-05, CS-10)` (ES-02).
* **ASSUMPTION:** marks anything not stated in `knowledge-docs`. It is listed in section 16 with a person who can confirm it (ES-03).
* **OPEN:** marks an unanswered question. It is listed in section 17 with the person who can answer it (ES-04).

## 1. Purpose and background

Northwind Traders is a business-to-business (B2B) distributor of specialty food products. It is based in Lyon, with a second warehouse in Antwerp. It supplies about 1,150 active business customers in France, Belgium and Luxembourg and employs 240 people. 38 of them work in Customer Operations, called the "Order Desk" (source: business-case §1, CS-03, CS-05).

Order Desk is also the name of the internal web application that staff use to enter and manage orders. It was built in 2013 on ASP.NET MVC 5 and .NET Framework 4.8 and runs in the company's own data centre in Lyon (source: CS-01, CS-06, CS-07).

This document covers two business needs:

1. **Move Order Desk to Microsoft Azure** before the data-centre lease ends on 30 June 2027, without stopping staff work (BA-01) (source: C-01, BR-13).
2. **Give business customers a secure web self-service Customer Portal** for their orders, supported by an upgraded Order Desk (BA-02) (source: business-case §3, BR-01 to BR-12).

### 1.1 Problems this work addresses

| ID | Problem | In scope? | Source |
|---|---|---|---|
| P-01 | About 1,900 orders per week are entered by hand. 62 % arrive by phone or e-mail. | Yes (BA-02) | (source: P-01, CS-05) |
| P-02 | Re-keying causes errors. 4.1 % of order lines need a correction after entry. | Yes (BA-02) | (source: P-02, SM-03) |
| P-03 | Customers cannot see order status. The Order Desk gets about 410 "where is my order?" calls per week, about 35 % of inbound calls. | Yes (BA-02) | (source: P-03, SM-02) |
| P-04 | Reordering is slow. 70 % of orders repeat a previous order with small changes, but customers dictate or re-type the whole list. | Yes (BA-02) | (source: P-04, BR-05) |
| P-05 | Staff search a network file share and e-mail invoice copies by hand, about 120 requests per week. | Yes (BA-02) | (source: P-05, SM-04, CS-08, CS-11) |
| P-06 | About 85 delivery claims per week are handled in a spreadsheet and by e-mail. | **No. Belongs to BA-03.** | (source: P-06, business-case §4) |

The platform need (BA-01) is not a numbered problem in the business case. Its drivers are the lease end (C-01) and the fact that both servers are past end of support, which Northwind pays extra to keep secure (C-02) (source: C-01, C-02, SM-07).

## 2. Objectives and success measures

### 2.1 Objectives

| # | Objective | Area | Source |
|---|---|---|---|
| O-1 | Order Desk and its database run in Azure before 30 June 2027. The exchange with StockPilot keeps working. Availability, recovery and cost targets are met. | BA-01 | (source: C-01, C-03, NFR-01, NFR-06, C-04, business-case §4) |
| O-2 | Staff keep working during the move. Planned downtime stays in the Sunday maintenance window, 06:00 to 12:00 CET. | BA-01 | (source: BR-13, CS-21) |
| O-3 | Business customers can sign in, see their own orders and their status, reorder, and get invoices without calling staff. | BA-02 | (source: BR-01 to BR-07, P-03, P-04, P-05) |
| O-4 | Order Desk becomes a base that the portal can safely use, and Order Desk remains the single source of truth for orders. | BA-02 | (source: C-05, business-case §4) |
| O-5 | Production servers past end of support go from 2 to 0 by 30 June 2027. | BA-01 | (source: SM-07, C-02) |

### 2.2 Success measures

Targets that depend on "portal launch" are open (OPEN-05).

| ID | Measure | Baseline | Target | Area | Source |
|---|---|---|---|---|---|
| SM-01 | Share of orders placed through the portal | 0 % | 35 %, 6 months after portal launch | BA-02 | (source: SM-01, P-01) |
| SM-02 | "Where is my order?" calls per week | 410 | 250 or fewer, 6 months after portal launch | BA-02 | (source: SM-02, P-03) |
| SM-03 | Order lines needing correction after entry | 4.1 % | 2.5 % or fewer, 6 months after portal launch | BA-02 | (source: SM-03, P-02) |
| SM-04 | Invoice copy requests handled by staff per week | 120 | 40 or fewer, 6 months after portal launch | BA-02 | (source: SM-04, P-05) |
| SM-07 | Production servers past end of support | 2 | 0 by 30 June 2027 | BA-01 | (source: SM-07, C-01, C-02, CS-06, CS-07) |

Notes:

* **OPEN:** "Portal launch" is not defined (OPEN-05). The target of 35 % (SM-01) applies 6 months after portal launch, and the pilot has 20 customers out of about 1,150 (business-case §8). **ASSUMPTION:** A-46 says a 35 % share is not expected to be reached with the pilot. It depends on the order volume of the pilot customers, which no source gives (source: SM-01, business-case §8, A-46).
* The two servers in SM-07 are most likely `NWWEB01` and `NWSQL01`, which both run Windows Server 2012 R2 (source: CS-06, CS-07). **OPEN:** whether the file server `NWFS01` counts is OPEN-12.
* SM-05 and SM-06 (claims) are out of scope (section 3).

## 3. Scope

### 3.1 In scope

| Area | Name | Delivery track | Tag | Release names (A-08) |
|---|---|---|---|---|
| BA-01 | Platform and data-centre exit | Azure | `track-azure` | `azure-r1`, `azure-r2`, `azure-r3` |
| BA-02 | Ordering and customer self-service | .NET | `track-dotnet` | `dotnet-r1`, `dotnet-r2`, `dotnet-r3`, `dotnet-r4` |

Each area is delivered by its own team on its own track and in its own numbered releases. Every epic, feature and story carries exactly one track tag (ES-30). A story that would need both tracks is split into one story per track (ES-30). A track never waits for another track. A dependency between tracks is written down as an **OPEN:** item (ES-31, section 12) (source: business-case §4, ES-30, ES-31).

In scope: BR-01 to BR-13, NFR-01 to NFR-08, C-01 to C-06, SM-01 to SM-04, SM-07, OQ-01 to OQ-03 and the current-state facts in section 11.

### 3.2 Out of scope

**Business area BA-03 Delivery claims and credit notes (Power Platform track, `track-power-platform`)** is out of scope. Its identifiers are listed here only so that nothing is lost (ES-06):

| Out-of-scope item | Identifiers |
|---|---|
| Business requirements | BR-14, BR-15, BR-16, BR-17, BR-18, BR-19 |
| Non-functional requirement | NFR-09 (claim decisions kept 7 years) |
| Constraints | C-07, C-08 |
| Success measures | SM-05, SM-06 |
| Problem | P-06 |
| Open questions | OQ-04, OQ-05 (informational only; no release in this scope waits for them) |
| Current-state facts | CS-24 to CS-28 |
| Standards for Power Platform | ES-32 to ES-37 |
| Timeline item | Delivery claims pilot in Q1 2027 (business-case §8) |

NFR-03 and NFR-04 are shared with BA-03. They are in scope here only for BA-01 and BA-02 (source: business-case §4).

**Exclusions in the business case, section 6** (out of scope for the first release):

* Online payment. Customers continue to pay by bank transfer on invoice.
* A native mobile app. A responsive web portal is enough for now.
* Changes to StockPilot, the warehouse management system in Antwerp.
* Replacing the finance system that produces invoices and credit notes.
* Customers recording claims themselves in the portal. (Claims belong to BA-03.)

**OPEN:** OPEN-24 (informational). BA-03 will need an Order Desk programming interface (API). This is noted here only so that it is not lost. No release in this scope depends on it, and no story is written for it.

## 4. Business areas and delivery tracks

| Area | Delivery track | What it covers | Identifiers | Source |
|---|---|---|---|---|
| BA-01 | Azure (`track-azure`) | Run Order Desk and its database in Azure before the lease ends. Keep the StockPilot exchange working. Meet the availability, recovery and cost targets. | BR-13, NFR-01, NFR-03, NFR-05, NFR-06, C-01 to C-04, C-06, SM-07 | (source: business-case §4) |
| BA-02 | .NET (`track-dotnet`) | The Customer Portal and the Order Desk application that serves it: sign-in, orders, status, reorder, invoices and prices. Also the upgrade of Order Desk that the portal depends on. | BR-01 to BR-12, NFR-02, NFR-04, NFR-05, NFR-07, NFR-08, C-05, SM-01 to SM-04 | (source: business-case §4) |

**ASSUMPTION:** The .NET track owns the modernisation of the Order Desk code. The Azure track owns hosting, data and the StockPilot exchange (A-03). **OPEN:** The business case wording for the two areas overlaps on "the upgrade of Order Desk". See OPEN-03.

## 5. Stakeholders

| Stakeholder | Interest | Can answer | Source |
|---|---|---|---|
| Lena Varga, Head of Customer Operations | Fewer calls, fewer errors for her team. Owns the product backlog and this document. | OPEN-01, 02, 03 (with Ahmed Benali), 05 (with Marc Dubois), 08, 11, 15, 16, 17, 20 (freshness), 22 (with Ahmed Benali) | (source: business-case §5) |
| Marc Dubois, COO (sponsor) | Exit the data centre on time and within budget. | OPEN-04, OPEN-05 (with Lena Varga) | (source: business-case §5, C-01, C-04) |
| Ahmed Benali, IT Manager | Platforms his 6-person team can operate. Cares about security, licences and cost. | OPEN-03, 07, 09 (with Julien Moreau), 10, 12, 13, 18, 19, 20 (schema), 21, 22, 23, 24, 25 | (source: business-case §5, C-06) |
| Sofie Peeters, Key Account Manager (Belgium) | Belgian customers asking for Dutch and for mobile access. | OPEN-10 (mobile), OPEN-14 (with Lena Varga) | (source: business-case §5, BR-11) |
| Customer users (grocers, chefs, purchasing staff) | Fast reorder, status visibility, invoice access. | Not asked directly in this document | (source: business-case §5) |
| Julien Moreau, Finance | Invoices and credit notes stay in the finance system. Other applications only show them. | OPEN-06, OPEN-09 (with Ahmed Benali) | (source: business-case §5, CS-11) |
| Pieter Janssens, Warehouse Supervisor (Antwerp) | Wants to know which picking errors cause claims (BA-03). Uses StockPilot, which Order Desk exchanges data with. | OPEN-07 (with Ahmed Benali) | (source: business-case §5, CS-10) |
| Order Desk team (38 staff) and other internal users (about 45) | Keep working during the move. See the order channel. | OPEN-02 (through Lena Varga) | (source: CS-03, BR-10, BR-13) |

**ASSUMPTION:** Who can answer which OPEN item follows the plan owners. They are proposals for Lena Varga to confirm (A-24).

## 6. Business requirements in scope (BR-01 to BR-13)

Priorities are from the business case. All BR items have a priority there (source: business-case §3.1).

### 6.1 BA-02 Ordering and customer self-service (`track-dotnet`)

| ID | Requirement (business case wording) | Priority | Source | Notes |
|---|---|---|---|---|
| BR-01 | A customer user can sign in and see only the orders of their own company. | Must | (source: BR-01, CS-04, NFR-04, C-05) | Today only staff sign in (CS-04). The method for customers is OPEN-13. |
| BR-02 | A customer user can see the list of their company's orders from the last 24 months with order date, status and total. | Must | (source: BR-02, CS-05, CS-07, P-03) | **OPEN:** Do 24 months of orders exist in the database (OPEN-09)? |
| BR-03 | A customer user can open an order and see its lines, quantities, prices, delivery address and current status. | Must | (source: BR-03, CS-05, P-03) | Prices follow BR-12. |
| BR-04 | A customer user sees the status of an order as one of: Received, Confirmed, Picking, Shipped, Delivered, Cancelled. The status is always up to date. | Must | (source: BR-04, P-03, CS-10, C-03) | **Conflict.** Picking and Shipped are updated once per night (CS-10), and StockPilot cannot change (C-03). "Always up to date" has no measurable freshness. **ASSUMPTION:** BR-04 is met "as of the 02:00 batch" (A-04). **OPEN:** OPEN-01 (freshness), OPEN-02 (source of Confirmed, Delivered, Cancelled), OPEN-20. |
| BR-05 | A customer user can create a new order by copying a previous order and changing quantities or removing lines before submitting it. | Must | (source: BR-05, P-04, CS-16) | |
| BR-06 | A submitted portal order appears in Order Desk without being re-keyed, with the status Received. | Must | (source: BR-06, P-01, P-02, C-05) | Supports SM-03. |
| BR-07 | A customer user can download the PDF invoice of a delivered order. | Should | (source: BR-07, P-05, CS-08, CS-11, CS-14) | **OPEN:** How invoice files reach Azure (OPEN-06), and the link from an order to an invoice number (OPEN-09). |
| BR-08 | A customer administrator can invite and remove users of their own company. | Should | (source: BR-08, OQ-03) | **OPEN:** OPEN-15 (all customers or only large ones). |
| BR-09 | A customer user receives an e-mail when an order changes to Shipped. | Could | (source: BR-09, CS-10, CS-12) | **ASSUMPTION:** Shipment date and carrier must be stored to support this (A-20). **OPEN:** OPEN-18 (mail path). |
| BR-10 | Order Desk staff can see whether an order was placed through the portal or entered by staff. | Must | (source: BR-10, CS-03) | **ASSUMPTION:** This is a small item: show the channel, filter by it, set the Portal channel on the server (A-18). |
| BR-11 | The portal is available in French and English. Dutch is requested by Belgian customers. | Should | (source: BR-11, business-case §1, §5, OQ-02) | **OPEN:** Dutch in the first release (OPEN-14). |
| BR-12 | The portal respects each customer's negotiated prices; the customer sees their price, not the list price. | Must | (source: BR-12, CS-20, C-05) | Pricing rules must not change (CS-20). **OPEN:** Show volume and Gold discounts, or only the net price (OPEN-16). |

### 6.2 BA-01 Platform and data-centre exit (`track-azure`)

| ID | Requirement (business case wording) | Priority | Source | Notes |
|---|---|---|---|---|
| BR-13 | Order Desk staff keep working through the move to Azure. Planned downtime stays inside the Sunday maintenance window (Sunday 06:00 to 12:00 CET). | Must | (source: BR-13, CS-21, CS-07, CS-10, C-01) | The database is 48 GB and grows about 1 GB per month (CS-07). The nightly StockPilot exchange must keep running (C-03). |

## 7. Non-functional requirements in scope (NFR-01 to NFR-08)

The business case gives **no priority** for NFR items. **ASSUMPTION:** The priority shown is "Must", assigned because each item gates a release that carries a Must outcome (A-12). Lena Varga can change it. NFR-09 is out of scope (section 3.2).

| ID | Requirement (business case wording) | Track | Assumed priority (A-12) | Gates release | Source | Notes |
|---|---|---|---|---|---|---|
| NFR-01 | Availability of 99.5 % during business hours, Monday to Saturday 06:00 to 20:00 CET. | Azure | Must | `azure-r2` | (source: NFR-01, CS-06, CS-22) | **ASSUMPTION:** It covers Order Desk and the portal and is measured by a probe (A-11). Today there is one server and only ping checks (CS-06, CS-22). **OPEN:** OPEN-08. |
| NFR-02 | Order list and order detail pages respond in under 2 seconds for 95 % of requests. | .NET | Must | `dotnet-r2` | (source: NFR-02, CS-03, BR-02, BR-03) | No load profile is given. Staff peak is about 60 concurrent users (CS-03). Portal users are unknown. **OPEN:** OPEN-08. |
| NFR-03 | Customer data and order data stay in the European Union (EU). | Both | Must | `azure-r1`, `dotnet-r2` | (source: NFR-03, CS-09, C-01) | Cross-cutting (section 8). |
| NFR-04 | Customer users authenticate with an identity managed outside the application. Northwind staff use their Microsoft Entra ID accounts. | Both | Must | `dotnet-r2` | (source: NFR-04, CS-04, OQ-01) | Staff sign in today with Windows Integrated Authentication (CS-04). **OPEN:** OPEN-13, OPEN-03. |
| NFR-05 | No secret (password, connection string with password, key) is stored in source code or in configuration files in the repository. | Both | Must | `azure-r1`, `dotnet-r1` | (source: NFR-05, CS-13, CS-17, ES-17) | Cross-cutting (section 8). Today the connection uses Windows sign-in, not a password (CS-13). |
| NFR-06 | Recovery point objective (RPO) of 1 hour and recovery time objective (RTO) of 4 hours for order data. | Azure | Must | `azure-r2` | (source: NFR-06, CS-07, CS-23) | RPO is how much data may be lost. RTO is how long recovery may take. Log backups run every 15 minutes (CS-07). Disaster recovery was never tested (CS-23). **OPEN:** OPEN-22. |
| NFR-07 | The portal meets WCAG 2.2 level AA (Web Content Accessibility Guidelines). | .NET | Must | `dotnet-r2` | (source: NFR-07, BR-03) | **ASSUMPTION:** The portal is a responsive web site for current browsers (A-13). |
| NFR-08 | Every change to an order (who, what, when, channel) is recorded for 7 years for audit purposes. | .NET | Must | `dotnet-r2` | (source: NFR-08, BR-10, CS-05) | **OPEN:** OPEN-17 (field-level detail), OPEN-22 (retention sizing and recovery), OPEN-08. |

## 8. Cross-cutting requirements: how they are split by track

NFR-03, NFR-04 and NFR-05 apply wherever they are relevant, whichever area a story belongs to (source: business-case §4). Because one story can carry only one track tag (ES-30), each requirement is expected to have **one story per track**. The traceability table in `traceability.md` will show both.

| Requirement | Azure track (platform side) | .NET track (application side) | Source |
|---|---|---|---|
| NFR-05 No secrets | No secret in infrastructure code or pipelines. Applications reach data services without passwords. | No password or secret in application configuration. | (source: NFR-05, ES-17, ES-25, CS-13) |
| NFR-03 Data in the EU | Regions and backups and logs stay in the EU. | The portal's sign-in, mail and telemetry services keep customer data in the EU. | (source: NFR-03, ES-20, BA-02 scope) |
| NFR-04 Sign-in | **OPEN:** An Azure story exists only if OPEN-03 or OPEN-13 assigns platform sign-in plumbing to the Azure track. Until then the traceability table shows "OPEN-13, no Azure story" (A-02). | Customer sign-in and staff Microsoft Entra ID sign-in. | (source: NFR-04, OQ-01, A-02) |
| NFR-06 and NFR-08 | Recovery of order data (RPO and RTO). | Audit content of order changes. Linked by OPEN-22 for 7-year retention. | (source: NFR-06, NFR-08) |
| C-04 Cost ceiling | Shared. | Shared. | (source: C-04, A-14, OPEN-04) |

**ASSUMPTION:** NFR-03, NFR-04 and NFR-05 are cross-cutting and get one story per track (A-02). NFR-03 is listed in BA-01 but not in BA-02 in the business case. It is applied to BA-02 because the portal stores customer data (A-02).

## 9. Constraints in scope (C-01 to C-06)

The business case uses `C-` IDs for constraints. They are kept as they are (A-15). C-07 and C-08 are out of scope.

| ID | Constraint | Track | Source |
|---|---|---|---|
| C-01 | The data-centre lease ends on **30 June 2027**. Order Desk must run in Microsoft Azure before that date. | Azure | (source: C-01, CS-06, CS-07, CS-09) |
| C-02 | The web server runs Windows Server 2012 R2 and the database runs SQL Server 2014. Both are past end of support. Northwind pays for Extended Security Updates and wants to stop. | Azure | (source: C-02, CS-06, CS-07, SM-07) |
| C-03 | StockPilot stays on premises in Antwerp until at least 2028. It exchanges order and shipment data with Order Desk. It does not change. | Azure | (source: C-03, CS-10, business-case §6) |
| C-04 | Target run cost of the Azure platform (Order Desk and portal, production and one test environment) is at most **EUR 1,500 per month**. | Shared (A-14) | (source: C-04, OPEN-04) |
| C-05 | The portal reuses Order Desk as the single source of truth for orders. No second order database. | .NET | (source: C-05, CS-01, BR-06) |
| C-06 | The IT team (6 people) knows .NET and SQL Server well. It has limited experience with containers and Kubernetes. | Azure | (source: C-06, business-case §5, ES-21) |

**ASSUMPTION:** The ceiling in C-04 is shared by both tracks (A-14). **OPEN:** Who is accountable for it (OPEN-04).

## 10. Standards that shape the work (not requirements)

These standards limit how the work is documented and delivered. They are listed so that readers know the boundaries. They are not business requirements.

| Standard | What it means here | Source |
|---|---|---|
| ES-01, ES-02, ES-03, ES-04 | Plain language. Every requirement cites its source. Assumptions and open questions are listed with owners. | (source: ES-01 to ES-04) |
| ES-06 | The traceability table maps every in-scope BR and NFR to stories and lists other areas as out of scope. | (source: ES-06) |
| ES-07 | Product documents are under `docs/product/`. Releases are under `docs/product/releases/`. | (source: ES-07, A-01) |
| ES-30, ES-31 | One track tag per item. Release names `<track>-r<n>`. No release waits for another track. Cross-track dependencies are **OPEN:** items. | (source: ES-30, ES-31, A-08) |
| ES-27 | Nothing is deployed in this workshop. | (source: ES-27) |

## 11. Current-state facts relied on

These facts are taken from `current-state.md` and relied on for the in-scope requirements. CS-24 to CS-28 (delivery claims) are out of scope.

| ID | Fact (short) | Used by |
|---|---|---|
| CS-01 | Order Desk is an ASP.NET MVC 5 application on .NET Framework 4.8, built in 2013, maintained by internal IT. | BA-01, BA-02, C-05 |
| CS-02 | Three projects (Core, Web, Tests) in the old project format. | BA-02 |
| CS-03 | 38 Order Desk staff and about 45 other internal users. About 60 concurrent users at peak (Monday 08:00 to 11:00). | NFR-02, BR-10, BR-13 |
| CS-04 | Staff sign in with Windows Integrated Authentication against the on-premises Active Directory domain. No customer-facing access today. | BR-01, NFR-04 |
| CS-05 | About 1,900 orders and 14,000 order lines per week. 1,150 active customers and 2,300 active products. | P-01, BR-02, NFR-08 |
| CS-06 | Web server `NWWEB01`: Windows Server 2012 R2, one server, no load balancer. | C-02, NFR-01, SM-07 |
| CS-07 | Database server `NWSQL01`: SQL Server 2014. Database 48 GB, growing about 1 GB per month. Log backups every 15 minutes, kept 35 days. | BR-13, NFR-06, C-02, SM-07 |
| CS-08 | File share `NWFS01` holds about 120 GB of invoice PDFs, growing about 2 GB per month. | BR-07, SM-04 |
| CS-09 | Lyon data centre with a site-to-site VPN to the Antwerp warehouse. No Azure presence yet. Microsoft 365 and Microsoft Entra ID are in place. | C-01, NFR-03, NFR-04 |
| CS-10 | A nightly batch at 02:00 exchanges orders and shipments with StockPilot through CSV files on an SFTP server. Picking and Shipped are updated once per night. | BR-04, BR-09, BR-13, C-03 |
| CS-11 | The finance system writes one PDF per invoice to the invoice share. Order Desk reads them. | BR-07 |
| CS-12 | Order confirmations are sent through the internal SMTP relay without authentication. | BR-09 |
| CS-13 | The database connection uses Windows sign-in and a fixed server name. | NFR-05, BR-13 |
| CS-14 | Invoice PDFs are read from a network (UNC) path in configuration. | BR-07 |
| CS-15 | Errors are written to the Windows Event Log. | BA-01, BA-02 |
| CS-16 | Session state is held in the web server's memory. The order being entered is kept in session. | BR-05, BR-13 |
| CS-17 | Configuration is read through `ConfigurationManager` throughout the code. | NFR-05 |
| CS-18 | Unit tests run only inside Visual Studio on the build machine. | BA-02 |
| CS-19 | No automated build or deployment. | BA-01, BA-02 |
| CS-20 | Pricing rules live in `PricingService.cs`, are covered by unit tests, and must not change during the move. | BR-12 |
| CS-21 | Planned maintenance window: Sunday 06:00 to 12:00 CET. | BR-13 |
| CS-22 | Monitoring is ping checks of two servers and a weekly look at the Event Log. | NFR-01 |
| CS-23 | Last disaster-recovery test: never. Backups were restored manually twice in five years. | NFR-06 |

### 11.1 Conflicts and gaps found between sources

| # | Finding | Handling |
|---|---|---|
| F-1 | BR-04 says "always up to date". CS-10 and C-03 say Picking and Shipped change once per night and StockPilot cannot change. | **ASSUMPTION:** "as of the 02:00 batch" (A-04). **OPEN:** OPEN-01. |
| F-2 | BA-01 says "run Order Desk and its database in Azure". BA-02 says "plus the upgrade of Order Desk that the portal depends on". It is not stated who fixes the old-technology points CS-13 to CS-17 or moves staff sign-in from CS-04 to Microsoft Entra ID. | **ASSUMPTION:** A-03. **OPEN:** OPEN-03. |
| F-3 | CS-12 says confirmation e-mails are sent through the relay. The research found no mail-sending code in `src/` (A-22). | **OPEN:** OPEN-18. |
| F-4 | The portal pilot is in Q2 2027, which ends on 30 June 2027, the same day as the lease end (C-01). | **OPEN:** OPEN-05. |
| F-5 | NFR-01 to NFR-08 have no priority and some have no measurement basis. | **ASSUMPTION:** A-11, A-12. **OPEN:** OPEN-08. |
| F-6 | Nothing says where Confirmed, Delivered and Cancelled come from. CS-10 mentions only Picking and Shipped. | **ASSUMPTION:** A-05. **OPEN:** OPEN-02. |

## 12. Cross-track dependencies

No track waits for another track (ES-31). Where one area needs an answer that involves the other, it is an **OPEN:** item. Each track continues with its stated assumption until the answer arrives. The full wording, owners and affected tracks are in section 17.

| OPEN item | Topic | Tracks involved |
|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Azure and .NET |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Azure and .NET |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Azure and .NET |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Azure and .NET |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Azure and .NET |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Azure and .NET |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Azure and .NET |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Azure and .NET |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Azure and .NET |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Azure and .NET |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Azure and .NET |
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | .NET, with an effect on Azure |

(source: ES-30, ES-31, business-case §4)

## 13. Risks

Ratings are an **ASSUMPTION:** judgement for discussion (A-25). Risks that rely on code or database findings use A-22 and A-23.

| ID | Risk | Likelihood | Impact | Business-level response | Owner | Source |
|---|---|---|---|---|---|---|
| R-01 | The move is late and misses the lease end of 30 June 2027. | Medium | High | Keep at least one spare Sunday window before the date. Dates are targets only (A-07). | Marc Dubois | (source: C-01, BR-13, CS-21, A-07) |
| R-02 | The nightly StockPilot exchange cannot move to Azure in the same form. The research found it depends on features of the current database server that Azure's managed database does not offer. StockPilot cannot change. | High | High | Prove the exchange early with identical files, before committing to a plan. | Ahmed Benali | (source: CS-10, C-03, A-23) |
| R-03 | Order Desk code does not limit a signed-in user to their own company's data. Exposing it to customers as it stands would show customers each other's orders. | High | High | Treat customer data separation as a first step before any portal story that shows data. | Ahmed Benali | (source: BR-01, CS-04, A-22) |
| R-04 | "Always up to date" (BR-04) cannot be met. Customers may keep phoning. | Medium | Medium | Test whether status "as of the 02:00 batch" is enough, with a small group of pilot customers. | Lena Varga | (source: BR-04, CS-10, SM-02, A-04) |
| R-05 | The shared cost ceiling of EUR 1,500 per month is exceeded. Private connections, backups and 120 GB of files may use much of it. | Medium | High | Estimate cost early for several options. Agree who is accountable. | Marc Dubois | (source: C-04, CS-08, A-09, A-14) |
| R-06 | Ownership of the Order Desk upgrade is unclear. Work is duplicated or left undone. | Medium | High | Confirm the split (A-03) with the IT Manager. Neither track waits. | Ahmed Benali | (source: F-2, CS-13 to CS-17, A-03) |
| R-07 | The 48 GB database cannot be moved, checked and rolled back inside the six-hour Sunday window. | Medium | High | Measure transfer time and rehearse the move before the real date. | Ahmed Benali | (source: CS-07, CS-21, BR-13) |
| R-08 | Recovery targets (RPO 1 hour, RTO 4 hours) are not met because recovery was never tested. | Medium | High | Plan a tested restore with a report. | Ahmed Benali | (source: NFR-06, CS-23) |
| R-09 | The six-person IT team is stretched by two tracks at the same time and has limited container skills. | Medium | Medium | Prefer platforms the team can run. Keep one solution and the existing project boundaries (ES-13, ES-21). | Ahmed Benali | (source: C-06, ES-13, ES-21) |
| R-10 | Invoice delivery depends on the finance system, which is out of scope. After the exit, it must write somewhere Order Desk can read. The invoice folder year may follow the order year, not the invoice year. | Medium | Medium | Agree the hand-off with Finance. Confirm the year rule. | Julien Moreau | (source: CS-08, CS-11, BR-07, OPEN-06, OPEN-09, A-22) |
| R-11 | The pilot (20 customers) may not show the 35 % portal share in SM-01, if the pilot customers place too few orders (**ASSUMPTION:** A-46; their order volume is part of OPEN-05). The result would be judged as a failure. | High | Medium | Define "portal launch" and read the pilot customers' order volume before measuring. | Lena Varga | (source: SM-01, business-case §8, OPEN-05, A-46) |
| R-12 | The new hosting uses a different clock or time zone than Lyon (UTC against CET). Batch times, order dates and the audit trail shift. | Medium | Medium | Decide one time rule for the whole system. | Ahmed Benali | (source: CS-10, CS-21, A-10, OPEN-23) |
| R-13 | The audit history for 7 years grows the database and complicates recovery. | Low | Medium | Size retention and recovery together. | Ahmed Benali | (source: NFR-08, NFR-06, OPEN-22) |
| R-14 | Order confirmation and "Shipped" e-mail rely on a mail path that may not work from Azure, and the research found no sending code in `src/`. | Medium | Medium | Find out who sends e-mail today and agree a path. | Ahmed Benali | (source: CS-12, BR-09, OPEN-18, A-22) |
| R-15 | Customer sign-in options (OQ-01) cost more or have limits not yet checked. | Medium | Medium | Check price and limits before choosing. | Ahmed Benali | (source: NFR-04, OQ-01, A-21, OPEN-25) |
| R-16 | The portal has no French, English or Dutch text support today. All text is in English in the current screens. | High | Low | Lay a language foundation early. | Ahmed Benali | (source: BR-11, A-22) |
| R-17 | Pricing changes by accident during the upgrade. | Low | High | Keep the existing pricing tests and their checks unchanged (CS-20, ES-18). | Ahmed Benali | (source: CS-20, BR-12, ES-18) |

## 14. Timeline and how it maps to releases

### 14.1 Business-case timeline

| Period | Event | In scope? | Source |
|---|---|---|---|
| October to November 2026 | Discovery and planning | Yes | (source: business-case §8) |
| Q1 2027 | Delivery claims solution pilot with the Lyon Order Desk team | **No (BA-03)** | (source: business-case §8) |
| Before 30 June 2027 | Order Desk in Azure ("lift and modernise") | Yes (BA-01, with BA-02 for the modernisation, OPEN-03) | (source: business-case §8, C-01) |
| Q2 2027 | Customer Portal first release: pilot with 20 customers | Yes (BA-02) | (source: business-case §8) |

### 14.2 Business-level mapping to track releases

Release dates are **ASSUMPTION:** targets, not commitments (A-07). Only the release names and themes are fixed in the plan.

| Track | Release | Theme | Target (A-07) | Business outcome | Requirements it mainly carries |
|---|---|---|---|---|---|
| Azure | `azure-r1` | Foundation and proof | End of January 2027 | The biggest unknowns are answered early. A cost estimate exists. | NFR-05, NFR-03, NFR-01 (design and measure), C-04 (estimate) |
| Azure | `azure-r2` | Production cutover | Rehearsal by end of April 2027. Cutover in May 2027 | Order Desk runs in Azure. Staff keep working. | BR-13, NFR-01, NFR-03, NFR-05, NFR-06, C-01, C-03 |
| Azure | `azure-r3` | Stabilise and decommission | By 30 June 2027 | Old servers are retired. SM-07 reaches 0. | SM-07, C-04, NFR-06 (tested) |
| .NET | `dotnet-r1` | Modernised Order Desk | End of February 2027 | Order Desk is on a current platform with the same behaviour. Staff see the order channel. | NFR-05 (application), BR-10 (staff view) |
| .NET | `dotnet-r2` | Portal pilot: Must items | Pilot start in April 2027 | 20 pilot customers use the portal for the Must items. | BR-01 to BR-06, BR-10, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08 |
| .NET | `dotnet-r3` | Should items | Not dated | Invoices, customer administrators, French and English. | BR-07, BR-08, BR-11 |
| .NET | `dotnet-r4` | Could items and measures | Not dated | Shipped e-mail. The success measures SM-01 to SM-04 are measured. | BR-09, SM-01 to SM-04 |

How to read the mapping:

* Releases follow priority: Must, then Should, then Could. Preparation work comes before the features that need it (ES-31).
* Each track states in its release files what it does without an answer to a cross-track **OPEN:** item. No release waits for another track.
* The portal pilot in Q2 2027 and the lease end on 30 June 2027 fall in the same quarter. Whether the pilot runs on Azure is **OPEN:** OPEN-05.
* **OPEN:** OPEN-26. The product owner may split `dotnet-r2` into a read-only slice and a reorder slice if value is needed earlier.
* A release is approved by the product owner. Only then is a Git tag `product/<track>-r<n>` created. That step is outside this document (A-08, ES-31).

## 15. Traceability pointer

The full table lives in `docs/product/traceability.md` (ES-06, A-01). It maps every in-scope `BR-` (BR-01 to BR-13) and `NFR-` (NFR-01 to NFR-08) to stories, by track and release. It lists any in-scope ID without a story, and it lists BA-03 as out of scope. Constraints, success measures and open questions are mapped there to where they are carried. At the time of writing, no story exists yet, so no coverage is claimed here.

## 16. Assumptions (ES-03)

Every assumption has a person who can confirm it. Wording is identical in every product document. The master register is in `docs/product/README.md`. Entries not used by this document are in the master register only.

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
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 17. OPEN items (ES-04)

Wording is identical in every product document. Items marked "both" or "Azure and .NET" are cross-track and appear in the release files of both tracks under the same ID. None is a blocker for this document.

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

Business-case open questions kept in scope: OQ-01 is OPEN-13, OQ-02 is OPEN-14 and OQ-03 is OPEN-15. OQ-04 and OQ-05 belong to BA-03 and are out of scope (section 3.2).
