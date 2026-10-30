# Release dotnet-r3: Should items (.NET track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D7 (ES-31) |
| Track | .NET, business area BA-02 Ordering and customer self-service |
| Release name | Should items: invoices, customer administrator, French and English |
| Release tag | `dotnet-r3` |
| Track tag | `track-dotnet` |
| Git tag | `product/dotnet-r3`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r3 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | Not dated. **ASSUMPTION:** A-07 (no date is set for `dotnet-r3`). |
| Date of this file | 2026-10-30 |
| Items in this release | 10: 1 epic, 3 features, 0 enablers, 6 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.6), `docs/product/business-requirements.md`, `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-13 to ES-19, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is built, deployed, published, committed or tagged from it (ES-27). |

## 1. Words used

* **BA-02** is the business area "Ordering and customer self-service". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard. **P-** is a problem named in the business case.
* **Order Desk** is the internal web application staff use to enter and manage orders. **Portal** is the customer web site built in `dotnet-r2`. A **customer user** is a person at a customer company who signs in to the portal. A **customer administrator** is a customer user who may invite and remove other users of the same company.
* **Invoice** is the PDF invoice of a delivered order. Invoice files are named `{invoiceNumber}.pdf` in one folder per year on a file share (CS-11).
* **Finance system** is the system that writes the invoices. It is not changed by this product (business case section 6).
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Customers can download the PDF invoice of a delivered order. Customer administrators can invite and remove users of their own company. The portal speaks French and English. These are the Should items of the business case. They remove work from staff and widen who can use the portal (source: BR-07, BR-08, BR-11, P-05, OQ-02, OQ-03).

The release builds on customer data separation, sign-in and the language scaffold from `dotnet-r2`, and on the invoice storage setting from `dotnet-r1` (inside the .NET track, section 7.1). It has no enabler of its own.

## 3. Items planned in this release

The list below is every item that carries the tags `track-dotnet` and `dotnet-r3`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `dotnet-r3`: 10 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-DN-06` | Epic | - | Self-service extras | Should | `track-dotnet`, `dotnet-r3` | BR-07, BR-08, BR-11 |
| `FT-DN-17` | Feature | `EP-DN-06` | Invoice download | Should | `track-dotnet`, `dotnet-r3` | BR-07, P-05, CS-08, CS-11, CS-14 |
| `FT-DN-18` | Feature | `EP-DN-06` | Customer administrator | Should | `track-dotnet`, `dotnet-r3` | BR-08, OQ-03 |
| `FT-DN-19` | Feature | `EP-DN-06` | French and English | Should | `track-dotnet`, `dotnet-r3` | BR-11, OQ-02 |
| `US-DN-022` | Story | `FT-DN-17` | Download the PDF invoice of a delivered order | Should | `track-dotnet`, `dotnet-r3` | BR-07, P-05, CS-11, CS-14 |
| `US-DN-023` | Story | `FT-DN-17` | Clear message when an invoice is not available | Should | `track-dotnet`, `dotnet-r3` | BR-07, P-05 |
| `US-DN-024` | Story | `FT-DN-18` | Customer administrator invites a user | Should | `track-dotnet`, `dotnet-r3` | BR-08, OQ-03, NFR-04 |
| `US-DN-025` | Story | `FT-DN-18` | Customer administrator removes a user | Should | `track-dotnet`, `dotnet-r3` | BR-08, OQ-03 |
| `US-DN-026` | Story | `FT-DN-19` | Use the portal in French or English | Should | `track-dotnet`, `dotnet-r3` | BR-11, OQ-02 |
| `US-DN-027` | Story | `FT-DN-19` | The portal remembers my language | Should | `track-dotnet`, `dotnet-r3` | BR-11, OQ-02 |

Counts: 1 epic, 3 features, 0 enablers and 6 stories (`US-DN-022` to `US-DN-027`). Total 10. All are priority Should.

## 4. Requirements covered

**Business requirements (BR-).**

| ID | What it says (short) | Priority | Source | Carried in this release by |
|---|---|---|---|---|
| BR-07 | A customer user can download the PDF invoice of a delivered order. | Should | BR-07, P-05, CS-11, CS-14 | `US-DN-022`, `US-DN-023`, `FT-DN-17` |
| BR-08 | A customer administrator can invite and remove users of their own company. | Should | BR-08, OQ-03 | `US-DN-024`, `US-DN-025`, `FT-DN-18` |
| BR-11 | The portal is available in French and English. Dutch is requested by Belgian customers. | Should | BR-11, OQ-02 | `US-DN-026`, `US-DN-027`, `FT-DN-19`. French and English only. Dutch is unplanned (OPEN-14). The language scaffold is in `dotnet-r2` (`EN-DN-12`). |

**Quality targets (NFR-).** NFR-04 is cited by `US-DN-024`: invitations use the customer sign-in set up in `dotnet-r2`. No NFR is carried as a main target of this release. New pages must stay at WCAG 2.2 level AA (NFR-07, carried in `dotnet-r2`).

**Constraints (C-) that apply.** C-04 (storage and hosting cost stay inside the EUR 1,500 ceiling, shared by both tracks, A-14) and C-05 (Order Desk stays the single source of truth). No item of this release cites a C- identifier in its own source line.

**Success measure (SM-) moved.** **SM-04: invoice copy requests handled by staff per week, 120 now, 40 or fewer six months after portal launch.** The invoice download stories reduce these requests. The measure is taken in `dotnet-r4` (`US-DN-033`). "Portal launch" is OPEN-05 (source: SM-04, P-05).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Customer sign-in, customer data separation, the language scaffold, the order views and reorder | `dotnet-r2` (already planned there) |
| Modernised Order Desk, tests and the invoice storage setting | `dotnet-r1` (already planned there) |
| Shipped e-mail (BR-09) and storing shipment date and carrier | `dotnet-r4` |
| Measuring SM-01 to SM-04 | `dotnet-r4` |
| Dutch (`US-DN-034`) | Unplanned (track tag only). See OPEN-14 and the appendix in `dotnet-r4`. |
| Any change to how the finance system writes invoices | Out of scope. See OPEN-06. |
| Customer administrators limited to large customers | Not planned. Until OPEN-15 is answered, Northwind staff set administrators for any customer. |
| Online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope (business case section 6). |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Deploying or publishing anything from this workshop | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a test that a customer user can download the PDF invoice of a delivered order of their own company and no one else's; a clear message when an invoice is not available; a test that a customer administrator can invite and remove users of their own company only; and a test that the portal shows French or English and remembers the choice. From those, Lena Varga can decide to widen the pilot and can start to measure SM-04.

## 7. Dependencies

### 7.1 Order inside the .NET track

This release builds on `dotnet-r2` (customer data separation `EN-DN-10`, customer sign-in `US-DN-004`, the order detail `US-DN-008` and the language scaffold `EN-DN-12`) and on `dotnet-r1` (the invoice storage setting `EN-DN-07`). The product owner may change the order inside a release without changing any tag (A-43). The "Depends on" column names items of the .NET track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 36 | `US-DN-022` | Download the PDF invoice of a delivered order | `EN-DN-07`, `EN-DN-10`, `US-DN-008` |
| 37 | `US-DN-023` | Clear message when an invoice is not available | `US-DN-022`, `EN-DN-10` |
| 38 | `US-DN-024` | Customer administrator invites a user | `US-DN-004`, `EN-DN-10` |
| 39 | `US-DN-025` | Customer administrator removes a user | `US-DN-024`, `EN-DN-10` |
| 40 | `US-DN-026` | Use the portal in French or English | `EN-DN-12`, `EN-DN-10` |
| 41 | `US-DN-027` | The portal remembers my language | `US-DN-026`, `EN-DN-10` |

The ranks continue from `dotnet-r2` (ranks 11 to 35). The epic and three features are ranked with their children. All items are Should, so the order follows what each story builds on (source: backlog section 4.2).

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Reads invoices through a storage setting, not a fixed path. Assumes nothing about where Finance writes (`US-DN-022`, `FT-DN-17`). |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Uses the hosting-independent invoice and draft handling from `dotnet-r1` (`EP-DN-06`). |

Other OPEN items used here concern the .NET track only: OPEN-09, 14, 15, 27 and 33 (section 9). In each case the release states its working position in the item itself.

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | Section 4 (SM-04 timing) |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET | `EP-DN-06`, `FT-DN-17`, `US-DN-022` |
| OPEN-09 | 24 months of orders exist; where `Orders.InvoiceNumber` is filled; invoice year rule | Julien Moreau, Ahmed Benali | .NET | `FT-DN-17`, `US-DN-022`, `US-DN-023` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-14 | Dutch in the first release (business case OQ-02) | Sofie Peeters with Lena Varga | .NET | `FT-DN-19`, `US-DN-026`, `US-DN-027` |
| OPEN-15 | Customer administrators for all customers or only large ones (business case OQ-03) | Lena Varga | .NET | `FT-DN-18`, `US-DN-024`, `US-DN-025` |
| OPEN-19 | Hosting and database target the portal and modernised app run on (instance count, session state) | Ahmed Benali | Azure and .NET | `EP-DN-06` |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET | `US-DN-026` (section 11, difference 3) |
| OPEN-33 | How do the first customer users get an account and a link to their company in `dotnet-r2`, before the customer administrator feature (`dotnet-r3`) exists? Option: Northwind staff or IT create and link the accounts for the 20 pilot customers | Lena Varga with Ahmed Benali | .NET | `US-DN-024` |

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 10 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-dotnet` and `dotnet-r3` on every item. A query on the tag `dotnet-r3` lists the release. |
| GitHub | Issue labels `track-dotnet` and `dotnet-r3`, and the milestone `dotnet-r3`. |
| Jira | Labels `track-dotnet` and `dotnet-r3`, and the fix version `dotnet-r3`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). The Git tag `product/dotnet-r3` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | OPEN-19 is on the plan's list for this release and is stated in `EP-DN-06`, but no story of this release cites it in its own text. It is shown in section 7.2 with what the release does without the answer. | `EP-DN-06` |
| 2 | `US-DN-024` cites OPEN-33 (first customer accounts) and NFR-04. Neither is in the plan's description of this release. | `US-DN-024` |
| 3 | BR-11 is split across two releases: the scaffold `EN-DN-12` (Should) is in `dotnet-r2`, and the French and English texts are here. OPEN-27 asks which language pilot customers see in `dotnet-r2`. `US-DN-026` depends on `EN-DN-12`. | `EN-DN-12`, `US-DN-026`, `US-DN-027` |
| 4 | The PRD and plan describe `EP-DN-06` as having no enablers. The register agrees (0 enablers). The invoice storage setting that `US-DN-022` uses is an enabler of `dotnet-r1` (`EN-DN-07`). | `US-DN-022`, `EN-DN-07` |

## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. `dotnet-r2` is accepted (inside the .NET track). Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer.

**Definition of done.** The release is done when the acceptance criteria of its 10 items are met by tests and review only (ES-27):

* *Invoices.* A customer user of one company can download the PDF invoice of a delivered order of that company, and cannot reach the invoice of any other company. When the invoice is not available, the customer sees a clear message. Invoices are read through the storage setting. Nothing is assumed about where Finance writes, and the finance system is not changed (OPEN-06, OPEN-09).
* *Customer administrator.* A customer administrator can invite and remove users of their own company and of no other company. Until OPEN-15 is answered, Northwind staff set administrators for any customer.
* *Language.* A customer user can choose French or English and the portal remembers the choice. Dutch is not part of this release (OPEN-14).
* *Tests (ES-18).* `dotnet test src/Northwind.OrderDesk.sln` still passes on Windows, macOS and Linux. **The pricing tests keep their assertions and results (CS-20).** No assertion is weakened or removed.
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop (ES-27).** This file does not start or authorise any build, deployment or tag.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/dotnet-r3` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/dotnet-r3` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/dotnet-r3`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/dotnet-r3` is created on the commit that holds this file.**
