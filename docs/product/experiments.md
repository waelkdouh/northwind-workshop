---
title: Northwind minimum viable experiments (MVE-01 to MVE-03)
doc: experiments
status: Draft for review
date: 2026-11-15
owner_role: experimenter (Experiment Designer)
lineage: .copilot-tracking/plans/2026-11-15/northwind-product-documents-plan.md (phase P02, Canonical Contract C8 row D3); docs/product/business-requirements.md (BRD-NW-001, checked 2026-11-15)
track_tags: track-azure (MVE-01), track-dotnet (MVE-02), track-power-platform (MVE-03)
---

# Northwind minimum viable experiments

| Field | Value |
|---|---|
| Status | **Draft for review.** Not approved. No experiment has been run; every result field is empty. |
| Date | 2026-11-15 |
| Scope | One experiment per business area: BA-01 (Azure), BA-02 (.NET), BA-03 (Power Platform) (source: business-case section 4) |
| Lineage | Goals `BG-01` to `BG-05`, dependencies `X-nn`, tensions `T-nn`, and the ASSUMPTION and OPEN ids used here have the same meaning as in the business requirements document [business-requirements.md](business-requirements.md) (`BRD-NW-001`, draft). Where this document adds an id, it starts with `MVE-` (section 5). |
| Business case status | "Approved for discovery. Not yet approved for build" (source: business-case header). Experiments are discovery work, so they fit that status. Approval to build is still **OPEN:** O-21. |
| Release | None of the three experiments belongs to a release. They run before the epics they gate are committed (ES-31 does not apply). |

All figures are the workshop's synthetic figures. Every claim cites its source in the form `(source: BR-05, CS-10)`. Anything not in `knowledge-docs` is marked **ASSUMPTION:** and listed in section 5 with an owner. Every unanswered question is marked **OPEN:** with an owner (ES-02, ES-03, ES-04).

## 1. Purpose and how the experiments are run

**Why experiments.** Each business area has one belief that, if wrong, would change what the team builds. An experiment tests that belief first, cheaply, before the team commits to the related epics. A pass lets the team go. A fail is also a useful result: it saves the team from building on a false belief.

**What an MVE is here.** A *minimum viable experiment* is the smallest test that can prove an assumption wrong. It is not a demo, not a first version of the product and not production code (red flags: demo, mini-MVP, production code expectations).

**How they are run (local only).** Nothing is deployed to Azure and nothing is created or changed in a Power Platform tenant or environment (source: ES-27, ES-37). The methods are: reading and running the existing scripts on a local machine, desk research against public price lists and documentation, calculators, a paper or clickable prototype, and short interviews. **ASSUMPTION:** A-09 (MVEs are local, prototype or paper-based).

**Rules that apply to all three.**

* Thresholds are set **before** the experiment runs and are not changed afterwards. A changed threshold is recorded as a divergence, not as a new pass.
* Each experiment tests one thing. Each has one pass or fail decision and three possible decisions: **go**, **adjust** or **stop**.
* All thresholds are starting points proposed by the experimenter and are labelled **ASSUMPTION:** A-35. Lena Varga sets the final numbers (source: plan P02-T01).
* Any claim about an Azure or Power Platform feature, price or licence that this document could not verify against the primary Microsoft documentation is labelled **ASSUMPTION:** in the text. The research read two Power Platform sources that were secondary, and Azure sources through search snippets only (source: research W#1 to W#4).
* **Measures and who measures them (OPEN: O-26).** The business case names targets for `SM-01` to `SM-07` but not who measures them or from which source, and it names no owner for the goals `BG-01` to `BG-05`. The BRD records this as **OPEN:** O-26 (owner Lena Varga) and proposes goal owners in its section 4.1. The checks in this document (M1a to M1c, R1 to R3, P3a to P3d) are **leading indicators** that stand in for those measures before anything is built. Each MVE names its own measurement source and owner for those checks. They do **not** replace the measurement source that O-26 asks for, and passing one does not mean the success measure is met (source: BRD section 4, G-05, **ASSUMPTION:** MVE-A-06).
* The IT team (6 people) pairs with whoever runs MVE-01 and MVE-03, so the knowledge stays with Northwind and does not stay with a visiting adviser (source: C-06).

## 2. Summary table

| MVE | BA | Track tag | Riskiest assumption (short) | Method | Threshold (ASSUMPTION: A-35) | Source ids | Decision owner |
|---|---|---|---|---|---|---|---|
| **MVE-01** | BA-01 Platform and data-centre exit | `track-azure` | A platform-as-a-service (PaaS) data tier can host `NorthwindOrders`, keep the nightly StockPilot exchange (file contract unchanged) and stay inside the cost cap, with a recovery point objective (RPO) of 1 hour | Local script inventory and file-contract baseline, desk research on supported features, indicative price calculation, paper recovery check. No deployment. | Pass only if one PaaS option satisfies all three: 0 unmapped constructs (M1a); indicative production plus test cost at or below **EUR 1,200 per month**, which is 80 % of C-04 (M1b); documented backup frequency at or below **60 minutes** (M1c) | BG-02, BG-04, C-01, C-03, C-04, NFR-06, BR-13, SM-07, CS-07, CS-10, ES-21, ES-25, ES-27, X-05, X-12, T-05 | Ahmed Benali (Marc Dubois for any change to C-04) |
| **MVE-02** | BA-02 Ordering and customer self-service | `track-dotnet` | Customers will reorder unaided and will trust an order status that is refreshed only once a night, enough to stop phoning | Moderated test of a clickable prototype with 5 to 8 customers (**ASSUMPTION:** MVE-A-05), plus a short interview. No code in `src/`. | At least **80 %** of participants finish the reorder unaided (R1) and at least **60 %** would use the status instead of phoning (R2); both rounded up per participant count | BG-01, BR-04, BR-05, BR-12, SM-01, SM-02, P-03, P-04, CS-10, CS-05, X-06, T-01, T-06 | Lena Varga |
| **MVE-03** | BA-03 Delivery claims and credit notes | `track-power-platform` | A claims solution can meet the custom-connector rule and the EUR 900 cap for about 52 users, and can hand credit-note requests to a finance system with no API | Desk research and paper design: capability-to-licence matrix, per-user cost arithmetic, field check of the order-line contract, options for handing over a comma-separated values (CSV) file. No tenant touched. | Pass if at least one option shows **cost per user at or below EUR 17.31 per month** (900 divided by 52), with **0 capabilities of unknown licence class**, an order-line path through a custom connector (ES-36) and a workable CSV hand-off; otherwise a recorded decision to relax C-07, C-08 or ES-36 | BG-03, BG-04, C-07, C-08, ES-34, ES-35, ES-36, ES-37, CS-25, CS-26, CS-27, BR-14, BR-15, BR-16, X-20, X-24, X-27, T-02, T-07 | Ahmed Benali (feasibility) and Lena Varga (backlog); Marc Dubois if a cap changes |

Gated epics and releases, in one view (epic ids from the Canonical Contract C5):

| MVE | Gates (decision is taken before these are committed) |
|---|---|
| MVE-01 | `EPIC-102` (data-tier decision `EA-05`, cost model `EA-09`, `azure-r1`); `EPIC-103` (exchange redesign `EA-06`, backup design `EA-08`, `azure-r2`; the production database settings of `EA-15` come from `EA-05`); `EPIC-104` (database migration and rehearsal `EA-16`, `azure-r3`) and the rest of the cutover plan through its inputs. |
| MVE-02 | `EPIC-202` (portal pilot stories for `BR-04`, `BR-05`, `BR-10`, `BR-12`, `dotnet-r2`); `EPIC-203` instrumentation for `SM-01` to `SM-04`. It does **not** gate `EPIC-201`, whose parity work is technical and low risk. |
| MVE-03 | `EPIC-301` (`EP-03`, `EP-04`, `EP-05`, `EP-06`), then `EPIC-302`, `EPIC-303`, `EPIC-304`. All are unplanned and keep only the `track-power-platform` tag. |

## 3. The experiments

### MVE-01: Can a PaaS data tier carry Order Desk and the StockPilot exchange inside the cost cap?

| Field | Value |
|---|---|
| Business area and track | BA-01 Platform and data-centre exit; `track-azure` (source: business-case section 4, ES-30) |
| Experiment type | Architecture and cost feasibility (desk research, local script analysis, paper recovery check) |
| Goals served (BRD section 4.1) | `BG-02` Order Desk runs in Azure before 30 June 2027 (`SM-07`; proposed goal owner Marc Dubois) and `BG-04` run cost inside the caps (C-04; proposed goal owner Ahmed Benali). Goal owners are proposals, **OPEN:** O-26. |
| Dependencies and tensions in play | `X-05` exchange redesign for a managed database, `X-12` shared cap C-04, `X-15` 7-year audit trail in Azure; tensions `T-03` (nobody owns the whole cap), `T-05` (exchange on `xp_cmdshell` versus the date and ES-21), `T-14` (recovery never tested) |
| Measurement source and owner | The experiment's own records: the inventory, the file-contract baseline, the dated calculator output and the documentation extract. Owner Ahmed Benali. The production source for `SM-07` and for the cost cap is **OPEN:** O-26 (Lena Varga). |
| Status | Not run |

#### 3.1.1 Riskiest assumption

**ASSUMPTION (to be tested):** A platform-as-a-service (PaaS) SQL tier can host the 48 GB `NorthwindOrders` database. It can keep the nightly StockPilot file exchange working with the CSV file contract unchanged. All of this fits inside EUR 1,500 a month for production plus one test environment, with a recovery point of 1 hour and a recovery time of 4 hours (source: C-01, C-03, C-04, NFR-06, CS-07, CS-10). This is the riskiest assumption in the PaaS direction A-21.

**Why this one is the riskiest.** It is the only integration that nobody has mapped, it depends on a hard date, and it competes for a shared cap.

| Evidence for | Evidence against |
|---|---|
| The database is small: 48 GB, growing about 1 GB a month, so about 56 GB by 30 June 2027 (**ASSUMPTION:** MVE-A-03, linear growth over 7 to 7.5 months) (source: CS-07, C-01). | The exchange depends on `xp_cmdshell`, `bcp`, `BULK INSERT` from a local `D:\` path and a SQL Server Agent job (source: CS-10, research C#9; `database/003-stockpilot-exchange.sql`). |
| Load is light: average CPU 18 %, peak 55 %, about 60 concurrent users (source: CS-06, CS-03). | Managed Instance does not support `xp_cmdshell` and cannot read file shares or Windows folders; `BULK INSERT` must read from Azure Blob Storage (source: research W#3, read as a search snippet, medium-high confidence). |
| The exchange logic is small: two stored procedures, 45 lines in one file (source: `database/003-stockpilot-exchange.sql`, C#9). | SQL Server Agent is not available on Azure SQL Database (**ASSUMPTION:** A-30, from general knowledge, not fetched). |
| 15-minute log backups exist today, which fits an RPO of 1 hour on paper (source: CS-07, NFR-06). | Managed Instance is probably the most expensive compatible tier; no prices are in the inputs (**ASSUMPTION:** A-32). Private endpoints on every data service add running cost (source: ES-25, T-03). |
| StockPilot must not change, so the file contract is fixed and can be written down exactly (source: C-03, business-case section 6, A-27). | A recovery has never been tested; backups were restored by hand twice in five years (source: CS-23, T-14). |
| | The export procedure sets orders to Picking even if the `bcp` file was not written, because the `UPDATE` does not check the result of `xp_cmdshell` (`NO_OUTPUT`). The import writes an audit row for every shipment line, even when no order changed. Both are existing behaviour: record them, do not fix them silently (source: C#9, T-13, ES-19). |
| | The Agent job definition and the Windows scheduled task that copies files to the Antwerp Secure File Transfer Protocol (SFTP) server are not in the repository (only mentioned in a comment) (source: CS-10, `database/003-stockpilot-exchange.sql`). **OPEN:** MVE-O-05. |

**Alternatives considered and ranked lower** (source: research section (c)): a migration inside the 6-hour Sunday window (likely feasible by log-based restore, **ASSUMPTION:** A-33, source: BR-13, CS-21); rehosting the unchanged app on a Windows virtual machine (VM), a contingency (A-20, O-03).

#### 3.1.2 Hypothesis

> We believe that at least one PaaS SQL option can run `NorthwindOrders` and the StockPilot exchange with the file contract unchanged. We will test this in three steps: (a) inventory every non-portable construct in `database/*.sql`; (b) price the options for production plus one test environment; (c) check the published backup capability against NFR-06 on paper. We will know we are **right** when one PaaS option passes M1a, M1b and M1c below. We will know we are **wrong** when no PaaS option passes all three.

Three checks make up one verdict; all three must pass **on the same option**:

| Check | Pass threshold (**ASSUMPTION:** A-35) | Fail signal | Linked ids |
|---|---|---|---|
| **M1a** Compatibility and file contract | Every construct on the inventory has at least one documented replacement on the option, and the replacement keeps the CSV contract captured in step 2: **0 unmapped constructs**. | One or more constructs without a documented replacement on every PaaS option. | C-03, CS-10, ES-21, BR-13, A-27, A-30 |
| **M1b** Indicative cost | Production plus one test environment for Order Desk (database, web host, invoice storage, monitoring, private endpoints) at or below **EUR 1,200 per month**, which is 80 % of C-04 and leaves EUR 300 for the portal and API (derived: EUR 1,500 less EUR 1,200; source: C-04, X-12). | Above EUR 1,500: the cap is broken. Between EUR 1,200 and EUR 1,500: headroom is lost and the result is "adjust". | C-04, ES-25, ES-26, X-12, T-03, A-32 |
| **M1c** Recovery point on paper | The published backup or point-in-time capability of the option gives a recovery point of **60 minutes or less**. The 4-hour recovery time is **not scored**: it is recorded as unproven and carried to the first recovery test plan `EA-14` and `azure-r3` (source: NFR-06, CS-23, T-14). | Capability above 60 minutes, or not documented. | NFR-06, CS-07, A-31 (**ASSUMPTION:** MVE-A-07, published figures not verified here) |

#### 3.1.3 Smallest experiment

| Item | Plan |
|---|---|
| Method | Local analysis and desk research. Nothing is deployed (source: ES-27). |
| Who | An engineer from the IT team runs it with an Azure adviser; the pairing makes the IT team own the result (source: C-06). **OPEN:** MVE-O-01 (name). Ahmed Benali reviews and decides. |
| Data | `database/001-schema.sql`, `002-sample-data.sql`, `003-stockpilot-exchange.sql`; `src/Northwind.OrderDesk.Core/Data/SqlOrderDeskStore.cs` (two `GETDATE()` and one `GETUTCDATE()` use); current-state facts CS-03, CS-06, CS-07, CS-08 (120 GB of invoices, about 135 GB by June 2027, **ASSUMPTION:** MVE-A-03). Synthetic orders only: the sample data has no orders (source: research C#10), so a throwaway script of about 20 orders is used and not committed. |
| Time-box | 5 working days of elapsed time. |
| Effort | About 4 person-days (**ASSUMPTION:** MVE-A-01). |
| Owner | Ahmed Benali (accountable). Marc Dubois is informed if the result touches C-04. |

Steps:

1. **Inventory (0.5 day).** List every construct in `database/*.sql` that depends on Windows, a local folder, a file tool or the server name, with file and line. Expected from reading the files: `xp_cmdshell` (1), the `bcp` command string (1), `BULK INSERT` (1), the `D:\Exchange\StockPilot` paths, the hard-coded `-S NWSQL01 -T` (Windows authentication, NFR-05), the Agent job named in a comment, and local-time functions (A-24). Mark each as supported, changed or unsupported on three options: Azure SQL Database, Azure SQL Managed Instance, and SQL Server on a virtual machine (the fallback, A-21). Use the full Microsoft pages behind W#3 and W#4, not only the snippets.
2. **File-contract baseline (0.5 day).** On a local SQL Server (Developer edition or container, **ASSUMPTION:** MVE-A-04), load `001` and `002`, add the synthetic orders, run the `SELECT` that sits inside the `bcp` command, and parse a made-up `shipments.csv` the way `BULK INSERT` does. Write down the exact contract. The export has five columns (`OrderNumber`, `LineNumber`, `Sku`, `Quantity`, `DeliveryAddress`), the separator `;`, no header row, and the file name `orders_<yyyymmdd>.csv`. The import has three columns (`OrderNumber`, `ShippedAt`, `Carrier`) and skips the first row (source: C#9, A-27). This is the reference that M1a is measured against.
3. **Replacement on paper (1 day).** For each unsupported or changed construct, name one documented replacement pattern, in one line. Do **not** design or build the exchange: that is `EA-06`. The test is only whether a replacement exists. **ASSUMPTION:** any Azure feature named here stays unverified until the full Microsoft page is read in step 1 (A-30, A-32).
4. **Indicative cost (1 day).** Use the public Azure pricing calculator, France Central (source: ES-20), for production plus one test environment, for each option. Size from today's load (source: CS-03, CS-06, CS-07). Include web host, database, invoice storage, Log Analytics, Application Insights, and private endpoints (source: ES-25, ES-26). Record the price date. Prices are **ASSUMPTION:** MVE-A-02 until Ahmed Benali confirms them.
5. **Recovery point on paper (0.5 day).** From the published documentation, record backup frequency and point-in-time restore for each option and compare with 60 minutes. Note the 4-hour recovery time as unproven.
6. **Review and decide (0.5 day).** Ahmed Benali reviews the three checks and records go, adjust or stop.

#### 3.1.4 What is explicitly NOT being built

* No Azure subscription, resource, trial database or deployment (ES-27).
* No Bicep, no `main.bicep`, no landing zone (`EA-01`).
* No redesign of the StockPilot exchange (`EA-06`); no change to StockPilot (C-03, business-case section 6).
* No migration rehearsal, no recovery test (`EA-16`, `EA-14`, `azure-r3`).
* No change to `src/` or to the three database scripts, and no silent fix of the defects found (ES-19, T-13).

#### 3.1.5 Success and failure criteria, and the decision they unlock

| Result | Criteria | Decision | What changes in the backlog and releases |
|---|---|---|---|
| **Go** | One PaaS option passes M1a, M1b and M1c. | Proceed with that option. | `EA-05` records it; `EA-06` starts from the documented replacements; `EA-09` takes the estimate as its baseline. `azure-r1` and `azure-r2` scope stays as in the Canonical Contract. |
| **Adjust** | Either only the VM option passes (the PaaS options fail M1a), or a PaaS option passes M1a and M1c but costs between EUR 1,200 and EUR 1,500. | Take the VM fallback (A-21) with a decision record because it departs from ES-21, or take the PaaS option and tell the sponsor that headroom for the portal is below EUR 300 (derived: EUR 1,500 less EUR 1,200). | `EA-05` moves to the VM fallback, or `EA-09` and `X-12` carry the reduced headroom; `EA-06` is re-scoped. Marc Dubois is informed. |
| **Stop** | No option stays within EUR 1,500 while meeting M1a and M1c. | Stop planning `azure-r2` scope on the current cap. | `EA-06`, `EA-08`, `EA-10` and `EA-16` are paused, and so are the production database settings of `EA-15`, which come from `EA-05`; `azure-r1` foundation items (`EA-01` to `EA-03`) continue because they do not depend on the data tier. Marc Dubois decides whether to relax C-04 or reduce scope (**OPEN:** O-21). |

A conformant experiment that ends in **stop** is a successful experiment: it found the problem before the team built on it.

#### 3.1.6 Constraints and vetting

* Constraints: C-01 (30 June 2027), C-02, C-03, C-04, C-06, NFR-03 (data stays in the European Union, EU), ES-20 to ES-27.
* Vetting: the business driver is a hard date and a cost cap (C-01, C-04). The problem is crisp. The next step for both outcomes is written above. The customer, here the IT team, can act on the result (C-06). Responsible AI does not apply: no AI is involved. Red-flag check: the experiment inspects and calculates, it does not demo or build.
* Linked ids: BG-02, BG-04, BG-05, C-01, C-02, C-03, C-04, C-06, BR-13, NFR-01, NFR-03, NFR-05, NFR-06, NFR-08, SM-07, CS-06, CS-07, CS-08, CS-10, CS-21, CS-23, ES-19 to ES-27, A-20, A-21, A-24, A-27, A-30, A-31, A-32, A-33, A-35, T-03, T-04, T-05, T-13, T-14, X-02, X-03, X-05, X-12, X-15, G-03, G-05, O-03, O-15, O-16, O-21, O-26.

---

### MVE-02: Will customers reorder unaided and trust a night-old status?

| Field | Value |
|---|---|
| Business area and track | BA-02 Ordering and customer self-service; `track-dotnet` (source: business-case section 4, ES-30) |
| Experiment type | Use case and UX (moderated prototype test and short interview) |
| Goals served (BRD section 4.1) | `BG-01` Customers serve themselves (`SM-01`, `SM-02`, `SM-03`, `SM-04`; proposed goal owner Lena Varga, **OPEN:** O-26). |
| Dependencies and tensions in play | `X-06` status freshness is bounded by the exchange cadence; `X-04` customer sign-in (provider-neutral here, A-10); tensions `T-01` ("always up to date" versus the nightly update) and `T-06` ("portal launch" versus a 20-customer pilot) |
| Measurement source and owner | The session notes and the scored checklist for R1 to R3, kept by the facilitator (**OPEN:** MVE-O-02). The production sources for `SM-01` and `SM-02` (for example order channel counts and call logs) are **OPEN:** O-26, owner Lena Varga; this experiment does not measure them. |
| Who speaks for customers | The BRD names no representative for customer users and asks O-26 to name one (source: BRD section 6). Until it is answered, the 5 to 8 participants (**ASSUMPTION:** MVE-A-05) speak for themselves only, and Lena Varga is the proposed voice of the customer users for the decision. |
| Status | Not run |

#### 3.2.1 Riskiest assumption

**ASSUMPTION (to be tested):** Customer users will complete a reorder themselves: copy a previous order, change quantities, remove lines and submit. They will also trust the order status shown, even though Picking and Shipped are refreshed only once a night. Both are enough for them to stop phoning the Order Desk (source: BR-04, BR-05, SM-01, SM-02, P-03, P-04, CS-10).

**Why this one is the riskiest.** The technology risk for BA-02 is low and known (source: research F2: about 2,000 lines of C#, 28 tests, 15 on pricing). What nobody has shown is customer behaviour. If customers do not reorder through the portal or do not trust the status, `SM-01` and `SM-02` are not reachable, whatever the quality of the code.

| Evidence for | Evidence against |
|---|---|
| 70 % of orders repeat a previous order with small changes (source: P-04). | No customer research is cited anywhere in the inputs. |
| 410 "where is my order?" calls a week are about 35 % of inbound calls (source: P-03). | Picking and Shipped change once a night; "Picking" really means "exported to StockPilot", and Delivered is set by hand (source: CS-10, A-03, T-01, research C#5, C#9). |
| The copy-and-reprice logic exists and is tested: `CopyOrder` checks ownership, `Submit` recalculates prices and drops zero-quantity lines (source: C#6; `OrderServiceTests.cs`: `CopyOrderCopiesProductsAndQuantitiesButNotPrices`, `SubmitRemovesZeroQuantityLinesAndRenumbers`). | 20 pilot customers are 1.7 % of 1,150 active customers (source: business-case section 8, CS-05); 35 % portal share (`SM-01`) is high for independent grocers and kitchens, with no evidence either way. |
| The six statuses in BR-04 already exist in the code (source: C#7, intake review). | Average demand is 1.65 orders per customer per week (1,900 divided by 1,150, derived from CS-05); 35 % means about 0.58 orders per customer per week through the portal, which is a lot if only some customers adopt it. |

**Alternatives considered and ranked lower:** the choice of customer identity provider (OQ-01; A-10 makes sign-in provider-neutral) and accessibility to the Web Content Accessibility Guidelines (WCAG) 2.2 level AA (NFR-07, standard practice) (source: research section (c)).

#### 3.2.2 Hypothesis

> We believe that customers can reorder unaided from a list of past orders and will use a status that shows "as of" the last update instead of phoning. We will test this by letting 5 to 8 customers use a clickable prototype and then asking what they would do. We will know we are **right** when both checks pass. At least 80 % must finish the reorder without help (R1). At least 60 % must say they would use the status instead of phoning (R2). We will know we are **wrong** when either is below its threshold.

| Check | Pass threshold (**ASSUMPTION:** A-35; Lena Varga sets the final numbers) | Linked ids |
|---|---|---|
| **R1** Reorder unaided | At least **80 %** of participants (rounded up: 4 of 5, 5 of 6, 6 of 7, 7 of 8) finish the task without help from the facilitator: copy a previous order, change two quantities, remove one line, submit. | BR-05, BR-12, P-04, SM-01 |
| **R2** Trust in the status | At least **60 %** of participants (rounded up: 3 of 5, 4 of 6, 5 of 7, 5 of 8) say they would use the shown status instead of phoning when an order shows Picking or Shipped "as of last night". The 60 % is set above the 39 % fall in calls that `SM-02` needs (410 to 250 is 160 fewer calls, 39 %), because people say they will do more than they do (**ASSUMPTION:** MVE-A-05). | BR-04, P-03, SM-02, A-03, CS-10 |
| **R3** Reading, not scored | Each participant states how many of their last 10 orders they would have placed through the portal. The median is recorded and compared with the 35 % of `SM-01` as a leading indicator only (source: SM-01, G-05). | SM-01 |

Verdict rule: **pass** needs R1 and R2. R3 informs the "adjust" decision only. With 5 to 8 participants the result is a **signal, not proof**; confidence is low and is stated as such in the outcome (**ASSUMPTION:** MVE-A-05).

#### 3.2.3 Smallest experiment

| Item | Plan |
|---|---|
| Method | Moderated test of a clickable prototype (paper or screen mock-up), 30 to 45 minutes per participant, then a short interview. No code is written in `src/`; the running .NET Framework 4.8 application is not used. |
| Prototype source | The fields and layout of the existing screens `Views/Orders/Index.cshtml` (order list with a "Copy to new order" button), `Details.cshtml` and `Draft.cshtml`, filled with synthetic orders (source: `src/Northwind.OrderDesk.Web/Views/Orders`). The six statuses of BR-04 are shown. The prototype adds only an "as of" line next to the status (A-03) and a customer-price column (BR-12). |
| Who | **5 to 8 existing customers** (**ASSUMPTION:** MVE-A-05), spread across France, Belgium and Luxembourg and across grocers and kitchens. Lena Varga sets the share and arranges any customer contact together with Sofie Peeters; the team does not contact customers itself (source: business-case section 5, plan P02-T01). **OPEN:** MVE-O-02 (facilitator and language: French, Dutch, English). |
| Tasks | T1 Reorder: copy a previous order, change two quantities, remove one line, submit. T2 Status: show two orders, one "Picking, as of 02:00 last night" and one "Shipped, as of last night's update"; ask what the participant would do next. T3 Interview: orders per week, how many repeat, channel used today, when they last phoned about an order and why. |
| Data | Synthetic orders and products only (source: `database/002-sample-data.sql` style data, six products). No real customer data, no real prices, no recordings. Notes are anonymised as P1, P2 and so on (ES-17, NFR-03). |
| Time-box | About 2 weeks elapsed: 1 week to recruit, 3 days of sessions, 1 day to analyse. |
| Effort | About 4 person-days: prototype 1.5, sessions and notes 1.5, analysis 1 (**ASSUMPTION:** MVE-A-01). |
| Owner | Lena Varga (accountable). Sofie Peeters supports the Belgian customers and Dutch. |

#### 3.2.4 What is explicitly NOT being built

* No working portal, no sign-in, no customer-user store, no deployment (`EN-11`, `EN-08`, ES-27).
* No change to `src/`; no fix of the missing ownership checks found in the controller (BR-01 is a build item in `EPIC-202`, source: research F4).
* No identity-provider comparison (OQ-01), no Dutch translation (OQ-02), no WCAG audit (NFR-07).
* No invoice download, no user administration, no e-mail (BR-07, BR-08, BR-09).
* No change to the StockPilot cadence (C-03).

#### 3.2.5 Success and failure criteria, and the decision they unlock

| Result | Criteria | Decision | What changes in the backlog and releases |
|---|---|---|---|
| **Go** | R1 and R2 pass. | Build the portal pilot as planned. | `EPIC-202` stories for `BR-04` and `BR-05` are committed as written, with the "as of" wording (A-03); `dotnet-r2` scope stays as in the Canonical Contract. |
| **Adjust** | R1 passes and R2 fails, or R1 fails and R2 passes, or R3 median is far below 35 %. | Change the design or the promise, then retest if cheap. For a failed R2: ask whether StockPilot's pick-up can run more than nightly without changing StockPilot (**OPEN:** O-16), or rename "Picking" so it is not misleading, or tell Lena Varga that `SM-02` needs a lower target (**OPEN:** O-04). For a failed R1: simplify the copy flow before `EPIC-202` is committed. | Acceptance criteria and wording of `BR-04` stories change; `SM-01` and `SM-02` targets are put back to Lena Varga (A-04, G-05). |
| **Stop** | Both R1 and R2 fail. | Do not commit the customer-facing portal stories (`EPIC-202`, `EPIC-203`) until the reason is understood. | `EPIC-201` parity work (a technical enabler) continues, because Order Desk must be modernised whatever the portal does (C-01, C-02). Lena Varga and Marc Dubois decide on the portal business case. |

#### 3.2.6 Constraints and vetting

* Constraints: C-05 (single source of truth for orders), NFR-03 (EU), NFR-07 (WCAG applies to the later portal, not to the prototype), ES-17 (no personal data in documents), ES-27.
* Vetting: the business driver is the portal's whole value (P-02 to P-04, SM-01 to SM-04). The problem is crisp. Next steps are written for each outcome. Lena Varga owns the backlog and can act. Responsible AI does not apply. Red-flag check: the prototype is a **test instrument**, not a demo to show off; it is thrown away after the sessions.
* Linked ids: BG-01, BG-05, BR-04, BR-05, BR-12, NFR-07, SM-01, SM-02, SM-03, P-02, P-03, P-04, CS-05, CS-10, C-05, A-03, A-04, A-10, A-35, T-01, T-06, X-04, X-06, G-04, G-05, OQ-01, OQ-02, O-04, O-05, O-16, O-26.

---

### MVE-03: Can a claims solution meet the connector rule and the cost cap?

| Field | Value |
|---|---|
| Business area and track | BA-03 Delivery claims and credit notes; `track-power-platform`; **no team and no release yet** (source: business-case section 4, ES-30, intake review G-08) |
| Experiment type | Architecture, licensing and cost feasibility (desk research and paper design) |
| Goals served (BRD section 4.1) | `BG-03` Delivery claims are faster and traceable (`SM-05`, `SM-06`; proposed goal owner Lena Varga) and `BG-04` run cost inside the caps (C-08; proposed goal owner Ahmed Benali). Goal owners are proposals, **OPEN:** O-26. |
| Dependencies and tensions in play | `X-20` Order Desk API, `X-21` order data contract, `X-22` endpoint reachable while data services stay private, `X-23` connector sign-in, `X-24` finance CSV drop and the share after the lease, `X-25` warehouse per order line, `X-27` governed environments, data loss prevention (DLP) and licensing; tensions `T-02` (C-07 versus ES-36 and the cap) and `T-07` (Q1 2027 claims pilot) |
| Measurement source and owner | The experiment's own records: the capability matrix, the date-stamped licence and price extract, and the cost arithmetic. Owner Ahmed Benali. The production sources for `SM-05` and `SM-06` do not exist yet (no claims launch, A-25, O-07) and are **OPEN:** O-26 (Lena Varga). |
| Status | Not run |

#### 3.3.1 Riskiest assumption

**ASSUMPTION (to be tested):** A claims solution can reach order lines only through a custom connector (ES-36). It keeps to the `NorthwindClaims` solution and dedicated environments (ES-34, ES-35). It stays within C-07 and EUR 900 a month for about 52 users (C-08). It also hands credit-note requests to a finance system that has no API by a CSV file (source: C-07, C-08, ES-34 to ES-36, CS-25, CS-27).

**Why this one is the riskiest.** If it fails, every BA-03 story fails with it. Usability, such as recording a claim in under 2 minutes (BR-14), is a lower risk and can be tested later.

| Evidence for | Evidence against |
|---|---|
| The 8 Antwerp supervisors have Entra ID accounts and Microsoft 365 E3 licences (source: CS-28). | C-07 allows standard connectors only; ES-36 requires a custom connector, which is premium (**ASSUMPTION:** A-22; source: research W#1, W#2, both secondary sources, medium confidence); this is tension T-02 (source: C-07, ES-36). |
| Claim capture, photos and a two-step approval are ordinary Power Apps and Power Automate scenarios (**ASSUMPTION:** A-34, general knowledge, not verified here) (source: BR-14, BR-15). | EUR 900 divided by 52 users is **EUR 17.31 per user per month** (source: C-08). Premium prices are not in the inputs; a sum above EUR 17.31 per user breaks C-08 (**ASSUMPTION:** A-22). |
| The CSV hand-off is simple: the finance system imports a CSV from `\\NWFS01\finance-import\` before 18:00 on working days (source: CS-25). | Order Desk has no API, and it is reachable only from the Lyon network (source: CS-27, CS-09, G-01). Nobody owns the API (**OPEN:** O-01). |
| Order data for a claim already exists: order number, customer, lines, quantities, prices, delivery address (source: `database/001-schema.sql`, `Orders` and `OrderLines`). | Writing to an on-premises share from a cloud flow needs a gateway or another bridge; where the share lives after 30 June 2027 is unknown (**OPEN:** O-15, X-24). |
| A design without a custom connector exists, for example a nightly snapshot of order lines into a list on standard connectors (research option C2) (source: research F5). | Only the default environment exists, with 23 personal apps and no data loss prevention policy (source: CS-26, ES-35). Dataverse may also need a premium licence (**ASSUMPTION:** A-23). |
| | The warehouse for each order line is not in the data, which BR-17 needs (source: C#10, A-18, X-25). |

**Alternatives considered and ranked lower:** testing the usability claim of BR-14 (under 2 minutes, 5 photos); that is a later experiment once feasibility is settled (source: research section (c)).

#### 3.3.2 Hypothesis

> We believe at least one design can meet ES-36 and the EUR 900 cap (C-08) for about 52 users. It must still hand credit-note requests to the finance system by CSV. We will test this on paper with a capability-to-licence matrix and a cost calculation for three design options. We will also check the order-line fields and the CSV hand-off. We will know we are **right** when at least one option passes all four checks below. We will know we are **wrong** when no option passes and no one with authority records a decision to relax C-07, C-08 or ES-36.

| Check | Pass threshold (**ASSUMPTION:** A-35) | Linked ids |
|---|---|---|
| **P3a** Licence class known | Every capability the five stories need (app, flow, approval, storage of claims and photos, custom connector, file hand-off) has a licence class (standard, premium, unknown) taken from Microsoft's primary licensing documentation: **0 capabilities left unknown**. | C-07, ES-34, A-22, A-23, MVE-A-08 |
| **P3b** Cost per user | Total monthly cost of licences, gateway or bridge and storage for about 52 users, divided by 52, is **at or below EUR 17.31** (900 divided by 52), with the arithmetic shown and prices date-stamped. | C-08, A-22, MVE-A-02 |
| **P3c** Order-line path | The order-line read goes through a custom connector described in OpenAPI 2.0 (ES-36), and every field a claim needs is in the contract or listed as missing with an owner: order number, customer, line number, SKU, product name, quantity, unit price, line total, delivery address are in `Orders` and `OrderLines`; warehouse per line is **not** (A-18, X-25). | BR-14, BR-17, ES-33, ES-36, X-20, X-21, G-01 |
| **P3d** Finance hand-off | A route is described by which a CSV reaches `\\NWFS01\finance-import\` before 18:00 without changing the finance system, with any extra cost counted in P3b, and the route still works after the lease (or the gap is an **OPEN:** item with an owner). | BR-16, CS-25, C-01, X-24, O-15, MVE-O-04 |

Three options are compared (labels are local to this document; they correspond to the research options C1 to C3, where C2 is the snapshot design and C3 the premium design):

| Option | Idea | Expected tension |
|---|---|---|
| **D1** Premium for everyone | Custom connector, Dataverse and flows, premium licence for all 52 users (research C3) | Likely above EUR 17.31 per user; breaks C-07 (**ASSUMPTION:** A-22) |
| **D2** Snapshot on standard connectors | Nightly snapshot of order lines into a list, no custom connector, no Dataverse (research C2) | Fits C-07 and C-08 but departs from ES-36 and shows stale order data; needs a decision record |
| **D3** Mixed | Premium only for the few users who need a premium component; the rest use standard components | Depends on a licensing rule that is unverified (**ASSUMPTION:** MVE-A-09) |

Verdict rule: **pass** needs P3a to P3d on one option. If the only passing option departs from ES-36, C-07 or C-08, the result is **adjust**, because the departure needs a recorded decision by the owner of that rule (**OPEN:** O-02, owner Ahmed Benali; Marc Dubois for money).

#### 3.3.3 Smallest experiment

| Item | Plan |
|---|---|
| Method | Desk research and paper design. No tenant, environment, connector or app is created, imported or changed (source: ES-37). |
| Who | An IT team member with a licensing adviser. There is no BA-03 team, so the person is **OPEN:** MVE-O-03 (related to O-07, G-08). Julien Moreau answers the CSV and finance questions. |
| Data | Business case BR-14 to BR-19 and NFR-09; CS-24 to CS-28; `database/001-schema.sql` (`Orders`, `OrderLines`); Microsoft's published licensing guide and price list (primary sources, read in full, because the research used two secondary sources). |
| Time-box | 5 working days elapsed. |
| Effort | About 4 person-days (**ASSUMPTION:** MVE-A-01). |
| Owner | Ahmed Benali (feasibility). Lena Varga records the backlog decision. |

Steps:

1. **Capability matrix (1 day).** For each of these, list the components needed and give each a licence class from the primary Microsoft documentation: BR-14 (record a claim, up to 5 photos), BR-15 (approval above EUR 500, no self-approval), BR-16 (credit-note request), BR-17 (warehouse view) and BR-18 (dashboard). Anything unread stays marked unknown and fails P3a.
2. **Cost (1 day).** For options D1, D2 and D3, compute total monthly cost and cost per user for 38 Order Desk staff, 6 Finance staff and 8 warehouse supervisors (source: C-08). Date-stamp every price (MVE-A-02). The break-even is EUR 17.31.
3. **Order-line contract field check (1 day).** Write the fields claims need next to the fields available in `Orders` and `OrderLines`. List what is missing (warehouse per line, delivery date, customer e-mail, X-25, X-26). The OpenAPI 2.0 file itself is the enabler `EP-03` and is **not** written here.
4. **CSV hand-off options (1 day).** Describe two or three ways to get a CSV to `\\NWFS01\finance-import\`: a data gateway, a file-sync agent on the Lyon network, or a finance-side pick-up from a shared location. State cost, owner and what happens after 30 June 2027 (**OPEN:** MVE-O-04, O-15).
5. **Review and decide (1 day).** Ahmed Benali and Lena Varga review P3a to P3d and record go, adjust or stop. They put any proposed relaxation of C-07, C-08 or ES-36 to its owner as a decision request.

#### 3.3.4 What is explicitly NOT being built

* No Power Platform environment, solution, app, flow, connection, data loss prevention policy or licence assignment (ES-37, ES-35).
* No custom connector file, no import into any tenant (`EP-03` and `powerplatform/` are later work, ES-33).
* No Order Desk API and no change to `src/` or `database/` (O-01, ES-36).
* No change to the finance system and no CSV written to `\\NWFS01\finance-import\` (business-case section 6).
* No migration of the 9,400 spreadsheet rows (OQ-05, A-14).
* No usability test of BR-14 (a later experiment).

#### 3.3.5 Success and failure criteria, and the decision they unlock

| Result | Criteria | Decision | What changes in the backlog |
|---|---|---|---|
| **Go** | One option passes P3a to P3d without relaxing any rule, or with a relaxation already agreed by its owner. | Keep BA-03 as designed; `EP-04` records the licence and cost decision. | `EPIC-301` enablers `EP-03`, `EP-04`, `EP-05` get a concrete design; `EPIC-302` to `EPIC-304` stay unplanned until O-07 names a team and a date. |
| **Adjust** | Only D2 (or another option that departs from ES-36, C-07 or C-08) passes. | Put a decision request to the owner of the rule (O-02): an exception to ES-36 with a decision record, a higher C-08, or relaxed C-07. | `EP-04` becomes the decision record; stories for `BR-14` and `BR-16` carry the chosen design; `BR-17` and `BR-18` are re-checked against the cost. |
| **Stop** | No option passes and no decision to relax is obtained. | BA-03 build stays unplanned and the Q1 2027 claims pilot is taken out of the plan (A-25). | `EPIC-301` to `EPIC-304` stay unplanned; Lena Varga and Marc Dubois decide whether to change the claims process some other way. |

A pass here proves a **design on paper**, not a working claims app. Acceptance wording for BA-03 stays "design validated locally" (source: plan risk table, ES-37).

#### 3.3.6 Constraints and vetting

* Constraints: C-07, C-08, NFR-03 (Europe), NFR-04, NFR-09, ES-33 to ES-37, CS-26 (no governed environments yet).
* Vetting: the business driver is the claims pilot and the cost cap (SM-05, SM-06, C-08). The problem is crisp. Both outcomes have a next step. **Red flag, stated plainly:** the customer has no team, no date and no licence decision for BA-03 (G-08, O-02, O-07), which is a low-commitment and no-follow-through risk. The experiment is cheap and its result may be "stop". The owners must accept that before it starts. Responsible AI does not apply.
* Linked ids: BG-03, BG-04, BG-05, BR-14, BR-15, BR-16, BR-17, BR-18, NFR-03, NFR-04, NFR-09, C-07, C-08, SM-05, SM-06, CS-24, CS-25, CS-26, CS-27, CS-28, ES-32 to ES-37, A-18, A-22, A-23, A-25, A-34, A-35, T-02, T-07, T-09, X-20 to X-27, G-01, G-02, G-08, OQ-04, OQ-05, O-01, O-02, O-07, O-15, O-26.

## 4. Rejected candidate experiments

| Candidate | Why it was not chosen | Source |
|---|---|---|
| Deploy a trial Azure SQL Managed Instance or database to measure cost and speed | Forbidden: nothing is deployed from this workshop. A calculator and documentation give the answer needed for a go, adjust or stop decision. | ES-27 |
| Import a trial custom connector into a Power Platform environment | Forbidden: nothing is created or changed in a tenant. | ES-37 |
| Rehearse the migration inside the 6-hour Sunday window | Likely feasible by log-based restore from existing backups; lower risk than the exchange and the cap. Belongs to `EA-13`, `EA-16` and `azure-r3`. | BR-13, CS-21, A-33 |
| Rehost the unchanged app on a Windows VM | A contingency, not the plan; kept as the fallback in MVE-01 "adjust". | A-20, O-03 |
| Compare customer identity providers | Sign-in is provider-neutral until OQ-01 is answered; the technology risk is lower than customer behaviour. | OQ-01, A-10 |
| Audit the portal against WCAG 2.2 AA | Standard practice; nothing to test before screens exist. | NFR-07 |
| Time a claim being recorded (BR-14 under 2 minutes, 5 photos) | A usability test is only worth running once feasibility and licensing are settled (MVE-03). | BR-14 |
| Build a working portal or claims app as an "experiment" | Red flags: demo, mini-MVP and production code expectations. It would not isolate one assumption. | ES-37 |

## 5. ASSUMPTION and OPEN registers

Ids from the Canonical Contract C9 and the research are reused unchanged. Ids that start with `MVE-` are new and local to this document; the coordinator may renumber them if they are promoted to the shared register. Every A- and O- id cited in this document has a row below. The registers in the business requirements document ([business-requirements.md](business-requirements.md) sections 12 and 13) are the register of record for the full list.

### 5.1 ASSUMPTION register

| Id | ASSUMPTION | Used in | Confirming owner |
|---|---|---|---|
| A-09 | MVEs are local, prototype or paper-based. | Section 1 | Lena Varga |
| A-10 | Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. | MVE-02 | Ahmed Benali |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | MVE-01 | Ahmed Benali |
| A-21 | A managed database service (PaaS, platform as a service) is the preferred data-tier direction. A virtual machine is the fallback. | MVE-01 | Ahmed Benali |
| A-22 | Premium Power Platform licences are needed for custom connectors and may exceed EUR 17.31 per user per month. Prices are unverified. | MVE-03 | Ahmed Benali |
| A-23 | Dataverse use also needs a premium licence outside the Teams environment. | MVE-03 | Ahmed Benali |
| A-24 | Azure runs in Coordinated Universal Time (UTC) by default. Order Desk stores local time. Parity needs explicit handling. | MVE-01 | Ahmed Benali |
| A-25 | The Q1 2027 claims pilot cannot be committed while BA-03 has no team. | MVE-03 | Lena Varga, Marc Dubois |
| A-27 | The StockPilot CSV contract and file pick-up stay as they are. | MVE-01 | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | MVE-01 | Ahmed Benali |
| A-31 | Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). | MVE-01 | Ahmed Benali |
| A-32 | Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. | MVE-01 | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Section 4 | Ahmed Benali |
| A-34 | Claim capture with photos and two-step approval is feasible with standard Power Apps and Power Automate features. | MVE-03 | Ahmed Benali |
| A-35 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | All | Lena Varga |
| A-03 | BR-04: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. BR-09 follows the same rule. | MVE-02 | Lena Varga |
| A-04 | "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot. | MVE-02 | Lena Varga |
| A-14 | Spreadsheet migration is a separate unplanned item. | Section 3.3.4 | Lena Varga, Julien Moreau |
| A-18 | The warehouse for each claim line can be derived from StockPilot or product data. It is not on order lines. | MVE-03 | Pieter Janssens |
| MVE-A-01 | The effort (about 4 person-days each) and the elapsed times in this document are planning estimates; the inputs give no sizing basis. | All | Ahmed Benali (MVE-01, MVE-03), Lena Varga (MVE-02) |
| MVE-A-02 | Public price lists (Azure pricing calculator, Microsoft licensing guide) are an adequate basis for indicative monthly figures; prices change, so each is date-stamped. | MVE-01, MVE-03 | Ahmed Benali |
| MVE-A-03 | Growth stays linear. From mid-November 2026 to 30 June 2027 is 7 to 7.5 months. The database then reaches about 56 GB (48 GB plus 7.5 months at 1 GB) and invoices about 135 GB (120 GB plus 7.5 months at 2 GB). The month count is itself an assumption, and the date of the 48 GB and 120 GB figures is not stated. | MVE-01 | Ahmed Benali |
| MVE-A-04 | A local SQL Server (Developer edition or container) is available to the experimenter to run the database scripts. | MVE-01 | Ahmed Benali |
| MVE-A-05 | Stated intent overstates real behaviour, and 5 to 8 participants give a signal and not statistical proof. The sample of 5 to 8 customers is a design choice, not a source fact. The R2 threshold of 60 % is set above the 39 % that `SM-02` needs to compensate. | MVE-02 | Lena Varga |
| MVE-A-06 | The checks in this document (M1a to M1c, R1 to R3, P3a to P3d) are leading indicators. Passing one does not show that a success measure (`SM-nn`) or goal (`BG-nn`) is met. The production measurement source and owner for each measure stay **OPEN:** O-26. | All | Lena Varga |
| MVE-A-07 | Backup frequency and point-in-time restore for each Azure SQL option come from public Microsoft documentation and are not verified here. | MVE-01 | Ahmed Benali |
| MVE-A-08 | The licence class of each Power Platform capability is read from Microsoft's primary licensing documentation at experiment time; until then, every class is an assumption. | MVE-03 | Ahmed Benali |
| MVE-A-09 | Whether a flow can run under a shared or service identity without a premium licence for every user is unknown; option D3 depends on it. | MVE-03 | Ahmed Benali |

### 5.2 OPEN register

| Id | OPEN | Owner |
|---|---|---|
| O-01 | Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? (G-01) | Ahmed Benali |
| O-02 | Does BA-03 need a premium licence, a data gateway or a custom connector inside C-07 and C-08? Is Dataverse used? (G-02) | Ahmed Benali |
| O-03 | Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (G-03) | Ahmed Benali |
| O-04 | What status freshness is acceptable, given the nightly batch? (G-04) | Lena Varga |
| O-05 | Does "portal launch" mean the pilot or general availability? (G-05) | Lena Varga |
| O-07 | Who is the BA-03 team, what are their skills, and what is the intended date (or is BA-03 unplanned)? (G-08) | Lena Varga, Marc Dubois |
| O-10 | Which identity provider do customer users use (OQ-01)? | Ahmed Benali |
| O-11 | Must Dutch be in the first release (OQ-02)? | Sofie Peeters, Lena Varga |
| O-13 | Who approves claims of EUR 500 or less (OQ-04)? | Julien Moreau, Lena Varga |
| O-14 | Must the claims already in the spreadsheet be moved to the new solution (OQ-05)? | Lena Varga, Julien Moreau |
| O-15 | Where do the finance system, the `NWFS01` shares (`claims.xlsx`, `finance-import`, invoices), the domain controllers and the Antwerp file-transfer (SFTP) route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-16 | How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? | Ahmed Benali, Pieter Janssens |
| O-21 | Approval and funding to build (the status says "not yet approved for build"). | Marc Dubois |
| O-26 | Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. | Lena Varga |
| MVE-O-01 | Which person from the IT team runs MVE-01 with the adviser. | Ahmed Benali |
| MVE-O-02 | Who facilitates the MVE-02 sessions, and in which languages (French, Dutch, English); which 5 to 8 customers take part. The wider question of who speaks for customer users is O-26. | Lena Varga, Sofie Peeters |
| MVE-O-03 | Who runs MVE-03, given that BA-03 has no team (related to O-07, G-08). | Ahmed Benali, Lena Varga |
| MVE-O-04 | How a CSV made in the cloud reaches `\\NWFS01\finance-import\` before 18:00: a gateway, a file-sync agent on the Lyon network, or a finance-side pick-up; and who runs and pays for it (related to O-15, X-24). | Julien Moreau, Ahmed Benali |
| MVE-O-05 | Where are the SQL Server Agent job "NW - StockPilot nightly" and the Windows scheduled task that copies files to the Antwerp SFTP server defined? They are not in the repository. | Ahmed Benali |
| MVE-O-06 | Start dates for the three experiments, so results arrive before the gated epics are committed. | Lena Varga, Marc Dubois |

Gaps carried, with their ids unchanged from the intake review and the BRD (section 13.3): G-01 (no owner for the Order Desk API), G-02 (Power Platform licensing conflict), G-03 (Azure and .NET boundary), G-04 (status freshness), G-05 (testability, "portal launch"), G-08 (no BA-03 team or release), G-09 (missing data facts). Business-case open questions OQ-01, OQ-02, OQ-04 and OQ-05 are referenced above, carried in the BRD as O-10, O-11, O-13 and O-14; none is answered by this document.

### 5.3 Goals, dependencies and tensions cited

Ids and meaning are as in the BRD (sections 4.1, 11.1 and 11.2). Nothing is redefined here.

| Id | Meaning (short) | Cited in |
|---|---|---|
| BG-01 | Customers serve themselves | MVE-02 |
| BG-02 | Order Desk runs in Azure before 30 June 2027 | MVE-01 |
| BG-03 | Delivery claims are faster and traceable | MVE-03 |
| BG-04 | Run cost stays inside the caps C-04 and C-08 | MVE-01, MVE-03 |
| BG-05 | Customer data protected, audit trail kept | MVE-01 (linked), MVE-02 (linked), MVE-03 (linked) |
| X-04, X-06 | Staff and customer sign-in; status freshness bounded by the exchange cadence | MVE-02 |
| X-05, X-12, X-15 | Exchange redesign for a managed database; shared cap C-04; 7-year audit trail in Azure | MVE-01 |
| X-20 to X-25, X-27 | Order Desk API and data contract; endpoint reachability; connector sign-in; finance CSV drop; warehouse per line; environments, DLP and licensing | MVE-03 |
| T-01, T-06 | "Always up to date" versus the nightly update; "portal launch" versus a 20-customer pilot | MVE-02 |
| T-02, T-07 | C-07 versus ES-36 and the cap; Q1 2027 claims pilot without a team | MVE-03 |
| T-03, T-05, T-14 | Shared cap C-04 has no single owner; exchange on `xp_cmdshell` versus the date; recovery never tested | MVE-01 |
| X-02, X-03, T-04, T-13, T-09 | Documented configuration and identity contract; database sign-in; "a track never waits"; audit-row accuracy; Power Platform skills | MVE-01 (X-02, X-03, T-04, T-13, linked); MVE-03 (T-09, linked) |

## 6. Safety statement

* No experiment in this document deploys anything, creates a resource in an Azure subscription, or creates, imports or changes anything in a Power Platform environment or tenant (source: ES-27, ES-37).
* No file in `src/`, `database/` or `knowledge-docs/` is changed by this document or by the experiments. Throwaway scripts and prototypes are not committed.
* No secrets, no real customer data and no personal data are used or recorded; interview notes are anonymised (source: ES-17, NFR-03, NFR-05).
* Customer contact for MVE-02 is arranged by Lena Varga and Sofie Peeters only.
* No Git tag and no commit result from this document; planned tags such as `product/azure-r1` do not exist (source: ES-31).
* The experiments have not been run. Nothing here is a result.
