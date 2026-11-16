---
traceability_id: "TRACE-NW-001"
title: "Northwind Traders: traceability of business and quality requirements to backlog stories"
status: "draft"
version: "0.1.0"
owners: ["Lena Varga"]
reviewers: ["Marc Dubois", "Ahmed Benali"]
created_date: "2026-11-15"
last_updated: "2026-11-15"
source_backlog_id: "BACKLOG-NW-001"
source_backlog_path: "docs/product/backlog.md"
source_prd_id: "PRD-NW-001"
scope: ["BA-01", "BA-02", "BA-03"]
---

# Northwind Traders: traceability table

> **TRACE-NW-001** | Status: **Draft for review** | Version 0.1.0 | Last updated 2026-11-15
>
> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> Built from the item register of [backlog.md](backlog.md) (`BACKLOG-NW-001`), so the two documents cannot drift. Nothing is published to a tracker and nothing is built or deployed (ES-27, ES-37).

This table proves, as ES-06 asks, that every `BR-` (business requirement) and `NFR-` (quality requirement) in scope is covered by at least one story, and lists any identifier that is not. A *story* here means a backlog story (`STORY-nnn`). Enabler stories (`EA-`, `EN-`, `EP-`) have no `BR-` or `NFR-` of their own (G-10); they are in section 6.

How to read the tables:

* **Split identifiers.** Where one id spans two tracks or two releases it is split into one story per track or per release (ES-30, ES-31; A-43). Each part is a **separate row with the same id**, so no id is credited to a story that does not cover it.
* **Covering stories** are the stories that *deliver* the id in that row, as in the canonical coverage matrix (plan C3, PRD section 16.1). **Notes** name items that *support* the id but do not cover it (for example an enabler, a design story or a parity story of an earlier release). Supporting items are not counted as coverage.
* **Release(s)** is the release tag the covering story carries (ES-31), or `unplanned` (the story carries only its track tag).
* **Status** values: *Covered* (a planned story covers it); *Covered, unplanned* (a story covers it but belongs to no release, BA-03 or the API implementation); *Covered, OPEN remains* (covered, with an **OPEN:** item that can change the acceptance criteria). Every row's document status is *Draft for review*. Nothing is approved (O-21).

## 1. Scope statement

The scope is business areas **BA-01 Platform and data-centre exit** (Azure track), **BA-02 Ordering and customer self-service** (.NET track) and **BA-03 Delivery claims and credit notes** (Power Platform track). That is **19 `BR-` identifiers** (`BR-01` to `BR-19`) and **9 `NFR-` identifiers** (`NFR-01` to `NFR-09`): **28 identifiers in all**.

| Business area | Delivery track and tag | Identifiers in scope (source: business-case section 4) | Planned releases |
|---|---|---|---|
| BA-01 | Azure, `track-azure` | BR-13; NFR-01, NFR-03, NFR-05, NFR-06; NFR-08 (retention side, A-43) | `azure-r1`, `azure-r2`, `azure-r3` |
| BA-02 | .NET, `track-dotnet` | BR-01 to BR-12; NFR-02, NFR-03 (portal side), NFR-04, NFR-05, NFR-07, NFR-08 | `dotnet-r1`, `dotnet-r2`, `dotnet-r3` |
| BA-03 | Power Platform, `track-power-platform` | BR-14 to BR-19; NFR-03 (BA-03 side), NFR-04 (BA-03 side), NFR-09 | none: unplanned (A-44) |

`NFR-03`, `NFR-04` and `NFR-05` apply wherever they are relevant, whichever area a story belongs to (business-case section 4), so each is split per track below.

Counts: 144 backlog items (12 epics, 39 features, 57 stories, 36 enablers). The 28 identifiers are covered by **39 rows** in sections 2 and 3 (22 `BR-` rows and 17 `NFR-` rows), because 3 `BR-` ids and 6 `NFR-` ids are split.

## 2. `BR-` to stories

Priority is from the business case (`BR-` ids). One row per covering part.

| Id | BA | Track | Priority | Covering stories | Release(s) | Status | Notes (split, supporting items, OPEN) |
|---|---|---|---|---|---|---|---|
| BR-01 | BA-02 | .NET | Must | STORY-230 | `dotnet-r2` | Covered, OPEN remains | Negative case in `STORY-230/AC2`. Supporting: `EN-11`, `EN-08`, `EN-12`. O-10, A-19. |
| BR-02 | BA-02 | .NET | Must | STORY-231 | `dotnet-r2` | Covered | Supporting: `STORY-206` and `EN-10` (time parity, `dotnet-r1`). A-16. |
| BR-03 | BA-02 | .NET | Must | STORY-232 | `dotnet-r2` | Covered | none |
| BR-04 | BA-02 | .NET | Must | STORY-233 | `dotnet-r2` | Covered, OPEN remains | Freshness "as of" time (A-03); gate MVE-02; O-04, O-16, T-01. |
| BR-05 | BA-02 | .NET | Must | STORY-234 | `dotnet-r2` | Covered, OPEN remains | Gate MVE-02. Supporting: `EN-06`. O-28. |
| BR-06 | BA-02 | .NET | Must | STORY-235 | `dotnet-r2` | Covered, OPEN remains | O-23, A-37, T-08. |
| BR-07 | BA-02 | .NET | Should | STORY-260 | `dotnet-r3` | Covered, OPEN remains | Supporting: `EN-07`; Azure `EA-07`, `STORY-141` (design). O-15. |
| BR-08 | BA-02 | .NET | Should | STORY-261 | `dotnet-r3` | Covered, OPEN remains | Scope per O-12 (A-12). |
| BR-09 | BA-02 | .NET | Could | STORY-262 | `dotnet-r3` | Covered, OPEN remains | Freshness (A-03). Supporting (not coverage): Azure `EA-12`, `STORY-144` in `azure-r2`. O-17, O-18, X-10. |
| BR-10 (parity) | BA-02 | .NET | Must | STORY-203 | `dotnet-r1` | Covered | Split part 1 of 2: parity of what staff see today (A-51). Supporting: `EN-01`. |
| BR-10 (portal value) | BA-02 | .NET | Must | STORY-236 | `dotnet-r2` | Covered | Split part 2 of 2. Gate MVE-02. Supporting: `EN-11`. |
| BR-11 (French and English) | BA-02 | .NET | Should | STORY-237 | `dotnet-r2` | Covered, OPEN remains | Split part 1 of 2. A-11, O-11, O-18. |
| BR-11 (Dutch) | BA-02 | .NET | Should | STORY-263 | `dotnet-r3` | Covered, OPEN remains | Split part 2 of 2. A-11, O-11. |
| BR-12 (parity) | BA-02 | .NET | Must | STORY-202 | `dotnet-r1` | Covered | Split part 1 of 2. Supporting: `EN-02`, `EN-10`, `STORY-206`. |
| BR-12 (customer prices) | BA-02 | .NET | Must | STORY-238 | `dotnet-r2` | Covered | Split part 2 of 2. Gate MVE-02. |
| BR-13 | BA-01 | Azure | Must | STORY-170, STORY-171 | `azure-r3` | Covered, OPEN remains | **What is covered:** the cutover plan, the rollback and rehearsal plan and the decommission runbook, reviewed and checked locally (`STORY-170`, `STORY-171`), together with two design items. `EA-15` (`azure-r2`) designs the hosting of the Order Desk web application for `tst` and `prd` as infrastructure code. `EA-16` (`azure-r3`) writes the database migration steps and the rehearsal plan and checks them locally. **What is not covered:** applying anything to a subscription, the rehearsals and the live cutover are planned execution after approval, which comes before 6 June 2027 (A-53, ES-27), so "Covered" means designs, procedures and runbooks, not a finished move. Supporting: `STORY-120`, `STORY-122`, `STORY-140`, `EA-05`, `EA-06`, `EA-13`. The runtime choice stays **OPEN:** (O-03, A-20) and the data tier waits for MVE-01. O-03, O-15, O-27. |
| BR-14 | BA-03 | Power Platform | Must (P1) | STORY-320 | unplanned | Covered, unplanned | Under 2 minutes, up to 5 photos. Gate MVE-03. Supporting: `EP-03`, `EP-04`, `EP-06`. X-20 to X-22. |
| BR-15 | BA-03 | Power Platform | Must (P1) | STORY-321 | unplanned | Covered, unplanned | No self-approval; only claims above EUR 500 (A-13, O-13). Supporting: `EP-06`. |
| BR-16 | BA-03 | Power Platform | Must (P1) | STORY-322 | unplanned | Covered, unplanned | Supporting: `EP-05`. X-24, O-15, O-29. |
| BR-17 | BA-03 | Power Platform | Should (P2) | STORY-350 | unplanned | Covered, unplanned | A-18, X-25, O-30. |
| BR-18 | BA-03 | Power Platform | Should (P2) | STORY-351 | unplanned | Covered, unplanned | O-22, A-57. |
| BR-19 | BA-03 | Power Platform | Could (P3) | STORY-370 | unplanned | Covered, unplanned | X-26, O-18. |

## 3. `NFR-` to stories

The business case gives the NFRs no priority, so each is Must (A-06). A cross-cutting NFR is split per track and, where design and proof differ, per release (C3, A-43). Every `NFR-` that applies to more than one track has one row per track.

| Id | BA | Track | Covering stories | Release(s) | Status | Notes (split, how it is covered, OPEN) |
|---|---|---|---|---|---|---|
| NFR-01 (design and alerting) | BA-01 | Azure | STORY-142 | `azure-r2` | Covered | Synthetic probe, local Central European time (A-05, T-17). Supporting: `EA-04`. It also applies to the portal when live. |
| NFR-01 (proof) | BA-01 | Azure | STORY-173 | `azure-r3` | Covered | Availability proof plan; the proof itself follows approval (A-53). |
| NFR-02 | BA-02 | .NET | STORY-243 | `dotnet-r2` | Covered, OPEN remains | Server-side p95, under 2 seconds for 95 % of requests (A-05). Supporting (not coverage): `STORY-231`, `STORY-232`. O-08, A-17. |
| NFR-03 (Azure) | BA-01 | Azure | STORY-104 | `azure-r1` | Covered | Supporting: `EA-01`; `EA-16` (`azure-r3`) keeps the moved database in an EU region (`EA-16/AC3`). |
| NFR-03 (portal) | BA-02 | .NET | STORY-239 | `dotnet-r2` | Covered, OPEN remains | Hosting, identity service and mail stay in the EU. O-24, T-15. |
| NFR-03 (claims) | BA-03 | Power Platform | STORY-301 | unplanned | Covered, unplanned | Supporting: `EP-01`, `EP-02`. X-27. |
| NFR-04 (staff) | BA-02 | .NET | STORY-204 | `dotnet-r1` | Covered, OPEN remains | Supporting: `EN-08`. The Azure side is X-04, listed as **OPEN:**, not as a story (O-03). |
| NFR-04 (customers) | BA-02 | .NET | STORY-240 | `dotnet-r2` | Covered, OPEN remains | A-10, O-10, O-24. |
| NFR-04 (claims) | BA-03 | Power Platform | STORY-302 | unplanned | Covered, unplanned | Supporting: `EP-06`. X-23. |
| NFR-05 (Azure) | BA-01 | Azure | STORY-103 | `azure-r1` | Covered | Supporting: `EA-03`. Release exit criterion: secret scan (A-54). |
| NFR-05 (.NET) | BA-02 | .NET | STORY-205 | `dotnet-r1` | Covered | Supporting: `EN-04`. Release exit criterion: secret scan (A-54). |
| NFR-06 (design) | BA-01 | Azure | STORY-146 | `azure-r2` | Covered | RPO 1 hour, RTO 4 hours; supporting: `EA-08`. Gate MVE-01. |
| NFR-06 (proof) | BA-01 | Azure | STORY-172 | `azure-r3` | Covered | Restore test limits 60 minutes and 4 hours; supporting: `EA-14`, and `EA-16` (hands the moved copy to the first restore test). T-14, A-53. |
| NFR-07 | BA-02 | .NET | STORY-242 | `dotnet-r2` | Covered | WCAG 2.2 AA review; a conformance statement needs a qualified reviewer (A-54). |
| NFR-08 (content) | BA-02 | .NET | STORY-241 | `dotnet-r2` | Covered, OPEN remains | Who, what, when, channel; known gaps listed (A-51, T-13). |
| NFR-08 (retention design) | BA-01 | Azure | STORY-145 | `azure-r2` | Covered | 7-year retention in Azure; supporting: `EA-08`. X-15, A-31. |
| NFR-09 | BA-03 | Power Platform | STORY-323 | unplanned | Covered, unplanned | Who, what, when, amount; 7 years (A-31). |

**Cross-cutting NFRs, one line each.** `NFR-01`: `STORY-142` (`azure-r2`) and `STORY-173` (`azure-r3`). `NFR-03`: `STORY-104` (Azure), `STORY-239` (.NET), `STORY-301` (Power Platform). `NFR-04`: `STORY-204`, `STORY-240` (.NET), `STORY-302` (Power Platform); the Azure side is X-04, **OPEN:**. `NFR-05`: `STORY-103` (Azure), `STORY-205` (.NET). `NFR-06`: `STORY-146` (`azure-r2`) and `STORY-172` (`azure-r3`). `NFR-08`: `STORY-241` (.NET) and `STORY-145` (Azure).

## 4. Identifiers in scope that are not covered

| Identifier | Reason | Owner |
|---|---|---|
| **none** | All 19 `BR-` and all 9 `NFR-` have at least one covering story (sections 2 and 3). | not applicable |

Two things are **not** gaps and are stated here so nobody reads them as gaps:

* `NFR-04` has no Azure-side story. The Azure side (how identity reaches Azure, for example staff sign-in in the Azure design) is the **OPEN:** dependency X-04 (owner Ahmed Benali), not an uncovered requirement: the business case lists `NFR-04` under BA-02 and BA-03 only.
* The claims requirements of BA-03 are covered by **unplanned** stories. "Covered" means a story with criteria exists; it does not mean a delivery date exists (A-25, O-07).
* `BR-13` is covered by designs, procedures and runbooks only. The two design items `EA-15` (application hosting) and `EA-16` (database migration and rehearsal) were added after the first review (A-59); what they cover is stated in the `BR-13` row of section 2. Nothing is applied to a subscription from this workshop (ES-27).

## 5. Business areas out of scope

| Business area | Treatment |
|---|---|
| **none** | **none: BA-01, BA-02 and BA-03 are all in scope.** BA-03 is in scope but unplanned (no release, no release tag; A-44). |

Not business areas, and not requirements of any planned release (business-case section 6): online payment, a native mobile app, changes to StockPilot, replacing the finance system, and customers recording claims themselves in the portal. No story covers them.

## 6. Enabler and standard-driven items

Enablers have no `BR-` or `NFR-` of their own, so they cite `CS-` (current state), `ES-` (engineering standard), `C-` (constraint) and the `NFR-` they protect (G-10). They are listed here instead of in sections 2 and 3. Priority follows A-49.

### 6.1 Enabler stories (36)

| Enabler | Track | Release | Priority | Source (CS-, ES-, C-, NFR- it protects) | Serves stories |
|---|---|---|---|---|---|
| EA-01 | Azure | `azure-r1` | Must | CS-09, ES-20 to ES-24; NFR-03 | STORY-101, STORY-104 |
| EA-02 | Azure | `azure-r1` | Must | CS-09, C-01, C-03 | STORY-102 |
| EA-03 | Azure | `azure-r1` | Must | CS-13, ES-17, ES-25; NFR-05 | STORY-103 |
| EA-05 | Azure | `azure-r1` | Must | CS-07, CS-21, C-02, ES-21 | STORY-120, STORY-122 |
| EA-09 | Azure | `azure-r1` | Must | C-04, CS-03, CS-06 | STORY-121 |
| EA-11 | Azure | `azure-r1` | Must | CS-19, ES-22, ES-27 | STORY-105 |
| EA-04 | Azure | `azure-r2` | Must | CS-15, CS-22, ES-26; NFR-01 | STORY-142, STORY-173 |
| EA-06 | Azure | `azure-r2` | Must | CS-10, C-03 | STORY-140 |
| EA-07 | Azure | `azure-r2` | Should | CS-08, CS-11, CS-14 | STORY-141 |
| EA-08 | Azure | `azure-r2` | Must | CS-07, CS-23; NFR-06, NFR-08 | STORY-145, STORY-146 |
| EA-10 | Azure | `azure-r2` | Must | ES-23, C-04 | STORY-143 |
| EA-12 | Azure | `azure-r2` | Should (A-49) | CS-12 | STORY-144 |
| EA-15 | Azure | `azure-r2` | Must (A-49) | BR-13, C-01, C-02, C-06, CS-06, CS-13, CS-16, ES-21, ES-25; NFR-01 | STORY-143, STORY-170 (added after the first review, A-59) |
| EA-13 | Azure | `azure-r3` | Must | CS-21, C-01, C-02, SM-07 | STORY-170, STORY-171, STORY-173, STORY-174 |
| EA-14 | Azure | `azure-r3` | Must | CS-23; NFR-06 | STORY-172 |
| EA-16 | Azure | `azure-r3` | Must (A-49) | BR-13, C-01, C-02, CS-07, CS-23; NFR-03, NFR-06 | STORY-170 and the `STORY-120` decision it carries out (added after the first review, A-59) |
| EN-01 | .NET | `dotnet-r1` | Must | CS-01, CS-02, ES-13, ES-14, ES-19 | STORY-201, STORY-203 |
| EN-02 | .NET | `dotnet-r1` | Must | CS-18, CS-20, ES-18 | STORY-202 |
| EN-03 | .NET | `dotnet-r1` | Must | CS-17, ES-15 | STORY-201 |
| EN-04 | .NET | `dotnet-r1` | Must | CS-13, ES-17, ES-25; NFR-05 | STORY-205 |
| EN-05 | .NET | `dotnet-r1` | Must | CS-15, ES-16 | STORY-201 |
| EN-06 | .NET | `dotnet-r1` | Must | CS-16 | STORY-234 |
| EN-08 | .NET | `dotnet-r1` | Must | CS-04, ES-14, ES-19; NFR-04 | STORY-201, STORY-204, STORY-230, STORY-240 |
| EN-09 | .NET | `dotnet-r1` | Must | CS-18, CS-19 | all .NET releases |
| EN-10 | .NET | `dotnet-r1` | Must | CS-20 | STORY-202, STORY-206, STORY-231, STORY-238 |
| EN-12 | .NET | `dotnet-r1` | Must | ES-27, ES-17 | all local testing, MVE-02 |
| EN-13 | .NET | `dotnet-r1` | Must | ES-13, ES-08 | STORY-201 |
| EN-11 | .NET | `dotnet-r2` | Must | CS-04, CS-05; BR-01, BR-10 (cited as sources of the protected behaviour) | STORY-230, STORY-236 |
| EN-07 | .NET | `dotnet-r3` | Should | CS-14, CS-11 | STORY-260 |
| EN-14 | .NET | `dotnet-r3` | Should (A-49) | CS-27, ES-36 | STORY-265, STORY-280 |
| EP-01 | Power Platform | unplanned | Must (P1) | CS-26, ES-35; NFR-03 | STORY-301 |
| EP-02 | Power Platform | unplanned | Must (P1) | ES-34 | STORY-301 |
| EP-03 | Power Platform | unplanned | Must (P1) | CS-27, ES-33, ES-36 | STORY-320 |
| EP-04 | Power Platform | unplanned | Must (P1) | C-07, C-08 | all BA-03 stories |
| EP-05 | Power Platform | unplanned | Must (P1) | CS-25 | STORY-322 |
| EP-06 | Power Platform | unplanned | Must (P1) | CS-28, ES-34; NFR-04 | STORY-302, STORY-321 |

Counts: Azure 16 (`azure-r1` 6, `azure-r2` 7, `azure-r3` 3), .NET 14 (`dotnet-r1` 11, `dotnet-r2` 1, `dotnet-r3` 2), Power Platform 6 (unplanned). `EA-15` and `EA-16` are new since the plan (A-59), continuing the numbering after `EA-14` (next free numbers: `EA-17`, `EN-15`, `EP-07`).

### 6.2 Stories driven by standards, constraints and current-state facts

These stories implement a product requirement (`FR-`) whose sources are `C-`, `CS-`, `ES-` or `SM-` ids, and **do not cover a `BR-` or `NFR-` of their own**; they support the ones named.

| Story | Track | Release | Sources | What it supports |
|---|---|---|---|---|
| STORY-101 | Azure | `azure-r1` | C-01, CS-09, ES-20, ES-22 to ES-24, ES-27 | Foundation for `NFR-03`, `NFR-05` (Azure) |
| STORY-102 | Azure | `azure-r1` | CS-09, C-01, C-03 | StockPilot exchange reachability |
| STORY-105 | Azure | `azure-r1` | CS-19, ES-22, ES-27 | Release validation |
| STORY-120 | Azure | `azure-r1` | C-02, C-06, CS-07, BR-13, ES-21 | `BR-13` (design side) |
| STORY-121 | Azure | `azure-r1` | C-04, T-03 | `C-04` cost cap |
| STORY-122 | Azure | `azure-r1` | BR-13, CS-07, CS-08, CS-21 | `BR-13` (design side) |
| STORY-140 | Azure | `azure-r2` | C-03, CS-10, BR-13 | `BR-13` (design side), `C-03` |
| STORY-141 | Azure | `azure-r2` | CS-08, CS-11, CS-14 | `BR-07` hosting |
| STORY-143 | Azure | `azure-r2` | ES-23, C-04 | Portal pilot environment |
| STORY-144 | Azure | `azure-r2` | CS-12, BR-09 | `BR-09` mail path |
| STORY-174 | Azure | `azure-r3` | C-02, SM-07, C-01 | `SM-07`, `C-01`, `C-02` |
| STORY-206 | .NET | `dotnet-r1` | BR-02, BR-12, CS-20 | `BR-02`, `BR-12` (time parity) |
| STORY-264 | .NET | `dotnet-r3` | SM-01 to SM-04 | Success-measure instrumentation (O-26) |
| STORY-265 | .NET | `dotnet-r3` | CS-27, ES-36, G-01 | The API contract for BA-03 |
| STORY-280 | .NET | unplanned | CS-27, ES-36, C-05, G-01 | The API implementation (O-01) |
| STORY-324 | Power Platform | unplanned | OQ-05, CS-24 | Spreadsheet claims migration (O-14) |

## 7. Supplementary coverage of constraints and success measures

**Supplementary: not required by ES-06.** `C-` constraints and `SM-` success measures are not in the `BR-`/`NFR-` scope, so a gap here is not an ES-06 gap. Release is the tag of the story.

| Id | What it is | Stories and enablers that serve it | Release(s) |
|---|---|---|---|
| C-01 | Order Desk in Azure before 30 June 2027 | STORY-102, `EA-02`; `EA-15`; `EA-16`; STORY-170, STORY-171, STORY-174, `EA-13` | `azure-r1`, `azure-r2`, `azure-r3` |
| C-02 | Servers past end of support; stop paying ESU | STORY-120, `EA-05`; `EA-15`; `EA-16`; STORY-174, `EA-13` | `azure-r1`, `azure-r2`, `azure-r3` |
| C-03 | StockPilot stays on premises, unchanged | STORY-102; STORY-140, `EA-06` | `azure-r1`, `azure-r2` |
| C-04 | Azure run cost at most EUR 1,500 a month | STORY-121, `EA-09`; STORY-143, `EA-10` | `azure-r1`, `azure-r2` |
| C-05 | One order source: no second order database | STORY-235; STORY-280 | `dotnet-r2`, unplanned |
| C-06 | Six-person team knows .NET and SQL Server | STORY-120, `EA-05`; `EA-15` | `azure-r1`, `azure-r2` |
| C-07 | Power Platform approved; standard connectors only | `EP-04`, STORY-301 | unplanned |
| C-08 | Claims run cost at most EUR 900 a month for about 52 users | `EP-04`, STORY-351 | unplanned |
| SM-01 | Share of orders placed through the portal | STORY-230 to STORY-236 (value); STORY-264 (instrumentation) | `dotnet-r2`, `dotnet-r3` |
| SM-02 | "Where is my order?" calls per week | STORY-233; STORY-264 (calls counted outside the product) | `dotnet-r2`, `dotnet-r3` |
| SM-03 | Order lines needing correction | STORY-234, STORY-235; STORY-264 | `dotnet-r2`, `dotnet-r3` |
| SM-04 | Invoice copy requests handled by staff | STORY-260; STORY-264 | `dotnet-r3` |
| SM-05 | Average time to resolve a claim | STORY-320, STORY-321, STORY-322, STORY-351 | unplanned |
| SM-06 | Claims lost or recorded twice | STORY-320 (duplicate warning, A-56), STORY-322 | unplanned |
| SM-07 | Production servers past end of support | STORY-170, STORY-174, `EA-13`, `EA-16` | `azure-r3` |

Measurement sources and owners for the success measures are **OPEN:** O-26 (Lena Varga). "6 months after portal launch" means general availability (A-04, O-05).

## 8. Release to ids (reverse view)

For each release: the `BR-` and `NFR-` it covers, in the words of the canonical release table (plan C1, PRD section 6.2), and the stories that cover them. The "BR / NFR covered" column equals the C1 column. A release never waits for another track.

| Release | BR / NFR covered (as in C1) | Covering stories | Other stories | Enablers |
|---|---|---|---|---|
| `azure-r1` | NFR-03 (Azure), NFR-05 (Azure); supports C-01, C-02, C-04, C-06 | STORY-104 (NFR-03), STORY-103 (NFR-05) | STORY-101, STORY-102, STORY-105, STORY-120, STORY-121, STORY-122 | EA-01, EA-02, EA-03, EA-05, EA-09, EA-11 |
| `azure-r2` | NFR-01 (design and alerting), NFR-06 (design), NFR-08 (retention design); supports C-03, C-04 | STORY-142 (NFR-01), STORY-146 (NFR-06), STORY-145 (NFR-08) | STORY-140, STORY-141, STORY-143, STORY-144 | EA-04, EA-06, EA-07, EA-08, EA-10, EA-12, EA-15 |
| `azure-r3` | BR-13; NFR-01 (proof), NFR-06 (proof); supports SM-07, C-01, C-02 | STORY-170, STORY-171 (BR-13), STORY-173 (NFR-01), STORY-172 (NFR-06) | STORY-174 | EA-13, EA-14, EA-16 |
| `dotnet-r1` | NFR-04 (staff), NFR-05 (.NET), BR-10 (parity), BR-12 (parity) | STORY-204 (NFR-04), STORY-205 (NFR-05), STORY-203 (BR-10), STORY-202 (BR-12) | STORY-201, STORY-206 | EN-01, EN-02, EN-03, EN-04, EN-05, EN-06, EN-08, EN-09, EN-10, EN-12, EN-13 |
| `dotnet-r2` | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-10 (portal value), BR-11 (French and English), BR-12 (customer prices); NFR-02, NFR-03 (.NET), NFR-04 (customers), NFR-07, NFR-08 (content) | STORY-230 (BR-01), STORY-231 (BR-02), STORY-232 (BR-03), STORY-233 (BR-04), STORY-234 (BR-05), STORY-235 (BR-06), STORY-236 (BR-10), STORY-237 (BR-11), STORY-238 (BR-12), STORY-243 (NFR-02), STORY-239 (NFR-03), STORY-240 (NFR-04), STORY-242 (NFR-07), STORY-241 (NFR-08) | none | EN-11 |
| `dotnet-r3` | BR-07, BR-08, BR-09, BR-11 (Dutch); SM-01 to SM-04 instrumentation | STORY-260 (BR-07), STORY-261 (BR-08), STORY-262 (BR-09), STORY-263 (BR-11), STORY-264 (SM-01 to SM-04) | STORY-265 | EN-07, EN-14 |
| unplanned, `track-dotnet` | none (serves BR-14 through X-20; C-05) | none | STORY-280 | none |
| unplanned, `track-power-platform` | BR-14 to BR-19, NFR-03 (BA-03), NFR-04 (BA-03), NFR-09: documented, tagged by track only | STORY-320 (BR-14), STORY-321 (BR-15), STORY-322 (BR-16), STORY-350 (BR-17), STORY-351 (BR-18), STORY-370 (BR-19), STORY-301 (NFR-03), STORY-302 (NFR-04), STORY-323 (NFR-09) | STORY-324 | EP-01, EP-02, EP-03, EP-04, EP-05, EP-06 |

Check: the planned releases cover `BR-01` to `BR-13` and all 9 `NFR-` ids (the split ids in parts); `BA-03` covers `BR-14` to `BR-19`, the claims side of `NFR-03` and `NFR-04`, and `NFR-09`, all unplanned. The rows across all releases and the unplanned groups total the 39 rows of sections 2 and 3.

## 9. Registers (ids used)

Full text, owners and wording are in [backlog.md](backlog.md) section 7, which is the register of record for every id introduced after the plan (`A-49` to `A-59`, `O-26` to `O-31`); none is restated here, so the two cannot drift.

* **ASSUMPTION ids used:** A-01 to A-25, A-27, A-29 to A-59 (the two unused numbers in the gap stay empty). New in the backlog: **A-55** (backlog authoring decisions), **A-56** (duplicate-claim warning, `STORY-320/AC6`), **A-57** (time to resolve, `STORY-351`), **A-58** (`azure-r3` window extended to 27 June 2027, owner Marc Dubois), **A-59** (`EA-15` and `EA-16` added after the first review, owner Ahmed Benali).
* **OPEN ids used:** O-01 to O-31 and the cross-track rows X-01 to X-15 and X-20 to X-27. New in the backlog: **O-28** (copied line of an unavailable product, Lena Varga), **O-29** (finance CSV columns, Julien Moreau), **O-30** (cause values for warehouse causes, Pieter Janssens), **O-31** (is the CC-BY 4.0 licence line in the BRD and PRD frontmatter intended, Lena Varga).
* **Coverage that carries an OPEN item:** `BR-01` (O-10), `BR-04` (O-04, O-16), `BR-05` (O-28), `BR-06` (O-23), `BR-07` (O-15), `BR-08` (O-12), `BR-09` (O-17, O-18), `BR-11` (O-11, O-18), `BR-13` (O-03, O-15, O-27), `BR-15` (O-13), `BR-16` (O-15, O-29), `BR-17` (O-30), `BR-18` (O-22), `BR-19` (O-18), `NFR-02` (O-08), `NFR-03` portal (O-24), `NFR-04` (O-10, O-24, X-04), `NFR-08` (T-13).
* **Gates still pending:** MVE-01 (`EPIC-102`, `EPIC-103`, inputs to `EPIC-104`), MVE-02 (`EPIC-202` stories for `BR-04`, `BR-05`, `BR-10`, `BR-12`; `STORY-264`), MVE-03 (`EPIC-301` to `EPIC-304`). No experiment has been run.

<!-- end of traceability -->
