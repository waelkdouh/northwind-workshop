---
release_id: "dotnet-r1"
title: "Release dotnet-r1: Modernised Order Desk with behavioural parity"
track: "dotnet"
release: "dotnet-r1"
track_tag: "track-dotnet"
release_tag: "dotnet-r1"
planned_git_tag: "product/dotnet-r1"
git_tag_created: false
status: "proposed"
document_status: "Draft for review"
target_window: "1 Dec 2026 to 26 Feb 2027"
approver: "OPEN: O-09"
approval_date: ""
source_backlog_id: "BACKLOG-NW-001"
source_backlog_path: "docs/product/backlog.md"
source_prd_id: "PRD-NW-001"
source_brd_id: "BRD-NW-001"
owners: ["Lena Varga"]
created_date: "2026-11-15"
---

# Release dotnet-r1: Modernised Order Desk with behavioural parity

> Status: **Draft for review** | Release status: **Proposed, awaiting product-owner approval** | Track: `track-dotnet` | Release tag: `dotnet-r1`
>
> Fictitious company created for the HVE Squad hands-on workshop. All figures are synthetic.
> This is a document. Nothing was built, deployed or published to a tracker to write it, and **no Git tag or commit exists for this release** (A-39, ES-27).

## 1. Document control

| Field | Value |
|---|---|
| Track | .NET, business area BA-02 (Ordering and customer self-service) |
| Track tag (ES-30) | `track-dotnet` |
| Release tag (ES-31) | `dotnet-r1` |
| Planned Git tag | `product/dotnet-r1` — **to be created on approval; not created** |
| Release status | Proposed, awaiting product-owner approval |
| Document status | Draft for review |
| Approver | **OPEN:** O-09 — the named approver for each track is not decided. **ASSUMPTION:** A-38 proposes the product owner, Lena Varga, with Marc Dubois as escalation. Owner to confirm: Marc Dubois. |
| Approval date | (blank until a human approves) |
| Release owner (document) | Lena Varga |
| Source documents | [backlog.md](../backlog.md) (item list is authoritative), [traceability.md](../traceability.md), [product-requirements.md](../product-requirements.md), [business-requirements.md](../business-requirements.md), [experiments.md](../experiments.md) |
| Rule | **A release never waits for another track** (ES-31). Needs from another track are **OPEN:** `X-nn` rows in section 6, each with a way to keep delivering. |

## 2. Objective, theme and target window

**Theme:** Modernised Order Desk with behavioural parity.

**Objective.** Run the same Order Desk, with the same prices and screens, on .NET 10 as one solution (`Core`, `Web`, `Tests`), with staff signing in through Microsoft Entra ID, no secret in the repository, and every test running on Windows, macOS and Linux. This release has little customer value by design. Every later .NET story needs it (source: EPIC-201, CS-13 to CS-20, ES-13 to ES-19, NFR-04, NFR-05, BR-10, BR-12).

**Target window:** 1 Dec 2026 to 26 Feb 2027. This is the period by which the release content is expected to be complete and ready for the product owner to approve. It is a target, not a commitment (A-01, A-42; **OPEN:** O-25, owners Lena Varga and Marc Dubois; **OPEN:** O-21, approval and funding to build, owner Marc Dubois).

**Main epic:** `EPIC-201` Modernise Order Desk to .NET 10 with parity.

**Experiment gate:** none. MVE-02 does **not** gate this release, because the parity work is technical and low risk (source: experiments.md section 2, backlog `EPIC-201`). MVE-02 is **not run**; its result is pending.

## 3. Items in this release

23 items: 1 epic, 5 features, 6 stories, 11 enablers. Every item carries the track tag `track-dotnet` **and** the release tag `dotnet-r1`, and appears in no other release (ES-31). Ids and titles are copied from the backlog item register (section 2.2). Rank is the order inside the .NET track; enablers come before the stories that need them (A-46). Priority for enablers follows A-49.

| Id | Title | Type | Priority | Rank | Source ids | Track tag | Release tag | MVE gate |
|---|---|---|---|---|---|---|---|---|
| EPIC-201 | Modernise Order Desk to .NET 10 with parity | epic | Must | — | NFR-04, NFR-05, BR-10, BR-12, C-01, C-02, CS-01, CS-02, CS-04, CS-13 to CS-20, ES-13 to ES-19 | `track-dotnet` | `dotnet-r1` | none |
| FEAT-201 | Modernise projects and web layer | feature | Must | — | CS-01, CS-02, CS-04, CS-15, CS-16, CS-17, ES-13 to ES-16, ES-19 | `track-dotnet` | `dotnet-r1` | none |
| EN-01 | Convert the solution to SDK-style projects on net10.0 | enabler | Must | 1 | CS-01, CS-02, ES-13, ES-14, ES-19 | `track-dotnet` | `dotnet-r1` | none |
| EN-13 | Record the decision on portal and API project shape | enabler | Must | 2 | ES-13, O-20 | `track-dotnet` | `dotnet-r1` | none |
| EN-03 | Replace direct ConfigurationManager calls with the options pattern | enabler | Must | 3 | CS-17, ES-15 | `track-dotnet` | `dotnet-r1` | none |
| EN-05 | Replace the Windows Event Log logger with standard logging | enabler | Must | 4 | CS-15, ES-16 | `track-dotnet` | `dotnet-r1` | none |
| EN-06 | Replace the in-process session order draft | enabler | Must | 5 | CS-16 | `track-dotnet` | `dotnet-r1` | none |
| EN-08 | Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in | enabler | Must | 6 | CS-04, NFR-04, ES-14, ES-19 | `track-dotnet` | `dotnet-r1` | none |
| STORY-201 | Run Order Desk on .NET 10 with unchanged staff screens | story | Must | 7 | CS-01, CS-02, ES-13, ES-14, ES-19 | `track-dotnet` | `dotnet-r1` | none |
| FEAT-202 | Test, build and local data | feature | Must | — | CS-18, CS-19, CS-20, ES-18, ES-27 | `track-dotnet` | `dotnet-r1` | none |
| EN-02 | Replace MSTest v1 so all tests run on Windows, macOS and Linux | enabler | Must | 8 | CS-18, CS-20, ES-18 | `track-dotnet` | `dotnet-r1` | none |
| EN-09 | Build an automated build and test pipeline | enabler | Must | 9 | CS-18, CS-19 | `track-dotnet` | `dotnet-r1` | none |
| EN-12 | Provide local test data with orders and a local database recipe | enabler | Must | 10 | ES-27, ES-17, A-51 | `track-dotnet` | `dotnet-r1` | none |
| FEAT-203 | Pricing, channel and time parity | feature | Must | — | BR-10, BR-12, BR-02, CS-20 | `track-dotnet` | `dotnet-r1` | none |
| EN-10 | Make time handling explicit and tested | enabler | Must | 11 | CS-20, A-24 | `track-dotnet` | `dotnet-r1` | none |
| STORY-202 | Keep pricing identical to today (pricing parity) | story | Must | 12 | BR-12, CS-20, ES-18 | `track-dotnet` | `dotnet-r1` | none |
| STORY-203 | Keep the order channel visible to staff (channel parity) | story | Must | 13 | BR-10, BR-06; **ASSUMPTION:** A-51 | `track-dotnet` | `dotnet-r1` | none |
| STORY-206 | Keep dates and price validity identical in any time zone (time parity) | story | Must | 14 | BR-02, BR-12, CS-20; **ASSUMPTION:** A-24 | `track-dotnet` | `dotnet-r1` | none |
| FEAT-204 | Staff sign-in with Entra ID | feature | Must | — | NFR-04, CS-04, G-03 | `track-dotnet` | `dotnet-r1` | none |
| STORY-204 | Sign staff in with Microsoft Entra ID | story | Must | 15 | NFR-04, CS-04, G-03 | `track-dotnet` | `dotnet-r1` | none |
| FEAT-205 | Secret-free configuration | feature | Must | — | NFR-05, CS-13, ES-17, ES-25 | `track-dotnet` | `dotnet-r1` | none |
| EN-04 | Remove Windows sign-in and server names from database configuration | enabler | Must | 16 | CS-13, NFR-05, ES-17, ES-25 | `track-dotnet` | `dotnet-r1` | none |
| STORY-205 | Keep secrets out of code, tests and configuration | story | Must | 17 | NFR-05, CS-13, ES-17 | `track-dotnet` | `dotnet-r1` | none |

Item counts by type: epic 1, feature 5, story 6 (`STORY-201`, `STORY-202`, `STORY-203`, `STORY-204`, `STORY-205`, `STORY-206`), enabler 11 (`EN-01`, `EN-02`, `EN-03`, `EN-04`, `EN-05`, `EN-06`, `EN-08`, `EN-09`, `EN-10`, `EN-12`, `EN-13`). Total 23. These match backlog section 3.

## 4. Business and quality requirements covered

The "covered" column is the canonical C1 text for `dotnet-r1`:

> NFR-04 (staff), NFR-05 (.NET), BR-10 (parity), BR-12 (parity)

Several identifiers are **split** so that every item belongs to one track and one release (ES-30, ES-31). This release covers only the part named in brackets; the other parts are in the releases shown.

| Identifier | Priority | Part covered here | Covering story | Supporting items | Other parts of the same identifier |
|---|---|---|---|---|---|
| BR-10 (parity) | Must | What staff see today about the order channel | `STORY-203` | `EN-01` | Portal value: `dotnet-r2`, `STORY-236` |
| BR-12 (parity) | Must | Prices equal today's prices | `STORY-202` | `EN-02`, `EN-10`, `STORY-206` | Customer prices: `dotnet-r2`, `STORY-238` |
| NFR-04 (staff) | Must (A-06) | Staff sign-in through Entra ID | `STORY-204` | `EN-08` | Customers: `dotnet-r2`, `STORY-240`. Azure side: **OPEN:** X-04, not a story. BA-03: unplanned. |
| NFR-05 (.NET) | Must (A-06) | No secret in code, tests or configuration | `STORY-205` | `EN-04` | Azure: `azure-r1` (another track). |

`STORY-206` (time parity) supports `BR-02` and `BR-12`; the coverage of those identifiers is in `dotnet-r2` (`STORY-231`, `STORY-238`), so they are not in the covered list above. Enabler coverage (G-10) is in [traceability.md](../traceability.md). Supplementary: `C-01` and `C-02` are supported through `EPIC-201`.

## 5. What this release leaves out, and where it moves

| Left out | Where it goes | Why |
|---|---|---|
| Everything customer-facing (sign-in for customers, order list, order detail, status, reorder, customer prices, French and English, audit, accessibility, performance: `EPIC-202`) | `dotnet-r2`, 1 Mar to 30 Apr 2027 | Must-only for the 20-customer pilot, apart from the one Should item `STORY-237` (C1, C2; see `dotnet-r2` section 2). |
| `EN-11` authorisation foundation for customer scoping and channel | `dotnet-r2` | Only customer-facing stories need it; it carries the MVE-02 gate for its channel part. |
| `EN-07` invoice store abstraction | `dotnet-r3` | Only `BR-07` (Should) needs it; moved from the research proposal so the pilot carries no invoice work (C2). |
| `EN-14` Order Desk API contract | `dotnet-r3` | No consumer until BA-03 has a team (O-07); moved from the research proposal (C2). |
| Invoices (`BR-07`), user administration (`BR-08`), e-mail (`BR-09`), Dutch (`BR-11`) | `dotnet-r3` | Should and Could items after pilot feedback. |
| Order Desk API implementation (`EPIC-204`, `FEAT-215`, `STORY-280`) | Unplanned; carries only `track-dotnet`. A candidate for `dotnet-r3` when **OPEN:** O-01 is answered. | A conditional item cannot carry a release tag (ES-31). |
| All BA-03 items (`EPIC-301` to `EPIC-304`) | Unplanned, `track-power-platform`; no release exists | No team (G-08, O-07). |
| Azure design and hosting work (`EPIC-101` to `EPIC-104`) | `azure-r1` to `azure-r3` (another track) | Delivered by the Azure team (A-02). |

## 6. Dependencies on other tracks (all OPEN, none is a wait)

**A release never waits for another track** (ES-31, A-45). **`dotnet-r1` proceeds without waiting for the Azure track, the Power Platform track or any other owner.** Every row below is **OPEN:** until its owner confirms it, and each row says how the .NET team keeps delivering meanwhile (local SQL Server, local test identity, console logging, its own pipeline, a decision record). The table lists **every** `X-nn` that an item of this release cites in the backlog (8 ids: X-01, X-02, X-03, X-04, X-07, X-08, X-11, X-14). Rows from C11 and the `EPIC-201` entry are X-03, X-04, X-08, X-11, X-14; X-01, X-02 and X-07 are cited by items only.

"Role" shows the side of `dotnet-r1`: **consumer-side** means this release needs something from another track; **supplier-side** means another track needs something from this release (the row is then carried in the Azure release file of the needing track as that track's **OPEN:** row, and is listed here for completeness, never as a wait).

| Id | **OPEN:** dependency | Role of `dotnet-r1` | Direction | Owner to confirm | How `dotnet-r1` proceeds without waiting | Items |
|---|---|---|---|---|---|---|
| X-01 | Hosting target and pilot test environment for the modernised application | Consumer-side | .NET needs Azure | Ahmed Benali | Build and test locally with a local SQL Server and the sample data (`EN-12`); hosting is not needed to finish this release. | `EN-12`, `STORY-201` |
| X-02 | A `net10.0` application that follows a documented configuration and identity contract | **Supplier-side** | Azure needs .NET | Ahmed Benali | `EN-01`, `EN-03` and `STORY-205` supply it; Azure designs against it (`azure-r1` row). | `EN-01`, `EN-03`, `STORY-205` |
| X-03 | Database sign-in moves from Windows-integrated to Entra ID or a managed identity | Consumer-side and supplier-side | Both | Ahmed Benali | Remove `Integrated Security=SSPI` and `NWSQL01` from configuration (`EN-04`); read the connection setting from user secrets or an environment variable; build and test against a local SQL Server (MVE-A-04, `EN-12`). | `EN-04`, `STORY-205` |
| X-04 (staff) | Staff sign-in moves to Entra ID; the Azure side stays **OPEN:** (O-03) | Consumer-side | .NET needs Azure or IT | Ahmed Benali | Provider-neutral sign-in with a local **test identity** (A-10, `EN-08/AC2`); no real account is needed. | `EN-08`, `STORY-204` |
| X-07 | The in-process session draft must be stateless before scale-out | **Supplier-side** | Azure needs .NET | Ahmed Benali | `EN-06` supplies it; Azure starts with a single instance, as today, until it is done (`azure-r3` row). | `EN-06` |
| X-08 | Logging moves to Application Insights and Log Analytics | Consumer-side | .NET needs Azure | Ahmed Benali | Log through `ILogger<T>` to the console (`EN-05/AC3`); wiring to Azure monitoring is the Azure team's later work. | `EN-05` |
| X-11 | Build and test pipeline (.NET) and deployment pipeline (Azure) | Consumer-side and supplier-side | Both | Ahmed Benali | The .NET team writes its own build and test pipeline (`EN-09`); the pipeline tool is **OPEN:** O-19. The deployment pipeline is Azure's. | `EN-09`, `EN-02` |
| X-14 | One solution and three projects versus a portal area and an API: a decision record is needed | Consumer-side and supplier-side | Both | Ahmed Benali | Write the decision record (`EN-13`) in `docs/architecture/`; no project is added without it (ES-13); the API part is marked **OPEN:** (O-01). | `EN-01`, `EN-13`, `STORY-201` |

Other related questions, **OPEN:** O-03 (rehost .NET Framework 4.8 or wait for `net10.0`, and staff Entra sign-in in BA-01; owner Ahmed Benali), O-19 (pipeline tool; owner Ahmed Benali), O-20 (portal and API project shape; owner Ahmed Benali).

## 7. Entry conditions

These are conditions inside the .NET track and in the governance of this document. None is a wait on another track.

| Id | Condition | Evidence | Status |
|---|---|---|---|
| EN-C1 | Approval and funding to build is given. | **OPEN:** O-21, owner Marc Dubois. The business case says "approved for discovery, not for build". | Not met; the window is a target (A-01). |
| EN-C2 | The product owner has reviewed this file and the backlog items listed in section 3. | Review note in section 10. | Pending |
| EN-C3 | A machine with the .NET 10 SDK and a local SQL Server (Developer edition or container) is available to the team. | `EN-12/AC1`; MVE-A-04. | **ASSUMPTION:** A-D1-01. Owner Ahmed Benali. |
| EN-C4 | The existing 28 test assertions, 15 of them on pricing, are the baseline that must be preserved. | CS-20, ES-18, `EN-02/AC2`. | Known |
| EN-C5 | No change is made to the namespaces, domain types or behaviour of Order Desk unless a decision record explains it. | ES-19, `STORY-201/AC3`. | Known |

## 8. Exit and acceptance criteria

The release is ready for approval only when **every** criterion below is met. Each is testable and tied to a story or enabler in section 3; the Given / When / Then wording is in [backlog.md](../backlog.md) under the criterion id. "Done" here means the code and tests pass on a developer machine or a build runner. No deployment is claimed (ES-27).

| Id | Exit criterion | Tested by | Items |
|---|---|---|---|
| EX-1 | `dotnet build src/Northwind.OrderDesk.sln` succeeds; `Core`, `Tests` and `Web` build as SDK-style projects on `net10.0`; one solution, the same three projects, no `packages.config`. | `EN-01/AC1`, `EN-01/AC2`, `STORY-201/AC1` | `EN-01`, `EN-08`, `STORY-201` |
| EX-2 | `dotnet test src/Northwind.OrderDesk.sln` runs and **passes on Windows, macOS and Linux**. All existing test assertions are kept and none is weakened (ES-18, CS-20). | `EN-02/AC1`, `EN-02/AC2`, `EN-02/AC3` | `EN-02` |
| EX-3 | **Pricing parity.** For the same customer, product, quantity and date the modernised price equals today's price, including customer-negotiated prices and volume discounts. The pricing checks pass under `dotnet test src/Northwind.OrderDesk.sln`. A difference of even one cent is a defect and blocks approval (CS-20, ES-18). | `STORY-202/AC1`, `STORY-202/AC2`, `STORY-202/AC3` | `STORY-202`, `EN-02`, `EN-10` |
| EX-4 | **Time parity.** Order dates, the 24-month window and price-agreement validity give identical results with the host time zone set to UTC and to Central European time; a price agreement ending at midnight local time is valid one minute before and not after. The rule says whether times are stored in UTC or local time (**ASSUMPTION:** A-24). | `EN-10/AC1`, `EN-10/AC2`, `EN-10/AC3`, `STORY-206/AC1`, `STORY-206/AC2`, `STORY-206/AC3` | `EN-10`, `STORY-206` |
| EX-5 | **Unchanged staff screens.** Each existing staff screen shows the same fields and behaves as before, shown by a regression checklist. A difference is a defect and the release is not approved until it is fixed or the product owner accepts it. | `STORY-201/AC2`, `STORY-201/AC4`, `EN-08/AC1` | `STORY-201`, `EN-08` |
| EX-6 | **Channel parity.** Staff see the channel of an order as entered by staff or as portal; an empty channel value does not fail the screen and any difference from today is listed. | `STORY-203/AC1`, `STORY-203/AC2`, `STORY-203/AC3` | `STORY-203` |
| EX-7 | **Staff sign-in (`NFR-04`).** A staff member with a Northwind Entra ID account reaches Order Desk (a local test identity is used here); an account that is not a Northwind staff account is refused; no Windows Integrated Authentication remains. | `STORY-204/AC1`, `STORY-204/AC2`, `STORY-204/AC3`, `EN-08/AC2`, `EN-08/AC3` | `STORY-204`, `EN-08` |
| EX-8 | **No secrets (`NFR-05`).** A scan of source and configuration files, including tests, finds no password, key or connection string with a password; `Integrated Security=SSPI` and `NWSQL01` appear in no configuration file; the pipeline definition and the local-data recipe hold no secret. A found secret blocks approval. This scan is part of the release exit criteria (PRD `NFR-05` measurement rule, A-54). | `STORY-205/AC1`, `STORY-205/AC2`, `STORY-205/AC3`, `EN-04/AC1`, `EN-04/AC2`, `EN-04/AC3`, `EN-09/AC3`, `EN-12/AC3` | `STORY-205`, `EN-04`, `EN-09`, `EN-12` |
| EX-9 | **Automated build and test.** A change to the solution is built and tested by the pipeline with `dotnet test src/Northwind.OrderDesk.sln`; a failing build or test blocks the change. | `EN-09/AC1`, `EN-09/AC2` | `EN-09` |
| EX-10 | **Settings, logging and drafts.** No direct `ConfigurationManager` call, no Windows Event Log write and no `InProc` session order draft remain; a missing required setting stops start-up with a message that names the setting and prints no secret; an order draft survives a restart. | `EN-03/AC1` to `EN-03/AC3`, `EN-05/AC1` to `EN-05/AC3`, `EN-06/AC1` to `EN-06/AC3` | `EN-03`, `EN-05`, `EN-06` |
| EX-11 | **Local data.** A clean machine with a local SQL Server can build the sample database from `database/` and run the solution against it; the data holds orders for at least two customers and no real or personal data. | `EN-12/AC1`, `EN-12/AC2` | `EN-12` |
| EX-12 | **Decision record.** The record on portal and API project shape exists in `docs/architecture/`; the Order Desk API part is marked **OPEN:** (O-01). | `EN-13/AC1`, `EN-13/AC2`, `EN-13/AC3` | `EN-13` |
| EX-13 | **Tags.** Every item in section 3 carries `track-dotnet` and `dotnet-r1`, and no item of this release appears in another release file. | Mechanical check of the backlog item register for tags and release membership | all 23 items |

Not part of the exit: any deployment, any hosting decision, any customer-facing behaviour, and the result of MVE-02 (not run, pending).

## 9. Assumptions and OPEN items relevant to this release

Ids and wording come from the backlog registers (backlog section 7, the register of record); owners are the confirming owners there. `G-` ids are gaps from the intake review, `T-` ids are tensions defined in PRD section 11, and `OQ-` ids are business-case open questions carried as the O- rows for those questions in backlog section 7.2.

| Id | Kind | Text (short) | Owner |
|---|---|---|---|
| A-01 | **ASSUMPTION:** | Build starts December 2026 after approval; windows are targets. | Marc Dubois |
| A-02 | **ASSUMPTION:** | .NET owns Order Desk code changes; Azure owns hosting, IaC, DR, monitoring and the C-04 cost model. | Ahmed Benali |
| A-06 | **ASSUMPTION:** | MoSCoW from the business case, then date and dependency risk; NFRs are Must. | Lena Varga |
| A-10 | **ASSUMPTION:** | Customer and staff sign-in is provider-neutral; a test identity is used locally. | Ahmed Benali |
| A-24 | **ASSUMPTION:** | Azure runs in UTC by default; Order Desk stores local time; parity needs explicit handling (from the code, not `knowledge-docs`). | Ahmed Benali |
| A-39 | **ASSUMPTION:** | Documents only: no deployment, no commit, no Git tags until approval. | Marc Dubois |
| A-38 | **ASSUMPTION:** | The release approver per track is the product owner (Lena Varga), with Marc Dubois as escalation. | Marc Dubois |
| A-42 | **ASSUMPTION:** | A target window is the period by which content is complete and ready to approve. | Marc Dubois |
| A-45 | **ASSUMPTION:** | Cross-track needs are **OPEN:** rows and never a wait. | Ahmed Benali |
| A-46 | **ASSUMPTION:** | Rank: enablers before the features that need them, then Must, Should, Could. | Lena Varga |
| A-49 | **ASSUMPTION:** | An enabler takes the highest priority of the requirements it serves in its own track. An enabler that protects an `NFR-` is Must (A-06). An enabler that serves only another track's requirements is Should (so `EN-14` and `FR-240` are Should). | Lena Varga |
| A-51 | **ASSUMPTION:** | Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. | Ahmed Benali |
| A-54 | **ASSUMPTION:** | The measurement rules for `NFR-03` to `NFR-09` are the author's proposals. | Ahmed Benali, Lena Varga |
| A-D1-01 | **ASSUMPTION:** (release-local; this file is its register) | The team has a .NET 10 SDK and a local SQL Server for the exit tests; no cloud resource is needed to finish this release. Not stated in `knowledge-docs`. | Ahmed Benali |
| A-D1-02 | **ASSUMPTION:** (release-local; this file is its register) | The regression checklist for the staff screens (`STORY-201/AC2`) is written by the .NET team from the current screens and reviewed by the product owner; the backlog does not name an author. | Ahmed Benali |
| MVE-A-04 | **ASSUMPTION:** | A local SQL Server (Developer edition or container) is available to run the database scripts. | Ahmed Benali |
| O-03 | **OPEN:** | Rehost .NET Framework 4.8 or wait for `net10.0` in `azure-r1`; is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-06 | **OPEN:** | Which backlog tool and which ES-28 prefix; item types and fields in a tool are not validated. | Lena Varga |
| O-07 | **OPEN:** | Who is the BA-03 team, what are their skills, and what is the intended date (or is BA-03 unplanned)? | Lena Varga, Marc Dubois |
| O-09 | **OPEN:** | Who is the named release approver for the .NET track? | Marc Dubois |
| O-19 | **OPEN:** | Which build and deployment pipeline tool (`EN-09`)? | Ahmed Benali |
| O-20 | **OPEN:** | Decision record on the portal and API project shape (`EN-13`, ES-13). | Ahmed Benali |
| O-21 | **OPEN:** | Approval and funding to build. | Marc Dubois |
| O-25 | **OPEN:** | Confirm release counts, windows and the three placement changes (C2). | Lena Varga, Marc Dubois |
| O-01 | **OPEN:** | Who owns the Order Desk API? Only the API part of `EN-13` depends on it. | Ahmed Benali |
| T-10 | Tension | ES-13 and ES-19 versus a portal, an API and a re-platform (`EN-13`). | Ahmed Benali |

## 10. Approval and tagging procedure

Nothing below has happened. The Git tag does not exist, and no commit was made for this release (A-39).

1. **Review.** The approver reads this file, the 23 items in [backlog.md](../backlog.md) and the exit criteria in section 8, and records review comments with the review owner. Approver: **OPEN:** O-09 (owner Marc Dubois).
2. **Approve.** Only a human approver may approve. The approver's name and the approval date are written in the block below. This file changes from `Proposed` to `Approved` only at that point.
3. **Commit.** After approval, and only then, a human-initiated, gated step commits the approved release files together with the items they list.
4. **Tag.** After the commit exists, a human-initiated, gated step creates the Git tag `product/dotnet-r1` on that commit (ES-31). Pushing the tag is a separate decision.
5. **Check.** `git tag -l 'product/dotnet-r1'` then lists the tag. Until step 4, the same command returns nothing.

| Approval block | |
|---|---|
| Approver | **OPEN:** O-09 |
| Approval decision | (blank) |
| Approval date | (blank) |
| Planned Git tag | `product/dotnet-r1` — **to be created after approval; not created** |
| Commit holding the approved release | (blank; not committed) |

## 11. Publication note (ES-39)

When the backlog is published to a tool, the track and release tags travel with every item of this release so the release stays identifiable. Nothing is published, no tool was contacted, and **OPEN:** O-06 (owner Lena Varga) says no tool or ES-28 prefix is chosen, so item types and fields are not validated (`needs_review`).

| Tool | Track tag | Release tag | Grouping |
|---|---|---|---|
| Azure DevOps | work-item tag `track-dotnet` | work-item tag `dotnet-r1` | tags only |
| GitHub | issue label `track-dotnet` | issue label `dotnet-r1` | milestone `dotnet-r1` |
| Jira | label `track-dotnet` | label `dotnet-r1` | fix version `dotnet-r1` |

Titles, descriptions and source ids follow ES-28 and ES-29 in every tool (`nw-workshop` tag and the participant prefix agreed with the facilitator).

## 12. Sources

* [backlog.md](../backlog.md) sections 1.1, 2.2, 3, 4.2, 5 and 7: items, ids, tags, priorities, ranks, acceptance criteria, registers.
* [traceability.md](../traceability.md): split identifiers and enabler coverage.
* [product-requirements.md](../product-requirements.md): release plan, `NFR-05` measurement rule, `X-nn` rows.
* [experiments.md](../experiments.md): MVE-02 gate and decisions (not run).
* `knowledge-docs/engineering-standards.md`: ES-13 to ES-19, ES-27, ES-28, ES-29, ES-30, ES-31, ES-39.
* `knowledge-docs/current-state.md`: CS-01, CS-02, CS-04, CS-13 to CS-20.
