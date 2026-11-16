---
release_id: "dotnet-r2"
title: "Release dotnet-r2: Portal pilot (Must items) for 20 customers"
track: "dotnet"
release: "dotnet-r2"
track_tag: "track-dotnet"
release_tag: "dotnet-r2"
planned_git_tag: "product/dotnet-r2"
git_tag_created: false
status: "proposed"
document_status: "Draft for review"
target_window: "1 Mar to 30 Apr 2027"
approver: "OPEN: O-09"
approval_date: ""
experiment_gate: "MVE-02 (not run, result pending)"
source_backlog_id: "BACKLOG-NW-001"
source_backlog_path: "docs/product/backlog.md"
source_prd_id: "PRD-NW-001"
source_brd_id: "BRD-NW-001"
owners: ["Lena Varga"]
created_date: "2026-11-15"
---

# Release dotnet-r2: Portal pilot (Must items) for 20 customers

> Status: **Draft for review** | Release status: **Proposed, awaiting product-owner approval** | Track: `track-dotnet` | Release tag: `dotnet-r2`
>
> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> This is a document. Nothing was built, deployed or published to a tracker to write it, and **no Git tag or commit exists for this release** (A-39, ES-27).

## 1. Document control

| Field | Value |
|---|---|
| Track | .NET, business area BA-02 (Ordering and customer self-service) |
| Track tag (ES-30) | `track-dotnet` |
| Release tag (ES-31) | `dotnet-r2` |
| Planned Git tag | `product/dotnet-r2` — **to be created on approval; not created** |
| Release status | Proposed, awaiting product-owner approval |
| Document status | Draft for review |
| Approver | **OPEN:** O-09 — the named approver for each track is not decided. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner to confirm: Marc Dubois. |
| Approval date | (blank until a human approves) |
| Release owner (document) | Lena Varga |
| Experiment gate | MVE-02 — **not run; result pending** |
| Source documents | [backlog.md](../backlog.md) (item list is authoritative), [traceability.md](../traceability.md), [product-requirements.md](../product-requirements.md), [business-requirements.md](../business-requirements.md), [experiments.md](../experiments.md) |
| Rule | **A release never waits for another track** (ES-31). Needs from another track are **OPEN:** rows in section 7, each with a way to keep delivering. |

## 2. Objective, theme and target window

**Theme:** Portal pilot (Must items) for 20 customers. This is the canonical theme text from C1 and is kept word for word so every product document agrees. **What the release actually contains:** all the Must items of the pilot, **plus one Should item**, `STORY-237` (French and English, `BR-11`). The release is therefore not "Must only". The reason and the open question are in the note below (**OPEN:** O-D2-02).

**Objective.** Let 20 pilot customers sign in, see only their own company's orders, open an order, see its status with an "as of" time, create a new order by copying a previous one, and see their negotiated prices, in French or English (the French and English part is the one Should item). Staff see each order arrive in Order Desk as Received and can tell whether it came from the portal. The release also covers the quality requirements that apply to the portal: response time, data residency, customer sign-in, accessibility and the audit trail (source: EPIC-202, BR-01 to BR-06, BR-10, BR-11, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08, C-05, CS-10).

**Target window:** 1 Mar to 30 Apr 2027. A target, not a commitment (A-01, A-42; **OPEN:** O-25, owners Lena Varga and Marc Dubois).

**Main epic:** `EPIC-202` Customer portal pilot: sign-in, orders, status, reorder.

**Note on the theme and the one Should item.** 13 of the 14 stories here are Must; the epic, the 5 features and the enabler are Must too (the epic and the features take the highest priority of their children). `STORY-237` (French and English, `BR-11`) is **Should**. **Reason it is here:** `BR-11` is split by language (C3, ES-31): French and English in `dotnet-r2`, Dutch in `dotnet-r3` (A-11), and a pilot for customers in France, Belgium and Luxembourg needs at least French and English. The Should item is **not** a Must item and does not become one by being here. **OPEN:** O-D2-02 asks Lena Varga whether the canonical theme wording "(Must items)" should be reworded in C1 and in every document at once; this file does not change the theme or move the item. **OPEN:** O-11 (must Dutch be in the first release?), owners Sofie Peeters and Lena Varga.

### 2.1 Experiment gate: MVE-02

MVE-02 asks: *will customers reorder unaided and trust a night-old status?* It is a moderated test of a clickable prototype with 5 to 8 customers (source: experiments.md section 3.2). **It has not been run. The result is pending, and this file never states an outcome.** A gate is a decision point taken **before** the gated item is committed. It is not a wait on another track and not a release wait (backlog section 1).

Pass checks (thresholds are an **ASSUMPTION:** A-35; Lena Varga sets the final numbers):

* **R1** at least 80 % of participants finish a reorder unaided (copy a previous order, change two quantities, remove one line, submit).
* **R2** at least 60 % would use the shown status instead of phoning when an order shows Picking or Shipped "as of last night".
* **R3** is recorded as a reading only (the median share of last 10 orders they would place through the portal, compared with the 35 % of `SM-01`).

Items gated by MVE-02 in this release: `EN-11` (for the channel part, `BR-10`), `STORY-233` (R2), `STORY-234` (R1), `STORY-236` and `STORY-238`; their features `FEAT-207`, `FEAT-208` and `FEAT-209` show the gate too.

| MVE-02 result | Effect on `dotnet-r2` (source: experiments.md section 3.2.5) |
|---|---|
| **Go** (R1 and R2 pass) | Build the portal pilot as planned. The stories for `BR-04` and `BR-05` are committed as written, with the "as of" wording (A-03). The scope of `dotnet-r2` stays as in this file. |
| **Adjust** (one of R1 and R2 fails, or the R3 median is far below 35 %) | Change the design or the promise, then retest if cheap. A failed R2: ask whether StockPilot's pick-up can run more than nightly without changing StockPilot (**OPEN:** O-16, owners Ahmed Benali and Pieter Janssens), rename "Picking" so it is not misleading, or put a lower `SM-02` target back to Lena Varga (**OPEN:** O-04). A failed R1: simplify the copy flow before `EPIC-202` is committed. The acceptance criteria and wording of the `BR-04` stories change, and the `SM-01` and `SM-02` targets go back to Lena Varga. |
| **Stop** (R1 and R2 both fail) | Do not commit the customer-facing portal stories (`EPIC-202`, `EPIC-203`) until the reason is understood. `EPIC-201` parity work (`dotnet-r1`) continues. Lena Varga and Marc Dubois decide on the portal business case. |

The decision owner is Lena Varga. A decision record of the result is an entry condition for the gated items (section 8).

## 3. Items in this release

21 items: 1 epic, 5 features, 14 stories, 1 enabler. Every item carries the track tag `track-dotnet` **and** the release tag `dotnet-r2`, and appears in no other release (ES-31). Ids and titles are copied from the backlog item register (section 2.2). Rank is the order inside the .NET track (A-46).

| Id | Title | Type | Priority | Rank | Source ids | Track tag | Release tag | MVE gate |
|---|---|---|---|---|---|---|---|---|
| EPIC-202 | Customer portal pilot: sign-in, orders, status, reorder | epic | Must | — | BR-01 to BR-06, BR-10, BR-11, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08, C-05, CS-10 | `track-dotnet` | `dotnet-r2` | MVE-02 (`STORY-233`, `STORY-234`, `STORY-236`, `STORY-238`) |
| FEAT-206 | Customer sign-in, company isolation and data residency | feature | Must | — | BR-01, NFR-03, NFR-04, CS-04, CS-05 | `track-dotnet` | `dotnet-r2` | none |
| EN-11 | Build the authorisation foundation for customer scoping and channel | enabler | Must | 18 | BR-01, BR-10; **ASSUMPTION:** A-51 | `track-dotnet` | `dotnet-r2` | MVE-02 (channel part, `BR-10`) |
| STORY-230 | Sign in and see only my own company's orders | story | Must | 19 | BR-01, CS-04, CS-05; **ASSUMPTION:** A-51 | `track-dotnet` | `dotnet-r2` | none |
| STORY-240 | Authenticate customers with an externally managed identity | story | Must | 20 | NFR-04, OQ-01, CS-28 | `track-dotnet` | `dotnet-r2` | none |
| STORY-239 | Keep portal hosting, identity and mail data in the EU | story | Must | 21 | NFR-03, ES-20 | `track-dotnet` | `dotnet-r2` | none |
| FEAT-207 | Order list, order detail and status | feature | Must | — | BR-02, BR-03, BR-04, P-03, CS-10 | `track-dotnet` | `dotnet-r2` | MVE-02 (`STORY-233`) |
| STORY-231 | See my company's orders from the last 24 months | story | Must | 22 | BR-02, P-03 | `track-dotnet` | `dotnet-r2` | none |
| STORY-232 | Open an order and see lines, prices, address and status | story | Must | 23 | BR-03, P-03 | `track-dotnet` | `dotnet-r2` | none |
| STORY-233 | See one of six order statuses with an as-of time | story | Must | 24 | BR-04, P-03, CS-10, C-03 | `track-dotnet` | `dotnet-r2` | MVE-02 (R2: at least 60 % would use the status instead of phoning) |
| FEAT-208 | Reorder, submit and channel | feature | Must | — | BR-05, BR-06, BR-10, C-05, P-01, P-02, P-04 | `track-dotnet` | `dotnet-r2` | MVE-02 (`STORY-234`, `STORY-236`) |
| STORY-234 | Create a new order by copying a previous order | story | Must | 25 | BR-05, P-04 | `track-dotnet` | `dotnet-r2` | MVE-02 (R1: at least 80 % finish a reorder unaided) |
| STORY-235 | Have a submitted portal order appear in Order Desk as Received | story | Must | 26 | BR-06, C-05, P-01, P-02 | `track-dotnet` | `dotnet-r2` | none |
| STORY-236 | Show staff whether an order came from the portal or from staff | story | Must | 27 | BR-10, BR-06; **ASSUMPTION:** A-51 | `track-dotnet` | `dotnet-r2` | MVE-02 |
| FEAT-209 | Customer prices and language | feature | Must | — | BR-11, BR-12, CS-20, OQ-02 | `track-dotnet` | `dotnet-r2` | MVE-02 (`STORY-238`) |
| STORY-238 | Show my negotiated prices, not list prices | story | Must | 28 | BR-12, CS-20 | `track-dotnet` | `dotnet-r2` | MVE-02 |
| STORY-237 | Use the portal in French and English | story | Should | 29 | BR-11, OQ-02 | `track-dotnet` | `dotnet-r2` | none |
| FEAT-210 | Audit, accessibility and performance | feature | Must | — | NFR-02, NFR-07, NFR-08, CS-03, CS-05, ES-19 | `track-dotnet` | `dotnet-r2` | none |
| STORY-241 | Record who, what, when and channel for every order change | story | Must | 30 | NFR-08, ES-19; **ASSUMPTION:** A-51 | `track-dotnet` | `dotnet-r2` | none |
| STORY-242 | Check every pilot screen against WCAG 2.2 level AA | story | Must | 31 | NFR-07 | `track-dotnet` | `dotnet-r2` | none |
| STORY-243 | Respond in under 2 seconds at the 95th percentile | story | Must | 32 | NFR-02, CS-03, CS-05 | `track-dotnet` | `dotnet-r2` | none |

Item counts by type: epic 1, feature 5, story 14 (`STORY-230` to `STORY-243`), enabler 1 (`EN-11`). Total 21. These match backlog section 3.

## 4. Business and quality requirements covered

The "covered" column is the canonical C1 text for `dotnet-r2`:

> BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-10 (portal value), BR-11 (French and English), BR-12 (customer prices); NFR-02, NFR-03 (.NET), NFR-04 (customers), NFR-07, NFR-08 (content)

| Identifier | Priority | Part covered here | Covering story | Supporting items | Other parts of the same identifier |
|---|---|---|---|---|---|
| BR-01 | Must | Whole requirement, including the negative case | `STORY-230` | `EN-11`, `EN-08` (`dotnet-r1`), `EN-12` (`dotnet-r1`) | none |
| BR-02 | Must | Whole requirement | `STORY-231` | `EN-10`, `STORY-206` (`dotnet-r1`) | none |
| BR-03 | Must | Whole requirement | `STORY-232` | `EN-11` | none |
| BR-04 | Must | Whole requirement, with the "as of" rule (A-03) | `STORY-233` | none | none |
| BR-05 | Must | Whole requirement | `STORY-234` | `EN-06` (`dotnet-r1`) | none |
| BR-06 | Must | Whole requirement | `STORY-235` | none | none |
| BR-10 (portal value) | Must | Staff see the portal or staff channel | `STORY-236` | `EN-11` | Parity: `dotnet-r1`, `STORY-203` |
| BR-11 (French and English) | Should | French and English | `STORY-237` | none | Dutch: `dotnet-r3`, `STORY-263` |
| BR-12 (customer prices) | Must | Negotiated prices for customers | `STORY-238` | `EN-10`, `STORY-202` (`dotnet-r1`) | Parity: `dotnet-r1`, `STORY-202` |
| NFR-02 | Must | Server-side 95th percentile under 2 seconds (A-05) | `STORY-243` | none | none |
| NFR-03 (.NET) | Must | Portal hosting, identity and mail stay in the EU | `STORY-239` | none | Azure: `azure-r1` (another track). BA-03: unplanned. |
| NFR-04 (customers) | Must (A-06) | Customer sign-in | `STORY-240` | `EN-08` (`dotnet-r1`) | Staff: `dotnet-r1`, `STORY-204`. BA-03: unplanned. Azure side: **OPEN:** X-04. |
| NFR-07 | Must | WCAG 2.2 level AA review of every pilot screen | `STORY-242` | none | none |
| NFR-08 (content) | Must | Who, what, when and channel of every order change | `STORY-241` | `EN-11` | Retention design: `azure-r2` (another track, **OPEN:** X-15). |

## 5. What this release leaves out, and where it moves

| Left out | Where it goes | Why |
|---|---|---|
| Invoice download (`BR-07`: `FEAT-211`, `EN-07`, `STORY-260`) | `dotnet-r3` | Should; `EN-07` was moved here from the research proposal so the pilot carries no invoice work (C2). |
| Customer user administration (`BR-08`: `STORY-261`); staff onboard customer users until then (A-19) | `dotnet-r3` | Should; scope depends on **OPEN:** O-12. |
| Shipping e-mail (`BR-09`: `STORY-262`) | `dotnet-r3` | Could; mail path **OPEN:** O-17, X-10. |
| Dutch (`BR-11` Dutch part: `STORY-263`) | `dotnet-r3` | A-11; **OPEN:** O-11. |
| Success-measure data for `SM-01` to `SM-04` (`STORY-264`) | `dotnet-r3` | Instrumentation follows the pilot; MVE-02 gate; **OPEN:** O-26. |
| Order Desk API contract (`EN-14`, `STORY-265`) | `dotnet-r3` | No consumer until BA-03 has a team (O-07). |
| Order Desk API implementation (`EPIC-204`, `FEAT-215`, `STORY-280`) | Unplanned; carries only `track-dotnet` until **OPEN:** O-01 is answered | A conditional item cannot carry a release tag (ES-31). |
| All BA-03 items | Unplanned, `track-power-platform`; no release exists | No team (G-08, O-07). |
| Parity work (`EPIC-201`) | `dotnet-r1` | Already delivered earlier in this track. |
| Hosting, pilot environment, exchange redesign, retention design | `azure-r1` and `azure-r2` (another track) | Delivered by the Azure team (A-02); needs are **OPEN:** rows in section 7. |

## 6. Items that this release builds on inside the .NET track

These are not cross-track dependencies. They are items of `dotnet-r1` that `dotnet-r2` items depend on (source: backlog item blocks).

| `dotnet-r2` item | Needs from `dotnet-r1` |
|---|---|
| `EN-11` | `EN-08` |
| `STORY-230` | `EN-08`, `EN-12` |
| `STORY-240` | `EN-08` |
| `STORY-231` | `EN-10` |
| `STORY-234` | `EN-06` |
| `STORY-238` | `EN-10`, `STORY-202` |
| `STORY-243` | `EN-10` |

## 7. Dependencies on other tracks (all OPEN, none is a wait)

**A release never waits for another track** (ES-31, A-45). **`dotnet-r2` proceeds without waiting for the Azure track, StockPilot, IT or any other owner.** Every row below is **OPEN:** until its owner confirms it, and each row says how the .NET team keeps delivering meanwhile (local SQL Server, local test identity, the "as of" time instead of a live claim, access only through Order Desk). The table lists **every** `X-nn` that an item of this release cites in the backlog (8 ids: X-01, X-04, X-05, X-06, X-07, X-12, X-13, X-15), plus the questions O-23 and A-37 from C11. Rows from C11 and the `EPIC-202` entry are X-01, X-04, X-05, X-06, X-13, X-15, O-23 and A-37; X-07 and X-12 are cited by items only.

"Role" shows the side of `dotnet-r2`: **consumer-side** means this release needs something from another track; **supplier-side** means another track needs something from this release (the row is then carried in the Azure release file of the needing track as that track's **OPEN:** row, and is listed here for completeness, never as a wait).

| Id | **OPEN:** dependency | Role of `dotnet-r2` | Direction | Owner to confirm | How `dotnet-r2` proceeds without waiting | Items |
|---|---|---|---|---|---|---|
| X-01 | Hosting target and pilot test environment for the modernised application | Consumer-side | .NET needs Azure | Ahmed Benali | Build and test locally with a local SQL Server and the `EN-12` sample data; no hosting is needed to finish the code. The pilot environment stays **OPEN:**. | `STORY-230`, `STORY-235` |
| X-04 (customers) | Customer sign-in follows O-10 (OQ-01); the Azure or IT side stays **OPEN:** | Consumer-side | .NET needs Azure or IT | Ahmed Benali | Provider-neutral sign-in (A-10) with a local test identity (`STORY-240/AC2`, `STORY-240/AC3`); no real customer account is needed. | `EN-11`, `STORY-230`, `STORY-240` |
| X-05 | StockPilot exchange redesign for a managed data tier; the file contract is fixed | Consumer-side | .NET needs Azure | Ahmed Benali | The StockPilot CSV contract and file pick-up stay as they are (A-27). The portal shows the status as Order Desk holds it and shows the "as of" time. | `STORY-233` |
| X-06 | Status freshness is bounded by the exchange cadence | Consumer-side | .NET needs Azure and StockPilot | Lena Varga | Show Picking and Shipped with the time of the last nightly update, and never claim to be live (A-03, `STORY-233/AC2`, `STORY-233/AC4`). MVE-02 R2 tests whether customers trust this. | `STORY-233` |
| X-07 | The in-process session draft must be stateless before scale-out | **Supplier-side** | Azure needs .NET | Ahmed Benali | `EN-06` (`dotnet-r1`) supplies it, and `STORY-234/AC3` proves a draft survives a restart or another instance. Azure starts with a single instance until then (`azure-r3` row). | `STORY-234` |
| X-12 | The shared monthly cap C-04 covers Order Desk and the portal | **Supplier-side** | Azure needs .NET sizing inputs | Ahmed Benali | `STORY-243/AC2` uses today's load (CS-03, CS-05) and the agreed pilot customer figure (**OPEN:** O-08, A-17) as the sizing input to hand over (`azure-r1` row). | `STORY-243` |
| X-13 | An internet-facing entry for customers while data services use private endpoints | Consumer-side | .NET needs Azure | Ahmed Benali | Azure designs the entry; .NET lists every service it uses with its region (`STORY-239/AC1`) and does not depend on the entry design to finish its stories. | `STORY-239` |
| X-15 | Keeping the 7-year audit trail once the database is in Azure | Consumer-side | .NET needs Azure | Ahmed Benali | Record who, what, when and channel of each change (`STORY-241`); retention is Azure's design (A-31). Known gaps in today's records are listed, not fixed silently (T-13). | `STORY-241` |
| O-23 | Which database does the Q2 2027 portal pilot read (T-08)? | Consumer-side | .NET needs Azure | Ahmed Benali | The portal reads and writes orders only through Order Desk, with no second order database (`STORY-235/AC2`, C-05); tests run on the local database. The pilot database stays **OPEN:**. | `STORY-235`, `EPIC-202` |
| A-37 | **ASSUMPTION:** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. | Consumer-side | .NET needs Azure | Ahmed Benali | If it is not true, the pilot reads the database named in O-23 through Order Desk; the stories do not change. | `STORY-235`, `EPIC-202` |

Other related questions, **OPEN:** O-04 (acceptable status freshness; Lena Varga), O-08 (order-to-invoice mapping, retention, customer concurrency, warehouse per order line; Ahmed Benali), O-10 (customer identity provider; Ahmed Benali), O-16 (how Delivered is set, pick-up cadence; Ahmed Benali and Pieter Janssens), O-18 (customer e-mail and language preference; Lena Varga), O-24 (customer identity service cost and C-04; Ahmed Benali), O-28 (copied order line whose product is no longer available; Lena Varga).

## 8. Entry conditions

| Id | Condition | Evidence | Status |
|---|---|---|---|
| EN-C1 | Approval and funding to build is given. | **OPEN:** O-21, owner Marc Dubois. | Not met; the window is a target (A-01). |
| EN-C2 | The `dotnet-r1` items listed in section 6 exist and pass their own criteria. This is inside the .NET track, not a wait on another track. | `dotnet-r1` exit criteria | Pending |
| EN-C3 | A **recorded MVE-02 decision** (Go, Adjust or Stop) exists **before** the gated items are committed: `EN-11` (channel part), `STORY-233`, `STORY-234`, `STORY-236`, `STORY-238`. An Adjust or Stop changes the scope of this file through the product owner. | experiments.md section 3.2.5 | Pending; MVE-02 is not run. Owner Lena Varga. |
| EN-C4 | The product owner has reviewed this file and the items in section 3. | Section 11 | Pending |
| EN-C5 | A local SQL Server and the `EN-12` sample data are available. | `EN-12` | **ASSUMPTION:** A-D2-01. Owner Ahmed Benali. |

## 9. Exit and acceptance criteria

The release is ready for approval only when **every** criterion is met. Each is tied to items in section 3; the Given / When / Then wording is in [backlog.md](../backlog.md) under the criterion id. "Done" means code and tests pass on a developer machine or a build runner and the review evidence is recorded. No deployment and no live pilot is claimed (ES-27; **ASSUMPTION:** A-D2-02).

| Id | Exit criterion | Tested by | Items |
|---|---|---|---|
| EX-1 | **Isolation (`BR-01`).** Every order a customer user sees belongs to their company. **Negative case:** a signed-in user of company A who asks for an order of company B (for example by changing the order number in the web address) is refused and sees no data of company B; no row of company B appears in the list; a failed sign-in shows no order data. The authorisation foundation refuses invoice and order requests across companies and a status change by a non-staff user. | `STORY-230/AC1` to `STORY-230/AC4`, `EN-11/AC1`, `EN-11/AC2`, `STORY-232/AC3` | `STORY-230`, `EN-11`, `STORY-232` |
| EX-2 | **Status freshness (`BR-04`).** Every order shows exactly one of Received, Confirmed, Picking, Shipped, Delivered, Cancelled. Picking and Shipped carry an "as of" time equal to the last nightly StockPilot update; Received, Confirmed and Cancelled carry the time of the last change; the portal never claims to be live; Delivered set by staff shows as Delivered (A-03). | `STORY-233/AC1` to `STORY-233/AC5` | `STORY-233` |
| EX-3 | **Order list and detail (`BR-02`, `BR-03`).** The last 24 months are listed with date, status and total; older orders are not listed; an empty list shows a message; an order shows lines, prices, address and status. | `STORY-231/AC1` to `STORY-231/AC3`, `STORY-232/AC1`, `STORY-232/AC2` | `STORY-231`, `STORY-232` |
| EX-4 | **Reorder and submit (`BR-05`, `BR-06`).** A copied order has the same lines and quantities; the submitted order has exactly the user's changes; a draft survives a restart or another instance; an empty draft cannot be submitted; a submitted order appears in Order Desk as Received without re-keying; the portal uses Order Desk and creates no second order database (C-05); when Order Desk cannot take the order, no partial order exists. | `STORY-234/AC1` to `STORY-234/AC4`, `STORY-235/AC1` to `STORY-235/AC3` | `STORY-234`, `STORY-235` |
| EX-5 | **Channel (`BR-10`).** A portal order shows the channel portal and a staff order shows staff; the server ignores any channel value sent by the customer. | `STORY-236/AC1` to `STORY-236/AC3`, `EN-11/AC3` | `STORY-236`, `EN-11` |
| EX-6 | **Prices (`BR-12`) and pricing parity.** The customer sees the negotiated price, never the list price; the price for the same customer, product, quantity and date equals the staff price; a line with no price shows an error and never falls back to the list price. `dotnet test src/Northwind.OrderDesk.sln` passes with the pricing assertions not weakened (ES-18, CS-20). | `STORY-238/AC1` to `STORY-238/AC3`, `STORY-232/AC2` | `STORY-238` |
| EX-7 | **Language (`BR-11`).** Every pilot screen appears in French and in English; a text without a translation is listed and fixed before approval; Dutch is not offered in this release. | `STORY-237/AC1` to `STORY-237/AC3` | `STORY-237` |
| EX-8 | **Customer sign-in (`NFR-04`).** Customers are authenticated by an externally managed identity and the application stores no password for them; local builds use a test identity; sign-in does not depend on one provider (A-10); an unknown user is refused. | `STORY-240/AC1` to `STORY-240/AC4` | `STORY-240` |
| EX-9 | **EU residency (`NFR-03`).** Every service the portal uses (hosting, identity service, outbound mail) is listed with its region and each is in the EU; a service that holds data outside the EU is not accepted; the cost question is marked **OPEN:** (O-24). | `STORY-239/AC1` to `STORY-239/AC3` | `STORY-239` |
| EX-10 | **Audit (`NFR-08`).** The audit record of every order change shows who, what, when and channel; known gaps in today's records are listed for the product owner and not changed silently (A-51, T-13). | `STORY-241/AC1` to `STORY-241/AC3` | `STORY-241` |
| EX-11 | **Accessibility (`NFR-07`).** Findings against WCAG 2.2 level AA (automated checks plus a manual keyboard and screen-reader review) are recorded per screen; each failure is fixed or listed with a reason; the result does not claim conformance, because a conformance statement needs a qualified reviewer (A-54). | `STORY-242/AC1` to `STORY-242/AC3` | `STORY-242` |
| EX-12 | **Performance (`NFR-02`).** Measured on the server, the 95th percentile is under 2 seconds for 95 % of requests on the order list and order detail pages, using about 60 concurrent staff users at peak (CS-03), the agreed pilot customer figure (**OPEN:** O-08, A-17) and today's data volume (about 14,000 order lines a week, CS-05). At 2 seconds or more `NFR-02` is recorded as not met and the release is not approved on this criterion. | `STORY-243/AC1` to `STORY-243/AC3` | `STORY-243` |
| EX-13 | **Whole-solution tests.** `dotnet test src/Northwind.OrderDesk.sln` passes on Windows, macOS and Linux and no earlier assertion is weakened (ES-18). | ES-18; `dotnet-r1` `EN-02/AC1` | all items |
| EX-14 | **MVE-02 recorded.** The MVE-02 decision (Go, Adjust or Stop) is recorded and the scope of this release matches it (section 2.1). | experiments.md section 3.2.5 | gated items |
| EX-15 | **Tags.** Every item in section 3 carries `track-dotnet` and `dotnet-r2`, and no item of this release appears in another release file. | Mechanical check of the backlog item register for tags and release membership | all 21 items |

Not part of the exit: a live pilot with real customers, any deployment, invoices, user administration, e-mail, Dutch, and the Order Desk API implementation.

## 10. Assumptions and OPEN items relevant to this release

Ids and wording come from the backlog registers (backlog section 7, the register of record); owners are the confirming owners there. `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

| Id | Kind | Text (short) | Owner |
|---|---|---|---|
| A-01 | **ASSUMPTION:** | Build starts December 2026 after approval; windows are targets. | Marc Dubois |
| A-02 | **ASSUMPTION:** | .NET owns Order Desk code changes; Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. | Ahmed Benali |
| A-03 | **ASSUMPTION:** | Received, Confirmed and Cancelled are current as of Order Desk; Picking and Shipped are current as of the last nightly run and shown with an "as of" time; Delivered is set by staff. | Lena Varga |
| A-05 | **ASSUMPTION:** | `NFR-02` is measured on the server at the 95th percentile with a load model from CS-03 and an agreed customer figure. | Ahmed Benali |
| A-06 | **ASSUMPTION:** | Prioritisation is MoSCoW from the business case, then date and dependency risk; NFRs are Must. | Lena Varga |
| A-10 | **ASSUMPTION:** | Customer sign-in is provider-neutral; a test identity is used in experiments and local builds. | Ahmed Benali |
| A-11 | **ASSUMPTION:** | Portal release 1 covers French and English; Dutch follows. | Sofie Peeters, Lena Varga |
| A-16 | **ASSUMPTION:** | 24 months is a display window over the complete history in the database. | Ahmed Benali |
| A-17 | **ASSUMPTION:** | Pilot customer concurrency is small (20 customers); no customer load figure exists. | Ahmed Benali |
| A-19 | **ASSUMPTION:** | In `dotnet-r2`, staff onboard customer users until `BR-08` is built. | Lena Varga |
| A-27 | **ASSUMPTION:** | The StockPilot CSV contract and file pick-up stay as they are. | Ahmed Benali |
| A-31 | **ASSUMPTION:** | Backup and long-term retention can cover the 7-year audit retention. | Ahmed Benali |
| A-35 | **ASSUMPTION:** | MVE success thresholds are starting points; Lena Varga sets the final numbers. | Lena Varga |
| A-37 | **ASSUMPTION:** | The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. | Ahmed Benali |
| A-38 | **ASSUMPTION:** | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | **ASSUMPTION:** | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-42 | **ASSUMPTION:** | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-43 | **ASSUMPTION:** | Cross-cutting NFRs are split per track and, where design and proof differ, per release. | Ahmed Benali |
| A-45 | **ASSUMPTION:** | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | **ASSUMPTION:** | Backlog rank: enablers before the features that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-51 | **ASSUMPTION:** | Facts read from the Order Desk code (no company check on an order, no role check on a status change, the channel is taken from the form, the channel is recorded only on creation) are not in `knowledge-docs`. | Ahmed Benali |
| A-54 | **ASSUMPTION:** | The measurement rules for `NFR-03` to `NFR-09` are the author's proposals. | Ahmed Benali, Lena Varga |
| A-D2-01 | **ASSUMPTION:** (release-local; this file is its register) | The team has a local SQL Server and the sample data to run the exit tests, including a data set with orders for at least two customers. | Ahmed Benali |
| A-D2-02 | **ASSUMPTION:** (release-local; this file is its register) | Approval of this release covers code, tests and review evidence produced locally. Choosing the 20 pilot customers, hosting the pilot and running it with real customers follow approval and are not claimed here. The backlog does not say who chooses the 20 customers; the proposal is Lena Varga with Sofie Peeters, as for MVE-02 contacts. | Lena Varga |
| O-01 | **OPEN:** | Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? | Ahmed Benali |
| O-04 | **OPEN:** | What status freshness is acceptable, given the nightly batch? | Lena Varga |
| O-06 | **OPEN:** | Which backlog tool and which ES-28 prefix? Item types and fields in the tool are not validated. | Lena Varga |
| O-07 | **OPEN:** | Who is the BA-03 team, what are their skills, and what is the intended date (or is BA-03 unplanned)? | Lena Varga, Marc Dubois |
| O-08 | **OPEN:** | Order-to-invoice mapping, order retention, customer concurrency, warehouse per order line. | Ahmed Benali |
| O-09 | **OPEN:** | Named release approver for the .NET track. | Marc Dubois |
| O-10 | **OPEN:** | Which identity provider do customer users use (OQ-01)? | Ahmed Benali |
| O-11 | **OPEN:** | Must Dutch be in the first release (OQ-02)? | Sofie Peeters, Lena Varga |
| O-12 | **OPEN:** | Do customer administrators exist for every customer or only for large ones (OQ-03)? | Lena Varga |
| O-16 | **OPEN:** | How an order gets Delivered; can StockPilot's pick-up run more than nightly without changing StockPilot? | Ahmed Benali, Pieter Janssens |
| O-17 | **OPEN:** | What sends order confirmations today? | Ahmed Benali |
| O-18 | **OPEN:** | Where do the customer e-mail address and language preference live? | Lena Varga |
| O-21 | **OPEN:** | Approval and funding to build. | Marc Dubois |
| O-23 | **OPEN:** | Which database does the Q2 2027 portal pilot read (T-08)? | Ahmed Benali |
| O-24 | **OPEN:** | What does the customer identity service cost, and does it count toward C-04? | Ahmed Benali |
| O-25 | **OPEN:** | Confirm release counts, windows and placement changes. | Lena Varga, Marc Dubois |
| O-26 | **OPEN:** | Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. | Lena Varga |
| O-28 | **OPEN:** | What happens to a line of a copied order whose product is no longer available (`STORY-234`)? | Lena Varga |
| X-10 | **OPEN:** | Outbound mail replaces the on-premises relay (both tracks; the shipping e-mail `STORY-262` is in `dotnet-r3`, not in this release). | Ahmed Benali |
| O-D2-01 | **OPEN:** (release-local; this file is its register) | The `dotnet-r2` window (1 Mar to 30 Apr 2027) overlaps the `azure-r2` window (1 Feb to 31 Mar 2027) by 31 days. The dependency is the database the pilot reads after `azure-r2` is approved (A-37, O-23), not a start order. `dotnet-r2` builds and tests locally under X-01 and does not wait. Confirm this reading. | Lena Varga, Ahmed Benali |
| O-D2-02 | **OPEN:** (release-local; this file is its register) | The canonical theme says "(Must items)" but this release contains one Should item, `STORY-237` (French and English), because `BR-11` is split by language (C3). Confirm that the theme wording may stay with the explanation in section 2, or reword the theme in C1 and every document at once. This file keeps the canonical theme and does not move the item. | Lena Varga |
| T-01 | Tension | `BR-04` says "always up to date" but Picking and Shipped change once a night (handled by A-03). | Lena Varga |
| T-08 | Tension | The Q2 2027 portal pilot and C-05 versus the database migration (A-37, O-23). | Ahmed Benali |
| T-13 | Tension | `NFR-08` asks for who, what, when and channel but today's audit rows may not record all. | Ahmed Benali |
| T-15 | Tension | `NFR-03` and `NFR-04` apply "wherever relevant" but BA-02 does not list `NFR-03` and BA-01 does not list `NFR-04` (split per track, A-43). | Ahmed Benali |

## 11. Approval and tagging procedure

Nothing below has happened. The Git tag does not exist, and no commit was made for this release (A-39).

1. **Review.** The approver reads this file, the 21 items in [backlog.md](../backlog.md), the exit criteria in section 9 and the recorded MVE-02 decision. Approver: **OPEN:** O-09 (owner Marc Dubois).
2. **Approve.** Only a human approver may approve. The approver's name and the approval date are written in the block below. This file changes from `Proposed` to `Approved` only at that point.
3. **Commit.** After approval, and only then, a human-initiated, gated step commits the approved release files together with the items they list.
4. **Tag.** After the commit exists, a human-initiated, gated step creates the Git tag `product/dotnet-r2` on that commit (ES-31). Pushing the tag is a separate decision.
5. **Check.** `git tag -l 'product/dotnet-r2'` then lists the tag. Until step 4, the same command returns nothing.

| Approval block | |
|---|---|
| Approver | **OPEN:** O-09 |
| Approval decision | (blank) |
| Approval date | (blank) |
| Planned Git tag | `product/dotnet-r2` — **to be created after approval; not created** |
| Commit holding the approved release | (blank; not committed) |

## 12. Publication note (ES-39)

When the backlog is published to a tool, the track and release tags travel with every item of this release so the release stays identifiable. Nothing is published, no tool was contacted, and **OPEN:** O-06 (owner Lena Varga) says no tool or ES-28 prefix is chosen, so item types and fields are not validated (`needs_review`).

| Tool | Track tag | Release tag | Grouping |
|---|---|---|---|
| Azure DevOps | work-item tag `track-dotnet` | work-item tag `dotnet-r2` | tags only |
| GitHub | issue label `track-dotnet` | issue label `dotnet-r2` | milestone `dotnet-r2` |
| Jira | label `track-dotnet` | label `dotnet-r2` | fix version `dotnet-r2` |

Titles, descriptions and source ids follow ES-28 and ES-29 in every tool (`nw-workshop` tag and the participant prefix agreed with the facilitator).

## 13. Sources

* [backlog.md](../backlog.md) sections 1.1, 2.2, 3, 4.2, 5 and 7: items, ids, tags, priorities, ranks, acceptance criteria, registers.
* [traceability.md](../traceability.md): split identifiers and enabler coverage.
* [product-requirements.md](../product-requirements.md): release plan and `X-nn` rows.
* [experiments.md](../experiments.md) section 3.2: MVE-02 gate, thresholds and decisions (not run).
* `knowledge-docs/engineering-standards.md`: ES-18, ES-19, ES-20, ES-27, ES-28, ES-29, ES-30, ES-31, ES-39.
* `knowledge-docs/current-state.md`: CS-03, CS-04, CS-05, CS-10, CS-20, CS-28.
