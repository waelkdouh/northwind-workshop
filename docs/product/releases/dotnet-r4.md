# Release dotnet-r4: Could items and measures (.NET track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D7 (ES-31) |
| Track | .NET, business area BA-02 Ordering and customer self-service |
| Release name | Could items and measures: shipped e-mail and success measures |
| Release tag | `dotnet-r4` |
| Track tag | `track-dotnet` |
| Git tag | `product/dotnet-r4`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/dotnet-r4 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | Not dated. **ASSUMPTION:** A-07 (no date is set for `dotnet-r4`). |
| Date of this file | 2026-10-30 |
| Items in this release | 11: 1 epic, 3 features, 1 enabler, 6 stories (section 3). Appendix A lists 9 further .NET items that are **not** part of this release or of any release. |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.7), `docs/product/business-requirements.md`, `docs/product/experiments.md` (`MVE-BA02`), `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-13 to ES-19, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is built, deployed, published, committed or tagged from it (ES-27). |

## 1. Words used

* **BA-02** is the business area "Ordering and customer self-service". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard. **P-** is a problem named in the business case.
* **Order Desk** is the internal web application staff use to enter and manage orders. **Portal** is the customer web site built in `dotnet-r2`. A **customer user** is a person at a customer company who signs in to the portal.
* **StockPilot** is the warehouse system in Antwerp. The **nightly import** reads the shipment file from StockPilot at 02:00 and updates Picking and Shipped (CS-10). It reads the shipment date and carrier but does not keep them today (A-20).
* **Shipped e-mail** is the message a customer user receives when an order changes to Shipped (BR-09). **SMTP** is the standard way to send e-mail; the **mail relay** is the internal server that forwards it (CS-12).
* **Success measures SM-01 to SM-04** are the four targets of the portal, each set "6 months after portal launch": share of orders placed through the portal (SM-01), "where is my order?" calls per week (SM-02), order lines needing correction after entry (SM-03) and invoice copy requests handled by staff per week (SM-04).
* **Enabler** is preparation work that must come before the features that use it. **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Customers receive an e-mail when an order is shipped, and the four portal success measures SM-01 to SM-04 are measured against their baselines. These are the Could items of the business case plus the measurement work (source: BR-09, SM-01, SM-02, SM-03, SM-04, CS-10).

The release builds on the portal order and status features of `dotnet-r2` and on the invoice download of `dotnet-r3` (inside the .NET track, section 7.1). BR-09 stays **partly covered** until a mail path is named (OPEN-18).

## 3. Items planned in this release

The list below is every item that carries the tags `track-dotnet` and `dotnet-r4`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `dotnet-r4`: 11 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1. The 9 items that carry only `track-dotnet` are **not** listed here. They are in Appendix A and are not part of this release.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-DN-07` | Epic | - | Notifications and measures | Could | `track-dotnet`, `dotnet-r4` | BR-09, SM-01, SM-02, SM-03, SM-04 |
| `FT-DN-20` | Feature | `EP-DN-07` | Keep shipment date and carrier | Could | `track-dotnet`, `dotnet-r4` | BR-09, CS-10 |
| `FT-DN-21` | Feature | `EP-DN-07` | Shipped e-mail | Could | `track-dotnet`, `dotnet-r4` | BR-09, CS-10, CS-12 |
| `FT-DN-22` | Feature | `EP-DN-07` | Measure the success measures | Could | `track-dotnet`, `dotnet-r4` | SM-01, SM-02, SM-03, SM-04 |
| `EN-DN-15` | Enabler | `FT-DN-20` | Store shipment date and carrier | Could | `track-dotnet`, `dotnet-r4` | BR-09, CS-10, C-03, ES-19 |
| `US-DN-028` | Story | `FT-DN-21` | Receive an e-mail when my order is shipped | Could | `track-dotnet`, `dotnet-r4` | BR-09, CS-10, CS-12 |
| `US-DN-029` | Story | `FT-DN-21` | The shipped e-mail is sent once and only to my company | Could | `track-dotnet`, `dotnet-r4` | BR-09, NFR-03 |
| `US-DN-030` | Story | `FT-DN-22` | Measure SM-01: share of orders placed through the portal | Could | `track-dotnet`, `dotnet-r4` | SM-01, BR-10 |
| `US-DN-031` | Story | `FT-DN-22` | Measure SM-02: "where is my order?" calls per week | Could | `track-dotnet`, `dotnet-r4` | SM-02, P-03 |
| `US-DN-032` | Story | `FT-DN-22` | Measure SM-03: order lines needing correction | Could | `track-dotnet`, `dotnet-r4` | SM-03, P-02 |
| `US-DN-033` | Story | `FT-DN-22` | Measure SM-04: invoice copy requests handled by staff | Could | `track-dotnet`, `dotnet-r4` | SM-04, P-05 |

Counts: 1 epic, 3 features, 1 enabler (`EN-DN-15`) and 6 stories (`US-DN-028` to `US-DN-033`). Total 11. All are priority Could.

## 4. Requirements covered

**Business requirement (BR-).**

| ID | What it says (short) | Priority | Source | Carried in this release by |
|---|---|---|---|---|
| BR-09 | A customer user receives an e-mail when an order changes to Shipped. | Could | BR-09, CS-10, CS-12 | `EN-DN-15` (keeps shipment date and carrier), `US-DN-028`, `US-DN-029`, `FT-DN-20`, `FT-DN-21`. **Partly covered** until a mail path is named (OPEN-18). |

**Quality targets (NFR-).** NFR-03 is cited by `US-DN-029`: the e-mail goes only to users of the same company and the mail service keeps data in the European Union. No NFR is carried as a main target of this release.

**Constraints (C-) that apply.** C-03 (StockPilot stays on premises and does not change; `EN-DN-15`), C-04 (mail service cost stays inside the EUR 1,500 ceiling, shared by both tracks, A-14) and C-05 (Order Desk stays the single source of truth). Of these, only C-03 is cited in an item's own source line (`EN-DN-15`).

**Success measures (SM-) moved.** This release takes the measures. Each target is "6 months after portal launch", and "portal launch" is OPEN-05.

| ID | Measure | Baseline | Target | Carried by |
|---|---|---|---|---|
| SM-01 | Share of orders placed through the portal | 0 % | 35 %, 6 months after portal launch | `US-DN-030` |
| SM-02 | "Where is my order?" calls per week | 410 | 250 or fewer, 6 months after portal launch | `US-DN-031` |
| SM-03 | Order lines needing correction after entry | 4.1 % | 2.5 % or fewer, 6 months after portal launch | `US-DN-032` |
| SM-04 | Invoice copy requests handled by staff per week | 120 | 40 or fewer, 6 months after portal launch | `US-DN-033` |

**ASSUMPTION:** A-46: a 35 % share (SM-01) is not expected to be reached with a pilot of 20 of about 1,150 customers. It depends on their order volume (OPEN-05). Where the numbers for SM-02, SM-03 and SM-04 come from, and how a correction is defined, is OPEN-31 (source: SM-01 to SM-04, CS-05).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| The portal order, status, invoice and sign-in features that the measures and the e-mail rely on | `dotnet-r2` and `dotnet-r3` (already planned there) |
| Replacing or sending through a new mail path, and any mail relay work | Not planned here. The Azure track replaces the relay only for the e-mail that CS-12 describes today. See OPEN-18. |
| Any change to StockPilot, and any change to the nightly exchange files | Out of scope (C-03). See OPEN-20. |
| A faster status refresh than the nightly 02:00 batch | Not planned. See OPEN-01 and OPEN-20. |
| Dutch, field-level audit, an Order Desk programming interface, status clarity options | Unplanned (track tag only). Listed in Appendix A. They are **not** part of this release. |
| Online payment, a native mobile app, replacing the finance system, customers recording claims themselves | Out of scope (business case section 6). |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Deploying or publishing anything from this workshop | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a record that the shipment date and carrier are kept when the nightly import runs, with the migration-impact check and decision record that ES-19 asks for; the content of a "shipped" e-mail, sent once per order and only to the users of that company, with a clear statement of whether a mail path exists; and four measurement reports for SM-01 to SM-04, each naming its data source and its definition. From those, Lena Varga can see whether the portal moves the four targets and which e-mail path is still open.

## 7. Dependencies

### 7.1 Order inside the .NET track

This release builds on the portal order and status features from `dotnet-r2` (`US-DN-011`, `US-DN-016`, `US-DN-017`), on the invoice download from `dotnet-r3` (`US-DN-022`) and on the modernised Order Desk from `dotnet-r1` (`EN-DN-01`). The product owner may change the order inside a release without changing any tag (A-43). The "Depends on" column names items of the .NET track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 42 | `EN-DN-15` | Store shipment date and carrier | `EN-DN-01` |
| 43 | `US-DN-028` | Receive an e-mail when my order is shipped | `EN-DN-15`, `US-DN-011`, `EN-DN-10` |
| 44 | `US-DN-029` | The shipped e-mail is sent once and only to my company | `US-DN-028`, `EN-DN-10` |
| 45 | `US-DN-030` | Measure SM-01: share of orders placed through the portal | `US-DN-017`, `EN-DN-10` |
| 46 | `US-DN-031` | Measure SM-02: "where is my order?" calls per week | `US-DN-011`, `EN-DN-10` |
| 47 | `US-DN-032` | Measure SM-03: order lines needing correction | `US-DN-016`, `EN-DN-10` |
| 48 | `US-DN-033` | Measure SM-04: invoice copy requests handled by staff | `US-DN-022`, `EN-DN-10` |

The ranks continue from `dotnet-r3` (ranks 36 to 41). The epic and three features are ranked with their children. The enabler comes before the e-mail it unblocks (source: backlog section 4.2).

**Effect of the experiment `MVE-BA02`.** The experiment tests whether a status view that is only as fresh as the 02:00 update is enough (A-06). If the result is "persevere", its call figures become the starting point for `US-DN-031`. If the result is "pivot", Lena Varga may decide to move the Shipped e-mail (`FT-DN-21`) to an earlier release. That is the product owner's decision. Nothing is changed here.

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Stores the shipment data and prepares the message content and the hand-off (`US-DN-028`, `US-DN-029`). Records BR-09 as partly covered until a mail path is named. |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Assumes the exchange files stay as they are. Runs a migration-impact check and records a decision (ES-19) before the new fields are stored (`EN-DN-15`). |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Used by `US-DN-030` and `US-DN-033`. Builds the measures so that the launch date is a setting, and does not assume a pilot environment. |

OPEN-05 is used by items in this release but is not in the plan's list of cross-track items for `dotnet-r4` (OPEN-18 and OPEN-20). It is shown here because `EP-DN-07`, `FT-DN-22`, `US-DN-030` and `US-DN-033` cite it (section 11, difference 1). Other OPEN items used here concern the .NET track only: OPEN-28, OPEN-29 and OPEN-31 (section 9).

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged. A-03, A-04, A-26, A-35 and A-36 are used by the items in Appendix A.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-20 | `ShippedAt` and `Carrier` must be stored for BR-09 | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-26 | The feature IDs `FT-AZ-01`..`FT-AZ-11` and `FT-DN-01`..`FT-DN-25` in PRD section 5 are the baseline for `backlog.md`. The backlog reuses them, may add new numbers, and never renumbers. The unplanned parent epic `EP-DN-08` is a proposed name | Lena Varga |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-33 | "Where is my order?" calls are unevenly spread across customers, so a group of about 10 heavier callers gives a baseline that can be measured. Most of these calls ask whether an order was received, picked or shipped. The call reasons are not recorded in the business case | Lena Varga |
| A-35 | The two status options in `FT-DN-26` (show the time each status last changed; explain Picking and Shipped in plain words) come from the pivot outcome of `MVE-BA02`. They are unplanned until the result is known. If the product owner plans them, the feature and its stories take the same track tag and the same release tag together (for example `dotnet-r2`) | Lena Varga |
| A-36 | The priorities of unplanned items are provisional: Dutch (BR-11) Should, field-level audit Could, status options Should, Order Desk API Could. The epic `EP-DN-08` takes the highest of them | Lena Varga |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) | Appendix A only: `FT-DN-26`, `US-DN-036`, `US-DN-037` |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET | `EP-DN-07`, `FT-DN-22`, `US-DN-030`, `US-DN-033` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-14 | Dutch in the first release (business case OQ-02) | Sofie Peeters with Lena Varga | .NET | Appendix A only: `FT-DN-23`, `US-DN-034` |
| OPEN-17 | Is the free-text audit action enough for NFR-08 or are field-level changes needed | Lena Varga | .NET | Appendix A only: `FT-DN-24`, `US-DN-035` |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET | `EP-DN-07`, `FT-DN-21`, `US-DN-028`, `US-DN-029` |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET | `EP-DN-07`, `FT-DN-20`, `EN-DN-15`. Appendix A: `FT-DN-26`, `US-DN-035` |
| OPEN-24 | Informational, BA-03: BA-03 will need an Order Desk API. BA-03 is out of scope; no release depends on it | Ahmed Benali | Informational only (neither track) | Appendix A only: `FT-DN-25` |
| OPEN-26 | Split `dotnet-r2` into a read-only slice and a reorder slice? | Lena Varga | .NET | Appendix A only: `US-DN-036` |
| OPEN-28 | Are "where is my order?" calls already counted by customer and by week (phone system or Order Desk records)? If not, who keeps the 4-week tally for `MVE-BA02`? | Lena Varga | .NET | `US-DN-031` |
| OPEN-29 | Which about 10 customers take part in `MVE-BA02`, who approves contacting them, and is a data-protection or consent step needed before sending a trial status e-mail? | Lena Varga with Sofie Peeters; data-protection check by Ahmed Benali | .NET | The experiment `MVE-BA02` (section 7.1); no item of this release depends on the answer |
| OPEN-31 | Where do the numbers for SM-02, SM-03 and SM-04 come from (call tally, "order line corrected after entry", invoice requests handled by staff), and how is a correction defined? The business case gives baselines but no record | Lena Varga | .NET | `US-DN-030`, `US-DN-031`, `US-DN-032`, `US-DN-033` |

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 11 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-dotnet` and `dotnet-r4` on every item. A query on the tag `dotnet-r4` lists the release. |
| GitHub | Issue labels `track-dotnet` and `dotnet-r4`, and the milestone `dotnet-r4`. |
| Jira | Labels `track-dotnet` and `dotnet-r4`, and the fix version `dotnet-r4`. |

The 9 unplanned items in Appendix A get the track label or tag `track-dotnet` only, and **no** milestone or fix version. Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). An enabler is published as a story whose title starts with its `EN-` ID. The Git tag `product/dotnet-r4` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | OPEN-05 (portal launch) is a cross-track item that `EP-DN-07`, `FT-DN-22`, `US-DN-030` and `US-DN-033` cite, but it is not in the plan's list for `dotnet-r4` (OPEN-18, OPEN-20). The backlog states it as "Other" in `EP-DN-07`. It is shown in section 7.2. | `EP-DN-07`, `FT-DN-22`, `US-DN-030`, `US-DN-033` |
| 2 | The measures are due "6 months after portal launch", but this release is not dated and "portal launch" is not defined (OPEN-05). The measurement stories can be built before any measurement is possible. **ASSUMPTION:** A-46: a 35 % share is not expected to be reached with 20 pilot customers. It depends on their order volume (OPEN-05). | `US-DN-030` to `US-DN-033`, SM-01 |
| 3 | Priority notes. `US-DN-030` is Could but cites BR-10, which is Must. `EP-DN-07` is Could by design. In Appendix A, `US-DN-036` and `US-DN-037` are Should but cite BR-04 (Must), and `US-DN-035` is Could but cites NFR-08. Priorities of unplanned items are provisional (A-36). | `US-DN-030`, `US-DN-035`, `US-DN-036`, `US-DN-037` |
| 4 | `FT-DN-25` (Order Desk API for reuse, Appendix A) is about BA-03, which is out of scope. It cites OPEN-24 as its only source and uses no BA-03 identifier as a source. The item is held back (unplanned, OPEN-24) and has no stories. | `FT-DN-25` |
| 5 | BR-09 is covered by three planned items but is only partly covered, because no mail-sending code is known in `src/` and the Azure relay work is a separate enabler (`EN-AZ-11`). | `EN-DN-15`, `US-DN-028`, `US-DN-029` |
| 6 | A-26 says the baseline feature IDs run `FT-DN-01` to `FT-DN-25`. The backlog adds `FT-DN-26` (status clarity options, Appendix A). A-26 allows new numbers, so this is informational. | `FT-DN-26` |

## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. `dotnet-r2` is accepted (inside the .NET track). Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer.

**Definition of done.** The release is done when the acceptance criteria of its 11 items are met by tests and review only (ES-27):

* *Shipment data.* A migration-impact check and a decision record (ES-19) exist before shipment date and carrier are stored. The nightly import files, cadence and paths are unchanged, and StockPilot is not changed (C-03, OPEN-20). The repeated "Shipped" rows are handled as the decision record says (A-19).
* *Shipped e-mail.* A message is prepared with the order number, the shipped date and the carrier, in the user's chosen language. It is sent once per order, only to users of that company (BR-09, NFR-03). Until a mail path is named, BR-09 is recorded as partly covered (OPEN-18).
* *Measures.* Four reports exist, one for each of SM-01 to SM-04. Each names its data source and its definition, including what counts as a correction for SM-03 (OPEN-31). Each shows the baseline from the business case next to the measured value.
* *Tests (ES-18).* `dotnet test src/Northwind.OrderDesk.sln` still passes on Windows, macOS and Linux. **The pricing tests keep their assertions and results (CS-20).** No assertion is weakened or removed.
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop (ES-27).** No e-mail is sent from this workshop. This file does not start or authorise any build, deployment or tag.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/dotnet-r4` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/dotnet-r4` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/dotnet-r4`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/dotnet-r4` is created on the commit that holds this file.**

## Appendix A. Unplanned items (track tag only, not in any release)

**These 9 items are not part of `dotnet-r4` and are not part of any release.** They carry only the track tag `track-dotnet` and no release tag (ES-31). They are listed here as a reference only and are not release content. The backlog (section 7, epic `EP-DN-08`, and the register in section 11) and the traceability file list them too. They are not counted in the 11 items of section 3, and they are not approved by approving this release. Each is held back because a decision or a result is missing. If the product owner plans one, the parent and its children take the same release tag together (A-35).

| ID | Type | Parent | Title | Priority (provisional, A-36) | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-DN-08` | Epic | - | Unplanned candidates (not in a release) | Should | `track-dotnet` | BR-11, NFR-08, BR-04, OQ-02 |
| `FT-DN-23` | Feature | `EP-DN-08` | Dutch language | Should | `track-dotnet` | BR-11, OQ-02 |
| `FT-DN-24` | Feature | `EP-DN-08` | Field-level order audit | Could | `track-dotnet` | NFR-08 |
| `FT-DN-25` | Feature | `EP-DN-08` | Order Desk API for reuse | Could | `track-dotnet` | none in knowledge-docs in scope; OPEN-24, informational |
| `FT-DN-26` | Feature | `EP-DN-08` | Status clarity options (only if `MVE-BA02` says pivot) | Should | `track-dotnet` | BR-04, CS-10, SM-02 |
| `US-DN-034` | Story | `FT-DN-23` | Use the portal in Dutch | Should | `track-dotnet` | BR-11, OQ-02 |
| `US-DN-035` | Story | `FT-DN-24` | See which field changed in an order | Could | `track-dotnet` | NFR-08 |
| `US-DN-036` | Story | `FT-DN-26` | See when each status last changed | Should | `track-dotnet` | BR-04, CS-10, SM-02 |
| `US-DN-037` | Story | `FT-DN-26` | Read Picking and Shipped in plain words | Should | `track-dotnet` | BR-04, CS-10, SM-02 |

Counts: 1 epic, 4 features, 0 enablers and 4 stories. Total 9.

| Why each is unplanned | Question that has to be answered first | Person |
|---|---|---|
| `FT-DN-23`, `US-DN-034` Dutch | Dutch in the first release (OPEN-14) | Sofie Peeters with Lena Varga |
| `FT-DN-24`, `US-DN-035` field-level audit | Is the free-text audit action enough, or are field-level changes needed (OPEN-17)? Any schema change also needs the migration-impact check (OPEN-20). | Lena Varga |
| `FT-DN-25` Order Desk API for reuse | Informational: BA-03 will need an Order Desk API. BA-03 is out of scope, no release depends on it, and no story is written (OPEN-24, A-03). | Ahmed Benali |
| `FT-DN-26`, `US-DN-036`, `US-DN-037` status clarity options | They come from the pivot outcome of `MVE-BA02`. Freshness is OPEN-01. A split of `dotnet-r2` is OPEN-26. | Lena Varga |
