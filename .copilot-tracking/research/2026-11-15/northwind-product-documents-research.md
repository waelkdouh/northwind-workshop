<!-- markdownlint-disable-file -->
# Task Research: Northwind product documents (BRD, PRD, MVEs, backlog, per-track releases, traceability)

| Field              | Value                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------|
| Date               | 2026-11-15 (date supplied by the caller; evidence root `.copilot-tracking/research/2026-11-15/`) |
| Researcher / agent | Squad Researcher (rpi-research skill); no lane worker dispatched (see Research Record)         |
| Output mode        | convergence (recommends release counts, themes and MVE targets; every choice is a proposal for the Lead and the product owner) |

Notation used in this file. Source ids are written verbatim from the knowledge documents: `BR-`, `NFR-`, `C-` (constraint, with hyphen), `SM-`, `P-`, `CS-`, `ES-`, `BA-`, `OQ-`, `G-` (intake gaps). Research evidence ids avoid the clash with constraint ids: codebase evidence is `C#1`, `C#2` ... and external evidence is `W#1` ... Research-added items are `T-` (tension), `X-` (cross-track dependency), `A-` (ASSUMPTION), `O-` (OPEN), `RG-` (research gap), `MVE-` (experiment candidate), `EN-`, `EA-`, `EP-` (enablers for .NET, Azure, Power Platform). These new id families are themselves an **ASSUMPTION (A-07)**, as the intake review recommended (G-07).

## Executive Summary

* Bottom line: the inputs support planning. No identifier in BR-01 to BR-19, NFR-01 to NFR-09, C-01 to C-08 or SM-01 to SM-07 is left without a business area (BA-01 to BA-03). What is uncovered is the problem list P-01 to P-06 and the `CS-` facts, which no BA lists (section a). Recommended shape: **Azure 3 releases, .NET 3 releases, Power Platform 0 releases** (all BA-03 items carry only `track-power-platform`).
* The decisive technical finding is that the **nightly StockPilot exchange cannot move to Azure as written**: it uses `xp_cmdshell`, `bcp`, `BULK INSERT` from a local `D:\` path and a SQL Server Agent job (C#9, CS-10), and Azure SQL Managed Instance does not support `xp_cmdshell` or file-share access (W#3). This is the riskiest assumption for BA-01 (MVE-01) and it interacts with the EUR 1,500 cap (C-04).
* The decisive finding for BA-03 is that **ES-36 (custom connector) conflicts with C-07 (standard connectors only)**, because custom connectors are premium (W#1, W#2; secondary sources), and the EUR 900 cap (C-08) is about EUR 17.31 per user for the 52 users. BA-03 is also blocked in practice by CS-27: Order Desk has no API and the API has no owner (G-01).
* The decisive finding for BA-02 is that **the legacy code is small and mostly portable (about 2,000 lines, 28 unit tests, 15 of them on pricing)** but the Web project is classic `System.Web` MVC 5 and must be re-hosted on ASP.NET Core (C#11). The riskiest assumption is about customers, not code: that they will self-serve reorders and trust a status that is refreshed once a night (MVE-02, BR-04, CS-10).
* Each track can deliver value without waiting (section b): Azure can finish landing zone, data tier, exchange redesign, storage, monitoring, DR and cost proof without any .NET change; .NET can build and test everything locally on macOS, Linux or Windows without Azure; Power Platform can design and validate against a stub connector contract (ES-33, ES-37). Hosting the modernised app, the pilot environment and the Order Desk API are the **OPEN** cross-track items.
* Research status: complete for the stated purpose. Confidence is high for facts read from the repository, medium for external claims (two are secondary sources) and low for anything about prices, volumes after 2026 and who owns what (all labelled ASSUMPTION or OPEN).

## What You May Not Know

1. **BR-04 is not only a nightly-batch problem.** The export procedure itself moves orders from Confirmed to Picking at 02:00 (so "Picking" means "sent to StockPilot", not "picking started"); the import moves Picking to Shipped; nothing in `database/` or `src/` sets Delivered except a staff drop-down in `OrdersController.ChangeStatus` (C#9, C#5, C#7). So Delivered, and therefore BR-07 (invoice only for delivered orders), depends on a manual staff step **ASSUMPTION A-03**.
2. **The portal's data isolation does not exist yet.** `OrdersController.Index(customerId)` trusts the URL, `Details(id)` and `Invoice(id)` never check the order belongs to the caller, and `ChangeStatus` has no role check (C#5). `OrderService.CopyOrder` is the only place that enforces ownership (C#6). BR-01 is therefore a real build item, not a configuration.
3. **The schema has no customer-user, e-mail address, language, warehouse-per-line, invoice-date or claims data** (C#10). BR-08, BR-09, BR-11, BR-17 and BR-19 each need new data that the documents do not describe (G-09).
4. **CS-12 says Order Desk sends confirmations through an SMTP relay, but no code in `src/` sends mail**; only configuration keys exist (C#12). Either mail is sent by something outside the repository or the statement is stale (RG-03).
5. **Time handling will change meaning in Azure.** The application stores local time (`DateTime.Now`, SQL `GETDATE()` in price-agreement validity), while audit rows use `GETUTCDATE()` (C#8). Azure services default to UTC (general platform behaviour, **ASSUMPTION A-24**), which moves the 24-month window, price-agreement day boundaries and order timestamps by one to two hours unless handled.
6. **Pilot size cannot reach SM-01.** 20 pilot customers are 1.7 % of the 1,150 active customers (section 8, CS-05); a 35 % portal share (SM-01) is only reachable after wider rollout, so "portal launch" must mean general availability (G-05, **A-04**).
7. **The lease end affects more than Order Desk.** `NWFS01` also holds `claims.xlsx` and `finance-import` (CS-24, CS-25); the finance system, domain controllers and the SFTP server are not said to be anywhere other than the Lyon data centre (CS-09, CS-04). Where they live after 30 June 2027 is undocumented (RG-01) and decides whether Windows Integrated Authentication (CS-04) and the finance CSV hand-off (CS-25) still work.

## Findings

### F1. Identifier coverage: nothing in scope is orphaned; the gaps are in problems, facts and shared items

All BR, NFR, C and SM identifiers appear in at least one BA row (business-case section 4); this confirms the intake review "checks that passed". Uncovered by any BA row: **P-01 to P-06** (the BA table lists no P ids; mapping below is **ASSUMPTION A-07**), and **all CS-01 to CS-28, ES, OQ** (not expected to be listed). Three identifiers are shared across two BAs and must be split by track (ES-30): NFR-03 (BA-01, BA-03), NFR-04 (BA-02, BA-03), NFR-05 (BA-01, BA-02).

* Questions: Q1
* Evidence state: evidence-backed finding
* Evidence: business-case section 3 and section 4 tables; intake review "Checks that passed".
* Confidence and limits: high; the P and CS mappings are inferences.

#### Inventory per business area (a)

| Item class | BA-01 Platform and data-centre exit (**Azure**, `track-azure`) | BA-02 Ordering and self-service (**.NET**, `track-dotnet`) | BA-03 Delivery claims (**Power Platform**, `track-power-platform`) |
|---|---|---|---|
| BR | BR-13 | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12 | BR-14, BR-15, BR-16, BR-17, BR-18, BR-19 |
| NFR | NFR-01, NFR-03, NFR-05, NFR-06 | NFR-02, NFR-04, NFR-05, NFR-07, NFR-08 | NFR-03, NFR-04, NFR-09 |
| C | C-01, C-02, C-03, C-04, C-06 | C-05 | C-07, C-08 |
| SM | SM-07 | SM-01, SM-02, SM-03, SM-04 | SM-05, SM-06 |
| P (A-07, inferred) | none stated; closest is the lease and out-of-support servers (C-01, C-02) | P-01, P-02, P-03, P-04, P-05 | P-06 |
| CS (A-07, inferred by what the fact constrains) | CS-06, CS-07, CS-08, CS-09, CS-10, CS-11 (hosting side), CS-12 (relay side), CS-19 (deploy side), CS-21, CS-22, CS-23; CS-13 to CS-17 (hosting and identity side) | CS-01 to CS-05, CS-04, CS-13 to CS-18, CS-20, CS-14 (code side), CS-27 (API owner gap) | CS-24, CS-25, CS-26, CS-27, CS-28 |
| Priority (business case) | Must: BR-13 | Must: BR-01 to BR-06, BR-10, BR-12. Should: BR-07, BR-08, BR-11. Could: BR-09 | Must: BR-14, BR-15, BR-16. Should: BR-17, BR-18. Could: BR-19 |
| NFR priority | not stated in any source; treated as Must for planning (**A-06**) | same | same |

In-scope total for ES-06: 19 BR + 9 NFR = 28 identifiers (BA-01, BA-02 and BA-03 all covered; none out of scope).

#### Coverage anomalies (identifiers that sit in one BA but are affected by another)

| Id | Sits in | Also affects | Why (source) |
|---|---|---|---|
| C-04 (EUR 1,500) | BA-01 | BA-02 portal, any Order Desk API | C-04 text covers "Order Desk and portal, production and one test environment". The portal is BA-02 work (T-03). |
| NFR-01 (availability) | BA-01 | BA-02 portal | Portal availability is not assigned to BA-02 (NFR-01 text names no application). |
| NFR-08 (7-year order audit) | BA-02 | BA-01 | Retention is a backup and retention-policy question once the database is in Azure (CS-07, C#8). |
| NFR-04 (identity) | BA-02, BA-03 | BA-01 | Staff move from Windows Integrated Authentication (CS-04) to Entra ID; BA-01 does not list NFR-04 (G-03). |
| NFR-03 (EU data) | BA-01, BA-03 | BA-02 | Portal hosting, customer identity tenant and mail service must stay in the EU; BA-02 does not list NFR-03 (business case: applies wherever relevant). |
| C-03 (StockPilot stays) | BA-01 | BA-02 | BR-04 status timeliness is bounded by C-03 and CS-10 (T-01). |
| C-06 (team knows .NET) | BA-01 | BA-03 | C-06 says nothing about Power Platform skills (G-08). |
| BR-10 (staff see channel) | BA-02 | none | Already visible in the staff screens today (`Index.cshtml`, `Details.cshtml`, `OrderChannel.Portal`) (C#5, C#7). |

### F2. The code is small, mostly portable, and has a precise list of blockers

Order Desk is about 2,000 lines of C#. The `Core` project holds domain, pricing, SQL access and logging; `Web` holds 3 controllers, 6 views and `Global.asax`; `Tests` holds 28 tests (15 pricing, 9 order service, 4 status rules) using in-memory fakes, so they need no database (C#4, C#11). All three projects are non-SDK `v4.8` with `packages.config`; `Web` uses `System.Web.Mvc` 5.2.9 and Windows authentication (C#1, C#11). That supports a "modernise in place" approach (ES-19) but the Web layer is a port to ASP.NET Core MVC (ES-14), not a retarget. The blockers CS-13 to CS-17 are confirmed and sized in the enabler table (section d). Pricing logic is pure and covered, so ES-18 and CS-20 parity is checkable on any operating system once MSTest v1 is replaced.

* Questions: Q2, Q4
* Evidence state: evidence-backed finding
* Evidence: C#1, C#2, C#3, C#4, C#11; CS-01, CS-02, CS-13 to CS-18, CS-20; ES-14, ES-15, ES-16, ES-18, ES-19.
* Confidence and limits: high for what the files contain; effort estimates are not made here (no sizing basis in the inputs).

### F3. The StockPilot exchange is the largest unplanned piece of Azure work

`database/003-stockpilot-exchange.sql` runs a SQL Server Agent job at 02:00 on `NWSQL01`, calls `xp_cmdshell` with `bcp ... queryout` to write `D:\Exchange\StockPilot\out\orders_<date>.csv`, marks confirmed orders as `Picking` (status 2), and imports `D:\Exchange\StockPilot\in\shipments.csv` with `BULK INSERT` to set `Shipped` (status 3). A Windows scheduled task synchronises that folder to the Antwerp SFTP server (C#9, CS-10). Per Microsoft documentation of the PaaS targets, `xp_cmdshell` is not supported on Managed Instance and Managed Instance cannot read Windows folders or file shares; `BULK INSERT` must read from Azure Blob Storage (W#3, W#4). SQL Server Agent on Azure SQL Database is not available (**ASSUMPTION A-30**, from general platform knowledge, not fetched). So the exchange must be rebuilt (for example a storage-based job) or the data tier must be a virtual machine, which ES-21 discourages. StockPilot itself must not change (C-03, business case section 6), so the CSV file contract (names, `;` separator, columns) is fixed (**A-27**). The import also writes an audit row for every row in the shipment file, even for orders that did not change status (C#9), which weakens NFR-08 accuracy; this is an existing defect to carry, not to fix silently (ES-19).

* Questions: Q3, Q5
* Evidence state: evidence-backed finding (code), partially supported claim (Azure feature support: W#3 is an official docs repository, W#4 a Microsoft Learn page; both reached by search snippet, not a full read)
* Evidence: C#9, W#3, W#4; CS-10, C-03, C-04, ES-21, ES-27.
* Confidence and limits: medium-high; no deployment or compatibility scan was run (ES-27 forbids deploying; a local compatibility assessment is the MVE-01 method).

### F4. Nothing in the current application is ready for customers

See "What You May Not Know" items 2 to 4. Customer scoping, a customer-user store, role checks, a stateless draft order, and a trusted channel value are all missing: `Draft(DraftOrderInput)` takes `Channel` from the form, so a user could post any channel, which breaks BR-10 integrity (C#5). The draft lives in `Session` (`InProc`, CS-16, C#1, C#5) so a second web instance or a slot swap in Azure loses it. Parts that **already work** and must be preserved: copy-order ownership check, price recalculation on submit, zero-quantity line removal, six statuses matching BR-04, `Portal` channel value, audit rows on create and status change, `OrderHistoryMonths=24` (BR-02) (C#1, C#6, C#7, C#8).

* Questions: Q4
* Evidence state: evidence-backed finding
* Evidence: C#1, C#5, C#6, C#7, C#8, C#10; BR-01, BR-02, BR-05, BR-06, BR-10, BR-12, NFR-08.
* Confidence and limits: high.

### F5. Power Platform feasibility rests on a licensing conflict and on a missing API

BA-03 stories need order lines (BR-14), but Order Desk has no API and sits on `NWSQL01` reachable only from Lyon (CS-27, CS-09). ES-36 forbids direct database access and requires a custom connector; custom connectors, the SQL Server connector, Dataverse and on-premises gateway use are premium connectors that need a standalone Power Apps or Power Automate licence, while Microsoft 365 plans include standard connectors only (W#1, W#2; **both secondary sources, medium confidence**; the primary Microsoft licensing guide should be checked by the owner, **O-02**). C-07 states standard connectors only; so either C-07 is relaxed, ES-36 is excepted by a decision record, or the cost fits C-08. Arithmetic from the inputs: EUR 900 divided by 52 users is **EUR 17.31 per user per month** (C-08). Premium per-user list prices are not in the inputs; a sum above EUR 17.31 per user would break C-08 (**A-22**, prices unverified). The finance hand-off is a CSV in `\\NWFS01\finance-import\` before 18:00 (CS-25); reaching an on-premises UNC path from a cloud flow needs a gateway, and the share's future location is unknown (RG-01). ES-34 requires a `NorthwindClaims` solution with tables (Dataverse is the usual home); whether Dataverse is premium here is part of O-02. Environments do not exist: only the default environment, 23 personal apps and no DLP (CS-26), so ES-35 is a build item, not an assumption.

* Questions: Q6
* Evidence state: partially supported claim (licensing), evidence-backed finding (the missing API and environments)
* Evidence: CS-24 to CS-28, C-07, C-08, ES-33 to ES-37, W#1, W#2.
* Confidence and limits: medium. Counter-evidence: SharePoint and Outlook connectors are standard, so a design with no custom connector exists (for example a nightly order-line snapshot to a SharePoint list), but it would depart from ES-36 and needs a decision record (alternative B2, section Recommendation).

### F6. The two business-case dates and the lease date collide in Q2 2027

C-01 30 June 2027 is a Wednesday; the last Sunday maintenance windows (CS-21, Sunday 06:00 to 12:00) are 6, 13, 20 and 27 June 2027 (computed). The portal pilot is Q2 2027 (section 8), so the portal pilot runs while the database is moving. C-05 says the portal reuses Order Desk as the single order source, so the pilot reads the same database that Azure is migrating (T-09). Claims pilot Q1 2027 has no team, no API, no environments and no licence decision (G-08, CS-26, CS-27, O-02), so it cannot be committed (A-25). Business-case status is "Approved for discovery. Not yet approved for build", so a December 2026 build start also needs approval (A-01, O-21).

* Questions: Q5
* Evidence state: evidence-backed finding (dates and weekdays), conjecture (pilot-versus-cutover sequencing risk)
* Evidence: C-01, CS-21, section 8, business-case header status, G-08.
* Confidence and limits: high for dates; the sequencing risk depends on where the pilot database sits (O-23).

## Recommendation and Alternatives

* Recommendation: **Azure 3 releases, .NET 3 releases, Power Platform no release.** Themes and dates in section (e). Per-track riskiest assumptions in section (c). These are inputs to the Lead and PRD, not commitments (G-06, G-11).
* Rationale: C-01 is a hard date, so Azure needs an early foundation release that does not wait for anyone, a middle release that lands the pilot environment before Q2 2027, and a final release dedicated to cutover and recovery proof (CS-21, CS-23, NFR-06). .NET needs an enabler-and-parity release first because every portal story needs `net10.0`, configuration, logging and a stateless draft (CS-13 to CS-17, ES-14 to ES-17), then a Must-only portal pilot release for Q2 2027, then the Should and Could set after pilot feedback.
* What could change this result: a decision on O-03 (rehost the .NET Framework app versus wait for `net10.0`), O-07 (a BA-03 team and date), O-01 (API owner), or an approver naming that adds or merges releases.

| Option | Benefits | Costs and risks | Evidence | Disposition |
|---|---|---|---|---|
| A1: Azure 3 releases (foundation and data, pilot environment and runtime, cutover and recovery) | Matches C-01 and the Q2 portal pilot; each release is reviewable without .NET | Docs, IaC and runbooks only (ES-27), so "value" is a validated, reviewed design | CS-21, CS-23, C-01, ES-27 | Selected |
| A2: Azure 2 releases | Fewer approvals | Cutover rehearsal and DR proof squeezed into one release before a hard date | CS-23, NFR-06 | Rejected |
| A3: Azure rehosts the unchanged .NET Framework app on a Windows VM | Meets C-01 even if .NET slips; no code change | Needs domain join or Entra Domain Services for Windows authentication (CS-04), keeps Windows administration, conflicts with ES-21 preference; stays a **contingency** | CS-04, ES-21, C-02 | Deferred contingency (O-03) |
| B1: .NET 3 releases (parity and enablers; portal pilot Musts; Should and Could) | Enablers precede features (G-10); pilot scope limited to Musts | Release 1 has little customer-visible value | CS-13 to CS-18, section 8 | Selected |
| B2: .NET single release for everything | One approval | Misses the Q2 pilot or ships untested enablers | section 8 | Rejected |
| C1: BA-03 no release now; items carry `track-power-platform` only | Matches intake amendment 2 and ES-31 | Q1 2027 pilot cannot be committed (O-07) | ES-31, G-08, intake review | Selected |
| C2: BA-03 snapshot design (order lines copied to a SharePoint list; no custom connector) | Fits C-07 and C-08 | Departs from ES-36, stale order data, needs a decision record | ES-36, C-07, W#1 | Viable alternative to record in the PRD as OPEN |
| C3: BA-03 premium licences for 52 users | Meets ES-36 | Likely above EUR 17.31 per user (C-08); prices unverified | C-08, W#1, W#2 | Viable, needs O-02 |

## (b) Cross-track dependency map and how each track keeps delivering

Direction wording: "A needs B" means track A needs something from track B. Every row is recorded as **OPEN:** in the release files of the needing track (ES-31); none is a wait.

| Id | Dependency | Needs | From | Source | Can the needing track still deliver without waiting? | Owner to confirm |
|---|---|---|---|---|---|---|
| X-01 | A hosting target for the modernised app (App Service or equivalent) and a pilot test environment | .NET needs Azure | Azure | C-01, ES-23, section 8 | Yes: .NET builds and tests locally (no Azure) with user secrets or environment variables (ES-17), in-memory tests (C#4) and a local SQL Server for the schema scripts 001 and 002; pilot hosting is OPEN | Ahmed Benali |
| X-02 | A `net10.0` app that honours a documented configuration and identity contract (environment variables, managed identity, no secrets) | Azure needs .NET | .NET | CS-13, CS-17, ES-15, ES-17, NFR-05 | Yes: Azure writes IaC parameterised by the contract and validates it with `az bicep build` (ES-27); app deployment stays OPEN | Ahmed Benali |
| X-03 | Database authentication: `Integrated Security=SSPI` (CS-13) becomes Entra or managed identity for the database | Both | Both | CS-13, ES-25, NFR-05, C#1 | Partly: Azure provisions the data tier and identities; .NET builds the connection logic (`Microsoft.Data.SqlClient`) against a local SQL Server | Ahmed Benali |
| X-04 | Staff sign-in moves from Windows Integrated Authentication to Entra ID (and customer sign-in per OQ-01) | .NET needs Azure/IT (app registrations, tenant); Azure has no code to do | Azure or IT | CS-04, NFR-04, OQ-01, G-03 | Yes: .NET uses a provider-neutral sign-in and a test identity (A-10) | Ahmed Benali |
| X-05 | StockPilot exchange redesign for a PaaS data tier; file contract fixed (C-03) | .NET needs Azure | Azure | C#9, CS-10, C-03, W#3 | Yes: Azure owns it end to end (database scripts and storage); .NET only reads the status results | Ahmed Benali |
| X-06 | Order status freshness shown in the portal (BR-04) is bounded by the exchange cadence | .NET needs Azure and StockPilot | Azure, StockPilot (unchanged) | BR-04, CS-10, C-03, T-01 | Yes: .NET shows an "as of" time and the six statuses (A-03) | Lena Varga |
| X-07 | `InProc` session draft (CS-16) must become stateless or distributed before scale-out or slot swaps | Azure needs .NET | .NET | CS-16, C#5 | Yes: Azure starts with a single instance (as today, CS-06) | Ahmed Benali |
| X-08 | Logging: `ILogger` (ES-16) to Application Insights and Log Analytics (ES-26); replaces Event Log and ping checks | .NET needs Azure (workspace, connection) | Azure | CS-15, CS-22, ES-26 | Yes: .NET logs to console and `ILogger`; Azure designs the workspace and alerts | Ahmed Benali |
| X-09 | Invoice files: UNC path (CS-14) to Azure storage; finance system keeps writing PDFs (CS-11) | Both | Both | CS-08, CS-11, CS-14, C#13 | Partly: .NET abstracts the invoice store with a local-folder provider; Azure designs storage and file sync; where the finance system writes after the lease is OPEN (RG-01) | Julien Moreau, Ahmed Benali |
| X-10 | Outbound mail: on-premises relay without authentication (CS-12) is not available after the lease; no send code exists (C#12) | Both | Both | CS-12, BR-09, RG-03 | Yes: .NET uses a mail abstraction and a local mail catcher; Azure designs the mail service | Ahmed Benali |
| X-11 | Build and test pipeline (.NET) and deployment pipeline and IaC (Azure) | Both | Both | CS-18, CS-19, ES-22, ES-27 | Yes: each writes its own pipeline definition; tool is OPEN (O-19) | Ahmed Benali |
| X-12 | Shared monthly cap C-04 covers Order Desk and portal in production and one test environment | Azure needs .NET sizing inputs | .NET | C-04, NFR-02, G-05 | Yes: Azure sizes from today's load (CS-03, CS-06: average CPU 18 %, peak 55 %, 60 peak users) and refines later | Ahmed Benali |
| X-13 | Internet-facing entry for customers versus private endpoints for data services (ES-25) | .NET needs Azure | Azure | ES-25, BR-01, NFR-03 | Yes: .NET builds the portal; ingress design is Azure's | Ahmed Benali |
| X-14 | One solution and three projects (ES-13) versus adding a portal area and an API: a decision record is required for any new project | Both | .NET (decision), Azure (hosting shape) | ES-13, O-20 | Yes: decision record is a .NET deliverable | Ahmed Benali |
| X-15 | Retention of the 7-year audit trail once the database is in Azure (backup and long-term retention settings) | .NET needs Azure | Azure | NFR-08, CS-07 | Yes: .NET defines audit content; Azure sets retention (A-31, retention feature limits not verified) | Ahmed Benali |
| X-20 | Order Desk API (read orders and lines) for the custom connector | Power Platform needs .NET (assumed) | .NET | CS-27, ES-36, G-01 | Yes: BA-03 designs against a stub OpenAPI 2.0 contract and mock (ES-33, ES-37); .NET can deliver the API with no consumer | Ahmed Benali |
| X-21 | Order data contract for claims: order number, lines, quantities, prices, customer, warehouse | Power Platform needs .NET | .NET | BR-14, BR-17, C#10, A-18 | Yes: contract is documented and stubbed | Lena Varga, Pieter Janssens |
| X-22 | The API endpoint must be reachable from Power Platform while data services use private endpoints (ES-25) | Power Platform needs Azure | Azure | ES-25, ES-36, T-14 | Yes: design assumes an Entra-protected endpoint; network path is OPEN | Ahmed Benali |
| X-23 | Connector authentication (Entra app registration, OAuth) | Power Platform needs Azure/IT | Azure or IT | ES-36, NFR-04, CS-28 | Yes: stub uses a placeholder security definition | Ahmed Benali |
| X-24 | Finance CSV drop to `\\NWFS01\finance-import\` before 18:00 (CS-25); share location after the lease | Power Platform needs Azure | Azure (storage and network) | CS-25, RG-01, C-01 | Yes: BA-03 designs the CSV format and a gateway-free alternative as options | Julien Moreau, Ahmed Benali |
| X-25 | Warehouse per order line for BR-17 | Power Platform needs .NET and StockPilot data | .NET | BR-17, C#10, A-18 | Yes: design the supervisor view with the cause field; warehouse source OPEN | Pieter Janssens |
| X-26 | Customer e-mail address for BR-19 and the portal's BR-09 | Both | .NET | C#10, BR-09, BR-19 | Yes: BR-19 is Could; list as OPEN | Lena Varga |
| X-27 | Environments, DLP and licensing: no Azure involvement; admin of Microsoft 365 tenant | Power Platform | IT | CS-26, ES-35, C-07, C-08 | Yes: design only (ES-37) | Ahmed Benali |

### What each track can deliver first, independent of the others

* **Azure (BA-01), no .NET code change required.** Landing zone and test and production foundations as Bicep with Azure Verified Modules, naming, tags, France Central (ES-20, ES-22 to ES-24, CS-09); hybrid connectivity design (CS-09); Key Vault, managed identities and private endpoints (ES-25); observability design to replace ping checks (CS-22, ES-26); data-tier decision record and migration plan for the 48 GB database growing 1 GB a month (CS-07, C-02, SM-07); StockPilot exchange redesign with the CSV contract unchanged (C#9, C-03); invoice storage for 120 GB growing 2 GB a month (CS-08); backup, recovery design and the first recovery test plan (CS-07, CS-23, NFR-06); cost model against C-04; cutover and rollback runbook for the Sunday window (CS-21, BR-13). All validated locally, nothing applied (ES-27).
* **.NET (BA-02), no Azure required.** Convert to SDK-style `net10.0`, replace MSTest v1, configuration, logging, session, invoice and time handling, port the Web project, then build the portal against a local SQL Server container or instance, in-memory fakes, a test identity and a local mail catcher (ES-14 to ES-18; A-10). The unit tests already run without a database (C#4). The only Azure-dependent activities are the pilot deployment and the managed-identity connection test (X-01, X-03).
* **Power Platform (BA-03), no Order Desk API and no environment required.** Solution design, Dataverse (or alternative) model, flows, approval rules (BR-15 no self-approval), environments and licensing options under `docs/power-platform/`, a stub connector definition (OpenAPI 2.0) under `powerplatform/`, validated locally (ES-32, ES-33, ES-37). Nothing is created in a tenant.

## (c) Riskiest assumption per business area (MVE targets)

An MVE here is local, prototype or paper-based because nothing may be deployed or changed (ES-27, ES-37; A-09). Method detail is for the experiment-design stage; this section fixes the target and the evidence.

| MVE | BA | Riskiest assumption (candidate) | Evidence for | Evidence against | Why this over the alternatives |
|---|---|---|---|---|---|
| MVE-01 | BA-01 | **A PaaS data tier can host `NorthwindOrders` and keep the nightly StockPilot exchange working (CSV contract unchanged) inside EUR 1,500 a month for production plus one test environment, with RPO 1 hour and RTO 4 hours** (C-01, C-03, C-04, NFR-06, CS-07, CS-10) | Database is only 48 GB (CS-07); load is light (average CPU 18 %, 60 peak users, CS-03, CS-06); exchange logic is about 40 lines in two procedures (C#9); 15-minute log backups already exist (CS-07) | The exchange depends on `xp_cmdshell`, `bcp`, `BULK INSERT` from `D:\`, Agent (C#9); Managed Instance does not support `xp_cmdshell` or file shares (W#3); Managed Instance is likely the most expensive compatible tier (price not in inputs, **A-32**); private endpoints on every data service (ES-25) add running cost; no recovery test has ever been done (CS-23) | It combines the hard date (C-01), the shared cap (C-04, T-03) and the only fully unmapped integration. Alternatives ranked lower: migration within a 6-hour window (BR-13, CS-21; likely feasible by log-based restore from the existing backups, **A-33**) and rehosting without code changes (O-03; a contingency, not the plan). |
| MVE-02 | BA-02 | **Customer users will complete a reorder themselves (copy a previous order, change quantities, submit) and will trust the order status shown, even though Picking and Shipped are refreshed only once a night, enough to stop phoning** (BR-04, BR-05, SM-01, SM-02, P-03, P-04, CS-10) | 70 % of orders repeat a previous order (P-04); 410 status calls a week are 35 % of inbound calls (P-03); copy and reprice logic already exists and is tested (C#6) | No customer research is cited; 20 pilot customers of 1,150 (section 8, CS-05); status is stale by design (CS-10, C#9); Delivered is set by hand (C#5, A-03); SM-01 35 % is high for independent grocers and restaurants (no evidence either way) | Technology risk for BA-02 is low (F2); the unproven part is behaviour. Alternatives ranked lower: identity provider choice (OQ-01, A-10 makes it provider-neutral) and WCAG 2.2 AA (NFR-07, standard practice). |
| MVE-03 | BA-03 | **A claims solution can meet ES-36 (reach order lines only through a custom connector) and ES-34 and ES-35 while staying inside C-07 and EUR 900 a month for about 52 users, and can hand credit-note requests to a finance system with no API through a CSV file** (C-07, C-08, ES-36, CS-25, CS-27) | The Antwerp supervisors already have Entra accounts with Microsoft 365 E3 (CS-28); claims capture, two-step approval and photos are ordinary Power Apps and Power Automate scenarios (**A-34**, general knowledge); the CSV hand-off is simple (CS-25) | Custom connector, SQL Server, Dataverse and gateway are premium (W#1, W#2); EUR 17.31 per user per month (C-08); no API (CS-27); on-premises share access after the lease is unknown (RG-01); only the default environment exists (CS-26) | A failure here blocks every BA-03 story, while the usability claim (record a claim in under 2 minutes, BR-14) is a lower-risk, lower-priority test that can come after. |

Quick-win criteria suggestions for the experiment stage, all labelled **ASSUMPTION A-35**: MVE-01 passes when a compatibility inventory of `database/*.sql` finds no unsupported feature without a documented replacement and an indicative monthly estimate is at or below 80 % of C-04 (leaving headroom for the portal, X-12); MVE-02 passes when at least a stated share of 5 to 8 test customers finish a reorder unaided and say they would use it instead of phoning (numbers to be set by Lena Varga); MVE-03 passes when at least one design satisfies ES-36 and C-08 with a stated per-user cost, or the decision to relax C-07 or C-08 is recorded.

## (d) Enabler work each track needs before its features

Enablers have no BR or NFR to cite (G-10); they cite CS, ES, C and the NFR they protect, and appear in a separate section of the traceability table.

### .NET enablers (`track-dotnet`)

| Id | Enabler | Why now (source) | Must precede |
|---|---|---|---|
| EN-01 | Convert `Core`, `Web`, `Tests` to SDK-style projects on `net10.0`; keep one solution and three projects; `System.Data.SqlClient` to `Microsoft.Data.SqlClient` | CS-02, CS-01, ES-13, ES-14, ES-19, C#11 | All portal stories |
| EN-02 | Replace MSTest v1 (GAC, Visual Studio only) so `dotnet test src/Northwind.OrderDesk.sln` runs on Windows, macOS, Linux; keep all 28 test assertions, pricing assertions unweakened | CS-18, CS-20, ES-18, C#4 | EN-01 sign-off; BR-12 |
| EN-03 | Replace `ConfigurationManager` (three call sites: `SqlOrderDeskStore`, `InvoiceStore`, `OrdersController.Index`) with `Microsoft.Extensions.Configuration` and options | CS-17, ES-15, C#2 | X-02 contract |
| EN-04 | Remove Integrated Security and server name from configuration; support user secrets and environment variables locally, managed identity in Azure | CS-13, NFR-05, ES-17, ES-25, C#1 | Any hosted environment |
| EN-05 | Replace `EventLogErrorLogger` and `IErrorLogger` with `ILogger<T>`; keep `RecordingLogger`-style test coverage | CS-15, ES-16, C#3 | Observability (X-08) |
| EN-06 | Replace `InProc` session draft with a stateless or distributed design | CS-16, C#5 | BR-05 in the portal; X-07 |
| EN-07 | Abstract the invoice store (UNC path to a provider model) and resolve the year folder rule (the code uses the order year, CS-11 says invoice year) | CS-14, CS-11, C#13, G-09, A-15 | BR-07 |
| EN-08 | Port `Web` to ASP.NET Core MVC; replace Windows Integrated Authentication with Entra ID OpenID Connect for staff | CS-04, NFR-04, C#11 | BR-01 |
| EN-09 | Automated build and test pipeline (today a developer publishes from Visual Studio) | CS-19, CS-18 | Any release tag |
| EN-10 | Make time handling explicit (one clock, UTC storage or documented local rule) and add tests; keep price-agreement validity behaviour | C#8, CS-20, A-24 | BR-02, BR-12 |
| EN-11 | Authorisation foundation: customer scoping in `GetOrder`, order list and invoice; role checks on `ChangeStatus`; channel set by the server | C#5, BR-01, BR-10 | BR-01 to BR-06 |
| EN-12 | Local test data with orders (sample data has customers, products and two price agreements, but no orders) and a local database recipe | C#10, ES-27 | All local testing and MVE-02 |
| EN-13 | Decision record: portal as an area of `Web` or a new project; API project or not | ES-13, O-20 | BR-01, O-01 |
| EN-14 | Order Desk API contract (read-only orders and lines) as OpenAPI 2.0 document; implementation is OPEN | CS-27, ES-36, G-01 | BA-03 connector |

### Azure enablers (`track-azure`)

| Id | Enabler | Why now (source) | Must precede |
|---|---|---|---|
| EA-01 | Foundation IaC: naming, tags, region, Bicep with Verified Modules, one `main.bicep` per environment, `.bicepparam` files | CS-09 (no Azure presence), ES-20 to ES-24 | Everything |
| EA-02 | Hybrid connectivity design (existing VPN to Antwerp, Lyon to Azure during migration, post-lease path) | CS-09, C-01, RG-01 | Data and exchange moves |
| EA-03 | Secrets and identity: Key Vault, managed identities, private endpoints, no passwords | CS-13, NFR-05, ES-17, ES-25 | Any app hosting |
| EA-04 | Observability: one Log Analytics workspace per environment, Application Insights, alerts replacing ping checks and a weekly Event Log look | CS-15, CS-22, ES-26, NFR-01 | Cutover readiness |
| EA-05 | Data-tier decision record (PaaS option versus VM) and migration approach within the Sunday window | CS-07, CS-21, C-02, ES-21, F3 | EA-06, EA-08 |
| EA-06 | StockPilot exchange redesign, CSV contract unchanged, no `xp_cmdshell` | C#9, CS-10, C-03 | Cutover |
| EA-07 | Invoice storage and synchronisation design (120 GB, plus 2 GB a month) | CS-08, CS-11, CS-14 | BR-07 hosting |
| EA-08 | Backup, long-term retention and recovery design; first recovery test plan | CS-07, CS-23, NFR-06, NFR-08 | Cutover |
| EA-09 | Cost model against C-04 including the portal and the API host | C-04, X-12 | All sizing |
| EA-10 | Test environment `tst` definition so a pilot can run | ES-23, section 8 | Portal pilot |
| EA-11 | Deployment pipeline and IaC validation (local `az bicep build`, no apply) | CS-19, ES-22, ES-27 | Release tags |
| EA-12 | Outbound mail service design replacing the on-premises relay | CS-12, A-29 | BR-09 |
| EA-13 | Cutover, rollback and decommission runbooks (Sunday window; stop paying for Extended Security Updates) | CS-21, BR-13, C-02, SM-07 | C-01 |

### Power Platform enablers (`track-power-platform`)

| Id | Enabler | Why now (source) | Must precede |
|---|---|---|---|
| EP-01 | Environment and DLP design: development, test and production in Europe, nothing in the default environment (23 personal apps exist) | CS-26, ES-35, NFR-03 | All BA-03 features |
| EP-02 | Solution `NorthwindClaims`, prefix `nw`, managed in test and production | ES-34 | All BA-03 features |
| EP-03 | Stub custom connector contract (OpenAPI 2.0) with connection and environment variables | ES-36, ES-33, CS-27 | BR-14 |
| EP-04 | Licensing and cost decision (premium versus standard, Dataverse or alternative) | C-07, C-08, W#1, W#2, O-02 | Data model |
| EP-05 | Finance CSV contract and drop-location design | CS-25, RG-01 | BR-16 |
| EP-06 | Identity and roles (recorder, approver, supervisor; no self-approval) | CS-28, NFR-04, BR-15 | BR-15 |

## (e) Recommended releases, themes and dates

Dates are **ASSUMPTION A-01** targets for the approval of each release (build start December 2026 after build approval, O-21). A release in the Azure and Power Platform tracks means a reviewed, locally validated design set, not a deployment (ES-27, ES-37).

### Azure: 3 releases (`azure-r1` to `azure-r3`, Git tags `product/azure-r1` to `product/azure-r3`)

| Release | Target approval | Theme | Main content (priority basis) | Covers | Leaves out |
|---|---|---|---|---|---|
| azure-r1 | end January 2027 | Foundation, data platform decision and cost proof | EA-01, EA-02, EA-03, EA-05, EA-09, EA-11; MVE-01 result; data-tier decision record | NFR-03, NFR-05 (Azure side), C-04, C-02, C-06 (design), part of C-01 | exchange build, hosting, DR test |
| azure-r2 | end March 2027 | Pilot environment and Order Desk runtime in Azure, exchange and storage | EA-04, EA-06, EA-07, EA-08 (design), EA-10, EA-12; hosting IaC runtime-agnostic (X-02) so portal pilot can start in Q2 2027 | NFR-01 (design and alerting), NFR-03, NFR-06 (design), C-03, C-04 | cutover rehearsal |
| azure-r3 | end May 2027 | Cutover and recovery proof | EA-13, recovery test evidence plan, rehearsals in Sunday windows (6 and 13 June 2027 keep 20 and 27 June as live and fallback windows), decommission plan, ESU stop | BR-13, NFR-06, NFR-01, SM-07, C-01, C-02 | optimisation after the lease (unplanned items) |

### .NET: 3 releases (`dotnet-r1` to `dotnet-r3`, tags `product/dotnet-r1` to `product/dotnet-r3`)

| Release | Target approval | Theme | Main content (priority basis) | Covers | Leaves out |
|---|---|---|---|---|---|
| dotnet-r1 | end February 2027 | Modernised Order Desk with behavioural parity | EN-01 to EN-06, EN-08 to EN-10, EN-12 to EN-14; staff Entra sign-in; BR-10 and BR-12 verified as parity | NFR-05, NFR-04 (staff), BR-10, BR-12 (parity), CS-20 parity | customer-facing features |
| dotnet-r2 | end April 2027 | Portal pilot (Musts) for 20 customers | EN-07 (design), EN-11; BR-01 to BR-06, BR-10 (Portal value), BR-12, BR-11 French and English, customer onboarding by staff before BR-08 (A-19) | BR-01 to BR-06, BR-10, BR-11 (FR, EN), BR-12, NFR-02, NFR-04 (customers), NFR-07, NFR-08 | invoices, user administration, e-mail, Dutch, API implementation |
| dotnet-r3 | end September 2027 (ASSUMPTION: after pilot feedback; measurement of SM-01 to SM-04 six months after launch, A-04) | Complete portal and the Order Desk API | BR-07, BR-08 (scope per OQ-03), BR-09 (status freshness per T-01), BR-11 Dutch (OQ-02), Order Desk API implementation if O-01 assigns it | BR-07, BR-08, BR-09, BR-11 (NL), SM-01 to SM-04 instrumentation | BA-03 stories |

### Power Platform: 0 releases

BA-03 is fully documented (all of BR-14 to BR-19, NFR-03, NFR-04, NFR-09) and tagged `track-power-platform` only, with a Release column showing "unplanned" (ES-31, intake amendments 2 and 3). Suggested priority bands, **not release tags** (A-36): P1 BR-14, BR-15, BR-16, NFR-09 with EP-01 to EP-06; P2 BR-17, BR-18; P3 BR-19; OQ-05 spreadsheet migration as a separate unplanned item. Every cross-track need is **OPEN:** (X-20 to X-27). The Q1 2027 claims pilot cannot be committed until O-07 and O-01 are answered (G-08, A-25).

### Release-to-identifier cover (proposed, for the traceability table)

| Id | Priority | Proposed release | Note |
|---|---|---|---|
| BR-01 | Must | dotnet-r2 | needs EN-11, EN-08 |
| BR-02 | Must | dotnet-r2 | 24 months is `OrderHistoryMonths` (C#1) |
| BR-03 | Must | dotnet-r2 | |
| BR-04 | Must | dotnet-r2 | freshness AC per A-03 |
| BR-05 | Must | dotnet-r2 | needs EN-06 |
| BR-06 | Must | dotnet-r2 | `Received` and `Portal` already supported (C#6, C#7) |
| BR-07 | Should | dotnet-r3 | needs A-15, EN-07 |
| BR-08 | Should | dotnet-r3 | OQ-03 |
| BR-09 | Could | dotnet-r3 | freshness; no mail code exists (C#12) |
| BR-10 | Must | dotnet-r1 (parity) and dotnet-r2 (Portal value) | one story per release is not allowed (ES-31: one release per item), so split into two stories |
| BR-11 | Should | dotnet-r2 (FR, EN), dotnet-r3 (NL) | OQ-02; split into two stories |
| BR-12 | Must | dotnet-r1 (parity) and dotnet-r2 (customer prices) | split into two stories |
| BR-13 | Must | azure-r3 | design in r1 and r2 |
| BR-14 to BR-19 | Must, Should, Could | unplanned | `track-power-platform` only |
| NFR-01 | n/a | azure-r2 and azure-r3 | monitoring then proof |
| NFR-02 | n/a | dotnet-r2 | measure point A-05 |
| NFR-03 | n/a | azure-r1 (Azure), unplanned (BA-03) | split per track |
| NFR-04 | n/a | dotnet-r1 (staff), dotnet-r2 (customers), unplanned (BA-03) | split per track |
| NFR-05 | n/a | azure-r1 (Azure), dotnet-r1 (.NET) | split per track |
| NFR-06 | n/a | azure-r3 | |
| NFR-07 | n/a | dotnet-r2 | |
| NFR-08 | n/a | dotnet-r2 (content), azure-r2 (retention design) | split per track |
| NFR-09 | n/a | unplanned | `track-power-platform` only |

## (f) Conflicts and tensions between inputs

| Id | Tension | Sources | Effect | Proposed handling |
|---|---|---|---|---|
| T-01 | BR-04 says status is "always up to date"; Picking and Shipped change once a night, Picking really means "exported", Delivered is manual; StockPilot is unchanged | BR-04, BR-09, CS-10, C-03, C#9, C#5 | BR-04 cannot be met literally | AC defines freshness (A-03); Azure may shorten the cadence only if StockPilot's pick-up can change without changing StockPilot (O-16) |
| T-02 | C-07 allows standard connectors only; ES-36 requires a custom connector (premium); ES-34 tables imply Dataverse; ES-35 needs environments that do not exist | C-07, ES-34, ES-35, ES-36, CS-26, W#1, W#2 | BA-03 as written is not feasible without a licence decision | O-02; PRD lists B2 and B3 alternatives |
| T-03 | C-04 is a shared cap held only by BA-01; portal (BA-02) and any API host consume it; C-08 is a separate cap; ES-25 private endpoints add cost | C-04, C-08, ES-25, X-12 | Nobody owns the whole cap | Azure owns the cost model; .NET supplies sizing inputs (A-02) |
| T-04 | "A track never waits" versus an app that needs code change to run in Azure | ES-31, BA-01, CS-13 to CS-17, G-03 | azure-r1 cannot assume a deployable app | Release 1 and 2 are independent of .NET code; runtime hosting uses a documented contract (X-02); A3 stays contingency |
| T-05 | BR-13 and C-01 versus an exchange built on `xp_cmdshell` and local files; ES-21 prefers PaaS | BR-13, C-01, C#9, W#3, ES-21 | Exchange rebuild is hidden work | EA-06, MVE-01 |
| T-06 | SM-01 35 % six months after "portal launch" versus a 20-customer pilot | SM-01, section 8, CS-05, G-05 | Target unreachable if launch means the pilot | A-04: launch means general availability; confirm with O-05 |
| T-07 | Claims pilot Q1 2027 versus no team, API, environments or licence decision | section 8, G-08, CS-26, CS-27, O-02 | Date cannot be committed | A-25, O-07 |
| T-08 | Portal pilot Q2 2027 and C-05 (single order source) versus database migration before 30 June 2027 | section 8, C-05, C-01 | Pilot may read a database that is mid-move | O-23: decide pilot database location; sequence pilot after azure-r2 data readiness |
| T-09 | C-06 lists .NET and SQL skills only; C-07 makes Power Platform the approved platform; Azure and Bicep skills not stated | C-06, C-07, ES-22, G-08 | Capacity assumption missing for Azure and Power Platform | O-07 |
| T-10 | ES-13 (one solution, three projects) and ES-19 (modernise in place) versus a portal, an API and a Web re-platform | ES-13, ES-19, ES-14, C#11 | New projects need a decision record | EN-13 |
| T-11 | ES-25 private endpoints versus customers and Power Platform needing a reachable endpoint | ES-25, X-13, X-22 | Ingress design missing | O-03, EA-02 |
| T-12 | CS-12 says mail is sent; `src/` sends none; settings point to an on-premises relay (port 25, no authentication) | CS-12, C#12, BR-09 | Unknown owner of confirmations | RG-03 |
| T-13 | NFR-08 asks for who, what, when, channel; audit rows record an action text, user, time and channel only on creation; shipment import writes audit rows for unchanged orders | NFR-08, C#8, C#9 | Audit accuracy and completeness unproven | Story AC; defect recorded, not fixed silently (ES-19) |
| T-14 | NFR-06 RPO 1 hour is met by 15-minute log backups on paper, but recovery has never been tested | NFR-06, CS-07, CS-23 | Claim unproven | azure-r3 recovery proof |
| T-15 | NFR-03 and NFR-04 apply "wherever relevant" but BA-02 does not list NFR-03 and BA-01 does not list NFR-04 | business-case section 4, G-03 | Risk of an uncovered obligation | Split per ES-30 and list both in the traceability table |
| T-16 | Business case "not yet approved for build" versus a December 2026 start | business-case header, section 8 | Date assumption | A-01, O-21 |
| T-17 | NFR-01 uses CET only; business hours cross the summer time change | NFR-01, G-05 | Ambiguity | A-05 |

## Scope and Questions

* Goal: provide planning-ready evidence so the Lead, analyst, experimenter and product owner can produce the BRD, PRD, three MVEs, backlog, releases and traceability without re-reading the sources.
* Audience and use: Squad Coordinator and Squad Lead (plan), BRD and PRD authors, MVE designer, product owner.
* In scope: `knowledge-docs/*.md`, intake review, `src/`, `database/`, standards ES-01 to ES-39; two external checks (Power Platform licensing, Azure SQL feature support).
* Out of scope: writing product documents, sizing effort, prices, any deployment or tenant change (ES-27, ES-37).
* Decision and evidence criteria: every statement cites a source id or is labelled ASSUMPTION or OPEN (ES-02, ES-03, ES-04).
* Requested output: this artifact, in the structure the caller specified, items (a) to (g).

| ID | Question | Source | Status |
|---|---|---|---|
| Q1 | Which BR, NFR, C, SM, CS and P ids belong to each BA, and which are uncovered? | caller (a) | answered (F1) |
| Q2 | What in `src/` and `database/` affects sizing and sequencing? | caller | answered (F2, F3, F4) |
| Q3 | What can each track deliver without waiting? | caller (b) | answered (section b) |
| Q4 | What is the riskiest assumption per BA, with evidence for and against? | caller (c) | answered (section c) |
| Q5 | What enabler work comes first (CS-13 to CS-23)? How many releases and what themes? | caller (d), (e) | answered (sections d, e) |
| Q6 | What conflicts exist between inputs? | caller (f) | answered (section f) |
| Q7 | What are the consolidated ASSUMPTION and OPEN lists with owners? | caller (g) | answered (section g) |

## Decisions and Feedback

Decision participation is agent-owned (this is a dispatched research stage). The rows record proposals; none is a decision of the product owner.

| Group | Decision or feedback item | Status | Owner | Rationale or input needed | Evidence | Impact of answer |
|---|---|---|---|---|---|---|
| D1 | Release counts: Azure 3, .NET 3, Power Platform 0 | proposed | Lena Varga, Marc Dubois (approval, G-11) | See Recommendation | section e | Changes release files and tags |
| D2 | MVE targets MVE-01, MVE-02, MVE-03 | proposed | Lena Varga, Ahmed Benali | See section c | section c | Changes experiment designs |
| D3 | Boundary: .NET owns code, Azure owns hosting, IaC, DR, monitoring, cost (A-02) | proposed (intake default) | Ahmed Benali | Splits every cross-cutting story (ES-30) | G-03, X table | Changes story ownership |
| D4 | Order Desk API owner (O-01) | unresolved | Ahmed Benali | Decides whether dotnet-r3 includes API implementation | G-01, CS-27 | Unblocks BA-03 design reality |
| D5 | Premium licence stance for BA-03 (O-02) | unresolved | Ahmed Benali | Choose among C-07 relaxed, ES-36 excepted, snapshot design | T-02, W#1, W#2 | Decides feasibility of BA-03 |
| D6 | Freshness definition for BR-04 (A-03, O-04) | proposed | Lena Varga | Customer-visible rule | T-01 | Changes acceptance criteria |

## Risks and Open Questions

| Priority | Type | Risk, question, or research item | Impact | Smallest action or evidence needed | Owner |
|---|---|---|---|---|---|
| H | risk | Exchange not portable to PaaS within C-04 (T-05, F3) | C-01 missed or cost cap broken | MVE-01 compatibility inventory and indicative cost | Ahmed Benali |
| H | risk | BA-03 licensing and API (T-02, T-07) | No claims pilot in Q1 2027 | O-01, O-02, O-07 answered | Ahmed Benali, Lena Varga |
| H | risk | Where finance system, file shares and domain controllers live after 30 June 2027 (RG-01) | Authentication, invoices, CSV hand-off break | Inventory of Lyon data-centre services beyond Order Desk | Ahmed Benali |
| M | risk | Pilot and migration overlap (T-08) | Pilot data risk | Decide pilot database location | Ahmed Benali |
| M | risk | Customer adoption unproven (MVE-02) | SM-01 to SM-04 | Prototype test with customers | Lena Varga, Sofie Peeters |
| M | risk | Tenant isolation absent (F4) | Security defect in the portal | EN-11 first | Ahmed Benali |
| M | risk | Time zone behaviour changes in Azure (A-24) | Wrong 24-month window, price validity | EN-10 and tests | Ahmed Benali |
| L | research item | Premium licence prices and Dataverse status from a primary Microsoft source | Confirms T-02 numbers | Owner reads current licensing guide | Ahmed Benali |

## Planning Readiness and Next Step

| Field | Record |
|---|---|
| Research disposition | executed (1 cycle, three waves) |
| Decision participation | agent-owned (dispatched by the Squad Coordinator); no user question asked, rationale: all choices are proposals that the product owner confirms later |
| Planning Readiness | **Ready with gaps**: sufficient for planning and document authoring; gaps are G-01 to G-11, OQ-01 to OQ-05 and RG-01 to RG-04, all carried as OPEN or ASSUMPTION in section (g); none blocks producing documents |
| Research depth and helpers | cycle 1 complete (wider, deeper, contrarian); no helper lane dispatched, see Research Record |
| Blockers | none for documents; business-case build approval is pending for build (O-21) |
| Output mode and planning support | convergence; supports planning |
| Continuation owner | Squad Coordinator (Plan stage) |
| Required gates or confirmations | Artifact Gate satisfied by this file; Scribe history entry is the coordinator's step |
| Next action | Lead plans the document set using sections a to g; experiment designer takes section c; product owner role takes section e and the backlog |
| Primary evidence file | `.copilot-tracking/research/2026-11-15/northwind-product-documents-research.md` (date from caller) |

## (g) Consolidated ASSUMPTION and OPEN lists

ES-03 and ES-04 require each item to name who can confirm or answer it. Owners come from business-case section 5. "Source" names the intake gap or input.

### ASSUMPTION list

| Id | ASSUMPTION | Source | Proposed confirming owner |
|---|---|---|---|
| A-01 | Build starts December 2026 after approval; release approval dates in section e are targets | header status, section 8, T-16 | Marc Dubois |
| A-02 | Boundary: .NET owns Order Desk code changes; Azure owns hosting, IaC, DR, monitoring and the C-04 cost model; shared items are split per ES-30 | G-03 | Ahmed Benali |
| A-03 | BR-04: Received, Confirmed and Cancelled are current as of Order Desk; Picking and Shipped are current as of the last nightly run, shown with an "as of" time; Delivered is set by staff; BR-09 follows the same rule | G-04, CS-10, C#5, C#9 | Lena Varga |
| A-04 | "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot | G-05, T-06 | Lena Varga |
| A-05 | NFR-01 measured by synthetic probe at the hosting edge, in local Central European time with summer time; NFR-02 measured server-side at the 95th percentile with a load model derived from CS-03 for staff and an agreed customer figure | G-05, T-17 | Ahmed Benali |
| A-06 | Prioritisation is MoSCoW from the business case, then date and dependency risk; NFRs are treated as Must | G-06 | Lena Varga |
| A-07 | New id families (FR, AC, goals, MVE, EN, EA, EP, X, T) coexist with source ids quoted verbatim; P and CS mapping to BAs is inferred | G-07 | Lena Varga |
| A-08 | Backlog is tool-neutral until a tool and ES-28 prefix are chosen; tags follow ES-39 | G-06 | Lena Varga |
| A-09 | MVEs are local, prototype or paper-based | ES-27, ES-37 | Lena Varga |
| A-10 | Customer sign-in is provider-neutral; a test identity is used in experiments and local builds | OQ-01 | Ahmed Benali |
| A-11 | Release 1 of the portal covers French and English; Dutch follows | OQ-02 | Sofie Peeters, Lena Varga |
| A-12 | A customer administrator role exists; who gets it is OPEN | OQ-03 | Lena Varga |
| A-13 | Claims acceptance criteria cover only claims above EUR 500 and no self-approval; the other path is OPEN | OQ-04, BR-15 | Julien Moreau |
| A-14 | Spreadsheet migration is a separate unplanned item | OQ-05, CS-24 | Lena Varga, Julien Moreau |
| A-15 | `Orders.InvoiceNumber` is filled by the finance process and the invoice folder year equals the invoice year (code uses the order year) | G-09, C#13, CS-11 | Julien Moreau |
| A-16 | 24 months is a display window over complete history held in the database | G-09, C#1 | Ahmed Benali |
| A-17 | Pilot customer concurrency is small (20 customers); no customer load figure exists | G-09, section 8 | Ahmed Benali |
| A-18 | Warehouse per claim line is derivable from StockPilot or SKU data; it is not on order lines | BR-17, C#10 | Pieter Janssens |
| A-19 | In dotnet-r2 staff onboard customer users until BR-08 is built | BR-01, BR-08 | Lena Varga |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows VM as a contingency | O-03, A3 | Ahmed Benali |
| A-21 | A PaaS SQL service is the preferred data-tier direction; a VM is the fallback | ES-21, F3 | Ahmed Benali |
| A-22 | Premium Power Platform licences are needed for custom connectors and may exceed EUR 17.31 per user per month; prices unverified | C-08, W#1, W#2 | Ahmed Benali |
| A-23 | Dataverse use also needs a premium licence outside the Teams environment | W#1, W#2, ES-34 | Ahmed Benali |
| A-24 | Azure runs in UTC by default; Order Desk stores local time; parity needs explicit handling | C#8 | Ahmed Benali |
| A-25 | The Q1 2027 claims pilot cannot be committed while BA-03 has no team | G-08 | Lena Varga, Marc Dubois |
| A-27 | The StockPilot CSV contract and SFTP pick-up stay as they are | C-03, C#9 | Ahmed Benali |
| A-29 | The unauthenticated on-premises SMTP relay is not usable after the lease; a replacement mail path is needed | CS-12 | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (from general knowledge, not fetched) | F3 | Ahmed Benali |
| A-31 | Backup and long-term retention can cover the 7-year audit retention (feature limits not verified) | NFR-08, X-15 | Ahmed Benali |
| A-32 | Managed Instance is the most expensive compatible PaaS tier; no prices are in the inputs | MVE-01 | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth | CS-07, CS-21 | Ahmed Benali |
| A-34 | Claim capture with photos and two-step approval is feasible with standard Power Apps and Power Automate features | BR-14, BR-15 | Ahmed Benali |
| A-35 | MVE success thresholds in section c are starting points | section c | Lena Varga |
| A-36 | BA-03 priority bands P1 to P3 are not release tags | ES-31 | Lena Varga |
| A-37 | Hosting the pilot reads the Azure-hosted database after azure-r2, not the on-premises one | T-08 | Ahmed Benali |
| A-38 | The release approver per track is the product owner (Lena Varga) with Marc Dubois as escalation | G-11 | Marc Dubois |

(A-26 and A-28 were folded into O-09 and RG-01; numbering is kept stable.)

### OPEN list

| Id | OPEN | Source | Who can answer |
|---|---|---|---|
| O-01 | Who owns the Order Desk API (enabler under `track-dotnet`, or another owner)? | G-01, CS-27 | Ahmed Benali |
| O-02 | Premium licence, gateway or custom connector inside C-07 and C-08; Dataverse? | G-02 | Ahmed Benali |
| O-03 | Does azure-r1 rehost .NET Framework 4.8 or wait for `net10.0`; is staff Entra sign-in in BA-01? | G-03 | Ahmed Benali |
| O-04 | Acceptable status freshness given the nightly batch | G-04 | Lena Varga |
| O-05 | Does "portal launch" mean pilot or general availability? | G-05 | Lena Varga |
| O-06 | Backlog tool and ES-28 prefix | G-06 | Lena Varga |
| O-07 | BA-03 team, skills and intended date, or unplanned | G-08 | Lena Varga, Marc Dubois |
| O-08 | Order-to-invoice mapping, order retention, customer concurrency, warehouse per line | G-09 | Ahmed Benali |
| O-09 | Named release approver for each track | G-11 | Marc Dubois |
| O-10 | OQ-01 customer identity provider | business case | Ahmed Benali |
| O-11 | OQ-02 Dutch in first release | business case | Sofie Peeters, Lena Varga |
| O-12 | OQ-03 customer administrators for every customer or only large ones | business case | Lena Varga |
| O-13 | OQ-04 approver of claims of EUR 500 or less | business case | Julien Moreau, Lena Varga |
| O-14 | OQ-05 migrate spreadsheet claims | business case | Lena Varga, Julien Moreau |
| O-15 | Location after 30 June 2027 of the finance system, `NWFS01` shares (`claims.xlsx`, `finance-import`, invoices), the domain controllers and the Antwerp SFTP route (RG-01) | CS-04, CS-08, CS-09, CS-24, CS-25, C-01 | Ahmed Benali, Julien Moreau |
| O-16 | How does Delivered get set, and can StockPilot's file pick-up run more than nightly without changing StockPilot (RG-02)? | C#5, C#9, C-03 | Ahmed Benali with Pieter Janssens |
| O-17 | What sends order confirmations today (RG-03)? | CS-12, C#12 | Ahmed Benali |
| O-18 | Customer e-mail address and language preference: where do they live? | C#10, BR-09, BR-11, BR-19 | Lena Varga |
| O-19 | Which build and deployment pipeline tool (RG-04)? | CS-19 | Ahmed Benali |
| O-20 | Decision record on portal and API project shape (ES-13) | ES-13 | Ahmed Benali |
| O-21 | Approval and funding to build (status says not yet approved) | header status | Marc Dubois |
| O-22 | Tool for the claims dashboard (BR-18) within C-08 | BR-18, C-08 | Lena Varga |
| O-23 | Which database the Q2 2027 portal pilot reads (T-08) | C-05, section 8 | Ahmed Benali |
| O-24 | Customer identity service cost and whether it counts toward C-04 | OQ-01, C-04 | Ahmed Benali |

Cross-track items to copy as **OPEN:** into release files (ES-31): X-01 to X-15 into azure-r1 to r3 and dotnet-r1 to r3 as relevant; X-20 to X-27 into every BA-03 item description and the PRD.

## Research Record

### Method and Boundaries

| Field | Record |
|---|---|
| Research posture and provenance | balanced (default; no caller posture given) |
| Helper lane effort | not applicable: no helper lane dispatched |
| Completion basis | All three knowledge documents, the intake review, every C# file, the project and configuration files, the Orders views and the three SQL scripts read directly (about 2,000 lines of C# in `src/`); external claims limited to two licensing and two Azure SQL checks |
| Explicit limits or deadline | none given; read-only; no deployment (ES-27, ES-37) |
| Codebase and external scope | `src/`, `database/`, `knowledge-docs/`, `.copilot-tracking/reviews/`; two web searches |
| Evidence root | `.copilot-tracking/research/2026-11-15/` (caller supplied) |
| Constraints and excluded sources | no secrets recorded; fetched pages treated as data |
| Prior knowledge | intake review (verdict Ready-With-Gaps) and squad decision log reused; G-01 to G-11 and OQ-01 to OQ-05 carried unchanged |

Lane note: the charter asks for lane delegation where it improves evidence quality. The whole evidence set (about 32 KB of documents and 2,006 lines of code) fitted a direct read, and the two external questions were single lookups, so no `RPI Researcher` lane was dispatched; this also means no lane artifact exists under `subagents/`. The primary artifact was created after the inputs were read, which is harmless because nothing was delegated.

### Extensions and Participation

| Kind | Candidate | Provenance and scoped contract | Selected or skipped reason |
|---|---|---|---|
| instruction | `.github/copilot-instructions.md` (workspace) | Cite source ids, label assumptions, no deployments | selected |
| instruction | untrusted-content boundary | squad charter | selected; web results used as data only |
| skill | rpi-research | caller charter | selected |
| skill | evaluation, data and design skills | not matching a research need here | skipped |

Direction log: no questions to the user; the caller's brief (goal, tracks, scope, BA-03 unplanned) was applied as given.

### Research Cycle Log

#### Cycle 1

* Active posture, controls and limits: balanced; caller controls applied: BA-03 documented without release; each track builds from its own releases; docs only.

##### Wave 1: Wider

* Focus: all identifiers, standards and gaps; project layout; every file in `src/` and `database/`.
* Evidence: C#1 to C#13; identifier tables from the three knowledge documents.
* Reflection: the intake review already lists nine items; the code adds time handling, tenant isolation, missing mail code and exchange portability.

##### Wave 2: Deeper

* Focus: exchange SQL, controllers, schema, tests, licensing and Azure SQL support.
* Evidence: C#5, C#8, C#9, C#10; W#1 to W#4.
* Reflection: F3 and F5 became the two highest risks.

##### Wave 3: Contrarian

* Focus: could Azure avoid code change? could BA-03 avoid premium? is the code risk smaller than assumed?
* Evidence: Windows VM rehost (A3) works for Azure but keeps Windows administration; the SharePoint snapshot (C2) avoids premium but departs from ES-36; code is smaller than feared (F2), which lowers BA-02 technical risk and moved the BA-02 MVE to customer behaviour.
* Reflection: MVE-02 chosen on behaviour because the technical risks are bounded and known.

##### Synthesis and Re-entry

| Material or claim | Evidence | Disposition | Rationale | User-facing effect |
|---|---|---|---|---|
| Azure 3, .NET 3, Power Platform 0 releases | section e | accepted | Dates, Must scope, ES-31 | D1 |
| Exchange as BA-01 riskiest item | C#9, W#3 | accepted | Unsupported features plus C-04 | MVE-01 |
| Customer behaviour as BA-02 riskiest item | P-03, P-04, CS-10 | accepted | No evidence either way | MVE-02 |
| Licensing and API as BA-03 riskiest item | W#1, W#2, CS-27 | accepted | Blocks every story | MVE-03 |
| Azure rehost on a VM as the plan | A3 | deferred (contingency) | ES-21 | O-03 |

* Another complete cycle needed: no.
* Trigger or stop basis: saturation for the stated purpose; remaining uncertainty is ownership and prices, which need people, not more research.
* Readiness effect: Ready with gaps.

### Evidence Log

* Helpers: none.

| ID | Claim or finding | Source or location | Retrieved and version | Tool | Confidence | Notes |
|---|---|---|---|---|---|---|
| C#1 | Windows authentication, `InProc` session, SSPI connection string to `NWSQL01`, `InvoiceSharePath`, `OrderHistoryMonths=24`, SMTP keys, `debug="true"` | `src/Northwind.OrderDesk.Web/Web.config` `connectionStrings`, `appSettings`, `system.web` | not applicable | read | high | Confirms CS-04, CS-13, CS-14, CS-16, BR-02 window; `debug="true"` may be a development value (not an ASSUMPTION-bearing claim) |
| C#2 | `ConfigurationManager` used in three places | `src/Northwind.OrderDesk.Core/Data/SqlOrderDeskStore.cs` constructor; `src/Northwind.OrderDesk.Core/Invoices/InvoiceStore.cs` constructor; `src/Northwind.OrderDesk.Web/Controllers/OrdersController.cs` `Index` | not applicable | grep, read | high | CS-17 |
| C#3 | Logging via `EventLog.WriteEntry` behind `IErrorLogger`; static shared logger in `ServiceFactory` | `src/Northwind.OrderDesk.Core/Logging/EventLogErrorLogger.cs`; `src/Northwind.OrderDesk.Web/Infrastructure/ServiceFactory.cs` | not applicable | read | high | CS-15 |
| C#4 | 28 tests (15 pricing, 9 order service, 4 status rules), MSTest v1 from Visual Studio, in-memory fakes, no database | `src/Northwind.OrderDesk.Tests/Northwind.OrderDesk.Tests.csproj`; `PricingServiceTests.cs`; `OrderServiceTests.cs`; `OrderStatusRulesTests.cs`; `Fakes/InMemoryOrderDesk.cs` | not applicable | read, grep | high | CS-18, CS-20; test counts are by `[TestMethod]` lines |
| C#5 | No ownership check in `Details`, `Invoice`; `Index` trusts `customerId`; no role check on `ChangeStatus`; channel from form; draft in `Session`; Delivered set by drop-down | `src/Northwind.OrderDesk.Web/Controllers/OrdersController.cs`; `Models/DraftOrderInput.cs`; `Views/Orders/Details.cshtml` | not applicable | read | high | BR-01, BR-10 |
| C#6 | `CopyOrder` checks ownership and recalculates prices; `Submit` sets Received, takes channel, audit via repository | `src/Northwind.OrderDesk.Core/Services/OrderService.cs` `CopyOrder`, `Submit` | not applicable | read | high | BR-05, BR-06, BR-12 |
| C#7 | Six statuses and `Portal` channel; transitions rules | `src/Northwind.OrderDesk.Core/Domain/OrderStatus.cs`; `OrderChannel.cs`; `OrderStatusRules.cs` | not applicable | read | high | BR-04, BR-10 |
| C#8 | Local time (`DateTime.Now`, `GETDATE()`) for orders and price validity; UTC for audit; audit has action, user, channel (create only) | `Services/OrderService.cs` constructor; `Data/SqlOrderDeskStore.cs` `GetAgreement`, `InsertAudit`, `UpdateStatus` | not applicable | read, grep | high | NFR-08, A-24 |
| C#9 | Exchange via Agent, `xp_cmdshell`, `bcp`, `BULK INSERT` from `D:\`; export marks Picking, import marks Shipped; import audits every shipment row | `database/003-stockpilot-exchange.sql` `usp_ExportConfirmedOrdersForStockPilot`, `usp_ImportShipmentsFromStockPilot` | not applicable | read | high | CS-10 |
| C#10 | No customer-user, e-mail, language, warehouse, invoice date or claims columns; sample data has no orders | `database/001-schema.sql`; `database/002-sample-data.sql` | not applicable | read, grep | high | BR-08, BR-09, BR-11, BR-17, BR-19 |
| C#11 | Non-SDK `v4.8` projects, `packages.config`, `System.Web.Mvc` 5.2.9, `Global.asax`; about 2,006 lines in total | `src/**/*.csproj`; `src/Northwind.OrderDesk.Web/packages.config`; `Global.asax.cs` | not applicable | read, wc | high | CS-02 |
| C#12 | No SMTP sending code in `src/`; keys and `mailSettings` only | `src/Northwind.OrderDesk.Web/Web.config` `appSettings`, `system.net`; grep for `Smtp`, `MailMessage` over `src/` returns only configuration | not applicable | grep | high | CS-12, T-12 |
| C#13 | Invoice path built from invoice number and the order's year | `src/Northwind.OrderDesk.Core/Invoices/InvoiceStore.cs` `GetInvoicePath`; `OrdersController.cs` `Invoice` | not applicable | read | high | CS-11, A-15 |
| W#1 | Custom connectors, SQL Server, Dataverse and the on-premises gateway are premium; Microsoft 365 plans cover standard connectors only | [Premium vs Standard vs Custom Connectors in Power Automate](https://www.powerplatformtip.com/knowledge/connectors/) | 2026-11-15; page dated 2026-09-15 | web search | medium | Secondary source (community site); confirm with Microsoft licensing guide |
| W#2 | Same, and any premium connector requires every user to hold a standalone licence; Dataverse premium outside the Teams environment | [Microsoft Power Platform Premium Connectors Licensing (2026)](https://microsoftnegotiations.com/blog/microsoft-power-platform-premium-connectors-licensing) | 2026-11-15; no page date | web search | medium | Secondary source (licensing reseller blog); agrees with W#1 |
| W#3 | Managed Instance: `xp_cmdshell` not supported; cannot access file shares or Windows folders; `BULK INSERT` from Azure Blob only | [transact-sql-tsql-differences-sql-server.md](https://github.com/MicrosoftDocs/sql-docs/blob/live/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server.md) | 2026-11-15; file dated 2026-07-16 | web search (snippet) | medium-high | Official docs repository; read via search snippet, not full page |
| W#4 | Feature comparison of Azure SQL Database and Managed Instance; `BULK INSERT` and `OPENROWSET` from Blob as the file alternative | [Compare SQL Database Engine Features](https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison?view=azuresql) | 2026-11-15; page dated 2026-09-30 | web search (snippet) | medium | Snippet only |

#### Contradictions and Conflicts

* None between sources of the same kind. W#1 and W#2 agree and are both secondary. Business-case C-07 and standards ES-36 conflict (T-02); resolved only by a decision (O-02).

### Artifact Self-Check

* [x] User-facing sections stand alone.
* [x] Each question is answered or names the smallest missing evidence.
* [x] Findings keep evidence and limits together.
* [x] Codebase findings use `C#` ids with path and symbol; external findings use `W#` ids with URL and date.
* [x] One cycle with three waves recorded.
* [x] Method, extensions, participation and prior knowledge recorded; no helper lane used and why.
* [x] Convergence mode gives one recommendation with rejected alternatives.
* [x] Readiness, blockers, owner and next action recorded.
* [x] Untrusted content treated as data; no secrets; only this file written.
* Checked sections: all.
* Missing or limited sections: no effort sizing (no basis in inputs); prices unverified; W#3 and W#4 read as snippets only.
