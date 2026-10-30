# Northwind Traders — Traceability: Platform and data-centre exit (BA-01) and Ordering and customer self-service (BA-02)

| Field | Value |
|---|---|
| Document | Traceability, deliverable D5 |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`, releases `azure-r1` to `azure-r3`) and **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`, releases `dotnet-r1` to `dotnet-r4`). **BA-03** Delivery claims and credit notes is out of scope (section 6). |
| Product owner (proposed) | Lena Varga, Head of Customer Operations (A-29 in the backlog) |
| Builds on | `docs/product/backlog.md` (D4; its section 11 register is the authority for every item ID, track tag, release tag and priority), `docs/product/business-requirements.md` (D1) and `docs/product/product-requirements.md` (D2) |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01 to ES-07, ES-30, ES-31, ES-39). Requirement text and priorities come from the BRD, which quotes the business case. |
| Boundary | This is a planning document (ES-06). Nothing is published to a tracker, deployed, committed or tagged in Git (ES-27). No code, database script or infrastructure file is changed. |

How to read this document:

* **BR-** is a business requirement. **NFR-** is a non-functional requirement (a quality target such as speed or security). **C-** is a constraint. **SM-** is a success measure. **OQ-** is an open question from the business case. **BA-** is a business area. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **EP-** is an epic (a release theme), **FT-** a feature, **US-** a user story and **EN-** an enabler (preparation work that must come first; it is a story of type "Enabler"). All IDs are shown in `monospace`.
* Each item has one **track tag** (`track-azure` or `track-dotnet`). A planned item also has one **release tag** (`azure-r1` to `azure-r3`, `dotnet-r1` to `dotnet-r4`). An item with no release tag is **unplanned** (ES-30, ES-31).
* Priorities use MoSCoW: **Must**, **Should**, **Could**. The business case gives no priority to NFR items. They are treated as Must (A-12).
* **ASSUMPTION:** marks anything not in `knowledge-docs` and **OPEN:** marks an unanswered question. Both are listed with a named person in sections 9 and 10.

## 1. Scope statement

This table maps every in-scope requirement to the stories that cover it, so that nothing is lost between the business case and the work a team will build (ES-06).

| Business area | Name | Track | Identifiers in scope |
|---|---|---|---|
| **BA-01** | Platform and data-centre exit | Azure, `track-azure` | `BR-13`, `NFR-01`, `NFR-03`, `NFR-05`, `NFR-06`, `C-01`, `C-02`, `C-03`, `C-04`, `C-06`, `SM-07` |
| **BA-02** | Ordering and customer self-service | .NET, `track-dotnet` | `BR-01` to `BR-12`, `NFR-02`, `NFR-04`, `NFR-05`, `NFR-07`, `NFR-08`, `C-05`, `SM-01` to `SM-04`, `OQ-01` to `OQ-03` |
| Shared (both areas, A-02) | Cross-cutting requirements | One story per track | `NFR-03`, `NFR-04`, `NFR-05`; `C-04` is a shared cost ceiling (A-14) |

**In scope in total:** `BR-01` to `BR-13` (13 identifiers) and `NFR-01` to `NFR-08` (8 identifiers), which makes 21 requirement identifiers, plus `C-01` to `C-06`, `SM-01` to `SM-04`, `SM-07` and `OQ-01` to `OQ-03`.

**Out of scope:** **BA-03** Delivery claims and credit notes (`track-power-platform`) with its identifiers `BR-14`, `BR-15`, `BR-16`, `BR-17`, `BR-18`, `BR-19`, `NFR-09`, `C-07`, `C-08`, `SM-05` and `SM-06`. The full list is in section 6. No story in the backlog covers any of them.

## 2. How coverage was worked out

Coverage was **derived from the backlog, not typed from memory**. A script read the register in backlog section 11 (one row for each of the 133 items: 47 Azure and 86 .NET) and the item text in backlog sections 6 and 7. For each requirement it listed every story and enabler whose own `(source: ...)` line cites the requirement. Then it compared that list with the "Requirement coverage check" in backlog section 5.

| Word | Meaning in this document |
|---|---|
| **Covers** | The story or enabler cites the requirement ID in its own `(source: ...)` line in the backlog. This is the main evidence. |
| `†` | **Named by the backlog, not cited by the item.** Backlog section 5 lists the item as supporting the requirement (with the same `†`), but the item's own source line does not cite that ID. It is shown so that nothing the backlog claims is hidden. The item is a supporting item. |
| **Features** | The feature whose own source line cites the requirement. A feature groups the stories, so it shows where in the backlog to look. |
| **Covered** | At least one planned story or enabler (one that has a release tag) covers the requirement on that track. |
| **Partly covered** | Planned stories exist, but a named open question stops the requirement being met in full. |
| **Not covered** | No story or enabler covers the requirement. See section 4. |

Each story keeps the priority of the requirement it serves (backlog section 1.2). Priority and release are shown for every item in the lists below and again in Appendix A.

## 3. Traceability table

### 3.1 Business requirements BR-01 to BR-13

| ID | Requirement (short) | Area | Track tag | Requirement priority | Stories (`US-`): release, priority | Enablers (`EN-`): release, priority | Features (`FT-`): release | Status |
|---|---|---|---|---|---|---|---|---|
| `BR-01` | Customer user signs in and sees only their own company's orders | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-003`, `US-DN-004` | (`dotnet-r2`, Must) `EN-DN-10` | (`dotnet-r2`) `FT-DN-06`, `FT-DN-07` | Covered. Customer sign-in method is OPEN-13. |
| `BR-02` | List of the company's orders, last 24 months | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-006` | none | (`dotnet-r2`) `FT-DN-09` | Covered. |
| `BR-03` | Open an order: lines, quantities, prices, address, status | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-008`, `US-DN-020` | none | (`dotnet-r2`) `FT-DN-10`, `FT-DN-16` | Covered. |
| `BR-04` | Order status: one of six values, "always up to date" | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-011`, `US-DN-012`; (unplanned, Should (provisional)) `US-DN-036`, `US-DN-037` | none | (`dotnet-r2`) `FT-DN-11`; (unplanned) `FT-DN-26` | Covered, "as of the 02:00 batch" (A-04, OPEN-01). Two status-clarity stories are unplanned until `MVE-BA02` reports. |
| `BR-05` | Create a new order by copying a previous order | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-013`, `US-DN-014` | none | (`dotnet-r2`) `FT-DN-12` | Covered. |
| `BR-06` | A portal order appears in Order Desk without re-keying | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-016` | none | (`dotnet-r2`) `FT-DN-13` | Covered. |
| `BR-07` | Download the PDF invoice of a delivered order | BA-02 | `track-dotnet` | Should | (`dotnet-r3`, Should) `US-DN-022`, `US-DN-023` | none | (`dotnet-r3`) `FT-DN-17` | Covered. |
| `BR-08` | Customer administrator invites and removes users of their company | BA-02 | `track-dotnet` | Should | (`dotnet-r3`, Should) `US-DN-024`, `US-DN-025` | none | (`dotnet-r3`) `FT-DN-18` | Covered. |
| `BR-09` | E-mail to the customer when an order changes to Shipped | BA-02 | `track-dotnet` | Could | (`dotnet-r4`, Could) `US-DN-028`, `US-DN-029` | (`dotnet-r4`, Could) `EN-DN-15` | (`dotnet-r4`) `FT-DN-20`, `FT-DN-21` | Partly covered. Stories are planned, but the mail path is not named (OPEN-18). Same position as backlog section 5.1. |
| `BR-10` | Staff can see whether an order came from the portal or from staff | BA-02 | `track-dotnet` | Must | (`dotnet-r1`, Must) `US-DN-001`, `US-DN-002`; (`dotnet-r2`, Must) `US-DN-017`, `US-DN-018`; (`dotnet-r4`, Could) `US-DN-030` | (`dotnet-r2`, Must) `EN-DN-13` | (`dotnet-r1`) `FT-DN-04`; (`dotnet-r2`) `FT-DN-13` | Covered (staff view in `dotnet-r1`, portal stamp in `dotnet-r2`). |
| `BR-11` | Portal in French and English; Dutch requested | BA-02 | `track-dotnet` | Should | (`dotnet-r3`, Should) `US-DN-026`, `US-DN-027`; (unplanned, Should (provisional)) `US-DN-034` | (`dotnet-r2`, Should) `EN-DN-12` | (`dotnet-r2`) `FT-DN-15`; (`dotnet-r3`) `FT-DN-19`; (unplanned) `FT-DN-23` | Covered for French and English (`dotnet-r3`). Dutch is unplanned (OPEN-14). Which language pilot users see in `dotnet-r2` is OPEN-27. |
| `BR-12` | Portal shows each customer's negotiated prices | BA-02 | `track-dotnet` | Must | (`dotnet-r2`, Must) `US-DN-009`, `US-DN-015` | none | (`dotnet-r2`) `FT-DN-10`, `FT-DN-12` | Covered. |
| `BR-13` | Staff keep working through the move to Azure; downtime only in the Sunday window | BA-01 | `track-azure` | Must | (`azure-r2`, Must) `US-AZ-010`, `US-AZ-011`, `US-AZ-012`†, `US-AZ-013`, `US-AZ-014` | (`azure-r2`, Must) `EN-AZ-08`, `EN-AZ-09`†, `EN-AZ-10`†, `EN-AZ-13`, `EN-AZ-14`† | (`azure-r2`) `FT-AZ-05`, `FT-AZ-07`, `FT-AZ-09` | Covered. |

Reading the table: "(`dotnet-r2`, Must)" in front of a list of IDs means "these items are in release `dotnet-r2` and have priority Must". The `†` mark is explained in section 2. Priorities of unplanned items are provisional (A-36).

### 3.2 Non-functional requirements NFR-01 to NFR-08

| ID | Requirement (short) | Area | Track tag | Requirement priority | Stories (`US-`): release, priority | Enablers (`EN-`): release, priority | Features (`FT-`): release | Status |
|---|---|---|---|---|---|---|---|---|
| `NFR-01` | Availability 99.5 % in business hours, Monday to Saturday 06:00 to 20:00 CET | BA-01 | `track-azure` | Must (assumed, A-12) | (`azure-r2`, Must) `US-AZ-007` | (`azure-r1`, Must) `EN-AZ-05` | (`azure-r1`) `FT-AZ-03`; (`azure-r2`) `FT-AZ-05` | Covered. |
| `NFR-02` | Order list and detail pages respond in under 2 seconds for 95 % of requests | BA-02 | `track-dotnet` | Must (assumed, A-12) | (`dotnet-r2`, Must) `US-DN-007`, `US-DN-010` | none | (`dotnet-r2`) `FT-DN-09`, `FT-DN-10` | Covered. Measurement basis is OPEN-08. |
| `NFR-03` | Customer and order data stay in the EU | BA-01 | `track-azure` | Must (assumed, A-12) | (`azure-r2`, Must) `US-AZ-008` | (`azure-r1`, Must) `EN-AZ-01`; (`azure-r2`, Must) `EN-AZ-06`, `EN-AZ-08`, `EN-AZ-11` | (`azure-r1`) `FT-AZ-01`; (`azure-r2`) `FT-AZ-05` | Covered. Primary story for this track: see section 3.3. |
| `NFR-03` | Customer and order data stay in the EU | BA-02 | `track-dotnet` | Must (assumed, A-12) | (`dotnet-r2`, Must) `US-DN-005`; (`dotnet-r4`, Could) `US-DN-029` | (`dotnet-r2`, Must) `EN-DN-11` | (`dotnet-r2`) `FT-DN-08` | Covered. Primary story for this track: see section 3.3. |
| `NFR-04` | Customers sign in with an identity managed outside the application; staff use Entra ID | BA-01 | `track-azure` | Must (assumed, A-12) | none | none | none | No Azure story, by assumption A-02: **OPEN-13, no Azure story** (see section 4). |
| `NFR-04` | Customers sign in with an identity managed outside the application; staff use Entra ID | BA-02 | `track-dotnet` | Must (assumed, A-12) | (`dotnet-r2`, Must) `US-DN-004`; (`dotnet-r3`, Should) `US-DN-024` | (`dotnet-r2`, Must) `EN-DN-08`, `EN-DN-11` | (`dotnet-r2`) `FT-DN-05`, `FT-DN-07` | Covered. Customer sign-in and staff Entra sign-in. |
| `NFR-05` | No secret in source code or repository configuration files | BA-01 | `track-azure` | Must (assumed, A-12) | (`azure-r1`, Must) `US-AZ-003`; (`azure-r2`, Must) `US-AZ-006` | (`azure-r1`, Must) `EN-AZ-04`, `EN-AZ-07`; (`azure-r2`, Must) `EN-AZ-11` | (`azure-r1`) `FT-AZ-03`; (`azure-r2`) `FT-AZ-05` | Covered. Primary story for this track: see section 3.3. |
| `NFR-05` | No secret in source code or repository configuration files | BA-02 | `track-dotnet` | Must (assumed, A-12) | none | (`dotnet-r1`, Must) `EN-DN-05`, `EN-DN-09` | (`dotnet-r1`) `FT-DN-02` | Covered. Primary story for this track: see section 3.3. |
| `NFR-06` | Recovery point 1 hour, recovery time 4 hours for order data | BA-01 | `track-azure` | Must (assumed, A-12) | (`azure-r2`, Must) `US-AZ-009`; (`azure-r3`, Must) `US-AZ-018` | (`azure-r2`, Must) `EN-AZ-06` | (`azure-r2`) `FT-AZ-06`; (`azure-r3`) `FT-AZ-11` | Covered. |
| `NFR-07` | Portal meets WCAG 2.2 level AA | BA-02 | `track-dotnet` | Must (assumed, A-12) | (`dotnet-r2`, Must) `US-DN-020`, `US-DN-021` | (`dotnet-r2`, Must) `EN-DN-14` | (`dotnet-r2`) `FT-DN-16` | Covered. |
| `NFR-08` | Every change to an order recorded for 7 years | BA-02 | `track-dotnet` | Must (assumed, A-12) | (`dotnet-r2`, Must) `US-DN-018`, `US-DN-019`; (unplanned, Could (provisional)) `US-DN-035` | (`dotnet-r2`, Must) `EN-DN-13` | (`dotnet-r2`) `FT-DN-14`; (unplanned) `FT-DN-24` | Covered. Field-level detail is unplanned (OPEN-17). |

### 3.3 Cross-cutting requirements: one story per track

A story can carry only one track tag (ES-30). So `NFR-03`, `NFR-04` and `NFR-05` each have a story on each track that needs one (A-02). The table names the **primary** story on each track (the first story that meets the requirement on that track, as named in backlog section 5.3). Follow-on and other stories are in section 3.2.

| Requirement | Azure track: primary story | Azure track: other stories | .NET track: primary story | .NET track: other stories |
|---|---|---|---|---|
| `NFR-05`: No secrets (platform side / application side) | `EN-AZ-04` (`azure-r1`, Must) | `US-AZ-003` (`azure-r1`, Must), `EN-AZ-07` (`azure-r1`, Must), `US-AZ-006` (`azure-r2`, Must), `EN-AZ-11` (`azure-r2`, Must) | `EN-DN-05` (`dotnet-r1`, Must) | `EN-DN-09` (`dotnet-r1`, Must) |
| `NFR-03`: Data stays in the EU (regions, backups and logs / portal sign-in, mail and monitoring) | `EN-AZ-01` (`azure-r1`, Must) | `US-AZ-008` (`azure-r2`, Must), `EN-AZ-06` (`azure-r2`, Must), `EN-AZ-08` (`azure-r2`, Must), `EN-AZ-11` (`azure-r2`, Must) | `US-DN-005` (`dotnet-r2`, Must) | `EN-DN-11` (`dotnet-r2`, Must), `US-DN-029` (`dotnet-r4`, Could) |
| `NFR-04`: Sign-in (platform plumbing / customer sign-in and staff Entra sign-in) | **none.** OPEN-13, no Azure story (A-02) | none | `US-DN-004` (`dotnet-r2`, Must), `EN-DN-08` (`dotnet-r2`, Must) | `EN-DN-11` (`dotnet-r2`, Must), `US-DN-024` (`dotnet-r3`, Should) |

`NFR-06` is a BA-01 requirement only (business case section 4), so it has no BA-02 row. `NFR-06` (Azure) and `NFR-08` (.NET) are not split. They are linked only by OPEN-22 (7-year audit retention against recovery targets). `NFR-06` has Azure stories `EN-AZ-06` (`azure-r2`, Must), `US-AZ-009` (`azure-r2`, Must) and `US-AZ-018` (`azure-r3`, Must). No .NET story cites it; the .NET audit stories cite `NFR-08`.

## 4. Not covered

**Identifiers in scope with no story: none.** All 13 business requirements (`BR-01` to `BR-13`) and all 8 non-functional requirements (`NFR-01` to `NFR-08`) have at least one planned story or enabler (one with a release tag). No requirement is covered only by an unplanned item.

Four cases need a plain explanation, because a reader could mistake them for gaps:

| Case | What is true | How it is handled | Source |
|---|---|---|---|
| `NFR-04`, Azure side | The business case says customers sign in with an identity managed outside the application, and staff use Entra ID. Today the backlog gives all sign-in work to the .NET track. **There is no Azure story for NFR-04.** | By assumption **A-02**: an Azure story exists only if OPEN-03 (who modernises Order Desk code) or OPEN-13 (customer identity provider and platform sign-in plumbing) gives that plumbing to the Azure track. Until then the table shows **"OPEN-13, no Azure story"**. If it is assigned, the Azure track adds a story with the next free number (the story numbers run to 019 today, so the next is 020) in `azure-r1` or `azure-r2`. Nothing in the backlog waits for the answer. | (source: NFR-04, OQ-01, A-02, backlog section 5.3) |
| `BR-09` | Three planned items cover it (`EN-DN-15`, `US-DN-028`, `US-DN-029`, all `dotnet-r4`). The mail path that sends the "shipped" e-mail is not named, because no mail-sending code is known in `src/`, and replacing the Azure mail relay is a separate enabler (`EN-AZ-11`). | **Partly covered** until OPEN-18 is answered. It is a Could item. | (source: BR-09, CS-10, CS-12, A-20, OPEN-18) |
| `BR-11` | French and English are planned in `dotnet-r3`. Dutch is a separate story that is unplanned. | French and English are covered. Dutch (`US-DN-034`) is unplanned until OPEN-14 is answered. OPEN-27 asks which language pilot users see in `dotnet-r2`. | (source: BR-11, OQ-02, OPEN-14, OPEN-27) |
| `NFR-08` | Audit of order changes is planned in `dotnet-r2`. Recording which field changed is a separate story that is unplanned. | The free-text audit story is covered. Field-level audit (`US-DN-035`) is unplanned until OPEN-17 is answered. | (source: NFR-08, OPEN-17) |

Items that cover requirements but are **unplanned** (track tag only, no release): `US-DN-034`, `US-DN-035`, `US-DN-036`, `US-DN-037`. They are candidates held back by an open question. None of them is the only cover for an in-scope requirement.

## 5. Reverse view: success measures, constraints and open questions

This view starts from the measure or constraint and shows where it is carried. "Stories that cover it" are stories whose own source line cites it. For the success measures, "Other items that move it" are stories linked through the problem ID the measure comes from (P-01, P-02, P-03, P-05 in the business case), or the enabler that prepares `SM-07`. For constraints, enablers that cite the constraint are shown in their own column.

### 5.1 Success measures in scope (`SM-01` to `SM-04`, `SM-07`)

| ID | Measure | Area | Release(s) that carry it | Stories that cover it | Other items that move it | Target |
|---|---|---|---|---|---|---|
| `SM-01` | Share of orders placed through the portal | BA-02 | `dotnet-r2`, `dotnet-r4` | `US-DN-030` | Stories that make a portal order possible and that cite problem P-01: `US-DN-016` (`dotnet-r2`, Must). The measure is taken in `dotnet-r4`. "Portal launch" is not defined (OPEN-05); **ASSUMPTION:** A-46: a 35 % share is not expected to be reached with a pilot of 20 customers out of about 1,150. It depends on their order volume (OPEN-05, BRD section 2.2). | 0 % now; 35 %, 6 months after portal launch |
| `SM-02` | "Where is my order?" calls per week | BA-02 | `dotnet-r2`, `dotnet-r4` | `US-DN-012`, `US-DN-031`, `US-DN-036` (unplanned), `US-DN-037` (unplanned) | Stories that show order status and cite problem P-03: `US-DN-006` (`dotnet-r2`, Must), `US-DN-008` (`dotnet-r2`, Must), `US-DN-011` (`dotnet-r2`, Must). Status clarity options `US-DN-036` and `US-DN-037` are unplanned until `MVE-BA02` reports. The measure is taken in `dotnet-r4`. | 410 now; 250 or fewer, 6 months after portal launch |
| `SM-03` | Order lines needing correction after entry | BA-02 | `dotnet-r2`, `dotnet-r4` | `US-DN-032` | Stories that cut re-keying and cite problem P-02: `US-DN-014` (`dotnet-r2`, Must), `US-DN-016` (`dotnet-r2`, Must). The measure is taken in `dotnet-r4`. | 4.1 % now; 2.5 % or fewer, 6 months after portal launch |
| `SM-04` | Invoice copy requests handled by staff per week | BA-02 | `dotnet-r3`, `dotnet-r4` | `US-DN-033` | Invoice download stories that cite problem P-05: `US-DN-022` (`dotnet-r3`, Should), `US-DN-023` (`dotnet-r3`, Should). The measure is taken in `dotnet-r4`. | 120 now; 40 or fewer, 6 months after portal launch |
| `SM-07` | Production servers past end of support | BA-01 | `azure-r2`, `azure-r3` | `US-AZ-015`, `US-AZ-016` | Enabler `EN-AZ-13` (`azure-r2`, Must) prepares the retirement. Release `azure-r3` retires the two old servers. Whether the file server `NWFS01` counts is OPEN-12. | 2 now; 0 by 30 June 2027 |

Where the numbers for `SM-02`, `SM-03` and `SM-04` come from is OPEN-31.

### 5.2 Constraints in scope (`C-01` to `C-06`)

| ID | Constraint | Track | Release(s) that carry it | Stories that cover it | Enablers that cover it |
|---|---|---|---|---|---|
| `C-01` | Data-centre lease ends 30 June 2027 | Azure | `azure-r1`, `azure-r2`, `azure-r3` | `US-AZ-013`, `US-AZ-014`, `US-AZ-015` | `EN-AZ-01`, `EN-AZ-08`, `EN-AZ-13` |
| `C-02` | Windows Server 2012 R2 and SQL Server 2014 are past end of support | Azure | `azure-r1`, `azure-r3` | `US-AZ-004`, `US-AZ-015`, `US-AZ-016` | `EN-AZ-03` |
| `C-03` | StockPilot stays on premises and does not change | Azure | `azure-r1`, `azure-r2`, `dotnet-r2`, `dotnet-r4` | `US-AZ-001`, `US-AZ-002`, `US-AZ-003`, `US-AZ-005`, `US-AZ-012`, `US-DN-012` | `EN-AZ-09`, `EN-AZ-14`, `EN-DN-15` |
| `C-04` | Azure run cost at most EUR 1,500 per month (shared by both tracks, A-14) | Shared | `azure-r1`, `azure-r3`, `dotnet-r2` | `US-AZ-004`, `US-AZ-017` | `EN-AZ-03`, `EN-AZ-12`, `EN-DN-11` |
| `C-05` | The portal reuses Order Desk as the single source of truth for orders | .NET | `dotnet-r2` | `US-DN-003`, `US-DN-009`, `US-DN-015`, `US-DN-016` | `EN-DN-10`, `EN-DN-11` |
| `C-06` | Small IT team; no Kubernetes | Azure | `azure-r1`, `azure-r3` | `US-AZ-019` | `EN-AZ-03`, `EN-AZ-12` |

`C-01` is also carried by the release order itself: the three Azure releases are fixed by the 30 June 2027 lease end, and one spare Sunday window stays free before it (`US-AZ-013`, `US-AZ-014`). `C-04` (EUR 1,500 per month) is shared by both tracks (A-14); who is accountable and how it is split is OPEN-04. `C-06` is also stated in the hosting decision record `EN-AZ-03`: platform services only, no Kubernetes (ES-21).

### 5.3 Open questions from the business case in scope (`OQ-01` to `OQ-03`)

| ID | Question | Area | Release(s) | Stories that cover it | Enablers that cover it |
|---|---|---|---|---|---|
| `OQ-01` | Which identity provider do customer users sign in with? | BA-02 | `dotnet-r2` | `US-DN-004` | `EN-DN-11` |
| `OQ-02` | Is Dutch needed in the first release? | BA-02 | `dotnet-r3` | `US-DN-026`, `US-DN-027`, `US-DN-034` (unplanned) | none |
| `OQ-03` | Customer administrators for all customers or only large ones? | BA-02 | `dotnet-r3` | `US-DN-024`, `US-DN-025` | none |

These questions are carried as OPEN items: `OQ-01` is OPEN-13, `OQ-02` is OPEN-14 and `OQ-03` is OPEN-15.

## 6. Out of scope (BA-03 and exclusions)

**Business area BA-03 Delivery claims and credit notes (`track-power-platform`)** is out of scope. Its identifiers are listed here so that nothing is lost (ES-06). No backlog item cites any of them as a source.

| Kind | Identifiers |
|---|---|
| Business requirements | `BR-14`, `BR-15`, `BR-16`, `BR-17`, `BR-18`, `BR-19` |
| Non-functional requirement | `NFR-09` (claim decisions kept 7 years) |
| Constraints | `C-07`, `C-08` |
| Success measures | `SM-05`, `SM-06` |
| Problem | `P-06` (delivery claims handled in a spreadsheet and by e-mail) |
| Open questions | `OQ-04`, `OQ-05` (informational only) |
| Current-state facts | `CS-24` to `CS-28` |
| Standards for Power Platform | `ES-32` to `ES-37` |
| Timeline item | Delivery claims pilot in Q1 2027 (business case section 8) |

Business case section 6 also excludes, for the first release: online payment, a native mobile app, changes to StockPilot, replacing the finance system, and customers recording claims themselves. No story covers them.

`NFR-03` and `NFR-04` are shared with BA-03. They are in scope here only for BA-01 and BA-02.

**OPEN:** OPEN-24 (informational). BA-03 will need an Order Desk programming interface (API). No release depends on it. The backlog holds `FT-DN-25` as an unplanned feature **without stories**, and no story is written for it.

## 7. Counts per release

Counts come from the register in backlog section 11 and agree with backlog section 3.1. A release tag of `-` in the register means unplanned.

| Track | Release | Epics | Features | Enablers | Stories | Total items | BR and NFR covered directly by its stories and enablers |
|---|---|---|---|---|---|---|---|
| `track-azure` | `azure-r1` | 1 | 4 | 7 | 5 | 17 | `NFR-01`, `NFR-03`, `NFR-05` |
| `track-azure` | `azure-r2` | 1 | 5 | 7 | 9 | 22 | `BR-13`, `NFR-01`, `NFR-03`, `NFR-05`, `NFR-06` |
| `track-azure` | `azure-r3` | 1 | 2 | 0 | 5 | 8 | `NFR-06` |
| `track-dotnet` | `dotnet-r1` | 1 | 4 | 8 | 2 | 15 | `BR-10`, `NFR-05` |
| `track-dotnet` | `dotnet-r2` | 4 | 12 | 6 | 19 | 41 | `BR-01`, `BR-02`, `BR-03`, `BR-04`, `BR-05`, `BR-06`, `BR-10`, `BR-11`, `BR-12`, `NFR-02`, `NFR-03`, `NFR-04`, `NFR-07`, `NFR-08` |
| `track-dotnet` | `dotnet-r3` | 1 | 3 | 0 | 6 | 10 | `BR-07`, `BR-08`, `BR-11`, `NFR-04` |
| `track-dotnet` | `dotnet-r4` | 1 | 3 | 1 | 6 | 11 | `BR-09`, `BR-10`, `NFR-03` |
| `track-dotnet` | unplanned (track tag only) | 1 | 4 | 0 | 4 | 9 | `BR-04`, `BR-11`, `NFR-08` |
| **`track-azure` total** | | **3** | **11** | **14** | **19** | **47** | |
| **`track-dotnet` total** | | **8** | **26** | **15** | **37** | **86** | |
| **Both tracks** | | **11** | **37** | **29** | **56** | **133** | |

* Planned items: 124 (47 Azure and 77 .NET). Unplanned: 9, all .NET (1 epic, 4 features and 4 stories, as `EP-DN-08` and its children).
* Release count is 3 for Azure and 4 for .NET, as fixed in the plan. All seven releases were approved on 2026-10-30. Each Git tag (`product/azure-r1` and so on) is created on the commit that holds the approved files.
* A requirement is "covered by a release" when one of that release's stories or enablers cites it. `BR-10` appears in `dotnet-r1`, `dotnet-r2` and `dotnet-r4`; `NFR-01`, `NFR-03`, `NFR-05` and `NFR-06` appear in more than one Azure release; this is a follow-on pattern, not a double count (one item has exactly one release tag).

## 8. Checks run and notes for the product owner

### 8.1 Checks that passed

| # | Check | Result |
|---|---|---|
| 1 | Register in backlog section 11 against the item text in sections 6 and 7: type, parent, title, track tag, release tag, priority, status and source identifiers for all 133 items | All agree. No item is missing on either side. |
| 2 | Every `EP-`, `FT-`, `US-` and `EN-` ID cited anywhere in the backlog, and every ID in this file, exists in the register | Yes. No unknown ID. |
| 3 | Exactly one track tag per item. A planned item has one release tag of the same track. An unplanned item has none. Parent and child share track and release. Parent types are right (feature under epic, story or enabler under feature) | Yes for all 133 items. |
| 4 | Every `BR-01` to `BR-13` and `NFR-01` to `NFR-08` has at least one planned story or enabler | Yes (section 4). |
| 5 | `NFR-03` and `NFR-05` have a story on each track; `NFR-04` has a .NET story and no Azure story by A-02 | Yes (section 3.3). |
  | 6 | Dependencies: "Depends on" and "Enables" lines name items of the same track only; no item depends on an item in a later release; no enabler enables an item in an earlier release | Yes. No cross-track dependency and no release-order break. |
| 7 | PRD section 8: the release of every epic, feature and enabler ID it names, against the register | All 72 IDs agree. Every planned epic, feature and enabler appears in the PRD. The PRD names no `US-` story, so story-to-release agreement can only be checked against the backlog. |
| 8 | No out-of-scope identifier (`BR-14` to `BR-19`, `NFR-09`, `C-07`, `C-08`, `SM-05`, `SM-06`, `OQ-04`, `OQ-05`, `CS-24` to `CS-28`, `ES-32` to `ES-37`) is cited as a source by any item | Yes. A script checked every register row and item block of the backlog and the other documents. These identifiers appear only in the out-of-scope lists. `FT-DN-25` cites OPEN-24 only, and OPEN-24 is informational (BA-03). |

### 8.2 Small differences between the backlog and the item text, and how they were settled

None of these left a requirement uncovered. Backlog section 5 and section 5.4 were corrected in the consistency pass, so they now agree with the item source lines. Differences that are still open are in the table. The settled ones are listed after it.

| # | Difference | Items |
|---|---|---|
| 1 | Backlog section 5.1 lists items as supporting `BR-13` (marked `†` there and here), but the item's own source line does not cite it. This is intended. Supporting items are shown so that nothing the backlog claims is hidden. | `BR-13`: `EN-AZ-09`, `EN-AZ-10`, `EN-AZ-14`, `US-AZ-012` |
| 2 | A measure story or provisional story has a lower priority than the requirement it cites. This is informational only: `EP-DN-07` is Could, and priorities of unplanned items are provisional (A-36). | `US-DN-030` (Could, cites `BR-10`, Must); `US-DN-035` (Could, cites `NFR-08`); `US-DN-036` and `US-DN-037` (Should, cite `BR-04`, Must) |

Settled in the consistency pass: `US-DN-007` and `US-DN-010` cite only `NFR-02`, so they are no longer listed for `BR-02` and `BR-03`. The items whose source line cites `BR-03`, `BR-10`, `NFR-03`, `NFR-04` and `NFR-05` are now in backlog section 5. `US-AZ-004` is no longer listed for `C-03` and `EN-DN-11` is no longer listed for `C-06` in backlog section 5.4. `US-DN-019` cites only `NFR-08`; `NFR-06` is Azure only and is linked to `NFR-08` by OPEN-22 only.

## 9. Assumptions (ES-03)

Every assumption has a person who can confirm it. Wording is identical to the backlog and the other product documents. This table lists only the assumptions used in this document. Assumptions A-02, A-12, A-14, A-16 and A-36 hold the rules this file depends on most.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-02 | NFR-03, NFR-04 and NFR-05 are cross-cutting: one story per track, both shown in the traceability table. Exception: NFR-04 gets an Azure story only if `OPEN-03` or `OPEN-13` assigns platform sign-in plumbing to Azure; until then the traceability table shows the Azure side as "OPEN-13, no Azure story" | Lena Varga |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-20 | `ShippedAt` and `Carrier` must be stored for BR-09 | Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-36 | The priorities of unplanned items are provisional: Dutch (BR-11) Should, field-level audit Could, status options Should, Order Desk API Could. The epic `EP-DN-08` takes the highest of them | Lena Varga |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 10. OPEN items (ES-04)

Wording is identical to the backlog and the other product documents. None blocks this document. Only the OPEN items used here are listed.

| ID | OPEN question or dependency | Person who can answer | Track(s) affected |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET |
| OPEN-08 | NFR measurement bases (NFR-01, NFR-02, NFR-08) | Lena Varga | Azure and .NET |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET |
| OPEN-14 | Dutch in the first release (business case OQ-02) | Sofie Peeters with Lena Varga | .NET |
| OPEN-15 | Customer administrators for all customers or only large ones (business case OQ-03) | Lena Varga | .NET |
| OPEN-17 | Is the free-text audit action enough for NFR-08 or are field-level changes needed | Lena Varga | .NET |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET |
| OPEN-24 | Informational, BA-03: BA-03 will need an Order Desk API. BA-03 is out of scope; no release depends on it | Ahmed Benali | Informational only (neither track) |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET |
| OPEN-31 | Where do the numbers for SM-02, SM-03 and SM-04 come from (call tally, "order line corrected after entry", invoice requests handled by staff), and how is a correction defined? The business case gives baselines but no record | Lena Varga | .NET |

## Appendix A. Every story and enabler with its tags

One row for each of the 29 enablers and 56 stories in the backlog register, in track order and then release order. "Covers" lists the `BR-` and `NFR-` identifiers in the item's own source line. "Other" lists `C-`, `SM-` and `OQ-` identifiers from the same line. A dash means none.

| ID | Type | Title | Feature | Track tag | Release tag | Priority | Covers (BR, NFR) | Other (C, SM, OQ) |
|---|---|---|---|---|---|---|---|---|
| `EN-AZ-01` | Enabler | Azure foundation: region, names, tags, Bicep, `tst` and `prd` | `FT-AZ-01` | `track-azure` | `azure-r1` | Must | `NFR-03` | `C-01` |
| `EN-AZ-02` | Enabler | Network foundation and private endpoints | `FT-AZ-01` | `track-azure` | `azure-r1` | Must | - | - |
| `EN-AZ-03` | Enabler | Hosting and data decision record | `FT-AZ-02` | `track-azure` | `azure-r1` | Must | - | `C-02`, `C-04`, `C-06` |
| `EN-AZ-04` | Enabler | Secrets and managed identity on `tst` | `FT-AZ-03` | `track-azure` | `azure-r1` | Must | `NFR-05` | - |
| `EN-AZ-05` | Enabler | Observability baseline on `tst` | `FT-AZ-03` | `track-azure` | `azure-r1` | Must | `NFR-01` | - |
| `EN-AZ-07` | Enabler | Infrastructure pipeline | `FT-AZ-01` | `track-azure` | `azure-r1` | Must | `NFR-05` | - |
| `EN-AZ-12` | Enabler | Cost model | `FT-AZ-02` | `track-azure` | `azure-r1` | Must | - | `C-04`, `C-06` |
| `US-AZ-001` | Story | Prove the nightly order file is identical | `FT-AZ-04` | `track-azure` | `azure-r1` | Must | - | `C-03` |
| `US-AZ-002` | Story | Prove the shipment file gives the same result | `FT-AZ-04` | `track-azure` | `azure-r1` | Must | - | `C-03` |
| `US-AZ-003` | Story | Confirm the Antwerp file-transfer details in writing | `FT-AZ-04` | `track-azure` | `azure-r1` | Must | `NFR-05` | `C-03` |
| `US-AZ-004` | Story | Record which server features the proof needed | `FT-AZ-04` | `track-azure` | `azure-r1` | Must | - | `C-04`, `C-02` |
| `US-AZ-005` | Story | Record the `MVE-BA01` outcome and its effect | `FT-AZ-04` | `track-azure` | `azure-r1` | Must | - | `C-03` |
| `EN-AZ-06` | Enabler | Backup, disaster recovery and restore method | `FT-AZ-06` | `track-azure` | `azure-r2` | Must | `NFR-06`, `NFR-03` | - |
| `EN-AZ-08` | Enabler | Database migration method and rehearsal | `FT-AZ-07` | `track-azure` | `azure-r2` | Must | `BR-13`, `NFR-03` | `C-01` |
| `EN-AZ-09` | Enabler | StockPilot exchange redesign | `FT-AZ-08` | `track-azure` | `azure-r2` | Must | - | `C-03` |
| `EN-AZ-10` | Enabler | Invoice store migration | `FT-AZ-07` | `track-azure` | `azure-r2` | Must | - | - |
| `EN-AZ-11` | Enabler | SMTP relay replacement | `FT-AZ-08` | `track-azure` | `azure-r2` | Must | `NFR-05`, `NFR-03` | - |
| `EN-AZ-13` | Enabler | Cutover runbook and rollback plan | `FT-AZ-09` | `track-azure` | `azure-r2` | Must | `BR-13` | `C-01`, `SM-07` |
| `EN-AZ-14` | Enabler | Hybrid connectivity to Antwerp | `FT-AZ-05` | `track-azure` | `azure-r2` | Must | - | `C-03` |
| `US-AZ-006` | Story | No secrets in production | `FT-AZ-05` | `track-azure` | `azure-r2` | Must | `NFR-05` | - |
| `US-AZ-007` | Story | Production monitoring and availability probe | `FT-AZ-05` | `track-azure` | `azure-r2` | Must | `NFR-01` | - |
| `US-AZ-008` | Story | Production data, backups and logs stay in the EU | `FT-AZ-05` | `track-azure` | `azure-r2` | Must | `NFR-03` | - |
| `US-AZ-009` | Story | Tested restore meets RPO and RTO | `FT-AZ-06` | `track-azure` | `azure-r2` | Must | `NFR-06` | - |
| `US-AZ-010` | Story | Order data is identical after the move | `FT-AZ-07` | `track-azure` | `azure-r2` | Must | `BR-13` | - |
| `US-AZ-011` | Story | Invoice PDFs are available in Azure | `FT-AZ-07` | `track-azure` | `azure-r2` | Must | `BR-13` | - |
| `US-AZ-012` | Story | The nightly exchange runs from Azure | `FT-AZ-08` | `track-azure` | `azure-r2` | Must | - | `C-03` |
| `US-AZ-013` | Story | Rehearse the cutover and rollback in the Sunday window | `FT-AZ-09` | `track-azure` | `azure-r2` | Must | `BR-13` | `C-01` |
| `US-AZ-014` | Story | Cut over production inside the Sunday window | `FT-AZ-09` | `track-azure` | `azure-r2` | Must | `BR-13` | `C-01` |
| `US-AZ-015` | Story | Retire the old web and database servers | `FT-AZ-10` | `track-azure` | `azure-r3` | Must | - | `SM-07`, `C-01`, `C-02` |
| `US-AZ-016` | Story | Decide whether the file server counts and report SM-07 | `FT-AZ-10` | `track-azure` | `azure-r3` | Must | - | `SM-07`, `C-02` |
| `US-AZ-017` | Story | Closing cost check against the ceiling | `FT-AZ-11` | `track-azure` | `azure-r3` | Must | - | `C-04` |
| `US-AZ-018` | Story | Recovery test and report on production | `FT-AZ-11` | `track-azure` | `azure-r3` | Must | `NFR-06` | - |
| `US-AZ-019` | Story | Runbooks the IT team can follow | `FT-AZ-11` | `track-azure` | `azure-r3` | Must | - | `C-06` |
| `EN-DN-01` | Enabler | SDK-style projects on `net10.0` | `FT-DN-01` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-02` | Enabler | Tests pass on Windows, macOS and Linux | `FT-DN-01` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-03` | Enabler | Configuration through options | `FT-DN-02` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-04` | Enabler | Logging through `ILogger<T>` | `FT-DN-02` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-05` | Enabler | No secrets and no Windows-sign-in database connection | `FT-DN-02` | `track-dotnet` | `dotnet-r1` | Must | `NFR-05` | - |
| `EN-DN-06` | Enabler | Draft order kept outside one server's memory | `FT-DN-03` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-07` | Enabler | Invoice storage setting instead of a fixed network path | `FT-DN-03` | `track-dotnet` | `dotnet-r1` | Must | - | - |
| `EN-DN-09` | Enabler | Build and test pipeline | `FT-DN-01` | `track-dotnet` | `dotnet-r1` | Must | `NFR-05` | - |
| `US-DN-001` | Story | Staff see the order channel | `FT-DN-04` | `track-dotnet` | `dotnet-r1` | Must | `BR-10` | - |
| `US-DN-002` | Story | Staff filter orders by channel | `FT-DN-04` | `track-dotnet` | `dotnet-r1` | Must | `BR-10` | - |
| `EN-DN-08` | Enabler | Staff sign-in with Microsoft Entra ID | `FT-DN-07` | `track-dotnet` | `dotnet-r2` | Must | `NFR-04` | - |
| `EN-DN-10` | Enabler | Customer data separation (tenant isolation) | `FT-DN-06` | `track-dotnet` | `dotnet-r2` | Must | `BR-01` | `C-05` |
| `EN-DN-11` | Enabler | Portal architecture and sign-in decision record | `FT-DN-05` | `track-dotnet` | `dotnet-r2` | Must | `NFR-04`, `NFR-03` | `OQ-01`, `C-04`, `C-05` |
| `EN-DN-12` | Enabler | Localisation scaffold | `FT-DN-15` | `track-dotnet` | `dotnet-r2` | Should | `BR-11` | - |
| `EN-DN-13` | Enabler | Audit completeness | `FT-DN-14` | `track-dotnet` | `dotnet-r2` | Must | `NFR-08`, `BR-10` | - |
| `EN-DN-14` | Enabler | Accessibility baseline (WCAG 2.2 AA) | `FT-DN-16` | `track-dotnet` | `dotnet-r2` | Must | `NFR-07` | - |
| `US-DN-003` | Story | Customer user sees only their own company | `FT-DN-06` | `track-dotnet` | `dotnet-r2` | Must | `BR-01` | `C-05` |
| `US-DN-004` | Story | Customer user signs in | `FT-DN-07` | `track-dotnet` | `dotnet-r2` | Must | `BR-01`, `NFR-04` | `OQ-01` |
| `US-DN-005` | Story | Portal sign-in, mail and monitoring keep data in the EU | `FT-DN-08` | `track-dotnet` | `dotnet-r2` | Must | `NFR-03` | - |
| `US-DN-006` | Story | See my company's orders from the last 24 months | `FT-DN-09` | `track-dotnet` | `dotnet-r2` | Must | `BR-02` | - |
| `US-DN-007` | Story | The order list responds in under 2 seconds | `FT-DN-09` | `track-dotnet` | `dotnet-r2` | Must | `NFR-02` | - |
| `US-DN-008` | Story | Open an order and see its details | `FT-DN-10` | `track-dotnet` | `dotnet-r2` | Must | `BR-03` | - |
| `US-DN-009` | Story | See my negotiated prices on an order | `FT-DN-10` | `track-dotnet` | `dotnet-r2` | Must | `BR-12` | `C-05` |
| `US-DN-010` | Story | The order detail responds in under 2 seconds | `FT-DN-10` | `track-dotnet` | `dotnet-r2` | Must | `NFR-02` | - |
| `US-DN-011` | Story | See one of six statuses on an order | `FT-DN-11` | `track-dotnet` | `dotnet-r2` | Must | `BR-04` | - |
| `US-DN-012` | Story | Understand how fresh the status is | `FT-DN-11` | `track-dotnet` | `dotnet-r2` | Must | `BR-04` | `C-03`, `SM-02` |
| `US-DN-013` | Story | Start a new order by copying a previous order | `FT-DN-12` | `track-dotnet` | `dotnet-r2` | Must | `BR-05` | - |
| `US-DN-014` | Story | Change quantities and remove lines before submitting | `FT-DN-12` | `track-dotnet` | `dotnet-r2` | Must | `BR-05` | - |
| `US-DN-015` | Story | See my prices on the draft order | `FT-DN-12` | `track-dotnet` | `dotnet-r2` | Must | `BR-12` | `C-05` |
| `US-DN-016` | Story | Submit the order and see it in Order Desk as Received | `FT-DN-13` | `track-dotnet` | `dotnet-r2` | Must | `BR-06` | `C-05` |
| `US-DN-017` | Story | The server marks portal orders with the Portal channel | `FT-DN-13` | `track-dotnet` | `dotnet-r2` | Must | `BR-10` | - |
| `US-DN-018` | Story | Every order change records who, what, when and channel | `FT-DN-14` | `track-dotnet` | `dotnet-r2` | Must | `NFR-08`, `BR-10` | - |
| `US-DN-019` | Story | Audit records are kept for 7 years | `FT-DN-14` | `track-dotnet` | `dotnet-r2` | Must | `NFR-08` | - |
| `US-DN-020` | Story | Use the portal with keyboard and screen reader | `FT-DN-16` | `track-dotnet` | `dotnet-r2` | Must | `NFR-07`, `BR-03` | - |
| `US-DN-021` | Story | Read the portal with enough contrast, zoom and clear errors | `FT-DN-16` | `track-dotnet` | `dotnet-r2` | Must | `NFR-07` | - |
| `US-DN-022` | Story | Download the PDF invoice of a delivered order | `FT-DN-17` | `track-dotnet` | `dotnet-r3` | Should | `BR-07` | - |
| `US-DN-023` | Story | Clear message when an invoice is not available | `FT-DN-17` | `track-dotnet` | `dotnet-r3` | Should | `BR-07` | - |
| `US-DN-024` | Story | Customer administrator invites a user | `FT-DN-18` | `track-dotnet` | `dotnet-r3` | Should | `BR-08`, `NFR-04` | `OQ-03` |
| `US-DN-025` | Story | Customer administrator removes a user | `FT-DN-18` | `track-dotnet` | `dotnet-r3` | Should | `BR-08` | `OQ-03` |
| `US-DN-026` | Story | Use the portal in French or English | `FT-DN-19` | `track-dotnet` | `dotnet-r3` | Should | `BR-11` | `OQ-02` |
| `US-DN-027` | Story | The portal remembers my language | `FT-DN-19` | `track-dotnet` | `dotnet-r3` | Should | `BR-11` | `OQ-02` |
| `EN-DN-15` | Enabler | Store shipment date and carrier | `FT-DN-20` | `track-dotnet` | `dotnet-r4` | Could | `BR-09` | `C-03` |
| `US-DN-028` | Story | Receive an e-mail when my order is shipped | `FT-DN-21` | `track-dotnet` | `dotnet-r4` | Could | `BR-09` | - |
| `US-DN-029` | Story | The shipped e-mail is sent once and only to my company | `FT-DN-21` | `track-dotnet` | `dotnet-r4` | Could | `BR-09`, `NFR-03` | - |
| `US-DN-030` | Story | Measure SM-01: share of orders placed through the portal | `FT-DN-22` | `track-dotnet` | `dotnet-r4` | Could | `BR-10` | `SM-01` |
| `US-DN-031` | Story | Measure SM-02: "where is my order?" calls per week | `FT-DN-22` | `track-dotnet` | `dotnet-r4` | Could | - | `SM-02` |
| `US-DN-032` | Story | Measure SM-03: order lines needing correction | `FT-DN-22` | `track-dotnet` | `dotnet-r4` | Could | - | `SM-03` |
| `US-DN-033` | Story | Measure SM-04: invoice copy requests handled by staff | `FT-DN-22` | `track-dotnet` | `dotnet-r4` | Could | - | `SM-04` |
| `US-DN-034` | Story | Use the portal in Dutch | `FT-DN-23` | `track-dotnet` | - (unplanned) | Should (provisional) | `BR-11` | `OQ-02` |
| `US-DN-035` | Story | See which field changed in an order | `FT-DN-24` | `track-dotnet` | - (unplanned) | Could (provisional) | `NFR-08` | - |
| `US-DN-036` | Story | See when each status last changed | `FT-DN-26` | `track-dotnet` | - (unplanned) | Should (provisional) | `BR-04` | `SM-02` |
| `US-DN-037` | Story | Read Picking and Shipped in plain words | `FT-DN-26` | `track-dotnet` | - (unplanned) | Should (provisional) | `BR-04` | `SM-02` |

