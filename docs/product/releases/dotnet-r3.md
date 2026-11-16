---
release_id: "dotnet-r3"
title: "Release dotnet-r3: Complete portal and API contract (general availability)"
track: "dotnet"
release: "dotnet-r3"
track_tag: "track-dotnet"
release_tag: "dotnet-r3"
planned_git_tag: "product/dotnet-r3"
git_tag_created: false
status: "proposed"
document_status: "Draft for review"
target_window: "1 May to 30 Sep 2027"
approver: "OPEN: O-09"
approval_date: ""
experiment_gate: "MVE-02 (instrumentation only; not run, result pending)"
source_backlog_id: "BACKLOG-NW-001"
source_backlog_path: "docs/product/backlog.md"
source_prd_id: "PRD-NW-001"
source_brd_id: "BRD-NW-001"
owners: ["Lena Varga"]
created_date: "2026-11-15"
---

# Release dotnet-r3: Complete portal and API contract (general availability)

> Status: **Draft for review** | Release status: **Proposed, awaiting product-owner approval** | Track: `track-dotnet` | Release tag: `dotnet-r3`
>
> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> This is a document. Nothing was built, deployed or published to a tracker to write it, and **no Git tag or commit exists for this release** (A-39, ES-27).

## 1. Document control

| Field | Value |
|---|---|
| Track | .NET, business area BA-02 (Ordering and customer self-service) |
| Track tag (ES-30) | `track-dotnet` |
| Release tag (ES-31) | `dotnet-r3` |
| Planned Git tag | `product/dotnet-r3` — **to be created on approval; not created** |
| Release status | Proposed, awaiting product-owner approval |
| Document status | Draft for review |
| Approver | **OPEN:** O-09 — the named approver for each track is not decided. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner to confirm: Marc Dubois. |
| Approval date | (blank until a human approves) |
| Release owner (document) | Lena Varga |
| Experiment gate | MVE-02 for the instrumentation story `STORY-264` only — **not run; result pending** |
| Source documents | [backlog.md](../backlog.md) (item list is authoritative), [traceability.md](../traceability.md), [product-requirements.md](../product-requirements.md), [business-requirements.md](../business-requirements.md), [experiments.md](../experiments.md) |
| Rule | **A release never waits for another track** (ES-31). Needs from another track are **OPEN:** rows in section 6, each with a way to keep delivering. |

## 2. Objective, theme and target window

**Theme:** Complete portal and API contract (general availability, A-04).

**Objective.** Complete the customer portal after the pilot: invoice download, customer user administration, the shipping e-mail, Dutch, and the data needed to compare the portal success measures `SM-01` to `SM-04` with their baselines. Publish the read-only Order Desk API contract as a file so that another track can build against it. The contract is a **document only**; the Order Desk API **implementation is not in this release** (source: EPIC-203, BR-07, BR-08, BR-09, BR-11, SM-01 to SM-04, CS-27, ES-36, G-01).

**Target window:** 1 May to 30 Sep 2027. A target, not a commitment (A-01, A-42; **OPEN:** O-25, owners Lena Varga and Marc Dubois). "General availability" follows **ASSUMPTION:** A-04 ("portal launch" in `SM-01` to `SM-04` means general availability, not the 20-customer pilot); **OPEN:** O-05 asks Lena Varga to confirm.

**Main epic:** `EPIC-203` Complete the portal and publish the Order Desk API contract.

**Experiment gate.** MVE-02 gates only the instrumentation story `STORY-264` (and its feature `FEAT-213`). MVE-02 is **not run; its result is pending.** The decision effect on this release (source: experiments.md section 3.2.5):

| MVE-02 result | Effect on `dotnet-r3` |
|---|---|
| **Go** | `STORY-264` goes ahead as written once **OPEN:** O-26 names the data and the source. |
| **Adjust** | The `SM-01` and `SM-02` targets go back to Lena Varga (A-04, G-05); `STORY-264` is re-checked against the changed targets. |
| **Stop** (both R1 and R2 fail) | Item-level effect: `STORY-264` (instrumentation of `SM-01` to `SM-04`) is **not committed**, because the portal measures have nothing to measure until the reason for the failure is understood. The other items of this release carry no MVE-02 item gate in the backlog and are **not held back by it**. Lena Varga and Marc Dubois decide on the portal business case. **Wording difference.** **OPEN:** O-D3-02 (owner Lena Varga): `experiments.md` section 3.2.5 words the Stop decision more widely ("do not commit the customer-facing portal stories (`EPIC-202`, `EPIC-203`)"), while the backlog and PRD gate only `STORY-264` in `EPIC-203`. This file follows the backlog item gates and does not change either document. |

## 3. Items in this release

13 items: 1 epic, 4 features, 6 stories, 2 enablers. Every item carries the track tag `track-dotnet` **and** the release tag `dotnet-r3`, and appears in no other release (ES-31). Ids and titles are copied from the backlog item register (section 2.2). Rank is the order inside the .NET track (A-46).

| Id | Title | Type | Priority | Rank | Source ids | Track tag | Release tag | MVE gate |
|---|---|---|---|---|---|---|---|---|
| EPIC-203 | Complete the portal and publish the Order Desk API contract | epic | Should | — | BR-07, BR-08, BR-09, BR-11, SM-01 to SM-04, CS-27, ES-36, G-01 | `track-dotnet` | `dotnet-r3` | MVE-02 (instrumentation, `STORY-264`) |
| FEAT-211 | Invoice download | feature | Should | — | BR-07, CS-08, CS-11, CS-14, P-05 | `track-dotnet` | `dotnet-r3` | none |
| EN-07 | Abstract the invoice store | enabler | Should | 33 | CS-14, CS-11, A-15 | `track-dotnet` | `dotnet-r3` | none |
| STORY-260 | Download the PDF invoice of a delivered order | story | Should | 34 | BR-07, P-05, CS-08, CS-11 | `track-dotnet` | `dotnet-r3` | none |
| FEAT-212 | Customer user administration and shipping e-mail | feature | Should | — | BR-08, BR-09, OQ-03, CS-10, CS-12 | `track-dotnet` | `dotnet-r3` | none |
| STORY-261 | Invite and remove users of my own company | story | Should | 35 | BR-08, OQ-03 | `track-dotnet` | `dotnet-r3` | none |
| STORY-262 | Receive an e-mail when an order changes to Shipped | story | Could | 36 | BR-09, P-03, CS-10, CS-12 | `track-dotnet` | `dotnet-r3` | none |
| FEAT-213 | Dutch and success-measure data | feature | Should | — | BR-11, SM-01 to SM-04, OQ-02 | `track-dotnet` | `dotnet-r3` | MVE-02 (`STORY-264`) |
| STORY-263 | Use the portal in Dutch | story | Should | 37 | BR-11, OQ-02 | `track-dotnet` | `dotnet-r3` | none |
| STORY-264 | Record data to compare SM-01 to SM-04 with their baselines | story | Should | 38 | SM-01, SM-02, SM-03, SM-04; **ASSUMPTION:** A-52 | `track-dotnet` | `dotnet-r3` | MVE-02 (instrumentation) |
| FEAT-214 | Order Desk API contract | feature | Should | — | CS-27, ES-36, G-01 | `track-dotnet` | `dotnet-r3` | none |
| EN-14 | Publish the read-only Order Desk API contract (OpenAPI 2.0) | enabler | Should | 39 | CS-27, ES-36, G-01 | `track-dotnet` | `dotnet-r3` | none |
| STORY-265 | Let another track build against the published order contract | story | Should | 40 | CS-27, ES-36, G-01 | `track-dotnet` | `dotnet-r3` | none |

Item counts by type: epic 1, feature 4, story 6 (`STORY-260`, `STORY-261`, `STORY-262`, `STORY-263`, `STORY-264`, `STORY-265`), enabler 2 (`EN-07`, `EN-14`). Total 13. These match backlog section 3.

## 4. Business and quality requirements covered

The "covered" column is the canonical C1 text for `dotnet-r3`:

> BR-07, BR-08, BR-09, BR-11 (Dutch); SM-01 to SM-04 instrumentation

| Identifier | Priority | Part covered here | Covering story | Supporting items | Other parts of the same identifier |
|---|---|---|---|---|---|
| BR-07 | Should | Whole requirement (PDF invoice download) | `STORY-260` | `EN-07` | Azure invoice storage design: `azure-r2` (another track, **OPEN:** X-09) |
| BR-08 | Should | Whole requirement; scope per O-12 | `STORY-261` | none | none |
| BR-09 | Could | Whole requirement; freshness per A-03 | `STORY-262` | none | Azure outbound mail design: `azure-r2` (another track, supporting, not coverage; **OPEN:** X-10) |
| BR-11 (Dutch) | Should | Dutch | `STORY-263` | none | French and English: `dotnet-r2`, `STORY-237` |
| SM-01 to SM-04 (supplementary, not required by ES-06) | — | Instrumentation | `STORY-264` | none | The measures need a source and owner: **OPEN:** O-26 |

`EN-14` and `STORY-265` cover no `BR-` or `NFR-`. They protect the BA-03 need for an order contract (`X-20`, `X-21`; source: CS-27, ES-36, G-01) and are listed as enabler coverage in [traceability.md](../traceability.md) (G-10).

## 5. What this release leaves out, and where it moves

| Left out | Where it goes | Why |
|---|---|---|
| **Order Desk API implementation** (`EPIC-204`, `FEAT-215`, `STORY-280`: a read-only service for orders and order lines) | **Unplanned.** It carries only `track-dotnet` and no release tag. It becomes a candidate for `dotnet-r3` when **OPEN:** O-01 (owner Ahmed Benali) is answered; that would be a revision of the canonical release table through the coordinator, not a change made in this file. | The API has no owner (G-01, O-01). A conditional item cannot carry a release tag (ES-31). `STORY-265/AC3` says the contract is published and the implementation is `EPIC-204`, unplanned. |
| All BA-03 items: `EPIC-301` to `EPIC-304`, their features and stories, and enablers `EP-01` to `EP-06` (30 items) | Unplanned, `track-power-platform`; **no release exists** | No team, API, governed environments or licence decision (G-08, O-02, O-07). The Q1 2027 claims pilot cannot be committed (A-25). |
| Azure items (`EPIC-101` to `EPIC-104`) | `azure-r1` to `azure-r3` (another track) | Delivered by the Azure team (A-02). |
| Anything earlier in this track | `dotnet-r1` (parity, enablers) and `dotnet-r2` (pilot) | Already placed in those releases. |

Nothing is moved out of `dotnet-r3` by this file. Optimisation after the lease is an Azure matter and has no item here.

## 6. Dependencies on other tracks (all OPEN, none is a wait)

**A release never waits for another track** (ES-31, A-45). **`dotnet-r3` proceeds without waiting for the Azure track, the Power Platform track, StockPilot or any other owner.** Every row below is **OPEN:** until its owner confirms it, and each row says how the .NET team keeps delivering meanwhile (an interface with a local provider, a local mail catcher, a published contract file instead of a running service). The table lists **every** `X-nn` that an item of this release cites in the backlog or in its acceptance criteria (7 ids: X-06, X-09, X-10, X-20, X-21, X-23, X-25). Rows from C11 and the `EPIC-203` entry are X-06, X-09, X-10, X-20 and X-21 (X-20 and X-21 as outbound); X-23 and X-25 are cited only in the acceptance criteria of `EN-14`.

"Role" shows the side of `dotnet-r3`: **consumer-side** means this release needs something from another track; **supplier-side** means another track needs something from this release (the row is then carried in the release file or backlog items of the needing track, here BA-03 with no release file, and is listed here for completeness, never as a wait).

| Id | **OPEN:** dependency | Role of `dotnet-r3` | Direction | Owner to confirm | How `dotnet-r3` proceeds without waiting | Items |
|---|---|---|---|---|---|---|
| X-06 | Status freshness is bounded by the exchange cadence | Consumer-side | .NET needs Azure and StockPilot | Lena Varga | The shipping e-mail arrives after the nightly update and states the "as of" time; it is never promised at the moment of physical shipment (`STORY-262/AC2`, A-03). | `STORY-262` |
| X-09 | Invoice files move from a network path to Azure storage | Consumer-side and supplier-side | Both | Julien Moreau, Ahmed Benali | `EN-07` puts the invoice store behind an interface with a local-folder provider, so an invoice is read without a UNC path (`EN-07/AC1`); a missing file gives a "not found" result (`EN-07/AC3`). Where invoices live after the lease is **OPEN:** O-15. | `EN-07`, `STORY-260` |
| X-10 | Outbound mail replaces the on-premises relay | Consumer-side and supplier-side | Both | Ahmed Benali | A mail abstraction and a local mail catcher meanwhile; a mail failure never changes the order status and is logged (`STORY-262/AC3`). The Azure mail design (`EA-12`) is another track's work and is never waited for. | `STORY-261` (if the invitation is sent by e-mail), `STORY-262` |
| X-20 (outbound) | An Order Desk API (read orders and lines) for the BA-03 custom connector | **Supplier-side** | Power Platform needs .NET | Ahmed Benali | `dotnet-r3` publishes the **contract** (`EN-14`, `STORY-265`) as a file. BA-03 designs against a stub meanwhile. The implementation is unplanned (O-01). | `EN-14`, `STORY-265` |
| X-21 (outbound) | An order data contract for claims: order number, lines, quantities, prices, customer, warehouse | **Supplier-side** | Power Platform needs .NET | Lena Varga, Pieter Janssens | The contract carries each field; the warehouse field is marked as not available while its source is unknown (A-18, X-25) and no value is invented (`EN-14/AC3`). | `EN-14` |
| X-23 | Connector sign-in (Entra app registration, OAuth) | Neither a need of `dotnet-r3` nor a wait: a **placeholder** only | Power Platform needs Azure or IT | Ahmed Benali | The contract carries a placeholder security definition and no implementation (`EN-14/AC4`); the real sign-in is for the implementation (`EPIC-204`, unplanned). | `EN-14` |
| X-25 | Warehouse for each order line, for `BR-17` | **Supplier-side** (field in the contract) | Power Platform needs .NET and StockPilot data | Pieter Janssens | `EN-14/AC3` marks the warehouse field as not available while its source is unknown (A-18); no value is invented. | `EN-14` |

Other related questions, **OPEN:** O-01 (Order Desk API owner; Ahmed Benali), O-05 (pilot or general availability; Lena Varga), O-11 (Dutch; Sofie Peeters, Lena Varga), O-12 (customer administrators; Lena Varga), O-15 (post-lease location of finance system, `NWFS01` shares, domain controllers, SFTP route; Ahmed Benali, Julien Moreau), O-17 (what sends order confirmations today; Ahmed Benali), O-18 (customer e-mail and language; Lena Varga), O-26 (measurement source and owner for `SM-01` to `SM-04`; Lena Varga).

## 7. Entry conditions

| Id | Condition | Evidence | Status |
|---|---|---|---|
| EN-C1 | Approval and funding to build is given. | **OPEN:** O-21, owner Marc Dubois. | Not met; the window is a target (A-01). |
| EN-C2 | The `dotnet-r2` items that `dotnet-r3` items depend on exist: `EN-11` (for `STORY-260`, `STORY-261`, `STORY-262`) and `STORY-237` (for `STORY-263`). This is inside the .NET track, not a wait on another track. | `dotnet-r2` exit criteria | Pending |
| EN-C3 | Pilot feedback is available to the product owner. The backlog places Should and Could items after pilot feedback (C2). | Product owner | **ASSUMPTION:** A-D3-01. Owner Lena Varga. |
| EN-C4 | For `STORY-264`: **OPEN:** O-26 has named the data and the source, and the MVE-02 decision is recorded. | `STORY-264/AC3`, experiments.md section 3.2.5 | Pending; MVE-02 is not run. |
| EN-C5 | The product owner has reviewed this file and the items in section 3. | Section 10 | Pending |

## 8. Exit and acceptance criteria

The release is ready for approval only when **every** criterion is met. Each is tied to items in section 3; the Given / When / Then wording is in [backlog.md](../backlog.md) under the criterion id. "Done" means code, tests and documents pass on a developer machine or a build runner. No deployment is claimed (ES-27; **ASSUMPTION:** A-D3-02).

| Id | Exit criterion | Tested by | Items |
|---|---|---|---|
| EX-1 | **Invoices (`BR-07`).** A delivered order with an invoice offers a PDF download that delivers the file; an order that is not Delivered offers none; a request for another company's invoice is refused; a missing PDF shows "not available yet" and logs the miss. The invoice store reads from a local folder without a UNC path, builds the path as `{year}\{invoiceNumber}.pdf` with the year rule written down (A-15), and returns "not found" without an exception. | `STORY-260/AC1` to `STORY-260/AC4`, `EN-07/AC1` to `EN-07/AC3` | `STORY-260`, `EN-07` |
| EX-2 | **User administration (`BR-08`).** A customer administrator can invite and remove users of their own company; an invited colleague sees only that company's orders; a removed user can no longer sign in; a request for another company is refused; a user who is not an administrator sees no administration screen. | `STORY-261/AC1` to `STORY-261/AC4` | `STORY-261` |
| EX-3 | **Shipping e-mail (`BR-09`).** An e-mail is sent when an order changes to Shipped; for a status set by the nightly update it arrives after that run and states the "as of" time (A-03); a mail failure leaves the status unchanged and is logged; with no e-mail address no e-mail is sent and the gap is logged (O-18). | `STORY-262/AC1` to `STORY-262/AC4` | `STORY-262` |
| EX-4 | **Dutch (`BR-11`).** Every portal screen appears in Dutch; French and English are unchanged; any text without a Dutch translation is listed and fixed before approval. | `STORY-263/AC1` to `STORY-263/AC3` | `STORY-263` |
| EX-5 | **Success-measure data (`SM-01` to `SM-04`).** The portal records or exposes the data agreed under O-26 for `SM-01`, `SM-03` and `SM-04` for a chosen period; the story states that `SM-02` calls handled by staff are counted outside the product. If O-26 has not named the data and the source, `STORY-264` is not started and stays Draft (`STORY-264/AC3`); this is recorded as **OPEN:** O-D3-01 for the product owner's decision at approval. | `STORY-264/AC1` to `STORY-264/AC3` | `STORY-264` |
| EX-6 | **Published contract (`EN-14`, `STORY-265`).** The contract file is a valid OpenAPI 2.0 document, **validated locally** (ES-36); every operation only reads and none creates, changes or deletes an order; it carries order number, lines, quantities, prices, customer and warehouse, with the warehouse field marked not available while its source is unknown (A-18, X-25) and no value invented; it contains no implementation and carries a placeholder security definition (X-23); it describes how to read one order and its lines by order number. | `EN-14/AC1` to `EN-14/AC4`, `STORY-265/AC1`, `STORY-265/AC2` | `EN-14`, `STORY-265` |
| EX-7 | **Statement about the implementation.** This release file states that the contract is published and that the implementation is `EPIC-204`, unplanned (O-01). Section 5 of this file is that statement. | `STORY-265/AC3` | `STORY-265` |
| EX-8 | **Whole-solution tests.** `dotnet test src/Northwind.OrderDesk.sln` passes on Windows, macOS and Linux and no earlier assertion is weakened, including the pricing assertions (ES-18, CS-20). | ES-18; `dotnet-r1` `EN-02/AC1`, `STORY-202/AC2` | all items |
| EX-9 | **Tags.** Every item in section 3 carries `track-dotnet` and `dotnet-r3`; no item of this release appears in another release file; `EPIC-204`, `FEAT-215` and `STORY-280` carry no release tag. | Mechanical check of the backlog item register for tags and release membership | all 13 items |

Not part of the exit: the Order Desk API implementation, any BA-03 item, any deployment, and the result of MVE-02 (not run, pending).

## 9. Assumptions and OPEN items relevant to this release

Ids and wording come from the backlog registers (backlog section 7, the register of record); owners are the confirming owners there. `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

| Id | Kind | Text (short) | Owner |
|---|---|---|---|
| A-01 | **ASSUMPTION:** | Build starts December 2026 after approval; windows are targets. | Marc Dubois |
| A-02 | **ASSUMPTION:** | .NET owns Order Desk code changes; Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. | Ahmed Benali |
| A-03 | **ASSUMPTION:** | Freshness rule for `BR-04` and `BR-09`: Picking and Shipped are current as of the last nightly run and shown with an "as of" time. | Lena Varga |
| A-04 | **ASSUMPTION:** | "Portal launch" in `SM-01` to `SM-04` means general availability, not the 20-customer pilot. | Lena Varga |
| A-11 | **ASSUMPTION:** | Portal release 1 covers French and English; Dutch follows. | Sofie Peeters, Lena Varga |
| A-12 | **ASSUMPTION:** | A customer administrator role exists; who gets it is **OPEN:**. | Lena Varga |
| A-15 | **ASSUMPTION:** | The invoice number is filled by the finance process, and the invoice folder year equals the invoice year. | Julien Moreau |
| A-18 | **ASSUMPTION:** | The warehouse for each claim line can be derived from StockPilot or product data; it is not on order lines. | Pieter Janssens |
| A-19 | **ASSUMPTION:** | Staff onboard customer users until `BR-08` is built. | Lena Varga |
| A-25 | **ASSUMPTION:** | The Q1 2027 claims pilot cannot be committed while BA-03 has no team. | Lena Varga, Marc Dubois |
| A-29 | **ASSUMPTION:** | The unauthenticated on-premises e-mail relay is not usable after the lease; a replacement mail path is needed. | Ahmed Benali |
| A-35 | **ASSUMPTION:** | MVE thresholds are starting points; Lena Varga sets the final numbers. | Lena Varga |
| A-38 | **ASSUMPTION:** | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-39 | **ASSUMPTION:** | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-42 | **ASSUMPTION:** | A target window is the period by which release content is complete and ready to approve. Targets, not commitments. | Marc Dubois |
| A-45 | **ASSUMPTION:** | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-46 | **ASSUMPTION:** | Backlog rank: enablers before the features that need them, then Must, Should, Could, then date risk. | Lena Varga |
| A-52 | **ASSUMPTION:** | `FR-234` (instrumentation for `SM-01` to `SM-04`) is Should, because the business case gives the measures no priority and names no source. | Lena Varga |
| A-D3-01 | **ASSUMPTION:** (release-local; this file is its register) | Pilot feedback from `dotnet-r2` reaches the product owner before `dotnet-r3` items are committed. The backlog places the items after pilot feedback but does not describe how feedback is collected. | Lena Varga |
| A-D3-02 | **ASSUMPTION:** (release-local; this file is its register) | Approval of this release covers code, tests and documents produced locally. General availability itself, hosting and rollout follow approval and are not claimed here. | Lena Varga |
| O-D3-01 | **OPEN:** (release-local; this file is its register) | `STORY-264` must stay Draft until O-26 names the data and the source. If O-26 is still open at approval, does the product owner approve `dotnet-r3` without it, recording the story as not started? This file does not move the item. | Lena Varga |
| O-D3-02 | **OPEN:** (release-local; this file is its register) | **Wording difference between documents.** `experiments.md` section 3.2.5 says a MVE-02 Stop holds back the customer-facing portal stories of `EPIC-202` and `EPIC-203`. The backlog and PRD gate only `STORY-264` in `EPIC-203`. Which reading is right for the other items of this release (`EN-07`, `STORY-260` to `STORY-263`, `EN-14`, `STORY-265`)? This file follows the item-level gates (only `STORY-264`) until the owner decides, and does not edit either document. | Lena Varga |
| O-01 | **OPEN:** | Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? | Ahmed Benali |
| O-02 | **OPEN:** | Does BA-03 need a premium licence, a data gateway or a custom connector inside C-07 and C-08? Is Dataverse used? | Ahmed Benali |
| O-05 | **OPEN:** | Does "portal launch" mean the pilot or general availability? | Lena Varga |
| O-06 | **OPEN:** | Which backlog tool and which ES-28 prefix; item types and fields in a tool are not validated. | Lena Varga |
| O-07 | **OPEN:** | Who is the BA-03 team, what are their skills, and what is the intended date (or is BA-03 unplanned)? | Lena Varga, Marc Dubois |
| O-09 | **OPEN:** | Named release approver for the .NET track. | Marc Dubois |
| O-11 | **OPEN:** | Must Dutch be in the first release (OQ-02)? | Sofie Peeters, Lena Varga |
| O-12 | **OPEN:** | Do customer administrators exist for every customer or only for large ones (OQ-03)? | Lena Varga |
| O-15 | **OPEN:** | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-17 | **OPEN:** | What sends order confirmations today? | Ahmed Benali |
| O-18 | **OPEN:** | Where do the customer e-mail address and language preference live? | Lena Varga |
| O-21 | **OPEN:** | Approval and funding to build. | Marc Dubois |
| O-25 | **OPEN:** | Confirm release counts, windows and placement changes. | Lena Varga, Marc Dubois |
| O-26 | **OPEN:** | Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. | Lena Varga |

## 10. Approval and tagging procedure

Nothing below has happened. The Git tag does not exist, and no commit was made for this release (A-39).

1. **Review.** The approver reads this file, the 13 items in [backlog.md](../backlog.md), the exit criteria in section 8 and the recorded MVE-02 decision for `STORY-264`. Approver: **OPEN:** O-09 (owner Marc Dubois).
2. **Approve.** Only a human approver may approve. The approver's name and the approval date are written in the block below. This file changes from `Proposed` to `Approved` only at that point.
3. **Commit.** After approval, and only then, a human-initiated, gated step commits the approved release files together with the items they list.
4. **Tag.** After the commit exists, a human-initiated, gated step creates the Git tag `product/dotnet-r3` on that commit (ES-31). Pushing the tag is a separate decision.
5. **Check.** `git tag -l 'product/dotnet-r3'` then lists the tag. Until step 4, the same command returns nothing.

| Approval block | |
|---|---|
| Approver | **OPEN:** O-09 |
| Approval decision | (blank) |
| Approval date | (blank) |
| Planned Git tag | `product/dotnet-r3` — **to be created after approval; not created** |
| Commit holding the approved release | (blank; not committed) |

## 11. Publication note (ES-39)

When the backlog is published to a tool, the track and release tags travel with every item of this release so the release stays identifiable. Nothing is published, no tool was contacted, and **OPEN:** O-06 (owner Lena Varga) says no tool or ES-28 prefix is chosen, so item types and fields are not validated (`needs_review`).

| Tool | Track tag | Release tag | Grouping |
|---|---|---|---|
| Azure DevOps | work-item tag `track-dotnet` | work-item tag `dotnet-r3` | tags only |
| GitHub | issue label `track-dotnet` | issue label `dotnet-r3` | milestone `dotnet-r3` |
| Jira | label `track-dotnet` | label `dotnet-r3` | fix version `dotnet-r3` |

Titles, descriptions and source ids follow ES-28 and ES-29 in every tool (`nw-workshop` tag and the participant prefix agreed with the facilitator).

## 12. Sources

* [backlog.md](../backlog.md) sections 1.1, 2.2, 3, 4.2, 5 and 7: items, ids, tags, priorities, ranks, acceptance criteria, registers.
* [traceability.md](../traceability.md): split identifiers and enabler coverage.
* [product-requirements.md](../product-requirements.md): release plan and `X-nn` rows.
* [experiments.md](../experiments.md) section 3.2: MVE-02 gate and decisions (not run).
* `knowledge-docs/engineering-standards.md`: ES-18, ES-27, ES-28, ES-29, ES-30, ES-31, ES-36, ES-39.
* `knowledge-docs/current-state.md`: CS-08, CS-10, CS-11, CS-12, CS-14, CS-20, CS-27.
