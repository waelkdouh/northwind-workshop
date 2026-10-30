# Release dotnet-r2: Portal pilot, Must items (.NET track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D7 (ES-31) |
| Track | .NET, business area BA-02 Ordering and customer self-service |
| Release name | Portal pilot: Must items |
| Release tag | `dotnet-r2` |
| Track tag | `track-dotnet` |
| Git tag | `product/dotnet-r2`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r2 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | Pilot start in April 2027, with 20 customers. **ASSUMPTION:** A-07 (a target, not a commitment). "Portal launch" and where the pilot runs are OPEN-05. |
| Date of this file | 2026-10-30 |
| Items in this release | 41: 4 epics, 12 features, 6 enablers, 19 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.5), `docs/product/business-requirements.md`, `docs/product/experiments.md` (`MVE-BA02`), `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-13 to ES-20, ES-25, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is built, deployed, published, committed or tagged from it (ES-27). |

## 1. Words used

* **BA-02** is the business area "Ordering and customer self-service". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **Order Desk** is the internal web application staff use to enter and manage orders. **Portal** is the new customer web site. A **customer user** is a person at a customer company who signs in to the portal. A **company** is one customer account in Order Desk. **Staff** are Order Desk employees.
* **Tenant isolation** (customer data separation) means that a customer user can only ever see the data of their own company (BR-01, C-05).
* **Status** is one of six: Received, Confirmed, Picking, Shipped, Delivered, Cancelled (BR-04). The **02:00 batch** is the nightly job that updates Picking and Shipped from the warehouse system StockPilot (CS-10).
* **Channel** is how an order was placed: Phone, E-mail, Order form or Portal (A-22).
* **Microsoft Entra ID** is Microsoft's sign-in service. **Entra External ID** is its option for customers outside the company. **ADR** (decision record) is a short written decision with its options and reasons.
* **WCAG 2.2 level AA** is the web accessibility standard the portal must meet (NFR-07).
* **Audit** is the record of who changed an order, what changed, when, and through which channel (NFR-08).
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

20 pilot customers use the portal for all Must items. They sign in, see only their own company's orders for the last 24 months, see the order details with their own negotiated prices, see the status of each order, copy a previous order into a new one, and submit it so that it appears in Order Desk as Received without re-keying. Staff can tell which orders came from the portal, and every change to an order is recorded. The portal meets WCAG 2.2 level AA from the start and keeps customer data in the European Union (source: BR-01 to BR-06, BR-10, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08).

This is the Must outcome of the .NET track. It is built on the modernised Order Desk from `dotnet-r1` (inside the .NET track, section 7.1). One Should item is also in this release: the language scaffold `EN-DN-12`, because it is cheaper to build before more screens exist (section 11, difference 1).

## 3. Items planned in this release

The list below is every item that carries the tags `track-dotnet` and `dotnet-r2`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `dotnet-r2`: 41 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-DN-02` | Epic | - | Secure access and tenant isolation | Must | `track-dotnet`, `dotnet-r2` | BR-01, NFR-03, NFR-04, C-05, OQ-01 |
| `EP-DN-03` | Epic | - | See my orders | Must | `track-dotnet`, `dotnet-r2` | BR-02, BR-03, BR-04, BR-12, NFR-02 |
| `EP-DN-04` | Epic | - | Reorder and hand-off | Must | `track-dotnet`, `dotnet-r2` | BR-05, BR-06, BR-10, BR-12, NFR-08, C-05 |
| `EP-DN-05` | Epic | - | Portal quality | Must | `track-dotnet`, `dotnet-r2` | NFR-07, BR-11 |
| `FT-DN-05` | Feature | `EP-DN-02` | Portal architecture decision | Must | `track-dotnet`, `dotnet-r2` | OQ-01, NFR-04, ES-13 |
| `FT-DN-06` | Feature | `EP-DN-02` | Customer data separation | Must | `track-dotnet`, `dotnet-r2` | BR-01, C-05 |
| `FT-DN-07` | Feature | `EP-DN-02` | Customer and staff sign-in | Must | `track-dotnet`, `dotnet-r2` | BR-01, NFR-04, CS-04, OQ-01 |
| `FT-DN-08` | Feature | `EP-DN-02` | Portal data stays in the EU | Must | `track-dotnet`, `dotnet-r2` | NFR-03, ES-20 |
| `FT-DN-09` | Feature | `EP-DN-03` | See my orders | Must | `track-dotnet`, `dotnet-r2` | BR-02, NFR-02, CS-05 |
| `FT-DN-10` | Feature | `EP-DN-03` | Order detail with my prices | Must | `track-dotnet`, `dotnet-r2` | BR-03, BR-12, NFR-02, CS-20, ES-18 |
| `FT-DN-11` | Feature | `EP-DN-03` | Order status as of the 02:00 batch | Must | `track-dotnet`, `dotnet-r2` | BR-04, CS-10, C-03 |
| `FT-DN-12` | Feature | `EP-DN-04` | Reorder by copying | Must | `track-dotnet`, `dotnet-r2` | BR-05, BR-12, P-04, CS-16 |
| `FT-DN-13` | Feature | `EP-DN-04` | Portal order reaches Order Desk | Must | `track-dotnet`, `dotnet-r2` | BR-06, BR-10, C-05 |
| `FT-DN-14` | Feature | `EP-DN-04` | Order change audit | Must | `track-dotnet`, `dotnet-r2` | NFR-08, CS-05 |
| `FT-DN-15` | Feature | `EP-DN-05` | Language foundation | Should | `track-dotnet`, `dotnet-r2` | BR-11 |
| `FT-DN-16` | Feature | `EP-DN-05` | Accessibility baseline | Must | `track-dotnet`, `dotnet-r2` | NFR-07, BR-03 |
| `EN-DN-11` | Enabler | `FT-DN-05` | Portal architecture and sign-in decision record | Must | `track-dotnet`, `dotnet-r2` | OQ-01, NFR-04, NFR-03, ES-13, ES-08, C-04, C-05 |
| `EN-DN-10` | Enabler | `FT-DN-06` | Customer data separation (tenant isolation) | Must | `track-dotnet`, `dotnet-r2` | BR-01, C-05, CS-04 |
| `EN-DN-08` | Enabler | `FT-DN-07` | Staff sign-in with Microsoft Entra ID | Must | `track-dotnet`, `dotnet-r2` | NFR-04, CS-04, CS-09 |
| `US-DN-004` | Story | `FT-DN-07` | Customer user signs in | Must | `track-dotnet`, `dotnet-r2` | BR-01, NFR-04, OQ-01, CS-04 |
| `US-DN-003` | Story | `FT-DN-06` | Customer user sees only their own company | Must | `track-dotnet`, `dotnet-r2` | BR-01, C-05 |
| `US-DN-005` | Story | `FT-DN-08` | Portal sign-in, mail and monitoring keep data in the EU | Must | `track-dotnet`, `dotnet-r2` | NFR-03, ES-20 |
| `EN-DN-14` | Enabler | `FT-DN-16` | Accessibility baseline (WCAG 2.2 AA) | Must | `track-dotnet`, `dotnet-r2` | NFR-07 |
| `US-DN-006` | Story | `FT-DN-09` | See my company's orders from the last 24 months | Must | `track-dotnet`, `dotnet-r2` | BR-02, CS-05, P-03 |
| `US-DN-007` | Story | `FT-DN-09` | The order list responds in under 2 seconds | Must | `track-dotnet`, `dotnet-r2` | NFR-02, CS-03, CS-05 |
| `US-DN-008` | Story | `FT-DN-10` | Open an order and see its details | Must | `track-dotnet`, `dotnet-r2` | BR-03, P-03, CS-05 |
| `US-DN-009` | Story | `FT-DN-10` | See my negotiated prices on an order | Must | `track-dotnet`, `dotnet-r2` | BR-12, CS-20, ES-18, C-05 |
| `US-DN-010` | Story | `FT-DN-10` | The order detail responds in under 2 seconds | Must | `track-dotnet`, `dotnet-r2` | NFR-02, CS-03 |
| `US-DN-011` | Story | `FT-DN-11` | See one of six statuses on an order | Must | `track-dotnet`, `dotnet-r2` | BR-04, P-03, CS-10 |
| `US-DN-012` | Story | `FT-DN-11` | Understand how fresh the status is | Must | `track-dotnet`, `dotnet-r2` | BR-04, CS-10, C-03, SM-02 |
| `US-DN-013` | Story | `FT-DN-12` | Start a new order by copying a previous order | Must | `track-dotnet`, `dotnet-r2` | BR-05, P-04, CS-16 |
| `US-DN-014` | Story | `FT-DN-12` | Change quantities and remove lines before submitting | Must | `track-dotnet`, `dotnet-r2` | BR-05, P-02, P-04 |
| `US-DN-015` | Story | `FT-DN-12` | See my prices on the draft order | Must | `track-dotnet`, `dotnet-r2` | BR-12, CS-20, C-05, ES-18 |
| `EN-DN-13` | Enabler | `FT-DN-14` | Audit completeness | Must | `track-dotnet`, `dotnet-r2` | NFR-08, BR-10, CS-05 |
| `US-DN-016` | Story | `FT-DN-13` | Submit the order and see it in Order Desk as Received | Must | `track-dotnet`, `dotnet-r2` | BR-06, C-05, P-01, P-02 |
| `US-DN-017` | Story | `FT-DN-13` | The server marks portal orders with the Portal channel | Must | `track-dotnet`, `dotnet-r2` | BR-10 |
| `US-DN-018` | Story | `FT-DN-14` | Every order change records who, what, when and channel | Must | `track-dotnet`, `dotnet-r2` | NFR-08, BR-10, CS-05 |
| `US-DN-019` | Story | `FT-DN-14` | Audit records are kept for 7 years | Must | `track-dotnet`, `dotnet-r2` | NFR-08, CS-05 |
| `US-DN-020` | Story | `FT-DN-16` | Use the portal with keyboard and screen reader | Must | `track-dotnet`, `dotnet-r2` | NFR-07, BR-03 |
| `US-DN-021` | Story | `FT-DN-16` | Read the portal with enough contrast, zoom and clear errors | Must | `track-dotnet`, `dotnet-r2` | NFR-07 |
| `EN-DN-12` | Enabler | `FT-DN-15` | Localisation scaffold | Should | `track-dotnet`, `dotnet-r2` | BR-11 |

Counts: 4 epics (`EP-DN-02` to `EP-DN-05`), 12 features (`FT-DN-05` to `FT-DN-16`), 6 enablers (`EN-DN-08`, `EN-DN-10`, `EN-DN-11`, `EN-DN-12`, `EN-DN-13`, `EN-DN-14`) and 19 stories (`US-DN-003` to `US-DN-021`). Total 41. 39 items are Must and 2 are Should (`FT-DN-15` and `EN-DN-12`). `EP-DN-05` is Must because an epic takes the highest priority of its children (backlog section 3.2).

## 4. Requirements covered

**Business requirements (BR-).**

| ID | What it says (short) | Priority | Source | Carried in this release by |
|---|---|---|---|---|
| BR-01 | A customer user can sign in and see only the orders of their own company. | Must | BR-01, C-05, NFR-04 | `EN-DN-10`, `US-DN-003`, `US-DN-004`, `FT-DN-06`, `FT-DN-07`, `EP-DN-02` |
| BR-02 | A customer user can see the list of their company's orders from the last 24 months with order date, status and total. | Must | BR-02, CS-05, P-03 | `US-DN-006`, `FT-DN-09` |
| BR-03 | A customer user can open an order and see its lines, quantities, prices, delivery address and current status. | Must | BR-03, P-03, CS-05 | `US-DN-008`, `US-DN-020`, `FT-DN-10` |
| BR-04 | A customer user sees the status of an order as one of six statuses. The business case says "always up to date". | Must | BR-04, CS-10, C-03 | `US-DN-011`, `US-DN-012`, `FT-DN-11`. Shown "as of the 02:00 batch" (A-04, OPEN-01). |
| BR-05 | A customer user can create a new order by copying a previous order and changing quantities or removing lines before submitting it. | Must | BR-05, P-02, P-04, CS-16 | `US-DN-013`, `US-DN-014`, `FT-DN-12` |
| BR-06 | A submitted portal order appears in Order Desk without being re-keyed, with the status Received. | Must | BR-06, C-05, P-01, P-02 | `US-DN-016`, `FT-DN-13` |
| BR-10 | Order Desk staff can see whether an order was placed through the portal or entered by staff. | Must | BR-10 | `US-DN-017` (the **portal stamp**: the server sets the Portal channel), `EN-DN-13`, `US-DN-018`. The staff view is in `dotnet-r1`. |
| BR-12 | The portal respects each customer's negotiated prices; the customer sees their price, not the list price. | Must | BR-12, CS-20, C-05 | `US-DN-009`, `US-DN-015`, `FT-DN-10`, `FT-DN-12`. Until OPEN-16 is answered the portal shows the net unit price and the net totals only (A-41). |
| BR-11 | The portal is available in French and English. Dutch is requested by Belgian customers. | Should | BR-11 | **Foundation only:** `EN-DN-12`, `FT-DN-15`. The French and English texts are in `dotnet-r3`. |

**Quality targets (NFR-).** An NFR has no priority in the business case. It is treated as Must because it gates a release that carries a Must outcome (A-12).

| ID | What it says (short) | Source | Carried in this release by | Note |
|---|---|---|---|---|
| NFR-02 | Order list and order detail pages respond in under 2 seconds for 95 % of requests | NFR-02, CS-03, CS-05 | `US-DN-007`, `US-DN-010` | Test figures are A-37. The measurement basis is OPEN-08. |
| NFR-03 | Customer data and order data stay in the European Union | NFR-03, ES-20 | `US-DN-005` (application side: sign-in, mail and monitoring), `FT-DN-08`, `EN-DN-11` | The platform side is an Azure-track story (A-02). |
| NFR-04 | Customers sign in with an identity managed outside the application; staff use Microsoft Entra ID | NFR-04, CS-04, OQ-01 | `EN-DN-08` (staff), `US-DN-004` (customers), `EN-DN-11`, `FT-DN-07` | There is no Azure story for NFR-04 (A-02, OPEN-13). |
| NFR-07 | The portal meets WCAG 2.2 level AA | NFR-07 | `EN-DN-14`, `US-DN-020`, `US-DN-021`, `FT-DN-16` | |
| NFR-08 | Every change to an order (who, what, when, channel) is recorded for 7 years | NFR-08, CS-05 | `EN-DN-13`, `US-DN-018`, `US-DN-019`, `FT-DN-14` | The "what" is the free-text action today (OPEN-17). 7-year sizing and retrieval are OPEN-22. |

**Constraints (C-) carried.**

| ID | What it says (short) | Carried by |
|---|---|---|
| C-03 | StockPilot stays on premises and does not change | `US-DN-012`, `FT-DN-11` (status is as fresh as the nightly exchange) |
| C-04 | Azure run cost of at most EUR 1,500 per month (shared by both tracks, A-14) | `EN-DN-11` (the decision record compares price). Hosting cost reporting is OPEN-04. |
| C-05 | The portal reuses Order Desk as the single source of truth for orders. No second order database. | `EN-DN-10`, `EN-DN-11`, `US-DN-003`, `US-DN-009`, `US-DN-015`, `US-DN-016` |

**Success measures (SM-) moved.** This release starts the clock for **SM-01** (share of orders placed through the portal: 0 % now, 35 % six months after portal launch), **SM-02** ("where is my order?" calls per week: 410 now, 250 or fewer) and **SM-03** (order lines needing correction after entry: 4.1 % now, 2.5 % or fewer). "Portal launch" is OPEN-05. **ASSUMPTION:** A-46: a 35 % share is not expected to be reached with 20 of about 1,150 customers. It depends on their order volume (OPEN-05). The measures themselves are taken in `dotnet-r4` (source: SM-01, SM-02, SM-03, CS-05).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Invoice download (BR-07) | `dotnet-r3` |
| Customer administrator who invites and removes users (BR-08) | `dotnet-r3` |
| French and English texts (BR-11). Only the language foundation is here. | `dotnet-r3` |
| Shipped e-mail (BR-09) and storing shipment date and carrier | `dotnet-r4` |
| Measuring SM-01 to SM-04 | `dotnet-r4` |
| Dutch, field-level audit, Order Desk programming interface, status clarity options | Unplanned (track tag only). See the appendix in `dotnet-r4`. |
| Changing the delivery address on a reorder | Not planned. A reorder keeps the address of the copied order (A-42). |
| Showing volume and Gold discounts to customers | Not planned until OPEN-16 is answered (A-41). |
| A faster status refresh than the nightly 02:00 batch | Not planned. See OPEN-01 and OPEN-20. |
| A pilot environment for the portal, and the hosting and database choice | Not planned in this track. See OPEN-05 and OPEN-19. |
| Creating customer accounts for the 20 pilot customers (before the customer administrator exists) | Not planned as a feature. See OPEN-33. |
| Online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope (business case section 6). |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Deploying or publishing anything from this workshop | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a decision record for the portal architecture and customer sign-in with its price and limit check; a test showing that a customer user of one company cannot see another company's data; a staff sign-in with Microsoft Entra ID; a list, detail and status view with the negotiated prices and the "as of the 02:00 batch" label; a reorder that appears in Order Desk as Received with the Portal channel; an audit trail for every order change; an accessibility report against WCAG 2.2 level AA; and a response-time test for the list and detail pages. From those, Lena Varga can decide to start the pilot with 20 customers.

## 7. Dependencies

### 7.1 Order inside the .NET track

This release builds on `dotnet-r1`: the modernised Order Desk, the tests, the configuration and the draft order handling that works on one or several instances. **Customer data separation (`EN-DN-10`) comes before every portal story that shows data, and each such story cites it** (A-22). The accessibility enabler `EN-DN-14` comes before the pages it shapes. The product owner may change the order inside a release without changing any tag (A-43). The "Depends on" column names items of the .NET track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 11 | `EN-DN-11` | Portal architecture and sign-in decision record | `EN-DN-01` |
| 12 | `EN-DN-10` | Customer data separation (tenant isolation) | `EN-DN-11` |
| 13 | `EN-DN-08` | Staff sign-in with Microsoft Entra ID | `EN-DN-11`, `EN-DN-01` |
| 14 | `US-DN-004` | Customer user signs in | `EN-DN-11`, `EN-DN-10` |
| 15 | `US-DN-003` | Customer user sees only their own company | `EN-DN-10`, `US-DN-004` |
| 16 | `US-DN-005` | Portal sign-in, mail and monitoring keep data in the EU | `EN-DN-11`, `EN-DN-10` |
| 17 | `EN-DN-14` | Accessibility baseline (WCAG 2.2 AA) | `EN-DN-01` |
| 18 | `US-DN-006` | See my company's orders from the last 24 months | `EN-DN-10`, `EN-DN-14`, `US-DN-004` |
| 19 | `US-DN-007` | The order list responds in under 2 seconds | `US-DN-006`, `EN-DN-10` |
| 20 | `US-DN-008` | Open an order and see its details | `EN-DN-10`, `EN-DN-14`, `US-DN-006` |
| 21 | `US-DN-009` | See my negotiated prices on an order | `US-DN-008`, `EN-DN-10` |
| 22 | `US-DN-010` | The order detail responds in under 2 seconds | `US-DN-008`, `EN-DN-10` |
| 23 | `US-DN-011` | See one of six statuses on an order | `US-DN-008`, `EN-DN-10` |
| 24 | `US-DN-012` | Understand how fresh the status is | `US-DN-011`, `EN-DN-10` |
| 25 | `US-DN-013` | Start a new order by copying a previous order | `EN-DN-06`, `US-DN-008`, `EN-DN-10` |
| 26 | `US-DN-014` | Change quantities and remove lines before submitting | `US-DN-013`, `EN-DN-10` |
| 27 | `US-DN-015` | See my prices on the draft order | `US-DN-014`, `US-DN-009`, `EN-DN-10` |
| 28 | `EN-DN-13` | Audit completeness | `EN-DN-01` |
| 29 | `US-DN-016` | Submit the order and see it in Order Desk as Received | `US-DN-014`, `EN-DN-13`, `EN-DN-10` |
| 30 | `US-DN-017` | The server marks portal orders with the Portal channel | `US-DN-016`, `US-DN-001`, `EN-DN-10` |
| 31 | `US-DN-018` | Every order change records who, what, when and channel | `EN-DN-13`, `US-DN-016`, `EN-DN-10` |
| 32 | `US-DN-019` | Audit records are kept for 7 years | `EN-DN-13`, `EN-DN-10` |
| 33 | `US-DN-020` | Use the portal with keyboard and screen reader | `US-DN-006`, `US-DN-008`, `US-DN-014`, `EN-DN-10` |
| 34 | `US-DN-021` | Read the portal with enough contrast, zoom and clear errors | `US-DN-020`, `EN-DN-10` |
| 35 | `EN-DN-12` | Localisation scaffold (Should) | `EN-DN-01` |

The ranks continue from `dotnet-r1` (ranks 1 to 10). `EN-DN-06` (draft order kept outside one server's memory), `EN-DN-01` and `US-DN-001` are in `dotnet-r1`. Why this order: nothing that shows customer data is built before the separation of customer data exists. `EN-DN-12` is a Should item and is ranked last in its priority block. It is cheaper to build before more screens exist, so the product owner may pull it forward inside this release without changing any tag (A-43, OPEN-27). The product owner may also split the release into a read-only slice and a reorder slice (OPEN-26). That is a decision for Lena Varga, not a change made here.

**Effect of the experiment `MVE-BA02`.** The experiment tests whether a status view that is only as fresh as the 02:00 update is enough for customers (A-06). Its result changes the shape of the status stories (`FT-DN-11`) and may bring the unplanned status options into this release (A-35). `dotnet-r1` is not affected. The pilot decision waits only for Lena Varga.

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | Shows status "as of the 02:00 batch" (A-04) (`US-DN-011`, `US-DN-012`). |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Builds on the modernised Order Desk from its own track (A-03). The .NET track does the staff sign-in (`EN-DN-08`). |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports the hosting cost of the portal. Applies no split (`EP-DN-02`). |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Builds so that it can run in any environment that meets ES-20 and ES-25. Does not assume a pilot environment. Takes the launch date as a setting. |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Compares the options in the decision record (`EN-DN-11`) and checks price and limits (OPEN-25). Starts customer sign-in once the choice is recorded. Other features in this release do not wait (`EN-DN-08`, `US-DN-004`). |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the modernised draft order handling from `dotnet-r1`, which works on one or several instances (`EN-DN-11`). |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Plans no schema change. Any change goes through a migration-impact check and a decision record (ES-19) (`US-DN-016`, `EN-DN-13`). |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Deletes no audit rows. Sets no sizing or retrieval target (`EN-DN-13`, `US-DN-019`). |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Used by `US-DN-016`. The order confirmation is on screen only. No confirmation e-mail is sent until a mail path is named. |

OPEN-18 is used by an item in this release but is not in the plan's list of cross-track items for `dotnet-r2` (section 11, difference 3). Other OPEN items used here concern the .NET track only: OPEN-02, 08, 09, 10, 16, 17, 25, 27, 33 (section 9).

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-05 | Confirmed, Delivered and Cancelled are manual staff actions today | Order Desk team via Lena Varga |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-13 | The portal is a responsive web site for current browsers (mobile via browser) | Sofie Peeters, Ahmed Benali |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-18 | BR-10 stories are small: show the channel, filter by it, and set the Portal channel on the server | Lena Varga |
| A-21 | Entra External ID pricing and limits, and .NET 10 on Azure App Service, are not verified | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-35 | The two status options in `FT-DN-26` (show the time each status last changed; explain Picking and Shipped in plain words) come from the pivot outcome of `MVE-BA02`. They are unplanned until the result is known. If the product owner plans them, the feature and its stories take the same track tag and the same release tag together (for example `dotnet-r2`) | Lena Varga |
| A-37 | Test figures not given in the business case. NFR-02 is tested with 60 users at once (the staff peak, CS-03), a test company with about 500 orders in 24 months, a test order with 100 lines, 20 orders per page, over 10 minutes. NFR-01 uses a probe about every 5 minutes, an alert after two failed checks in a row, and a calendar-week measurement (84 business hours, about 25 minutes of downtime allowed at 99.5 %) | Lena Varga, Ahmed Benali |
| A-41 | Until OPEN-16 is answered, the portal shows each customer's net unit price and the net line and order totals, and no discount breakdown | Lena Varga |
| A-42 | A reorder keeps the delivery address of the copied order. Changing the address in the portal is not part of the pilot | Lena Varga |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) | `EP-DN-02`, `FT-DN-11`, `US-DN-011`, `US-DN-012` |
| OPEN-02 | Source of Confirmed, Delivered, Cancelled status | Lena Varga with the Order Desk team | .NET | `FT-DN-11`, `US-DN-011` |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET | `EP-DN-02`, `EN-DN-08` |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | `EP-DN-02` |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | `EP-DN-02` |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET | `FT-DN-09`, `US-DN-007`, `US-DN-010`, `US-DN-019` |
| OPEN-09 | 24 months of orders exist; where `Orders.InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | .NET | `FT-DN-09`, `US-DN-006` |
| OPEN-10 | Data-protection requirement for customer users (Ahmed Benali); mobile expectations (Sofie Peeters) | Ahmed Benali, Sofie Peeters | .NET | `EN-DN-11`, `EN-DN-14`, `US-DN-005` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET | `FT-DN-05`, `FT-DN-07`, `EN-DN-08`, `EN-DN-11`, `US-DN-004` |
| OPEN-16 | Show volume and Gold discounts to customers, or only the net price | Lena Varga | .NET | `FT-DN-10`, `US-DN-009`, `US-DN-015` |
| OPEN-17 | Is the free-text audit action enough for NFR-08 or are field-level changes needed | Lena Varga | .NET | `FT-DN-14`, `EN-DN-13`, `US-DN-018` |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET | `US-DN-016` |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | `EP-DN-02`, `EN-DN-11` |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET | `EP-DN-02`, `EN-DN-13`, `US-DN-016` |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET | `EP-DN-02`, `FT-DN-14`, `EN-DN-13`, `US-DN-019` |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET | `US-DN-012` (named in backlog section 8; its own text does not cite it, section 11, difference 4) |
| OPEN-25 | Verify Entra External ID pricing and .NET 10 on App Service | Ahmed Benali | .NET | `FT-DN-05`, `EN-DN-11`, `US-DN-004` |
| OPEN-26 | Split `dotnet-r2` into a read-only slice and a reorder slice? | Lena Varga | .NET | The release as a whole (section 7.1) |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET | `FT-DN-15`, `EN-DN-12` |
| OPEN-33 | How do the first customer users get an account and a link to their company in `dotnet-r2`, before the customer administrator feature (`dotnet-r3`) exists? Option: Northwind staff or IT create and link the accounts for the 20 pilot customers | Lena Varga with Ahmed Benali | .NET | `EN-DN-10`, `US-DN-004` |

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 41 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-dotnet` and `dotnet-r2` on every item. A query on the tag `dotnet-r2` lists the release. |
| GitHub | Issue labels `track-dotnet` and `dotnet-r2`, and the milestone `dotnet-r2`. |
| Jira | Labels `track-dotnet` and `dotnet-r2`, and the fix version `dotnet-r2`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). An enabler is published as a story whose title starts with its `EN-` ID. The Git tag `product/dotnet-r2` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | The plan calls this release "Portal pilot: Must items". The register puts the language scaffold, a **Should** item (BR-11), in it. The backlog gives the reason (cheaper before more screens exist) and OPEN-27 asks whether to pull more of BR-11 forward. `EP-DN-05` is Must only because an epic takes the highest priority of its children. | `EN-DN-12`, `FT-DN-15`, `EP-DN-05` |
| 2 | The plan's "Covers" list for this release does not name BR-11. The register's items cite it (traceability section 7 counts it for `dotnet-r2`). | `EN-DN-12`, `FT-DN-15` |
| 3 | `US-DN-016` cites OPEN-18 (mail path), a cross-track item that is not in the plan's list for `dotnet-r2` (OPEN-01, 03, 04, 05, 13, 19, 20, 22). It is shown in section 7.2. | `US-DN-016` |
| 4 | The backlog (section 8) lists `US-DN-012` for OPEN-23 (time zone), but the item text does not cite OPEN-23. OPEN-23 is not on the plan's list for this release. It is shown in section 9 so that the ID has a row. | `US-DN-012` |
| 5 | The business case says the status is "always up to date" (BR-04). The backlog shows it "as of the 02:00 batch" (A-04) because StockPilot cannot change (C-03). The gap is OPEN-01 and `MVE-BA02`. | `US-DN-011`, `US-DN-012`, `FT-DN-11` |
| 6 | `EP-DN-02` states eight cross-track OPEN items for the whole release, as the plan asks. In their own text, the items under `EP-DN-02` cite only OPEN-03, 13 and 19. OPEN-01, 20 and 22 are cited by items under other epics. OPEN-04 and OPEN-05 are cited by no item of this release. | `EP-DN-02` |

## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. `dotnet-r1` is accepted (inside the .NET track). Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer. The sign-in choice is recorded in `EN-DN-11` before customer sign-in starts (OPEN-13).

**Definition of done.** The release is done when the acceptance criteria of its 41 items are met by tests and review only (ES-27):

* *Decision.* A decision record compares the customer sign-in options on price, limits, EU data location and the data-protection requirement, checks Entra External ID and .NET 10 on App Service against the official Microsoft pages, and is approved by a named person (OPEN-13, OPEN-25).
* *Customer data separation.* A test with two test companies shows that a customer user can never read or change the data of another company, in lists, details, reorders and downloads (BR-01, C-05).
* *Sign-in.* Customer users sign in with an identity managed outside the application. Staff sign in with Microsoft Entra ID (NFR-04). Sign-in, mail and monitoring for the portal keep data in the EU (NFR-03).
* *See my orders.* A customer user sees the orders of their company for the last 24 months, the details with their own negotiated prices and the status "as of the 02:00 batch". List and detail pages respond in under 2 seconds for 95 % of requests under the test in A-37 (NFR-02). **Pricing results are unchanged and the pricing tests keep their assertions (CS-20, ES-18).**
* *Reorder and hand-off.* A reorder starts from a copy, lets the customer change quantities and remove lines, shows their prices, and appears in Order Desk as Received with the Portal channel, without re-keying (BR-05, BR-06, BR-10).
* *Audit.* Every order change records who, what, when and channel, and audit rows are kept and not deleted (NFR-08, OPEN-22).
* *Quality.* The portal passes a WCAG 2.2 level AA check, including keyboard, screen reader, contrast, zoom and clear errors (NFR-07). The language scaffold is in place and the default language is a setting (`EN-DN-12`, OPEN-27).
* *Tests (ES-18).* `dotnet test src/Northwind.OrderDesk.sln` still passes on Windows, macOS and Linux, with no assertion weakened or removed.
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop (ES-27).** The pilot with 20 customers is started by Northwind in its own controlled process. This file does not start or authorise it.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/dotnet-r2` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/dotnet-r2` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/dotnet-r2`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/dotnet-r2` is created on the commit that holds this file.**
