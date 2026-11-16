# Intake review: Northwind knowledge-docs

Captured by the Squad Coordinator as transport of the BRD Quality Reviewer's read-only return. Reviewer verdict: **Ready-With-Gaps** (0 blocking gaps, 11 non-blocking gaps). No BRD draft existed, so `BRD_STANDARD_FINDINGS_V1` and `BRD_QUALITY_REPORT_V1` were not produced.

## Assessment of the coordinator's scope interpretation

Accepted with five amendments:

1. `track-power-platform` already exists in ES-30 for BA-03. What is missing is a delivery team and a release for BA-03, not a track. Tag BA-03 items `track-power-platform`; no placeholder.
2. Zero releases is allowed (ES-31: unplanned items carry only the track tag). Record BA-03 cross-track dependencies in the BRD, PRD and backlog.
3. If BA-03 is covered it is in scope: every BR-14 to BR-19 and NFR-09 needs a story. Add a Release column showing "unplanned". Do not list BA-03 as out of scope.
4. Business case section 8 makes the claims pilot (Q1 2027) the earliest milestone. Leaving BA-03 unplanned means that date cannot be committed. Record as OPEN, owner Lena Varga (G-08).
5. The Order Desk API dependency (CS-27, ES-36) is correctly an OPEN item, but the API work sits in no business area (G-01).

## Blocking gaps

None.

## Non-blocking gaps

| ID | Gap | Source | How to carry it | Owner |
|---|---|---|---|---|
| G-01 | The Order Desk API has no owner. BA-03 cannot reach order lines for BR-14 without one; ES-36 forbids direct database access and Order Desk has no API. The portal also needs a way to read Order Desk. | CS-27, ES-36, C-05 | OPEN. Ask whether to add an enabler story under `track-dotnet`. BA-03 MVE uses a stub connector contract (ES-33, ES-37). | Ahmed Benali |
| G-02 | Power Platform licensing and feasibility conflict. C-07 allows standard connectors only; ES-36 requires a custom connector; SQL Server and file access look premium; CS-25 and CS-27 need on-premises access; C-08 caps cost at EUR 900/month; Dataverse licensing unclear. | C-07, C-08, ES-36, CS-25, CS-27 | OPEN. Mark any price or licence claim as ASSUMPTION. | Ahmed Benali |
| G-03 | The Azure and .NET boundary is unclear. Azure hosts an app needing code changes (CS-13 to CS-17). "A track never waits" conflicts with azure-r1 needing a deployable app. Staff sign-in moves from Windows Integrated Authentication (CS-04) to Entra ID, but NFR-04 is not mapped to BA-01. The EUR 1,500 cap (C-04) spans both tracks. Invoice share (CS-08, CS-11) and SMTP relay (CS-12) placement in Azure undefined. | BA-01, BA-02, ES-30, CS-13 to CS-17 | Split stories per ES-30. Default: .NET owns code changes, Azure owns hosting, IaC, DR and monitoring. Cross-track dependency as OPEN. | Ahmed Benali |
| G-04 | BR-04 ("always up to date") conflicts with CS-10 (Picking and Shipped update once per night; StockPilot unchanged per section 6). BR-09 has the same issue. | BR-04, BR-09, CS-10, C-03 | Define freshness in acceptance criteria as ASSUMPTION and OPEN. | Lena Varga |
| G-05 | Weak testability: NFR-01 and NFR-02 have no measurement point or load; C-04 says both "target" and "at most"; SM-01 to SM-04 say "portal launch" (pilot or general availability); CET/CEST mixed. | NFR-01, NFR-02, C-04, SM-01 to SM-04 | MVE and acceptance criteria use leading indicators. Definitions as ASSUMPTION. | Lena Varga |
| G-06 | No defined MVE or PRD structure, prioritisation method beyond MoSCoW, release count, backlog tool (ES-39) or ES-28 prefix. ES-27 and ES-37 mean MVEs are local, prototype or paper-based. | ES-07, ES-27, ES-37, ES-39 | ASSUMPTION list. | Lena Varga |
| G-07 | Identifier scheme: source uses `BR-` and `C-` with two digits; no FR, AC or goal identifiers. | ES-02 | Keep source IDs verbatim. Introduce new IDs for FR, AC, goals as ASSUMPTION. | Lena Varga |
| G-08 | BA-03 has no team or release; the Q1 2027 claims pilot cannot be committed. Power Platform skills not named (C-06 is .NET only). CS-26 shows no governed environments while ES-35 requires them. | section 8, C-06, CS-26, ES-35 | OPEN. | Lena Varga, Marc Dubois |
| G-09 | Missing data facts: order-to-invoice-number mapping (BR-07, CS-11); 24-month retention (BR-02) unconfirmed; no customer concurrency figure; BR-17 needs warehouse per order line. | BR-02, BR-07, BR-17, CS-11 | ASSUMPTION or OPEN. | Ahmed Benali |
| G-10 | Enabler work has no BR or NFR to cite (build pipeline CS-19, tests CS-18, logging CS-15). | ES-02, ES-06 | Cite ES, CS and C items; add a section to the traceability table. | Lena Varga |
| G-11 | Release approver per track not named (ES-31). | ES-31 | OPEN. | Marc Dubois |

## Open questions OQ-01 to OQ-05

All five are non-blocking for producing the documents.

| OQ | Blocks later | Proposed ASSUMPTION | Owner |
|---|---|---|---|
| OQ-01 Identity provider for customers | BA-02 sign-in design, NFR-04 detail | MVE uses a test identity; sign-in story is provider-neutral; options listed as OPEN. | Ahmed Benali |
| OQ-02 Dutch in first release | BA-02 release 1 scope | BR-11 is Should. Release 1 French and English; Dutch follows. | Sofie Peeters, Lena Varga |
| OQ-03 Customer administrators | BR-08 scope | Role exists; who gets it is OPEN. | Lena Varga |
| OQ-04 Approver of claims of EUR 500 or less | BA-03 approval workflow | Acceptance criteria cover only above EUR 500 and no self-approval (BR-15); other path OPEN. | Julien Moreau, Lena Varga |
| OQ-05 Migrate spreadsheet claims | BA-03 scope (about 9,400 rows, CS-24) | Separate unplanned item. | Lena Varga, Julien Moreau |

## Checks that passed

* All 19 BR, 9 NFR and 8 C items map to at least one business area in section 4.
* Section 6 out-of-scope list is clear and consistent with BR-14.
* The six BR-04 statuses match `OrderStatus.cs`.
* CS-13 to CS-17 are consistent with `src/`.
* Track tag and release names are consistent with ES-30, ES-31 and ES-39.
* Business case status "Approved for discovery, not for build" fits planning documents.

## Clarifying questions (carried as OPEN items)

1. Order Desk API: enabler under `track-dotnet`, or OPEN dependency only? Owner? (G-01)
2. Premium Power Platform licence, data gateway or custom connector within C-07 and C-08? (G-02)
3. Does .NET own all Order Desk code changes, and does azure-r1 deploy a rehosted .NET Framework 4.8 app or wait for .NET 10? (G-03)
4. Is staff sign-in with Entra ID in scope for BA-01? (G-03)
5. Acceptable status freshness given the nightly batch? (G-04)
6. Does "portal launch" mean the pilot or general availability? (G-05)
7. Which backlog tool and ES-28 prefix? (G-06)
8. Intended date for BA-03, or unplanned? (G-08)
9. Who approves releases per track? (G-11)

Reviewer tool calls: 10 (reads, globs and greps, no writes). Reviewer model: not reported.
