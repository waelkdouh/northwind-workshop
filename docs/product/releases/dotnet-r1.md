# Release dotnet-r1: Modernised Order Desk (.NET track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D7 (ES-31) |
| Track | .NET, business area BA-02 Ordering and customer self-service |
| Release name | Modernised Order Desk (enabler release) |
| Release tag | `dotnet-r1` |
| Track tag | `track-dotnet` |
| Git tag | `product/dotnet-r1`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r1 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | End of February 2027. **ASSUMPTION:** A-07 (a target, not a commitment). |
| Date of this file | 2026-10-30 |
| Items in this release | 15: 1 epic, 4 features, 8 enablers, 2 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.4), `docs/product/business-requirements.md`, `docs/product/experiments.md`, `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-13 to ES-19, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is built, deployed, published, committed or tagged from it (ES-27). |

## 1. Words used

* **BA-02** is the business area "Ordering and customer self-service". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **Order Desk** is the internal web application staff use to enter and manage orders. **Portal** is the new customer web site, built in later .NET releases. **Staff** are Order Desk employees.
* **.NET 10** (`net10.0`) is the current supported version of the Microsoft platform that Order Desk is built on. Today Order Desk runs on **.NET Framework 4.8**, built in 2013 (CS-01). **SDK-style project** is the current project file format. Today's projects use an old format with `packages.config` (CS-02).
* **Channel** is how an order was placed: Phone, E-mail, Order form or Portal (A-22).
* **Pipeline** is an automated job that builds the code and runs the tests on every change. **Pricing rules** are the customer-negotiated prices and volume discounts in the code (CS-20).
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Order Desk is on a current platform and behaves as before. The 28 existing tests run on Windows, macOS and Linux and still protect the pricing rules. Nothing in the application ties it to one server: no password in the configuration, no fixed network path for invoices, no order held in one server's memory. Staff can see, and filter by, how each order was placed (source: CS-01, CS-02, CS-13 to CS-20, NFR-05, BR-10, ES-14 to ES-19).

This is a small, early outcome that the product owner can approve on its own. Every later .NET release is built on it. Nothing for customers can be built safely on .NET Framework 4.8 with tests that run only inside Visual Studio (source: CS-01, CS-18, ES-14, ES-18).

## 3. Items planned in this release

The list below is every item that carries the tags `track-dotnet` and `dotnet-r1`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `dotnet-r1`: 15 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-DN-01` | Epic | - | Modernised Order Desk | Must | `track-dotnet`, `dotnet-r1` | BR-10, NFR-05, CS-01, CS-02, CS-13, CS-14, CS-15, CS-16, CS-17, CS-18, CS-19, CS-20, ES-13, ES-14, ES-15, ES-16, ES-17, ES-18, ES-19 |
| `FT-DN-01` | Feature | `EP-DN-01` | Current platform and safety net | Must | `track-dotnet`, `dotnet-r1` | CS-01, CS-02, CS-18, CS-19, CS-20, ES-13, ES-14, ES-18, ES-19 |
| `FT-DN-02` | Feature | `EP-DN-01` | Configuration, logging and no secrets | Must | `track-dotnet`, `dotnet-r1` | NFR-05, CS-13, CS-15, CS-17, ES-15, ES-16, ES-17 |
| `FT-DN-03` | Feature | `EP-DN-01` | Draft order and invoice storage free of one server | Must | `track-dotnet`, `dotnet-r1` | CS-14, CS-16 |
| `FT-DN-04` | Feature | `EP-DN-01` | Staff see the order channel | Must | `track-dotnet`, `dotnet-r1` | BR-10, CS-03 |
| `EN-DN-01` | Enabler | `FT-DN-01` | SDK-style projects on `net10.0` | Must | `track-dotnet`, `dotnet-r1` | CS-01, CS-02, ES-13, ES-14, ES-19 |
| `EN-DN-02` | Enabler | `FT-DN-01` | Tests pass on Windows, macOS and Linux | Must | `track-dotnet`, `dotnet-r1` | CS-18, CS-20, ES-18 |
| `EN-DN-09` | Enabler | `FT-DN-01` | Build and test pipeline | Must | `track-dotnet`, `dotnet-r1` | CS-19, CS-18, ES-18, NFR-05 |
| `EN-DN-03` | Enabler | `FT-DN-02` | Configuration through options | Must | `track-dotnet`, `dotnet-r1` | CS-17, ES-15 |
| `EN-DN-04` | Enabler | `FT-DN-02` | Logging through `ILogger<T>` | Must | `track-dotnet`, `dotnet-r1` | CS-15, ES-16 |
| `EN-DN-05` | Enabler | `FT-DN-02` | No secrets and no Windows-sign-in database connection | Must | `track-dotnet`, `dotnet-r1` | NFR-05, CS-13, ES-17, ES-25 |
| `EN-DN-06` | Enabler | `FT-DN-03` | Draft order kept outside one server's memory | Must | `track-dotnet`, `dotnet-r1` | CS-16, ES-19 |
| `EN-DN-07` | Enabler | `FT-DN-03` | Invoice storage setting instead of a fixed network path | Must | `track-dotnet`, `dotnet-r1` | CS-14, CS-11 |
| `US-DN-001` | Story | `FT-DN-04` | Staff see the order channel | Must | `track-dotnet`, `dotnet-r1` | BR-10, CS-03 |
| `US-DN-002` | Story | `FT-DN-04` | Staff filter orders by channel | Must | `track-dotnet`, `dotnet-r1` | BR-10, CS-03 |

Counts: 1 epic, 4 features, 8 enablers (`EN-DN-01` to `EN-DN-07` and `EN-DN-09`) and 2 stories (`US-DN-001`, `US-DN-002`). Total 15. All are priority Must.

## 4. Requirements covered

**Business requirement (BR-).**

| ID | What it says (short) | Priority | Source | Carried in this release by |
|---|---|---|---|---|
| BR-10 | Order Desk staff can see whether an order was placed through the portal or entered by staff. | Must | BR-10, CS-03 | `US-DN-001` (show the channel), `US-DN-002` (filter by channel), `FT-DN-04`. This is the **staff view** only. The server stamping portal orders with the Portal channel is in `dotnet-r2`. Scope follows A-18. |

**Quality target (NFR-).** An NFR has no priority in the business case. It is treated as Must because it gates a release that carries a Must outcome (A-12).

| ID | What it says (short) | Source | Carried in this release by | Note |
|---|---|---|---|---|
| NFR-05 | No secret (password, connection string with password, key) in source code or in configuration files in the repository | NFR-05, CS-13, ES-17, ES-25 | `EN-DN-05` (application side), `EN-DN-09` (no secret in the pipeline), `FT-DN-02` | The platform side (Key Vault, managed identities) is a separate story in the Azure track (A-02). |

**Constraints and standards that apply.** C-05 (Order Desk stays the single source of truth for orders) and C-06 (small IT team that knows .NET and SQL Server). ES-13 (one solution, three projects), ES-14 (current platform), ES-15 (configuration), ES-16 (logging), ES-17 (no secrets), ES-18 (tests) and ES-19 (modernise in place; keep behaviour unless a decision record explains a change). **Pricing rules do not change** (CS-20).

**Success measures (SM-) moved.** None directly. This release protects the pricing rules and makes the later measures possible (source: CS-20, SM-01 to SM-04).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Customer sign-in, customer data separation, staff Microsoft Entra ID sign-in, the portal decision record | `dotnet-r2` (already planned there) |
| The Portal channel stamp on submitted portal orders, and the audit work | `dotnet-r2` |
| The language foundation and accessibility baseline | `dotnet-r2` |
| Invoice download, customer administrator, French and English | `dotnet-r3` |
| Shipped e-mail, storing shipment date and carrier, measuring SM-01 to SM-04 | `dotnet-r4` |
| Dutch, field-level audit, Order Desk programming interface, status clarity options | Unplanned (track tag only). See the appendix in `dotnet-r4`. |
| A deployment pipeline to a server, and any hosting or database work | Not planned in this release. See OPEN-21 and OPEN-19. This release delivers the build and test pipeline only. |
| A change of pricing rules, screens or behaviour | Not planned. Behaviour stays the same unless a decision record says otherwise (ES-19). |
| Any change to StockPilot and any change to the finance system | Out of scope (C-03). |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Business case section 6 exclusions: online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope. |
| Deploying or publishing anything from this workshop | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a statement that Order Desk builds on .NET 10 with the same three projects and the same staff screens; a test result showing the same number of tests (28 or more) passing on Windows, macOS and Linux, with the pricing tests unchanged; a build and test pipeline that reports a failed check when a test fails; a configuration and logging change with no secret left in the repository; a draft order and invoice reading that work on one server or several; and a staff screen that shows and filters the order channel. From those, the Order Desk team can approve the base on which the portal is built.

## 7. Dependencies

### 7.1 Order inside the .NET track

This is the first .NET release. It uses no earlier .NET release. Every later .NET item builds on `EN-DN-01`. The product owner may change the order inside a release without changing any tag (A-43). The "Depends on" column names items of the .NET track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 1 | `EN-DN-01` | SDK-style projects on `net10.0` | none |
| 2 | `EN-DN-02` | Tests pass on Windows, macOS and Linux | `EN-DN-01` |
| 3 | `EN-DN-09` | Build and test pipeline | `EN-DN-02` |
| 4 | `EN-DN-03` | Configuration through options | `EN-DN-01` |
| 5 | `EN-DN-04` | Logging through `ILogger<T>` | `EN-DN-01` |
| 6 | `EN-DN-05` | No secrets and no Windows-sign-in database connection | `EN-DN-03` |
| 7 | `EN-DN-06` | Draft order kept outside one server's memory | `EN-DN-01` |
| 8 | `EN-DN-07` | Invoice storage setting instead of a fixed network path | `EN-DN-03` |
| 9 | `US-DN-001` | Staff see the order channel | `EN-DN-01` |
| 10 | `US-DN-002` | Staff filter orders by channel | `US-DN-001` |

Why this order: the platform move comes first, the tests come next so that every later change is protected, and the staff story comes last because it is the only change a staff member can see. The epic and the four features are ranked with their children (source: backlog section 4.2).

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | The .NET track modernises the Order Desk code in place (A-03). It does not wait for hosting work (`EN-DN-01`). |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports any change that adds hosting cost and applies no split (`EP-DN-01`). |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Makes the draft order and invoice reading independent of any one server, so any hosting target works (`EN-DN-05`, `EN-DN-06`, `FT-DN-03`). |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Delivers the build and test pipeline for the solution (`EN-DN-09`). It includes no deployment steps. |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Keeps today's behaviour (local time for order dates, UTC for audit) and documents it. Changes it only with a decision record (ES-19) (`EP-DN-01`). |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Used by `EN-DN-07`. Reads invoices through a storage setting and assumes nothing about where Finance writes. The year used in the folder name stays as it is today. |

OPEN-06 is used by an item in this release but is not in the plan's list of cross-track items for `dotnet-r1`. It is shown here because `EN-DN-07` cites it (section 11, difference 1).

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-18 | BR-10 stories are small: show the channel, filter by it, and set the Portal channel on the server | Lena Varga |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-40 | ASP.NET MVC 5 does not run on .NET 10, so the `Web` project moves to ASP.NET Core MVC with the same routes, screens and behaviour. The project boundaries stay as they are (ES-13) | Ahmed Benali |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET | `EP-DN-01`, `EN-DN-01` |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | `EP-DN-01` |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET | `EN-DN-07` |
| OPEN-09 | 24 months of orders exist; where `Orders.InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | .NET | `EN-DN-07` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET | No item of this release. It is named in A-02 (no Azure story for NFR-04). Customer sign-in is in `dotnet-r2`. |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | `EP-DN-01`, `FT-DN-03`, `EN-DN-05`, `EN-DN-06` |
| OPEN-21 | CI/CD ownership: build and test pipeline vs deployment pipeline | Ahmed Benali | Azure and .NET | `EP-DN-01`, `EN-DN-09` |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET | `EP-DN-01` |

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 15 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-dotnet` and `dotnet-r1` on every item. A query on the tag `dotnet-r1` lists the release. |
| GitHub | Issue labels `track-dotnet` and `dotnet-r1`, and the milestone `dotnet-r1`. |
| Jira | Labels `track-dotnet` and `dotnet-r1`, and the fix version `dotnet-r1`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). An enabler is published as a story whose title starts with its `EN-` ID. The Git tag `product/dotnet-r1` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | `EN-DN-07` cites OPEN-06 and OPEN-09. OPEN-06 is a cross-track item that is not in the plan's list for `dotnet-r1` (OPEN-03, 04, 19, 21, 23). OPEN-09 is a .NET-only item. Both are shown in sections 7.2 and 9 with what the release does without the answer. | `EN-DN-07` |
| 2 | OPEN-04, OPEN-19 and OPEN-23 are on the plan's list for this release. The backlog states them at epic level (`EP-DN-01`). OPEN-19 is also cited by `EN-DN-05`, `EN-DN-06` and `FT-DN-03`. No item of this release cites OPEN-04 or OPEN-23 in its own text. | `EP-DN-01` |
| 3 | The plan names `EN-DN-07` "invoice storage abstraction". The backlog title is "Invoice storage setting instead of a fixed network path". Same item, different words. | `EN-DN-07` |

## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer.

**Definition of done.** The release is done when the acceptance criteria of its 15 items are met by tests and review only (ES-27):

* *Platform.* `src/Northwind.OrderDesk.sln` still holds exactly the projects `Core`, `Web` and `Tests`, all SDK-style and all on `net10.0`. No `packages.config` remains. Namespaces and domain type names are unchanged. Each existing staff screen (order list, order detail, draft order, change status, invoice) gives the same results as before (ES-13, ES-14, ES-19).
* *Tests (ES-18).* `dotnet test src/Northwind.OrderDesk.sln` finds and passes every test on Windows, macOS and Linux. The number of tests is not lower than the 28 that exist today, and no assertion is weakened or removed. **The pricing tests keep exactly the same expected values, because pricing rules do not change (CS-20).**
* *Pipeline.* A change under `src/` triggers a build and the tests on all three systems. A failing test or build gives a failed check. No password, key or connection string is stored in the pipeline definition (NFR-05). Deployment to a server is not part of it (OPEN-21).
* *Configuration, logging and secrets.* Configuration and logging use the current platform methods (ES-15, ES-16). A scan of the repository finds no secret and no Windows-sign-in database connection (NFR-05, ES-17).
* *Free of one server.* The draft order survives a change of server or a restart. Invoices are read through a setting instead of a fixed network path, and the year rule stays as it is today (OPEN-06, OPEN-09).
* *Staff view.* Staff see the channel of each order and can filter the order list by channel (BR-10, A-18).
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop (ES-27).** This file does not start or authorise any build, deployment or tag.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/dotnet-r1` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/dotnet-r1` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/dotnet-r1`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/dotnet-r1` is created on the commit that holds this file.**
