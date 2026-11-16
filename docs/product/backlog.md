---
backlog_id: "BACKLOG-NW-001"
title: "Northwind Traders: prioritised backlog for the Customer Portal, the Order Desk move to Azure and delivery claims"
status: "draft"
version: "0.1.0"
owners: ["Lena Varga"]
reviewers: ["Marc Dubois", "Ahmed Benali"]
created_date: "2026-11-15"
last_updated: "2026-11-15"
source_prd_id: "PRD-NW-001"
source_prd_path: "docs/product/product-requirements.md"
source_brd_id: "BRD-NW-001"
source_experiments_path: "docs/product/experiments.md"
scope: ["BA-01", "BA-02", "BA-03"]
tracker_published: false
---

# Northwind Traders: prioritised backlog

> **BACKLOG-NW-001** | Status: **Draft for review** | Version 0.1.0 | Last updated 2026-11-15
>
> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> This is a document, a file-based backlog. **Nothing has been published to Azure DevOps, GitHub or Jira** (O-06 names no tool). Nothing is built, deployed or changed in any tenant (ES-27, ES-37).

## 1. How to read this backlog

This backlog turns the product requirements (`PRD-NW-001`, `docs/product/product-requirements.md`) into epics, features, user stories and enabler stories that a delivery team can build from. A developer who has not read the business case should be able to build each story from its own text (ES-05).

* **Source cites (ES-02).** Every item says where it comes from, for example `(source: BR-05, CS-10)`. `BR-` is a business requirement, `NFR-` a quality requirement (a quality the solution must have), `C-` a constraint, `SM-` a success measure, `CS-` a current-state fact, `ES-` an engineering standard, `OQ-` an open question from the business case. `FR-` is a product functional requirement from the PRD. Source ids are quoted exactly and never renumbered.
* **ASSUMPTION: and OPEN: (ES-03, ES-04).** Anything not stated in `knowledge-docs` is marked **ASSUMPTION:** and listed in section 7 with a confirming owner. Every unanswered question is marked **OPEN:** and listed in section 7 with the person who can answer it.
* **Item types.** An *epic* groups features. A *feature* groups stories. A *story* is written *As a ... I want ... so that ...*. An *enabler* (`EA-nn` Azure, `EN-nn` .NET, `EP-nn` Power Platform) is a story with a technical role: technical work that stories need first (G-10). Enablers are stories in this backlog.
* **Acceptance criteria.** Each is written *Given / When / Then* (GWT) and has the id `<item id>/AC<n>`, for example `STORY-230/AC2`. Every story and enabler has at least two, including a failure or edge case where one is meaningful.
* **"Design validated locally".** For the Azure and Power Platform tracks, "done" means a reviewed design set that passes local validation (for example `az bicep build`), never a deployment or a change in a tenant (ES-27, ES-37). Acceptance wording says so.
* **Experiment gates.** A *gate* is a minimum viable experiment (MVE, the smallest test that can prove an assumption wrong) whose decision (go, adjust or stop) is taken **before** the gated item is committed (source: `docs/product/experiments.md`). A gate is a decision point, not a release wait. **No experiment has been run; every result is pending.** Items show `Gate: MVE-nn` where it applies.
* **Status of every item** is *Draft for review*. Nothing here is approved or committed (O-21).
* **Additions after the first review (A-59).** `FEAT-113`, `FEAT-114`, `EA-15` and `EA-16` were added after the first review. `FEAT-113` and `FEAT-114` sit outside the feature id ranges first reserved for their epics (`FEAT-106` to `FEAT-109` for `EPIC-103`, `FEAT-110` to `FEAT-112` for `EPIC-104`); those ranges are extended to include them. Ids are never reused. `EA-15` and `EA-16` are design items: infrastructure code and procedures, checked locally. Nothing is applied in Azure (ES-27).

Terms used in the items: *RPO* (recovery point objective) is how much recent data may be lost; *RTO* (recovery time objective) is how long recovery may take; *PaaS* is a managed platform service; *IaC* is infrastructure written as code; *DLP* is a data loss prevention policy; *WCAG* is the Web Content Accessibility Guidelines; *ESU* is paid Extended Security Updates; *SFTP* is a secure file-transfer service; *CSV* is a plain comma-separated file; *p95* is the 95th percentile (95 of 100 requests are at least this fast); *CET* is Central European Time; *OpenAPI 2.0* is a standard file format that describes a web API.

### 1.1 Canonical release table

This table is the canonical release proposal and is identical in every product document (PRD section 6.2). Target windows are targets, not commitments (A-01, A-42). **OPEN:** O-25 asks Lena Varga and Marc Dubois to confirm the release counts, windows and placements.

| Track | Release | Theme | Target window | Main epics | BR / NFR covered | What it leaves out |
|-------|---------|-------|---------------|-----------|------------------|--------------------|
| Azure (`track-azure`) | `azure-r1` | Foundation, data platform decision and cost proof | 1 Dec 2026 to 29 Jan 2027 | `EPIC-101`, `EPIC-102` | NFR-03 (Azure), NFR-05 (Azure); supports C-01, C-02, C-04, C-06 | Exchange redesign, hosting runtime, pilot environment, monitoring, recovery, cutover, `BR-13` |
| Azure | `azure-r2` | Pilot environment, exchange and storage, observability | 1 Feb to 31 Mar 2027 | `EPIC-103` | NFR-01 (design and alerting), NFR-06 (design), NFR-08 (retention design); supports C-03, C-04 | Cutover rehearsal and runbooks, recovery proof, `BR-13`, decommission |
| Azure | `azure-r3` | Cutover and recovery proof | 1 Apr to 27 June 2027 | `EPIC-104` | BR-13; NFR-01 (proof), NFR-06 (proof); supports SM-07, C-01, C-02 | Optimisation after the lease (unplanned items) |
| .NET (`track-dotnet`) | `dotnet-r1` | Modernised Order Desk with behavioural parity | 1 Dec 2026 to 26 Feb 2027 | `EPIC-201` | NFR-04 (staff), NFR-05 (.NET), BR-10 (parity), BR-12 (parity) | Everything customer-facing, `EN-11`, `EN-07`, `EN-14` |
| .NET | `dotnet-r2` | Portal pilot (Must items) for 20 customers | 1 Mar to 30 Apr 2027 | `EPIC-202` | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-10 (portal value), BR-11 (French and English), BR-12 (customer prices); NFR-02, NFR-03 (.NET), NFR-04 (customers), NFR-07, NFR-08 (content) | Invoices (`BR-07`), user administration (`BR-08`), e-mail (`BR-09`), Dutch, Order Desk API implementation |
| .NET | `dotnet-r3` | Complete portal and API contract (general availability, A-04) | 1 May to 30 Sep 2027 | `EPIC-203` | BR-07, BR-08, BR-09, BR-11 (Dutch); SM-01 to SM-04 instrumentation | Order Desk API implementation (`EPIC-204`, unplanned until O-01), all BA-03 items |
| Power Platform (`track-power-platform`) | none | No release: no team (G-08, O-07) | none | `EPIC-301` to `EPIC-304` (unplanned) | BR-14 to BR-19, NFR-03 (BA-03), NFR-04 (BA-03), NFR-09: documented, tagged by track only | The Q1 2027 claims pilot cannot be committed (A-25) |

**ASSUMPTION:** A-58 (owner Marc Dubois) extends the `azure-r3` target window to 27 June 2027, so that the rehearsal Sundays (6 and 13 June 2027) and the live cutover and fallback Sundays (20 and 27 June 2027) fall inside it. This leaves 3 days before the lease ends (C-01). **OPEN:** O-27 asks Marc Dubois to confirm the extended window and the 3-day margin.

Release counts: **Azure 3, .NET 3, Power Platform 0**. **A release never waits for another track** (ES-31): a need from another track is an **OPEN:** `X-nn` row in the item and in the release file of the needing track (A-45). The planned Git tags `product/<track>-r<n>` are text only and **not yet created** (A-39).

### 1.2 Tag legend

| Tag | Meaning | Where it appears |
|---|---|---|
| `track-azure` | Delivered by the Azure team (BA-01). Ids `EPIC-1nn`, `FEAT-1nn`, `STORY-1nn`, `EA-nn`. | Exactly one track tag on every epic, feature, story and enabler (ES-30). |
| `track-dotnet` | Delivered by the .NET team (BA-02). Ids `EPIC-2nn`, `FEAT-2nn`, `STORY-2nn`, `EN-nn`. | Same. |
| `track-power-platform` | Delivered by the Power Platform team (BA-03). Ids `EPIC-3nn`, `FEAT-3nn`, `STORY-3nn`, `EP-nn`. No team exists yet (O-07). | Same. |
| `azure-r1`, `azure-r2`, `azure-r3` | Release tag for items planned in that Azure release (ES-31). | Planned Azure items only. At most one release tag per item. |
| `dotnet-r1`, `dotnet-r2`, `dotnet-r3` | Release tag for items planned in that .NET release. | Planned .NET items only. |
| (no release tag) | The item is **unplanned**: it carries only its track tag. The Release column shows `unplanned`. | All BA-03 items and `EPIC-204`. |

Rules: a story that needs two tracks is split into one story per track (ES-30); a story that spans two releases is split into one story per release (ES-31). An epic or feature sits entirely inside one release, or entirely unplanned, so its release tag equals the tag of every child. The release tag's track always equals the track tag. The id block matches the track: 1xx Azure, 2xx .NET, 3xx Power Platform.

### 1.3 Priority method

| Rule | How it is applied | Source |
|---|---|---|
| MoSCoW from the business requirements | A story that serves a `BR-` takes that `BR-` priority from the business case: Must, Should or Could. There is no Won't item. | BR-01 to BR-19; A-06 |
| Quality requirements are Must | A story that serves an `NFR-` is Must, because the business case gives the NFRs no priority. | A-06 |
| Enabler rule (A-49) | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must. An enabler that serves only another track's requirements is Should. | A-49 |
| Epics and features | Take the highest priority of their children. | this backlog |
| Rank within a track | Releases in order (r1, r2, r3, then unplanned). Inside a release, enablers come before the stories that need them, then Must, Should, Could, then date risk. Rank is a whole number, 1 is first, and is set for stories and enablers only. Document order equals rank order. Every enabler ranks before every story it serves. | A-46 |
| BA-03 bands | P1, P2 and P3 are shown next to the priority. They are a **priority band, not a release tag** and not a tag at all. P1 = Must, P2 = Should, P3 = Could. | A-36 |
| Not set | `FR-314` (spreadsheet claims migration) has no priority until O-14 is answered. | O-14 |

### 1.4 Backlog authoring decisions

**ASSUMPTION:** A-55 holds these decisions, owner Lena Varga. They do not change any requirement.

| Id | Decision |
|---|---|
| BD-01 | One story per product functional requirement: the 57 `FR-` items of the PRD become 57 stories. Each story names the `FR-` it implements and keeps that requirement's source ids, priority and release. |
| BD-02 | An enabler and a story can share one subject (for example `EA-01` and `STORY-101`). The **enabler** is the technical work (the thing is built or designed). The **story** is the outcome that a stakeholder reviews and accepts. Their criteria differ. |
| BD-03 | The PRD gives ranges of feature ids per epic (PRD section 6.5). This backlog decides which feature holds which story and enabler. All `EP-01` to `EP-06` sit under `EPIC-301` (PRD section 16.2). |
| BD-04 | Item titles are plain text of at most 100 characters, so they work in Azure DevOps, GitHub and Jira. The published form is `<id> <title>` (ES-28, ES-29). |
| BD-05 | Where acceptance criteria need a number, the number comes from a source id. Where a source gives none, the criterion says so and points to an **OPEN:** item instead of inventing one. |

### 1.5 Where to find things

Section 2 is the item register. Section 3 has counts. Section 4 holds every item in rank order: 4.1 Azure, 4.2 .NET, 4.3 Power Platform. Section 5 lists the unplanned items. Section 6 maps tags to Azure DevOps, GitHub and Jira (ES-39) and lists every item with its published title. Section 7 holds the ASSUMPTION and OPEN registers. The story-level traceability is [traceability.md](traceability.md).

## 2. Item register

One row per item (144 items: 12 epics, 39 features, 57 stories, 36 enablers). Epics and features show `—` for rank. Release `unplanned` means the item carries only its track tag. Enablers have type *enabler*. Priority for BA-03 shows the band (A-36).

### 2.1 Azure (`track-azure`)

| Id | Type | Title | Track tag | Release tag | Priority | Rank |
|---|---|---|---|---|---|---|
| EPIC-101 | epic | Azure foundation and security baseline | `track-azure` | `azure-r1` | Must | — |
| FEAT-101 | feature | Environment foundation as code and validation | `track-azure` | `azure-r1` | Must | — |
| EA-01 | enabler | Build the Azure foundation as code (naming, tags, region, modules) | `track-azure` | `azure-r1` | Must | 1 |
| EA-11 | enabler | Build the infrastructure validation and deployment pipeline design | `track-azure` | `azure-r1` | Must | 2 |
| STORY-101 | story | Review a test and production environment design set | `track-azure` | `azure-r1` | Must | 3 |
| STORY-104 | story | Keep every Azure resource in an EU region | `track-azure` | `azure-r1` | Must | 4 |
| STORY-105 | story | Validate every infrastructure definition locally before release | `track-azure` | `azure-r1` | Must | 5 |
| FEAT-102 | feature | Hybrid connectivity design | `track-azure` | `azure-r1` | Must | — |
| EA-02 | enabler | Design hybrid connectivity between Lyon, Azure and Antwerp | `track-azure` | `azure-r1` | Must | 6 |
| STORY-102 | story | Agree the connection design for the move and after the lease | `track-azure` | `azure-r1` | Must | 7 |
| FEAT-103 | feature | Secrets, identity and private access | `track-azure` | `azure-r1` | Must | — |
| EA-03 | enabler | Design secrets, managed identities and private endpoints | `track-azure` | `azure-r1` | Must | 8 |
| STORY-103 | story | Keep secrets out of Azure-hosted code and configuration | `track-azure` | `azure-r1` | Must | 9 |
| EPIC-102 | epic | Data platform decision, cost and migration approach | `track-azure` | `azure-r1` | Must | — |
| FEAT-104 | feature | Data tier decision | `track-azure` | `azure-r1` | Must | — |
| EA-05 | enabler | Record the data-tier decision and migration approach | `track-azure` | `azure-r1` | Must | 10 |
| STORY-120 | story | Decide the data tier for the order database | `track-azure` | `azure-r1` | Must | 11 |
| FEAT-105 | feature | Cost model and migration approach | `track-azure` | `azure-r1` | Must | — |
| EA-09 | enabler | Build the Azure cost model against the monthly cap | `track-azure` | `azure-r1` | Must | 12 |
| STORY-121 | story | Show the monthly cost against the EUR 1,500 cap | `track-azure` | `azure-r1` | Must | 13 |
| STORY-122 | story | Define the database and invoice migration approach | `track-azure` | `azure-r1` | Must | 14 |
| EPIC-103 | epic | Pilot environment, exchange, storage and observability | `track-azure` | `azure-r2` | Must | — |
| FEAT-113 | feature | Application hosting | `track-azure` | `azure-r2` | Must | — |
| EA-15 | enabler | Host the Order Desk web application in the test and production environments | `track-azure` | `azure-r2` | Must | 15 |
| FEAT-106 | feature | StockPilot exchange, invoice storage and outbound mail | `track-azure` | `azure-r2` | Must | — |
| EA-06 | enabler | Redesign the StockPilot exchange without changing the file contract | `track-azure` | `azure-r2` | Must | 16 |
| EA-07 | enabler | Design invoice storage and synchronisation | `track-azure` | `azure-r2` | Should | 17 |
| EA-12 | enabler | Design outbound mail to replace the on-premises relay | `track-azure` | `azure-r2` | Should | 18 |
| STORY-140 | story | Keep the nightly StockPilot exchange working after the database moves | `track-azure` | `azure-r2` | Must | 19 |
| STORY-141 | story | Decide where invoice files live after the lease | `track-azure` | `azure-r2` | Should | 20 |
| STORY-144 | story | Replace the on-premises mail relay for outbound e-mail | `track-azure` | `azure-r2` | Could | 21 |
| FEAT-107 | feature | Observability and alerting | `track-azure` | `azure-r2` | Must | — |
| EA-04 | enabler | Build observability: log workspace, application monitoring and alerts | `track-azure` | `azure-r2` | Must | 22 |
| STORY-142 | story | Monitor availability with a synthetic probe and alerts | `track-azure` | `azure-r2` | Must | 23 |
| FEAT-108 | feature | Test environment for the portal pilot | `track-azure` | `azure-r2` | Must | — |
| EA-10 | enabler | Define the tst environment | `track-azure` | `azure-r2` | Must | 24 |
| STORY-143 | story | Define a test environment where the portal pilot can run | `track-azure` | `azure-r2` | Must | 25 |
| FEAT-109 | feature | Backup, retention and recovery design | `track-azure` | `azure-r2` | Must | — |
| EA-08 | enabler | Design backup, long-term retention and recovery | `track-azure` | `azure-r2` | Must | 26 |
| STORY-145 | story | Keep order-change records for 7 years in Azure | `track-azure` | `azure-r2` | Must | 27 |
| STORY-146 | story | Design backup and recovery for RPO 1 hour and RTO 4 hours | `track-azure` | `azure-r2` | Must | 28 |
| EPIC-104 | epic | Cutover and recovery proof | `track-azure` | `azure-r3` | Must | — |
| FEAT-114 | feature | Database migration and rehearsal | `track-azure` | `azure-r3` | Must | — |
| EA-16 | enabler | Migrate the NorthwindOrders database to the chosen data tier and rehearse the move | `track-azure` | `azure-r3` | Must | 29 |
| FEAT-110 | feature | Cutover and rollback runbooks | `track-azure` | `azure-r3` | Must | — |
| EA-13 | enabler | Write cutover, rollback and decommission runbooks | `track-azure` | `azure-r3` | Must | 30 |
| STORY-170 | story | Keep staff working through the cutover inside the Sunday window | `track-azure` | `azure-r3` | Must | 31 |
| STORY-171 | story | Define rollback and rehearsal for every cutover step | `track-azure` | `azure-r3` | Must | 32 |
| FEAT-111 | feature | Recovery and availability proof | `track-azure` | `azure-r3` | Must | — |
| EA-14 | enabler | Write the first recovery test plan and evidence template | `track-azure` | `azure-r3` | Must | 33 |
| STORY-172 | story | Prove recovery against RPO 1 hour and RTO 4 hours | `track-azure` | `azure-r3` | Must | 34 |
| STORY-173 | story | Plan the availability proof for the first weeks in Azure | `track-azure` | `azure-r3` | Must | 35 |
| FEAT-112 | feature | Decommission of the old servers | `track-azure` | `azure-r3` | Must | — |
| STORY-174 | story | Retire the old web and database servers before 30 June 2027 | `track-azure` | `azure-r3` | Must | 36 |

### 2.2 .NET (`track-dotnet`)

| Id | Type | Title | Track tag | Release tag | Priority | Rank |
|---|---|---|---|---|---|---|
| EPIC-201 | epic | Modernise Order Desk to .NET 10 with parity | `track-dotnet` | `dotnet-r1` | Must | — |
| FEAT-201 | feature | Modernise projects and web layer | `track-dotnet` | `dotnet-r1` | Must | — |
| EN-01 | enabler | Convert the solution to SDK-style projects on net10.0 | `track-dotnet` | `dotnet-r1` | Must | 1 |
| EN-13 | enabler | Record the decision on portal and API project shape | `track-dotnet` | `dotnet-r1` | Must | 2 |
| EN-03 | enabler | Replace direct ConfigurationManager calls with the options pattern | `track-dotnet` | `dotnet-r1` | Must | 3 |
| EN-05 | enabler | Replace the Windows Event Log logger with standard logging | `track-dotnet` | `dotnet-r1` | Must | 4 |
| EN-06 | enabler | Replace the in-process session order draft | `track-dotnet` | `dotnet-r1` | Must | 5 |
| EN-08 | enabler | Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in | `track-dotnet` | `dotnet-r1` | Must | 6 |
| STORY-201 | story | Run Order Desk on .NET 10 with unchanged staff screens | `track-dotnet` | `dotnet-r1` | Must | 7 |
| FEAT-202 | feature | Test, build and local data | `track-dotnet` | `dotnet-r1` | Must | — |
| EN-02 | enabler | Replace MSTest v1 so all tests run on Windows, macOS and Linux | `track-dotnet` | `dotnet-r1` | Must | 8 |
| EN-09 | enabler | Build an automated build and test pipeline | `track-dotnet` | `dotnet-r1` | Must | 9 |
| EN-12 | enabler | Provide local test data with orders and a local database recipe | `track-dotnet` | `dotnet-r1` | Must | 10 |
| FEAT-203 | feature | Pricing, channel and time parity | `track-dotnet` | `dotnet-r1` | Must | — |
| EN-10 | enabler | Make time handling explicit and tested | `track-dotnet` | `dotnet-r1` | Must | 11 |
| STORY-202 | story | Keep pricing identical to today (pricing parity) | `track-dotnet` | `dotnet-r1` | Must | 12 |
| STORY-203 | story | Keep the order channel visible to staff (channel parity) | `track-dotnet` | `dotnet-r1` | Must | 13 |
| STORY-206 | story | Keep dates and price validity identical in any time zone (time parity) | `track-dotnet` | `dotnet-r1` | Must | 14 |
| FEAT-204 | feature | Staff sign-in with Entra ID | `track-dotnet` | `dotnet-r1` | Must | — |
| STORY-204 | story | Sign staff in with Microsoft Entra ID | `track-dotnet` | `dotnet-r1` | Must | 15 |
| FEAT-205 | feature | Secret-free configuration | `track-dotnet` | `dotnet-r1` | Must | — |
| EN-04 | enabler | Remove Windows sign-in and server names from database configuration | `track-dotnet` | `dotnet-r1` | Must | 16 |
| STORY-205 | story | Keep secrets out of code, tests and configuration | `track-dotnet` | `dotnet-r1` | Must | 17 |
| EPIC-202 | epic | Customer portal pilot: sign-in, orders, status, reorder | `track-dotnet` | `dotnet-r2` | Must | — |
| FEAT-206 | feature | Customer sign-in, company isolation and data residency | `track-dotnet` | `dotnet-r2` | Must | — |
| EN-11 | enabler | Build the authorisation foundation for customer scoping and channel | `track-dotnet` | `dotnet-r2` | Must | 18 |
| STORY-230 | story | Sign in and see only my own company's orders | `track-dotnet` | `dotnet-r2` | Must | 19 |
| STORY-240 | story | Authenticate customers with an externally managed identity | `track-dotnet` | `dotnet-r2` | Must | 20 |
| STORY-239 | story | Keep portal hosting, identity and mail data in the EU | `track-dotnet` | `dotnet-r2` | Must | 21 |
| FEAT-207 | feature | Order list, order detail and status | `track-dotnet` | `dotnet-r2` | Must | — |
| STORY-231 | story | See my company's orders from the last 24 months | `track-dotnet` | `dotnet-r2` | Must | 22 |
| STORY-232 | story | Open an order and see lines, prices, address and status | `track-dotnet` | `dotnet-r2` | Must | 23 |
| STORY-233 | story | See one of six order statuses with an as-of time | `track-dotnet` | `dotnet-r2` | Must | 24 |
| FEAT-208 | feature | Reorder, submit and channel | `track-dotnet` | `dotnet-r2` | Must | — |
| STORY-234 | story | Create a new order by copying a previous order | `track-dotnet` | `dotnet-r2` | Must | 25 |
| STORY-235 | story | Have a submitted portal order appear in Order Desk as Received | `track-dotnet` | `dotnet-r2` | Must | 26 |
| STORY-236 | story | Show staff whether an order came from the portal or from staff | `track-dotnet` | `dotnet-r2` | Must | 27 |
| FEAT-209 | feature | Customer prices and language | `track-dotnet` | `dotnet-r2` | Must | — |
| STORY-238 | story | Show my negotiated prices, not list prices | `track-dotnet` | `dotnet-r2` | Must | 28 |
| STORY-237 | story | Use the portal in French and English | `track-dotnet` | `dotnet-r2` | Should | 29 |
| FEAT-210 | feature | Audit, accessibility and performance | `track-dotnet` | `dotnet-r2` | Must | — |
| STORY-241 | story | Record who, what, when and channel for every order change | `track-dotnet` | `dotnet-r2` | Must | 30 |
| STORY-242 | story | Check every pilot screen against WCAG 2.2 level AA | `track-dotnet` | `dotnet-r2` | Must | 31 |
| STORY-243 | story | Respond in under 2 seconds at the 95th percentile | `track-dotnet` | `dotnet-r2` | Must | 32 |
| EPIC-203 | epic | Complete the portal and publish the Order Desk API contract | `track-dotnet` | `dotnet-r3` | Should | — |
| FEAT-211 | feature | Invoice download | `track-dotnet` | `dotnet-r3` | Should | — |
| EN-07 | enabler | Abstract the invoice store | `track-dotnet` | `dotnet-r3` | Should | 33 |
| STORY-260 | story | Download the PDF invoice of a delivered order | `track-dotnet` | `dotnet-r3` | Should | 34 |
| FEAT-212 | feature | Customer user administration and shipping e-mail | `track-dotnet` | `dotnet-r3` | Should | — |
| STORY-261 | story | Invite and remove users of my own company | `track-dotnet` | `dotnet-r3` | Should | 35 |
| STORY-262 | story | Receive an e-mail when an order changes to Shipped | `track-dotnet` | `dotnet-r3` | Could | 36 |
| FEAT-213 | feature | Dutch and success-measure data | `track-dotnet` | `dotnet-r3` | Should | — |
| STORY-263 | story | Use the portal in Dutch | `track-dotnet` | `dotnet-r3` | Should | 37 |
| STORY-264 | story | Record data to compare SM-01 to SM-04 with their baselines | `track-dotnet` | `dotnet-r3` | Should | 38 |
| FEAT-214 | feature | Order Desk API contract | `track-dotnet` | `dotnet-r3` | Should | — |
| EN-14 | enabler | Publish the read-only Order Desk API contract (OpenAPI 2.0) | `track-dotnet` | `dotnet-r3` | Should | 39 |
| STORY-265 | story | Let another track build against the published order contract | `track-dotnet` | `dotnet-r3` | Should | 40 |
| EPIC-204 | epic | Order Desk API implementation for other tracks | `track-dotnet` | unplanned | Should | — |
| FEAT-215 | feature | Order Desk read-only API service | `track-dotnet` | unplanned | Should | — |
| STORY-280 | story | Offer a read-only Order Desk service for orders and order lines | `track-dotnet` | unplanned | Should | 41 |

### 2.3 Power Platform (`track-power-platform`, all unplanned)

| Id | Type | Title | Track tag | Release tag | Priority (band) | Rank |
|---|---|---|---|---|---|---|
| EPIC-301 | epic | Claims platform foundation: environments, solution, connector stub, licensing, roles | `track-power-platform` | unplanned | Must (P1) | — |
| FEAT-301 | feature | Environments, data loss prevention and solution | `track-power-platform` | unplanned | Must (P1) | — |
| EP-01 | enabler | Design environments and data loss prevention policy | `track-power-platform` | unplanned | Must (P1) | 1 |
| EP-02 | enabler | Design the NorthwindClaims solution | `track-power-platform` | unplanned | Must (P1) | 2 |
| STORY-301 | story | Keep claims data in dedicated Europe environments with a DLP policy | `track-power-platform` | unplanned | Must (P1) | 3 |
| FEAT-302 | feature | Licensing, connector stub and finance contract | `track-power-platform` | unplanned | Must (P1) | — |
| EP-04 | enabler | Decide licensing and cost | `track-power-platform` | unplanned | Must (P1) | 4 |
| EP-03 | enabler | Define the stub custom connector contract | `track-power-platform` | unplanned | Must (P1) | 5 |
| EP-05 | enabler | Define the finance CSV contract and drop location | `track-power-platform` | unplanned | Must (P1) | 6 |
| FEAT-303 | feature | Identity and roles | `track-power-platform` | unplanned | Must (P1) | — |
| EP-06 | enabler | Define identity and roles with no self-approval | `track-power-platform` | unplanned | Must (P1) | 7 |
| STORY-302 | story | Sign claims users in with Entra ID and assign roles | `track-power-platform` | unplanned | Must (P1) | 8 |
| EPIC-302 | epic | Record, approve and hand off claims; claims history | `track-power-platform` | unplanned | Must (P1) | — |
| FEAT-304 | feature | Record a claim | `track-power-platform` | unplanned | Must (P1) | — |
| STORY-320 | story | Record a delivery claim in under 2 minutes with up to 5 photos | `track-power-platform` | unplanned | Must (P1) | 9 |
| FEAT-305 | feature | Approve claims and audit decisions | `track-power-platform` | unplanned | Must (P1) | — |
| STORY-321 | story | Approve claims above EUR 500 without self-approval | `track-power-platform` | unplanned | Must (P1) | 10 |
| STORY-323 | story | Record every claim decision for 7 years | `track-power-platform` | unplanned | Must (P1) | 11 |
| FEAT-306 | feature | Credit-note hand-off to Finance | `track-power-platform` | unplanned | Must (P1) | — |
| STORY-322 | story | Send an approved claim to Finance as a credit-note request | `track-power-platform` | unplanned | Must (P1) | 12 |
| FEAT-307 | feature | Claims history migration | `track-power-platform` | unplanned | Not set (O-14) | — |
| STORY-324 | story | Decide whether spreadsheet claims move to the new solution | `track-power-platform` | unplanned | Not set (O-14) | 13 |
| EPIC-303 | epic | Warehouse causes and claims dashboard | `track-power-platform` | unplanned | Should (P2) | — |
| FEAT-308 | feature | Warehouse cause recording | `track-power-platform` | unplanned | Should (P2) | — |
| STORY-350 | story | Let warehouse supervisors see and record causes of their claims | `track-power-platform` | unplanned | Should (P2) | 14 |
| FEAT-309 | feature | Weekly claims dashboard | `track-power-platform` | unplanned | Should (P2) | — |
| STORY-351 | story | Show a weekly claims dashboard | `track-power-platform` | unplanned | Should (P2) | 15 |
| EPIC-304 | epic | Customer claim notifications | `track-power-platform` | unplanned | Could (P3) | — |
| FEAT-310 | feature | Customer claim e-mail | `track-power-platform` | unplanned | Could (P3) | — |
| STORY-370 | story | E-mail the customer when a claim is approved or rejected | `track-power-platform` | unplanned | Could (P3) | 16 |

## 3. Counts per track and release

Epics, features, stories and enablers (enablers are stories with a technical role and are counted on their own). Stories here are the 57 product-requirement stories.

| Track | Release | Epics | Features | Stories | Enablers | Items (all four types) |
|---|---|---|---|---|---|---|
| Azure | `azure-r1` | 2 | 5 | 8 | 6 | 21 |
| Azure | `azure-r2` | 1 | 5 | 7 | 7 | 20 |
| Azure | `azure-r3` | 1 | 4 | 5 | 3 | 13 |
| Azure | **total** | **4** | **14** | **20** | **16** | **54** |
| .NET | `dotnet-r1` | 1 | 5 | 6 | 11 | 23 |
| .NET | `dotnet-r2` | 1 | 5 | 14 | 1 | 21 |
| .NET | `dotnet-r3` | 1 | 4 | 6 | 2 | 13 |
| .NET | unplanned | 1 | 1 | 1 | 0 | 3 |
| .NET | **total** | **4** | **15** | **27** | **14** | **60** |
| Power Platform | unplanned (no release) | 4 | 10 | 10 | 6 | 30 |
| **All tracks** | | **12** | **39** | **57** | **36** | **144** |

These counts match PRD section 16.2: 57 product functional requirements (Azure 20, .NET 27, Power Platform 10) and 36 enablers (16, 14, 6). `EA-15` and `EA-16` (with `FEAT-113` and `FEAT-114`) were added after the first review (A-59).

## 4. Items by track, in rank order

Each item block shows: tags, priority, rank, parent, source (ES-02), gate, the story text, acceptance criteria, dependencies and the ASSUMPTION and OPEN ids it relies on. Cross-track needs are **OPEN:** `X-nn` rows (full text in section 7.3) and **never** a wait: each block says how the track keeps delivering.

### 4.1 Azure track (`track-azure`, business area BA-01)

Azure items are a reviewed, locally validated design set, never a deployment (ES-27). The Azure team owns hosting, IaC, recovery, monitoring and the C-04 cost model (A-02).

---

#### EPIC-101 Azure foundation and security baseline

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Features:** FEAT-101, FEAT-102, FEAT-103
* **Source:** (source: NFR-03, NFR-05, C-01, CS-09, CS-13, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27)
* **Gate:** none. `EA-01` to `EA-03` do not depend on the data tier (MVE-01 does not gate them).
* **Goal:** One validated foundation (naming, tags, region, connectivity, secrets, private access) that every later Azure item builds on, in design form only.
* **Cross-track (OPEN):** X-02, X-03, X-11, X-14 (see the items below). **Relies on:** A-02, A-39, A-45; O-15, O-19.

##### FEAT-101 Environment foundation as code and validation

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Parent:** EPIC-101 · **Contains:** EA-01, EA-11, STORY-101, STORY-104, STORY-105
* **Source:** (source: CS-09, CS-19, NFR-03, ES-20 to ES-24, ES-27) · **Gate:** none

###### EA-01 Build the Azure foundation as code (naming, tags, region, modules)

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-03) · **Rank:** 1 · **Parent:** FEAT-101 · **Serves:** FR-101, FR-104
* **Source:** (source: CS-09, NFR-03, ES-20, ES-21, ES-22, ES-23, ES-24, ES-27) · **Gate:** none
* **Story:** As an Azure platform engineer, I want the naming rule, the required tags, the primary region and the infrastructure definitions written as code with Azure Verified Modules, so that every later Azure item builds on one validated foundation.
* **Acceptance criteria:**
  * `EA-01/AC1` Given an entry point `main.bicep` and a `.bicepparam` file for each of `tst` and `prd` under `infra/` (ES-10, ES-22), When `az bicep build` is run locally on each, Then it finishes with no error and nothing is applied to a subscription (ES-27).
  * `EA-01/AC2` Given any resource defined, When its name is generated, Then it follows `<resource-abbreviation>-nw-<workload>-<environment>-<region>` with environment `tst` or `prd` (for example `app-nw-orderdesk-prd-frc`) (ES-23).
  * `EA-01/AC3` Given any resource definition, When it is reviewed, Then it carries the tags `workload`, `environment`, `owner` and `costCenter`; a definition missing one tag is rejected until the tag is added (ES-24).
  * `EA-01/AC4` Given an Azure Verified Module exists for a resource, When the resource is defined, Then the module is used; where none exists, the exception and its reason are written next to the definition (ES-22).
* **Dependencies:** none; this is the first Azure item. **Cross-track (OPEN):** X-02 (the application's configuration contract is written by .NET; Azure writes infrastructure around it and validates locally). **Relies on:** A-02, A-39.

###### EA-11 Build the infrastructure validation and deployment pipeline design

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 2 · **Parent:** FEAT-101 · **Serves:** FR-105
* **Source:** (source: CS-19, ES-22, ES-27) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a pipeline definition that validates every infrastructure file locally and never applies it, so that releases have a repeatable, reviewed check instead of a manual copy (CS-19).
* **Acceptance criteria:**
  * `EA-11/AC1` Given a change to any file under `infra/`, When the validation step runs, Then it runs `az bicep build` on every `main.bicep` and reports the result.
  * `EA-11/AC2` Given a `main.bicep` with no matching `.bicepparam` file, or a file that does not build, When the validation step runs, Then it fails and names the file.
  * `EA-11/AC3` Given the pipeline definition, When it is reviewed, Then it contains no step that applies anything to a subscription from this workshop; any deploy stage is marked as needing human approval (ES-27).
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-11 (the .NET track writes its own build pipeline; each track keeps delivering on its own). **Relies on:** O-19 (pipeline tool not chosen; the definition is tool-neutral until answered).

###### STORY-101 Review a test and production environment design set

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 3 · **Parent:** FEAT-101 · **Implements:** FR-101
* **Source:** (source: C-01, CS-09, ES-20, ES-22, ES-23, ES-24, ES-27) · **Gate:** none
* **Story:** As the IT manager, I want a reviewed design set for a test environment and a production environment, so that the team agrees one platform baseline before any hosting work starts.
* **Acceptance criteria:**
  * `STORY-101/AC1` Given the design set, When the product owner and the IT manager review it, Then it shows one naming rule, the four required tags, France Central as the primary region and infrastructure written as code for both `tst` and `prd`.
  * `STORY-101/AC2` Given the design set, When it is validated locally, Then it passes and nothing is applied to a subscription (ES-27).
  * `STORY-101/AC3` Given a reviewer finds a name that breaks the rule or a resource without the four tags, When the review ends, Then `azure-r1` cannot be approved until it is fixed.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-02, X-14. **Relies on:** A-39; O-09 (approver).

###### STORY-104 Keep every Azure resource in an EU region

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must (A-06) · **Rank:** 4 · **Parent:** FEAT-101 · **Implements:** FR-104 · **Covers:** NFR-03 (Azure side)
* **Source:** (source: NFR-03, ES-20) · **Gate:** none
* **Story:** As the IT manager, I want every Azure resource for Order Desk and the portal placed in France Central or another EU region, so that customer data and order data stay in the European Union.
* **Acceptance criteria:**
  * `STORY-104/AC1` Given the design set, When every resource is listed with its region, Then each resource is in France Central, or in another EU region if it is a secondary region (ES-20).
  * `STORY-104/AC2` Given a resource defined outside the EU, When the list is reviewed, Then the design is rejected and the resource is moved to an EU region before `azure-r1` is approved.
  * `STORY-104/AC3` Given a secondary region is proposed, When it is reviewed, Then it is in the EU, or it is not accepted.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-04 is the Azure side of customer and staff identity and stays **OPEN:**; the identity and mail services of the portal are covered by STORY-239 (O-24). **Relies on:** A-54.

###### STORY-105 Validate every infrastructure definition locally before release

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 5 · **Parent:** FEAT-101 · **Implements:** FR-105
* **Source:** (source: CS-19, ES-22, ES-27) · **Gate:** none
* **Story:** As the IT manager, I want a deployment pipeline design in which every infrastructure definition is validated locally and reviewed before a release is approved, so that nothing unchecked reaches a subscription later.
* **Acceptance criteria:**
  * `STORY-105/AC1` Given any infrastructure definition in the release, When `az bicep build` is run locally (for example), Then it passes and a reviewer has recorded the review before release approval.
  * `STORY-105/AC2` Given a definition that fails to build, When the release content is assembled, Then that definition is left out and listed as a finding.
  * `STORY-105/AC3` Given the pipeline design, When it is read, Then it states which stage needs a human approval before anything is applied and that nothing is applied from this workshop.
* **Dependencies:** `EA-11`. **Cross-track (OPEN):** X-11. **Relies on:** O-19.

##### FEAT-102 Hybrid connectivity design

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Parent:** EPIC-101 · **Contains:** EA-02, STORY-102
* **Source:** (source: CS-09, C-01, C-03) · **Gate:** none

###### EA-02 Design hybrid connectivity between Lyon, Azure and Antwerp

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 6 · **Parent:** FEAT-102 · **Serves:** FR-102
* **Source:** (source: CS-09, C-01, C-03, O-15) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a connectivity design for the existing link to Antwerp, the link from Lyon to Azure during the migration and the path after the lease, so that the StockPilot exchange stays reachable throughout.
* **Acceptance criteria:**
  * `EA-02/AC1` Given today's site-to-site VPN between Lyon and Antwerp (CS-09), When the design is reviewed, Then it shows how Antwerp keeps reaching the order data during the migration and after 30 June 2027.
  * `EA-02/AC2` Given the location after the lease of the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route is not known (O-15), When the design names any of them, Then each is marked **OPEN:** with its owner and is not designed as a fact.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** none new. **Relies on:** O-15.

###### STORY-102 Agree the connection design for the move and after the lease

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 7 · **Parent:** FEAT-102 · **Implements:** FR-102
* **Source:** (source: CS-09, C-01, C-03) · **Gate:** none
* **Story:** As the IT manager, I want one agreed design of how Azure, the Lyon data centre and the Antwerp warehouse connect during the move and after the lease, so that the StockPilot exchange never loses its path.
* **Acceptance criteria:**
  * `STORY-102/AC1` Given the connection design, When it is reviewed, Then it describes the connections for two periods: during the migration and after the lease ends.
  * `STORY-102/AC2` Given the nightly 02:00 StockPilot exchange (CS-10), When each period is read, Then the exchange stays reachable in both.
  * `STORY-102/AC3` Given a path depends on an unanswered item from O-15, When the design is reviewed, Then that path is marked **OPEN:** with an owner and the release is not blocked by it.
* **Dependencies:** `EA-02`. **Cross-track (OPEN):** none. **Relies on:** O-15.

##### FEAT-103 Secrets, identity and private access

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Parent:** EPIC-101 · **Contains:** EA-03, STORY-103
* **Source:** (source: NFR-05, CS-13, ES-17, ES-25) · **Gate:** none

###### EA-03 Design secrets, managed identities and private endpoints

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-05) · **Rank:** 8 · **Parent:** FEAT-103 · **Serves:** FR-103
* **Source:** (source: CS-13, NFR-05, ES-17, ES-25) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a managed secret store, managed identities and private endpoints designed and defined as code, so that no Azure-hosted part of Order Desk needs a password.
* **Acceptance criteria:**
  * `EA-03/AC1` Given any Azure-hosted application in the design, When its credentials are listed, Then each is held in the secret store or replaced by a managed identity, and no definition contains a password (ES-25).
  * `EA-03/AC2` Given a data service (database, storage, Key Vault), When its network access is reviewed, Then it is reached through a private endpoint (ES-25).
  * `EA-03/AC3` Given a parameter file that contains a password, key or connection string with a password, When the secret scan runs, Then the scan fails and names the file.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-02, X-03 (database sign-in moves from Windows-integrated to a managed identity; .NET builds against a local SQL Server meanwhile). **Relies on:** A-02.

###### STORY-103 Keep secrets out of Azure-hosted code and configuration

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must (A-06) · **Rank:** 9 · **Parent:** FEAT-103 · **Implements:** FR-103 · **Covers:** NFR-05 (Azure side)
* **Source:** (source: NFR-05, CS-13, ES-17, ES-25) · **Gate:** none
* **Story:** As the IT manager, I want the Azure-hosted parts of Order Desk to hold no secret in source code or in configuration files in the repository, so that a leaked repository exposes no credential.
* **Acceptance criteria:**
  * `STORY-103/AC1` Given the release content, When a scan of source and configuration files runs as part of the release exit criteria, Then it finds no password, key or connection string with a password.
  * `STORY-103/AC2` Given an application needs a credential, When the design is reviewed, Then it uses the managed secret store with a managed identity and no password.
  * `STORY-103/AC3` Given the scan finds a secret, When the release is considered for approval, Then it is not approved until the secret is removed.
* **Dependencies:** `EA-03`. **Cross-track (OPEN):** X-02, X-03. **Relies on:** A-54 (measurement rule).

---

#### EPIC-102 Data platform decision, cost and migration approach

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Features:** FEAT-104, FEAT-105
* **Source:** (source: C-02, C-04, C-06, BR-13, CS-07, CS-08, CS-21, ES-21, ES-25)
* **Gate:** **MVE-01** (a PaaS data tier can host `NorthwindOrders`, keep the nightly StockPilot exchange with an unchanged file contract and stay inside the cost cap; pass thresholds `M1a`, `M1b`, `M1c`, **ASSUMPTION:** A-35). Applies to `EA-05` and `EA-09`. Result **pending**.
* **Goal:** Decide where the order database runs, prove the monthly cost fits the cap and fix how the data moves inside the Sunday window.
* **Cross-track (OPEN):** X-12. **Relies on:** A-20, A-21, A-30, A-32, A-33, A-35; O-03, O-21, O-24.

##### FEAT-104 Data tier decision

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Parent:** EPIC-102 · **Contains:** EA-05, STORY-120
* **Source:** (source: C-02, C-06, CS-07, ES-21) · **Gate:** MVE-01

###### EA-05 Record the data-tier decision and migration approach

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 10 · **Parent:** FEAT-104 · **Serves:** FR-106, FR-108
* **Source:** (source: CS-07, CS-21, C-02, ES-21) · **Gate:** MVE-01 (decision before commit)
* **Story:** As an Azure platform engineer, I want a decision record that compares the managed-service options with a virtual machine and states the migration approach, so that later exchange, backup and cost work starts from one chosen option.
* **Acceptance criteria:**
  * `EA-05/AC1` Given MVE-01 has been decided (go, adjust or stop), When the record is written, Then it names the chosen option and shows how that option was checked against `M1a` (0 unmapped constructs), `M1b` (cost at or below EUR 1,200 a month, A-35) and `M1c` (backup frequency of 60 minutes or less).
  * `EA-05/AC2` Given MVE-01 has not been decided, When the epic is considered for commitment, Then `EA-05` stays uncommitted (gate) and `EA-01` to `EA-03` continue.
  * `EA-05/AC3` Given a construct of the current database has no equivalent in an option (for example a SQL Server Agent job, A-30), When it is checked, Then it is listed as unmapped and that option fails `M1a`.
* **Dependencies:** `EA-01`; blocks `EA-06`, `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-20, A-21, A-30, A-32, A-35; O-03.

###### STORY-120 Decide the data tier for the order database

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 11 · **Parent:** FEAT-104 · **Implements:** FR-106
* **Source:** (source: C-02, C-06, CS-07, BR-13, ES-21) · **Gate:** MVE-01
* **Story:** As the IT manager, I want a written decision on the data tier for the order database, so that the team knows where `NorthwindOrders` will run and how the old servers leave support.
* **Acceptance criteria:**
  * `STORY-120/AC1` Given the decision record, When it is read, Then it names the chosen data tier, states that a managed service (PaaS) is preferred and a virtual machine is the fallback (A-21), and introduces no Kubernetes (ES-21).
  * `STORY-120/AC2` Given the decision, When it is read, Then it states how the old web server and database server leave support (C-02).
  * `STORY-120/AC3` Given the decision, When it is reviewed, Then it keeps the StockPilot exchange working and fits what a six-person team that knows .NET and SQL Server can run (C-06).
  * `STORY-120/AC4` Given MVE-01 ends in **adjust** because only the virtual machine passes, When the record is written, Then it chooses the virtual machine and explains in a decision record why it departs from ES-21.
* **Dependencies:** `EA-05`; the decision is carried out by `EA-16` (`azure-r3`). **Cross-track (OPEN):** none. **Relies on:** A-20, A-21; O-03, O-21.

##### FEAT-105 Cost model and migration approach

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Parent:** EPIC-102 · **Contains:** EA-09, STORY-121, STORY-122
* **Source:** (source: C-04, BR-13, CS-07, CS-08, CS-21) · **Gate:** MVE-01

###### EA-09 Build the Azure cost model against the monthly cap

* **Tags:** `track-azure` `azure-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 12 · **Parent:** FEAT-105 · **Serves:** FR-107
* **Source:** (source: C-04, X-12, CS-03, CS-06) · **Gate:** MVE-01
* **Story:** As an Azure platform engineer, I want a cost model for the production and one test environment that includes the portal and the Order Desk API host, so that every sizing choice is checked against the monthly cap.
* **Acceptance criteria:**
  * `EA-09/AC1` Given today's load (about 60 concurrent users at peak, CS-03; average CPU 18 % and peak 55 %, CS-06), When the model is built, Then it lists a monthly figure for each component of production and one test environment.
  * `EA-09/AC2` Given the model, When it is read, Then it shows the monthly total, the EUR 1,500 cap (C-04) and the headroom left.
  * `EA-09/AC3` Given a price comes from a public price list, When it is entered, Then it is date-stamped and labelled indicative; no price is presented as a quote.
* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-12 (the portal and API host share the cap; Azure sizes from today's load and refines later). **Relies on:** A-02, A-35; O-24.

###### STORY-121 Show the monthly cost against the EUR 1,500 cap

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 13 · **Parent:** FEAT-105 · **Implements:** FR-107
* **Source:** (source: C-04, X-12, T-03) · **Gate:** MVE-01
* **Story:** As the sponsor (Marc Dubois), I want a cost model of the whole Azure platform against the EUR 1,500 monthly cap, so that I can see whether Order Desk and the portal fit before anything is built.
* **Acceptance criteria:**
  * `STORY-121/AC1` Given the cost model, When it is reviewed, Then it covers Order Desk, the portal and the Order Desk API host in production and one test environment, and shows the monthly total and the headroom against EUR 1,500.
  * `STORY-121/AC2` Given the estimate for Order Desk alone is above EUR 1,200 (80 % of the cap, the MVE-01 starting threshold, A-35), When the model is reviewed, Then the result is recorded as **adjust** and the sponsor is told that headroom for the portal is below EUR 300 (derived: EUR 1,500 less EUR 1,200).
  * `STORY-121/AC3` Given the total is above EUR 1,500 for every option that passes `M1a` and `M1c`, When the model is reviewed, Then the result is **stop** and Marc Dubois decides whether to relax C-04 or reduce scope (O-21).
* **Dependencies:** `EA-09`. **Cross-track (OPEN):** X-12. **Relies on:** A-02, A-35; O-21, O-24.

###### STORY-122 Define the database and invoice migration approach

* **Tags:** `track-azure` `azure-r1` · **Priority:** Must · **Rank:** 14 · **Parent:** FEAT-105 · **Implements:** FR-108
* **Source:** (source: BR-13, CS-07, CS-08, CS-21) · **Gate:** MVE-01 (through the data-tier option)
* **Story:** As the IT manager, I want a migration approach for the order database (48 GB, growing about 1 GB a month) and the invoice files (120 GB, growing about 2 GB a month), so that the move fits the Sunday maintenance window of 06:00 to 12:00 CET.
* **Acceptance criteria:**
  * `STORY-122/AC1` Given the approach, When it is read, Then it states the steps, the expected downtime and the fallback for the database and for the invoice files.
  * `STORY-122/AC2` Given the planned steps are added up, When the total is longer than the window of 06:00 to 12:00 CET, Then the approach is not accepted until steps are split across Sundays or a fallback is defined.
  * `STORY-122/AC3` Given the claim that a log-based restore fits the window cannot be proved on paper (A-33), When the approach is reviewed, Then the claim is marked **ASSUMPTION:** and the proof is left to `EA-16` and to the rehearsals planned in `EA-13`.
* **Dependencies:** `EA-05`. **Cross-track (OPEN):** none. **Relies on:** A-33.

---

#### EPIC-103 Pilot environment, exchange, storage and observability

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Features:** FEAT-113, FEAT-106, FEAT-107, FEAT-108, FEAT-109
* **Source:** (source: BR-13, C-01, C-02, C-03, C-04, C-06, NFR-01, NFR-06, NFR-08, CS-06, CS-08, CS-10, CS-12, CS-13, CS-15, CS-16, CS-22, CS-23, ES-21, ES-23, ES-25, ES-26)
* **Gate:** **MVE-01** for `EA-06` and `EA-08` (and the stories they serve), and for the production database settings of `EA-15`. Result **pending**.
* **Goal:** Land the pilot environment, the application host, the StockPilot exchange, invoice storage, monitoring and the backup and retention design before the Q2 2027 portal pilot.
* **Cross-track (OPEN):** X-02, X-07, X-09, X-10. **Relies on:** A-05, A-20, A-27, A-29, A-31, A-33, A-37, A-59; O-03, O-15, O-16, O-17.

##### FEAT-113 Application hosting

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Parent:** EPIC-103 · **Contains:** EA-15
* **Source:** (source: BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25) · **Gate:** MVE-01 for the production database settings of `EA-15` only; the rest of the feature has none

###### EA-15 Host the Order Desk web application in the test and production environments

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-01 and serves BR-13) · **Rank:** 15 · **Parent:** FEAT-113 · **Serves:** FR-112, FR-116 · **Added after the first review (A-59)**
* **Source:** (source: BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25) · **Gate:** MVE-01 for the production database settings only (decision before those settings are committed); test hosting does not wait for it, and the runtime choice is a decision under O-03, not an experiment
* **Story:** As an Azure platform engineer, I want the hosting of the Order Desk web application designed as code for `tst` and `prd`, with its settings for sign-in, secrets, size and monitoring, checked locally (nothing is applied in Azure, ES-27), so that the application has a defined place to run before the database moves and the cutover.
* **Acceptance criteria:**
  * `EA-15/AC1` Given the hosting definition for `tst` and for `prd`, When `az bicep build` is run locally on each, Then it passes, names and tags follow ES-23 and ES-24, and nothing is applied to a subscription (ES-27).
  * `EA-15/AC2` Given it is not yet decided whether Order Desk is rehosted unchanged on a Windows virtual machine or waits for `net10.0` and a managed web service (O-03, A-20), When the definition is reviewed, Then it states which runtime it describes, names the other as **OPEN:** O-03 with Ahmed Benali as owner, and presents no runtime as decided.
  * `EA-15/AC3` Given the hosted application needs the order database and Key Vault, When its settings are reviewed, Then it reaches them through a managed identity and a private endpoint with no password in any file (CS-13, ES-25).
  * `EA-15/AC4` Given Order Desk keeps the order draft in the process session today (CS-16), When the definition is reviewed, Then it runs one instance until the draft is stateless (X-07), and no scale-out is assumed.
  * `EA-15/AC5` Given today's load of average CPU 18 % and peak 55 % (CS-06), When the host size is chosen, Then the size is listed in the cost model of `EA-09`, and the definition exposes the endpoint that the synthetic probe of `STORY-142` calls (NFR-01).
  * `EA-15/AC6` Given the data tier is not yet decided (MVE-01, `EA-05`), When the definitions are reviewed, Then `tst` hosting is complete with a placeholder connection setting that points to user secrets or a managed identity and holds no password (ES-17, ES-25), and the production database settings in `prd` are marked **OPEN:** until `EA-05` records the decision; a Stop or Adjust result delays only those production settings.
* **Dependencies:** `EA-01`, `EA-03`; its production database settings take the data-tier record `EA-05` (they wait for the MVE-01 decision); test hosting and the other settings proceed without it; feeds `EA-16`, `EA-13`. **Cross-track (OPEN):** X-02 (the Order Desk build comes from the .NET track as a `net10.0` application, or the unchanged application is rehosted per A-20; Azure writes the definition for either and validates it locally; `azure-r2` does not wait for the build), X-07 (single instance). **Relies on:** A-20, A-59; O-03.

##### FEAT-106 StockPilot exchange, invoice storage and outbound mail

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Parent:** EPIC-103 · **Contains:** EA-06, EA-07, EA-12, STORY-140, STORY-141, STORY-144
* **Source:** (source: C-03, CS-08, CS-10, CS-11, CS-12, BR-09) · **Gate:** MVE-01 (`EA-06`, `STORY-140`)

###### EA-06 Redesign the StockPilot exchange without changing the file contract

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 16 · **Parent:** FEAT-106 · **Serves:** FR-109
* **Source:** (source: CS-10, C-03) · **Gate:** MVE-01
* **Story:** As an Azure platform engineer, I want the nightly exchange with StockPilot redesigned for the chosen data tier with the file contract unchanged and no Windows-only tool, so that StockPilot (which stays on premises until at least 2028) needs no change.
* **Acceptance criteria:**
  * `EA-06/AC1` Given the nightly job at 02:00 that exports confirmed orders as CSV files to an SFTP server and imports shipment updates (CS-10), When the redesign is compared with the file-contract baseline, Then file format, file names and the pick-up point are the same as today (A-27).
  * `EA-06/AC2` Given the redesign, When its steps are listed, Then none depends on `xp_cmdshell` or another Windows-only tool.
  * `EA-06/AC3` Given the SFTP route after the lease is not known (O-15), When the redesign names it, Then the route is marked **OPEN:** with its owner.
* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-05 (Azure owns the exchange end to end; .NET only reads the status results). **Relies on:** A-27, A-30; O-15, O-16; MVE-O-05.

###### EA-07 Design invoice storage and synchronisation

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Should (A-49) · **Rank:** 17 · **Parent:** FEAT-106 · **Serves:** FR-110
* **Source:** (source: CS-08, CS-11, CS-14) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a design for storing and synchronising the invoice PDFs, so that the portal can later serve invoices from Azure while the finance system keeps writing them.
* **Acceptance criteria:**
  * `EA-07/AC1` Given the finance system writes one PDF per invoice to `\\NWFS01\invoices\{year}\{invoiceNumber}.pdf` (CS-11), When the design is read, Then the finance system stays the writer and the design states where the files live after the lease.
  * `EA-07/AC2` Given about 120 GB today growing about 2 GB a month (CS-08), When capacity is checked, Then the design covers about 135 GB by 30 June 2027 and continued growth (linear growth over 7 to 7.5 months, MVE-A-03).
  * `EA-07/AC3` Given where the finance system writes after the lease is unknown (O-15), When the design names the location, Then it is marked **OPEN:**.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-15.

###### EA-12 Design outbound mail to replace the on-premises relay

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Should (A-49: it serves only `BR-09`, a requirement of another track) · **Rank:** 18 · **Parent:** FEAT-106 · **Serves:** FR-113
* **Source:** (source: CS-12, A-29, BR-09) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a design for an outbound mail service, so that e-mail still leaves Northwind after the unauthenticated on-premises relay `smtp.northwind.local` stops being usable.
* **Acceptance criteria:**
  * `EA-12/AC1` Given the current relay on port 25 without authentication (CS-12), When the design is read, Then it names the outbound mail path for after the lease and requires authentication.
  * `EA-12/AC2` Given it is not known what sends order confirmations today (O-17), When the design is reviewed, Then that question is marked **OPEN:** and the design does not assume an answer.
* **Dependencies:** none. **Cross-track (OPEN):** X-10 (.NET uses a mail abstraction and a local mail catcher meanwhile). **Relies on:** A-29, A-51; O-17.

###### STORY-140 Keep the nightly StockPilot exchange working after the database moves

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Rank:** 19 · **Parent:** FEAT-106 · **Implements:** FR-109
* **Source:** (source: C-03, CS-10, BR-13) · **Gate:** MVE-01
* **Story:** As an Order Desk supervisor, I want the nightly exchange of confirmed orders and shipment updates with StockPilot to keep working after the database is in Azure, so that warehouse picking in Antwerp is not interrupted.
* **Acceptance criteria:**
  * `STORY-140/AC1` Given the order database is in Azure, When the nightly job runs at 02:00, Then confirmed orders are exported with the same file format to the same pick-up point and shipment updates are imported; StockPilot is not changed.
  * `STORY-140/AC2` Given the replacement design, When it is reviewed, Then it does not depend on Windows-only tools.
  * `STORY-140/AC3` Given a produced file differs from the baseline format in a column, a name or a location, When the comparison is run, Then the story fails and no file is handed to StockPilot.
* **Dependencies:** `EA-06`. **Cross-track (OPEN):** X-05. **Relies on:** A-27, A-30; O-16; MVE-O-05.

###### STORY-141 Decide where invoice files live after the lease

* **Tags:** `track-azure` `azure-r2` · **Priority:** Should · **Rank:** 20 · **Parent:** FEAT-106 · **Implements:** FR-110
* **Source:** (source: CS-08, CS-11, CS-14) · **Gate:** none
* **Story:** As the IT manager, I want a design for invoice storage that states where the PDFs live after the lease, so that invoice access keeps working when the file share is gone.
* **Acceptance criteria:**
  * `STORY-141/AC1` Given about 120 GB of invoice PDFs growing about 2 GB a month, When the design is reviewed, Then it covers that size and growth and the finance system stays the writer.
  * `STORY-141/AC2` Given the location after the lease depends on an unanswered question (O-15), When the design is reviewed, Then the location is marked **OPEN:** with Julien Moreau and Ahmed Benali as owners and the story still completes as a design.
* **Dependencies:** `EA-07`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-15.

###### STORY-144 Replace the on-premises mail relay for outbound e-mail

* **Tags:** `track-azure` `azure-r2` · **Priority:** Could · **Rank:** 21 · **Parent:** FEAT-106 · **Implements:** FR-113
* **Source:** (source: CS-12, BR-09) · **Gate:** none
* **Story:** As the IT manager, I want a design for outbound e-mail that replaces the on-premises relay, so that e-mails such as the Shipped notice (`BR-09`) can still be sent after the lease.
* **Acceptance criteria:**
  * `STORY-144/AC1` Given the on-premises relay is not usable after the lease (A-29), When the design is reviewed, Then it names the replacement path and that path is in the EU (NFR-03).
  * `STORY-144/AC2` Given what sends order confirmations today is unknown (O-17), When the design is reviewed, Then the open question is listed and no assumption is built in.
* **Dependencies:** `EA-12`. **Cross-track (OPEN):** X-10. **Relies on:** A-29; O-17, O-24. **Note:** supports `BR-09`; `BR-09` itself is covered by STORY-262.

##### FEAT-107 Observability and alerting

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Parent:** EPIC-103 · **Contains:** EA-04, STORY-142
* **Source:** (source: NFR-01, CS-15, CS-22, ES-26) · **Gate:** none

###### EA-04 Build observability: log workspace, application monitoring and alerts

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-01) · **Rank:** 22 · **Parent:** FEAT-107 · **Serves:** FR-111, FR-119
* **Source:** (source: CS-15, CS-22, ES-26, NFR-01) · **Gate:** none
* **Story:** As an Azure platform engineer, I want one log workspace per environment, one application monitoring service and alerts defined as code, so that the ping checks and the weekly look at the Windows Event Log (CS-22) are replaced.
* **Acceptance criteria:**
  * `EA-04/AC1` Given the environments `tst` and `prd`, When the design is validated locally, Then each has exactly one log workspace and the diagnostics of every resource are sent to it (ES-26).
  * `EA-04/AC2` Given an application of Order Desk or the portal, When its monitoring is reviewed, Then it reports to the application monitoring service.
  * `EA-04/AC3` Given today's ping checks of `NWWEB01` and `NWSQL01` and the weekly Event Log look, When the alerts are listed, Then an availability alert and an application-error alert replace each of them.
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-08 (.NET logs through the standard logger to the console meanwhile). **Relies on:** A-05.

###### STORY-142 Monitor availability with a synthetic probe and alerts

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must (A-06) · **Rank:** 23 · **Parent:** FEAT-107 · **Implements:** FR-111 · **Covers:** NFR-01 (design and alerting)
* **Source:** (source: NFR-01, CS-15, CS-22, ES-26) · **Gate:** none
* **Story:** As the IT manager, I want availability measured by a synthetic probe and alerted on, so that I know whether the 99.5 % target for Monday to Saturday 06:00 to 20:00 is met.
* **Acceptance criteria:**
  * `STORY-142/AC1` Given the portal is live, When a synthetic probe at the hosting edge requests it, Then availability is calculated per week in local Central European time, with summer time, over Monday to Saturday 06:00 to 20:00 (84 hours a week) (A-05, T-17).
  * `STORY-142/AC2` Given 99.5 % of 84 hours allows about 25 minutes of downtime a week (derived), When measured availability in a week falls below 99.5 %, Then an alert goes to the IT team.
  * `STORY-142/AC3` Given downtime on a Sunday between 06:00 and 12:00 (the maintenance window, CS-21), When availability is calculated, Then that downtime is not counted, because it is outside business hours.
  * `STORY-142/AC4` Given the week of a summer-time change, When the business hours are applied, Then they follow local Central European time, not a fixed offset.
* **Dependencies:** `EA-04`. **Cross-track (OPEN):** X-08. **Relies on:** A-05; T-17.

##### FEAT-108 Test environment for the portal pilot

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Parent:** EPIC-103 · **Contains:** EA-10, STORY-143
* **Source:** (source: ES-23, C-04, business-case section 8) · **Gate:** none

###### EA-10 Define the tst environment

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 24 · **Parent:** FEAT-108 · **Serves:** FR-112
* **Source:** (source: ES-23, business-case section 8) · **Gate:** none
* **Story:** As an Azure platform engineer, I want the `tst` environment defined as code, so that the portal pilot has an environment to run on.
* **Acceptance criteria:**
  * `EA-10/AC1` Given the `tst` entry point, When `az bicep build` is run locally, Then it passes, names follow ES-23 and tags follow ES-24.
  * `EA-10/AC2` Given the application is not yet on `net10.0`, When the `tst` definition is validated, Then it still validates, because it does not depend on how the application is built (X-02).
  * `EA-10/AC3` Given the pilot must not read a database that is being moved, When the definition is reviewed, Then it states which database the pilot reads; until O-23 is answered that statement is **ASSUMPTION:** A-37 (the Azure-hosted database after `azure-r2` is approved).
* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-01, X-02. **Relies on:** A-37; O-23.

###### STORY-143 Define a test environment where the portal pilot can run

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Rank:** 25 · **Parent:** FEAT-108 · **Implements:** FR-112
* **Source:** (source: ES-23, C-04, business-case section 8) · **Gate:** none
* **Story:** As the .NET team lead, I want a defined test environment, so that the 20-customer portal pilot planned for Q2 2027 can run on it.
* **Acceptance criteria:**
  * `STORY-143/AC1` Given the `tst` definition, When it is validated locally, Then it passes, lists every resource the pilot needs, and each resource name and tag follow ES-23 and ES-24.
  * `STORY-143/AC2` Given the definition, When it is reviewed, Then it does not depend on how the application is built, so the .NET track is not blocked and the Azure track is not blocked by .NET (X-02).
  * `STORY-143/AC3` Given the cost of `tst` is part of the EUR 1,500 cap, When the definition is reviewed, Then it appears in the cost model (STORY-121).
* **Dependencies:** `EA-10`; the pilot runs on the application hosting of `EA-15`. **Cross-track (OPEN):** X-01 (.NET builds and tests locally until pilot hosting is answered), X-02. **Relies on:** A-37; O-23.

##### FEAT-109 Backup, retention and recovery design

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must · **Parent:** EPIC-103 · **Contains:** EA-08, STORY-145, STORY-146
* **Source:** (source: NFR-06, NFR-08, CS-07, CS-23) · **Gate:** MVE-01 (`EA-08`, `STORY-146`)

###### EA-08 Design backup, long-term retention and recovery

* **Tags:** `track-azure` `azure-r2` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-06, NFR-08) · **Rank:** 26 · **Parent:** FEAT-109 · **Serves:** FR-114, FR-115
* **Source:** (source: CS-07, CS-23, NFR-06, NFR-08) · **Gate:** MVE-01
* **Story:** As an Azure platform engineer, I want the backup, long-term retention and restore design for the order database, so that recovery and the 7-year audit record are designed before cutover. The first recovery test plan is `EA-14` in `azure-r3`.
* **Acceptance criteria:**
  * `EA-08/AC1` Given today's log backups every 15 minutes (CS-07), When the design states the backup frequency in Azure, Then it is 60 minutes or less (the RPO of 1 hour).
  * `EA-08/AC2` Given order-change records must be kept 7 years, When the design is read, Then it shows how backup and long-term retention achieve 7 years; limits not verified are marked **ASSUMPTION:** A-31.
  * `EA-08/AC3` Given the design, When it is reviewed, Then it names the restore method and who runs a restore.
* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-15. **Relies on:** A-31, A-33; T-14.

###### STORY-145 Keep order-change records for 7 years in Azure

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must (A-06) · **Rank:** 27 · **Parent:** FEAT-109 · **Implements:** FR-114 · **Covers:** NFR-08 (retention design)
* **Source:** (source: NFR-08, CS-07) · **Gate:** through `EA-08` (MVE-01)
* **Story:** As the IT manager, I want a retention design that keeps the record of every order change for 7 years once the database is in Azure, so that the audit requirement stays met after the move.
* **Acceptance criteria:**
  * `STORY-145/AC1` Given the retention design, When it is reviewed, Then it shows 7 years for the order-change records and states how backup and long-term retention achieve it.
  * `STORY-145/AC2` Given a chosen service tier keeps backups for less than 7 years, When the design is reviewed, Then it is rejected or an exception is sent to the product owner; it is not accepted silently.
  * `STORY-145/AC3` Given the feature limits are not verified (A-31), When the design is read, Then they are listed as **ASSUMPTION:** with Ahmed Benali as confirming owner.
* **Dependencies:** `EA-08`. **Cross-track (OPEN):** X-15 (.NET defines the audit content, Azure sets retention). **Relies on:** A-31.

###### STORY-146 Design backup and recovery for RPO 1 hour and RTO 4 hours

* **Tags:** `track-azure` `azure-r2` · **Priority:** Must (A-06) · **Rank:** 28 · **Parent:** FEAT-109 · **Implements:** FR-115 · **Covers:** NFR-06 (design)
* **Source:** (source: NFR-06, CS-07, CS-23) · **Gate:** MVE-01
* **Story:** As the IT manager, I want a backup and recovery design that reaches an RPO of 1 hour and an RTO of 4 hours for order data, so that a failure loses at most an hour of orders and is repaired within four hours.
* **Acceptance criteria:**
  * `STORY-146/AC1` Given the design, When it is read, Then it states the backup frequency, the restore method and who runs a restore, and shows how RPO 1 hour and RTO 4 hours are reached.
  * `STORY-146/AC2` Given the documented backup frequency is longer than 60 minutes (`M1c` fails), When the design is reviewed, Then RPO 1 hour is not met and the design is returned for rework.
  * `STORY-146/AC3` Given a recovery has never been tested (CS-23), When the design is read, Then it does not claim the target is met; proof is the restore test of `STORY-172` in `azure-r3`.
* **Dependencies:** `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-33; T-14.

---

#### EPIC-104 Cutover and recovery proof

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Features:** FEAT-114, FEAT-110, FEAT-111, FEAT-112
* **Source:** (source: BR-13, NFR-01, NFR-03, NFR-06, C-01, C-02, SM-07, CS-07, CS-21, CS-23)
* **Gate:** **MVE-01**, through its inputs (the chosen data tier and its backup and cost figures). Result **pending**.
* **Goal:** A reviewed database migration and rehearsal procedure, and a reviewed cutover, rollback, recovery-test and decommission plan, so that Order Desk can move inside the Sunday window before 30 June 2027. **Release approval comes before the first rehearsal Sunday (before 6 June 2027) and covers the procedures, plans and runbooks, validated locally. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test are planned execution after that approval (A-53, ES-27).** The target window ends on 27 June 2027, so these Sundays are inside it, 3 days before the lease ends (A-58). **OPEN:** O-27 asks Marc Dubois to confirm the extended window, the 3-day margin and the approval date before 6 June 2027.
* **Cross-track (OPEN):** X-03, X-07 (single instance), O-15 (post-lease locations). **Relies on:** A-30, A-33, A-53, A-58, A-59; O-03, O-27.

##### FEAT-114 Database migration and rehearsal

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Parent:** EPIC-104 · **Contains:** EA-16
* **Source:** (source: BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23) · **Gate:** MVE-01 (through the data-tier option)

###### EA-16 Migrate the NorthwindOrders database to the chosen data tier and rehearse the move

* **Tags:** `track-azure` `azure-r3` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-03 and NFR-06 and serves BR-13) · **Rank:** 29 · **Parent:** FEAT-114 · **Serves:** FR-106, FR-116 · **Added after the first review (A-59)**
* **Source:** (source: BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23) · **Gate:** MVE-01 (decision before commit)
* **Story:** As an Azure platform engineer, I want the move of the `NorthwindOrders` database to the chosen data tier written as repeatable steps that are checked locally, with a rehearsal plan, so that the data can move inside the Sunday window and the first restore test starts from a database that was moved the same way.
* **Acceptance criteria:**
  * `EA-16/AC1` Given the data tier decided in `STORY-120` (MVE-01 decided), When the migration steps are read, Then they cover schema, data, sign-in and every job that has no equivalent (A-30), each step has a longest allowed duration, and the total fits the Sunday window set in `STORY-122`.
  * `EA-16/AC2` Given a rehearsal copy of the database, When the row counts and checksums of the order tables are compared with the source, Then they match; a difference fails the rehearsal and the migration is not accepted.
  * `EA-16/AC3` Given the target data tier, When its region is read, Then it is France Central or another EU region (NFR-03); a tier outside the EU is rejected.
  * `EA-16/AC4` Given recovery has never been tested (CS-23), When the migration procedure is read, Then it hands the moved copy to `EA-14` for the first restore test (NFR-06) and claims no recovery result before that test is run.
  * `EA-16/AC5` Given MVE-01 has not been decided or ended in **stop**, When the release is considered for commitment, Then `EA-16` stays uncommitted (gate) and the items marked gate *none* continue.
  * `EA-16/AC6` Given `azure-r3` is approved before the first rehearsal Sunday (before 6 June 2027), When the rehearsal Sundays (6 and 13 June 2027) arrive, Then the rehearsals are planned execution after that approval and are not claimed in this release (A-53, ES-27).
* **Dependencies:** `EA-05`, `EA-08`, `EA-15`; feeds `EA-13`, `EA-14`. **Cross-track (OPEN):** X-03 (database sign-in moves from Windows-integrated to a managed identity; .NET builds against a local SQL Server meanwhile). **Relies on:** A-21, A-30, A-33, A-53, A-59; O-03, O-15, O-27.

##### FEAT-110 Cutover and rollback runbooks

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Parent:** EPIC-104 · **Contains:** EA-13, STORY-170, STORY-171
* **Source:** (source: BR-13, C-01, C-02, CS-21, SM-07) · **Gate:** none

###### EA-13 Write cutover, rollback and decommission runbooks

* **Tags:** `track-azure` `azure-r3` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 30 · **Parent:** FEAT-110 · **Serves:** FR-116, FR-117, FR-119, FR-120
* **Source:** (source: CS-21, BR-13, C-02, SM-07) · **Gate:** none
* **Story:** As an Azure platform engineer, I want written runbooks for cutover, rollback and decommission, so that the move and the retirement of the old servers follow reviewed steps.
* **Acceptance criteria:**
  * `EA-13/AC1` Given the Sunday window of 06:00 to 12:00 CET (CS-21), When a cutover runbook is read, Then every step has a longest allowed duration and the sum fits the window.
  * `EA-13/AC2` Given any cutover step, When the rollback runbook is read, Then it has a path that returns Order Desk to the previous service inside the same window.
  * `EA-13/AC3` Given the decommission runbook, When it is read, Then it states how and when `NWWEB01` and `NWSQL01` are retired so that no production server is past end of support by 30 June 2027.
  * `EA-13/AC4` Given the rehearsal plan, When it is read, Then it names 6 and 13 June 2027 for rehearsal and 20 and 27 June 2027 for live cutover and fallback (Sundays computed from CS-21), all inside the `azure-r3` window that ends on 27 June 2027 (A-58); the plan states that approval comes before the first rehearsal Sunday, before 6 June 2027 (A-53), and carries **OPEN:** O-27.
* **Dependencies:** `EA-04`, `EA-08`, `EA-05`, `EA-15`, `EA-16`. **Cross-track (OPEN):** X-07, O-15. **Relies on:** A-33, A-53, A-58; O-03, O-27.

###### STORY-170 Keep staff working through the cutover inside the Sunday window

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Rank:** 31 · **Parent:** FEAT-110 · **Implements:** FR-116 · **Covers:** BR-13
* **Source:** (source: BR-13, C-01, CS-21) · **Gate:** none
* **Story:** As an Order Desk staff member, I want planned downtime during the move to stay inside the Sunday maintenance window, so that I can keep taking orders Monday to Saturday.
* **Acceptance criteria:**
  * `STORY-170/AC1` Given the cutover plan, When its steps are added up, Then planned downtime is inside Sunday 06:00 to 12:00 CET.
  * `STORY-170/AC2` Given a step has no stated longest duration, When the plan is reviewed, Then the plan is not accepted.
  * `STORY-170/AC3` Given a step's longest duration would push the total past 12:00, When the plan is reviewed, Then the step is split across Sundays or a rollback is defined; the plan is not accepted otherwise.
* **Dependencies:** `EA-13`; it also builds on the hosting `EA-15` and the migration procedure `EA-16`. **Cross-track (OPEN):** X-07, O-15. **Relies on:** A-33, A-53; O-03, O-27.

###### STORY-171 Define rollback and rehearsal for every cutover step

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Rank:** 32 · **Parent:** FEAT-110 · **Implements:** FR-117 · **Covers:** BR-13
* **Source:** (source: BR-13, C-01, CS-21) · **Gate:** none
* **Story:** As the IT manager, I want every cutover step to have a rollback path and a rehearsal plan with a result template, so that a failed Sunday never leaves Order Desk down on Monday.
* **Acceptance criteria:**
  * `STORY-171/AC1` Given each cutover step, When the rollback is read, Then it returns Order Desk to the previous service inside the same window.
  * `STORY-171/AC2` Given the rehearsal plan, When it is read, Then it names the Sundays for rehearsal, live cutover and fallback and includes a template to record each result.
  * `STORY-171/AC3` Given a step has no rollback path, When the plan is reviewed, Then the release is not approved.
* **Dependencies:** `EA-13`. **Cross-track (OPEN):** X-07. **Relies on:** A-53; O-27.

##### FEAT-111 Recovery and availability proof

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Parent:** EPIC-104 · **Contains:** EA-14, STORY-172, STORY-173
* **Source:** (source: NFR-01, NFR-06, CS-22, CS-23, T-14) · **Gate:** none

###### EA-14 Write the first recovery test plan and evidence template

* **Tags:** `track-azure` `azure-r3` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-06) · **Rank:** 33 · **Parent:** FEAT-111 · **Serves:** FR-118 · **New in this plan (split from `EA-08`)**
* **Source:** (source: NFR-06, CS-23, T-14) · **Gate:** none
* **Story:** As an Azure platform engineer, I want a recovery test plan and an evidence template, so that the first restore test has fixed steps and a fixed way to record the result.
* **Acceptance criteria:**
  * `EA-14/AC1` Given a restore test, When the template is filled in, Then it records the measured data loss in minutes and the restore time in hours, next to the pass limits of 60 minutes and 4 hours.
  * `EA-14/AC2` Given the plan, When it is read, Then it states who restores, from which backup and when.
  * `EA-14/AC3` Given recovery has never been tested (CS-23), When the plan is read, Then it calls the first test the baseline and does not claim any earlier result.
* **Dependencies:** `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-33, A-53; T-14.

###### STORY-172 Prove recovery against RPO 1 hour and RTO 4 hours

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must (A-06) · **Rank:** 34 · **Parent:** FEAT-111 · **Implements:** FR-118 · **Covers:** NFR-06 (proof)
* **Source:** (source: NFR-06, CS-07, CS-23) · **Gate:** none
* **Story:** As the IT manager, I want a recovery test plan and evidence template that define how a restore is tested against RPO 1 hour and RTO 4 hours, so that the product owner can see proof and not only a design.
* **Acceptance criteria:**
  * `STORY-172/AC1` Given a restore test is run from backups, When the result is recorded in the template, Then data loss is at most 60 minutes (RPO 1 hour) and time to restore is at most 4 hours (RTO 4 hours) for a pass.
  * `STORY-172/AC2` Given a measured data loss of more than 60 minutes or a restore time of more than 4 hours, When the result is recorded, Then `NFR-06` is recorded as **not met** and the backup design (`EA-08`) is reopened.
  * `STORY-172/AC3` Given the release is approved, When the test is carried out, Then it is a real-world operation after approval and not claimed in this release (A-53, ES-27).
* **Dependencies:** `EA-14`. **Cross-track (OPEN):** none. **Relies on:** A-33, A-53; T-14.

###### STORY-173 Plan the availability proof for the first weeks in Azure

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must (A-06) · **Rank:** 35 · **Parent:** FEAT-111 · **Implements:** FR-119 · **Covers:** NFR-01 (proof)
* **Source:** (source: NFR-01, CS-22) · **Gate:** none
* **Story:** As the product owner, I want a plan that states how availability is observed in the first weeks in Azure and what evidence I will see, so that I can judge whether 99.5 % is met.
* **Acceptance criteria:**
  * `STORY-173/AC1` Given the proof plan, When it is read, Then it uses the synthetic-probe rule of `STORY-142` (hosting edge, local Central European time with summer time, Monday to Saturday 06:00 to 20:00) (A-05).
  * `STORY-173/AC2` Given the plan, When it is read, Then it lists the evidence shown to the product owner: the weekly availability figure and each downtime event with its start, end and cause.
  * `STORY-173/AC3` Given a week below 99.5 %, When the evidence is read, Then the week is flagged `not met` and not averaged away.
* **Dependencies:** `EA-13`, `EA-04`. **Cross-track (OPEN):** none. **Relies on:** A-05; T-17.

##### FEAT-112 Decommission of the old servers

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Parent:** EPIC-104 · **Contains:** STORY-174
* **Source:** (source: C-01, C-02, SM-07) · **Gate:** none

###### STORY-174 Retire the old web and database servers before 30 June 2027

* **Tags:** `track-azure` `azure-r3` · **Priority:** Must · **Rank:** 36 · **Parent:** FEAT-112 · **Implements:** FR-120
* **Source:** (source: C-02, SM-07, C-01) · **Gate:** none
* **Story:** As the sponsor (Marc Dubois), I want a decommission plan for the old web server and database server, so that no production server is past end of support by 30 June 2027 and payments for Extended Security Updates stop.
* **Acceptance criteria:**
  * `STORY-174/AC1` Given the decommission plan, When it is read, Then it states how and when `NWWEB01` and `NWSQL01` are retired so that the count of production servers past end of support is 0 by 30 June 2027 (SM-07).
  * `STORY-174/AC2` Given the plan, When it is read, Then it states the date on which ESU payments stop.
  * `STORY-174/AC3` Given a retirement date after 30 June 2027, When the plan is reviewed, Then the plan is not accepted.
* **Dependencies:** `EA-13`. **Cross-track (OPEN):** O-15 (where the finance system, shares and domain controllers live after the lease). **Relies on:** A-53; O-15.

### 4.2 .NET track (`track-dotnet`, business area BA-02)

.NET items can be built and tested on a developer machine without Azure (X-01). The .NET team owns Order Desk code changes (A-02).

---

#### EPIC-201 Modernise Order Desk to .NET 10 with parity

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Features:** FEAT-201, FEAT-202, FEAT-203, FEAT-204, FEAT-205
* **Source:** (source: NFR-04, NFR-05, BR-10, BR-12, C-01, C-02, CS-01, CS-02, CS-04, CS-13 to CS-20, ES-13 to ES-19)
* **Gate:** none. MVE-02 does not gate parity work (it is technical and low risk).
* **Goal:** The same Order Desk, with the same prices and screens, running on .NET 10 as one solution, with staff signing in through Microsoft Entra ID and no secret in the repository. Little customer value by design; every later .NET story needs it.
* **Cross-track (OPEN):** X-03, X-04 (staff), X-08, X-11, X-14. **Relies on:** A-02, A-24, A-51; O-03, O-19, O-20.

##### FEAT-201 Modernise projects and web layer

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Parent:** EPIC-201 · **Contains:** EN-01, EN-13, EN-03, EN-05, EN-06, EN-08, STORY-201
* **Source:** (source: CS-01, CS-02, CS-04, CS-15, CS-16, CS-17, ES-13 to ES-16, ES-19) · **Gate:** none

###### EN-01 Convert the solution to SDK-style projects on net10.0

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 1 · **Parent:** FEAT-201 · **Serves:** FR-201, FR-203
* **Source:** (source: CS-01, CS-02, ES-13, ES-14, ES-19) · **Gate:** none
* **Story:** As a .NET developer, I want `Core`, `Web` and `Tests` converted to SDK-style projects on `net10.0` inside the one existing solution, so that the application builds on the current long-term support release.
* **Acceptance criteria:**
  * `EN-01/AC1` Given `src/Northwind.OrderDesk.sln`, When `dotnet build src/Northwind.OrderDesk.sln` runs, Then `Core` and `Tests` build as SDK-style projects targeting `net10.0`, no `packages.config` remains, and `Web` builds once `EN-08` is also done.
  * `EN-01/AC2` Given the solution, When its projects are listed, Then there is one solution and the same three projects (ES-13); namespaces and domain types are unchanged (ES-19).
  * `EN-01/AC3` Given a change would add a project, When it is proposed, Then a decision record (`EN-13`) must exist first; without it the change is rejected.
  * `EN-01/AC4` Given the database client, When the solution is built, Then it uses the current SQL client library.
* **Dependencies:** none; first .NET item. **Cross-track (OPEN):** X-02, X-14. **Relies on:** O-03, O-20.

###### EN-13 Record the decision on portal and API project shape

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 2 · **Parent:** FEAT-201 · **Serves:** FR-201
* **Source:** (source: ES-13, O-20) · **Gate:** none
* **Story:** As the .NET team lead, I want a decision record that says whether the portal is an area of `Web` or a new project and whether an API project exists, so that no project is added without a reason (ES-13).
* **Acceptance criteria:**
  * `EN-13/AC1` Given the decision, When the record is read, Then it is stored with the architecture decision records (`docs/architecture/`, ES-08) and states the choice, the reasons and the consequences.
  * `EN-13/AC2` Given no decision record exists, When anyone proposes a new project, Then it is not added (ES-13).
  * `EN-13/AC3` Given who owns the Order Desk API is unknown (O-01), When the record discusses an API project, Then it marks that part **OPEN:** and does not assume an owner.
* **Dependencies:** none. **Cross-track (OPEN):** X-14 (hosting shape is Azure's). **Relies on:** O-01, O-20; T-10.

###### EN-03 Replace direct ConfigurationManager calls with the options pattern

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 3 · **Parent:** FEAT-201 · **Serves:** FR-201
* **Source:** (source: CS-17, ES-15) · **Gate:** none
* **Story:** As a .NET developer, I want configuration read through `Microsoft.Extensions.Configuration` and the options pattern, so that the application takes settings from environment variables and the cloud, as the contract with Azure needs.
* **Acceptance criteria:**
  * `EN-03/AC1` Given the code base, When it is searched, Then no direct `ConfigurationManager` call remains (ES-15).
  * `EN-03/AC2` Given each setting that was read before, When the application starts with the same values, Then it behaves as before (a check covers each setting).
  * `EN-03/AC3` Given a required setting is missing, When the application starts, Then startup fails with a message that names the setting and never prints a secret value.
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-02. **Relies on:** none.

###### EN-05 Replace the Windows Event Log logger with standard logging

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 4 · **Parent:** FEAT-201 · **Serves:** FR-201
* **Source:** (source: CS-15, ES-16) · **Gate:** none
* **Story:** As a .NET developer, I want errors logged through `ILogger<T>` instead of the Windows Event Log, so that logging works on any machine and can later feed Azure monitoring.
* **Acceptance criteria:**
  * `EN-05/AC1` Given the code base, When it is searched, Then nothing writes to the Windows Event Log (ES-16).
  * `EN-05/AC2` Given the existing tests of logging behaviour, When `dotnet test` runs, Then they still pass and their coverage is kept.
  * `EN-05/AC3` Given an error on macOS or Linux, When it occurs, Then it appears in the console log.
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-08. **Relies on:** none.

###### EN-06 Replace the in-process session order draft

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 5 · **Parent:** FEAT-201 · **Serves:** FR-214
* **Source:** (source: CS-16) · **Gate:** none
* **Story:** As a .NET developer, I want the order being entered stored outside the web process, so that a restart or a second server does not lose it.
* **Acceptance criteria:**
  * `EN-06/AC1` Given a user has an order draft, When the application restarts or the next request goes to another instance, Then the draft is still there.
  * `EN-06/AC2` Given the code base, When it is searched, Then no `InProc` session state remains for the order draft (CS-16).
  * `EN-06/AC3` Given a draft that does not exist (for example removed), When the user opens it, Then a clear "draft not found" message is shown and no error page.
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-07 (Azure starts with a single instance, as today, until this is done). **Relies on:** none.

###### EN-08 Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 6 · **Parent:** FEAT-201 · **Serves:** FR-201, FR-204, FR-210, FR-220
* **Source:** (source: CS-04, NFR-04, ES-14, ES-19) · **Gate:** none
* **Story:** As a .NET developer, I want the web layer on ASP.NET Core MVC with Microsoft Entra ID sign-in for staff, so that the application no longer needs Windows Integrated Authentication or Windows-only hosting.
* **Acceptance criteria:**
  * `EN-08/AC1` Given the existing staff screens, When they are opened after the port, Then each shows the same fields and behaves as before; any difference is listed as a defect.
  * `EN-08/AC2` Given a Northwind staff member with a Microsoft Entra ID account, When they sign in (a test identity is used locally), Then they reach Order Desk; given an account that is not a Northwind staff account, Then sign-in is refused.
  * `EN-08/AC3` Given the code base, When it is searched, Then no Windows Integrated Authentication setting remains (CS-04).
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-04 (staff sign-in; .NET uses provider-neutral sign-in and a test identity). **Relies on:** A-10; O-03.

###### STORY-201 Run Order Desk on .NET 10 with unchanged staff screens

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Rank:** 7 · **Parent:** FEAT-201 · **Implements:** FR-201
* **Source:** (source: CS-01, CS-02, ES-13, ES-14, ES-19) · **Gate:** none
* **Story:** As an Order Desk staff member, I want Order Desk to run on the current .NET long-term support release with the screens I use today, so that my daily work does not change while the platform under it does.
* **Acceptance criteria:**
  * `STORY-201/AC1` Given the solution, When `dotnet build src/Northwind.OrderDesk.sln` runs, Then all three projects build on `net10.0`.
  * `STORY-201/AC2` Given each existing staff screen, When it is compared with the current application using a regression checklist, Then fields and behaviour are the same.
  * `STORY-201/AC3` Given a namespace, domain type or behaviour, When it is compared, Then it is unchanged unless a decision record explains the change (ES-19).
  * `STORY-201/AC4` Given a screen behaves differently from today, When the checklist is reviewed, Then the difference is a defect and the release is not approved until it is fixed or accepted by the product owner.
* **Dependencies:** `EN-01`, `EN-03`, `EN-05`, `EN-08`, `EN-13`. **Cross-track (OPEN):** X-14; hosting is X-01. **Relies on:** O-20.

##### FEAT-202 Test, build and local data

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Parent:** EPIC-201 · **Contains:** EN-02, EN-09, EN-12
* **Source:** (source: CS-18, CS-19, CS-20, ES-18, ES-27) · **Gate:** none

###### EN-02 Replace MSTest v1 so all tests run on Windows, macOS and Linux

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 8 · **Parent:** FEAT-202 · **Serves:** FR-202
* **Source:** (source: CS-18, CS-20, ES-18) · **Gate:** none
* **Story:** As a .NET developer, I want the unit tests moved off MSTest v1 (which only runs inside Visual Studio) to a current test framework, so that anyone can run them anywhere.
* **Acceptance criteria:**
  * `EN-02/AC1` Given any machine with the .NET SDK, When `dotnet test src/Northwind.OrderDesk.sln` runs on Windows, macOS and Linux, Then the tests run and pass (ES-18).
  * `EN-02/AC2` Given the existing tests (28 test assertions), When they are moved, Then all are kept and the pricing assertions are not weakened (CS-20).
  * `EN-02/AC3` Given a pricing test is changed in a way that accepts a wider result than before, When it is reviewed, Then it is rejected.
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-11. **Relies on:** none.

###### EN-09 Build an automated build and test pipeline

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 9 · **Parent:** FEAT-202 · **Serves:** all .NET releases
* **Source:** (source: CS-18, CS-19) · **Gate:** none
* **Story:** As a .NET developer, I want every change to be built and tested automatically, so that a developer no longer publishes from Visual Studio to a file share by hand (CS-19).
* **Acceptance criteria:**
  * `EN-09/AC1` Given a change to the solution, When it is submitted, Then the pipeline builds it and runs `dotnet test src/Northwind.OrderDesk.sln`.
  * `EN-09/AC2` Given a failing test or build, When the pipeline runs, Then the change is blocked and the failure is reported.
  * `EN-09/AC3` Given the pipeline definition, When the repository is scanned, Then it contains no secret (ES-17).
* **Dependencies:** `EN-02`. **Cross-track (OPEN):** X-11 (each track writes its own pipeline). **Relies on:** O-19.

###### EN-12 Provide local test data with orders and a local database recipe

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 10 · **Parent:** FEAT-202 · **Serves:** all local testing, MVE-02
* **Source:** (source: ES-27, ES-17, A-51) · **Gate:** none
* **Story:** As a .NET developer, I want local sample data that includes orders from several customers and a recipe to build a local database from the scripts in `database/`, so that every story can be tested without Azure and without real data.
* **Acceptance criteria:**
  * `EN-12/AC1` Given a clean machine with a local SQL Server, When the recipe is followed, Then a local database with the sample data is created from `database/` and the solution runs against it.
  * `EN-12/AC2` Given the sample data, When it is read, Then it contains orders for at least two different customers (so that isolation tests in `STORY-230` are possible) and no real customer or personal data.
  * `EN-12/AC3` Given the recipe, When the repository is scanned, Then it holds no password; credentials come from user secrets or environment variables (ES-17).
* **Dependencies:** none. **Cross-track (OPEN):** X-01 (.NET builds locally until pilot hosting is answered). **Relies on:** A-51; MVE-A-04.

##### FEAT-203 Pricing, channel and time parity

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Parent:** EPIC-201 · **Contains:** EN-10, STORY-202, STORY-203, STORY-206
* **Source:** (source: BR-10, BR-12, BR-02, CS-20) · **Gate:** none

###### EN-10 Make time handling explicit and tested

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 11 · **Parent:** FEAT-203 · **Serves:** FR-202, FR-206, FR-211, FR-218
* **Source:** (source: CS-20, A-24) · **Gate:** none
* **Story:** As a .NET developer, I want one clock and one written rule for stored and compared times, so that the application gives the same results in local time and in the cloud's default time (UTC).
* **Acceptance criteria:**
  * `EN-10/AC1` Given the same input, When the tests run with the host time zone set to UTC and to Central European time, Then order dates, the 24-month window and price-agreement validity give identical results.
  * `EN-10/AC2` Given a price agreement that ends at midnight local time, When it is checked at the minute before and the minute after, Then it is valid before and not valid after, in both time zones.
  * `EN-10/AC3` Given the rule, When it is read, Then it states whether times are stored in UTC or in local time (ASSUMPTION: A-24 describes the current behaviour and needs confirmation).
* **Dependencies:** `EN-02`. **Cross-track (OPEN):** none. **Relies on:** A-24.

###### STORY-202 Keep pricing identical to today (pricing parity)

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Rank:** 12 · **Parent:** FEAT-203 · **Implements:** FR-202 · **Covers:** BR-12 (parity side)
* **Source:** (source: BR-12, CS-20, ES-18) · **Gate:** none
* **Story:** As an Order Desk staff member, I want the modernised Order Desk to give the same price as today for the same customer, product, quantity and date, so that negotiated prices and volume discounts do not change by accident.
* **Acceptance criteria:**
  * `STORY-202/AC1` Given the same customer, product, quantity and date, When the price is computed in the modernised application, Then it equals the price computed by the current application, including customer-negotiated prices and volume discounts.
  * `STORY-202/AC2` Given the existing pricing checks, When `dotnet test src/Northwind.OrderDesk.sln` runs, Then all pass and no assertion is weakened.
  * `STORY-202/AC3` Given any price differs, even by one cent, When the comparison is run, Then it is a defect and the release is not approved until it is fixed.
* **Dependencies:** `EN-02`, `EN-10`. **Cross-track (OPEN):** none. **Relies on:** none.

###### STORY-203 Keep the order channel visible to staff (channel parity)

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Rank:** 13 · **Parent:** FEAT-203 · **Implements:** FR-203 · **Covers:** BR-10 (parity side)
* **Source:** (source: BR-10, BR-06; **ASSUMPTION:** A-51) · **Gate:** none
* **Story:** As an Order Desk staff member, I want to see for every order whether it was placed through the portal or entered by staff, as I do today, so that I know where an order came from.
* **Acceptance criteria:**
  * `STORY-203/AC1` Given an order entered by staff, When staff open it, Then its channel is shown as entered by staff.
  * `STORY-203/AC2` Given a test order with the channel value for the portal, When staff open it, Then its channel is shown as portal.
  * `STORY-203/AC3` Given an order with an empty channel value, When staff open it, Then the screen behaves as the current screen does and does not fail; any difference from today is listed.
* **Dependencies:** `EN-01`. **Cross-track (OPEN):** none. **Relies on:** A-51.

###### STORY-206 Keep dates and price validity identical in any time zone (time parity)

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Rank:** 14 · **Parent:** FEAT-203 · **Implements:** FR-206
* **Source:** (source: BR-02, BR-12, CS-20; **ASSUMPTION:** A-24) · **Gate:** none
* **Story:** As an Order Desk staff member, I want order dates, the 24-month history window and price-agreement validity to be the same whether the application runs in local time or in the cloud's default time, so that a move to Azure never shifts an order or a price.
* **Acceptance criteria:**
  * `STORY-206/AC1` Given an order placed at 23:30 local time, When the application runs with the host time zone set to UTC and to Central European time, Then its order date is the same.
  * `STORY-206/AC2` Given an order exactly 24 months old at the edge of the window, When the list is built in each time zone, Then the same orders are shown.
  * `STORY-206/AC3` Given a price agreement whose last day is today, When a price is requested in each time zone, Then the same price is returned.
* **Dependencies:** `EN-10`. **Cross-track (OPEN):** none. **Note:** supports `BR-02` and `BR-12`; those are covered in `dotnet-r2` (STORY-231, STORY-238). **Relies on:** A-24.

##### FEAT-204 Staff sign-in with Entra ID

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Parent:** EPIC-201 · **Contains:** STORY-204
* **Source:** (source: NFR-04, CS-04, G-03) · **Gate:** none

###### STORY-204 Sign staff in with Microsoft Entra ID

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must (A-06) · **Rank:** 15 · **Parent:** FEAT-204 · **Implements:** FR-204 · **Covers:** NFR-04 (staff side)
* **Source:** (source: NFR-04, CS-04, G-03) · **Gate:** none
* **Story:** As a Northwind staff member, I want to sign in to Order Desk with my Microsoft Entra ID account, so that I no longer depend on Windows Integrated Authentication against the on-premises domain.
* **Acceptance criteria:**
  * `STORY-204/AC1` Given a staff member with a Northwind Entra ID account, When they sign in, Then they reach Order Desk with no separate password stored by the application.
  * `STORY-204/AC2` Given the code base, When it is searched, Then no Windows Integrated Authentication remains.
  * `STORY-204/AC3` Given an account that is not a Northwind staff account, When it tries to sign in, Then access is refused.
* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04 (the Azure side of sign-in stays **OPEN:**; .NET uses a test identity locally). **Relies on:** A-10; O-03.

##### FEAT-205 Secret-free configuration

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must · **Parent:** EPIC-201 · **Contains:** EN-04, STORY-205
* **Source:** (source: NFR-05, CS-13, ES-17, ES-25) · **Gate:** none

###### EN-04 Remove Windows sign-in and server names from database configuration

* **Tags:** `track-dotnet` `dotnet-r1` · **Type:** enabler · **Priority:** Must (A-49: protects NFR-05) · **Rank:** 16 · **Parent:** FEAT-205 · **Serves:** FR-205
* **Source:** (source: CS-13, NFR-05, ES-17, ES-25) · **Gate:** none
* **Story:** As a .NET developer, I want the database connection to carry no Windows-integrated sign-in and no server name in configuration, so that the same code runs locally (secrets from user secrets or environment variables) and in Azure (managed identity).
* **Acceptance criteria:**
  * `EN-04/AC1` Given the repository, When it is searched, Then `Integrated Security=SSPI` and the server name `NWSQL01` appear in no configuration file (CS-13).
  * `EN-04/AC2` Given a developer machine, When the application starts, Then it reads the connection setting from user secrets or an environment variable.
  * `EN-04/AC3` Given the connection setting is missing, When the application starts, Then it fails with a message naming the setting and prints no value.
* **Dependencies:** `EN-03`. **Cross-track (OPEN):** X-03 (database sign-in moves to Entra or a managed identity; .NET builds against a local SQL Server). **Relies on:** none.

###### STORY-205 Keep secrets out of code, tests and configuration

* **Tags:** `track-dotnet` `dotnet-r1` · **Priority:** Must (A-06) · **Rank:** 17 · **Parent:** FEAT-205 · **Implements:** FR-205 · **Covers:** NFR-05 (.NET side)
* **Source:** (source: NFR-05, CS-13, ES-17) · **Gate:** none
* **Story:** As the IT manager, I want the modernised application and its tests to hold no secret in source code or in configuration files in the repository, so that a leaked repository exposes no credential.
* **Acceptance criteria:**
  * `STORY-205/AC1` Given the release content, When a scan of source and configuration files (including tests) runs as part of the release exit criteria, Then it finds no password, key or connection string with a password.
  * `STORY-205/AC2` Given the application runs locally, When it needs a secret, Then it comes from user secrets or an environment variable; given it runs in Azure, Then it uses a managed identity.
  * `STORY-205/AC3` Given the scan finds a secret, When the release is considered for approval, Then it is not approved until the secret is removed.
* **Dependencies:** `EN-04`. **Cross-track (OPEN):** X-02, X-03. **Relies on:** A-54.

---

#### EPIC-202 Customer portal pilot: sign-in, orders, status, reorder

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Features:** FEAT-206, FEAT-207, FEAT-208, FEAT-209, FEAT-210
* **Source:** (source: BR-01 to BR-06, BR-10, BR-11, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08, C-05, CS-10)
* **Gate:** **MVE-02** (customers reorder unaided and trust a status refreshed once a night; pass thresholds `R1` at least 80 % finish a reorder unaided, `R2` at least 60 % would use the status instead of phoning, **ASSUMPTION:** A-35). Applies to the stories for `BR-04`, `BR-05`, `BR-10` and `BR-12` (`STORY-233`, `STORY-234`, `STORY-236`, `STORY-238`). Result **pending**.
* **Goal:** A Must-only pilot for 20 customers: sign in, see own orders, follow status, reorder, with the quality requirements (isolation, residency, accessibility, performance, audit).
* **Cross-track (OPEN):** X-01, X-04 (customers), X-05, X-06, X-13, X-15, O-23, A-37. **Relies on:** A-03, A-10, A-16, A-17, A-19; O-04, O-08, O-10, O-16, O-24.

##### FEAT-206 Customer sign-in, company isolation and data residency

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Parent:** EPIC-202 · **Contains:** EN-11, STORY-230, STORY-240, STORY-239
* **Source:** (source: BR-01, NFR-03, NFR-04, CS-04, CS-05) · **Gate:** none

###### EN-11 Build the authorisation foundation for customer scoping and channel

* **Tags:** `track-dotnet` `dotnet-r2` · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 18 · **Parent:** FEAT-206 · **Serves:** FR-210, FR-216
* **Source:** (source: BR-01, BR-10; **ASSUMPTION:** A-51) · **Gate:** MVE-02 (for the channel part, `BR-10`)
* **Story:** As a .NET developer, I want server-side checks that scope every read to the signed-in customer's company, check the role when an order status is changed and set the order channel on the server, so that the portal cannot show another company's data or accept a forged channel.
* **Acceptance criteria:**
  * `EN-11/AC1` Given a signed-in user of company A, When a request asks for an order, an order list or an invoice of company B, Then it is refused and no data of company B is returned.
  * `EN-11/AC2` Given a user who is not Order Desk staff, When they try to change an order status, Then the change is refused (the current code has no such check, A-51).
  * `EN-11/AC3` Given a request that contains a channel value, When the order is created, Then the server ignores the value and sets the channel from the way the order arrived.
* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04. **Relies on:** A-51.

###### STORY-230 Sign in and see only my own company's orders

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 19 · **Parent:** FEAT-206 · **Implements:** FR-210 · **Covers:** BR-01
* **Source:** (source: BR-01, CS-04, CS-05; **ASSUMPTION:** A-51) · **Gate:** none
* **Story:** As a customer user, I want to sign in and see only the orders of my own company, so that my company's orders stay private from other customers.
* **Acceptance criteria:**
  * `STORY-230/AC1` Given a customer user of company A, When they sign in and open the order list, Then every order shown belongs to company A.
  * `STORY-230/AC2` **Negative case:** Given a signed-in user of company A, When they ask for an order of company B (for example by changing the order number in the web address), Then the portal refuses the request and shows no data from company B.
  * `STORY-230/AC3` Given a signed-in user of company A, When they ask for the order list, Then no row of company B appears in it.
  * `STORY-230/AC4` Given sign-in fails (unknown user or wrong credentials), When the user tries to open any order page, Then no order data is shown.
* **Dependencies:** `EN-11`, `EN-08`, `EN-12`. **Cross-track (OPEN):** X-01, X-04. **Relies on:** A-10, A-19; O-10.

###### STORY-240 Authenticate customers with an externally managed identity

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must (A-06) · **Rank:** 20 · **Parent:** FEAT-206 · **Implements:** FR-220 · **Covers:** NFR-04 (customer side)
* **Source:** (source: NFR-04, OQ-01, CS-28) · **Gate:** none
* **Story:** As the IT manager, I want customer users to authenticate with an identity managed outside the application, so that the application stores no customer password.
* **Acceptance criteria:**
  * `STORY-240/AC1` Given a customer user known to the identity service, When they sign in, Then they are authenticated by the external identity and the application stores no password for them.
  * `STORY-240/AC2` Given local builds and experiments, When sign-in is tested, Then a test identity is used and no real customer account is needed.
  * `STORY-240/AC3` Given the identity provider is not decided (OQ-01), When the story is built, Then sign-in does not depend on one provider (A-10).
  * `STORY-240/AC4` Given a user not known to the identity service, When they try to sign in, Then access is refused.
* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04. **Relies on:** A-10; O-10, O-24.

###### STORY-239 Keep portal hosting, identity and mail data in the EU

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must (A-06) · **Rank:** 21 · **Parent:** FEAT-206 · **Implements:** FR-219 · **Covers:** NFR-03 (.NET side)
* **Source:** (source: NFR-03, ES-20) · **Gate:** none
* **Story:** As the IT manager, I want the portal's hosting, the identity service that holds customer sign-ins and outbound mail to keep customer data and order data in the EU, so that the portal meets the residency requirement.
* **Acceptance criteria:**
  * `STORY-239/AC1` Given the portal design, When every service it uses (hosting, identity service, outbound mail) is listed with its region, Then each is in the EU.
  * `STORY-239/AC2` Given an identity or mail service that holds data outside the EU, When the list is reviewed, Then it is not accepted and the owner of O-24 is told.
  * `STORY-239/AC3` Given the cost of the identity service counts toward C-04 or not is unknown (O-24), When the list is read, Then that question is marked **OPEN:**.
* **Dependencies:** `STORY-240`. **Cross-track (OPEN):** X-13 (internet-facing entry while data services stay private; Azure designs the entry). **Relies on:** T-15; O-24.

##### FEAT-207 Order list, order detail and status

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Parent:** EPIC-202 · **Contains:** STORY-231, STORY-232, STORY-233
* **Source:** (source: BR-02, BR-03, BR-04, P-03, CS-10) · **Gate:** MVE-02 (`STORY-233`)

###### STORY-231 See my company's orders from the last 24 months

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 22 · **Parent:** FEAT-207 · **Implements:** FR-211 · **Covers:** BR-02
* **Source:** (source: BR-02, P-03) · **Gate:** none
* **Story:** As a customer user, I want to see the list of my company's orders from the last 24 months with order date, status and total, so that I can find an order without phoning the Order Desk.
* **Acceptance criteria:**
  * `STORY-231/AC1` Given company A has orders, When a user of company A opens the list, Then each order from the last 24 months is shown with its order date, status and total.
  * `STORY-231/AC2` Given an order older than 24 months, When the list is shown, Then it is not listed (24 months is a display window over the complete history, A-16).
  * `STORY-231/AC3` Given company A has no orders in the last 24 months, When the list is opened, Then an empty-list message is shown and no error.
* **Dependencies:** `EN-10`, `EN-11`. **Cross-track (OPEN):** none. **Relies on:** A-16; O-08.

###### STORY-232 Open an order and see lines, prices, address and status

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 23 · **Parent:** FEAT-207 · **Implements:** FR-212 · **Covers:** BR-03
* **Source:** (source: BR-03, P-03) · **Gate:** none
* **Story:** As a customer user, I want to open an order and see its lines, quantities, prices, delivery address and current status, so that I can check what was ordered and where it goes.
* **Acceptance criteria:**
  * `STORY-232/AC1` Given an order of the user's company, When the user opens it, Then it shows each line with product, quantity and price, the delivery address and the current status.
  * `STORY-232/AC2` Given the prices shown, When they are compared with `STORY-238`, Then they are the customer's negotiated prices.
  * `STORY-232/AC3` Given an order that belongs to another company, When the user opens its address, Then the request is refused (see `STORY-230/AC2`).
* **Dependencies:** `EN-11`. **Cross-track (OPEN):** none. **Relies on:** none.

###### STORY-233 See one of six order statuses with an as-of time

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 24 · **Parent:** FEAT-207 · **Implements:** FR-213 · **Covers:** BR-04
* **Source:** (source: BR-04, P-03, CS-10, C-03) · **Gate:** **MVE-02** (`R2`: at least 60 % would use the status instead of phoning)
* **Story:** As a customer user, I want to see the status of an order as one of Received, Confirmed, Picking, Shipped, Delivered or Cancelled, with the time it was last updated, so that I know how current the status is before I decide to phone.
* **Acceptance criteria:**
  * `STORY-233/AC1` Given any order, When the user opens it, Then its status is exactly one of Received, Confirmed, Picking, Shipped, Delivered, Cancelled.
  * `STORY-233/AC2` Given the status is Picking or Shipped, When it is shown, Then it carries an "as of" date and time equal to the time of the last nightly StockPilot update (A-03).
  * `STORY-233/AC3` Given the status is Received, Confirmed or Cancelled, When it is shown, Then it is current as of Order Desk and carries the time of the last change.
  * `STORY-233/AC4` Given an order is shipped in the warehouse after the 02:00 batch, When the customer views it before the next night's run, Then the portal still shows the previous status with its "as of" time and does not claim to be live (T-01).
  * `STORY-233/AC5` Given staff set an order to Delivered in Order Desk, When the customer opens it, Then the portal shows Delivered.
* **Dependencies:** none inside the track. **Cross-track (OPEN):** X-05, X-06 (freshness is bounded by the exchange cadence; .NET shows the "as of" time). **Relies on:** A-03; O-04, O-16; T-01.

##### FEAT-208 Reorder, submit and channel

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Parent:** EPIC-202 · **Contains:** STORY-234, STORY-235, STORY-236
* **Source:** (source: BR-05, BR-06, BR-10, C-05, P-01, P-02, P-04) · **Gate:** MVE-02 (`STORY-234`, `STORY-236`)

###### STORY-234 Create a new order by copying a previous order

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 25 · **Parent:** FEAT-208 · **Implements:** FR-214 · **Covers:** BR-05
* **Source:** (source: BR-05, P-04) · **Gate:** **MVE-02** (`R1`: at least 80 % finish a reorder unaided)
* **Story:** As a customer user, I want to create a new order by copying a previous order, changing quantities or removing lines and then submitting it, so that I do not have to dictate or retype the whole list.
* **Acceptance criteria:**
  * `STORY-234/AC1` Given a previous order of my company, When I choose to copy it, Then a new draft is created with the same lines and quantities.
  * `STORY-234/AC2` Given a draft, When I change a quantity or remove a line and submit, Then the submitted order has exactly my changes.
  * `STORY-234/AC3` Given I am preparing a draft, When the server restarts or my next request is handled by another instance, Then my draft is not lost (`EN-06`).
  * `STORY-234/AC4` Given a draft with no lines, When I try to submit, Then the submission is refused with a message and no order is created.
* **Dependencies:** `EN-06`, `EN-11`. **Cross-track (OPEN):** X-07. **Relies on:** O-28 (**OPEN:** the rule for a copied line whose product is no longer available is not in the sources).

###### STORY-235 Have a submitted portal order appear in Order Desk as Received

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 26 · **Parent:** FEAT-208 · **Implements:** FR-215 · **Covers:** BR-06
* **Source:** (source: BR-06, C-05, P-01, P-02) · **Gate:** none
* **Story:** As an Order Desk staff member, I want a submitted portal order to appear in Order Desk with the status Received without being re-keyed, so that I stop retyping orders and the correction rate falls.
* **Acceptance criteria:**
  * `STORY-235/AC1` Given a customer submits an order in the portal, When staff open Order Desk, Then the order is there with the status Received and nobody has re-keyed it.
  * `STORY-235/AC2` Given the portal, When its data access is reviewed, Then it reads and writes orders only through Order Desk and no second order database exists (C-05).
  * `STORY-235/AC3` Given Order Desk cannot take the order at the time of submission, When the customer submits, Then the customer is told the order was not submitted and no partial order exists.
* **Dependencies:** `STORY-234`. **Cross-track (OPEN):** X-01 (the pilot reads the database named in O-23). **Relies on:** A-37; O-23; T-08.

###### STORY-236 Show staff whether an order came from the portal or from staff

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 27 · **Parent:** FEAT-208 · **Implements:** FR-216 · **Covers:** BR-10 (portal value)
* **Source:** (source: BR-10, BR-06; **ASSUMPTION:** A-51) · **Gate:** **MVE-02**
* **Story:** As an Order Desk staff member, I want to see whether an order was placed through the portal or entered by staff, so that I can handle portal orders knowing where they came from.
* **Acceptance criteria:**
  * `STORY-236/AC1` Given a customer submits an order in the portal, When staff open it, Then its channel is portal.
  * `STORY-236/AC2` Given an order entered by staff, When staff open it, Then its channel is staff.
  * `STORY-236/AC3` Given a request from a customer that carries any channel value, When the order is created, Then the server sets the channel to portal and the customer cannot choose it (`EN-11/AC3`).
* **Dependencies:** `EN-11`. **Cross-track (OPEN):** none. **Relies on:** A-51.

##### FEAT-209 Customer prices and language

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Parent:** EPIC-202 · **Contains:** STORY-238, STORY-237
* **Source:** (source: BR-11, BR-12, CS-20, OQ-02) · **Gate:** MVE-02 (`STORY-238`)

###### STORY-238 Show my negotiated prices, not list prices

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Rank:** 28 · **Parent:** FEAT-209 · **Implements:** FR-218 · **Covers:** BR-12 (customer prices)
* **Source:** (source: BR-12, CS-20) · **Gate:** **MVE-02**
* **Story:** As a customer user, I want to see my own negotiated prices and not the list price, so that what I see is what I will be invoiced.
* **Acceptance criteria:**
  * `STORY-238/AC1` Given a customer with a negotiated price for a product, When they view an order, a draft or the order list total, Then the negotiated price is shown and not the list price.
  * `STORY-238/AC2` Given a price for the same customer, product, quantity and date, When it is compared with the staff screens, Then it is identical (`STORY-202`).
  * `STORY-238/AC3` Given the pricing rules cannot return a price for a line, When the portal shows the line, Then it shows an error for that line and never falls back to the list price.
* **Dependencies:** `EN-10`, `STORY-202`. **Cross-track (OPEN):** none. **Relies on:** none.

###### STORY-237 Use the portal in French and English

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Should · **Rank:** 29 · **Parent:** FEAT-209 · **Implements:** FR-217 · **Covers:** BR-11 (French and English)
* **Source:** (source: BR-11, OQ-02) · **Gate:** none
* **Story:** As a customer user, I want the portal in French or English, so that I can use it in my working language.
* **Acceptance criteria:**
  * `STORY-237/AC1` Given any pilot screen, When the user selects French or English, Then all text of the screen appears in the selected language.
  * `STORY-237/AC2` Given a pilot screen has a text without a translation, When the screens are reviewed, Then it is listed and fixed before the release is approved.
  * `STORY-237/AC3` Given a user whose preference is Dutch, When they open the portal, Then Dutch is not offered in `dotnet-r2` (see `STORY-263`) and French or English remains available.
* **Dependencies:** none. **Cross-track (OPEN):** none. **Relies on:** A-11; O-11, O-18.

##### FEAT-210 Audit, accessibility and performance

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must · **Parent:** EPIC-202 · **Contains:** STORY-241, STORY-242, STORY-243
* **Source:** (source: NFR-02, NFR-07, NFR-08, CS-03, CS-05, ES-19) · **Gate:** none

###### STORY-241 Record who, what, when and channel for every order change

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must (A-06) · **Rank:** 30 · **Parent:** FEAT-210 · **Implements:** FR-221 · **Covers:** NFR-08 (content)
* **Source:** (source: NFR-08, ES-19; **ASSUMPTION:** A-51) · **Gate:** none
* **Story:** As the product owner, I want every change to an order, by a customer or by staff, to record who, what, when and channel, so that the 7-year audit record is complete.
* **Acceptance criteria:**
  * `STORY-241/AC1` Given a change to an order by a customer or by staff, When the audit record is read, Then it shows who, what, when and channel.
  * `STORY-241/AC2` Given a sample of order changes, When the audit records are checked, Then each of the four fields is present.
  * `STORY-241/AC3` Given today's record is incomplete (the channel is recorded only on creation and the shipment import writes audit rows for unchanged orders, A-51), When the gap is found, Then it is listed for the product owner to decide and is not changed silently (ES-19).
* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-15 (Azure sets the 7-year retention). **Relies on:** A-31, A-51; T-13.

###### STORY-242 Check every pilot screen against WCAG 2.2 level AA

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must (A-06) · **Rank:** 31 · **Parent:** FEAT-210 · **Implements:** FR-222 · **Covers:** NFR-07
* **Source:** (source: NFR-07) · **Gate:** none
* **Story:** As a customer user who relies on a keyboard or a screen reader, I want every pilot screen to meet WCAG 2.2 level AA, so that I can use the portal.
* **Acceptance criteria:**
  * `STORY-242/AC1` Given every pilot screen, When automated checks and a manual keyboard and screen-reader review run against the WCAG 2.2 AA success criteria, Then the findings are recorded per screen (A-54).
  * `STORY-242/AC2` Given a failure is found, When the release is considered for approval, Then it is fixed or listed with the reason it stays.
  * `STORY-242/AC3` Given the review is done, When the result is reported, Then it does not claim conformance, because a conformance statement needs a qualified accessibility reviewer.
* **Dependencies:** none. **Cross-track (OPEN):** none. **Relies on:** A-54.

###### STORY-243 Respond in under 2 seconds at the 95th percentile

* **Tags:** `track-dotnet` `dotnet-r2` · **Priority:** Must (A-06) · **Rank:** 32 · **Parent:** FEAT-210 · **Implements:** FR-223 · **Covers:** NFR-02
* **Source:** (source: NFR-02, CS-03, CS-05) · **Gate:** none
* **Story:** As a customer user, I want the order list and order detail pages to respond quickly, so that checking an order is faster than phoning.
* **Acceptance criteria:**
  * `STORY-243/AC1` Given the order list and order detail pages, When response time is measured **on the server** at the 95th percentile, Then it is under 2 seconds for 95 % of requests (A-05).
  * `STORY-243/AC2` Given the load model, When the measurement runs, Then it uses about 60 concurrent staff users at peak (CS-03) plus the agreed pilot customer figure (**OPEN:** O-08, A-17) and today's data volume (about 14,000 order lines a week, CS-05).
  * `STORY-243/AC3` Given the 95th percentile is 2 seconds or more, When the result is reported, Then `NFR-02` is recorded as not met and the cause is listed; the release is not approved on this criterion.
* **Dependencies:** `EN-10`. **Cross-track (OPEN):** X-12 (Azure sizes from today's load). **Relies on:** A-05, A-17; O-08.

---

#### EPIC-203 Complete the portal and publish the Order Desk API contract

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Features:** FEAT-211, FEAT-212, FEAT-213, FEAT-214
* **Source:** (source: BR-07, BR-08, BR-09, BR-11, SM-01 to SM-04, CS-27, ES-36, G-01)
* **Gate:** **MVE-02** for the instrumentation (`STORY-264`, `SM-01` to `SM-04`). Result **pending**.
* **Goal:** Add invoices, user administration, e-mail and Dutch after pilot feedback, record the data for the success measures and publish the read-only API contract that another track can build against.
* **Cross-track (OPEN):** X-06, X-09, X-10; X-20, X-21 outbound (the contract `EN-14` serves BA-03). **Relies on:** A-03, A-04, A-11, A-12, A-15, A-19, A-29, A-52; O-01, O-05, O-11, O-12, O-15, O-17, O-18, O-26.

##### FEAT-211 Invoice download

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Parent:** EPIC-203 · **Contains:** EN-07, STORY-260
* **Source:** (source: BR-07, CS-08, CS-11, CS-14, P-05) · **Gate:** none

###### EN-07 Abstract the invoice store

* **Tags:** `track-dotnet` `dotnet-r3` · **Type:** enabler · **Priority:** Should (A-49) · **Rank:** 33 · **Parent:** FEAT-211 · **Serves:** FR-230
* **Source:** (source: CS-14, CS-11, A-15) · **Gate:** none
* **Story:** As a .NET developer, I want invoice access behind an interface with a local-folder provider, so that the code no longer depends on a network path and a storage provider can be added later.
* **Acceptance criteria:**
  * `EN-07/AC1` Given the interface, When the application runs with the local-folder provider on a developer machine, Then an invoice is read without a UNC path (CS-14).
  * `EN-07/AC2` Given an invoice number and year, When the path is built, Then it follows `{year}\{invoiceNumber}.pdf` and the rule for which year is used is written down (A-15).
  * `EN-07/AC3` Given the file does not exist, When it is requested, Then the interface returns a "not found" result and no exception reaches the user.
* **Dependencies:** none. **Cross-track (OPEN):** X-09 (Azure designs storage and synchronisation). **Relies on:** A-15; O-15.

###### STORY-260 Download the PDF invoice of a delivered order

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Rank:** 34 · **Parent:** FEAT-211 · **Implements:** FR-230 · **Covers:** BR-07
* **Source:** (source: BR-07, P-05, CS-08, CS-11) · **Gate:** none
* **Story:** As a customer user, I want to download the PDF invoice of a delivered order, so that I do not have to ask the Order Desk to e-mail me a copy.
* **Acceptance criteria:**
  * `STORY-260/AC1` Given an order with the status Delivered and an invoice, When I open it, Then a download of the PDF invoice is offered and delivers the file.
  * `STORY-260/AC2` Given an order that is not Delivered, When I open it, Then no invoice download is offered.
  * `STORY-260/AC3` Given an invoice of another company's order, When I request it, Then the request is refused (`EN-11/AC1`).
  * `STORY-260/AC4` Given the PDF cannot be found, When I request it, Then a message says the invoice is not available yet and the miss is logged.
* **Dependencies:** `EN-07`, `EN-11`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-08, O-15.

##### FEAT-212 Customer user administration and shipping e-mail

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Parent:** EPIC-203 · **Contains:** STORY-261, STORY-262
* **Source:** (source: BR-08, BR-09, OQ-03, CS-10, CS-12) · **Gate:** none

###### STORY-261 Invite and remove users of my own company

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Rank:** 35 · **Parent:** FEAT-212 · **Implements:** FR-231 · **Covers:** BR-08
* **Source:** (source: BR-08, OQ-03) · **Gate:** none
* **Story:** As a customer administrator, I want to invite and remove users of my own company, so that I manage my colleagues' access without asking Northwind staff.
* **Acceptance criteria:**
  * `STORY-261/AC1` Given I am a customer administrator, When I invite a colleague of my company, Then the colleague can sign in and sees only my company's orders.
  * `STORY-261/AC2` Given I am a customer administrator, When I remove a user of my company, Then that user can no longer sign in.
  * `STORY-261/AC3` Given I am a customer administrator, When I try to invite or remove a user of another company, Then the request is refused.
  * `STORY-261/AC4` Given I am not a customer administrator, When I open the portal, Then no user-administration screen is offered.
* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-10 if the invitation is sent by e-mail (mail abstraction and a local mail catcher meanwhile). **Relies on:** A-12, A-19; O-12 (**OPEN:** who receives the administrator role).

###### STORY-262 Receive an e-mail when an order changes to Shipped

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Could · **Rank:** 36 · **Parent:** FEAT-212 · **Implements:** FR-232 · **Covers:** BR-09
* **Source:** (source: BR-09, P-03, CS-10, CS-12) · **Gate:** none
* **Story:** As a customer user, I want an e-mail when one of my orders changes to Shipped, so that I know without opening the portal.
* **Acceptance criteria:**
  * `STORY-262/AC1` Given an order changes to Shipped in Order Desk, When Order Desk learns of the change, Then the customer user receives an e-mail.
  * `STORY-262/AC2` Given the Shipped status is set by the nightly StockPilot update, When the e-mail is sent, Then it arrives after that run and states the "as of" time; it is not promised at the moment of physical shipment (A-03).
  * `STORY-262/AC3` Given the mail service fails, When the order changes to Shipped, Then the order status is unaffected and the failure is logged.
  * `STORY-262/AC4` Given no customer e-mail address is known for the user, When the order changes to Shipped, Then no e-mail is sent and the gap is logged (O-18).
* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-10 (the Azure mail design `EA-12` is a different track's work and is never waited for) (mail abstraction and a local mail catcher meanwhile), X-06. **Relies on:** A-03, A-29; O-17, O-18.

##### FEAT-213 Dutch and success-measure data

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Parent:** EPIC-203 · **Contains:** STORY-263, STORY-264
* **Source:** (source: BR-11, SM-01 to SM-04, OQ-02) · **Gate:** MVE-02 (`STORY-264`)

###### STORY-263 Use the portal in Dutch

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Rank:** 37 · **Parent:** FEAT-213 · **Implements:** FR-233 · **Covers:** BR-11 (Dutch)
* **Source:** (source: BR-11, OQ-02) · **Gate:** none
* **Story:** As a Belgian customer user, I want the portal in Dutch, so that I can use it in my working language.
* **Acceptance criteria:**
  * `STORY-263/AC1` Given any portal screen, When I select Dutch, Then all text of the screen appears in Dutch.
  * `STORY-263/AC2` Given Dutch is added, When I select French or English, Then those languages are unchanged.
  * `STORY-263/AC3` Given a screen has text without a Dutch translation, When the screens are reviewed, Then it is listed and fixed before the release is approved.
* **Dependencies:** `STORY-237`. **Cross-track (OPEN):** none. **Relies on:** A-11; O-11, O-18.

###### STORY-264 Record data to compare SM-01 to SM-04 with their baselines

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should (A-52) · **Rank:** 38 · **Parent:** FEAT-213 · **Implements:** FR-234 · **Supports:** SM-01, SM-02, SM-03, SM-04 (supplementary, not required by ES-06)
* **Source:** (source: SM-01, SM-02, SM-03, SM-04; **ASSUMPTION:** A-52) · **Gate:** **MVE-02** (instrumentation)
* **Story:** As the head of Customer Operations, I want the portal to record or expose the data that I need to compare the portal success measures with their baselines, so that I can tell after general availability whether they are met.
* **Acceptance criteria:**
  * `STORY-264/AC1` Given the data agreed under O-26 for `SM-01`, `SM-03` and `SM-04`, When a reporting period is chosen, Then the portal records or exposes those data for the period.
  * `STORY-264/AC2` Given `SM-02` counts calls handled by staff, When the data are described, Then the story states that those calls are counted outside the product.
  * `STORY-264/AC3` Given O-26 has not named which data and from which source, When the story is considered, Then it is not started and stays Draft.
* **Dependencies:** none inside the track. **Cross-track (OPEN):** none. **Relies on:** A-04, A-52; O-05, O-26.

##### FEAT-214 Order Desk API contract

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Parent:** EPIC-203 · **Contains:** EN-14, STORY-265
* **Source:** (source: CS-27, ES-36, G-01) · **Gate:** none

###### EN-14 Publish the read-only Order Desk API contract (OpenAPI 2.0)

* **Tags:** `track-dotnet` `dotnet-r3` · **Type:** enabler · **Priority:** Should (A-49: serves another track) · **Rank:** 39 · **Parent:** FEAT-214 · **Serves:** FR-235, FR-240
* **Source:** (source: CS-27, ES-36, G-01) · **Gate:** none
* **Story:** As a .NET developer, I want a read-only contract for orders and order lines written as an OpenAPI 2.0 document, so that another track can design against it before any implementation exists.
* **Acceptance criteria:**
  * `EN-14/AC1` Given the contract file, When it is validated locally, Then it is a valid OpenAPI 2.0 document (ES-36).
  * `EN-14/AC2` Given the contract, When its operations are listed, Then every operation only reads and none creates, changes or deletes an order.
  * `EN-14/AC3` Given the fields X-21 asks for (order number, lines, quantities, prices, customer, warehouse), When the contract is read, Then each is present; the warehouse field is marked as not available while its source is unknown (A-18, X-25), and no value is invented.
  * `EN-14/AC4` Given the contract, When it is read, Then it contains no implementation and carries a placeholder security definition (X-23).
* **Dependencies:** none. **Cross-track (OPEN):** X-20, X-21 outbound (BA-03 designs against a stub meanwhile). **Relies on:** A-18; O-01.

###### STORY-265 Let another track build against the published order contract

* **Tags:** `track-dotnet` `dotnet-r3` · **Priority:** Should · **Rank:** 40 · **Parent:** FEAT-214 · **Implements:** FR-235
* **Source:** (source: CS-27, ES-36, G-01) · **Gate:** none
* **Story:** As a developer on another delivery track (for example the Power Platform track), I want a published read-only contract for orders and order lines, so that I can build a connector against it without access to the Order Desk database.
* **Acceptance criteria:**
  * `STORY-265/AC1` Given the contract is published in the repository, When another track reads it, Then it describes how to read one order and its lines by order number and follows OpenAPI 2.0.
  * `STORY-265/AC2` Given the contract, When it is reviewed, Then it excludes any operation that writes data and excludes the implementation.
  * `STORY-265/AC3` Given the owner of the implementation is unknown (O-01), When the release file is written, Then it states that the contract is published and the implementation is `EPIC-204`, unplanned.
* **Dependencies:** `EN-14`. **Cross-track (OPEN):** X-20, X-21. **Relies on:** O-01.

---

#### EPIC-204 Order Desk API implementation for other tracks

* **Tags:** `track-dotnet` · **Release:** unplanned (no release tag) · **Priority:** Should (A-49) · **Features:** FEAT-215
* **Source:** (source: CS-27, ES-36, C-05, G-01)
* **Gate:** none; **waits on O-01 (owner of the Order Desk API), not on a release.** It becomes a candidate for `dotnet-r3` when O-01 is answered; until then it carries no release tag (ES-31).
* **Cross-track (OPEN):** X-20 to X-23. **Relies on:** A-49; O-01, O-07.

##### FEAT-215 Order Desk read-only API service

* **Tags:** `track-dotnet` · **Release:** unplanned · **Priority:** Should · **Parent:** EPIC-204 · **Contains:** STORY-280
* **Source:** (source: CS-27, ES-36, C-05, G-01) · **Gate:** none

###### STORY-280 Offer a read-only Order Desk service for orders and order lines

* **Tags:** `track-dotnet` · **Release:** unplanned · **Priority:** Should (A-49) · **Rank:** 41 · **Parent:** FEAT-215 · **Implements:** FR-240
* **Source:** (source: CS-27, ES-36, C-05, G-01) · **Gate:** none (waits on O-01)
* **Story:** As a developer on another delivery track, I want Order Desk to offer a read-only service for orders and order lines, so that no other system reads its database directly.
* **Acceptance criteria:**
  * `STORY-280/AC1` Given the published contract (`EN-14`), When a valid request for one order number arrives, Then the service returns that order and its lines as the contract describes.
  * `STORY-280/AC2` Given a request without valid sign-in, When it arrives, Then it is refused and no order data is returned.
  * `STORY-280/AC3` Given any request that would create, change or delete data, When it arrives, Then the service offers no such operation.
  * `STORY-280/AC4` Given the service exists, When other systems need order data, Then they use it and do not read the database directly (C-05).
* **Dependencies:** `EN-14`. **Cross-track (OPEN):** X-20, X-21, X-22, X-23 (reachability and sign-in are Azure's or IT's). **Relies on:** O-01, O-07.

### 4.3 Power Platform track (`track-power-platform`, business area BA-03, **unplanned**)

Every BA-03 item carries **only** `track-power-platform`; the release is `unplanned`; there is no placeholder release and no release file (ES-31, A-44). The priority band P1 to P3 is shown next to the priority and is **not** a release tag (A-36). Acceptance wording is "design validated locally": nothing is created or changed in a tenant (ES-37). Order lines come from a stub contract until the Order Desk API exists (X-20). **Every item depends on MVE-03.** The Q1 2027 claims pilot of the business case cannot be committed (A-25; **OPEN:** O-07, owners Lena Varga and Marc Dubois). Customers do not record claims themselves: staff record every claim (business-case section 6).

---

#### EPIC-301 Claims platform foundation: environments, solution, connector stub, licensing, roles

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Features:** FEAT-301, FEAT-302, FEAT-303
* **Source:** (source: NFR-03, NFR-04, C-07, C-08, CS-25, CS-26, CS-27, CS-28, ES-33, ES-34, ES-35, ES-36, ES-37)
* **Gate:** **MVE-03** (a claims solution can meet the custom-connector rule ES-36 and the cap C-08 for about 52 users, and hand credit-note requests to a finance system with no API; pass checks `P3a` to `P3d`: 0 capabilities of unknown licence class; at most EUR 17.31 per user per month (900 divided by 52); an order-line path through a custom connector; a workable CSV hand-off; **ASSUMPTION:** A-35). Applies to `EP-03` to `EP-06` and, through them, to all BA-03 stories. Result **pending**.
* **Goal:** The governed foundation a claims solution needs, as a reviewed design: environments and DLP, the `NorthwindClaims` solution, a licensing and cost decision, a stub connector, the finance hand-off format and the roles.
* **Cross-track (OPEN):** X-20 to X-27. **Relies on:** A-22, A-23, A-25, A-34, A-36, A-44; O-02, O-07, O-15.

##### FEAT-301 Environments, data loss prevention and solution

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-301 · **Contains:** EP-01, EP-02, STORY-301
* **Source:** (source: NFR-03, CS-26, ES-34, ES-35) · **Gate:** MVE-03

###### EP-01 Design environments and data loss prevention policy

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 1 · **Parent:** FEAT-301 · **Serves:** FR-301
* **Source:** (source: CS-26, ES-35, NFR-03) · **Gate:** MVE-03
* **Story:** As a Power Platform administrator, I want a design for dedicated development, test and production environments in the Europe region and a DLP policy, so that nothing for claims is built in the default environment where 23 personal apps and flows already exist.
* **Acceptance criteria:**
  * `EP-01/AC1` Given the design, When it is read, Then it lists a development, a test and a production environment, each in the Europe region, and the default environment is not used.
  * `EP-01/AC2` Given the DLP policy design, When it is read, Then it lists the connectors the solution needs and blocks all others.
  * `EP-01/AC3` Given a connector that is not on the allowed list, When the design is reviewed, Then it is blocked and the request to add it goes to the administrator.
  * `EP-01/AC4` Given the design is reviewed, When it is accepted, Then it is "design validated locally"; no environment or policy is created in any tenant (ES-37).
* **Dependencies:** none. **Cross-track (OPEN):** X-27 (administration of the Microsoft 365 tenant is IT's). **Relies on:** O-02.

###### EP-02 Design the NorthwindClaims solution

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 2 · **Parent:** FEAT-301 · **Serves:** FR-301
* **Source:** (source: ES-34) · **Gate:** MVE-03
* **Story:** As a Power Platform maker, I want the `NorthwindClaims` solution designed with the publisher prefix `nw`, so that every app, flow, table and connector lives in one managed unit.
* **Acceptance criteria:**
  * `EP-02/AC1` Given the design, When it is read, Then it names the solution `NorthwindClaims` with the publisher prefix `nw` and places every app, flow, table and connector inside it (ES-34).
  * `EP-02/AC2` Given the design, When it is read, Then the solution is unmanaged only in development and managed in test and production.
  * `EP-02/AC3` Given a component is designed outside the solution, When the design is reviewed, Then it is returned until the component is inside `NorthwindClaims`.
* **Dependencies:** `EP-01`. **Cross-track (OPEN):** X-27. **Relies on:** A-23 (Dataverse use needs a premium licence outside Teams; **OPEN:** O-02).

###### STORY-301 Keep claims data in dedicated Europe environments with a DLP policy

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1, A-06) · **Rank:** 3 · **Parent:** FEAT-301 · **Implements:** FR-301 · **Covers:** NFR-03 (BA-03 side)
* **Source:** (source: NFR-03, ES-35, CS-26) · **Gate:** MVE-03
* **Story:** As the IT manager, I want claims data stored and processed only in dedicated Europe environments under a DLP policy, so that customer data stays in the EU.
* **Acceptance criteria:**
  * `STORY-301/AC1` Given the claims design, When every environment is listed with its region, Then development, test and production are in Europe and nothing is built in the default environment. Acceptance wording: design validated locally.
  * `STORY-301/AC2` Given the DLP policy design, When it is reviewed, Then only the connectors the solution needs are allowed.
  * `STORY-301/AC3` Given a design element that stores claims data outside Europe, When it is reviewed, Then the design is rejected.
* **Dependencies:** `EP-01`, `EP-02`. **Cross-track (OPEN):** X-27. **Relies on:** O-02.

##### FEAT-302 Licensing, connector stub and finance contract

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-301 · **Contains:** EP-04, EP-03, EP-05
* **Source:** (source: C-07, C-08, CS-25, CS-27, ES-33, ES-36) · **Gate:** MVE-03

###### EP-04 Decide licensing and cost

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 4 · **Parent:** FEAT-302 · **Serves:** BG-04 and all BA-03 features
* **Source:** (source: C-07, C-08; **ASSUMPTION:** A-22, A-23) · **Gate:** MVE-03 (`P3a`, `P3b`)
* **Story:** As the IT manager, I want a licensing and cost decision (premium or standard, Dataverse or an alternative), so that the claims solution fits the cap of EUR 900 a month for about 52 users before its data model is designed.
* **Acceptance criteria:**
  * `EP-04/AC1` Given the claims solution, When its capabilities are listed, Then each has a licence class and none has an unknown class (`P3a`).
  * `EP-04/AC2` Given the cost for about 52 users, When it is calculated, Then it is at most EUR 17.31 per user per month (EUR 900 divided by 52) (`P3b`), or a decision to relax C-07, C-08 or ES-36 is recorded by the owner of that rule (O-02).
  * `EP-04/AC3` Given a price or licence rule is not verified against primary Microsoft documentation, When it is written, Then it is date-stamped and marked **ASSUMPTION:** (A-22, A-23, MVE-A-08).
* **Dependencies:** none. **Cross-track (OPEN):** X-27. **Relies on:** A-22, A-23, A-35; O-02; MVE-A-09.

###### EP-03 Define the stub custom connector contract

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 5 · **Parent:** FEAT-302 · **Serves:** FR-310
* **Source:** (source: ES-36, ES-33, CS-27) · **Gate:** MVE-03 (`P3c`)
* **Story:** As a Power Platform maker, I want a stub custom connector definition (OpenAPI 2.0) with a connection reference and an environment variable, so that claims can be designed against order lines before the Order Desk API exists.
* **Acceptance criteria:**
  * `EP-03/AC1` Given the stub, When it is validated locally, Then it is a valid OpenAPI 2.0 definition kept with the Power Platform source (`powerplatform/`, ES-33).
  * `EP-03/AC2` Given the stub, When it is read, Then the endpoint is an environment variable and the connection is a connection reference; nothing is hard-coded (ES-36).
  * `EP-03/AC3` Given an app or flow in the design, When its data access is reviewed, Then it reaches Order Desk only through the connector and never connects directly to the order database (ES-36, CS-27).
  * `EP-03/AC4` Given the connector, When it is read, Then it carries a placeholder security definition until X-23 is answered.
* **Dependencies:** none. **Cross-track (OPEN):** X-20, X-21, X-22, X-23. **Relies on:** O-01, O-02.

###### EP-05 Define the finance CSV contract and drop location

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 6 · **Parent:** FEAT-302 · **Serves:** FR-312
* **Source:** (source: CS-25, O-15) · **Gate:** MVE-03 (`P3d`)
* **Story:** As a Power Platform maker, I want the CSV file format and the drop location for credit-note requests designed, so that Finance receives approved claims without re-keying although the finance system has no API.
* **Acceptance criteria:**
  * `EP-05/AC1` Given the finance system imports a CSV file placed in `\\NWFS01\finance-import\` before 18:00 on working days (CS-25), When the design is read, Then it states the file's columns and naming as agreed with Finance; until agreed they are **OPEN:** O-29.
  * `EP-05/AC2` Given a request is approved after 18:00 or on a non-working day, When the design is read, Then it is included in the file of the next working day.
  * `EP-05/AC3` Given where the share lives after the lease is unknown (O-15), When the design names the location, Then it is marked **OPEN:** with Julien Moreau and Ahmed Benali as owners.
* **Dependencies:** none. **Cross-track (OPEN):** X-24. **Relies on:** O-15, O-29; MVE-O-04.

##### FEAT-303 Identity and roles

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-301 · **Contains:** EP-06, STORY-302
* **Source:** (source: NFR-04, CS-28, BR-15) · **Gate:** MVE-03

###### EP-06 Define identity and roles with no self-approval

* **Tags:** `track-power-platform` · **Release:** unplanned · **Type:** enabler · **Priority:** Must (P1) · **Rank:** 7 · **Parent:** FEAT-303 · **Serves:** FR-302, FR-311
* **Source:** (source: CS-28, NFR-04, BR-15) · **Gate:** MVE-03
* **Story:** As a Power Platform maker, I want the roles recorder, approver and supervisor defined with Microsoft Entra ID sign-in, so that the approval rule can be enforced by design.
* **Acceptance criteria:**
  * `EP-06/AC1` Given the design, When it is read, Then it defines the three roles and gives each the actions it may do.
  * `EP-06/AC2` Given a user holds both the recorder and the approver role, When they open a claim they recorded, Then the approve action is unavailable to them.
  * `EP-06/AC3` Given a user who signs in with an Entra ID account but holds no claims role, When they open the solution, Then they see no claim.
* **Dependencies:** none. **Cross-track (OPEN):** X-23 (connector sign-in, Entra app registration), X-27. **Relies on:** none.

###### STORY-302 Sign claims users in with Entra ID and assign roles

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1, A-06) · **Rank:** 8 · **Parent:** FEAT-303 · **Implements:** FR-302 · **Covers:** NFR-04 (BA-03 side)
* **Source:** (source: NFR-04, CS-28, BR-15) · **Gate:** MVE-03
* **Story:** As an Order Desk staff member, a Finance staff member or a warehouse supervisor, I want to sign in with my Microsoft Entra ID account and hold a role of recorder, approver or supervisor, so that I see only what my role allows.
* **Acceptance criteria:**
  * `STORY-302/AC1` Given the design, When it is read, Then staff, Finance and the 8 warehouse supervisors in Antwerp (who already hold Entra ID accounts, CS-28) sign in with those accounts and no separate password exists.
  * `STORY-302/AC2` Given the roles recorder, approver and supervisor, When a user signs in, Then they see only the screens their role allows (design validated locally).
  * `STORY-302/AC3` Given a signed-in user with no claims role, When they open the solution, Then no claim is shown.
* **Dependencies:** `EP-06`. **Cross-track (OPEN):** X-23. **Relies on:** none.

---

#### EPIC-302 Record, approve and hand off claims; claims history

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Features:** FEAT-304, FEAT-305, FEAT-306, FEAT-307
* **Source:** (source: BR-14, BR-15, BR-16, NFR-09, SM-05, SM-06, OQ-04, OQ-05, CS-24, CS-25, CS-27)
* **Gate:** **MVE-03** (see EPIC-301). Result **pending**.
* **Goal:** Staff record a claim in under 2 minutes, Finance approves claims above EUR 500 with no self-approval, an approved claim reaches the finance system without re-keying, and every decision is kept 7 years. Moving the spreadsheet claims is separate and open.
* **Cross-track (OPEN):** X-20, X-21, X-22, X-24. **Relies on:** A-13, A-14, A-25, A-31, A-34, A-56; O-01, O-02, O-13, O-14, O-15, O-29.

##### FEAT-304 Record a claim

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-302 · **Contains:** STORY-320
* **Source:** (source: BR-14, P-06, CS-24, CS-27) · **Gate:** MVE-03

###### STORY-320 Record a delivery claim in under 2 minutes with up to 5 photos

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Rank:** 9 · **Parent:** FEAT-304 · **Implements:** FR-310 · **Covers:** BR-14
* **Source:** (source: BR-14, P-06, CS-24, CS-27; supports SM-05, SM-06) · **Gate:** MVE-03
* **Story:** As an Order Desk staff member, I want to record a delivery claim against one or more lines of an existing order, with a reason (damaged, missing or wrong product) and up to 5 photos, in under 2 minutes, so that claims are captured at once and no longer lost in a shared spreadsheet.
* **Acceptance criteria:**
  * `STORY-320/AC1` Given an existing order with several lines, When I select two of them, choose the reason damaged, missing or wrong product, and save, Then one claim is recorded against exactly those two lines (design validated locally).
  * `STORY-320/AC2` Given a walkthrough of the design with a staff member, When the time is taken from opening the order to saving the claim, Then it is under 2 minutes.
  * `STORY-320/AC3` Given I attach 5 photos, When I save, Then all 5 are kept; given I try to attach a 6th photo, Then it is refused with a message that the limit is 5.
  * `STORY-320/AC4` Given I have not chosen a reason or no line, When I try to save, Then the claim is not saved and the missing item is named.
  * `STORY-320/AC5` Given an order number that does not exist in Order Desk, When I search for it, Then no claim can be recorded against it.
  * `STORY-320/AC6` **ASSUMPTION:** A-56 (derived from SM-06, owner Lena Varga). Given a claim already exists for the same order line and reason, When I save a second one, Then I am warned of the possible duplicate and must confirm it.
* **Dependencies:** `EP-03`, `EP-06`, `EP-04`. **Cross-track (OPEN):** X-20, X-21, X-22 (order lines come from the stub until the API exists). **Relies on:** A-34, A-56; O-01, O-02.

##### FEAT-305 Approve claims and audit decisions

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-302 · **Contains:** STORY-321, STORY-323
* **Source:** (source: BR-15, NFR-09, OQ-04, P-06) · **Gate:** MVE-03

###### STORY-321 Approve claims above EUR 500 without self-approval

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Rank:** 10 · **Parent:** FEAT-305 · **Implements:** FR-311 · **Covers:** BR-15
* **Source:** (source: BR-15, P-06, OQ-04) · **Gate:** MVE-03
* **Story:** As a Finance staff member, I want claims above EUR 500 to be approved by Finance and nobody to be able to approve a claim they recorded, so that no claim is approved by the person who raised it.
* **Acceptance criteria:**
  * `STORY-321/AC1` Given a claim whose value is above EUR 500 (for example EUR 501), When a Finance user who did not record it approves it, Then the claim is approved and the decision is recorded.
  * `STORY-321/AC2` **No self-approval:** Given a user who recorded a claim, When the same user tries to approve it, Then the approval is refused whatever their role, Finance included.
  * `STORY-321/AC3` Given a claim of exactly EUR 500 or less, When it is recorded, Then this story does not decide who approves it; that path is **OPEN:** O-13 (owners Julien Moreau and Lena Varga) and **ASSUMPTION:** A-13 limits the criteria to claims above EUR 500.
  * `STORY-321/AC4` Given a claim above EUR 500 that no one has approved, When it is read, Then it is shown as waiting for approval and no credit-note request exists for it.
* **Dependencies:** `EP-06`. **Cross-track (OPEN):** X-23. **Relies on:** A-13; O-13.

###### STORY-323 Record every claim decision for 7 years

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1, A-06) · **Rank:** 11 · **Parent:** FEAT-305 · **Implements:** FR-313 · **Covers:** NFR-09
* **Source:** (source: NFR-09) · **Gate:** MVE-03
* **Story:** As the head of Customer Operations, I want every claim decision recorded with who, what, when and amount and kept for 7 years, so that the audit requirement is met.
* **Acceptance criteria:**
  * `STORY-323/AC1` Given a claim is approved or rejected, When the audit record is read, Then it shows who decided, what was decided, when and the amount.
  * `STORY-323/AC2` Given a sample of claim decisions, When the audit records are checked, Then each of the four fields is present.
  * `STORY-323/AC3` Given the retention design, When it is read, Then it shows 7 years (**ASSUMPTION:** A-31, feature limits not verified).
  * `STORY-323/AC4` Given a decision that lacks any of the four fields, When it is saved, Then it is not saved.
* **Dependencies:** `EP-02`, `EP-04`. **Cross-track (OPEN):** none. **Relies on:** A-31.

##### FEAT-306 Credit-note hand-off to Finance

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Parent:** EPIC-302 · **Contains:** STORY-322
* **Source:** (source: BR-16, CS-25) · **Gate:** MVE-03

###### STORY-322 Send an approved claim to Finance as a credit-note request

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Must (P1) · **Rank:** 12 · **Parent:** FEAT-306 · **Implements:** FR-312 · **Covers:** BR-16
* **Source:** (source: BR-16, CS-25; supports SM-05, SM-06) · **Gate:** MVE-03
* **Story:** As a Finance staff member, I want an approved claim to reach the finance system as a credit-note request without re-keying, so that I stop keying requests from e-mails.
* **Acceptance criteria:**
  * `STORY-322/AC1` Given a claim is approved, When the daily file is made, Then the credit-note request is in a CSV file placed in the finance import location before 18:00 on a working day (CS-25) and nobody re-keys it.
  * `STORY-322/AC2` Given a claim is approved after 18:00 or on a non-working day, When the files are made, Then it is in the file of the next working day.
  * `STORY-322/AC3` Given the file cannot be placed, When the hand-off runs, Then the claim stays "approved, not sent" and is visible to Finance; it is not lost.
  * `STORY-322/AC4` Given a claim that is rejected or not yet approved, When the files are made, Then it is not in any file.
* **Dependencies:** `EP-05`, `EP-03`. **Cross-track (OPEN):** X-24 (CSV drop and location after the lease). **Relies on:** O-15, O-29; MVE-O-04.

##### FEAT-307 Claims history migration

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Not set (O-14) · **Parent:** EPIC-302 · **Contains:** STORY-324
* **Source:** (source: OQ-05, CS-24; **ASSUMPTION:** A-14) · **Gate:** MVE-03

###### STORY-324 Decide whether spreadsheet claims move to the new solution

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Not set (O-14) · **Rank:** 13 · **Parent:** FEAT-307 · **Implements:** FR-314
* **Source:** (source: OQ-05, CS-24; **ASSUMPTION:** A-14) · **Gate:** MVE-03
* **Story:** As the head of Customer Operations, I want to know whether the claims already in the spreadsheet (about 9,400 rows since January 2023) move to the new solution, so that the claims history is not lost or duplicated.
* **Acceptance criteria:**
  * `STORY-324/AC1` Given O-14 is not answered, When the backlog is read, Then this item is **not** a requirement and is not started.
  * `STORY-324/AC2` Given the answer to O-14 is yes, When the item is refined, Then the product owner sets its priority and criteria, which must cover the conflicting copies found each week in the spreadsheet (CS-24).
  * `STORY-324/AC3` Given the answer to O-14 is no, When the answer is recorded, Then the item is closed and the spreadsheet stays read-only as the historical record (**ASSUMPTION:** A-14).
* **Dependencies:** none. **Cross-track (OPEN):** none. **Relies on:** A-14; O-14.

---

#### EPIC-303 Warehouse causes and claims dashboard

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Should (P2) · **Features:** FEAT-308, FEAT-309
* **Source:** (source: BR-17, BR-18, P-06, CS-28, C-08)
* **Gate:** **MVE-03**. Result **pending**.
* **Goal:** Warehouse supervisors record the cause of claims about missing or wrong products, and Customer Operations sees a weekly dashboard.
* **Cross-track (OPEN):** X-25. **Relies on:** A-18, A-57; O-08, O-22, O-30.

##### FEAT-308 Warehouse cause recording

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Should (P2) · **Parent:** EPIC-303 · **Contains:** STORY-350
* **Source:** (source: BR-17, CS-28) · **Gate:** MVE-03

###### STORY-350 Let warehouse supervisors see and record causes of their claims

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Should (P2) · **Rank:** 14 · **Parent:** FEAT-308 · **Implements:** FR-320 · **Covers:** BR-17
* **Source:** (source: BR-17, CS-28) · **Gate:** MVE-03
* **Story:** As a warehouse supervisor in Antwerp, I want to see the claims about missing or wrong products from my warehouse and record the cause, so that I learn which picking errors cause claims.
* **Acceptance criteria:**
  * `STORY-350/AC1` Given claims exist for several warehouses, When a supervisor of the Antwerp warehouse opens the view, Then only claims with the reason missing or wrong product from that warehouse are shown.
  * `STORY-350/AC2` Given a claim in the view, When the supervisor records a cause, Then the cause is saved with the claim.
  * `STORY-350/AC3` Given a claim with the reason damaged, or a claim of another warehouse, When the supervisor opens the view, Then it is not shown.
  * `STORY-350/AC4` Given the warehouse of a claim line cannot be determined (A-18, X-25), When the view is built, Then the claim is shown to no supervisor and is flagged for staff.
* **Dependencies:** `EP-06`, `STORY-320`. **Cross-track (OPEN):** X-25 (the warehouse for each order line; the supervisor view is designed with the cause field and the source stays **OPEN:**). **Relies on:** A-18; O-08, O-30 (**OPEN:** the list of cause values is not in the sources; owner Pieter Janssens).

##### FEAT-309 Weekly claims dashboard

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Should (P2) · **Parent:** EPIC-303 · **Contains:** STORY-351
* **Source:** (source: BR-18, P-06) · **Gate:** MVE-03

###### STORY-351 Show a weekly claims dashboard

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Should (P2) · **Rank:** 15 · **Parent:** FEAT-309 · **Implements:** FR-321 · **Covers:** BR-18
* **Source:** (source: BR-18, P-06; supports SM-05) · **Gate:** MVE-03
* **Story:** As the head of Customer Operations, I want a weekly claims dashboard with the number, value, cause and time to resolve, so that I can see whether claims are getting faster and what causes them.
* **Acceptance criteria:**
  * `STORY-351/AC1` Given claims were recorded in a week, When I open the dashboard for that week, Then it shows the number of claims, their total value, the count by cause and the time to resolve.
  * `STORY-351/AC2` Given a week with no claims, When I open the dashboard, Then it shows zero and not a blank or an error.
  * `STORY-351/AC3` Given time to resolve is measured from the claim being recorded to it being approved or rejected (**ASSUMPTION:** A-57), When a claim is still open, Then it is counted as open and is not given a resolve time.
  * `STORY-351/AC4` Given the dashboard tool must keep the solution within EUR 900 a month (C-08), When the tool is chosen, Then the choice is recorded against O-22 before the story is started.
* **Dependencies:** `EP-04`, `STORY-350`. **Cross-track (OPEN):** none. **Relies on:** A-57; O-22.

---

#### EPIC-304 Customer claim notifications

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Could (P3) · **Features:** FEAT-310
* **Source:** (source: BR-19)
* **Gate:** **MVE-03**. Result **pending**.
* **Goal:** The customer is told by e-mail when a claim is approved or rejected.
* **Cross-track (OPEN):** X-26. **Relies on:** O-18.

##### FEAT-310 Customer claim e-mail

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Could (P3) · **Parent:** EPIC-304 · **Contains:** STORY-370
* **Source:** (source: BR-19) · **Gate:** MVE-03

###### STORY-370 E-mail the customer when a claim is approved or rejected

* **Tags:** `track-power-platform` · **Release:** unplanned · **Priority:** Could (P3) · **Rank:** 16 · **Parent:** FEAT-310 · **Implements:** FR-330 · **Covers:** BR-19
* **Source:** (source: BR-19) · **Gate:** MVE-03
* **Story:** As a customer user whose delivery claim has been decided, I want an e-mail when it is approved or rejected, so that I do not have to phone to find out.
* **Acceptance criteria:**
  * `STORY-370/AC1` Given a claim is approved, When the decision is recorded, Then an e-mail saying approved is sent to the customer.
  * `STORY-370/AC2` Given a claim is rejected, When the decision is recorded, Then an e-mail saying rejected is sent to the customer.
  * `STORY-370/AC3` Given no customer e-mail address is known, When the decision is recorded, Then no e-mail is sent and the claim is flagged for staff (X-26, O-18).
* **Dependencies:** `STORY-321`. **Cross-track (OPEN):** X-26 (where the customer e-mail address and language live). **Relies on:** O-18.

## 5. Unplanned items

These items have **no release tag** (ES-31). They are listed in full in section 4; this table says why each is unplanned and what moves it. Unplanned items carry only their track tag, and unplanned does not mean out of scope: BA-03 is in scope (A-44).

| Items | Track tag | Why unplanned | What would move it into a release | Owner to answer |
|---|---|---|---|---|
| EPIC-301 to EPIC-304 with FEAT-301 to FEAT-310, `EP-01` to `EP-06`, STORY-301, STORY-302, STORY-320 to STORY-324, STORY-350, STORY-351, STORY-370 (BA-03, 30 items) | `track-power-platform` | The business area has no team, no Order Desk API, no governed environments and no licence decision (G-08, CS-26, CS-27, O-02, O-07). A placeholder release would invent a commitment. The Q1 2027 claims pilot **cannot be committed** (A-25). | A named team, skills and date (O-07), the licence and connector decision (O-02, MVE-03), an owner of the Order Desk API (O-01). A new release name would then be proposed with a new `<track>-r<n>` tag. | Lena Varga, Marc Dubois (O-07); Ahmed Benali (O-01, O-02) |
| EPIC-204, FEAT-215, STORY-280 (Order Desk API implementation, 3 items) | `track-dotnet` | A conditional item cannot carry a release tag (ES-31). The API has no owner (G-01, O-01). | O-01 is answered; the item becomes a candidate for `dotnet-r3`. | Ahmed Benali |
| STORY-324 (spreadsheet claims migration, FEAT-307) | `track-power-platform` | It is not a requirement until O-14 is answered; priority not set (A-14). | O-14 answered yes, then priority and criteria set by the product owner. | Lena Varga, Julien Moreau |

Optimisation after the lease (Azure) is not planned and has no item; it would be an unplanned item with only `track-azure` (PRD section 6.2).

## 6. Publication mapping (ES-39)

This is a plan for a later step. **Nothing is published.** No Azure DevOps, GitHub or Jira tool is chosen, so no tool was contacted and the item types and fields below were **not validated** there (`needs_review`; **OPEN:** O-06, owner Lena Varga). The ES-28 prefix is also **OPEN:** O-06; when items are created during the workshop they carry the tag or label `nw-workshop` and the participant prefix agreed with the facilitator.

### 6.1 How the tags travel in each tool

| Backlog concept | Azure DevOps | GitHub | Jira |
|---|---|---|---|
| Track tag (`track-azure`, `track-dotnet`, `track-power-platform`) | Work-item tag | Issue label | Label |
| Release tag (`azure-r1` to `dotnet-r3`) | Work-item tag | Issue label **and** one milestone per release, named after it | Label **and** one fix version per release, named after it |
| Epic | Epic | Issue that parents the feature issues (sub-issues) | Epic |
| Feature | Feature | Issue that parents the story issues (sub-issues) | Story that parents the stories (**needs_review**: Jira has no feature type by default) |
| Story and enabler (`EA-`, `EN-`, `EP-`) | User Story | Issue (sub-issue of its feature) | Story |
| Id, title, source ids | Title `<id> <title>`; description holds the source ids and acceptance criteria (ES-29) | Same | Same |
| Unplanned item | Track tag only, no release tag, no iteration | Track label only, **no milestone** | Track label only, **no fix version** |

Rules that apply in every tool: titles are the plain titles below; every description starts with the item id and the source ids (`BR-`, `NFR-`, `C-`, `SM-`, `CS-`, `ES-`) (ES-28, ES-29); an item has exactly one track tag and at most one release tag (ES-30, ES-31); the milestone or fix version name equals the release tag. The Git tags `product/<track>-r<n>` are created only after the product owner approves a release and are **not yet created** (A-39).

### 6.2 Published titles, tags and milestones

Milestone (GitHub) or fix version (Jira) name equals the release tag. Azure DevOps has no milestone; its release tag is a work-item tag. `none` means the item is unplanned and has no milestone or fix version.

| Item id | Title as published | Tags / labels | Milestone / fix version |
|---|---|---|---|
| EPIC-101 | EPIC-101 Azure foundation and security baseline | `track-azure`, `azure-r1` | `azure-r1` |
| FEAT-101 | FEAT-101 Environment foundation as code and validation | `track-azure`, `azure-r1` | `azure-r1` |
| EA-01 | EA-01 Build the Azure foundation as code (naming, tags, region, modules) | `track-azure`, `azure-r1` | `azure-r1` |
| EA-11 | EA-11 Build the infrastructure validation and deployment pipeline design | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-101 | STORY-101 Review a test and production environment design set | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-104 | STORY-104 Keep every Azure resource in an EU region | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-105 | STORY-105 Validate every infrastructure definition locally before release | `track-azure`, `azure-r1` | `azure-r1` |
| FEAT-102 | FEAT-102 Hybrid connectivity design | `track-azure`, `azure-r1` | `azure-r1` |
| EA-02 | EA-02 Design hybrid connectivity between Lyon, Azure and Antwerp | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-102 | STORY-102 Agree the connection design for the move and after the lease | `track-azure`, `azure-r1` | `azure-r1` |
| FEAT-103 | FEAT-103 Secrets, identity and private access | `track-azure`, `azure-r1` | `azure-r1` |
| EA-03 | EA-03 Design secrets, managed identities and private endpoints | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-103 | STORY-103 Keep secrets out of Azure-hosted code and configuration | `track-azure`, `azure-r1` | `azure-r1` |
| EPIC-102 | EPIC-102 Data platform decision, cost and migration approach | `track-azure`, `azure-r1` | `azure-r1` |
| FEAT-104 | FEAT-104 Data tier decision | `track-azure`, `azure-r1` | `azure-r1` |
| EA-05 | EA-05 Record the data-tier decision and migration approach | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-120 | STORY-120 Decide the data tier for the order database | `track-azure`, `azure-r1` | `azure-r1` |
| FEAT-105 | FEAT-105 Cost model and migration approach | `track-azure`, `azure-r1` | `azure-r1` |
| EA-09 | EA-09 Build the Azure cost model against the monthly cap | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-121 | STORY-121 Show the monthly cost against the EUR 1,500 cap | `track-azure`, `azure-r1` | `azure-r1` |
| STORY-122 | STORY-122 Define the database and invoice migration approach | `track-azure`, `azure-r1` | `azure-r1` |
| EPIC-103 | EPIC-103 Pilot environment, exchange, storage and observability | `track-azure`, `azure-r2` | `azure-r2` |
| FEAT-113 | FEAT-113 Application hosting | `track-azure`, `azure-r2` | `azure-r2` |
| EA-15 | EA-15 Host the Order Desk web application in the test and production environments | `track-azure`, `azure-r2` | `azure-r2` |
| FEAT-106 | FEAT-106 StockPilot exchange, invoice storage and outbound mail | `track-azure`, `azure-r2` | `azure-r2` |
| EA-06 | EA-06 Redesign the StockPilot exchange without changing the file contract | `track-azure`, `azure-r2` | `azure-r2` |
| EA-07 | EA-07 Design invoice storage and synchronisation | `track-azure`, `azure-r2` | `azure-r2` |
| EA-12 | EA-12 Design outbound mail to replace the on-premises relay | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-140 | STORY-140 Keep the nightly StockPilot exchange working after the database moves | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-141 | STORY-141 Decide where invoice files live after the lease | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-144 | STORY-144 Replace the on-premises mail relay for outbound e-mail | `track-azure`, `azure-r2` | `azure-r2` |
| FEAT-107 | FEAT-107 Observability and alerting | `track-azure`, `azure-r2` | `azure-r2` |
| EA-04 | EA-04 Build observability: log workspace, application monitoring and alerts | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-142 | STORY-142 Monitor availability with a synthetic probe and alerts | `track-azure`, `azure-r2` | `azure-r2` |
| FEAT-108 | FEAT-108 Test environment for the portal pilot | `track-azure`, `azure-r2` | `azure-r2` |
| EA-10 | EA-10 Define the tst environment | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-143 | STORY-143 Define a test environment where the portal pilot can run | `track-azure`, `azure-r2` | `azure-r2` |
| FEAT-109 | FEAT-109 Backup, retention and recovery design | `track-azure`, `azure-r2` | `azure-r2` |
| EA-08 | EA-08 Design backup, long-term retention and recovery | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-145 | STORY-145 Keep order-change records for 7 years in Azure | `track-azure`, `azure-r2` | `azure-r2` |
| STORY-146 | STORY-146 Design backup and recovery for RPO 1 hour and RTO 4 hours | `track-azure`, `azure-r2` | `azure-r2` |
| EPIC-104 | EPIC-104 Cutover and recovery proof | `track-azure`, `azure-r3` | `azure-r3` |
| FEAT-114 | FEAT-114 Database migration and rehearsal | `track-azure`, `azure-r3` | `azure-r3` |
| EA-16 | EA-16 Migrate the NorthwindOrders database to the chosen data tier and rehearse the move | `track-azure`, `azure-r3` | `azure-r3` |
| FEAT-110 | FEAT-110 Cutover and rollback runbooks | `track-azure`, `azure-r3` | `azure-r3` |
| EA-13 | EA-13 Write cutover, rollback and decommission runbooks | `track-azure`, `azure-r3` | `azure-r3` |
| STORY-170 | STORY-170 Keep staff working through the cutover inside the Sunday window | `track-azure`, `azure-r3` | `azure-r3` |
| STORY-171 | STORY-171 Define rollback and rehearsal for every cutover step | `track-azure`, `azure-r3` | `azure-r3` |
| FEAT-111 | FEAT-111 Recovery and availability proof | `track-azure`, `azure-r3` | `azure-r3` |
| EA-14 | EA-14 Write the first recovery test plan and evidence template | `track-azure`, `azure-r3` | `azure-r3` |
| STORY-172 | STORY-172 Prove recovery against RPO 1 hour and RTO 4 hours | `track-azure`, `azure-r3` | `azure-r3` |
| STORY-173 | STORY-173 Plan the availability proof for the first weeks in Azure | `track-azure`, `azure-r3` | `azure-r3` |
| FEAT-112 | FEAT-112 Decommission of the old servers | `track-azure`, `azure-r3` | `azure-r3` |
| STORY-174 | STORY-174 Retire the old web and database servers before 30 June 2027 | `track-azure`, `azure-r3` | `azure-r3` |
| EPIC-201 | EPIC-201 Modernise Order Desk to .NET 10 with parity | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| FEAT-201 | FEAT-201 Modernise projects and web layer | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-01 | EN-01 Convert the solution to SDK-style projects on net10.0 | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-13 | EN-13 Record the decision on portal and API project shape | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-03 | EN-03 Replace direct ConfigurationManager calls with the options pattern | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-05 | EN-05 Replace the Windows Event Log logger with standard logging | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-06 | EN-06 Replace the in-process session order draft | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-08 | EN-08 Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-201 | STORY-201 Run Order Desk on .NET 10 with unchanged staff screens | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| FEAT-202 | FEAT-202 Test, build and local data | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-02 | EN-02 Replace MSTest v1 so all tests run on Windows, macOS and Linux | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-09 | EN-09 Build an automated build and test pipeline | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-12 | EN-12 Provide local test data with orders and a local database recipe | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| FEAT-203 | FEAT-203 Pricing, channel and time parity | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-10 | EN-10 Make time handling explicit and tested | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-202 | STORY-202 Keep pricing identical to today (pricing parity) | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-203 | STORY-203 Keep the order channel visible to staff (channel parity) | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-206 | STORY-206 Keep dates and price validity identical in any time zone (time parity) | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| FEAT-204 | FEAT-204 Staff sign-in with Entra ID | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-204 | STORY-204 Sign staff in with Microsoft Entra ID | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| FEAT-205 | FEAT-205 Secret-free configuration | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EN-04 | EN-04 Remove Windows sign-in and server names from database configuration | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| STORY-205 | STORY-205 Keep secrets out of code, tests and configuration | `track-dotnet`, `dotnet-r1` | `dotnet-r1` |
| EPIC-202 | EPIC-202 Customer portal pilot: sign-in, orders, status, reorder | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| FEAT-206 | FEAT-206 Customer sign-in, company isolation and data residency | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| EN-11 | EN-11 Build the authorisation foundation for customer scoping and channel | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-230 | STORY-230 Sign in and see only my own company's orders | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-240 | STORY-240 Authenticate customers with an externally managed identity | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-239 | STORY-239 Keep portal hosting, identity and mail data in the EU | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| FEAT-207 | FEAT-207 Order list, order detail and status | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-231 | STORY-231 See my company's orders from the last 24 months | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-232 | STORY-232 Open an order and see lines, prices, address and status | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-233 | STORY-233 See one of six order statuses with an as-of time | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| FEAT-208 | FEAT-208 Reorder, submit and channel | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-234 | STORY-234 Create a new order by copying a previous order | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-235 | STORY-235 Have a submitted portal order appear in Order Desk as Received | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-236 | STORY-236 Show staff whether an order came from the portal or from staff | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| FEAT-209 | FEAT-209 Customer prices and language | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-238 | STORY-238 Show my negotiated prices, not list prices | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-237 | STORY-237 Use the portal in French and English | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| FEAT-210 | FEAT-210 Audit, accessibility and performance | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-241 | STORY-241 Record who, what, when and channel for every order change | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-242 | STORY-242 Check every pilot screen against WCAG 2.2 level AA | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| STORY-243 | STORY-243 Respond in under 2 seconds at the 95th percentile | `track-dotnet`, `dotnet-r2` | `dotnet-r2` |
| EPIC-203 | EPIC-203 Complete the portal and publish the Order Desk API contract | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| FEAT-211 | FEAT-211 Invoice download | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| EN-07 | EN-07 Abstract the invoice store | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-260 | STORY-260 Download the PDF invoice of a delivered order | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| FEAT-212 | FEAT-212 Customer user administration and shipping e-mail | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-261 | STORY-261 Invite and remove users of my own company | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-262 | STORY-262 Receive an e-mail when an order changes to Shipped | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| FEAT-213 | FEAT-213 Dutch and success-measure data | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-263 | STORY-263 Use the portal in Dutch | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-264 | STORY-264 Record data to compare SM-01 to SM-04 with their baselines | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| FEAT-214 | FEAT-214 Order Desk API contract | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| EN-14 | EN-14 Publish the read-only Order Desk API contract (OpenAPI 2.0) | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| STORY-265 | STORY-265 Let another track build against the published order contract | `track-dotnet`, `dotnet-r3` | `dotnet-r3` |
| EPIC-204 | EPIC-204 Order Desk API implementation for other tracks | `track-dotnet` | none |
| FEAT-215 | FEAT-215 Order Desk read-only API service | `track-dotnet` | none |
| STORY-280 | STORY-280 Offer a read-only Order Desk service for orders and order lines | `track-dotnet` | none |
| EPIC-301 | EPIC-301 Claims platform foundation: environments, solution, connector stub, licensing, roles | `track-power-platform` | none |
| FEAT-301 | FEAT-301 Environments, data loss prevention and solution | `track-power-platform` | none |
| EP-01 | EP-01 Design environments and data loss prevention policy | `track-power-platform` | none |
| EP-02 | EP-02 Design the NorthwindClaims solution | `track-power-platform` | none |
| STORY-301 | STORY-301 Keep claims data in dedicated Europe environments with a DLP policy | `track-power-platform` | none |
| FEAT-302 | FEAT-302 Licensing, connector stub and finance contract | `track-power-platform` | none |
| EP-04 | EP-04 Decide licensing and cost | `track-power-platform` | none |
| EP-03 | EP-03 Define the stub custom connector contract | `track-power-platform` | none |
| EP-05 | EP-05 Define the finance CSV contract and drop location | `track-power-platform` | none |
| FEAT-303 | FEAT-303 Identity and roles | `track-power-platform` | none |
| EP-06 | EP-06 Define identity and roles with no self-approval | `track-power-platform` | none |
| STORY-302 | STORY-302 Sign claims users in with Entra ID and assign roles | `track-power-platform` | none |
| EPIC-302 | EPIC-302 Record, approve and hand off claims; claims history | `track-power-platform` | none |
| FEAT-304 | FEAT-304 Record a claim | `track-power-platform` | none |
| STORY-320 | STORY-320 Record a delivery claim in under 2 minutes with up to 5 photos | `track-power-platform` | none |
| FEAT-305 | FEAT-305 Approve claims and audit decisions | `track-power-platform` | none |
| STORY-321 | STORY-321 Approve claims above EUR 500 without self-approval | `track-power-platform` | none |
| STORY-323 | STORY-323 Record every claim decision for 7 years | `track-power-platform` | none |
| FEAT-306 | FEAT-306 Credit-note hand-off to Finance | `track-power-platform` | none |
| STORY-322 | STORY-322 Send an approved claim to Finance as a credit-note request | `track-power-platform` | none |
| FEAT-307 | FEAT-307 Claims history migration | `track-power-platform` | none |
| STORY-324 | STORY-324 Decide whether spreadsheet claims move to the new solution | `track-power-platform` | none |
| EPIC-303 | EPIC-303 Warehouse causes and claims dashboard | `track-power-platform` | none |
| FEAT-308 | FEAT-308 Warehouse cause recording | `track-power-platform` | none |
| STORY-350 | STORY-350 Let warehouse supervisors see and record causes of their claims | `track-power-platform` | none |
| FEAT-309 | FEAT-309 Weekly claims dashboard | `track-power-platform` | none |
| STORY-351 | STORY-351 Show a weekly claims dashboard | `track-power-platform` | none |
| EPIC-304 | EPIC-304 Customer claim notifications | `track-power-platform` | none |
| FEAT-310 | FEAT-310 Customer claim e-mail | `track-power-platform` | none |
| STORY-370 | STORY-370 E-mail the customer when a claim is approved or rejected | `track-power-platform` | none |

## 7. ASSUMPTION and OPEN registers

Ids are those of the PRD (`PRD-NW-001`, sections 14 and 15) and keep their numbers. **This section 7 is the register of record for every id introduced after the plan was written**: `A-49` to `A-59` and `O-26` to `O-31` (the BRD and PRD registers may not hold the newest rows). Ids `A-55` to `A-59` and `O-28` to `O-31` are new in this backlog. Release-local ids (`AZ1-O1`, `A-D1-01`, `O-D2-01` and the like) are defined in the release file that cites them and are copied, with their owners, into section 7.5. Only ids cited in this backlog or in a release file are listed.

### 7.1 ASSUMPTION register (ES-03)

An assumption is not in `knowledge-docs`. It is never presented as a requirement.

| Id | ASSUMPTION | Confirming owner |
|---|---|---|
| A-01 | Build starts December 2026 after approval; release approval dates are targets. | Marc Dubois |
| A-02 | .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. | Ahmed Benali |
| A-03 | `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. | Lena Varga |
| A-04 | "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot. | Lena Varga |
| A-05 | `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. | Ahmed Benali |
| A-06 | Prioritisation is MoSCoW from the business case, then date and dependency risk. NFRs are Must. | Lena Varga |
| A-10 | Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. | Ahmed Benali |
| A-11 | Portal release 1 covers French and English. Dutch follows. | Sofie Peeters, Lena Varga |
| A-12 | A customer administrator role exists. Who gets it is **OPEN:**. | Lena Varga |
| A-13 | Claims acceptance criteria cover only claims above EUR 500 and no self-approval. The other path is **OPEN:**. | Julien Moreau |
| A-14 | Spreadsheet migration is a separate unplanned item. | Lena Varga, Julien Moreau |
| A-15 | The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. | Julien Moreau |
| A-16 | 24 months is a display window over the complete history held in the database. | Ahmed Benali |
| A-17 | Pilot customer concurrency is small (20 customers). No customer load figure exists. | Ahmed Benali |
| A-18 | The warehouse for each claim line can be derived from StockPilot or product data. It is not on order lines. | Pieter Janssens |
| A-19 | In `dotnet-r2`, staff onboard customer users until `BR-08` is built. | Lena Varga |
| A-20 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | Ahmed Benali |
| A-21 | A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. | Ahmed Benali |
| A-22 | Premium Power Platform licences are needed for custom connectors and may exceed EUR 17.31 per user per month. Prices are unverified. | Ahmed Benali |
| A-23 | Dataverse use also needs a premium licence outside the Teams environment. | Ahmed Benali |
| A-24 | Azure runs in UTC by default. Order Desk stores local time. Parity needs explicit handling. (From the code, not in `knowledge-docs`.) | Ahmed Benali |
| A-25 | The Q1 2027 claims pilot cannot be committed while BA-03 has no team. | Lena Varga, Marc Dubois |
| A-27 | The StockPilot CSV contract and file pick-up stay as they are. | Ahmed Benali |
| A-29 | The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. | Ahmed Benali |
| A-30 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | Ahmed Benali |
| A-31 | Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). | Ahmed Benali |
| A-32 | Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. | Ahmed Benali |
| A-33 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Ahmed Benali |
| A-34 | Claim capture with photos and two-step approval is feasible with standard Power Apps and Power Automate features. | Ahmed Benali |
| A-35 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | Lena Varga |
| A-36 | BA-03 priority bands P1 to P3 are not release tags. | Lena Varga |
| A-37 | The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. | Ahmed Benali |
| A-38 | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-40 | Enabler id families `EN-`, `EA-`, `EP-` and hundreds blocks per track for `EPIC-`, `FEAT-`, `STORY-` and `FR-`. | Lena Varga |
| A-41 | Release counts Azure 3, .NET 3, Power Platform 0 hold, with the three placement changes in PRD section 6.3. | Lena Varga, Marc Dubois |
| A-42 | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-43 | Cross-cutting NFRs are split per track and, where design and proof differ, per release. The first recovery test plan is `EA-14`. | Ahmed Benali |
| A-44 | BA-03 is in scope for `BR-14` to `BR-19`, `NFR-09` and the BA-03 side of `NFR-03` and `NFR-04`. No placeholder release. | Lena Varga |
| A-45 | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | Backlog rank per track: enablers before the features that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-47 | BRD and PRD carry the ids `BRD-NW-001` and `PRD-NW-001` with `status: draft`. Lena Varga owns them. Marc Dubois and Ahmed Benali are the proposed reviewers. | Lena Varga |
| A-48 | In an unattended run the interactive builders take the plan's answers. Leftovers become **OPEN:** items. | Lena Varga |
| A-49 | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must (A-06). An enabler that serves only another track's requirements is Should (so `EN-14` and `FR-240` are Should). | Lena Varga |
| A-50 | The users and journeys in the PRD (section 3) are role descriptions taken from `business-case.md` and `current-state.md`. They are not research-based personas. | Lena Varga |
| A-51 | Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. | Ahmed Benali |
| A-52 | `FR-234` (instrumentation for SM-01 to SM-04) is Should, because the business case gives the measures no priority and names no measurement source. | Lena Varga |
| A-53 | Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). | Ahmed Benali |
| A-54 | The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. | Ahmed Benali, Lena Varga |
| **A-55** | **New.** The backlog authoring decisions BD-01 to BD-05 (section 1.4): one story per `FR-`, enabler and story kept distinct, feature grouping chosen here, plain titles, no invented numbers. | Lena Varga |
| **A-56** | **New.** A warning for a possible duplicate claim (same order line and reason) is part of recording a claim, derived from SM-06 (11 % of claims lost or recorded twice; target under 1 %). Not stated in `FR-310`. | Lena Varga |
| **A-57** | **New.** For the claims dashboard, "time to resolve" runs from the claim being recorded to it being approved or rejected. The business case does not define it. | Lena Varga |
| **A-58** | **New.** The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). | Marc Dubois |
| **A-59** | **New.** `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. | Ahmed Benali |

### 7.2 OPEN register (ES-04)

An open item is a question nobody has answered yet.

| Id | OPEN | Who can answer |
|---|---|---|
| O-01 | Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? | Ahmed Benali |
| O-02 | Does BA-03 need a premium licence, a data gateway or a custom connector inside C-07 and C-08? Is Dataverse used? | Ahmed Benali |
| O-03 | Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-04 | What status freshness is acceptable, given the nightly batch? | Lena Varga |
| O-05 | Does "portal launch" mean the pilot or general availability? | Lena Varga |
| O-06 | Which backlog tool and which ES-28 prefix? Also: item types and fields in the tool are not validated. | Lena Varga |
| O-07 | Who is the BA-03 team, what are their skills, and what is the intended date (or is BA-03 unplanned)? | Lena Varga, Marc Dubois |
| O-08 | Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. | Ahmed Benali |
| O-09 | Who is the named release approver for each track? | Marc Dubois |
| O-10 | Which identity provider do customer users use (OQ-01)? | Ahmed Benali |
| O-11 | Must Dutch be in the first release (OQ-02)? | Sofie Peeters, Lena Varga |
| O-12 | Do customer administrators exist for every customer or only for large ones (OQ-03)? | Lena Varga |
| O-13 | Who approves claims of EUR 500 or less (OQ-04)? | Julien Moreau, Lena Varga |
| O-14 | Must the claims already in the spreadsheet be moved to the new solution (OQ-05)? | Lena Varga, Julien Moreau |
| O-15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-16 | How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? | Ahmed Benali, Pieter Janssens |
| O-17 | What sends order confirmations today? | Ahmed Benali |
| O-18 | Where do the customer e-mail address and language preference live? | Lena Varga |
| O-19 | Which build and deployment pipeline tool? | Ahmed Benali |
| O-20 | Decision record on the portal and API project shape (ES-13). | Ahmed Benali |
| O-21 | Approval and funding to build (the business case says "not yet approved for build"). | Marc Dubois |
| O-22 | Which tool for the claims dashboard (BR-18) within C-08? | Lena Varga |
| O-23 | Which database does the Q2 2027 portal pilot read (T-08)? | Ahmed Benali |
| O-24 | What does the customer identity service cost, and does it count toward C-04? | Ahmed Benali |
| O-25 | Confirm the release counts, windows and the three placement changes (PRD section 6.3). | Lena Varga, Marc Dubois |
| O-26 | Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. | Lena Varga |
| O-27 | Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. | Marc Dubois |
| **O-28** | **New.** What happens to a line of a copied order whose product is no longer available (`STORY-234`)? Not stated in the sources. | Lena Varga |
| **O-29** | **New.** What columns, file naming and format does the finance system's CSV import expect for a credit-note request (`EP-05`, `STORY-322`)? Not stated in the sources. | Julien Moreau |
| **O-30** | **New.** Which values may a warehouse supervisor record as the cause of a claim (`STORY-350`)? Not stated in the sources. | Pieter Janssens |
| **O-31** | **New.** Is the CC-BY 4.0 licence line in the BRD and PRD frontmatter intended? The licence is unchanged. | Lena Varga |

### 7.3 Cross-track dependencies (`X-nn`), all OPEN, none is a wait

"A needs B" means track A needs something from track B. Each needing track keeps delivering as shown in the item (ES-31, A-45). Full text is in the PRD, section 10.1.

| Id | OPEN: dependency (short) | Needs | Owner to confirm |
|---|---|---|---|
| X-01 | Hosting target and pilot test environment for the modernised application | .NET needs Azure | Ahmed Benali |
| X-02 | A `net10.0` application that follows a documented configuration and identity contract | Azure needs .NET | Ahmed Benali |
| X-03 | Database sign-in moves from Windows-integrated to Entra or a managed identity | Both | Ahmed Benali |
| X-04 | Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) | .NET needs Azure or IT | Ahmed Benali |
| X-05 | StockPilot exchange redesign for a managed data tier; file contract fixed | .NET needs Azure | Ahmed Benali |
| X-06 | Status freshness is bounded by the exchange cadence | .NET needs Azure and StockPilot | Lena Varga |
| X-07 | The in-process session draft must be stateless before scale-out | Azure needs .NET | Ahmed Benali |
| X-08 | Logging moves to Application Insights and Log Analytics | .NET needs Azure | Ahmed Benali |
| X-09 | Invoice files move from a network path to Azure storage | Both | Julien Moreau, Ahmed Benali |
| X-10 | Outbound mail replaces the on-premises relay | Both | Ahmed Benali |
| X-11 | Build and test pipeline (.NET) and deployment pipeline (Azure) | Both | Ahmed Benali |
| X-12 | The shared monthly cap C-04 covers Order Desk and the portal | Azure needs .NET sizing inputs | Ahmed Benali |
| X-13 | An internet-facing entry for customers while data services use private endpoints | .NET needs Azure | Ahmed Benali |
| X-14 | One solution and three projects versus a portal area and an API: a decision record is needed | Both | Ahmed Benali |
| X-15 | Keeping the 7-year audit trail once the database is in Azure | .NET needs Azure | Ahmed Benali |
| X-20 | An Order Desk API (read orders and lines) for the custom connector | Power Platform needs .NET | Ahmed Benali |
| X-21 | An order data contract for claims: order number, lines, quantities, prices, customer, warehouse | Power Platform needs .NET | Lena Varga, Pieter Janssens |
| X-22 | The API endpoint must be reachable from Power Platform while data services stay private | Power Platform needs Azure | Ahmed Benali |
| X-23 | Connector sign-in (Entra app registration, OAuth) | Power Platform needs Azure or IT | Ahmed Benali |
| X-24 | Finance CSV drop before 18:00, and where the share lives after the lease | Power Platform needs Azure | Julien Moreau, Ahmed Benali |
| X-25 | Warehouse for each order line, for `BR-17` | Power Platform needs .NET and StockPilot data | Pieter Janssens |
| X-26 | Customer e-mail address, for `BR-19` and the portal's `BR-09` | Both | Lena Varga |
| X-27 | Environments, DLP and licensing: administration of the Microsoft 365 tenant | Power Platform needs IT | Ahmed Benali |

### 7.4 Other ids cited

| Id | Meaning | Owner |
|---|---|---|
| T-01 | `BR-04` says "always up to date" but Picking and Shipped change once a night (handled by A-03). | Lena Varga |
| T-03 | C-04 is a shared cap held only by BA-01 (handled by A-02, X-12). | Ahmed Benali |
| T-08 | The Q2 2027 portal pilot and C-05 versus the database migration (A-37, O-23). | Ahmed Benali |
| T-10 | ES-13 (one solution) and ES-19 versus a portal, an API and a re-platform (`EN-13`). | Ahmed Benali |
| T-13 | `NFR-08` asks for who, what, when and channel but today's audit rows may not record all (listed, not fixed silently). | Ahmed Benali |
| T-14 | The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). | Ahmed Benali |
| T-15 | `NFR-03` and `NFR-04` apply "wherever relevant" but BA-02 does not list `NFR-03` and BA-01 does not list `NFR-04` (split per track, A-43). | Ahmed Benali |
| T-17 | `NFR-01` uses CET only but business hours cross the summer-time change (A-05). | Ahmed Benali |
| G-01, G-03, G-08, G-10 | Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. | Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10) |
| OQ-01 to OQ-05 | Business-case open questions, carried as O-10, O-11, O-12, O-13, O-14. | as the O- rows |
| MVE-A-03 | Growth stays linear. From mid-November 2026 to 30 June 2027 is 7 to 7.5 months, so the database reaches about 56 GB (48 GB plus 7.5 months at 1 GB) and invoices about 135 GB (120 GB plus 7.5 months at 2 GB). The month count is itself an assumption. | Ahmed Benali |
| MVE-A-04 | A local SQL Server (Developer edition or container) is available to run the database scripts. | Ahmed Benali |
| MVE-A-08 | The licence class of each Power Platform capability is read from primary Microsoft documentation at experiment time. | Ahmed Benali |
| MVE-A-09 | Whether a flow can run under a shared or service identity without a premium licence for every user is unknown. | Ahmed Benali |
| MVE-O-04 | How a CSV made in the cloud reaches the finance import share before 18:00, and who runs and pays for it. | Julien Moreau, Ahmed Benali |
| MVE-O-05 | Where the SQL Server Agent job and the Windows scheduled task for the Antwerp transfer are defined. | Ahmed Benali |

### 7.5 Release-local ids

These ids are defined in the release file named in the second column. The text and owner are copied here so that this section stays the register of record. `G-` ids in 7.4 are intake-review gaps; `T-` ids are tensions defined in PRD section 11.

| Id | Release file | ASSUMPTION or OPEN | Owner |
|---|---|---|---|
| A-D1-01 | `dotnet-r1` | **ASSUMPTION:** The team has a .NET 10 SDK and a local SQL Server for the exit tests; no cloud resource is needed to finish this release. Not stated in `knowledge-docs`. | Ahmed Benali |
| A-D1-02 | `dotnet-r1` | **ASSUMPTION:** The regression checklist for the staff screens (`STORY-201/AC2`) is written by the .NET team from the current screens and reviewed by the product owner; the backlog does not name an author. | Ahmed Benali |
| A-D2-01 | `dotnet-r2` | **ASSUMPTION:** The team has a local SQL Server and the sample data to run the exit tests, including a data set with orders for at least two customers. | Ahmed Benali |
| A-D2-02 | `dotnet-r2` | **ASSUMPTION:** Approval of this release covers code, tests and review evidence produced locally. Choosing the 20 pilot customers, hosting the pilot and running it with real customers follow approval and are not claimed here. The backlog does not say who chooses the 20 customers; the proposal is Lena Varga with Sofie Peeters, as for MVE-02 contacts. | Lena Varga |
| A-D3-01 | `dotnet-r3` | **ASSUMPTION:** Pilot feedback from `dotnet-r2` reaches the product owner before `dotnet-r3` items are committed. The backlog places the items after pilot feedback but does not describe how feedback is collected. | Lena Varga |
| A-D3-02 | `dotnet-r3` | **ASSUMPTION:** Approval of this release covers code, tests and documents produced locally. General availability itself, hosting and rollout follow approval and are not claimed here. | Lena Varga |
| O-D2-01 | `dotnet-r2` | **OPEN:** The `dotnet-r2` window (1 Mar to 30 Apr 2027) overlaps the `azure-r2` window (1 Feb to 31 Mar 2027) by 31 days. The dependency is the database the pilot reads after `azure-r2` is approved (A-37, O-23), not a start order. `dotnet-r2` builds and tests locally under X-01 and does not wait. Confirm this reading. | Lena Varga, Ahmed Benali |
| O-D2-02 | `dotnet-r2` | **OPEN:** The canonical theme says "(Must items)" but this release contains one Should item, `STORY-237` (French and English), because `BR-11` is split by language (C3). Confirm that the theme wording may stay with the explanation in section 2, or reword the theme in C1 and every document at once. This file keeps the canonical theme and does not move the item. | Lena Varga |
| O-D3-01 | `dotnet-r3` | **OPEN:** `STORY-264` must stay Draft until O-26 names the data and the source. If O-26 is still open at approval, does the product owner approve `dotnet-r3` without it, recording the story as not started? This file does not move the item. | Lena Varga |
| O-D3-02 | `dotnet-r3` | **OPEN:** Wording difference between documents. `experiments.md` section 3.2.5 says a MVE-02 Stop holds back the customer-facing portal stories of `EPIC-202` and `EPIC-203`. The backlog and PRD gate only `STORY-264` in `EPIC-203`. Which reading is right for the other items of this release (`EN-07`, `STORY-260` to `STORY-263`, `EN-14`, `STORY-265`)? This file follows the item-level gates (only `STORY-264`) until the owner decides, and does not edit either document. | Lena Varga |
| AZ1-O1 | `azure-r1` | **OPEN:** The hosting runtime choice (rehost the unchanged application on a Windows virtual machine, or wait for `net10.0`) is not made. `EA-15` in `azure-r2` defines the hosting and names the runtime it describes. Confirm the runtime before `EA-15` is committed (O-03, A-20). | Ahmed Benali (O-03), Lena Varga (commitment) |
| AZ1-O2 | `azure-r1` | **OPEN:** If MVE-01 ends in **stop**, does the product owner approve `azure-r1` without `EA-05`, `EA-09` and their stories, or hold the release? Items do not move. | Lena Varga, Marc Dubois |
| AZ2-O1 | `azure-r2` | **OPEN:** If MVE-01 ends in **stop**, does the product owner approve `azure-r2` without the paused items (`EA-06`, `EA-08`, `EA-10` and their stories) and without the production database settings of `EA-15`, or hold it? Items do not move. | Lena Varga, Marc Dubois |
| AZ2-O2 | `azure-r2` | **OPEN:** Which runtime does `EA-15` describe first: the unchanged application rehosted on a Windows virtual machine (A-20), or a managed web service for `net10.0`? Confirm before `EA-15` is committed (O-03). | Ahmed Benali |
| AZ3-O1 | `azure-r3` | **OPEN:** If MVE-01 ends in **stop**, does the product owner approve `azure-r3` without the affected items (`EA-16`, `EA-13`, `EA-14` and their stories), or hold it? Items do not move. | Lena Varga, Marc Dubois |
