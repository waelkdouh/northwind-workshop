# Research: Northwind product documents for BA-01 (Azure) and BA-02 (.NET)

| Field | Value |
|---|---|
| Date | 2026-10-30 |
| Output mode | Convergence for planning (feeds Plan, then Author roles) |
| Posture | balanced (default), bounded by the caller's scope |
| Artifact path | `.copilot-tracking/research/2026-10-30/northwind-product-documents-research.md` |
| Inputs read | `knowledge-docs/business-case.md`, `current-state.md`, `engineering-standards.md`; `.copilot-tracking/reviews/intake-validation-ba01-ba02.md`; `README.md`; `.github/copilot-instructions.md`; `src/` (Core, Web, Tests); `database/001..003` |
| Planning readiness | **ready-with-gaps** (0 blocking, see sections 9 and 14) |

How to read the labels in this file:

* `BR-`, `NFR-`, `C-`, `SM-`, `CS-`, `ES-`, `BA-`, `OQ-`, `P-` = knowledge-docs identifiers (source of truth).
* `C1`..`C17` (no hyphen) = **research evidence IDs for code and database findings**. They are not business-case constraints (`C-01`..`C-08`).
* `W1` = external finding. `G-01`..`G-16` = intake gaps (intake-validation-ba01-ba02.md).
* **SRC** = verified in `src/` or `database/`. **DOC** = stated in knowledge-docs. **ASSUMPTION:** = anything else (ES-03). **OPEN:** = unanswered, with owner (ES-04).

---

## 1. Executive summary

* The scope is two business areas. BA-01 Azure owns BR-13 and the platform NFRs and constraints. BA-02 .NET owns BR-01..BR-12 and the portal NFRs. BA-03 Power Platform is out of scope (section 2.3). (DOC: business-case §4)
* **The Order Desk code is not safe to expose to customers as it stands.** No controller action checks which customer an order belongs to; `customerId` and order `id` come straight from the URL or form. The order `Channel` is posted by the browser, and the draft-order screen offers no Portal choice. BR-01, BR-10 and BR-06 therefore need new work, not just a new front end. (SRC: C5, C1)
* **The nightly StockPilot exchange is the hardest Azure item.** It is built on `xp_cmdshell`, `bcp`, `BULK INSERT` from a local `D:\` path and a SQL Server Agent job on `NWSQL01`. Azure SQL Managed Instance does not support `xp_cmdshell`, and its `BULK INSERT` reads only from Azure Blob storage (W1). StockPilot cannot change (C-03), so the exchange needs a redesign that keeps the file formats. (SRC: C3; DOC: CS-10, C-03)
* **BR-04 "always up to date" cannot be met as written.** Picking is set when the 02:00 export runs, Shipped when the 02:00 import runs, and Confirmed/Delivered/Cancelled have no automatic source in the code. (SRC: C2; DOC: CS-10, C-03; G-01, G-02)
* **The deadline drives the Azure slicing.** C-01 (30 June 2027) is a hard date. SM-07 (zero servers past end of support by that date) has no value until cutover, so Azure releases are ordered foundation, then production cutover, then hardening and decommission. The portal pilot (Q2 2027, DOC: §8) ends on the same day as the lease, so the pilot's hosting is an `OPEN:` item (G-07).
* **Recommended experiments:** BA-01, prove the StockPilot exchange in an Azure-compatible form before any build. BA-02, test whether nightly-fresh status is good enough to cut "where is my order?" calls, using a manual daily status e-mail with pilot customers. Both are cheap and need no deployment (ES-27). Details in section 6.
* Tracks never wait for each other. Section 8 lists 12 cross-track dependencies as `OPEN:` items for the release files (ES-31).

## 2. In-scope requirement inventory (answer a)

### 2.1 BA-01 Platform and data-centre exit — `track-azure`, releases `azure-r<n>`, Git tags `product/azure-r<n>` (DOC: §4, ES-30, ES-31)

| ID | Statement (DOC) | Priority | Cross-cutting? / note |
|---|---|---|---|
| BR-13 | Staff keep working through the move; planned downtime stays inside the Sunday window (CS-21: Sunday 06:00–12:00 CET) | Must | BA-01 only |
| NFR-01 | 99.5 % availability Mon–Sat 06:00–20:00 CET | none given (G-11) | Measurement method and scope (Order Desk only, or portal too) undefined. ASSUMPTION: Order Desk and portal both in scope; owner Lena Varga |
| NFR-03 | Customer and order data stay in the EU | none given | **Cross-cutting:** BA-01 lists it, BA-02 does not, but the portal stores EU customer data (G-03). One story per track (ES-30) |
| NFR-05 | No secret in source or repo config | none given | **Cross-cutting:** listed in both BA-01 and BA-02. One story per track (ES-30, ES-17, ES-25) |
| NFR-06 | RPO 1 h, RTO 4 h for order data | none given | BA-01. CS-07 has 15-minute log backups; CS-23 DR never tested |
| C-01 | Lease ends 30 June 2027; Order Desk must run in Azure before | — | Drives all dates |
| C-02 | Windows Server 2012 R2 and SQL Server 2014 are past end of support; ESU paid | — | Motivation |
| C-03 | StockPilot stays on premises (Antwerp) until at least 2028; exchange continues | — | No StockPilot change |
| C-04 | Run cost at most EUR 1,500/month for Order Desk + portal, prod + one test | — | **Shared** with BA-02 (G-06). OPEN: accountable owner |
| C-06 | 6-person IT team knows .NET/SQL Server; limited container skills | — | ES-21: PaaS, no Kubernetes |
| SM-07 | Production servers past end of support: 2, target 0 by 30 June 2027 | — | Measure: NWWEB01 and NWSQL01. OPEN: does NWFS01 count (G-16)? |
| ES-20..27 | France Central; PaaS; Bicep + AVM; naming `<abbr>-nw-<workload>-<env>-<region>` (env `tst`, `prd`); four tags; private endpoints + managed identity; one Log Analytics workspace per environment + App Insights; nothing deployed, validate with `az bicep build` | — | Constrain every Azure story |

Current-state facts the Azure track must cite: CS-06, CS-07, CS-08, CS-09, CS-10, CS-11, CS-12, CS-19, CS-21, CS-22, CS-23. Facts relevant when code is touched: CS-13..CS-17 (see section 4 and G-04).

### 2.2 BA-02 Ordering and customer self-service — `track-dotnet`, releases `dotnet-r<n>`, Git tags `product/dotnet-r<n>` (DOC: §4; tag forms are ASSUMPTION per G-14)

| ID | Requirement (DOC) | Priority |
|---|---|---|
| BR-01 | Customer user signs in and sees only own company's orders | Must |
| BR-02 | List of own company's orders, last 24 months: date, status, total | Must |
| BR-03 | Order detail: lines, quantities, prices, delivery address, status | Must |
| BR-04 | Status shown as Received / Confirmed / Picking / Shipped / Delivered / Cancelled, "always up to date" | Must (conflicts with CS-10, G-01) |
| BR-05 | New order by copying a previous one, edit quantities, remove lines | Must |
| BR-06 | Submitted portal order appears in Order Desk, status Received, no re-keying | Must |
| BR-07 | Download PDF invoice of a delivered order | Should |
| BR-08 | Customer administrator invites/removes own company's users | Should (OQ-03) |
| BR-09 | E-mail when order becomes Shipped | Could |
| BR-10 | Order Desk staff see whether an order came via portal or staff | Must |
| BR-11 | Portal in French and English; Dutch requested | Should (OQ-02) |
| BR-12 | Portal applies the customer's negotiated prices | Must |
| NFR-02 | Order list/detail under 2 s for 95 % of requests | none given; load profile unknown (G-11) |
| NFR-04 | Customers authenticate with an externally managed identity; staff use Entra ID | **Cross-cutting** (also BA-03). Staff move from Windows Integrated Authentication (CS-04) to Entra ID: ownership G-04 |
| NFR-05 | No secrets in source or config | **Cross-cutting** with BA-01: one story per track |
| NFR-07 | WCAG 2.2 AA | none given |
| NFR-08 | Every order change (who, what, when, channel) kept 7 years | none given; retention and retrieval undefined (G-11) |
| C-05 | Portal reuses Order Desk as single source of truth; no second order database | — |
| SM-01..SM-04 | Portal share 35 %; status calls 410→≤250; line corrections 4.1 %→≤2.5 %; invoice requests 120→≤40, all 6 months after portal launch | — (SM-01 vs 20-customer pilot, G-08; "launch" undefined) |
| OQ-01, OQ-02, OQ-03 | Customer IdP; Dutch in first release; customer admins for all or only large customers | OPEN |

ES that constrain .NET stories: ES-13..ES-19 (one solution, Core/Web/Tests; SDK-style, `net10.0`; options pattern; `ILogger<T>`; no secrets; `dotnet test src/Northwind.OrderDesk.sln` cross-platform without weakening assertions; modernise in place, keep namespaces).

### 2.3 Out of scope (list in every document; ES-06)

BA-03 Delivery claims and credit notes (`track-power-platform`): BR-14..BR-19, NFR-09, C-07, C-08, SM-05, SM-06, OQ-04, OQ-05, CS-24..CS-28, ES-32..ES-37. BA-03 shares NFR-03 and NFR-04 (DOC: §4). Business-case §6 exclusions: online payment, native mobile app, StockPilot changes, replacing the finance system, customer-recorded claims.

Informational only: BA-03 will need an Order Desk API (CS-27, ES-36). If the .NET track builds an API for the portal, BA-03 could reuse it. This is an `OPEN:` item (X-12), not a dependency of any release.

### 2.4 Cross-cutting requirements: how to split (ES-30)

| Requirement | `track-azure` story (platform) | `track-dotnet` story (application) |
|---|---|---|
| NFR-05 | Key Vault, managed identities, no secret in IaC or pipeline variables (ES-17, ES-25) | Remove `Integrated Security`/passwords and secrets from `Web.config`; options pattern (CS-13, CS-17, ES-15) |
| NFR-03 | Regions France Central + EU secondary only; EU-resident backups and logs (ES-20) | Portal IdP, e-mail provider and telemetry store customer data only in the EU (ASSUMPTION: BA-02 must cite NFR-03, G-03) |
| NFR-04 | Platform-side sign-in plumbing (Entra tenant, app registrations, hosting auth), only if the platform track owns it (ASSUMPTION; G-04) | Customer IdP integration (OQ-01) and staff Entra sign-in in the app |
| NFR-06 / NFR-08 | RPO/RTO for the order database (NFR-06) | Audit content (NFR-08); retention of 7 years sized and backed up by Azure (X-10) |

## 3. Method and boundaries (short Research Record)

* Extensions: `.github/copilot-instructions.md` applied (scope, identifiers, no deployment). The `rpi-research` skill is the contract.
* Prior-knowledge gate: intake gaps G-01..G-16 taken as given and not re-derived.
* Waves in one cycle: **Wider** read all knowledge-docs, README, the 33 `.cs` files, 7 `.cshtml` views, `Web.config` and 3 SQL scripts. **Deeper** followed status, channel, pricing, invoices, audit, configuration and exchange paths line by line. **Contrarian** looked for evidence against the intake assumptions. Result: CS-12 says confirmations go through SMTP, yet no sending code exists in `src/` (C14); the BA-02 text in §4 does assign the Order Desk upgrade to BA-02 (G-04, X-01); `Orders.InvoiceNumber` already exists (C7).
* Helper lanes: **none dispatched.** The evidence base was one small repository that fit a direct read, so isolating lanes would not have improved evidence. Lane table: not applicable. The charter's lane contract was not exercised.
* External: one web search (Azure SQL MI T-SQL differences, W1). A second search (Entra External ID pricing, .NET 10 on App Service) **failed (HTTP 504)** and stays unverified (U1 in section 9).

## 4. Code and database findings (answer b)

All rows are **SRC** (sourced from `src/` or `database/`) unless marked. Paths are relative to `C:\demos\northwind-workshop`. Anything in the "Why it matters" column that is not in knowledge-docs is an ASSUMPTION.

| ID | Finding | Source (file / symbol) | Why it matters | vs knowledge-docs |
|---|---|---|---|---|
| C1 | **Order channel (BR-10).** Stored as `Orders.Channel TINYINT` (0 Phone, 1 Email, 2 OrderForm, 3 Portal). Enum `OrderChannel` already has `Portal = 3`. The channel is shown to staff in the order list and detail. `OrderService.Submit(draft, channel, user)` takes the channel as a parameter, and the MVC form posts it from a dropdown that offers only Phone, E-mail and Order form. | `database/001-schema.sql` (Orders); `Core/Domain/OrderChannel.cs`; `Web/Views/Orders/Draft.cshtml`; `Web/Models/DraftOrderInput.cs`; `Web/Views/Orders/Index.cshtml`, `Details.cshtml` | BR-10 is largely a data-model fact already. A portal must set the channel server-side (never trust a client-supplied value). ASSUMPTION: BR-10 stories are small (display and filter) plus a portal-side stamp. | New detail; supports BR-10 |
| C2 | **Status handling (BR-04).** Codes 0 Received, 1 Confirmed, 2 Picking, 3 Shipped, 4 Delivered, 9 Cancelled. Allowed transitions: Received→Confirmed/Cancelled; Confirmed→Picking/Cancelled; Picking→Shipped; Shipped→Delivered; all else refused. Staff move status by hand through `OrdersController.ChangeStatus`. The 02:00 export sets Confirmed→Picking (`Status = 2`) itself; the 02:00 import sets Picking→Shipped for orders listed in `shipments.csv`. No code path sets Delivered or Confirmed automatically. | `Core/Domain/OrderStatusRules.cs`; `Web/Controllers/OrdersController.cs` (ChangeStatus); `database/003-stockpilot-exchange.sql`; `database/001-schema.sql` | Freshness of Picking/Shipped is "as of 02:00" (CS-10). ASSUMPTION: Delivered, Confirmed and Cancelled are entered manually by staff. OPEN: status-to-source mapping (G-02; owner Lena Varga). BR-04 stories should state freshness as an ASSUMPTION. | Supports CS-10; refines it: Picking is set by Order Desk at export, not imported |
| C3 | **StockPilot exchange (BA-01).** SQL Agent job "NW - StockPilot nightly" at 02:00 runs `usp_ExportConfirmedOrdersForStockPilot` (`xp_cmdshell` + `bcp queryout` to `D:\Exchange\StockPilot\out\orders_YYYYMMDD.csv`, delimiter `;`, `-S NWSQL01 -T`; selects Status=1 and not yet exported) and `usp_ImportShipmentsFromStockPilot` (`BULK INSERT` from `D:\Exchange\StockPilot\in\shipments.csv`, header row skipped, columns OrderNumber;ShippedAt;Carrier). A Windows scheduled task on `NWSQL01` syncs the folder to the Antwerp SFTP server. The server name is hard-coded. | `database/003-stockpilot-exchange.sql` (header comments, both procedures) | Not portable as is. W1: Azure SQL MI has no `xp_cmdshell` and `BULK INSERT` reads only from Azure Blob; SQL Agent is supported in MI. File formats must stay identical (C-03). `ShippedAt` and `Carrier` are read but never stored (ASSUMPTION: BR-09 and any shipment detail need them stored). The SFTP host location is not in knowledge-docs (G-10). | Supports CS-10; adds detail not in DOC |
| C4 | **Import audit defect.** The import writes `Status:Shipped` audit rows for every joined shipment row, not only for orders actually moved from Picking, so a replay or a repeated row adds false audit entries. The procedure is not idempotent. | `database/003-stockpilot-exchange.sql` (`usp_ImportShipmentsFromStockPilot`) | Touches NFR-08 audit integrity; any migration of the exchange should preserve or consciously fix this (ES-19: a change needs a decision record). ASSUMPTION: unintended. | New; not in DOC |
| C5 | **No customer scoping or authorisation.** `OrdersController.Index(customerId)`, `Details(id)` and `Invoice(id)` accept ids from the request and return the data. `Copy(id, customerId)` verifies the order belongs to the posted `customerId`, but that id is client-supplied. The only protection is a global `[Authorize]` filter and Windows authentication with `deny users="?"`. `HomeController.FindCustomer` lets any signed-in user open any customer. | `Web/Controllers/OrdersController.cs`; `Web/Controllers/HomeController.cs`; `Web/App_Start/FilterConfig.cs`; `Web/Web.config` | BR-01 (Must) cannot be met by reusing the controllers. Tenant isolation (company claim → customer id) is net-new and security-critical. Also relevant to BR-07 (invoice ownership). | Consistent with CS-04 (staff only today) |
| C6 | **Pricing (BR-12, CS-20).** `PricingService`: negotiated price replaces list price; volume discount 5 % from 50 units, 8 % from 100 units unless the agreement excludes it; Gold tier gets 2 % off the order at a subtotal of EUR 1,000; rounding half away from zero per line and total. Agreements are valid when `ValidFrom <= GETDATE()` and `ValidTo` is null or in the future. `CopyOrder` copies lines and quantities only; **prices are never copied and are recalculated only in `Submit`**, so the draft screen shows no prices. | `Core/Pricing/PricingService.cs`; `Core/Services/OrderService.cs` (`CopyOrder`, `Submit`); `Core/Data/SqlOrderDeskStore.cs` (`GetAgreement`); `Web/Views/Orders/Draft.cshtml` | The portal must call the same `PricingService` (C-05, CS-20). BR-12 "customer sees their price" before submitting is new work (for example using the public `PriceLine`). OPEN: should the customer see volume and Gold discounts (Lena Varga)? 15 `[TestMethod]` tests in `PricingServiceTests.cs` guard this (ES-18). | Supports CS-20; adds the draft-price gap |
| C7 | **Invoices (BR-07).** `InvoiceStore` builds `{InvoiceSharePath}\{year}\{invoiceNumber}.pdf`; `OrdersController.Invoice` passes **`order.OrderDate`** as the date, so the year folder is the *order* year. Served only if status is Delivered and `InvoiceNumber` is set. `Orders.InvoiceNumber` (nullable) already exists. Nothing in `src/` writes it. | `Core/Invoices/InvoiceStore.cs`; `Web/Controllers/OrdersController.cs` (Invoice); `database/001-schema.sql` | ASSUMPTION: the finance system or an unseen job fills `InvoiceNumber`; if an invoice is issued in a later year than the order, the lookup fails (CS-11 says the folder is by invoice year). OPEN: confirm (Julien Moreau; G-12). In Azure the UNC share needs a replacement (120 GB, +2 GB/month, CS-08) and the finance system writes there (G-09). | Supports CS-11, CS-14; adds the year risk |
| C8 | **Order history (BR-02, NFR-02).** `OrderHistoryMonths = 24` in `appSettings`. The list query is `WHERE CustomerId AND OrderDate >= @from ORDER BY OrderDate DESC`, supported by `IX_Orders_Customer_Date`. There is **no paging**. Sample data holds only 4 customers and a few rows. | `Web/Web.config`; `Web/Controllers/OrdersController.cs` (Index); `Core/Data/SqlOrderDeskStore.cs`; `database/002-sample-data.sql` | The index supports BR-02. Paging and a load profile are needed for NFR-02. Whether 24 months of orders exist in production is unconfirmed (G-12). | Consistent with BR-02 |
| C9 | **Audit (NFR-08).** `OrderAudit(Action, ChangedBy NVARCHAR(100), Channel, ChangedAt UTC)` is written on Created and on every `UpdateStatus`. Channel is `NULL` on status changes. Order edits do not exist today. There is no retention, immutability or archive mechanism; the schema comment says "kept for 7 years". | `Core/Data/SqlOrderDeskStore.cs` (`InsertAudit`, `UpdateStatus`); `database/001-schema.sql` | NFR-08 asks for who, what, when, channel. Status-change rows lack channel; "what" is a free-text action. ASSUMPTION: field-level detail is not needed until order edits exist (OPEN: Lena Varga). The portal user identity must fit 100 characters. | Partially supports NFR-08 |
| C10 | **Time zone.** `OrderService` uses `DateTime.Now` (local) and `Orders.OrderDate` is `DATETIME`; exports use `GETDATE()` (server local); audit uses `GETUTCDATE()`. | `Core/Services/OrderService.cs`; `Core/Data/SqlOrderDeskStore.cs`; `database/003-stockpilot-exchange.sql` | ASSUMPTION: Azure hosts default to UTC, so "02:00 CET" semantics, the 24-month window and `orders_YYYYMMDD.csv` file dates can shift. Needs an explicit decision (X-11). | New; not in DOC |
| C11 | **Session state (CS-16).** `Session["DraftOrder"]` holds the draft order; `sessionState mode="InProc"` with 60 min timeout. Any scale-out above one instance loses drafts. | `Web/Controllers/OrdersController.cs` (`DraftSessionKey`); `Web/Web.config` | Constrains instance count and cost (C-04) unless drafts move to a shared store; the portal reorder flow (BR-05) depends on it. | Confirms CS-16 |
| C12 | **Configuration and logging (CS-13, CS-15, CS-17).** Connection string `Data Source=NWSQL01;...;Integrated Security=SSPI`; `InvoiceSharePath=\\NWFS01\invoices`; `SmtpHost=smtp.northwind.local` port 25; `ConfigurationManager` in `SqlOrderDeskStore` and `InvoiceStore`; `EventLogErrorLogger` writes source "Northwind Order Desk" (created by an install script on `NWWEB01`; the script is not in the repo); `ServiceFactory` creates services statically (no DI). | `Web/Web.config`; `Core/Data/SqlOrderDeskStore.cs`; `Core/Invoices/InvoiceStore.cs`; `Core/Logging/EventLogErrorLogger.cs`; `Web/Infrastructure/ServiceFactory.cs` | Direct evidence for CS-13..CS-17 and for NFR-05/ES-15..ES-17 stories. No secret is stored today because SSPI is used; moving to managed identity changes the connection model (ES-25). | Confirms |
| C13 | **Build and tests (CS-18, CS-19).** Old-style projects, .NET Framework 4.8, `packages.config`. Tests reference `Microsoft.VisualStudio.QualityTools.UnitTestFramework 10.1.0.0` from the VS installation. 28 `[TestMethod]`s: Pricing 15, OrderService 9, OrderStatusRules 4. | `src/Northwind.OrderDesk.*/*.csproj`; `src/Northwind.OrderDesk.Tests/*.cs` | A pipeline can only build on Windows with VS-style tooling until migrated (ES-14, ES-18). The test count gives a baseline for ES-18. | Confirms CS-18 |
| C14 | **No e-mail sending code.** SMTP settings exist in `Web.config` (`smtp.northwind.local:25`, no authentication), but no `SmtpClient` or `MailMessage` code exists in `src/`. | `Web/Web.config`; search over `src/` found no mail code | CS-12 says confirmations are sent. ASSUMPTION: sent by another component, or not from this repo. OPEN: Ahmed Benali. BR-09 (Could) needs new sending code and a relay path (X-09). | Does not match CS-12 |
| C15 | **No localisation.** No `.resx` files; view text is hard-coded English ("Customer number", "Back to customer orders"). | `Web/Views/**` | BR-11 is net-new; supports laying down a resource-file scaffold early. | New |
| C16 | **No API and no JSON endpoints.** Server-rendered MVC views only. | `Web/Controllers/*` | Consistent with CS-27. The portal can be added to `Web` (ES-13: one solution, no new project without a decision record) or as a separate project with an ADR. OPEN decision for the architect. | Confirms CS-27 |
| C17 | **Order numbers.** `NW-` + sequence `OrderNumberSequence` formatted `D7`. | `Core/Data/SqlOrderDeskStore.cs` (`NextOrderNumber`); `database/001-schema.sql` | A portal order uses the same sequence (C-05); the same `OrderNumber` is the StockPilot key. | New |

External:

| ID | Finding | Source | Retrieved | Confidence |
|---|---|---|---|---|
| W1 | Azure SQL Managed Instance does not support `xp_cmdshell`; `BULK INSERT` is supported only from Azure Blob storage; SQL Server Agent is supported in Managed Instance (and not in Azure SQL Database). | https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server?view=azuresql (via search summary; page not opened in full) | 2026-10-30 | Medium (summary of the official page; confirm before the ADR) |

## 5. Candidate enabler work (answer d)

Enablers are stories tagged with one track tag, citing sources. IDs below are *candidate* names for the backlog author.

### 5.1 `track-azure` enablers

| Candidate | Why before features | Sources |
|---|---|---|
| AZ-EN-01 Azure foundation: subscription layout, France Central, naming, tags, Bicep + AVM skeleton per environment (`tst`, `prd`), validated with `az bicep build` only | Everything else lands here | C-01, ES-20, ES-22..ES-24, ES-27 |
| AZ-EN-02 Network and hybrid connectivity: replacement for the Lyon–Antwerp VPN, private endpoints, path to the Antwerp SFTP host and to AD/Entra Connect | StockPilot exchange and identity depend on it. OPEN: path owner (G-10) | CS-09, CS-10, C-03, ES-25 |
| AZ-EN-03 Hosting and data target decision (ADR): app host, SQL target (Managed Instance vs SQL Database vs IaaS VM), cost-checked against C-04 | The SQL target decides how the exchange is rebuilt (W1) | C-02, C-04, C-06, ES-21, C3, W1 |
| AZ-EN-04 Secrets, managed identities and Key Vault (platform side of NFR-05) | NFR-05 | NFR-05, ES-17, ES-25 |
| AZ-EN-05 Observability baseline: Log Analytics workspace per environment, App Insights, availability probe for NFR-01, alerts | Replaces ping checks and a weekly Event Log look | CS-22, NFR-01, ES-26 |
| AZ-EN-06 Backup, DR and a **tested** restore (RPO 1 h, RTO 4 h) | Never tested today | CS-07, CS-23, NFR-06 |
| AZ-EN-07 Deployment pipeline for infrastructure and the web app (separate from the .NET build pipeline, see X-07) | No automated deploy today | CS-19, ES-22 |
| AZ-EN-08 Database migration approach and rehearsal (48 GB, +1 GB/month) inside the Sunday window | BR-13 | CS-07, CS-21, BR-13 |
| AZ-EN-09 StockPilot exchange redesign preserving file formats, 02:00 cadence and CSV paths for Antwerp | Not portable (C3) | CS-10, C-03, C3, W1 |
| AZ-EN-10 Invoice file store migration (120 GB, +2 GB/month) and the finance write target | The finance system writes to the share (OPEN with Julien Moreau) | CS-08, CS-11, G-09 |
| AZ-EN-11 SMTP relay replacement (for example an authenticated service reachable from Azure) | The internal relay is not reachable after exit (ASSUMPTION) | CS-12, C14 |
| AZ-EN-12 Cost model for prd + one tst against C-04 | The ceiling is a hard constraint | C-04, G-06 |
| AZ-EN-13 Cutover runbook, rollback plan and decommissioning checklist | BR-13, SM-07 | BR-13, CS-21, SM-07 |

### 5.2 `track-dotnet` enablers

| Candidate | Why before features | Sources |
|---|---|---|
| DN-EN-01 Move the solution to SDK-style projects on `net10.0`, keep one solution and the Core/Web/Tests boundaries, keep namespaces | Prerequisite for every portal story | CS-01, CS-02, ES-13, ES-14, ES-19 |
| DN-EN-02 Make `dotnet test src/Northwind.OrderDesk.sln` pass on Windows, macOS and Linux with the 28 tests, no weakened assertions, pricing unchanged | Safety net for pricing | CS-18, CS-20, ES-18, C13 |
| DN-EN-03 Configuration via `Microsoft.Extensions.Configuration` and options; no `ConfigurationManager` | | CS-17, ES-15, C12 |
| DN-EN-04 Logging via `ILogger<T>`; remove Event Log | | CS-15, ES-16, C12 |
| DN-EN-05 Remove `Integrated Security` and any secret from configuration (application side of NFR-05) | | CS-13, NFR-05, ES-17 |
| DN-EN-06 Replace in-process session for the draft order | | CS-16, C11 |
| DN-EN-07 Replace the UNC invoice read with a storage abstraction (path or blob) | | CS-14, C7 |
| DN-EN-08 Staff sign-in with Entra ID (replaces Windows Integrated Authentication) | NFR-04. OPEN ownership (G-04) | CS-04, NFR-04 |
| DN-EN-09 Build and test pipeline for the solution | | CS-19, CS-18, X-07 |
| DN-EN-10 Tenant-isolation foundation: map a signed-in customer user to one customer and apply it to every data read | Prerequisite for BR-01, BR-02, BR-03, BR-07 | C5, BR-01, C-05 |
| DN-EN-11 Portal architecture ADR: add portal to `Web` or add a project, API shape, IdP choice (OQ-01) | Needed before stories are sliced further | ES-13, C16, OQ-01 |
| DN-EN-12 Localisation scaffold (resource files) | Cheaper before more screens exist | BR-11, C15 |
| DN-EN-13 Audit completeness: channel on status changes, retention approach | NFR-08 | C9, NFR-08, G-11 |
| DN-EN-14 Accessibility baseline for the portal (WCAG 2.2 AA) | NFR-07 is easier to build in than to add | NFR-07 |

## 6. Candidate riskiest assumptions and cheap experiments (answer c)

Rules for all experiments: design and review only. Nothing is deployed, no production data leaves its place, no change to `src/`, `database/` or `infra/` (ES-27 and the run boundary). Thresholds are **ASSUMPTION:** to be confirmed by the owner.

### 6.1 BA-01

| # | Assumption | Why risky | Evidence | Cheap test (before building) |
|---|---|---|---|---|
| A1 (**recommended MVE**) | The nightly StockPilot exchange (export CSV, import CSV, 02:00 cadence, Antwerp SFTP) can be reproduced in an Azure-compatible way with **byte-identical files** and no StockPilot change | It silently stops shipments if wrong; C-03 forbids changing StockPilot; the current design uses features Managed Instance lacks (W1); the SFTP path after the VPN is unknown (G-10) | C3, C4, W1, CS-10, C-03 | Take the two procedures and sample data. Write a one-page design plus a local, throwaway proof on a developer SQL Server (no Azure) that produces `orders_YYYYMMDD.csv` and ingests a sample `shipments.csv` without `xp_cmdshell` or a local `D:\` bulk load. Compare output byte for byte with the legacy output of the same sample. Ask Antwerp IT in a 30-minute call for the SFTP host, the account type and the file pick-up window. **Success (ASSUMPTION):** identical bytes on 3 sample runs, a named network path, and Antwerp confirmation. **Pivot:** if identical files need SQL on a VM, re-run A3 with that cost. |
| A2 | The 48 GB database (+1 GB/month) can be moved and cut over inside the Sunday 06:00–12:00 window and meet RPO 1 h / RTO 4 h | BR-13 is Must; unknown network throughput from Lyon; nobody has restored a backup under time pressure (CS-23) | CS-07, CS-21, NFR-06, BR-13 | Measure upload throughput from Lyon to a test storage location with a non-production file; compute transfer time for 48 GB (plus 1 GB/month until cutover) and compare to the 6-hour window; list the options (backup/restore, log shipping, migration service). **Success (ASSUMPTION):** the model finishes in 3 hours or less, leaving half the window for validation and rollback. |
| A3 | Production plus one test environment, with private endpoints, backup and monitoring, fits EUR 1,500/month | A SQL service plus private endpoints and storage could use most of the budget; C-04 covers the portal too | C-04, C-06, ES-21, ES-25, G-06 | Desk estimate with the Azure pricing calculator for 3 options (A: SQL Managed Instance + App Service; B: SQL Database + App Service; C: IaaS VM) with every private endpoint and 120 GB of files counted. **Success (ASSUMPTION):** at least one option at or under EUR 1,350 (10 % headroom). Do this first; it takes about a day. |
| A4 | The legacy app can run on the target platform with config-only change until the .NET track delivers | If false, azure-r2 depends on a dotnet release, which ES-31 forbids | C12, CS-13, CS-04, G-04 | List every point where the app breaks without Windows authentication, UNC paths and the Event Log; classify config-only vs code. OPEN: ownership (G-04). |

### 6.2 BA-02

| # | Assumption | Why risky | Evidence | Cheap test |
|---|---|---|---|---|
| B1 (**recommended MVE**) | A status view that is only as fresh as the nightly 02:00 update is good enough that customers stop phoning "where is my order?" (410 calls/week, 35 % of inbound calls) | BR-04 says "always up to date" but CS-10 and C-03 make that impossible; if customers need hour-level status, SM-02 will not move and the portal's main value (P-03) fails | P-03, BR-04, CS-10, C-03, C2, SM-02, G-01 | A manual concierge test with the Order Desk team and about 10 of the 20 pilot customers: for 2 weeks, send a short daily e-mail at 08:00 with the status of each open order, built from the same status data (C2) and labelled "as of 02:00". Track weekly "where is my order?" calls from those 10 customers against their own prior 2-week baseline, and ask a 2-question survey ("did it answer your question?"). **Success (ASSUMPTION):** at least 30 % fewer such calls from that group and at least 70 % say the status was enough. **Pivot:** if not, re-open BR-04 freshness with Lena Varga and raise the StockPilot constraint (out of scope today). |
| B2 | 70 % of orders repeat a previous order with small changes, so copy-and-edit (BR-05) is the right first order feature | The 70 % figure is a business-case claim without a data source (P-04) | P-04, BR-05, SM-01 | A read-only query on the last 12 months of order lines (by a person with database access, for example Ahmed Benali): for each order, the share of lines that also appeared in the same customer's previous order. **Success (ASSUMPTION):** at least 60 % of orders have at least 70 % overlap. No build needed. |
| B3 | Customers (1,150, mostly small grocers and kitchens) will accept the chosen sign-in method, and a company administrator can manage users (BR-01, BR-08, OQ-01, OQ-03) | Onboarding friction can stall the pilot; OQ-01 is open | OQ-01, OQ-03, NFR-04 | Interview 5–8 pilot customers with a paper or clickable mock of the sign-in and invite flow; record how many complete it unaided. |
| B4 | The 20-customer pilot can reach a meaningful share of orders to learn from (SM-01) | 35 % of all orders is not reachable with 20 of 1,150 customers (G-08) | SM-01, DOC §8, G-08 | Desk calculation: orders per pilot customer from the same query as B2. OPEN: define "launch". |

## 7. Proposed release slicing (answer e)

Dates are **ASSUMPTION:** to be set with the product owner (G-07). Items are ordered Must before Should before Could; enablers precede the features that need them. Every release file must state its dependencies on the other track as `OPEN:` items and never wait for it (ES-31).

Calendar anchors: discovery Oct–Nov 2026 (DOC §8); portal pilot with 20 customers in Q2 2027 (DOC §8); lease end and Order Desk in Azure by 30 June 2027 (C-01).

### 7.1 `track-azure`

| Release | Theme | Candidate content | Covers | Rationale and target (ASSUMPTION) |
|---|---|---|---|---|
| `azure-r1` | **Foundation and proof** | AZ-EN-01..AZ-EN-03, AZ-EN-12; findings of experiments A1, A2, A3; AZ-EN-04, AZ-EN-05 on `tst`; AZ-EN-07 for infrastructure | NFR-05 (platform), NFR-03 (platform), NFR-01 (design and measure), C-04 estimate; partial NFR-06 design | Removes the biggest unknowns early. Target: ready by end of January 2027, so rehearsals can run. A cutover cannot happen without these. |
| `azure-r2` | **Production cutover** | AZ-EN-02, AZ-EN-06, AZ-EN-08..AZ-EN-11, AZ-EN-13; `prd` environment; rehearsal on `tst`; cutover in a Sunday window | BR-13, NFR-01, NFR-03, NFR-05, NFR-06, C-01, C-03 | The Must outcome. Target: rehearsal complete by end of April 2027, production cutover in a Sunday window in May 2027, leaving about 6 weeks of contingency before 30 June 2027. At least one spare Sunday must stay free. |
| `azure-r3` | **Stabilise and decommission** | Decommission NWWEB01 and NWSQL01 (and NWFS01 if it counts in SM-07); cost check against C-04; DR test report; runbooks | SM-07, C-04, NFR-06 (tested) | Closes SM-07 by 30 June 2027. May be merged into `azure-r2` if the product owner prefers two releases. |

### 7.2 `track-dotnet`

| Release | Theme | Candidate content | Covers | Rationale and target (ASSUMPTION) |
|---|---|---|---|---|
| `dotnet-r1` | **Modernised Order Desk (enabler release)** | DN-EN-01..DN-EN-07, DN-EN-09; staff-visible BR-10 stories (channel shown, Portal value) | NFR-05 (application), BR-10 (staff view), ES-14..ES-19 | Nothing for customers can be built safely on .NET Framework 4.8 and a test suite that only runs in Visual Studio (C13). Behaviour preserved, pricing tests intact (CS-20). Target: end of February 2027. |
| `dotnet-r2` | **Portal pilot: Must items** | DN-EN-08, DN-EN-10..DN-EN-14; BR-01, BR-02, BR-03, BR-04 (nightly-freshness ASSUMPTION), BR-05, BR-06, BR-10 (portal stamp), BR-12; NFR-02, NFR-03 (application), NFR-04, NFR-07, NFR-08 | Must items BR-01..BR-06, BR-10, BR-12; NFR-02, 03, 04, 07, 08 | The nine Must items make up the pilot expected in Q2 2027. Target: pilot start in April 2027. Hosting of the pilot is `OPEN:` (X-02, X-08). Could be split into a read-only slice (BR-01..BR-04, BR-12 display) and a reorder slice (BR-05, BR-06) if the product owner wants value earlier (B1 evidence). |
| `dotnet-r3` | **Should items** | BR-07 (invoices), BR-08 (customer admin), BR-11 (French/English; Dutch per OQ-02) | BR-07, BR-08, BR-11 | Next-priority items. Pilot customers are in FR/BE/LU (DOC §1), so French may be needed earlier: a trade-off for the product owner (OQ-02, Sofie Peeters). Depends on B3 and on invoice storage (X-05). |
| `dotnet-r4` | **Could items and growth** | BR-09 (shipped e-mail); work towards SM-01..SM-04 after the pilot | BR-09; SM-01..SM-04 measurement | Only after Must and Should. Needs the SMTP path (X-09) and stored shipment data (C3). |

Items not yet planned stay with the track tag only (ES-31).

## 8. Cross-track dependency candidates — write each as `OPEN:` in both releases; none blocks a release (answer g)

| ID | Dependency candidate | Between | Proposed owner | Sources |
|---|---|---|---|---|
| X-01 | **Who modernises the Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in)?** ASSUMPTION: `.NET` owns the code (DOC §4 BA-02 says "plus the upgrade of Order Desk that the portal depends on") and `Azure` owns hosting, data and the exchange. DOC §4 BA-01 says only "run Order Desk and its database in Azure". | azure ↔ dotnet | Ahmed Benali (IT Manager), with Lena Varga | G-04, CS-13..CS-17, ES-12, ES-19 |
| X-02 | Hosting target and database target that the portal and the modernised app will run on (runtime, SQL choice, instance count, session state C11) | dotnet needs azure's ADR (AZ-EN-03) | Ahmed Benali | C-04, C-06, ES-21, C11 |
| X-03 | Customer identity provider (OQ-01) vs the Entra tenant and platform sign-in plumbing | dotnet ↔ azure | Ahmed Benali | OQ-01, NFR-04, G-03 |
| X-04 | StockPilot exchange redesign (azure) vs the BR-04 freshness assumption and any schema change from the .NET track; schema changes need a migration-impact check | azure ↔ dotnet | Lena Varga (freshness), Ahmed Benali (schema) | G-01, G-10, C2, C3, C-03 |
| X-05 | Invoice storage after exit: where the finance system writes and how Order Desk reads | azure ↔ dotnet (and Finance) | Julien Moreau | CS-08, CS-11, BR-07, C7, G-09, G-12 |
| X-06 | Cost ceiling C-04 shared by both tracks; accountable owner and split | azure ↔ dotnet | Marc Dubois (sponsor) | C-04, G-06 |
| X-07 | CI/CD: one solution, two tracks; who owns the build/test pipeline and who owns the deployment pipeline | azure ↔ dotnet | Ahmed Benali | CS-19, CS-18, ES-13 |
| X-08 | Portal pilot timing vs lease end: pilot environment, and whether the pilot runs on Azure | dotnet ↔ azure | Marc Dubois, Lena Varga | G-07, C-01, DOC §8 |
| X-09 | SMTP relay replacement (azure) vs BR-09 and order confirmation e-mail (dotnet); C14 shows no sending code in `src/` | azure ↔ dotnet | Ahmed Benali | CS-12, BR-09, C14 |
| X-10 | Audit retention: 7-year order audit (NFR-08) sizing, backup and retrieval vs RPO/RTO (NFR-06) | dotnet ↔ azure | Lena Varga (retention need), Ahmed Benali | NFR-06, NFR-08, C9, G-11 |
| X-11 | Time zone and clock: CET vs UTC for batch times, order dates and audit | azure ↔ dotnet | Ahmed Benali | C10, CS-10, CS-21 |
| X-12 | Order Desk API (informational): BA-03 needs one (CS-27, ES-36); the portal may create one | dotnet ↔ power-platform (out of scope) | Ahmed Benali | CS-27, ES-36 |

## 9. Open questions and proposed owners (answer f; ES-04)

Owners are **ASSUMPTION:** proposals for the product owner (Lena Varga owns the backlog, DOC §5) to confirm (G-05).

| ID | Question | Proposed owner | Area |
|---|---|---|---|
| OQ-01 | Identity provider for customer users | Ahmed Benali | BA-02 |
| OQ-02 | Dutch in the first release | Sofie Peeters with Lena Varga | BA-02 |
| OQ-03 | Customer administrators for all customers or only large ones | Lena Varga | BA-02 |
| OQ-04, OQ-05 | Claims questions | Julien Moreau; Lena Varga | **BA-03, out of scope; informational** |
| G-01 | Acceptable freshness for BR-04 (nightly) | Lena Varga | BA-02 |
| G-02 | Source of Confirmed, Delivered, Cancelled status | Lena Varga with the Order Desk team | BA-02 |
| G-04 | Ownership of the Order Desk modernisation (X-01) | Ahmed Benali | both |
| G-06 | Accountable owner of the EUR 1,500 ceiling | Marc Dubois | both |
| G-07 / G-08 | Meaning of "portal launch"; pilot on Azure before 30 June 2027? | Marc Dubois, Lena Varga | both |
| G-09 | How invoice output reaches Azure | Julien Moreau | azure |
| G-10 | Network path and SFTP host location after the exit | Ahmed Benali with Pieter Janssens (Antwerp) | azure |
| G-11 | NFR measurement bases and priorities (NFR-01, NFR-02, NFR-08) | Lena Varga | both |
| G-12 | 24 months of orders present; where `InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | dotnet |
| G-13 | Mobile and browser support; data-protection requirement for customer users | Ahmed Benali (data protection), Sofie Peeters (mobile) | dotnet |
| G-14 | Backlog publishing tool (ES-39); confirm release names `azure-r<n>`, `dotnet-r<n>` | Lena Varga | both |
| G-16 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | azure |
| New (C6) | Should customers see volume and Gold discounts, or only the net price? | Lena Varga | BA-02 |
| New (C9) | Is the free-text audit action enough for NFR-08, or are field-level changes needed? | Lena Varga | BA-02 |
| New (C7) | Is `Orders.InvoiceNumber` filled by the finance system, and is the invoice year the order year? | Julien Moreau | BA-02 |
| New (C14) | Is the order confirmation e-mail sent by something outside this repo? | Ahmed Benali | both |

Unverified items: **U1** Entra External ID pricing and limits, and .NET 10 support on Azure App Service, were not verified (the search failed). Treat as ASSUMPTION until the architect checks them. **U2** W1 comes from a search summary, not a full page read.

## 10. Assumptions table (ES-03)

| # | ASSUMPTION | Owner who can confirm |
|---|---|---|
| AS-01 | Document set filenames under `docs/product/`: `business-requirements.md`, `product-requirements.md`, `experiments.md`, `backlog.md`, `traceability.md`; releases in `docs/product/releases/` (ES-07 fixes folders, not names) | Lena Varga |
| AS-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting and get one story per track (G-03) | Lena Varga |
| AS-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange (X-01) | Ahmed Benali |
| AS-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| AS-05 | Delivered, Confirmed and Cancelled are manual staff actions (C2) | Order Desk team via Lena Varga |
| AS-06 | Experiment success thresholds in section 6 | Lena Varga, Ahmed Benali |
| AS-07 | Release target dates in section 7 | Marc Dubois, Lena Varga |
| AS-08 | Release names `azure-r<n>`, `dotnet-r<n>`; Git tags `product/azure-r<n>`, `product/dotnet-r<n>` (G-14) | Lena Varga |
| AS-09 | The cost model assumes SQL and private endpoints are the main spend (A3) | Ahmed Benali |
| AS-10 | Time zone behaviour on Azure may differ from the Lyon servers (C10) | Ahmed Benali |

## 11. Traceability starting points (ES-06)

| In-scope ID | Likely track stories (candidate) | Coverage note |
|---|---|---|
| BR-13 | azure: AZ-EN-08, AZ-EN-09, AZ-EN-13 (cutover) | azure-r2 |
| NFR-01 | azure: AZ-EN-05; dotnet: none (scope OPEN) | G-11 |
| NFR-03 | azure: AZ-EN-01; dotnet: portal data-residency story | one per track |
| NFR-05 | azure: AZ-EN-04; dotnet: DN-EN-05 | one per track |
| NFR-06 | azure: AZ-EN-06 | azure-r2, tested in r3 |
| BR-01..BR-06, BR-10, BR-12 | dotnet r2 (BR-10 staff view also r1) | all Must |
| BR-07, BR-08, BR-11 | dotnet r3 | Should |
| BR-09 | dotnet r4 | Could |
| NFR-02, NFR-07, NFR-08 | dotnet r2 | measurement basis open (G-11) |
| NFR-04 | dotnet: DN-EN-08 and customer sign-in; azure: platform plumbing if X-01/X-03 resolve that way | cross-cutting |
| C-01..C-06, SM-01..SM-04, SM-07 | Carried as constraints and measures in the BRD and PRD; SM-07 by azure-r3 | — |

Every BR and NFR in scope has at least one candidate home. No uncovered identifier was found; the author must list any that remain uncovered after story writing (ES-06).

## 12. Recommendation and alternatives

* **Recommended:** three Azure releases (foundation, cutover, decommission) and four .NET releases (modernised app, Must pilot, Should, Could) as in section 7, with one MVE per area (A1 for BA-01, B1 for BA-02) plus A3 and B2 as one-day desk exercises. Evidence: C2, C3, C5, C6, W1, C-01, DOC §8.
* **Alternative 1 (Azure):** one combined `azure-r1` containing foundation and cutover. Rejected as the default because the exchange and database unknowns need an early proof; acceptable if the product owner prefers fewer files.
* **Alternative 2 (.NET):** merge `dotnet-r1` into `dotnet-r2`. Rejected: it hides the largest technical enabler and its test baseline (C13, ES-18) and removes an early, small, approvable release.
* **Alternative 3 (.NET):** pull BR-11 (French/English) into `dotnet-r2`. Valid if the pilot customers need French; costs scope in the Must release. Decision for OQ-02.
* **Alternative 4 (Azure):** host the legacy .NET Framework app first and let the .NET track modernise later. Possible only if A4 shows config-only changes; it conflicts with CS-13, CS-04 (SSPI, Windows authentication) and ES-17, so it is not recommended without A4 evidence.

## 13. Risks

| Risk | Effect | Evidence |
|---|---|---|
| Exchange redesign misses a detail | Warehouse stops receiving orders | C3, C4 |
| Cutover slips beyond 30 June 2027 | Lease penalty, ESU cost continues | C-01, C-02 |
| Portal pilot has no Azure environment by Q2 2027 | Pilot cannot run | G-07, X-08 |
| Customer data exposed through unscoped controllers | Security breach | C5 |
| Cost above EUR 1,500/month | Constraint breached | C-04, A3 |
| BR-04 expectation vs nightly data | Customers distrust the portal; calls not reduced | G-01, C2, B1 |
| Tracks implicitly wait for each other (violates ES-31) | Both slip | X-01..X-12 |

## 14. Planning readiness and handoff

* **ready-with-gaps.** The Plan and Author roles can start. Missing evidence is recorded as `OPEN:` or `ASSUMPTION:` and does not block drafting.
* Author notes: (1) each cross-cutting NFR gets one story per track, and the traceability table shows both; (2) mark every item from section 4 that is not in knowledge-docs as ASSUMPTION; (3) write section 8 as `OPEN:` in every release file; (4) list BA-03 and its identifiers as out of scope; (5) no code, deployment or change to `src/`, `database/` or `infra/`.

## 15. Return summary for the Squad Coordinator

* **Research artifact:** `C:\demos\northwind-workshop\.copilot-tracking\research\2026-10-30\northwind-product-documents-research.md` (the only file written).
* **Lanes dispatched:** none. Reason: the full evidence base fit a direct read in the parent context.
* **Conflicts:** BR-04 vs CS-10 and C-03 (G-01); CS-12 vs `src/` (no mail code); BA-01 vs BA-02 wording on the Order Desk upgrade (G-04).
* **Gaps:** section 9, plus U1 and U2.
* **Planning readiness:** ready-with-gaps.
