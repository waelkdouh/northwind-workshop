<!-- markdownlint-disable-file -->
# Azure DevOps publication preview: Northwind Traders releases (READ-ONLY)

> **Nothing has been created, updated or linked in Azure DevOps.** This is a preview. It needs your approval before any write (section I).
> Source: `docs/product/backlog.md` (BACKLOG-NW-001 v0.1.0), the six release files and `traceability.md`, copied by `build_ado_payload.py`.
> Machine-readable twin: `ado-publish-payload.json` (same folder). Date of this preview: 2026-11-17.

## A. Target and scope summary

| Field | Value |
|---|---|
| Organization / project | `waelconsulting` / `northwind-workshop` (**needs_review**: not verified, see section F) |
| Participant prefix (ES-28) | `wael-01`. Every title starts with `wael-01 ` |
| Tags on every item (ES-28, ES-30, ES-31, ES-39) | `nw-workshop`, exactly one track tag, and exactly one release tag when the item is planned in a release |
| Scope | The 111 items planned in the six releases: 7 epics, 28 features, 76 user stories (of which 30 are enablers `EA-`/`EN-`, published as User Story per backlog section 6.1) |
| Out of scope (optional add-on, section G) | 33 unplanned items: 30 Power Platform and 3 .NET (`EPIC-204`, `FEAT-215`, `STORY-280`) |
| Acceptance criteria | 245 criteria on 76 stories and enablers. Epics and features have none in the backlog |
| Hyperlinks | 499 link operations (average 4.5 per item), section E |
| Git evidence | The six tags `product/azure-r1` to `product/dotnet-r3` exist on `origin` and point to commit `5ad7971`. `docs/` and `knowledge-docs/` have not changed since that commit. `origin/main` equals local `HEAD` (`e56447b`) |
| Documentation base URL | `https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/<file>` |

### Counts by track, release and type

| Track | Release | Epics | Features | User Stories | of which enablers | Total |
|---|---|---|---|---|---|---|
| Azure | `azure-r1` | 2 | 5 | 14 | 6 | 21 |
| Azure | `azure-r2` | 1 | 5 | 14 | 7 | 20 |
| Azure | `azure-r3` | 1 | 4 | 8 | 3 | 13 |
| **Azure total** | | **4** | **14** | **36** | **16** | **54** |
| .NET | `dotnet-r1` | 1 | 5 | 17 | 11 | 23 |
| .NET | `dotnet-r2` | 1 | 5 | 15 | 1 | 21 |
| .NET | `dotnet-r3` | 1 | 4 | 8 | 2 | 13 |
| **.NET total** | | **3** | **14** | **40** | **14** | **57** |
| **All planned** | | **7** | **28** | **76** | **30** | **111** |

These counts equal backlog section 3 (Azure 54 = 21 + 20 + 13; .NET planned 57 = 23 + 21 + 13). The backlog has 144 items in total: 111 planned plus 33 unplanned.

### Checks run on the payload by the script (all must pass)

| Result | Check | Detail |
|---|---|---|
| PASS | no id is duplicated | 144 records, 144 unique ids |
| PASS | every line of every item block was recognised by the parser | 0 unrecognised: [] |
| PASS | 144 items parsed and equal to the item register (section 2) | parsed 144, register 144 |
| PASS | counts per track/release/type equal backlog section 3 | azure-r1/track-azure epics,features,stories,enablers=(2, 5, 8, 6); azure-r2/track-azure epics,features,stories,enablers=(1, 5, 7, 7); azure-r3/track-azure epics,features,stories,enablers=(1, 4, 5, 3); dotnet-r1/track-dotnet epics,features,stories,enablers=(1, 5, 6, 11); dotnet-r2/track-dotnet epics, |
| PASS | planned = 111 (azure 54, dotnet 57) | planned 111 |
| PASS | unplanned = 33 (power platform 30, .NET 3 incl. EPIC-204) | unplanned 33 |
| PASS | planned: nw-workshop + exactly one track tag + exactly one release tag | [] |
| PASS | unplanned: nw-workshop + exactly one track tag + no release tag | [] |
| PASS | every title starts with 'wael-01 ' |  |
| PASS | title lengths | longest published title 101 chars (ADO limit 255); longest backlog title 84 (BD-04 limit 100) |
| PASS | title = 'wael-01 ' + published title of backlog section 6.2 |  |
| PASS | tags = nw-workshop + tags of backlog section 6.2 |  |
| PASS | block fields (title, tags, priority, rank) equal item register of section 2 | [] |
| PASS | every description begins with the item id and contains source ids | [] |
| PASS | every description carries the '(source: ...)' cite (ES-02, ES-29) |  |
| PASS | every story and enabler has >= 2 acceptance criteria | [] |
| PASS | every criterion id is '<item id>/AC<n>' (contiguous) and in Given/When/Then form | [] |
| PASS | epics and features carry no acceptance criteria in the backlog |  |
| PASS | every parent exists, has the right level, and shares track and release | [] |
| PASS | Contains/Features lists equal the children found by Parent | [] |
| PASS | every planned item id is named in its release file | missing: [] |
| PASS | operation order creates every parent before its children |  |
| PASS | Guards 1, 2, 3, 5: no #nnn references, @mentions, images or URLs, .copilot-tracking paths, planning ids or template placeholders in outbound text | [] |
| PASS | Guard 6: no secret or credential indicator in outbound text | [] |
| PASS | every cited A-/O-/X-/T-/G- id resolves in backlog section 7 | {} |

## B. Proposed operations, in order

Tool names below are the ones the Azure DevOps remote MCP server normally offers. **needs_review:** the server `ado-remote-mcp` is declared in `.mcp.json`, but none of its tools could be called in this session (section F), so names and parameters are not confirmed. No call below has been made.

| Step | Operation | Tool (needs_review) | Calls | Notes |
|---|---|---|---|---|
| 0 | Read-only checks before any write: project, process, work item types, fields, duplicates, tag permission | `core_list_projects`, `wit_get_work_item_type`, `wit_query`, `search_workitem` | about 6 to 10 reads | Section F lists each check. Stop if one fails. |
| 1 | Create the 7 epics (type `Epic`) with title, tags, description, priority | `wit_create_work_item` | 7 | Parents first. One call per item. No parent. Record each returned id against its `localId`. |
| 2 | Create the 28 features (type `Feature`) | `wit_create_work_item` | 28 | Then link each feature to its epic (step 2b). |
| 2b | Parent link feature to epic | `wit_work_items_link` (type `parent`) | 28 link operations (1 call per batch if the tool accepts a list; else 28 calls) | One hierarchical parent per item (ES-30 splits cross-track stories, so no feature needs a second parent). |
| 3 | Create the 76 user stories (backlog stories and enablers, type `User Story`) with `Microsoft.VSTS.Common.AcceptanceCriteria` | `wit_create_work_item` | 76 | Then link each story to its feature (step 3b). |
| 3b | Parent link story to feature | `wit_work_items_link` (type `parent`) | 76 link operations (batched or one call each) | |
| 4 | Add the 499 documentation hyperlinks (Hyperlink relation with a comment) | `wit_update_work_item` (add `/relations/-`, `rel: Hyperlink`) or `wit_update_work_items_batch` | 111 (one per item) or fewer when batched | Section E gives the URL and comment per item. |
| 5 | Read back every created item and compare title, tags, parent and field text with the payload | `wit_get_work_items_batch_by_ids` | about 5 to 12 reads | Report any difference. Nothing is fixed without a new approval. |

**Totals if nothing is batched:** 111 creates + 104 parent links + 111 hyperlink updates = **326 write calls**, plus reads. Batching can lower the link and hyperlink calls. The order is fixed: epics, then features, then stories, then hyperlinks. A parent is always created before its child (checked: yes).

Fields written per item (all **needs_review** until section F is done): `System.Title`, `System.Tags` (semicolon separated), `System.Description` (HTML), `Microsoft.VSTS.Common.Priority` (proposed Must=1, Should=2, Could=3), and for User Stories `Microsoft.VSTS.Common.AcceptanceCriteria` (HTML). If that field does not exist on the type, the criteria move into the description (payload field `descriptionWithAcceptanceCriteriaHtmlFallback`). `Microsoft.VSTS.Common.StackRank` is **not** proposed by default (see risk R5).

Content guards (backlog-management skill) applied to every outbound text: no `.copilot-tracking/` paths, no planning reference ids (`WI001`), no `{{TEMP-n}}` placeholders, no `#nnn` references, `@` mentions, images or URLs inside descriptions, no secret indicators. The backlog ids (`EPIC-101`, `STORY-104`, `EA-01`) stay because you asked for them (ES-29). All checks passed (section A).

## C. All 111 items

Doc link codes: **BRD** business requirements, **PRD** product requirements, **EXP** experiments, **TRC** traceability, **REL** release file, **BKL** backlog entry (anchor). Full URLs are in section E.

| # | localId | ADO type | Exact title | Tags | Parent | Release | Doc links |
|---|---|---|---|---|---|---|---|
| 1 | `EPIC-101` | Epic | wael-01 EPIC-101 Azure foundation and security baseline | `nw-workshop; track-azure; azure-r1` | none | `azure-r1` | BRD PRD REL EXP BKL |
| 2 | `EPIC-102` | Epic | wael-01 EPIC-102 Data platform decision, cost and migration approach | `nw-workshop; track-azure; azure-r1` | none | `azure-r1` | BRD PRD REL EXP BKL |
| 3 | `EPIC-103` | Epic | wael-01 EPIC-103 Pilot environment, exchange, storage and observability | `nw-workshop; track-azure; azure-r2` | none | `azure-r2` | BRD PRD REL EXP BKL |
| 4 | `EPIC-104` | Epic | wael-01 EPIC-104 Cutover and recovery proof | `nw-workshop; track-azure; azure-r3` | none | `azure-r3` | BRD PRD REL EXP BKL |
| 5 | `EPIC-201` | Epic | wael-01 EPIC-201 Modernise Order Desk to .NET 10 with parity | `nw-workshop; track-dotnet; dotnet-r1` | none | `dotnet-r1` | BRD PRD REL EXP BKL |
| 6 | `EPIC-202` | Epic | wael-01 EPIC-202 Customer portal pilot: sign-in, orders, status, reorder | `nw-workshop; track-dotnet; dotnet-r2` | none | `dotnet-r2` | BRD PRD REL EXP BKL |
| 7 | `EPIC-203` | Epic | wael-01 EPIC-203 Complete the portal and publish the Order Desk API contract | `nw-workshop; track-dotnet; dotnet-r3` | none | `dotnet-r3` | BRD PRD REL EXP BKL |
| 8 | `FEAT-101` | Feature | wael-01 FEAT-101 Environment foundation as code and validation | `nw-workshop; track-azure; azure-r1` | `EPIC-101` | `azure-r1` | PRD REL BKL |
| 9 | `FEAT-102` | Feature | wael-01 FEAT-102 Hybrid connectivity design | `nw-workshop; track-azure; azure-r1` | `EPIC-101` | `azure-r1` | PRD REL BKL |
| 10 | `FEAT-103` | Feature | wael-01 FEAT-103 Secrets, identity and private access | `nw-workshop; track-azure; azure-r1` | `EPIC-101` | `azure-r1` | PRD REL BKL |
| 11 | `FEAT-104` | Feature | wael-01 FEAT-104 Data tier decision | `nw-workshop; track-azure; azure-r1` | `EPIC-102` | `azure-r1` | PRD REL EXP BKL |
| 12 | `FEAT-105` | Feature | wael-01 FEAT-105 Cost model and migration approach | `nw-workshop; track-azure; azure-r1` | `EPIC-102` | `azure-r1` | PRD REL EXP BKL |
| 13 | `FEAT-113` | Feature | wael-01 FEAT-113 Application hosting | `nw-workshop; track-azure; azure-r2` | `EPIC-103` | `azure-r2` | PRD REL EXP BKL |
| 14 | `FEAT-106` | Feature | wael-01 FEAT-106 StockPilot exchange, invoice storage and outbound mail | `nw-workshop; track-azure; azure-r2` | `EPIC-103` | `azure-r2` | PRD REL EXP BKL |
| 15 | `FEAT-107` | Feature | wael-01 FEAT-107 Observability and alerting | `nw-workshop; track-azure; azure-r2` | `EPIC-103` | `azure-r2` | PRD REL BKL |
| 16 | `FEAT-108` | Feature | wael-01 FEAT-108 Test environment for the portal pilot | `nw-workshop; track-azure; azure-r2` | `EPIC-103` | `azure-r2` | PRD REL BKL |
| 17 | `FEAT-109` | Feature | wael-01 FEAT-109 Backup, retention and recovery design | `nw-workshop; track-azure; azure-r2` | `EPIC-103` | `azure-r2` | PRD REL EXP BKL |
| 18 | `FEAT-114` | Feature | wael-01 FEAT-114 Database migration and rehearsal | `nw-workshop; track-azure; azure-r3` | `EPIC-104` | `azure-r3` | PRD REL EXP BKL |
| 19 | `FEAT-110` | Feature | wael-01 FEAT-110 Cutover and rollback runbooks | `nw-workshop; track-azure; azure-r3` | `EPIC-104` | `azure-r3` | PRD REL BKL |
| 20 | `FEAT-111` | Feature | wael-01 FEAT-111 Recovery and availability proof | `nw-workshop; track-azure; azure-r3` | `EPIC-104` | `azure-r3` | PRD REL BKL |
| 21 | `FEAT-112` | Feature | wael-01 FEAT-112 Decommission of the old servers | `nw-workshop; track-azure; azure-r3` | `EPIC-104` | `azure-r3` | PRD REL BKL |
| 22 | `FEAT-201` | Feature | wael-01 FEAT-201 Modernise projects and web layer | `nw-workshop; track-dotnet; dotnet-r1` | `EPIC-201` | `dotnet-r1` | PRD REL BKL |
| 23 | `FEAT-202` | Feature | wael-01 FEAT-202 Test, build and local data | `nw-workshop; track-dotnet; dotnet-r1` | `EPIC-201` | `dotnet-r1` | PRD REL BKL |
| 24 | `FEAT-203` | Feature | wael-01 FEAT-203 Pricing, channel and time parity | `nw-workshop; track-dotnet; dotnet-r1` | `EPIC-201` | `dotnet-r1` | PRD REL BKL |
| 25 | `FEAT-204` | Feature | wael-01 FEAT-204 Staff sign-in with Entra ID | `nw-workshop; track-dotnet; dotnet-r1` | `EPIC-201` | `dotnet-r1` | PRD REL BKL |
| 26 | `FEAT-205` | Feature | wael-01 FEAT-205 Secret-free configuration | `nw-workshop; track-dotnet; dotnet-r1` | `EPIC-201` | `dotnet-r1` | PRD REL BKL |
| 27 | `FEAT-206` | Feature | wael-01 FEAT-206 Customer sign-in, company isolation and data residency | `nw-workshop; track-dotnet; dotnet-r2` | `EPIC-202` | `dotnet-r2` | PRD REL BKL |
| 28 | `FEAT-207` | Feature | wael-01 FEAT-207 Order list, order detail and status | `nw-workshop; track-dotnet; dotnet-r2` | `EPIC-202` | `dotnet-r2` | PRD REL EXP BKL |
| 29 | `FEAT-208` | Feature | wael-01 FEAT-208 Reorder, submit and channel | `nw-workshop; track-dotnet; dotnet-r2` | `EPIC-202` | `dotnet-r2` | PRD REL EXP BKL |
| 30 | `FEAT-209` | Feature | wael-01 FEAT-209 Customer prices and language | `nw-workshop; track-dotnet; dotnet-r2` | `EPIC-202` | `dotnet-r2` | PRD REL EXP BKL |
| 31 | `FEAT-210` | Feature | wael-01 FEAT-210 Audit, accessibility and performance | `nw-workshop; track-dotnet; dotnet-r2` | `EPIC-202` | `dotnet-r2` | PRD REL BKL |
| 32 | `FEAT-211` | Feature | wael-01 FEAT-211 Invoice download | `nw-workshop; track-dotnet; dotnet-r3` | `EPIC-203` | `dotnet-r3` | PRD REL BKL |
| 33 | `FEAT-212` | Feature | wael-01 FEAT-212 Customer user administration and shipping e-mail | `nw-workshop; track-dotnet; dotnet-r3` | `EPIC-203` | `dotnet-r3` | PRD REL BKL |
| 34 | `FEAT-213` | Feature | wael-01 FEAT-213 Dutch and success-measure data | `nw-workshop; track-dotnet; dotnet-r3` | `EPIC-203` | `dotnet-r3` | PRD REL EXP BKL |
| 35 | `FEAT-214` | Feature | wael-01 FEAT-214 Order Desk API contract | `nw-workshop; track-dotnet; dotnet-r3` | `EPIC-203` | `dotnet-r3` | PRD REL BKL |
| 36 | `EA-01` | User Story (enabler) | wael-01 EA-01 Build the Azure foundation as code (naming, tags, region, modules) | `nw-workshop; track-azure; azure-r1` | `FEAT-101` | `azure-r1` | PRD BRD TRC REL BKL |
| 37 | `EA-11` | User Story (enabler) | wael-01 EA-11 Build the infrastructure validation and deployment pipeline design | `nw-workshop; track-azure; azure-r1` | `FEAT-101` | `azure-r1` | PRD TRC REL BKL |
| 38 | `STORY-101` | User Story | wael-01 STORY-101 Review a test and production environment design set | `nw-workshop; track-azure; azure-r1` | `FEAT-101` | `azure-r1` | PRD TRC REL BKL |
| 39 | `STORY-104` | User Story | wael-01 STORY-104 Keep every Azure resource in an EU region | `nw-workshop; track-azure; azure-r1` | `FEAT-101` | `azure-r1` | PRD BRD TRC REL BKL |
| 40 | `STORY-105` | User Story | wael-01 STORY-105 Validate every infrastructure definition locally before release | `nw-workshop; track-azure; azure-r1` | `FEAT-101` | `azure-r1` | PRD TRC REL BKL |
| 41 | `EA-02` | User Story (enabler) | wael-01 EA-02 Design hybrid connectivity between Lyon, Azure and Antwerp | `nw-workshop; track-azure; azure-r1` | `FEAT-102` | `azure-r1` | PRD TRC REL BKL |
| 42 | `STORY-102` | User Story | wael-01 STORY-102 Agree the connection design for the move and after the lease | `nw-workshop; track-azure; azure-r1` | `FEAT-102` | `azure-r1` | PRD TRC REL BKL |
| 43 | `EA-03` | User Story (enabler) | wael-01 EA-03 Design secrets, managed identities and private endpoints | `nw-workshop; track-azure; azure-r1` | `FEAT-103` | `azure-r1` | PRD BRD TRC REL BKL |
| 44 | `STORY-103` | User Story | wael-01 STORY-103 Keep secrets out of Azure-hosted code and configuration | `nw-workshop; track-azure; azure-r1` | `FEAT-103` | `azure-r1` | PRD BRD TRC REL BKL |
| 45 | `EA-05` | User Story (enabler) | wael-01 EA-05 Record the data-tier decision and migration approach | `nw-workshop; track-azure; azure-r1` | `FEAT-104` | `azure-r1` | PRD TRC REL EXP BKL |
| 46 | `STORY-120` | User Story | wael-01 STORY-120 Decide the data tier for the order database | `nw-workshop; track-azure; azure-r1` | `FEAT-104` | `azure-r1` | PRD BRD TRC REL EXP BKL |
| 47 | `EA-09` | User Story (enabler) | wael-01 EA-09 Build the Azure cost model against the monthly cap | `nw-workshop; track-azure; azure-r1` | `FEAT-105` | `azure-r1` | PRD TRC REL EXP BKL |
| 48 | `STORY-121` | User Story | wael-01 STORY-121 Show the monthly cost against the EUR 1,500 cap | `nw-workshop; track-azure; azure-r1` | `FEAT-105` | `azure-r1` | PRD TRC REL EXP BKL |
| 49 | `STORY-122` | User Story | wael-01 STORY-122 Define the database and invoice migration approach | `nw-workshop; track-azure; azure-r1` | `FEAT-105` | `azure-r1` | PRD BRD TRC REL EXP BKL |
| 50 | `EA-15` | User Story (enabler) | wael-01 EA-15 Host the Order Desk web application in the test and production environments | `nw-workshop; track-azure; azure-r2` | `FEAT-113` | `azure-r2` | PRD BRD TRC REL EXP BKL |
| 51 | `EA-06` | User Story (enabler) | wael-01 EA-06 Redesign the StockPilot exchange without changing the file contract | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD TRC REL EXP BKL |
| 52 | `EA-07` | User Story (enabler) | wael-01 EA-07 Design invoice storage and synchronisation | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD TRC REL BKL |
| 53 | `EA-12` | User Story (enabler) | wael-01 EA-12 Design outbound mail to replace the on-premises relay | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD BRD TRC REL BKL |
| 54 | `STORY-140` | User Story | wael-01 STORY-140 Keep the nightly StockPilot exchange working after the database moves | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD BRD TRC REL EXP BKL |
| 55 | `STORY-141` | User Story | wael-01 STORY-141 Decide where invoice files live after the lease | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD TRC REL BKL |
| 56 | `STORY-144` | User Story | wael-01 STORY-144 Replace the on-premises mail relay for outbound e-mail | `nw-workshop; track-azure; azure-r2` | `FEAT-106` | `azure-r2` | PRD BRD TRC REL BKL |
| 57 | `EA-04` | User Story (enabler) | wael-01 EA-04 Build observability: log workspace, application monitoring and alerts | `nw-workshop; track-azure; azure-r2` | `FEAT-107` | `azure-r2` | PRD BRD TRC REL BKL |
| 58 | `STORY-142` | User Story | wael-01 STORY-142 Monitor availability with a synthetic probe and alerts | `nw-workshop; track-azure; azure-r2` | `FEAT-107` | `azure-r2` | PRD BRD TRC REL BKL |
| 59 | `EA-10` | User Story (enabler) | wael-01 EA-10 Define the tst environment | `nw-workshop; track-azure; azure-r2` | `FEAT-108` | `azure-r2` | PRD TRC REL BKL |
| 60 | `STORY-143` | User Story | wael-01 STORY-143 Define a test environment where the portal pilot can run | `nw-workshop; track-azure; azure-r2` | `FEAT-108` | `azure-r2` | PRD TRC REL BKL |
| 61 | `EA-08` | User Story (enabler) | wael-01 EA-08 Design backup, long-term retention and recovery | `nw-workshop; track-azure; azure-r2` | `FEAT-109` | `azure-r2` | PRD BRD TRC REL EXP BKL |
| 62 | `STORY-145` | User Story | wael-01 STORY-145 Keep order-change records for 7 years in Azure | `nw-workshop; track-azure; azure-r2` | `FEAT-109` | `azure-r2` | PRD BRD TRC REL EXP BKL |
| 63 | `STORY-146` | User Story | wael-01 STORY-146 Design backup and recovery for RPO 1 hour and RTO 4 hours | `nw-workshop; track-azure; azure-r2` | `FEAT-109` | `azure-r2` | PRD BRD TRC REL EXP BKL |
| 64 | `EA-16` | User Story (enabler) | wael-01 EA-16 Migrate the NorthwindOrders database to the chosen data tier and rehearse the move | `nw-workshop; track-azure; azure-r3` | `FEAT-114` | `azure-r3` | PRD BRD TRC REL EXP BKL |
| 65 | `EA-13` | User Story (enabler) | wael-01 EA-13 Write cutover, rollback and decommission runbooks | `nw-workshop; track-azure; azure-r3` | `FEAT-110` | `azure-r3` | PRD BRD TRC REL BKL |
| 66 | `STORY-170` | User Story | wael-01 STORY-170 Keep staff working through the cutover inside the Sunday window | `nw-workshop; track-azure; azure-r3` | `FEAT-110` | `azure-r3` | PRD BRD TRC REL BKL |
| 67 | `STORY-171` | User Story | wael-01 STORY-171 Define rollback and rehearsal for every cutover step | `nw-workshop; track-azure; azure-r3` | `FEAT-110` | `azure-r3` | PRD BRD TRC REL BKL |
| 68 | `EA-14` | User Story (enabler) | wael-01 EA-14 Write the first recovery test plan and evidence template | `nw-workshop; track-azure; azure-r3` | `FEAT-111` | `azure-r3` | PRD BRD TRC REL BKL |
| 69 | `STORY-172` | User Story | wael-01 STORY-172 Prove recovery against RPO 1 hour and RTO 4 hours | `nw-workshop; track-azure; azure-r3` | `FEAT-111` | `azure-r3` | PRD BRD TRC REL BKL |
| 70 | `STORY-173` | User Story | wael-01 STORY-173 Plan the availability proof for the first weeks in Azure | `nw-workshop; track-azure; azure-r3` | `FEAT-111` | `azure-r3` | PRD BRD TRC REL BKL |
| 71 | `STORY-174` | User Story | wael-01 STORY-174 Retire the old web and database servers before 30 June 2027 | `nw-workshop; track-azure; azure-r3` | `FEAT-112` | `azure-r3` | PRD TRC REL BKL |
| 72 | `EN-01` | User Story (enabler) | wael-01 EN-01 Convert the solution to SDK-style projects on net10.0 | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 73 | `EN-13` | User Story (enabler) | wael-01 EN-13 Record the decision on portal and API project shape | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 74 | `EN-03` | User Story (enabler) | wael-01 EN-03 Replace direct ConfigurationManager calls with the options pattern | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 75 | `EN-05` | User Story (enabler) | wael-01 EN-05 Replace the Windows Event Log logger with standard logging | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 76 | `EN-06` | User Story (enabler) | wael-01 EN-06 Replace the in-process session order draft | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 77 | `EN-08` | User Story (enabler) | wael-01 EN-08 Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 78 | `STORY-201` | User Story | wael-01 STORY-201 Run Order Desk on .NET 10 with unchanged staff screens | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-201` | `dotnet-r1` | PRD TRC REL BKL |
| 79 | `EN-02` | User Story (enabler) | wael-01 EN-02 Replace MSTest v1 so all tests run on Windows, macOS and Linux | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-202` | `dotnet-r1` | PRD TRC REL BKL |
| 80 | `EN-09` | User Story (enabler) | wael-01 EN-09 Build an automated build and test pipeline | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-202` | `dotnet-r1` | PRD TRC REL BKL |
| 81 | `EN-12` | User Story (enabler) | wael-01 EN-12 Provide local test data with orders and a local database recipe | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-202` | `dotnet-r1` | PRD TRC REL BKL |
| 82 | `EN-10` | User Story (enabler) | wael-01 EN-10 Make time handling explicit and tested | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-203` | `dotnet-r1` | PRD TRC REL BKL |
| 83 | `STORY-202` | User Story | wael-01 STORY-202 Keep pricing identical to today (pricing parity) | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-203` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 84 | `STORY-203` | User Story | wael-01 STORY-203 Keep the order channel visible to staff (channel parity) | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-203` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 85 | `STORY-206` | User Story | wael-01 STORY-206 Keep dates and price validity identical in any time zone (time parity) | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-203` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 86 | `STORY-204` | User Story | wael-01 STORY-204 Sign staff in with Microsoft Entra ID | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-204` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 87 | `EN-04` | User Story (enabler) | wael-01 EN-04 Remove Windows sign-in and server names from database configuration | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-205` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 88 | `STORY-205` | User Story | wael-01 STORY-205 Keep secrets out of code, tests and configuration | `nw-workshop; track-dotnet; dotnet-r1` | `FEAT-205` | `dotnet-r1` | PRD BRD TRC REL BKL |
| 89 | `EN-11` | User Story (enabler) | wael-01 EN-11 Build the authorisation foundation for customer scoping and channel | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-206` | `dotnet-r2` | PRD BRD TRC REL EXP BKL |
| 90 | `STORY-230` | User Story | wael-01 STORY-230 Sign in and see only my own company's orders | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-206` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 91 | `STORY-240` | User Story | wael-01 STORY-240 Authenticate customers with an externally managed identity | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-206` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 92 | `STORY-239` | User Story | wael-01 STORY-239 Keep portal hosting, identity and mail data in the EU | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-206` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 93 | `STORY-231` | User Story | wael-01 STORY-231 See my company's orders from the last 24 months | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-207` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 94 | `STORY-232` | User Story | wael-01 STORY-232 Open an order and see lines, prices, address and status | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-207` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 95 | `STORY-233` | User Story | wael-01 STORY-233 See one of six order statuses with an as-of time | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-207` | `dotnet-r2` | PRD BRD TRC REL EXP BKL |
| 96 | `STORY-234` | User Story | wael-01 STORY-234 Create a new order by copying a previous order | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-208` | `dotnet-r2` | PRD BRD TRC REL EXP BKL |
| 97 | `STORY-235` | User Story | wael-01 STORY-235 Have a submitted portal order appear in Order Desk as Received | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-208` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 98 | `STORY-236` | User Story | wael-01 STORY-236 Show staff whether an order came from the portal or from staff | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-208` | `dotnet-r2` | PRD BRD TRC REL EXP BKL |
| 99 | `STORY-238` | User Story | wael-01 STORY-238 Show my negotiated prices, not list prices | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-209` | `dotnet-r2` | PRD BRD TRC REL EXP BKL |
| 100 | `STORY-237` | User Story | wael-01 STORY-237 Use the portal in French and English | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-209` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 101 | `STORY-241` | User Story | wael-01 STORY-241 Record who, what, when and channel for every order change | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-210` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 102 | `STORY-242` | User Story | wael-01 STORY-242 Check every pilot screen against WCAG 2.2 level AA | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-210` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 103 | `STORY-243` | User Story | wael-01 STORY-243 Respond in under 2 seconds at the 95th percentile | `nw-workshop; track-dotnet; dotnet-r2` | `FEAT-210` | `dotnet-r2` | PRD BRD TRC REL BKL |
| 104 | `EN-07` | User Story (enabler) | wael-01 EN-07 Abstract the invoice store | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-211` | `dotnet-r3` | PRD TRC REL BKL |
| 105 | `STORY-260` | User Story | wael-01 STORY-260 Download the PDF invoice of a delivered order | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-211` | `dotnet-r3` | PRD BRD TRC REL BKL |
| 106 | `STORY-261` | User Story | wael-01 STORY-261 Invite and remove users of my own company | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-212` | `dotnet-r3` | PRD BRD TRC REL BKL |
| 107 | `STORY-262` | User Story | wael-01 STORY-262 Receive an e-mail when an order changes to Shipped | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-212` | `dotnet-r3` | PRD BRD TRC REL BKL |
| 108 | `STORY-263` | User Story | wael-01 STORY-263 Use the portal in Dutch | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-213` | `dotnet-r3` | PRD BRD TRC REL BKL |
| 109 | `STORY-264` | User Story | wael-01 STORY-264 Record data to compare SM-01 to SM-04 with their baselines | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-213` | `dotnet-r3` | PRD TRC REL EXP BKL |
| 110 | `EN-14` | User Story (enabler) | wael-01 EN-14 Publish the read-only Order Desk API contract (OpenAPI 2.0) | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-214` | `dotnet-r3` | PRD TRC REL BKL |
| 111 | `STORY-265` | User Story | wael-01 STORY-265 Let another track build against the published order contract | `nw-workshop; track-dotnet; dotnet-r3` | `FEAT-214` | `dotnet-r3` | PRD TRC REL BKL |

## D. Exact description and acceptance criteria of every item

Text is copied by the script from the backlog and shown as Markdown. The payload holds the same text as HTML. Item order is the creation order. Each description starts with the item id and the source ids (ES-02, ES-29), then the story or goal, the ASSUMPTION and OPEN markers with their register text, and the gate.

### 1. wael-01 EPIC-101 Azure foundation and security baseline

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-101** (BACKLOG-NW-001) · **Source ids:** C-01, CS-09, CS-13, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27, NFR-03, NFR-05

**Source:** (source: NFR-03, NFR-05, C-01, CS-09, CS-13, ES-20, ES-22, ES-23, ES-24, ES-25, ES-27)

**Goal:** One validated foundation (naming, tags, region, connectivity, secrets, private access) that every later Azure item builds on, in design form only.

**Features:** FEAT-101, FEAT-102, FEAT-103

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-02, X-03, X-11, X-14 (see the items below). **Relies on:** A-02, A-39, A-45; O-15, O-19.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **A-39** Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. (owner: Marc Dubois)
* **A-45** Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-19** Which build and deployment pipeline tool? (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)
* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none. `EA-01` to `EA-03` do not depend on the data tier (MVE-01 does not gate them).

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 2. wael-01 EPIC-102 Data platform decision, cost and migration approach

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-102** (BACKLOG-NW-001) · **Source ids:** BR-13, C-02, C-04, C-06, CS-07, CS-08, CS-21, ES-21, ES-25

**Source:** (source: C-02, C-04, C-06, BR-13, CS-07, CS-08, CS-21, ES-21, ES-25)

**Goal:** Decide where the order database runs, prove the monthly cost fits the cap and fix how the data moves inside the Sunday window.

**Features:** FEAT-104, FEAT-105

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-12. **Relies on:** A-20, A-21, A-30, A-32, A-33, A-35; O-03, O-21, O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-20** If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. (owner: Ahmed Benali)
* **A-21** A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. (owner: Ahmed Benali)
* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **A-32** Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. (owner: Ahmed Benali)
* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-35** MVE success thresholds are starting points. Lena Varga sets the final numbers. (owner: Lena Varga)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-21** Approval and funding to build (the business case says "not yet approved for build"). (owner: Marc Dubois)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-12** The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) (owner: Ahmed Benali)

**Gate:** **MVE-01** (a PaaS data tier can host `NorthwindOrders`, keep the nightly StockPilot exchange with an unchanged file contract and stay inside the cost cap; pass thresholds `M1a`, `M1b`, `M1c`, **ASSUMPTION:** A-35). Applies to `EA-05` and `EA-09`. Result **pending**.

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 3. wael-01 EPIC-103 Pilot environment, exchange, storage and observability

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-103** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, C-03, C-04, C-06, CS-06, CS-08, CS-10, CS-12, CS-13, CS-15, CS-16, CS-22, CS-23, ES-21, ES-23, ES-25, ES-26, NFR-01, NFR-06, NFR-08

**Source:** (source: BR-13, C-01, C-02, C-03, C-04, C-06, NFR-01, NFR-06, NFR-08, CS-06, CS-08, CS-10, CS-12, CS-13, CS-15, CS-16, CS-22, CS-23, ES-21, ES-23, ES-25, ES-26)

**Goal:** Land the pilot environment, the application host, the StockPilot exchange, invoice storage, monitoring and the backup and retention design before the Q2 2027 portal pilot.

**Features:** FEAT-113, FEAT-106, FEAT-107, FEAT-108, FEAT-109

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-02, X-07, X-09, X-10. **Relies on:** A-05, A-20, A-27, A-29, A-31, A-33, A-37, A-59; O-03, O-15, O-16, O-17.

**Register text for the ids cited in this item (backlog section 7):**

* **A-05** `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. (owner: Ahmed Benali)
* **A-20** If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. (owner: Ahmed Benali)
* **A-27** The StockPilot CSV contract and file pick-up stay as they are. (owner: Ahmed Benali)
* **A-29** The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. (owner: Ahmed Benali)
* **A-31** Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). (owner: Ahmed Benali)
* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-37** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. (owner: Ahmed Benali)
* **A-59** `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-16** How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? (owner: Ahmed Benali, Pieter Janssens)
* **O-17** What sends order confirmations today? (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)

**Gate:** **MVE-01** for `EA-06` and `EA-08` (and the stories they serve), and for the production database settings of `EA-15`. Result **pending**.

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 4. wael-01 EPIC-104 Cutover and recovery proof

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-104** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, CS-07, CS-21, CS-23, NFR-01, NFR-03, NFR-06, SM-07

**Source:** (source: BR-13, NFR-01, NFR-03, NFR-06, C-01, C-02, SM-07, CS-07, CS-21, CS-23)

**Goal:** A reviewed database migration and rehearsal procedure, and a reviewed cutover, rollback, recovery-test and decommission plan, so that Order Desk can move inside the Sunday window before 30 June 2027. **Release approval comes before the first rehearsal Sunday (before 6 June 2027) and covers the procedures, plans and runbooks, validated locally. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test are planned execution after that approval (A-53, ES-27).** The target window ends on 27 June 2027, so these Sundays are inside it, 3 days before the lease ends (A-58). **OPEN:** O-27 asks Marc Dubois to confirm the extended window, the 3-day margin and the approval date before 6 June 2027.

**Features:** FEAT-114, FEAT-110, FEAT-111, FEAT-112

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-03, X-07 (single instance), O-15 (post-lease locations). **Relies on:** A-30, A-33, A-53, A-58, A-59; O-03, O-27.

**Register text for the ids cited in this item (backlog section 7):**

* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **A-58** The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). (owner: Marc Dubois)
* **A-59** `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-27** Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. (owner: Marc Dubois)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** **MVE-01**, through its inputs (the chosen data tier and its backup and cost figures). Result **pending**.

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 5. wael-01 EPIC-201 Modernise Order Desk to .NET 10 with parity

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-201** (BACKLOG-NW-001) · **Source ids:** BR-10, BR-12, C-01, C-02, CS-01, CS-02, CS-04, CS-13, CS-20, ES-13, ES-19, NFR-04, NFR-05

**Source:** (source: NFR-04, NFR-05, BR-10, BR-12, C-01, C-02, CS-01, CS-02, CS-04, CS-13 to CS-20, ES-13 to ES-19)

**Goal:** The same Order Desk, with the same prices and screens, running on .NET 10 as one solution, with staff signing in through Microsoft Entra ID and no secret in the repository. Little customer value by design; every later .NET story needs it.

**Features:** FEAT-201, FEAT-202, FEAT-203, FEAT-204, FEAT-205

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-03, X-04 (staff), X-08, X-11, X-14. **Relies on:** A-02, A-24, A-51; O-03, O-19, O-20.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **A-24** Azure runs in UTC by default. Order Desk stores local time. Parity needs explicit handling. (From the code, not in `knowledge-docs`.) (owner: Ahmed Benali)
* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-19** Which build and deployment pipeline tool? (owner: Ahmed Benali)
* **O-20** Decision record on the portal and API project shape (ES-13). (owner: Ahmed Benali)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)
* **X-08** Logging moves to Application Insights and Log Analytics (.NET needs Azure) (owner: Ahmed Benali)
* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none. MVE-02 does not gate parity work (it is technical and low risk).

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 6. wael-01 EPIC-202 Customer portal pilot: sign-in, orders, status, reorder

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** none · **Priority:** Must (proposed ADO priority 1)

**Description**

**EPIC-202** (BACKLOG-NW-001) · **Source ids:** BR-01, BR-06, BR-10, BR-11, BR-12, C-05, CS-10, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08

**Source:** (source: BR-01 to BR-06, BR-10, BR-11, BR-12, NFR-02, NFR-03, NFR-04, NFR-07, NFR-08, C-05, CS-10)

**Goal:** A Must-only pilot for 20 customers: sign in, see own orders, follow status, reorder, with the quality requirements (isolation, residency, accessibility, performance, audit).

**Features:** FEAT-206, FEAT-207, FEAT-208, FEAT-209, FEAT-210

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-01, X-04 (customers), X-05, X-06, X-13, X-15, O-23, A-37. **Relies on:** A-03, A-10, A-16, A-17, A-19; O-04, O-08, O-10, O-16, O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-03** `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. (owner: Lena Varga)
* **A-10** Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. (owner: Ahmed Benali)
* **A-16** 24 months is a display window over the complete history held in the database. (owner: Ahmed Benali)
* **A-17** Pilot customer concurrency is small (20 customers). No customer load figure exists. (owner: Ahmed Benali)
* **A-19** In `dotnet-r2`, staff onboard customer users until `BR-08` is built. (owner: Lena Varga)
* **A-35** MVE success thresholds are starting points. Lena Varga sets the final numbers. (owner: Lena Varga)
* **A-37** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. (owner: Ahmed Benali)
* **O-04** What status freshness is acceptable, given the nightly batch? (owner: Lena Varga)
* **O-08** Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. (owner: Ahmed Benali)
* **O-10** Which identity provider do customer users use (OQ-01)? (owner: Ahmed Benali)
* **O-16** How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? (owner: Ahmed Benali, Pieter Janssens)
* **O-23** Which database does the Q2 2027 portal pilot read (T-08)? (owner: Ahmed Benali)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)
* **X-05** StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) (owner: Ahmed Benali)
* **X-06** Status freshness is bounded by the exchange cadence (.NET needs Azure and StockPilot) (owner: Lena Varga)
* **X-13** An internet-facing entry for customers while data services use private endpoints (.NET needs Azure) (owner: Ahmed Benali)
* **X-15** Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** **MVE-02** (customers reorder unaided and trust a status refreshed once a night; pass thresholds `R1` at least 80 % finish a reorder unaided, `R2` at least 60 % would use the status instead of phoning, **ASSUMPTION:** A-35). Applies to the stories for `BR-04`, `BR-05`, `BR-10` and `BR-12` (`STORY-233`, `STORY-234`, `STORY-236`, `STORY-238`). Result **pending**.

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** epic · **Priority:** Must · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 7. wael-01 EPIC-203 Complete the portal and publish the Order Desk API contract

* **Type:** Epic (backlog type: epic) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** none · **Priority:** Should (proposed ADO priority 2)

**Description**

**EPIC-203** (BACKLOG-NW-001) · **Source ids:** BR-07, BR-08, BR-09, BR-11, CS-27, ES-36, SM-01, SM-04

**Source:** (source: BR-07, BR-08, BR-09, BR-11, SM-01 to SM-04, CS-27, ES-36, G-01)

**Goal:** Add invoices, user administration, e-mail and Dutch after pilot feedback, record the data for the success measures and publish the read-only API contract that another track can build against.

**Features:** FEAT-211, FEAT-212, FEAT-213, FEAT-214

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Cross-track (OPEN):** X-06, X-09, X-10; X-20, X-21 outbound (the contract `EN-14` serves BA-03). **Relies on:** A-03, A-04, A-11, A-12, A-15, A-19, A-29, A-52; O-01, O-05, O-11, O-12, O-15, O-17, O-18, O-26.

**Register text for the ids cited in this item (backlog section 7):**

* **A-03** `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. (owner: Lena Varga)
* **A-04** "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot. (owner: Lena Varga)
* **A-11** Portal release 1 covers French and English. Dutch follows. (owner: Sofie Peeters, Lena Varga)
* **A-12** A customer administrator role exists. Who gets it is **OPEN:**. (owner: Lena Varga)
* **A-15** The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. (owner: Julien Moreau)
* **A-19** In `dotnet-r2`, staff onboard customer users until `BR-08` is built. (owner: Lena Varga)
* **A-29** The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. (owner: Ahmed Benali)
* **A-52** `FR-234` (instrumentation for SM-01 to SM-04) is Should, because the business case gives the measures no priority and names no measurement source. (owner: Lena Varga)
* **G-01** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))
* **O-01** Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? (owner: Ahmed Benali)
* **O-05** Does "portal launch" mean the pilot or general availability? (owner: Lena Varga)
* **O-11** Must Dutch be in the first release (OQ-02)? (owner: Sofie Peeters, Lena Varga)
* **O-12** Do customer administrators exist for every customer or only for large ones (OQ-03)? (owner: Lena Varga)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-17** What sends order confirmations today? (owner: Ahmed Benali)
* **O-18** Where do the customer e-mail address and language preference live? (owner: Lena Varga)
* **O-26** Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. (owner: Lena Varga)
* **X-06** Status freshness is bounded by the exchange cadence (.NET needs Azure and StockPilot) (owner: Lena Varga)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)
* **X-20** An Order Desk API (read orders and lines) for the custom connector (Power Platform needs .NET) (owner: Ahmed Benali)
* **X-21** An order data contract for claims: order number, lines, quantities, prices, customer, warehouse (Power Platform needs .NET) (owner: Lena Varga, Pieter Janssens)

**Gate:** **MVE-02** for the instrumentation (`STORY-264`, `SM-01` to `SM-04`). Result **pending**.

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** epic · **Priority:** Should · **Parent:** none

**Acceptance criteria:** none in the backlog for an epic.

### 8. wael-01 FEAT-101 Environment foundation as code and validation

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** EPIC-101 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-101** (BACKLOG-NW-001) · **Source ids:** CS-09, CS-19, ES-20, ES-24, ES-27, NFR-03

**Source:** (source: CS-09, CS-19, NFR-03, ES-20 to ES-24, ES-27)

**Contains:** EA-01, EA-11, STORY-101, STORY-104, STORY-105

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-101

**Acceptance criteria:** none in the backlog for a feature.

### 9. wael-01 FEAT-102 Hybrid connectivity design

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** EPIC-101 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-102** (BACKLOG-NW-001) · **Source ids:** C-01, C-03, CS-09

**Source:** (source: CS-09, C-01, C-03)

**Contains:** EA-02, STORY-102

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-101

**Acceptance criteria:** none in the backlog for a feature.

### 10. wael-01 FEAT-103 Secrets, identity and private access

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** EPIC-101 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-103** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, ES-25, NFR-05

**Source:** (source: NFR-05, CS-13, ES-17, ES-25)

**Contains:** EA-03, STORY-103

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-101

**Acceptance criteria:** none in the backlog for a feature.

### 11. wael-01 FEAT-104 Data tier decision

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** EPIC-102 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-104** (BACKLOG-NW-001) · **Source ids:** C-02, C-06, CS-07, ES-21

**Source:** (source: C-02, C-06, CS-07, ES-21)

**Contains:** EA-05, STORY-120

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-102

**Acceptance criteria:** none in the backlog for a feature.

### 12. wael-01 FEAT-105 Cost model and migration approach

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** EPIC-102 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-105** (BACKLOG-NW-001) · **Source ids:** BR-13, C-04, CS-07, CS-08, CS-21

**Source:** (source: C-04, BR-13, CS-07, CS-08, CS-21)

**Contains:** EA-09, STORY-121, STORY-122

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-102

**Acceptance criteria:** none in the backlog for a feature.

### 13. wael-01 FEAT-113 Application hosting

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** EPIC-103 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-113** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, C-06, CS-06, CS-13, CS-16, ES-21, ES-25, NFR-01

**Source:** (source: BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25)

**Contains:** EA-15

**Gate:** MVE-01 for the production database settings of `EA-15` only; the rest of the feature has none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-103

**Acceptance criteria:** none in the backlog for a feature.

### 14. wael-01 FEAT-106 StockPilot exchange, invoice storage and outbound mail

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** EPIC-103 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-106** (BACKLOG-NW-001) · **Source ids:** BR-09, C-03, CS-08, CS-10, CS-11, CS-12

**Source:** (source: C-03, CS-08, CS-10, CS-11, CS-12, BR-09)

**Contains:** EA-06, EA-07, EA-12, STORY-140, STORY-141, STORY-144

**Gate:** MVE-01 (`EA-06`, `STORY-140`)

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-103

**Acceptance criteria:** none in the backlog for a feature.

### 15. wael-01 FEAT-107 Observability and alerting

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** EPIC-103 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-107** (BACKLOG-NW-001) · **Source ids:** CS-15, CS-22, ES-26, NFR-01

**Source:** (source: NFR-01, CS-15, CS-22, ES-26)

**Contains:** EA-04, STORY-142

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-103

**Acceptance criteria:** none in the backlog for a feature.

### 16. wael-01 FEAT-108 Test environment for the portal pilot

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** EPIC-103 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-108** (BACKLOG-NW-001) · **Source ids:** C-04, ES-23

**Source:** (source: ES-23, C-04, business-case section 8)

**Contains:** EA-10, STORY-143

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-103

**Acceptance criteria:** none in the backlog for a feature.

### 17. wael-01 FEAT-109 Backup, retention and recovery design

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** EPIC-103 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-109** (BACKLOG-NW-001) · **Source ids:** CS-07, CS-23, NFR-06, NFR-08

**Source:** (source: NFR-06, NFR-08, CS-07, CS-23)

**Contains:** EA-08, STORY-145, STORY-146

**Gate:** MVE-01 (`EA-08`, `STORY-146`)

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-103

**Acceptance criteria:** none in the backlog for a feature.

### 18. wael-01 FEAT-114 Database migration and rehearsal

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** EPIC-104 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-114** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, CS-07, CS-23, NFR-03, NFR-06

**Source:** (source: BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23)

**Contains:** EA-16

**Gate:** MVE-01 (through the data-tier option)

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-104

**Acceptance criteria:** none in the backlog for a feature.

### 19. wael-01 FEAT-110 Cutover and rollback runbooks

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** EPIC-104 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-110** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, CS-21, SM-07

**Source:** (source: BR-13, C-01, C-02, CS-21, SM-07)

**Contains:** EA-13, STORY-170, STORY-171

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-104

**Acceptance criteria:** none in the backlog for a feature.

### 20. wael-01 FEAT-111 Recovery and availability proof

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** EPIC-104 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-111** (BACKLOG-NW-001) · **Source ids:** CS-22, CS-23, NFR-01, NFR-06

**Source:** (source: NFR-01, NFR-06, CS-22, CS-23, T-14)

**Contains:** EA-14, STORY-172, STORY-173

**Register text for the ids cited in this item (backlog section 7):**

* **T-14** The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-104

**Acceptance criteria:** none in the backlog for a feature.

### 21. wael-01 FEAT-112 Decommission of the old servers

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** EPIC-104 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-112** (BACKLOG-NW-001) · **Source ids:** C-01, C-02, SM-07

**Source:** (source: C-01, C-02, SM-07)

**Contains:** STORY-174

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-104

**Acceptance criteria:** none in the backlog for a feature.

### 22. wael-01 FEAT-201 Modernise projects and web layer

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** EPIC-201 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-201** (BACKLOG-NW-001) · **Source ids:** CS-01, CS-02, CS-04, CS-15, CS-16, CS-17, ES-13, ES-16, ES-19

**Source:** (source: CS-01, CS-02, CS-04, CS-15, CS-16, CS-17, ES-13 to ES-16, ES-19)

**Contains:** EN-01, EN-13, EN-03, EN-05, EN-06, EN-08, STORY-201

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-201

**Acceptance criteria:** none in the backlog for a feature.

### 23. wael-01 FEAT-202 Test, build and local data

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** EPIC-201 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-202** (BACKLOG-NW-001) · **Source ids:** CS-18, CS-19, CS-20, ES-18, ES-27

**Source:** (source: CS-18, CS-19, CS-20, ES-18, ES-27)

**Contains:** EN-02, EN-09, EN-12

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-201

**Acceptance criteria:** none in the backlog for a feature.

### 24. wael-01 FEAT-203 Pricing, channel and time parity

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** EPIC-201 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-203** (BACKLOG-NW-001) · **Source ids:** BR-02, BR-10, BR-12, CS-20

**Source:** (source: BR-10, BR-12, BR-02, CS-20)

**Contains:** EN-10, STORY-202, STORY-203, STORY-206

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-201

**Acceptance criteria:** none in the backlog for a feature.

### 25. wael-01 FEAT-204 Staff sign-in with Entra ID

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** EPIC-201 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-204** (BACKLOG-NW-001) · **Source ids:** CS-04, NFR-04

**Source:** (source: NFR-04, CS-04, G-03)

**Contains:** STORY-204

**Register text for the ids cited in this item (backlog section 7):**

* **G-03** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-201

**Acceptance criteria:** none in the backlog for a feature.

### 26. wael-01 FEAT-205 Secret-free configuration

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** EPIC-201 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-205** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, ES-25, NFR-05

**Source:** (source: NFR-05, CS-13, ES-17, ES-25)

**Contains:** EN-04, STORY-205

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-201

**Acceptance criteria:** none in the backlog for a feature.

### 27. wael-01 FEAT-206 Customer sign-in, company isolation and data residency

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** EPIC-202 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-206** (BACKLOG-NW-001) · **Source ids:** BR-01, CS-04, CS-05, NFR-03, NFR-04

**Source:** (source: BR-01, NFR-03, NFR-04, CS-04, CS-05)

**Contains:** EN-11, STORY-230, STORY-240, STORY-239

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-202

**Acceptance criteria:** none in the backlog for a feature.

### 28. wael-01 FEAT-207 Order list, order detail and status

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** EPIC-202 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-207** (BACKLOG-NW-001) · **Source ids:** BR-02, BR-03, BR-04, CS-10

**Source:** (source: BR-02, BR-03, BR-04, P-03, CS-10)

**Contains:** STORY-231, STORY-232, STORY-233

**Gate:** MVE-02 (`STORY-233`)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-202

**Acceptance criteria:** none in the backlog for a feature.

### 29. wael-01 FEAT-208 Reorder, submit and channel

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** EPIC-202 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-208** (BACKLOG-NW-001) · **Source ids:** BR-05, BR-06, BR-10, C-05

**Source:** (source: BR-05, BR-06, BR-10, C-05, P-01, P-02, P-04)

**Contains:** STORY-234, STORY-235, STORY-236

**Gate:** MVE-02 (`STORY-234`, `STORY-236`)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-202

**Acceptance criteria:** none in the backlog for a feature.

### 30. wael-01 FEAT-209 Customer prices and language

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** EPIC-202 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-209** (BACKLOG-NW-001) · **Source ids:** BR-11, BR-12, CS-20, OQ-02

**Source:** (source: BR-11, BR-12, CS-20, OQ-02)

**Contains:** STORY-238, STORY-237

**Gate:** MVE-02 (`STORY-238`)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-202

**Acceptance criteria:** none in the backlog for a feature.

### 31. wael-01 FEAT-210 Audit, accessibility and performance

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** EPIC-202 · **Priority:** Must (proposed ADO priority 1)

**Description**

**FEAT-210** (BACKLOG-NW-001) · **Source ids:** CS-03, CS-05, ES-19, NFR-02, NFR-07, NFR-08

**Source:** (source: NFR-02, NFR-07, NFR-08, CS-03, CS-05, ES-19)

**Contains:** STORY-241, STORY-242, STORY-243

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** feature · **Priority:** Must · **Parent:** EPIC-202

**Acceptance criteria:** none in the backlog for a feature.

### 32. wael-01 FEAT-211 Invoice download

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** EPIC-203 · **Priority:** Should (proposed ADO priority 2)

**Description**

**FEAT-211** (BACKLOG-NW-001) · **Source ids:** BR-07, CS-08, CS-11, CS-14

**Source:** (source: BR-07, CS-08, CS-11, CS-14, P-05)

**Contains:** EN-07, STORY-260

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** feature · **Priority:** Should · **Parent:** EPIC-203

**Acceptance criteria:** none in the backlog for a feature.

### 33. wael-01 FEAT-212 Customer user administration and shipping e-mail

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** EPIC-203 · **Priority:** Should (proposed ADO priority 2)

**Description**

**FEAT-212** (BACKLOG-NW-001) · **Source ids:** BR-08, BR-09, CS-10, CS-12, OQ-03

**Source:** (source: BR-08, BR-09, OQ-03, CS-10, CS-12)

**Contains:** STORY-261, STORY-262

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** feature · **Priority:** Should · **Parent:** EPIC-203

**Acceptance criteria:** none in the backlog for a feature.

### 34. wael-01 FEAT-213 Dutch and success-measure data

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** EPIC-203 · **Priority:** Should (proposed ADO priority 2)

**Description**

**FEAT-213** (BACKLOG-NW-001) · **Source ids:** BR-11, OQ-02, SM-01, SM-04

**Source:** (source: BR-11, SM-01 to SM-04, OQ-02)

**Contains:** STORY-263, STORY-264

**Gate:** MVE-02 (`STORY-264`)

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** feature · **Priority:** Should · **Parent:** EPIC-203

**Acceptance criteria:** none in the backlog for a feature.

### 35. wael-01 FEAT-214 Order Desk API contract

* **Type:** Feature (backlog type: feature) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** EPIC-203 · **Priority:** Should (proposed ADO priority 2)

**Description**

**FEAT-214** (BACKLOG-NW-001) · **Source ids:** CS-27, ES-36

**Source:** (source: CS-27, ES-36, G-01)

**Contains:** EN-14, STORY-265

**Register text for the ids cited in this item (backlog section 7):**

* **G-01** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** feature · **Priority:** Should · **Parent:** EPIC-203

**Acceptance criteria:** none in the backlog for a feature.

### 36. wael-01 EA-01 Build the Azure foundation as code (naming, tags, region, modules)

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-101 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 1

**Description**

**EA-01** (BACKLOG-NW-001) · **Source ids:** CS-09, ES-20, ES-21, ES-22, ES-23, ES-24, ES-27, FR-101, FR-104, NFR-03

**Source:** (source: CS-09, NFR-03, ES-20, ES-21, ES-22, ES-23, ES-24, ES-27)

**Serves:** FR-101, FR-104

**Story:** As an Azure platform engineer, I want the naming rule, the required tags, the primary region and the infrastructure definitions written as code with Azure Verified Modules, so that every later Azure item builds on one validated foundation.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none; this is the first Azure item. **Cross-track (OPEN):** X-02 (the application's configuration contract is written by .NET; Azure writes infrastructure around it and validates locally). **Relies on:** A-02, A-39.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **A-39** Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. (owner: Marc Dubois)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-03) · **Rank:** 1 · **Parent:** FEAT-101

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-01/AC1** Given an entry point `main.bicep` and a `.bicepparam` file for each of `tst` and `prd` under `infra/` (ES-10, ES-22), When `az bicep build` is run locally on each, Then it finishes with no error and nothing is applied to a subscription (ES-27).
* **EA-01/AC2** Given any resource defined, When its name is generated, Then it follows `<resource-abbreviation>-nw-<workload>-<environment>-<region>` with environment `tst` or `prd` (for example `app-nw-orderdesk-prd-frc`) (ES-23).
* **EA-01/AC3** Given any resource definition, When it is reviewed, Then it carries the tags `workload`, `environment`, `owner` and `costCenter`; a definition missing one tag is rejected until the tag is added (ES-24).
* **EA-01/AC4** Given an Azure Verified Module exists for a resource, When the resource is defined, Then the module is used; where none exists, the exception and its reason are written next to the definition (ES-22).

### 37. wael-01 EA-11 Build the infrastructure validation and deployment pipeline design

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-101 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 2

**Description**

**EA-11** (BACKLOG-NW-001) · **Source ids:** CS-19, ES-22, ES-27, FR-105

**Source:** (source: CS-19, ES-22, ES-27)

**Serves:** FR-105

**Story:** As an Azure platform engineer, I want a pipeline definition that validates every infrastructure file locally and never applies it, so that releases have a repeatable, reviewed check instead of a manual copy (CS-19).

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-11 (the .NET track writes its own build pipeline; each track keeps delivering on its own). **Relies on:** O-19 (pipeline tool not chosen; the definition is tool-neutral until answered).

**Register text for the ids cited in this item (backlog section 7):**

* **O-19** Which build and deployment pipeline tool? (owner: Ahmed Benali)
* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 2 · **Parent:** FEAT-101

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-11/AC1** Given a change to any file under `infra/`, When the validation step runs, Then it runs `az bicep build` on every `main.bicep` and reports the result.
* **EA-11/AC2** Given a `main.bicep` with no matching `.bicepparam` file, or a file that does not build, When the validation step runs, Then it fails and names the file.
* **EA-11/AC3** Given the pipeline definition, When it is reviewed, Then it contains no step that applies anything to a subscription from this workshop; any deploy stage is marked as needing human approval (ES-27).

### 38. wael-01 STORY-101 Review a test and production environment design set

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-101 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 3

**Description**

**STORY-101** (BACKLOG-NW-001) · **Source ids:** C-01, CS-09, ES-20, ES-22, ES-23, ES-24, ES-27, FR-101

**Source:** (source: C-01, CS-09, ES-20, ES-22, ES-23, ES-24, ES-27)

**Implements:** FR-101

**Story:** As the IT manager, I want a reviewed design set for a test environment and a production environment, so that the team agrees one platform baseline before any hosting work starts.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-02, X-14. **Relies on:** A-39; O-09 (approver).

**Register text for the ids cited in this item (backlog section 7):**

* **A-39** Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. (owner: Marc Dubois)
* **O-09** Who is the named release approver for each track? (owner: Marc Dubois)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 3 · **Parent:** FEAT-101

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-101/AC1** Given the design set, When the product owner and the IT manager review it, Then it shows one naming rule, the four required tags, France Central as the primary region and infrastructure written as code for both `tst` and `prd`.
* **STORY-101/AC2** Given the design set, When it is validated locally, Then it passes and nothing is applied to a subscription (ES-27).
* **STORY-101/AC3** Given a reviewer finds a name that breaks the rule or a resource without the four tags, When the review ends, Then `azure-r1` cannot be approved until it is fixed.

### 39. wael-01 STORY-104 Keep every Azure resource in an EU region

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-101 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 4

**Description**

**STORY-104** (BACKLOG-NW-001) · **Source ids:** ES-20, FR-104, NFR-03

**Source:** (source: NFR-03, ES-20)

**Implements:** FR-104 · **Covers:** NFR-03 (Azure side)

**Story:** As the IT manager, I want every Azure resource for Order Desk and the portal placed in France Central or another EU region, so that customer data and order data stay in the European Union.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-04 is the Azure side of customer and staff identity and stays **OPEN:**; the identity and mail services of the portal are covered by STORY-239 (O-24). **Relies on:** A-54.

**Register text for the ids cited in this item (backlog section 7):**

* **A-54** The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. (owner: Ahmed Benali, Lena Varga)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 4 · **Parent:** FEAT-101

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-104/AC1** Given the design set, When every resource is listed with its region, Then each resource is in France Central, or in another EU region if it is a secondary region (ES-20).
* **STORY-104/AC2** Given a resource defined outside the EU, When the list is reviewed, Then the design is rejected and the resource is moved to an EU region before `azure-r1` is approved.
* **STORY-104/AC3** Given a secondary region is proposed, When it is reviewed, Then it is in the EU, or it is not accepted.

### 40. wael-01 STORY-105 Validate every infrastructure definition locally before release

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-101 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 5

**Description**

**STORY-105** (BACKLOG-NW-001) · **Source ids:** CS-19, ES-22, ES-27, FR-105

**Source:** (source: CS-19, ES-22, ES-27)

**Implements:** FR-105

**Story:** As the IT manager, I want a deployment pipeline design in which every infrastructure definition is validated locally and reviewed before a release is approved, so that nothing unchecked reaches a subscription later.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-11`. **Cross-track (OPEN):** X-11. **Relies on:** O-19.

**Register text for the ids cited in this item (backlog section 7):**

* **O-19** Which build and deployment pipeline tool? (owner: Ahmed Benali)
* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 5 · **Parent:** FEAT-101

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-105/AC1** Given any infrastructure definition in the release, When `az bicep build` is run locally (for example), Then it passes and a reviewer has recorded the review before release approval.
* **STORY-105/AC2** Given a definition that fails to build, When the release content is assembled, Then that definition is left out and listed as a finding.
* **STORY-105/AC3** Given the pipeline design, When it is read, Then it states which stage needs a human approval before anything is applied and that nothing is applied from this workshop.

### 41. wael-01 EA-02 Design hybrid connectivity between Lyon, Azure and Antwerp

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-102 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 6

**Description**

**EA-02** (BACKLOG-NW-001) · **Source ids:** C-01, C-03, CS-09, FR-102

**Source:** (source: CS-09, C-01, C-03, O-15)

**Serves:** FR-102

**Story:** As an Azure platform engineer, I want a connectivity design for the existing link to Antwerp, the link from Lyon to Azure during the migration and the path after the lease, so that the StockPilot exchange stays reachable throughout.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** none new. **Relies on:** O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 6 · **Parent:** FEAT-102

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-02/AC1** Given today's site-to-site VPN between Lyon and Antwerp (CS-09), When the design is reviewed, Then it shows how Antwerp keeps reaching the order data during the migration and after 30 June 2027.
* **EA-02/AC2** Given the location after the lease of the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route is not known (O-15), When the design names any of them, Then each is marked **OPEN:** with its owner and is not designed as a fact.

### 42. wael-01 STORY-102 Agree the connection design for the move and after the lease

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-102 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 7

**Description**

**STORY-102** (BACKLOG-NW-001) · **Source ids:** C-01, C-03, CS-09, FR-102

**Source:** (source: CS-09, C-01, C-03)

**Implements:** FR-102

**Story:** As the IT manager, I want one agreed design of how Azure, the Lyon data centre and the Antwerp warehouse connect during the move and after the lease, so that the StockPilot exchange never loses its path.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-02`. **Cross-track (OPEN):** none. **Relies on:** O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 7 · **Parent:** FEAT-102

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-102/AC1** Given the connection design, When it is reviewed, Then it describes the connections for two periods: during the migration and after the lease ends.
* **STORY-102/AC2** Given the nightly 02:00 StockPilot exchange (CS-10), When each period is read, Then the exchange stays reachable in both.
* **STORY-102/AC3** Given a path depends on an unanswered item from O-15, When the design is reviewed, Then that path is marked **OPEN:** with an owner and the release is not blocked by it.

### 43. wael-01 EA-03 Design secrets, managed identities and private endpoints

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-103 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 8

**Description**

**EA-03** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, ES-25, FR-103, NFR-05

**Source:** (source: CS-13, NFR-05, ES-17, ES-25)

**Serves:** FR-103

**Story:** As an Azure platform engineer, I want a managed secret store, managed identities and private endpoints designed and defined as code, so that no Azure-hosted part of Order Desk needs a password.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-02, X-03 (database sign-in moves from Windows-integrated to a managed identity; .NET builds against a local SQL Server meanwhile). **Relies on:** A-02.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-05) · **Rank:** 8 · **Parent:** FEAT-103

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-03/AC1** Given any Azure-hosted application in the design, When its credentials are listed, Then each is held in the secret store or replaced by a managed identity, and no definition contains a password (ES-25).
* **EA-03/AC2** Given a data service (database, storage, Key Vault), When its network access is reviewed, Then it is reached through a private endpoint (ES-25).
* **EA-03/AC3** Given a parameter file that contains a password, key or connection string with a password, When the secret scan runs, Then the scan fails and names the file.

### 44. wael-01 STORY-103 Keep secrets out of Azure-hosted code and configuration

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-103 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 9

**Description**

**STORY-103** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, ES-25, FR-103, NFR-05

**Source:** (source: NFR-05, CS-13, ES-17, ES-25)

**Implements:** FR-103 · **Covers:** NFR-05 (Azure side)

**Story:** As the IT manager, I want the Azure-hosted parts of Order Desk to hold no secret in source code or in configuration files in the repository, so that a leaked repository exposes no credential.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-03`. **Cross-track (OPEN):** X-02, X-03. **Relies on:** A-54 (measurement rule).

**Register text for the ids cited in this item (backlog section 7):**

* **A-54** The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. (owner: Ahmed Benali, Lena Varga)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 9 · **Parent:** FEAT-103

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-103/AC1** Given the release content, When a scan of source and configuration files runs as part of the release exit criteria, Then it finds no password, key or connection string with a password.
* **STORY-103/AC2** Given an application needs a credential, When the design is reviewed, Then it uses the managed secret store with a managed identity and no password.
* **STORY-103/AC3** Given the scan finds a secret, When the release is considered for approval, Then it is not approved until the secret is removed.

### 45. wael-01 EA-05 Record the data-tier decision and migration approach

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-104 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 10

**Description**

**EA-05** (BACKLOG-NW-001) · **Source ids:** C-02, CS-07, CS-21, ES-21, FR-106, FR-108

**Source:** (source: CS-07, CS-21, C-02, ES-21)

**Serves:** FR-106, FR-108

**Story:** As an Azure platform engineer, I want a decision record that compares the managed-service options with a virtual machine and states the migration approach, so that later exchange, backup and cost work starts from one chosen option.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`; blocks `EA-06`, `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-20, A-21, A-30, A-32, A-35; O-03.

**Register text for the ids cited in this item (backlog section 7):**

* **A-20** If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. (owner: Ahmed Benali)
* **A-21** A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. (owner: Ahmed Benali)
* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **A-32** Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. (owner: Ahmed Benali)
* **A-35** MVE success thresholds are starting points. Lena Varga sets the final numbers. (owner: Lena Varga)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)

**Gate:** MVE-01 (decision before commit)

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 10 · **Parent:** FEAT-104

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-05/AC1** Given MVE-01 has been decided (go, adjust or stop), When the record is written, Then it names the chosen option and shows how that option was checked against `M1a` (0 unmapped constructs), `M1b` (cost at or below EUR 1,200 a month, A-35) and `M1c` (backup frequency of 60 minutes or less).
* **EA-05/AC2** Given MVE-01 has not been decided, When the epic is considered for commitment, Then `EA-05` stays uncommitted (gate) and `EA-01` to `EA-03` continue.
* **EA-05/AC3** Given a construct of the current database has no equivalent in an option (for example a SQL Server Agent job, A-30), When it is checked, Then it is listed as unmapped and that option fails `M1a`.

### 46. wael-01 STORY-120 Decide the data tier for the order database

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-104 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 11

**Description**

**STORY-120** (BACKLOG-NW-001) · **Source ids:** BR-13, C-02, C-06, CS-07, ES-21, FR-106

**Source:** (source: C-02, C-06, CS-07, BR-13, ES-21)

**Implements:** FR-106

**Story:** As the IT manager, I want a written decision on the data tier for the order database, so that the team knows where `NorthwindOrders` will run and how the old servers leave support.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`; the decision is carried out by `EA-16` (`azure-r3`). **Cross-track (OPEN):** none. **Relies on:** A-20, A-21; O-03, O-21.

**Register text for the ids cited in this item (backlog section 7):**

* **A-20** If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. (owner: Ahmed Benali)
* **A-21** A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-21** Approval and funding to build (the business case says "not yet approved for build"). (owner: Marc Dubois)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 11 · **Parent:** FEAT-104

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-120/AC1** Given the decision record, When it is read, Then it names the chosen data tier, states that a managed service (PaaS) is preferred and a virtual machine is the fallback (A-21), and introduces no Kubernetes (ES-21).
* **STORY-120/AC2** Given the decision, When it is read, Then it states how the old web server and database server leave support (C-02).
* **STORY-120/AC3** Given the decision, When it is reviewed, Then it keeps the StockPilot exchange working and fits what a six-person team that knows .NET and SQL Server can run (C-06).
* **STORY-120/AC4** Given MVE-01 ends in **adjust** because only the virtual machine passes, When the record is written, Then it chooses the virtual machine and explains in a decision record why it departs from ES-21.

### 47. wael-01 EA-09 Build the Azure cost model against the monthly cap

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-105 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 12

**Description**

**EA-09** (BACKLOG-NW-001) · **Source ids:** C-04, CS-03, CS-06, FR-107

**Source:** (source: C-04, X-12, CS-03, CS-06)

**Serves:** FR-107

**Story:** As an Azure platform engineer, I want a cost model for the production and one test environment that includes the portal and the Order Desk API host, so that every sizing choice is checked against the monthly cap.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-12 (the portal and API host share the cap; Azure sizes from today's load and refines later). **Relies on:** A-02, A-35; O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **A-35** MVE success thresholds are starting points. Lena Varga sets the final numbers. (owner: Lena Varga)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-12** The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 12 · **Parent:** FEAT-105

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-09/AC1** Given today's load (about 60 concurrent users at peak, CS-03; average CPU 18 % and peak 55 %, CS-06), When the model is built, Then it lists a monthly figure for each component of production and one test environment.
* **EA-09/AC2** Given the model, When it is read, Then it shows the monthly total, the EUR 1,500 cap (C-04) and the headroom left.
* **EA-09/AC3** Given a price comes from a public price list, When it is entered, Then it is date-stamped and labelled indicative; no price is presented as a quote.

### 48. wael-01 STORY-121 Show the monthly cost against the EUR 1,500 cap

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-105 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 13

**Description**

**STORY-121** (BACKLOG-NW-001) · **Source ids:** C-04, FR-107

**Source:** (source: C-04, X-12, T-03)

**Implements:** FR-107

**Story:** As the sponsor (Marc Dubois), I want a cost model of the whole Azure platform against the EUR 1,500 monthly cap, so that I can see whether Order Desk and the portal fit before anything is built.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-09`. **Cross-track (OPEN):** X-12. **Relies on:** A-02, A-35; O-21, O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-02** .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. (owner: Ahmed Benali)
* **A-35** MVE success thresholds are starting points. Lena Varga sets the final numbers. (owner: Lena Varga)
* **O-21** Approval and funding to build (the business case says "not yet approved for build"). (owner: Marc Dubois)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **T-03** C-04 is a shared cap held only by BA-01 (handled by A-02, X-12). (owner: Ahmed Benali)
* **X-12** The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 13 · **Parent:** FEAT-105

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-121/AC1** Given the cost model, When it is reviewed, Then it covers Order Desk, the portal and the Order Desk API host in production and one test environment, and shows the monthly total and the headroom against EUR 1,500.
* **STORY-121/AC2** Given the estimate for Order Desk alone is above EUR 1,200 (80 % of the cap, the MVE-01 starting threshold, A-35), When the model is reviewed, Then the result is recorded as **adjust** and the sponsor is told that headroom for the portal is below EUR 300 (derived: EUR 1,500 less EUR 1,200).
* **STORY-121/AC3** Given the total is above EUR 1,500 for every option that passes `M1a` and `M1c`, When the model is reviewed, Then the result is **stop** and Marc Dubois decides whether to relax C-04 or reduce scope (O-21).

### 49. wael-01 STORY-122 Define the database and invoice migration approach

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r1` · **Parent:** FEAT-105 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 14

**Description**

**STORY-122** (BACKLOG-NW-001) · **Source ids:** BR-13, CS-07, CS-08, CS-21, FR-108

**Source:** (source: BR-13, CS-07, CS-08, CS-21)

**Implements:** FR-108

**Story:** As the IT manager, I want a migration approach for the order database (48 GB, growing about 1 GB a month) and the invoice files (120 GB, growing about 2 GB a month), so that the move fits the Sunday maintenance window of 06:00 to 12:00 CET.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`. **Cross-track (OPEN):** none. **Relies on:** A-33.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)

**Gate:** MVE-01 (through the data-tier option)

**Track tag:** track-azure · **Release tag:** azure-r1 · **Type:** story · **Priority:** Must · **Rank:** 14 · **Parent:** FEAT-105

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-122/AC1** Given the approach, When it is read, Then it states the steps, the expected downtime and the fallback for the database and for the invoice files.
* **STORY-122/AC2** Given the planned steps are added up, When the total is longer than the window of 06:00 to 12:00 CET, Then the approach is not accepted until steps are split across Sundays or a fallback is defined.
* **STORY-122/AC3** Given the claim that a log-based restore fits the window cannot be proved on paper (A-33), When the approach is reviewed, Then the claim is marked **ASSUMPTION:** and the proof is left to `EA-16` and to the rehearsals planned in `EA-13`.

### 50. wael-01 EA-15 Host the Order Desk web application in the test and production environments

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-113 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 15

**Description**

**EA-15** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, C-06, CS-06, CS-13, CS-16, ES-21, ES-25, FR-112, FR-116, NFR-01

**Source:** (source: BR-13, C-01, C-02, C-06, NFR-01, CS-06, CS-13, CS-16, ES-21, ES-25)

**Serves:** FR-112, FR-116 · **Added after the first review (A-59)**

**Story:** As an Azure platform engineer, I want the hosting of the Order Desk web application designed as code for `tst` and `prd`, with its settings for sign-in, secrets, size and monitoring, checked locally (nothing is applied in Azure, ES-27), so that the application has a defined place to run before the database moves and the cutover.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`, `EA-03`; its production database settings take the data-tier record `EA-05` (they wait for the MVE-01 decision); test hosting and the other settings proceed without it; feeds `EA-16`, `EA-13`. **Cross-track (OPEN):** X-02 (the Order Desk build comes from the .NET track as a `net10.0` application, or the unchanged application is rehosted per A-20; Azure writes the definition for either and validates it locally; `azure-r2` does not wait for the build), X-07 (single instance). **Relies on:** A-20, A-59; O-03.

**Register text for the ids cited in this item (backlog section 7):**

* **A-20** If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. (owner: Ahmed Benali)
* **A-59** `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** MVE-01 for the production database settings only (decision before those settings are committed); test hosting does not wait for it, and the runtime choice is a decision under O-03, not an experiment

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-01 and serves BR-13) · **Rank:** 15 · **Parent:** FEAT-113

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-15/AC1** Given the hosting definition for `tst` and for `prd`, When `az bicep build` is run locally on each, Then it passes, names and tags follow ES-23 and ES-24, and nothing is applied to a subscription (ES-27).
* **EA-15/AC2** Given it is not yet decided whether Order Desk is rehosted unchanged on a Windows virtual machine or waits for `net10.0` and a managed web service (O-03, A-20), When the definition is reviewed, Then it states which runtime it describes, names the other as **OPEN:** O-03 with Ahmed Benali as owner, and presents no runtime as decided.
* **EA-15/AC3** Given the hosted application needs the order database and Key Vault, When its settings are reviewed, Then it reaches them through a managed identity and a private endpoint with no password in any file (CS-13, ES-25).
* **EA-15/AC4** Given Order Desk keeps the order draft in the process session today (CS-16), When the definition is reviewed, Then it runs one instance until the draft is stateless (X-07), and no scale-out is assumed.
* **EA-15/AC5** Given today's load of average CPU 18 % and peak 55 % (CS-06), When the host size is chosen, Then the size is listed in the cost model of `EA-09`, and the definition exposes the endpoint that the synthetic probe of `STORY-142` calls (NFR-01).
* **EA-15/AC6** Given the data tier is not yet decided (MVE-01, `EA-05`), When the definitions are reviewed, Then `tst` hosting is complete with a placeholder connection setting that points to user secrets or a managed identity and holds no password (ES-17, ES-25), and the production database settings in `prd` are marked **OPEN:** until `EA-05` records the decision; a Stop or Adjust result delays only those production settings.

### 51. wael-01 EA-06 Redesign the StockPilot exchange without changing the file contract

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 16

**Description**

**EA-06** (BACKLOG-NW-001) · **Source ids:** C-03, CS-10, FR-109

**Source:** (source: CS-10, C-03)

**Serves:** FR-109

**Story:** As an Azure platform engineer, I want the nightly exchange with StockPilot redesigned for the chosen data tier with the file contract unchanged and no Windows-only tool, so that StockPilot (which stays on premises until at least 2028) needs no change.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-05 (Azure owns the exchange end to end; .NET only reads the status results). **Relies on:** A-27, A-30; O-15, O-16; MVE-O-05.

**Register text for the ids cited in this item (backlog section 7):**

* **A-27** The StockPilot CSV contract and file pick-up stay as they are. (owner: Ahmed Benali)
* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **MVE-O-05** Where the SQL Server Agent job and the Windows scheduled task for the Antwerp transfer are defined. (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-16** How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? (owner: Ahmed Benali, Pieter Janssens)
* **X-05** StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 16 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-06/AC1** Given the nightly job at 02:00 that exports confirmed orders as CSV files to an SFTP server and imports shipment updates (CS-10), When the redesign is compared with the file-contract baseline, Then file format, file names and the pick-up point are the same as today (A-27).
* **EA-06/AC2** Given the redesign, When its steps are listed, Then none depends on `xp_cmdshell` or another Windows-only tool.
* **EA-06/AC3** Given the SFTP route after the lease is not known (O-15), When the redesign names it, Then the route is marked **OPEN:** with its owner.

### 52. wael-01 EA-07 Design invoice storage and synchronisation

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 17

**Description**

**EA-07** (BACKLOG-NW-001) · **Source ids:** CS-08, CS-11, CS-14, FR-110

**Source:** (source: CS-08, CS-11, CS-14)

**Serves:** FR-110

**Story:** As an Azure platform engineer, I want a design for storing and synchronising the invoice PDFs, so that the portal can later serve invoices from Azure while the finance system keeps writing them.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **A-15** The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. (owner: Julien Moreau)
* **MVE-A-03** Growth stays linear. From mid-November 2026 to 30 June 2027 is 7 to 7.5 months, so the database reaches about 56 GB (48 GB plus 7.5 months at 1 GB) and invoices about 135 GB (120 GB plus 7.5 months at 2 GB). The month count is itself an assumption. (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Should (A-49) · **Rank:** 17 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-07/AC1** Given the finance system writes one PDF per invoice to `\\NWFS01\invoices\{year}\{invoiceNumber}.pdf` (CS-11), When the design is read, Then the finance system stays the writer and the design states where the files live after the lease.
* **EA-07/AC2** Given about 120 GB today growing about 2 GB a month (CS-08), When capacity is checked, Then the design covers about 135 GB by 30 June 2027 and continued growth (linear growth over 7 to 7.5 months, MVE-A-03).
* **EA-07/AC3** Given where the finance system writes after the lease is unknown (O-15), When the design names the location, Then it is marked **OPEN:**.

### 53. wael-01 EA-12 Design outbound mail to replace the on-premises relay

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 18

**Description**

**EA-12** (BACKLOG-NW-001) · **Source ids:** BR-09, CS-12, FR-113

**Source:** (source: CS-12, A-29, BR-09)

**Serves:** FR-113

**Story:** As an Azure platform engineer, I want a design for an outbound mail service, so that e-mail still leaves Northwind after the unauthenticated on-premises relay `smtp.northwind.local` stops being usable.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** X-10 (.NET uses a mail abstraction and a local mail catcher meanwhile). **Relies on:** A-29, A-51; O-17.

**Register text for the ids cited in this item (backlog section 7):**

* **A-29** The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. (owner: Ahmed Benali)
* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **O-17** What sends order confirmations today? (owner: Ahmed Benali)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Should (A-49: it serves only `BR-09`, a requirement of another track) · **Rank:** 18 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-12/AC1** Given the current relay on port 25 without authentication (CS-12), When the design is read, Then it names the outbound mail path for after the lease and requires authentication.
* **EA-12/AC2** Given it is not known what sends order confirmations today (O-17), When the design is reviewed, Then that question is marked **OPEN:** and the design does not assume an answer.

### 54. wael-01 STORY-140 Keep the nightly StockPilot exchange working after the database moves

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 19

**Description**

**STORY-140** (BACKLOG-NW-001) · **Source ids:** BR-13, C-03, CS-10, FR-109

**Source:** (source: C-03, CS-10, BR-13)

**Implements:** FR-109

**Story:** As an Order Desk supervisor, I want the nightly exchange of confirmed orders and shipment updates with StockPilot to keep working after the database is in Azure, so that warehouse picking in Antwerp is not interrupted.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-06`. **Cross-track (OPEN):** X-05. **Relies on:** A-27, A-30; O-16; MVE-O-05.

**Register text for the ids cited in this item (backlog section 7):**

* **A-27** The StockPilot CSV contract and file pick-up stay as they are. (owner: Ahmed Benali)
* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **MVE-O-05** Where the SQL Server Agent job and the Windows scheduled task for the Antwerp transfer are defined. (owner: Ahmed Benali)
* **O-16** How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? (owner: Ahmed Benali, Pieter Janssens)
* **X-05** StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Must · **Rank:** 19 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-140/AC1** Given the order database is in Azure, When the nightly job runs at 02:00, Then confirmed orders are exported with the same file format to the same pick-up point and shipment updates are imported; StockPilot is not changed.
* **STORY-140/AC2** Given the replacement design, When it is reviewed, Then it does not depend on Windows-only tools.
* **STORY-140/AC3** Given a produced file differs from the baseline format in a column, a name or a location, When the comparison is run, Then the story fails and no file is handed to StockPilot.

### 55. wael-01 STORY-141 Decide where invoice files live after the lease

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 20

**Description**

**STORY-141** (BACKLOG-NW-001) · **Source ids:** CS-08, CS-11, CS-14, FR-110

**Source:** (source: CS-08, CS-11, CS-14)

**Implements:** FR-110

**Story:** As the IT manager, I want a design for invoice storage that states where the PDFs live after the lease, so that invoice access keeps working when the file share is gone.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-07`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **A-15** The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. (owner: Julien Moreau)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Should · **Rank:** 20 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-141/AC1** Given about 120 GB of invoice PDFs growing about 2 GB a month, When the design is reviewed, Then it covers that size and growth and the finance system stays the writer.
* **STORY-141/AC2** Given the location after the lease depends on an unanswered question (O-15), When the design is reviewed, Then the location is marked **OPEN:** with Julien Moreau and Ahmed Benali as owners and the story still completes as a design.

### 56. wael-01 STORY-144 Replace the on-premises mail relay for outbound e-mail

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-106 · **Priority:** Could (proposed ADO priority 3) · **Rank:** 21

**Description**

**STORY-144** (BACKLOG-NW-001) · **Source ids:** BR-09, CS-12, FR-113

**Source:** (source: CS-12, BR-09)

**Implements:** FR-113

**Story:** As the IT manager, I want a design for outbound e-mail that replaces the on-premises relay, so that e-mails such as the Shipped notice (`BR-09`) can still be sent after the lease.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-12`. **Cross-track (OPEN):** X-10. **Relies on:** A-29; O-17, O-24. **Note:** supports `BR-09`; `BR-09` itself is covered by STORY-262.

**Register text for the ids cited in this item (backlog section 7):**

* **A-29** The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. (owner: Ahmed Benali)
* **O-17** What sends order confirmations today? (owner: Ahmed Benali)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Could · **Rank:** 21 · **Parent:** FEAT-106

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-144/AC1** Given the on-premises relay is not usable after the lease (A-29), When the design is reviewed, Then it names the replacement path and that path is in the EU (NFR-03).
* **STORY-144/AC2** Given what sends order confirmations today is unknown (O-17), When the design is reviewed, Then the open question is listed and no assumption is built in.

### 57. wael-01 EA-04 Build observability: log workspace, application monitoring and alerts

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-107 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 22

**Description**

**EA-04** (BACKLOG-NW-001) · **Source ids:** CS-15, CS-22, ES-26, FR-111, FR-119, NFR-01

**Source:** (source: CS-15, CS-22, ES-26, NFR-01)

**Serves:** FR-111, FR-119

**Story:** As an Azure platform engineer, I want one log workspace per environment, one application monitoring service and alerts defined as code, so that the ping checks and the weekly look at the Windows Event Log (CS-22) are replaced.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-08 (.NET logs through the standard logger to the console meanwhile). **Relies on:** A-05.

**Register text for the ids cited in this item (backlog section 7):**

* **A-05** `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. (owner: Ahmed Benali)
* **X-08** Logging moves to Application Insights and Log Analytics (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-01) · **Rank:** 22 · **Parent:** FEAT-107

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-04/AC1** Given the environments `tst` and `prd`, When the design is validated locally, Then each has exactly one log workspace and the diagnostics of every resource are sent to it (ES-26).
* **EA-04/AC2** Given an application of Order Desk or the portal, When its monitoring is reviewed, Then it reports to the application monitoring service.
* **EA-04/AC3** Given today's ping checks of `NWWEB01` and `NWSQL01` and the weekly Event Log look, When the alerts are listed, Then an availability alert and an application-error alert replace each of them.

### 58. wael-01 STORY-142 Monitor availability with a synthetic probe and alerts

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-107 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 23

**Description**

**STORY-142** (BACKLOG-NW-001) · **Source ids:** CS-15, CS-22, ES-26, FR-111, NFR-01

**Source:** (source: NFR-01, CS-15, CS-22, ES-26)

**Implements:** FR-111 · **Covers:** NFR-01 (design and alerting)

**Story:** As the IT manager, I want availability measured by a synthetic probe and alerted on, so that I know whether the 99.5 % target for Monday to Saturday 06:00 to 20:00 is met.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-04`. **Cross-track (OPEN):** X-08. **Relies on:** A-05; T-17.

**Register text for the ids cited in this item (backlog section 7):**

* **A-05** `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. (owner: Ahmed Benali)
* **T-17** `NFR-01` uses CET only but business hours cross the summer-time change (A-05). (owner: Ahmed Benali)
* **X-08** Logging moves to Application Insights and Log Analytics (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 23 · **Parent:** FEAT-107

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-142/AC1** Given the portal is live, When a synthetic probe at the hosting edge requests it, Then availability is calculated per week in local Central European time, with summer time, over Monday to Saturday 06:00 to 20:00 (84 hours a week) (A-05, T-17).
* **STORY-142/AC2** Given 99.5 % of 84 hours allows about 25 minutes of downtime a week (derived), When measured availability in a week falls below 99.5 %, Then an alert goes to the IT team.
* **STORY-142/AC3** Given downtime on a Sunday between 06:00 and 12:00 (the maintenance window, CS-21), When availability is calculated, Then that downtime is not counted, because it is outside business hours.
* **STORY-142/AC4** Given the week of a summer-time change, When the business hours are applied, Then they follow local Central European time, not a fixed offset.

### 59. wael-01 EA-10 Define the tst environment

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-108 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 24

**Description**

**EA-10** (BACKLOG-NW-001) · **Source ids:** ES-23, FR-112

**Source:** (source: ES-23, business-case section 8)

**Serves:** FR-112

**Story:** As an Azure platform engineer, I want the `tst` environment defined as code, so that the portal pilot has an environment to run on.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-01`. **Cross-track (OPEN):** X-01, X-02. **Relies on:** A-37; O-23.

**Register text for the ids cited in this item (backlog section 7):**

* **A-37** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. (owner: Ahmed Benali)
* **O-23** Which database does the Q2 2027 portal pilot read (T-08)? (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 24 · **Parent:** FEAT-108

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-10/AC1** Given the `tst` entry point, When `az bicep build` is run locally, Then it passes, names follow ES-23 and tags follow ES-24.
* **EA-10/AC2** Given the application is not yet on `net10.0`, When the `tst` definition is validated, Then it still validates, because it does not depend on how the application is built (X-02).
* **EA-10/AC3** Given the pilot must not read a database that is being moved, When the definition is reviewed, Then it states which database the pilot reads; until O-23 is answered that statement is **ASSUMPTION:** A-37 (the Azure-hosted database after `azure-r2` is approved).

### 60. wael-01 STORY-143 Define a test environment where the portal pilot can run

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-108 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 25

**Description**

**STORY-143** (BACKLOG-NW-001) · **Source ids:** C-04, ES-23, FR-112

**Source:** (source: ES-23, C-04, business-case section 8)

**Implements:** FR-112

**Story:** As the .NET team lead, I want a defined test environment, so that the 20-customer portal pilot planned for Q2 2027 can run on it.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-10`; the pilot runs on the application hosting of `EA-15`. **Cross-track (OPEN):** X-01 (.NET builds and tests locally until pilot hosting is answered), X-02. **Relies on:** A-37; O-23.

**Register text for the ids cited in this item (backlog section 7):**

* **A-37** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. (owner: Ahmed Benali)
* **O-23** Which database does the Q2 2027 portal pilot read (T-08)? (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Must · **Rank:** 25 · **Parent:** FEAT-108

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-143/AC1** Given the `tst` definition, When it is validated locally, Then it passes, lists every resource the pilot needs, and each resource name and tag follow ES-23 and ES-24.
* **STORY-143/AC2** Given the definition, When it is reviewed, Then it does not depend on how the application is built, so the .NET track is not blocked and the Azure track is not blocked by .NET (X-02).
* **STORY-143/AC3** Given the cost of `tst` is part of the EUR 1,500 cap, When the definition is reviewed, Then it appears in the cost model (STORY-121).

### 61. wael-01 EA-08 Design backup, long-term retention and recovery

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-109 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 26

**Description**

**EA-08** (BACKLOG-NW-001) · **Source ids:** CS-07, CS-23, FR-114, FR-115, NFR-06, NFR-08

**Source:** (source: CS-07, CS-23, NFR-06, NFR-08)

**Serves:** FR-114, FR-115

**Story:** As an Azure platform engineer, I want the backup, long-term retention and restore design for the order database, so that recovery and the 7-year audit record are designed before cutover. The first recovery test plan is `EA-14` in `azure-r3`.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`. **Cross-track (OPEN):** X-15. **Relies on:** A-31, A-33; T-14.

**Register text for the ids cited in this item (backlog section 7):**

* **A-31** Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). (owner: Ahmed Benali)
* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **T-14** The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). (owner: Ahmed Benali)
* **X-15** Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-06, NFR-08) · **Rank:** 26 · **Parent:** FEAT-109

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-08/AC1** Given today's log backups every 15 minutes (CS-07), When the design states the backup frequency in Azure, Then it is 60 minutes or less (the RPO of 1 hour).
* **EA-08/AC2** Given order-change records must be kept 7 years, When the design is read, Then it shows how backup and long-term retention achieve 7 years; limits not verified are marked **ASSUMPTION:** A-31.
* **EA-08/AC3** Given the design, When it is reviewed, Then it names the restore method and who runs a restore.

### 62. wael-01 STORY-145 Keep order-change records for 7 years in Azure

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-109 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 27

**Description**

**STORY-145** (BACKLOG-NW-001) · **Source ids:** CS-07, FR-114, NFR-08

**Source:** (source: NFR-08, CS-07)

**Implements:** FR-114 · **Covers:** NFR-08 (retention design)

**Story:** As the IT manager, I want a retention design that keeps the record of every order change for 7 years once the database is in Azure, so that the audit requirement stays met after the move.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-08`. **Cross-track (OPEN):** X-15 (.NET defines the audit content, Azure sets retention). **Relies on:** A-31.

**Register text for the ids cited in this item (backlog section 7):**

* **A-31** Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). (owner: Ahmed Benali)
* **X-15** Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** through `EA-08` (MVE-01)

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 27 · **Parent:** FEAT-109

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-145/AC1** Given the retention design, When it is reviewed, Then it shows 7 years for the order-change records and states how backup and long-term retention achieve it.
* **STORY-145/AC2** Given a chosen service tier keeps backups for less than 7 years, When the design is reviewed, Then it is rejected or an exception is sent to the product owner; it is not accepted silently.
* **STORY-145/AC3** Given the feature limits are not verified (A-31), When the design is read, Then they are listed as **ASSUMPTION:** with Ahmed Benali as confirming owner.

### 63. wael-01 STORY-146 Design backup and recovery for RPO 1 hour and RTO 4 hours

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r2` · **Parent:** FEAT-109 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 28

**Description**

**STORY-146** (BACKLOG-NW-001) · **Source ids:** CS-07, CS-23, FR-115, NFR-06

**Source:** (source: NFR-06, CS-07, CS-23)

**Implements:** FR-115 · **Covers:** NFR-06 (design)

**Story:** As the IT manager, I want a backup and recovery design that reaches an RPO of 1 hour and an RTO of 4 hours for order data, so that a failure loses at most an hour of orders and is repaired within four hours.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-33; T-14.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **T-14** The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). (owner: Ahmed Benali)

**Gate:** MVE-01

**Track tag:** track-azure · **Release tag:** azure-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 28 · **Parent:** FEAT-109

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-146/AC1** Given the design, When it is read, Then it states the backup frequency, the restore method and who runs a restore, and shows how RPO 1 hour and RTO 4 hours are reached.
* **STORY-146/AC2** Given the documented backup frequency is longer than 60 minutes (`M1c` fails), When the design is reviewed, Then RPO 1 hour is not met and the design is returned for rework.
* **STORY-146/AC3** Given a recovery has never been tested (CS-23), When the design is read, Then it does not claim the target is met; proof is the restore test of `STORY-172` in `azure-r3`.

### 64. wael-01 EA-16 Migrate the NorthwindOrders database to the chosen data tier and rehearse the move

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-114 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 29

**Description**

**EA-16** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, C-02, CS-07, CS-23, FR-106, FR-116, NFR-03, NFR-06

**Source:** (source: BR-13, C-01, C-02, NFR-03, NFR-06, CS-07, CS-23)

**Serves:** FR-106, FR-116 · **Added after the first review (A-59)**

**Story:** As an Azure platform engineer, I want the move of the `NorthwindOrders` database to the chosen data tier written as repeatable steps that are checked locally, with a rehearsal plan, so that the data can move inside the Sunday window and the first restore test starts from a database that was moved the same way.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-05`, `EA-08`, `EA-15`; feeds `EA-13`, `EA-14`. **Cross-track (OPEN):** X-03 (database sign-in moves from Windows-integrated to a managed identity; .NET builds against a local SQL Server meanwhile). **Relies on:** A-21, A-30, A-33, A-53, A-59; O-03, O-15, O-27.

**Register text for the ids cited in this item (backlog section 7):**

* **A-21** A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. (owner: Ahmed Benali)
* **A-30** SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). (owner: Ahmed Benali)
* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **A-59** `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-27** Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. (owner: Marc Dubois)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)

**Gate:** MVE-01 (decision before commit)

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-03 and NFR-06 and serves BR-13) · **Rank:** 29 · **Parent:** FEAT-114

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-16/AC1** Given the data tier decided in `STORY-120` (MVE-01 decided), When the migration steps are read, Then they cover schema, data, sign-in and every job that has no equivalent (A-30), each step has a longest allowed duration, and the total fits the Sunday window set in `STORY-122`.
* **EA-16/AC2** Given a rehearsal copy of the database, When the row counts and checksums of the order tables are compared with the source, Then they match; a difference fails the rehearsal and the migration is not accepted.
* **EA-16/AC3** Given the target data tier, When its region is read, Then it is France Central or another EU region (NFR-03); a tier outside the EU is rejected.
* **EA-16/AC4** Given recovery has never been tested (CS-23), When the migration procedure is read, Then it hands the moved copy to `EA-14` for the first restore test (NFR-06) and claims no recovery result before that test is run.
* **EA-16/AC5** Given MVE-01 has not been decided or ended in **stop**, When the release is considered for commitment, Then `EA-16` stays uncommitted (gate) and the items marked gate *none* continue.
* **EA-16/AC6** Given `azure-r3` is approved before the first rehearsal Sunday (before 6 June 2027), When the rehearsal Sundays (6 and 13 June 2027) arrive, Then the rehearsals are planned execution after that approval and are not claimed in this release (A-53, ES-27).

### 65. wael-01 EA-13 Write cutover, rollback and decommission runbooks

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-110 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 30

**Description**

**EA-13** (BACKLOG-NW-001) · **Source ids:** BR-13, C-02, CS-21, FR-116, FR-117, FR-119, FR-120, SM-07

**Source:** (source: CS-21, BR-13, C-02, SM-07)

**Serves:** FR-116, FR-117, FR-119, FR-120

**Story:** As an Azure platform engineer, I want written runbooks for cutover, rollback and decommission, so that the move and the retirement of the old servers follow reviewed steps.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-04`, `EA-08`, `EA-05`, `EA-15`, `EA-16`. **Cross-track (OPEN):** X-07, O-15. **Relies on:** A-33, A-53, A-58; O-03, O-27.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **A-58** The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). (owner: Marc Dubois)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-27** Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. (owner: Marc Dubois)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 30 · **Parent:** FEAT-110

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-13/AC1** Given the Sunday window of 06:00 to 12:00 CET (CS-21), When a cutover runbook is read, Then every step has a longest allowed duration and the sum fits the window.
* **EA-13/AC2** Given any cutover step, When the rollback runbook is read, Then it has a path that returns Order Desk to the previous service inside the same window.
* **EA-13/AC3** Given the decommission runbook, When it is read, Then it states how and when `NWWEB01` and `NWSQL01` are retired so that no production server is past end of support by 30 June 2027.
* **EA-13/AC4** Given the rehearsal plan, When it is read, Then it names 6 and 13 June 2027 for rehearsal and 20 and 27 June 2027 for live cutover and fallback (Sundays computed from CS-21), all inside the `azure-r3` window that ends on 27 June 2027 (A-58); the plan states that approval comes before the first rehearsal Sunday, before 6 June 2027 (A-53), and carries **OPEN:** O-27.

### 66. wael-01 STORY-170 Keep staff working through the cutover inside the Sunday window

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-110 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 31

**Description**

**STORY-170** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, CS-21, FR-116

**Source:** (source: BR-13, C-01, CS-21)

**Implements:** FR-116 · **Covers:** BR-13

**Story:** As an Order Desk staff member, I want planned downtime during the move to stay inside the Sunday maintenance window, so that I can keep taking orders Monday to Saturday.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-13`; it also builds on the hosting `EA-15` and the migration procedure `EA-16`. **Cross-track (OPEN):** X-07, O-15. **Relies on:** A-33, A-53; O-03, O-27.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **O-27** Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. (owner: Marc Dubois)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** story · **Priority:** Must · **Rank:** 31 · **Parent:** FEAT-110

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-170/AC1** Given the cutover plan, When its steps are added up, Then planned downtime is inside Sunday 06:00 to 12:00 CET.
* **STORY-170/AC2** Given a step has no stated longest duration, When the plan is reviewed, Then the plan is not accepted.
* **STORY-170/AC3** Given a step's longest duration would push the total past 12:00, When the plan is reviewed, Then the step is split across Sundays or a rollback is defined; the plan is not accepted otherwise.

### 67. wael-01 STORY-171 Define rollback and rehearsal for every cutover step

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-110 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 32

**Description**

**STORY-171** (BACKLOG-NW-001) · **Source ids:** BR-13, C-01, CS-21, FR-117

**Source:** (source: BR-13, C-01, CS-21)

**Implements:** FR-117 · **Covers:** BR-13

**Story:** As the IT manager, I want every cutover step to have a rollback path and a rehearsal plan with a result template, so that a failed Sunday never leaves Order Desk down on Monday.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-13`. **Cross-track (OPEN):** X-07. **Relies on:** A-53; O-27.

**Register text for the ids cited in this item (backlog section 7):**

* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **O-27** Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. (owner: Marc Dubois)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** story · **Priority:** Must · **Rank:** 32 · **Parent:** FEAT-110

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-171/AC1** Given each cutover step, When the rollback is read, Then it returns Order Desk to the previous service inside the same window.
* **STORY-171/AC2** Given the rehearsal plan, When it is read, Then it names the Sundays for rehearsal, live cutover and fallback and includes a template to record each result.
* **STORY-171/AC3** Given a step has no rollback path, When the plan is reviewed, Then the release is not approved.

### 68. wael-01 EA-14 Write the first recovery test plan and evidence template

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-111 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 33

**Description**

**EA-14** (BACKLOG-NW-001) · **Source ids:** CS-23, FR-118, NFR-06

**Source:** (source: NFR-06, CS-23, T-14)

**Serves:** FR-118 · **New in this plan (split from `EA-08`)**

**Story:** As an Azure platform engineer, I want a recovery test plan and an evidence template, so that the first restore test has fixed steps and a fixed way to record the result.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-08`. **Cross-track (OPEN):** none. **Relies on:** A-33, A-53; T-14.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **T-14** The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-06) · **Rank:** 33 · **Parent:** FEAT-111

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EA-14/AC1** Given a restore test, When the template is filled in, Then it records the measured data loss in minutes and the restore time in hours, next to the pass limits of 60 minutes and 4 hours.
* **EA-14/AC2** Given the plan, When it is read, Then it states who restores, from which backup and when.
* **EA-14/AC3** Given recovery has never been tested (CS-23), When the plan is read, Then it calls the first test the baseline and does not claim any earlier result.

### 69. wael-01 STORY-172 Prove recovery against RPO 1 hour and RTO 4 hours

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-111 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 34

**Description**

**STORY-172** (BACKLOG-NW-001) · **Source ids:** CS-07, CS-23, FR-118, NFR-06

**Source:** (source: NFR-06, CS-07, CS-23)

**Implements:** FR-118 · **Covers:** NFR-06 (proof)

**Story:** As the IT manager, I want a recovery test plan and evidence template that define how a restore is tested against RPO 1 hour and RTO 4 hours, so that the product owner can see proof and not only a design.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-14`. **Cross-track (OPEN):** none. **Relies on:** A-33, A-53; T-14.

**Register text for the ids cited in this item (backlog section 7):**

* **A-33** A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. (owner: Ahmed Benali)
* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **T-14** The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 34 · **Parent:** FEAT-111

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-172/AC1** Given a restore test is run from backups, When the result is recorded in the template, Then data loss is at most 60 minutes (RPO 1 hour) and time to restore is at most 4 hours (RTO 4 hours) for a pass.
* **STORY-172/AC2** Given a measured data loss of more than 60 minutes or a restore time of more than 4 hours, When the result is recorded, Then `NFR-06` is recorded as **not met** and the backup design (`EA-08`) is reopened.
* **STORY-172/AC3** Given the release is approved, When the test is carried out, Then it is a real-world operation after approval and not claimed in this release (A-53, ES-27).

### 70. wael-01 STORY-173 Plan the availability proof for the first weeks in Azure

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-111 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 35

**Description**

**STORY-173** (BACKLOG-NW-001) · **Source ids:** CS-22, FR-119, NFR-01

**Source:** (source: NFR-01, CS-22)

**Implements:** FR-119 · **Covers:** NFR-01 (proof)

**Story:** As the product owner, I want a plan that states how availability is observed in the first weeks in Azure and what evidence I will see, so that I can judge whether 99.5 % is met.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-13`, `EA-04`. **Cross-track (OPEN):** none. **Relies on:** A-05; T-17.

**Register text for the ids cited in this item (backlog section 7):**

* **A-05** `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. (owner: Ahmed Benali)
* **T-17** `NFR-01` uses CET only but business hours cross the summer-time change (A-05). (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 35 · **Parent:** FEAT-111

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-173/AC1** Given the proof plan, When it is read, Then it uses the synthetic-probe rule of `STORY-142` (hosting edge, local Central European time with summer time, Monday to Saturday 06:00 to 20:00) (A-05).
* **STORY-173/AC2** Given the plan, When it is read, Then it lists the evidence shown to the product owner: the weekly availability figure and each downtime event with its start, end and cause.
* **STORY-173/AC3** Given a week below 99.5 %, When the evidence is read, Then the week is flagged `not met` and not averaged away.

### 71. wael-01 STORY-174 Retire the old web and database servers before 30 June 2027

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-azure; azure-r3` · **Parent:** FEAT-112 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 36

**Description**

**STORY-174** (BACKLOG-NW-001) · **Source ids:** C-01, C-02, FR-120, SM-07

**Source:** (source: C-02, SM-07, C-01)

**Implements:** FR-120

**Story:** As the sponsor (Marc Dubois), I want a decommission plan for the old web server and database server, so that no production server is past end of support by 30 June 2027 and payments for Extended Security Updates stop.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EA-13`. **Cross-track (OPEN):** O-15 (where the finance system, shares and domain controllers live after the lease). **Relies on:** A-53; O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **A-53** Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)

**Gate:** none

**Track tag:** track-azure · **Release tag:** azure-r3 · **Type:** story · **Priority:** Must · **Rank:** 36 · **Parent:** FEAT-112

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-174/AC1** Given the decommission plan, When it is read, Then it states how and when `NWWEB01` and `NWSQL01` are retired so that the count of production servers past end of support is 0 by 30 June 2027 (SM-07).
* **STORY-174/AC2** Given the plan, When it is read, Then it states the date on which ESU payments stop.
* **STORY-174/AC3** Given a retirement date after 30 June 2027, When the plan is reviewed, Then the plan is not accepted.

### 72. wael-01 EN-01 Convert the solution to SDK-style projects on net10.0

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 1

**Description**

**EN-01** (BACKLOG-NW-001) · **Source ids:** CS-01, CS-02, ES-13, ES-14, ES-19, FR-201, FR-203

**Source:** (source: CS-01, CS-02, ES-13, ES-14, ES-19)

**Serves:** FR-201, FR-203

**Story:** As a .NET developer, I want `Core`, `Web` and `Tests` converted to SDK-style projects on `net10.0` inside the one existing solution, so that the application builds on the current long-term support release.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none; first .NET item. **Cross-track (OPEN):** X-02, X-14. **Relies on:** O-03, O-20.

**Register text for the ids cited in this item (backlog section 7):**

* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **O-20** Decision record on the portal and API project shape (ES-13). (owner: Ahmed Benali)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 1 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-01/AC1** Given `src/Northwind.OrderDesk.sln`, When `dotnet build src/Northwind.OrderDesk.sln` runs, Then `Core` and `Tests` build as SDK-style projects targeting `net10.0`, no `packages.config` remains, and `Web` builds once `EN-08` is also done.
* **EN-01/AC2** Given the solution, When its projects are listed, Then there is one solution and the same three projects (ES-13); namespaces and domain types are unchanged (ES-19).
* **EN-01/AC3** Given a change would add a project, When it is proposed, Then a decision record (`EN-13`) must exist first; without it the change is rejected.
* **EN-01/AC4** Given the database client, When the solution is built, Then it uses the current SQL client library.

### 73. wael-01 EN-13 Record the decision on portal and API project shape

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 2

**Description**

**EN-13** (BACKLOG-NW-001) · **Source ids:** ES-13, FR-201

**Source:** (source: ES-13, O-20)

**Serves:** FR-201

**Story:** As the .NET team lead, I want a decision record that says whether the portal is an area of `Web` or a new project and whether an API project exists, so that no project is added without a reason (ES-13).

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** X-14 (hosting shape is Azure's). **Relies on:** O-01, O-20; T-10.

**Register text for the ids cited in this item (backlog section 7):**

* **O-01** Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? (owner: Ahmed Benali)
* **O-20** Decision record on the portal and API project shape (ES-13). (owner: Ahmed Benali)
* **T-10** ES-13 (one solution) and ES-19 versus a portal, an API and a re-platform (`EN-13`). (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 2 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-13/AC1** Given the decision, When the record is read, Then it is stored with the architecture decision records (`docs/architecture/`, ES-08) and states the choice, the reasons and the consequences.
* **EN-13/AC2** Given no decision record exists, When anyone proposes a new project, Then it is not added (ES-13).
* **EN-13/AC3** Given who owns the Order Desk API is unknown (O-01), When the record discusses an API project, Then it marks that part **OPEN:** and does not assume an owner.

### 74. wael-01 EN-03 Replace direct ConfigurationManager calls with the options pattern

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 3

**Description**

**EN-03** (BACKLOG-NW-001) · **Source ids:** CS-17, ES-15, FR-201

**Source:** (source: CS-17, ES-15)

**Serves:** FR-201

**Story:** As a .NET developer, I want configuration read through `Microsoft.Extensions.Configuration` and the options pattern, so that the application takes settings from environment variables and the cloud, as the contract with Azure needs.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-02. **Relies on:** none.

**Register text for the ids cited in this item (backlog section 7):**

* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 3 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-03/AC1** Given the code base, When it is searched, Then no direct `ConfigurationManager` call remains (ES-15).
* **EN-03/AC2** Given each setting that was read before, When the application starts with the same values, Then it behaves as before (a check covers each setting).
* **EN-03/AC3** Given a required setting is missing, When the application starts, Then startup fails with a message that names the setting and never prints a secret value.

### 75. wael-01 EN-05 Replace the Windows Event Log logger with standard logging

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 4

**Description**

**EN-05** (BACKLOG-NW-001) · **Source ids:** CS-15, ES-16, FR-201

**Source:** (source: CS-15, ES-16)

**Serves:** FR-201

**Story:** As a .NET developer, I want errors logged through `ILogger<T>` instead of the Windows Event Log, so that logging works on any machine and can later feed Azure monitoring.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-08. **Relies on:** none.

**Register text for the ids cited in this item (backlog section 7):**

* **X-08** Logging moves to Application Insights and Log Analytics (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 4 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-05/AC1** Given the code base, When it is searched, Then nothing writes to the Windows Event Log (ES-16).
* **EN-05/AC2** Given the existing tests of logging behaviour, When `dotnet test` runs, Then they still pass and their coverage is kept.
* **EN-05/AC3** Given an error on macOS or Linux, When it occurs, Then it appears in the console log.

### 76. wael-01 EN-06 Replace the in-process session order draft

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 5

**Description**

**EN-06** (BACKLOG-NW-001) · **Source ids:** CS-16, FR-214

**Source:** (source: CS-16)

**Serves:** FR-214

**Story:** As a .NET developer, I want the order being entered stored outside the web process, so that a restart or a second server does not lose it.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-07 (Azure starts with a single instance, as today, until this is done). **Relies on:** none.

**Register text for the ids cited in this item (backlog section 7):**

* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 5 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-06/AC1** Given a user has an order draft, When the application restarts or the next request goes to another instance, Then the draft is still there.
* **EN-06/AC2** Given the code base, When it is searched, Then no `InProc` session state remains for the order draft (CS-16).
* **EN-06/AC3** Given a draft that does not exist (for example removed), When the user opens it, Then a clear "draft not found" message is shown and no error page.

### 77. wael-01 EN-08 Port the web layer to ASP.NET Core MVC with Entra ID staff sign-in

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 6

**Description**

**EN-08** (BACKLOG-NW-001) · **Source ids:** CS-04, ES-14, ES-19, FR-201, FR-204, FR-210, FR-220, NFR-04

**Source:** (source: CS-04, NFR-04, ES-14, ES-19)

**Serves:** FR-201, FR-204, FR-210, FR-220

**Story:** As a .NET developer, I want the web layer on ASP.NET Core MVC with Microsoft Entra ID sign-in for staff, so that the application no longer needs Windows Integrated Authentication or Windows-only hosting.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-04 (staff sign-in; .NET uses provider-neutral sign-in and a test identity). **Relies on:** A-10; O-03.

**Register text for the ids cited in this item (backlog section 7):**

* **A-10** Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. (owner: Ahmed Benali)
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 6 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-08/AC1** Given the existing staff screens, When they are opened after the port, Then each shows the same fields and behaves as before; any difference is listed as a defect.
* **EN-08/AC2** Given a Northwind staff member with a Microsoft Entra ID account, When they sign in (a test identity is used locally), Then they reach Order Desk; given an account that is not a Northwind staff account, Then sign-in is refused.
* **EN-08/AC3** Given the code base, When it is searched, Then no Windows Integrated Authentication setting remains (CS-04).

### 78. wael-01 STORY-201 Run Order Desk on .NET 10 with unchanged staff screens

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-201 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 7

**Description**

**STORY-201** (BACKLOG-NW-001) · **Source ids:** CS-01, CS-02, ES-13, ES-14, ES-19, FR-201

**Source:** (source: CS-01, CS-02, ES-13, ES-14, ES-19)

**Implements:** FR-201

**Story:** As an Order Desk staff member, I want Order Desk to run on the current .NET long-term support release with the screens I use today, so that my daily work does not change while the platform under it does.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`, `EN-03`, `EN-05`, `EN-08`, `EN-13`. **Cross-track (OPEN):** X-14; hosting is X-01. **Relies on:** O-20.

**Register text for the ids cited in this item (backlog section 7):**

* **O-20** Decision record on the portal and API project shape (ES-13). (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)
* **X-14** One solution and three projects versus a portal area and an API: a decision record is needed (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must · **Rank:** 7 · **Parent:** FEAT-201

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-201/AC1** Given the solution, When `dotnet build src/Northwind.OrderDesk.sln` runs, Then all three projects build on `net10.0`.
* **STORY-201/AC2** Given each existing staff screen, When it is compared with the current application using a regression checklist, Then fields and behaviour are the same.
* **STORY-201/AC3** Given a namespace, domain type or behaviour, When it is compared, Then it is unchanged unless a decision record explains the change (ES-19).
* **STORY-201/AC4** Given a screen behaves differently from today, When the checklist is reviewed, Then the difference is a defect and the release is not approved until it is fixed or accepted by the product owner.

### 79. wael-01 EN-02 Replace MSTest v1 so all tests run on Windows, macOS and Linux

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-202 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 8

**Description**

**EN-02** (BACKLOG-NW-001) · **Source ids:** CS-18, CS-20, ES-18, FR-202

**Source:** (source: CS-18, CS-20, ES-18)

**Serves:** FR-202

**Story:** As a .NET developer, I want the unit tests moved off MSTest v1 (which only runs inside Visual Studio) to a current test framework, so that anyone can run them anywhere.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** X-11. **Relies on:** none.

**Register text for the ids cited in this item (backlog section 7):**

* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 8 · **Parent:** FEAT-202

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-02/AC1** Given any machine with the .NET SDK, When `dotnet test src/Northwind.OrderDesk.sln` runs on Windows, macOS and Linux, Then the tests run and pass (ES-18).
* **EN-02/AC2** Given the existing tests (28 test assertions), When they are moved, Then all are kept and the pricing assertions are not weakened (CS-20).
* **EN-02/AC3** Given a pricing test is changed in a way that accepts a wider result than before, When it is reviewed, Then it is rejected.

### 80. wael-01 EN-09 Build an automated build and test pipeline

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-202 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 9

**Description**

**EN-09** (BACKLOG-NW-001) · **Source ids:** CS-18, CS-19

**Source:** (source: CS-18, CS-19)

**Serves:** all .NET releases

**Story:** As a .NET developer, I want every change to be built and tested automatically, so that a developer no longer publishes from Visual Studio to a file share by hand (CS-19).

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-02`. **Cross-track (OPEN):** X-11 (each track writes its own pipeline). **Relies on:** O-19.

**Register text for the ids cited in this item (backlog section 7):**

* **O-19** Which build and deployment pipeline tool? (owner: Ahmed Benali)
* **X-11** Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 9 · **Parent:** FEAT-202

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-09/AC1** Given a change to the solution, When it is submitted, Then the pipeline builds it and runs `dotnet test src/Northwind.OrderDesk.sln`.
* **EN-09/AC2** Given a failing test or build, When the pipeline runs, Then the change is blocked and the failure is reported.
* **EN-09/AC3** Given the pipeline definition, When the repository is scanned, Then it contains no secret (ES-17).

### 81. wael-01 EN-12 Provide local test data with orders and a local database recipe

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-202 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 10

**Description**

**EN-12** (BACKLOG-NW-001) · **Source ids:** ES-17, ES-27

**Source:** (source: ES-27, ES-17, A-51)

**Serves:** all local testing, MVE-02

**Story:** As a .NET developer, I want local sample data that includes orders from several customers and a recipe to build a local database from the scripts in `database/`, so that every story can be tested without Azure and without real data.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** X-01 (.NET builds locally until pilot hosting is answered). **Relies on:** A-51; MVE-A-04.

**Register text for the ids cited in this item (backlog section 7):**

* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **MVE-A-04** A local SQL Server (Developer edition or container) is available to run the database scripts. (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 10 · **Parent:** FEAT-202

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-12/AC1** Given a clean machine with a local SQL Server, When the recipe is followed, Then a local database with the sample data is created from `database/` and the solution runs against it.
* **EN-12/AC2** Given the sample data, When it is read, Then it contains orders for at least two different customers (so that isolation tests in `STORY-230` are possible) and no real customer or personal data.
* **EN-12/AC3** Given the recipe, When the repository is scanned, Then it holds no password; credentials come from user secrets or environment variables (ES-17).

### 82. wael-01 EN-10 Make time handling explicit and tested

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-203 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 11

**Description**

**EN-10** (BACKLOG-NW-001) · **Source ids:** CS-20, FR-202, FR-206, FR-211, FR-218

**Source:** (source: CS-20, A-24)

**Serves:** FR-202, FR-206, FR-211, FR-218

**Story:** As a .NET developer, I want one clock and one written rule for stored and compared times, so that the application gives the same results in local time and in the cloud's default time (UTC).

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-02`. **Cross-track (OPEN):** none. **Relies on:** A-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-24** Azure runs in UTC by default. Order Desk stores local time. Parity needs explicit handling. (From the code, not in `knowledge-docs`.) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 11 · **Parent:** FEAT-203

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-10/AC1** Given the same input, When the tests run with the host time zone set to UTC and to Central European time, Then order dates, the 24-month window and price-agreement validity give identical results.
* **EN-10/AC2** Given a price agreement that ends at midnight local time, When it is checked at the minute before and the minute after, Then it is valid before and not valid after, in both time zones.
* **EN-10/AC3** Given the rule, When it is read, Then it states whether times are stored in UTC or in local time (ASSUMPTION: A-24 describes the current behaviour and needs confirmation).

### 83. wael-01 STORY-202 Keep pricing identical to today (pricing parity)

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-203 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 12

**Description**

**STORY-202** (BACKLOG-NW-001) · **Source ids:** BR-12, CS-20, ES-18, FR-202

**Source:** (source: BR-12, CS-20, ES-18)

**Implements:** FR-202 · **Covers:** BR-12 (parity side)

**Story:** As an Order Desk staff member, I want the modernised Order Desk to give the same price as today for the same customer, product, quantity and date, so that negotiated prices and volume discounts do not change by accident.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-02`, `EN-10`. **Cross-track (OPEN):** none. **Relies on:** none.

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must · **Rank:** 12 · **Parent:** FEAT-203

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-202/AC1** Given the same customer, product, quantity and date, When the price is computed in the modernised application, Then it equals the price computed by the current application, including customer-negotiated prices and volume discounts.
* **STORY-202/AC2** Given the existing pricing checks, When `dotnet test src/Northwind.OrderDesk.sln` runs, Then all pass and no assertion is weakened.
* **STORY-202/AC3** Given any price differs, even by one cent, When the comparison is run, Then it is a defect and the release is not approved until it is fixed.

### 84. wael-01 STORY-203 Keep the order channel visible to staff (channel parity)

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-203 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 13

**Description**

**STORY-203** (BACKLOG-NW-001) · **Source ids:** BR-06, BR-10, FR-203

**Source:** (source: BR-10, BR-06; **ASSUMPTION:** A-51)

**Implements:** FR-203 · **Covers:** BR-10 (parity side)

**Story:** As an Order Desk staff member, I want to see for every order whether it was placed through the portal or entered by staff, as I do today, so that I know where an order came from.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-01`. **Cross-track (OPEN):** none. **Relies on:** A-51.

**Register text for the ids cited in this item (backlog section 7):**

* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must · **Rank:** 13 · **Parent:** FEAT-203

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-203/AC1** Given an order entered by staff, When staff open it, Then its channel is shown as entered by staff.
* **STORY-203/AC2** Given a test order with the channel value for the portal, When staff open it, Then its channel is shown as portal.
* **STORY-203/AC3** Given an order with an empty channel value, When staff open it, Then the screen behaves as the current screen does and does not fail; any difference from today is listed.

### 85. wael-01 STORY-206 Keep dates and price validity identical in any time zone (time parity)

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-203 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 14

**Description**

**STORY-206** (BACKLOG-NW-001) · **Source ids:** BR-02, BR-12, CS-20, FR-206

**Source:** (source: BR-02, BR-12, CS-20; **ASSUMPTION:** A-24)

**Implements:** FR-206

**Story:** As an Order Desk staff member, I want order dates, the 24-month history window and price-agreement validity to be the same whether the application runs in local time or in the cloud's default time, so that a move to Azure never shifts an order or a price.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-10`. **Cross-track (OPEN):** none. **Note:** supports `BR-02` and `BR-12`; those are covered in `dotnet-r2` (STORY-231, STORY-238). **Relies on:** A-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-24** Azure runs in UTC by default. Order Desk stores local time. Parity needs explicit handling. (From the code, not in `knowledge-docs`.) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must · **Rank:** 14 · **Parent:** FEAT-203

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-206/AC1** Given an order placed at 23:30 local time, When the application runs with the host time zone set to UTC and to Central European time, Then its order date is the same.
* **STORY-206/AC2** Given an order exactly 24 months old at the edge of the window, When the list is built in each time zone, Then the same orders are shown.
* **STORY-206/AC3** Given a price agreement whose last day is today, When a price is requested in each time zone, Then the same price is returned.

### 86. wael-01 STORY-204 Sign staff in with Microsoft Entra ID

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-204 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 15

**Description**

**STORY-204** (BACKLOG-NW-001) · **Source ids:** CS-04, FR-204, NFR-04

**Source:** (source: NFR-04, CS-04, G-03)

**Implements:** FR-204 · **Covers:** NFR-04 (staff side)

**Story:** As a Northwind staff member, I want to sign in to Order Desk with my Microsoft Entra ID account, so that I no longer depend on Windows Integrated Authentication against the on-premises domain.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04 (the Azure side of sign-in stays **OPEN:**; .NET uses a test identity locally). **Relies on:** A-10; O-03.

**Register text for the ids cited in this item (backlog section 7):**

* **A-10** Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. (owner: Ahmed Benali)
* **G-03** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))
* **O-03** Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 15 · **Parent:** FEAT-204

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-204/AC1** Given a staff member with a Northwind Entra ID account, When they sign in, Then they reach Order Desk with no separate password stored by the application.
* **STORY-204/AC2** Given the code base, When it is searched, Then no Windows Integrated Authentication remains.
* **STORY-204/AC3** Given an account that is not a Northwind staff account, When it tries to sign in, Then access is refused.

### 87. wael-01 EN-04 Remove Windows sign-in and server names from database configuration

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-205 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 16

**Description**

**EN-04** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, ES-25, FR-205, NFR-05

**Source:** (source: CS-13, NFR-05, ES-17, ES-25)

**Serves:** FR-205

**Story:** As a .NET developer, I want the database connection to carry no Windows-integrated sign-in and no server name in configuration, so that the same code runs locally (secrets from user secrets or environment variables) and in Azure (managed identity).

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-03`. **Cross-track (OPEN):** X-03 (database sign-in moves to Entra or a managed identity; .NET builds against a local SQL Server). **Relies on:** none.

**Register text for the ids cited in this item (backlog section 7):**

* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** enabler · **Priority:** Must (A-49: protects NFR-05) · **Rank:** 16 · **Parent:** FEAT-205

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-04/AC1** Given the repository, When it is searched, Then `Integrated Security=SSPI` and the server name `NWSQL01` appear in no configuration file (CS-13).
* **EN-04/AC2** Given a developer machine, When the application starts, Then it reads the connection setting from user secrets or an environment variable.
* **EN-04/AC3** Given the connection setting is missing, When the application starts, Then it fails with a message naming the setting and prints no value.

### 88. wael-01 STORY-205 Keep secrets out of code, tests and configuration

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r1` · **Parent:** FEAT-205 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 17

**Description**

**STORY-205** (BACKLOG-NW-001) · **Source ids:** CS-13, ES-17, FR-205, NFR-05

**Source:** (source: NFR-05, CS-13, ES-17)

**Implements:** FR-205 · **Covers:** NFR-05 (.NET side)

**Story:** As the IT manager, I want the modernised application and its tests to hold no secret in source code or in configuration files in the repository, so that a leaked repository exposes no credential.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-04`. **Cross-track (OPEN):** X-02, X-03. **Relies on:** A-54.

**Register text for the ids cited in this item (backlog section 7):**

* **A-54** The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. (owner: Ahmed Benali, Lena Varga)
* **X-02** A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) (owner: Ahmed Benali)
* **X-03** Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r1 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 17 · **Parent:** FEAT-205

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-205/AC1** Given the release content, When a scan of source and configuration files (including tests) runs as part of the release exit criteria, Then it finds no password, key or connection string with a password.
* **STORY-205/AC2** Given the application runs locally, When it needs a secret, Then it comes from user secrets or an environment variable; given it runs in Azure, Then it uses a managed identity.
* **STORY-205/AC3** Given the scan finds a secret, When the release is considered for approval, Then it is not approved until the secret is removed.

### 89. wael-01 EN-11 Build the authorisation foundation for customer scoping and channel

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-206 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 18

**Description**

**EN-11** (BACKLOG-NW-001) · **Source ids:** BR-01, BR-10, FR-210, FR-216

**Source:** (source: BR-01, BR-10; **ASSUMPTION:** A-51)

**Serves:** FR-210, FR-216

**Story:** As a .NET developer, I want server-side checks that scope every read to the signed-in customer's company, check the role when an order status is changed and set the order channel on the server, so that the portal cannot show another company's data or accept a forged channel.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04. **Relies on:** A-51.

**Register text for the ids cited in this item (backlog section 7):**

* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** MVE-02 (for the channel part, `BR-10`)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** enabler · **Priority:** Must (A-49) · **Rank:** 18 · **Parent:** FEAT-206

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-11/AC1** Given a signed-in user of company A, When a request asks for an order, an order list or an invoice of company B, Then it is refused and no data of company B is returned.
* **EN-11/AC2** Given a user who is not Order Desk staff, When they try to change an order status, Then the change is refused (the current code has no such check, A-51).
* **EN-11/AC3** Given a request that contains a channel value, When the order is created, Then the server ignores the value and sets the channel from the way the order arrived.

### 90. wael-01 STORY-230 Sign in and see only my own company's orders

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-206 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 19

**Description**

**STORY-230** (BACKLOG-NW-001) · **Source ids:** BR-01, CS-04, CS-05, FR-210

**Source:** (source: BR-01, CS-04, CS-05; **ASSUMPTION:** A-51)

**Implements:** FR-210 · **Covers:** BR-01

**Story:** As a customer user, I want to sign in and see only the orders of my own company, so that my company's orders stay private from other customers.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`, `EN-08`, `EN-12`. **Cross-track (OPEN):** X-01, X-04. **Relies on:** A-10, A-19; O-10.

**Register text for the ids cited in this item (backlog section 7):**

* **A-10** Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. (owner: Ahmed Benali)
* **A-19** In `dotnet-r2`, staff onboard customer users until `BR-08` is built. (owner: Lena Varga)
* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **O-10** Which identity provider do customer users use (OQ-01)? (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 19 · **Parent:** FEAT-206

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-230/AC1** Given a customer user of company A, When they sign in and open the order list, Then every order shown belongs to company A.
* **STORY-230/AC2** **Negative case:** Given a signed-in user of company A, When they ask for an order of company B (for example by changing the order number in the web address), Then the portal refuses the request and shows no data from company B.
* **STORY-230/AC3** Given a signed-in user of company A, When they ask for the order list, Then no row of company B appears in it.
* **STORY-230/AC4** Given sign-in fails (unknown user or wrong credentials), When the user tries to open any order page, Then no order data is shown.

### 91. wael-01 STORY-240 Authenticate customers with an externally managed identity

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-206 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 20

**Description**

**STORY-240** (BACKLOG-NW-001) · **Source ids:** CS-28, FR-220, NFR-04, OQ-01

**Source:** (source: NFR-04, OQ-01, CS-28)

**Implements:** FR-220 · **Covers:** NFR-04 (customer side)

**Story:** As the IT manager, I want customer users to authenticate with an identity managed outside the application, so that the application stores no customer password.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-08`. **Cross-track (OPEN):** X-04. **Relies on:** A-10; O-10, O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **A-10** Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. (owner: Ahmed Benali)
* **O-10** Which identity provider do customer users use (OQ-01)? (owner: Ahmed Benali)
* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **X-04** Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 20 · **Parent:** FEAT-206

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-240/AC1** Given a customer user known to the identity service, When they sign in, Then they are authenticated by the external identity and the application stores no password for them.
* **STORY-240/AC2** Given local builds and experiments, When sign-in is tested, Then a test identity is used and no real customer account is needed.
* **STORY-240/AC3** Given the identity provider is not decided (OQ-01), When the story is built, Then sign-in does not depend on one provider (A-10).
* **STORY-240/AC4** Given a user not known to the identity service, When they try to sign in, Then access is refused.

### 92. wael-01 STORY-239 Keep portal hosting, identity and mail data in the EU

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-206 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 21

**Description**

**STORY-239** (BACKLOG-NW-001) · **Source ids:** ES-20, FR-219, NFR-03

**Source:** (source: NFR-03, ES-20)

**Implements:** FR-219 · **Covers:** NFR-03 (.NET side)

**Story:** As the IT manager, I want the portal's hosting, the identity service that holds customer sign-ins and outbound mail to keep customer data and order data in the EU, so that the portal meets the residency requirement.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `STORY-240`. **Cross-track (OPEN):** X-13 (internet-facing entry while data services stay private; Azure designs the entry). **Relies on:** T-15; O-24.

**Register text for the ids cited in this item (backlog section 7):**

* **O-24** What does the customer identity service cost, and does it count toward C-04? (owner: Ahmed Benali)
* **T-15** `NFR-03` and `NFR-04` apply "wherever relevant" but BA-02 does not list `NFR-03` and BA-01 does not list `NFR-04` (split per track, A-43). (owner: Ahmed Benali)
* **X-13** An internet-facing entry for customers while data services use private endpoints (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 21 · **Parent:** FEAT-206

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-239/AC1** Given the portal design, When every service it uses (hosting, identity service, outbound mail) is listed with its region, Then each is in the EU.
* **STORY-239/AC2** Given an identity or mail service that holds data outside the EU, When the list is reviewed, Then it is not accepted and the owner of O-24 is told.
* **STORY-239/AC3** Given the cost of the identity service counts toward C-04 or not is unknown (O-24), When the list is read, Then that question is marked **OPEN:**.

### 93. wael-01 STORY-231 See my company's orders from the last 24 months

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-207 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 22

**Description**

**STORY-231** (BACKLOG-NW-001) · **Source ids:** BR-02, FR-211

**Source:** (source: BR-02, P-03)

**Implements:** FR-211 · **Covers:** BR-02

**Story:** As a customer user, I want to see the list of my company's orders from the last 24 months with order date, status and total, so that I can find an order without phoning the Order Desk.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-10`, `EN-11`. **Cross-track (OPEN):** none. **Relies on:** A-16; O-08.

**Register text for the ids cited in this item (backlog section 7):**

* **A-16** 24 months is a display window over the complete history held in the database. (owner: Ahmed Benali)
* **O-08** Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 22 · **Parent:** FEAT-207

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-231/AC1** Given company A has orders, When a user of company A opens the list, Then each order from the last 24 months is shown with its order date, status and total.
* **STORY-231/AC2** Given an order older than 24 months, When the list is shown, Then it is not listed (24 months is a display window over the complete history, A-16).
* **STORY-231/AC3** Given company A has no orders in the last 24 months, When the list is opened, Then an empty-list message is shown and no error.

### 94. wael-01 STORY-232 Open an order and see lines, prices, address and status

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-207 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 23

**Description**

**STORY-232** (BACKLOG-NW-001) · **Source ids:** BR-03, FR-212

**Source:** (source: BR-03, P-03)

**Implements:** FR-212 · **Covers:** BR-03

**Story:** As a customer user, I want to open an order and see its lines, quantities, prices, delivery address and current status, so that I can check what was ordered and where it goes.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`. **Cross-track (OPEN):** none. **Relies on:** none.

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 23 · **Parent:** FEAT-207

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-232/AC1** Given an order of the user's company, When the user opens it, Then it shows each line with product, quantity and price, the delivery address and the current status.
* **STORY-232/AC2** Given the prices shown, When they are compared with `STORY-238`, Then they are the customer's negotiated prices.
* **STORY-232/AC3** Given an order that belongs to another company, When the user opens its address, Then the request is refused (see `STORY-230/AC2`).

### 95. wael-01 STORY-233 See one of six order statuses with an as-of time

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-207 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 24

**Description**

**STORY-233** (BACKLOG-NW-001) · **Source ids:** BR-04, C-03, CS-10, FR-213

**Source:** (source: BR-04, P-03, CS-10, C-03)

**Implements:** FR-213 · **Covers:** BR-04

**Story:** As a customer user, I want to see the status of an order as one of Received, Confirmed, Picking, Shipped, Delivered or Cancelled, with the time it was last updated, so that I know how current the status is before I decide to phone.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none inside the track. **Cross-track (OPEN):** X-05, X-06 (freshness is bounded by the exchange cadence; .NET shows the "as of" time). **Relies on:** A-03; O-04, O-16; T-01.

**Register text for the ids cited in this item (backlog section 7):**

* **A-03** `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. (owner: Lena Varga)
* **O-04** What status freshness is acceptable, given the nightly batch? (owner: Lena Varga)
* **O-16** How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? (owner: Ahmed Benali, Pieter Janssens)
* **T-01** `BR-04` says "always up to date" but Picking and Shipped change once a night (handled by A-03). (owner: Lena Varga)
* **X-05** StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) (owner: Ahmed Benali)
* **X-06** Status freshness is bounded by the exchange cadence (.NET needs Azure and StockPilot) (owner: Lena Varga)

**Gate:** **MVE-02** (`R2`: at least 60 % would use the status instead of phoning)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 24 · **Parent:** FEAT-207

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-233/AC1** Given any order, When the user opens it, Then its status is exactly one of Received, Confirmed, Picking, Shipped, Delivered, Cancelled.
* **STORY-233/AC2** Given the status is Picking or Shipped, When it is shown, Then it carries an "as of" date and time equal to the time of the last nightly StockPilot update (A-03).
* **STORY-233/AC3** Given the status is Received, Confirmed or Cancelled, When it is shown, Then it is current as of Order Desk and carries the time of the last change.
* **STORY-233/AC4** Given an order is shipped in the warehouse after the 02:00 batch, When the customer views it before the next night's run, Then the portal still shows the previous status with its "as of" time and does not claim to be live (T-01).
* **STORY-233/AC5** Given staff set an order to Delivered in Order Desk, When the customer opens it, Then the portal shows Delivered.

### 96. wael-01 STORY-234 Create a new order by copying a previous order

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-208 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 25

**Description**

**STORY-234** (BACKLOG-NW-001) · **Source ids:** BR-05, FR-214

**Source:** (source: BR-05, P-04)

**Implements:** FR-214 · **Covers:** BR-05

**Story:** As a customer user, I want to create a new order by copying a previous order, changing quantities or removing lines and then submitting it, so that I do not have to dictate or retype the whole list.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-06`, `EN-11`. **Cross-track (OPEN):** X-07. **Relies on:** O-28 (**OPEN:** the rule for a copied line whose product is no longer available is not in the sources).

**Register text for the ids cited in this item (backlog section 7):**

* **O-28** What happens to a line of a copied order whose product is no longer available (`STORY-234`)? Not stated in the sources. (owner: Lena Varga)
* **X-07** The in-process session draft must be stateless before scale-out (Azure needs .NET) (owner: Ahmed Benali)

**Gate:** **MVE-02** (`R1`: at least 80 % finish a reorder unaided)

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 25 · **Parent:** FEAT-208

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-234/AC1** Given a previous order of my company, When I choose to copy it, Then a new draft is created with the same lines and quantities.
* **STORY-234/AC2** Given a draft, When I change a quantity or remove a line and submit, Then the submitted order has exactly my changes.
* **STORY-234/AC3** Given I am preparing a draft, When the server restarts or my next request is handled by another instance, Then my draft is not lost (`EN-06`).
* **STORY-234/AC4** Given a draft with no lines, When I try to submit, Then the submission is refused with a message and no order is created.

### 97. wael-01 STORY-235 Have a submitted portal order appear in Order Desk as Received

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-208 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 26

**Description**

**STORY-235** (BACKLOG-NW-001) · **Source ids:** BR-06, C-05, FR-215

**Source:** (source: BR-06, C-05, P-01, P-02)

**Implements:** FR-215 · **Covers:** BR-06

**Story:** As an Order Desk staff member, I want a submitted portal order to appear in Order Desk with the status Received without being re-keyed, so that I stop retyping orders and the correction rate falls.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `STORY-234`. **Cross-track (OPEN):** X-01 (the pilot reads the database named in O-23). **Relies on:** A-37; O-23; T-08.

**Register text for the ids cited in this item (backlog section 7):**

* **A-37** The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. (owner: Ahmed Benali)
* **O-23** Which database does the Q2 2027 portal pilot read (T-08)? (owner: Ahmed Benali)
* **T-08** The Q2 2027 portal pilot and C-05 versus the database migration (A-37, O-23). (owner: Ahmed Benali)
* **X-01** Hosting target and pilot test environment for the modernised application (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 26 · **Parent:** FEAT-208

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-235/AC1** Given a customer submits an order in the portal, When staff open Order Desk, Then the order is there with the status Received and nobody has re-keyed it.
* **STORY-235/AC2** Given the portal, When its data access is reviewed, Then it reads and writes orders only through Order Desk and no second order database exists (C-05).
* **STORY-235/AC3** Given Order Desk cannot take the order at the time of submission, When the customer submits, Then the customer is told the order was not submitted and no partial order exists.

### 98. wael-01 STORY-236 Show staff whether an order came from the portal or from staff

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-208 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 27

**Description**

**STORY-236** (BACKLOG-NW-001) · **Source ids:** BR-06, BR-10, FR-216

**Source:** (source: BR-10, BR-06; **ASSUMPTION:** A-51)

**Implements:** FR-216 · **Covers:** BR-10 (portal value)

**Story:** As an Order Desk staff member, I want to see whether an order was placed through the portal or entered by staff, so that I can handle portal orders knowing where they came from.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`. **Cross-track (OPEN):** none. **Relies on:** A-51.

**Register text for the ids cited in this item (backlog section 7):**

* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)

**Gate:** **MVE-02**

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 27 · **Parent:** FEAT-208

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-236/AC1** Given a customer submits an order in the portal, When staff open it, Then its channel is portal.
* **STORY-236/AC2** Given an order entered by staff, When staff open it, Then its channel is staff.
* **STORY-236/AC3** Given a request from a customer that carries any channel value, When the order is created, Then the server sets the channel to portal and the customer cannot choose it (`EN-11/AC3`).

### 99. wael-01 STORY-238 Show my negotiated prices, not list prices

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-209 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 28

**Description**

**STORY-238** (BACKLOG-NW-001) · **Source ids:** BR-12, CS-20, FR-218

**Source:** (source: BR-12, CS-20)

**Implements:** FR-218 · **Covers:** BR-12 (customer prices)

**Story:** As a customer user, I want to see my own negotiated prices and not the list price, so that what I see is what I will be invoiced.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-10`, `STORY-202`. **Cross-track (OPEN):** none. **Relies on:** none.

**Gate:** **MVE-02**

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must · **Rank:** 28 · **Parent:** FEAT-209

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-238/AC1** Given a customer with a negotiated price for a product, When they view an order, a draft or the order list total, Then the negotiated price is shown and not the list price.
* **STORY-238/AC2** Given a price for the same customer, product, quantity and date, When it is compared with the staff screens, Then it is identical (`STORY-202`).
* **STORY-238/AC3** Given the pricing rules cannot return a price for a line, When the portal shows the line, Then it shows an error for that line and never falls back to the list price.

### 100. wael-01 STORY-237 Use the portal in French and English

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-209 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 29

**Description**

**STORY-237** (BACKLOG-NW-001) · **Source ids:** BR-11, FR-217, OQ-02

**Source:** (source: BR-11, OQ-02)

**Implements:** FR-217 · **Covers:** BR-11 (French and English)

**Story:** As a customer user, I want the portal in French or English, so that I can use it in my working language.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** none. **Relies on:** A-11; O-11, O-18.

**Register text for the ids cited in this item (backlog section 7):**

* **A-11** Portal release 1 covers French and English. Dutch follows. (owner: Sofie Peeters, Lena Varga)
* **O-11** Must Dutch be in the first release (OQ-02)? (owner: Sofie Peeters, Lena Varga)
* **O-18** Where do the customer e-mail address and language preference live? (owner: Lena Varga)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Should · **Rank:** 29 · **Parent:** FEAT-209

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-237/AC1** Given any pilot screen, When the user selects French or English, Then all text of the screen appears in the selected language.
* **STORY-237/AC2** Given a pilot screen has a text without a translation, When the screens are reviewed, Then it is listed and fixed before the release is approved.
* **STORY-237/AC3** Given a user whose preference is Dutch, When they open the portal, Then Dutch is not offered in `dotnet-r2` (see `STORY-263`) and French or English remains available.

### 101. wael-01 STORY-241 Record who, what, when and channel for every order change

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-210 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 30

**Description**

**STORY-241** (BACKLOG-NW-001) · **Source ids:** ES-19, FR-221, NFR-08

**Source:** (source: NFR-08, ES-19; **ASSUMPTION:** A-51)

**Implements:** FR-221 · **Covers:** NFR-08 (content)

**Story:** As the product owner, I want every change to an order, by a customer or by staff, to record who, what, when and channel, so that the 7-year audit record is complete.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-15 (Azure sets the 7-year retention). **Relies on:** A-31, A-51; T-13.

**Register text for the ids cited in this item (backlog section 7):**

* **A-31** Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). (owner: Ahmed Benali)
* **A-51** Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. (owner: Ahmed Benali)
* **T-13** `NFR-08` asks for who, what, when and channel but today's audit rows may not record all (listed, not fixed silently). (owner: Ahmed Benali)
* **X-15** Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 30 · **Parent:** FEAT-210

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-241/AC1** Given a change to an order by a customer or by staff, When the audit record is read, Then it shows who, what, when and channel.
* **STORY-241/AC2** Given a sample of order changes, When the audit records are checked, Then each of the four fields is present.
* **STORY-241/AC3** Given today's record is incomplete (the channel is recorded only on creation and the shipment import writes audit rows for unchanged orders, A-51), When the gap is found, Then it is listed for the product owner to decide and is not changed silently (ES-19).

### 102. wael-01 STORY-242 Check every pilot screen against WCAG 2.2 level AA

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-210 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 31

**Description**

**STORY-242** (BACKLOG-NW-001) · **Source ids:** FR-222, NFR-07

**Source:** (source: NFR-07)

**Implements:** FR-222 · **Covers:** NFR-07

**Story:** As a customer user who relies on a keyboard or a screen reader, I want every pilot screen to meet WCAG 2.2 level AA, so that I can use the portal.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** none. **Relies on:** A-54.

**Register text for the ids cited in this item (backlog section 7):**

* **A-54** The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. (owner: Ahmed Benali, Lena Varga)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 31 · **Parent:** FEAT-210

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-242/AC1** Given every pilot screen, When automated checks and a manual keyboard and screen-reader review run against the WCAG 2.2 AA success criteria, Then the findings are recorded per screen (A-54).
* **STORY-242/AC2** Given a failure is found, When the release is considered for approval, Then it is fixed or listed with the reason it stays.
* **STORY-242/AC3** Given the review is done, When the result is reported, Then it does not claim conformance, because a conformance statement needs a qualified accessibility reviewer.

### 103. wael-01 STORY-243 Respond in under 2 seconds at the 95th percentile

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r2` · **Parent:** FEAT-210 · **Priority:** Must (proposed ADO priority 1) · **Rank:** 32

**Description**

**STORY-243** (BACKLOG-NW-001) · **Source ids:** CS-03, CS-05, FR-223, NFR-02

**Source:** (source: NFR-02, CS-03, CS-05)

**Implements:** FR-223 · **Covers:** NFR-02

**Story:** As a customer user, I want the order list and order detail pages to respond quickly, so that checking an order is faster than phoning.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-10`. **Cross-track (OPEN):** X-12 (Azure sizes from today's load). **Relies on:** A-05, A-17; O-08.

**Register text for the ids cited in this item (backlog section 7):**

* **A-05** `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. (owner: Ahmed Benali)
* **A-17** Pilot customer concurrency is small (20 customers). No customer load figure exists. (owner: Ahmed Benali)
* **O-08** Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. (owner: Ahmed Benali)
* **X-12** The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r2 · **Type:** story · **Priority:** Must (A-06) · **Rank:** 32 · **Parent:** FEAT-210

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-243/AC1** Given the order list and order detail pages, When response time is measured **on the server** at the 95th percentile, Then it is under 2 seconds for 95 % of requests (A-05).
* **STORY-243/AC2** Given the load model, When the measurement runs, Then it uses about 60 concurrent staff users at peak (CS-03) plus the agreed pilot customer figure (**OPEN:** O-08, A-17) and today's data volume (about 14,000 order lines a week, CS-05).
* **STORY-243/AC3** Given the 95th percentile is 2 seconds or more, When the result is reported, Then `NFR-02` is recorded as not met and the cause is listed; the release is not approved on this criterion.

### 104. wael-01 EN-07 Abstract the invoice store

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-211 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 33

**Description**

**EN-07** (BACKLOG-NW-001) · **Source ids:** CS-11, CS-14, FR-230

**Source:** (source: CS-14, CS-11, A-15)

**Serves:** FR-230

**Story:** As a .NET developer, I want invoice access behind an interface with a local-folder provider, so that the code no longer depends on a network path and a storage provider can be added later.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** X-09 (Azure designs storage and synchronisation). **Relies on:** A-15; O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **A-15** The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. (owner: Julien Moreau)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** enabler · **Priority:** Should (A-49) · **Rank:** 33 · **Parent:** FEAT-211

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-07/AC1** Given the interface, When the application runs with the local-folder provider on a developer machine, Then an invoice is read without a UNC path (CS-14).
* **EN-07/AC2** Given an invoice number and year, When the path is built, Then it follows `{year}\{invoiceNumber}.pdf` and the rule for which year is used is written down (A-15).
* **EN-07/AC3** Given the file does not exist, When it is requested, Then the interface returns a "not found" result and no exception reaches the user.

### 105. wael-01 STORY-260 Download the PDF invoice of a delivered order

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-211 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 34

**Description**

**STORY-260** (BACKLOG-NW-001) · **Source ids:** BR-07, CS-08, CS-11, FR-230

**Source:** (source: BR-07, P-05, CS-08, CS-11)

**Implements:** FR-230 · **Covers:** BR-07

**Story:** As a customer user, I want to download the PDF invoice of a delivered order, so that I do not have to ask the Order Desk to e-mail me a copy.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-07`, `EN-11`. **Cross-track (OPEN):** X-09. **Relies on:** A-15; O-08, O-15.

**Register text for the ids cited in this item (backlog section 7):**

* **A-15** The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. (owner: Julien Moreau)
* **O-08** Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. (owner: Ahmed Benali)
* **O-15** Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? (owner: Ahmed Benali, Julien Moreau)
* **X-09** Invoice files move from a network path to Azure storage (Both) (owner: Julien Moreau, Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Should · **Rank:** 34 · **Parent:** FEAT-211

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-260/AC1** Given an order with the status Delivered and an invoice, When I open it, Then a download of the PDF invoice is offered and delivers the file.
* **STORY-260/AC2** Given an order that is not Delivered, When I open it, Then no invoice download is offered.
* **STORY-260/AC3** Given an invoice of another company's order, When I request it, Then the request is refused (`EN-11/AC1`).
* **STORY-260/AC4** Given the PDF cannot be found, When I request it, Then a message says the invoice is not available yet and the miss is logged.

### 106. wael-01 STORY-261 Invite and remove users of my own company

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-212 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 35

**Description**

**STORY-261** (BACKLOG-NW-001) · **Source ids:** BR-08, FR-231, OQ-03

**Source:** (source: BR-08, OQ-03)

**Implements:** FR-231 · **Covers:** BR-08

**Story:** As a customer administrator, I want to invite and remove users of my own company, so that I manage my colleagues' access without asking Northwind staff.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-10 if the invitation is sent by e-mail (mail abstraction and a local mail catcher meanwhile). **Relies on:** A-12, A-19; O-12 (**OPEN:** who receives the administrator role).

**Register text for the ids cited in this item (backlog section 7):**

* **A-12** A customer administrator role exists. Who gets it is **OPEN:**. (owner: Lena Varga)
* **A-19** In `dotnet-r2`, staff onboard customer users until `BR-08` is built. (owner: Lena Varga)
* **O-12** Do customer administrators exist for every customer or only for large ones (OQ-03)? (owner: Lena Varga)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Should · **Rank:** 35 · **Parent:** FEAT-212

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-261/AC1** Given I am a customer administrator, When I invite a colleague of my company, Then the colleague can sign in and sees only my company's orders.
* **STORY-261/AC2** Given I am a customer administrator, When I remove a user of my company, Then that user can no longer sign in.
* **STORY-261/AC3** Given I am a customer administrator, When I try to invite or remove a user of another company, Then the request is refused.
* **STORY-261/AC4** Given I am not a customer administrator, When I open the portal, Then no user-administration screen is offered.

### 107. wael-01 STORY-262 Receive an e-mail when an order changes to Shipped

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-212 · **Priority:** Could (proposed ADO priority 3) · **Rank:** 36

**Description**

**STORY-262** (BACKLOG-NW-001) · **Source ids:** BR-09, CS-10, CS-12, FR-232

**Source:** (source: BR-09, P-03, CS-10, CS-12)

**Implements:** FR-232 · **Covers:** BR-09

**Story:** As a customer user, I want an e-mail when one of my orders changes to Shipped, so that I know without opening the portal.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-11`. **Cross-track (OPEN):** X-10 (the Azure mail design `EA-12` is a different track's work and is never waited for) (mail abstraction and a local mail catcher meanwhile), X-06. **Relies on:** A-03, A-29; O-17, O-18.

**Register text for the ids cited in this item (backlog section 7):**

* **A-03** `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. (owner: Lena Varga)
* **A-29** The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. (owner: Ahmed Benali)
* **O-17** What sends order confirmations today? (owner: Ahmed Benali)
* **O-18** Where do the customer e-mail address and language preference live? (owner: Lena Varga)
* **X-06** Status freshness is bounded by the exchange cadence (.NET needs Azure and StockPilot) (owner: Lena Varga)
* **X-10** Outbound mail replaces the on-premises relay (Both) (owner: Ahmed Benali)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Could · **Rank:** 36 · **Parent:** FEAT-212

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-262/AC1** Given an order changes to Shipped in Order Desk, When Order Desk learns of the change, Then the customer user receives an e-mail.
* **STORY-262/AC2** Given the Shipped status is set by the nightly StockPilot update, When the e-mail is sent, Then it arrives after that run and states the "as of" time; it is not promised at the moment of physical shipment (A-03).
* **STORY-262/AC3** Given the mail service fails, When the order changes to Shipped, Then the order status is unaffected and the failure is logged.
* **STORY-262/AC4** Given no customer e-mail address is known for the user, When the order changes to Shipped, Then no e-mail is sent and the gap is logged (O-18).

### 108. wael-01 STORY-263 Use the portal in Dutch

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-213 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 37

**Description**

**STORY-263** (BACKLOG-NW-001) · **Source ids:** BR-11, FR-233, OQ-02

**Source:** (source: BR-11, OQ-02)

**Implements:** FR-233 · **Covers:** BR-11 (Dutch)

**Story:** As a Belgian customer user, I want the portal in Dutch, so that I can use it in my working language.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `STORY-237`. **Cross-track (OPEN):** none. **Relies on:** A-11; O-11, O-18.

**Register text for the ids cited in this item (backlog section 7):**

* **A-11** Portal release 1 covers French and English. Dutch follows. (owner: Sofie Peeters, Lena Varga)
* **O-11** Must Dutch be in the first release (OQ-02)? (owner: Sofie Peeters, Lena Varga)
* **O-18** Where do the customer e-mail address and language preference live? (owner: Lena Varga)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Should · **Rank:** 37 · **Parent:** FEAT-213

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-263/AC1** Given any portal screen, When I select Dutch, Then all text of the screen appears in Dutch.
* **STORY-263/AC2** Given Dutch is added, When I select French or English, Then those languages are unchanged.
* **STORY-263/AC3** Given a screen has text without a Dutch translation, When the screens are reviewed, Then it is listed and fixed before the release is approved.

### 109. wael-01 STORY-264 Record data to compare SM-01 to SM-04 with their baselines

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-213 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 38

**Description**

**STORY-264** (BACKLOG-NW-001) · **Source ids:** FR-234, SM-01, SM-02, SM-03, SM-04

**Source:** (source: SM-01, SM-02, SM-03, SM-04; **ASSUMPTION:** A-52)

**Implements:** FR-234

**Story:** As the head of Customer Operations, I want the portal to record or expose the data that I need to compare the portal success measures with their baselines, so that I can tell after general availability whether they are met.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none inside the track. **Cross-track (OPEN):** none. **Relies on:** A-04, A-52; O-05, O-26.

**Register text for the ids cited in this item (backlog section 7):**

* **A-04** "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot. (owner: Lena Varga)
* **A-52** `FR-234` (instrumentation for SM-01 to SM-04) is Should, because the business case gives the measures no priority and names no measurement source. (owner: Lena Varga)
* **O-05** Does "portal launch" mean the pilot or general availability? (owner: Lena Varga)
* **O-26** Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. (owner: Lena Varga)

**Gate:** **MVE-02** (instrumentation)

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Should (A-52) · **Rank:** 38 · **Parent:** FEAT-213

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-264/AC1** Given the data agreed under O-26 for `SM-01`, `SM-03` and `SM-04`, When a reporting period is chosen, Then the portal records or exposes those data for the period.
* **STORY-264/AC2** Given `SM-02` counts calls handled by staff, When the data are described, Then the story states that those calls are counted outside the product.
* **STORY-264/AC3** Given O-26 has not named which data and from which source, When the story is considered, Then it is not started and stays Draft.

### 110. wael-01 EN-14 Publish the read-only Order Desk API contract (OpenAPI 2.0)

* **Type:** User Story (backlog type: enabler) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-214 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 39

**Description**

**EN-14** (BACKLOG-NW-001) · **Source ids:** CS-27, ES-36, FR-235, FR-240

**Source:** (source: CS-27, ES-36, G-01)

**Serves:** FR-235, FR-240

**Story:** As a .NET developer, I want a read-only contract for orders and order lines written as an OpenAPI 2.0 document, so that another track can design against it before any implementation exists.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** none. **Cross-track (OPEN):** X-20, X-21 outbound (BA-03 designs against a stub meanwhile). **Relies on:** A-18; O-01.

**Register text for the ids cited in this item (backlog section 7):**

* **A-18** The warehouse for each claim line can be derived from StockPilot or product data. It is not on order lines. (owner: Pieter Janssens)
* **G-01** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))
* **O-01** Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? (owner: Ahmed Benali)
* **X-20** An Order Desk API (read orders and lines) for the custom connector (Power Platform needs .NET) (owner: Ahmed Benali)
* **X-21** An order data contract for claims: order number, lines, quantities, prices, customer, warehouse (Power Platform needs .NET) (owner: Lena Varga, Pieter Janssens)
* **X-23** Connector sign-in (Entra app registration, OAuth) (Power Platform needs Azure or IT) (owner: Ahmed Benali)
* **X-25** Warehouse for each order line, for `BR-17` (Power Platform needs .NET and StockPilot data) (owner: Pieter Janssens)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** enabler · **Priority:** Should (A-49: serves another track) · **Rank:** 39 · **Parent:** FEAT-214

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **EN-14/AC1** Given the contract file, When it is validated locally, Then it is a valid OpenAPI 2.0 document (ES-36).
* **EN-14/AC2** Given the contract, When its operations are listed, Then every operation only reads and none creates, changes or deletes an order.
* **EN-14/AC3** Given the fields X-21 asks for (order number, lines, quantities, prices, customer, warehouse), When the contract is read, Then each is present; the warehouse field is marked as not available while its source is unknown (A-18, X-25), and no value is invented.
* **EN-14/AC4** Given the contract, When it is read, Then it contains no implementation and carries a placeholder security definition (X-23).

### 111. wael-01 STORY-265 Let another track build against the published order contract

* **Type:** User Story (backlog type: story) · **Tags:** `nw-workshop; track-dotnet; dotnet-r3` · **Parent:** FEAT-214 · **Priority:** Should (proposed ADO priority 2) · **Rank:** 40

**Description**

**STORY-265** (BACKLOG-NW-001) · **Source ids:** CS-27, ES-36, FR-235

**Source:** (source: CS-27, ES-36, G-01)

**Implements:** FR-235

**Story:** As a developer on another delivery track (for example the Power Platform track), I want a published read-only contract for orders and order lines, so that I can build a connector against it without access to the Order Desk database.

**ASSUMPTION / OPEN markers (as written in the backlog):**

* **Dependencies:** `EN-14`. **Cross-track (OPEN):** X-20, X-21. **Relies on:** O-01.

**Register text for the ids cited in this item (backlog section 7):**

* **G-01** Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. (owner: Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10))
* **O-01** Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? (owner: Ahmed Benali)
* **X-20** An Order Desk API (read orders and lines) for the custom connector (Power Platform needs .NET) (owner: Ahmed Benali)
* **X-21** An order data contract for claims: order number, lines, quantities, prices, customer, warehouse (Power Platform needs .NET) (owner: Lena Varga, Pieter Janssens)

**Gate:** none

**Track tag:** track-dotnet · **Release tag:** dotnet-r3 · **Type:** story · **Priority:** Should · **Rank:** 40 · **Parent:** FEAT-214

**Acceptance criteria** (field `Microsoft.VSTS.Common.AcceptanceCriteria`)

* **STORY-265/AC1** Given the contract is published in the repository, When another track reads it, Then it describes how to read one order and its lines by order number and follows OpenAPI 2.0.
* **STORY-265/AC2** Given the contract, When it is reviewed, Then it excludes any operation that writes data and excludes the implementation.
* **STORY-265/AC3** Given the owner of the implementation is unknown (O-01), When the release file is written, Then it states that the contract is published and the implementation is `EPIC-204`, unplanned.

## E. Documentation links and why

All URLs start with `https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/`. They point at `main`. The six release tags point at the same commit, and the files have not changed since.

| Item level | Linked documents | Why |
|---|---|---|
| Epic | BRD, PRD, REL, BKL, and EXP when gated | The epic is the outcome, so it links the business case behind it (BRD), the product requirement (PRD) and the release that plans it. |
| Feature | PRD, REL, BKL, and EXP when gated | A feature groups stories that implement product requirements. |
| Story and enabler | PRD, TRC, REL, BKL, and EXP when gated; BRD when the source line cites a `BR-` or `NFR-` | The story implements an `FR-` (PRD), is proven covered in the traceability table (ES-06), and sits in a release. Enablers that cite only `CS-`, `ES-` or `C-` get no BRD link. |
| Gated item (`Gate: MVE-nn`) | EXP | The experiment decision comes before the item is committed. No result exists yet. |
| BKL | `backlog.md#<item heading>` | The anchor is built from the heading, so the link opens the item itself. |

### Link counts by document

| Document | Items linked | Link operations |
|---|---|---|
| business-requirements.md (BRD) | 55 | 55 |
| product-requirements.md (PRD) | 111 | 111 |
| experiments.md (EXP) | 35 | 35 |
| traceability.md (TRC) | 76 | 76 |
| backlog.md (with anchor) (BKL) | 111 | 111 |
| releases/<release>.md (REL) | 111 | 111 |
| **Total** | | **499** |

### Items that link `experiments.md` (35)

`EPIC-101`, `EPIC-102`, `EPIC-103`, `EPIC-104`, `EPIC-201`, `EPIC-202`, `EPIC-203`, `FEAT-104`, `FEAT-105`, `FEAT-113`, `FEAT-106`, `FEAT-109`, `FEAT-114`, `FEAT-207`, `FEAT-208`, `FEAT-209`, `FEAT-213`, `EA-05`, `STORY-120`, `EA-09`, `STORY-121`, `STORY-122`, `EA-15`, `EA-06`, `STORY-140`, `EA-08`, `STORY-145`, `STORY-146`, `EA-16`, `EN-11`, `STORY-233`, `STORY-234`, `STORY-236`, `STORY-238`, `STORY-264`

Gates on the planned items are all `MVE-01` (Azure) and `MVE-02` (.NET). `MVE-03` gates only unplanned Power Platform items.

### Items without a BRD link

56 items: features (all 28) and stories or enablers with no `BR-` or `NFR-` in their source line: `EA-11`, `STORY-101`, `STORY-105`, `EA-02`, `STORY-102`, `EA-05`, `EA-09`, `STORY-121`, `EA-06`, `EA-07`, `STORY-141`, `EA-10`, `STORY-143`, `STORY-174`, `EN-01`, `EN-13`, `EN-03`, `EN-05`, `EN-06`, `STORY-201`, `EN-02`, `EN-09`, `EN-12`, `EN-10`, `EN-07`, `STORY-264`, `EN-14`, `STORY-265`

### Full link list per item (URL and comment)

| localId | URL | Comment |
|---|---|---|
| `EPIC-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EPIC-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EPIC-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-101-azure-foundation-and-security-baseline | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EPIC-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EPIC-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-102-data-platform-decision-cost-and-migration-approach | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EPIC-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EPIC-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-103-pilot-environment-exchange-storage-and-observability | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `EPIC-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EPIC-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-104-cutover-and-recovery-proof | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EPIC-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `EPIC-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-201-modernise-order-desk-to-net-10-with-parity | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `EPIC-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `EPIC-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-202-customer-portal-pilot-sign-in-orders-status-reorder | Backlog (BACKLOG-NW-001): this item with its full text |
| `EPIC-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business requirements, goals and constraints behind this epic |
| `EPIC-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements, journeys and release placement |
| `EPIC-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `EPIC-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `EPIC-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#epic-203-complete-the-portal-and-publish-the-order-desk-api-contract | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-101-environment-foundation-as-code-and-validation | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-102-hybrid-connectivity-design | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-103-secrets-identity-and-private-access | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-104-data-tier-decision | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-105-cost-model-and-migration-approach | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-113` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-113` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-113` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-113` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-113-application-hosting | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-106` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-106` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-106` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-106` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-106-stockpilot-exchange-invoice-storage-and-outbound-mail | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-107` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-107` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-107` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-107-observability-and-alerting | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-108` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-108` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-108` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-108-test-environment-for-the-portal-pilot | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-109` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-109` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-109` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-109` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-109-backup-retention-and-recovery-design | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-114` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-114` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-114` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `FEAT-114` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-114-database-migration-and-rehearsal | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-110` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-110` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-110` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-110-cutover-and-rollback-runbooks | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-111` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-111` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-111` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-111-recovery-and-availability-proof | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-112` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-112` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-112` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-112-decommission-of-the-old-servers | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-201-modernise-projects-and-web-layer | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-202-test-build-and-local-data | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-203-pricing-channel-and-time-parity | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-204-staff-sign-in-with-entra-id | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `FEAT-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-205-secret-free-configuration | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-206-customer-sign-in-company-isolation-and-data-residency | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-207` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-207` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-207` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `FEAT-207` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-207-order-list-order-detail-and-status | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-208` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-208` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-208` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `FEAT-208` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-208-reorder-submit-and-channel | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-209` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-209` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-209` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `FEAT-209` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-209-customer-prices-and-language | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-210` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-210` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `FEAT-210` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-210-audit-accessibility-and-performance | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-211` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-211` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-211` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-211-invoice-download | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-212` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-212` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-212` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-212-customer-user-administration-and-shipping-e-mail | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-213` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-213` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-213` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `FEAT-213` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-213-dutch-and-success-measure-data | Backlog (BACKLOG-NW-001): this item with its full text |
| `FEAT-214` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product requirements covered by this feature |
| `FEAT-214` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `FEAT-214` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#feat-214-order-desk-api-contract | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-101, FR-104 |
| `EA-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-03) |
| `EA-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-01-build-the-azure-foundation-as-code-naming-tags-region-modules | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-105 |
| `EA-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-11-build-the-infrastructure-validation-and-deployment-pipeline-design | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-101 |
| `STORY-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-101` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-101-review-a-test-and-production-environment-design-set | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-104 |
| `STORY-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-03) |
| `STORY-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-104` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-104-keep-every-azure-resource-in-an-eu-region | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-105 |
| `STORY-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-105` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-105-validate-every-infrastructure-definition-locally-before-release | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-102 |
| `EA-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-02-design-hybrid-connectivity-between-lyon-azure-and-antwerp | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-102 |
| `STORY-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-102` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-102-agree-the-connection-design-for-the-move-and-after-the-lease | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-103 |
| `EA-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-05) |
| `EA-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-03-design-secrets-managed-identities-and-private-endpoints | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-103 |
| `STORY-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-05) |
| `STORY-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-103` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-103-keep-secrets-out-of-azure-hosted-code-and-configuration | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-106, FR-108 |
| `EA-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-05-record-the-data-tier-decision-and-migration-approach | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-106 |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-120` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-120-decide-the-data-tier-for-the-order-database | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-107 |
| `EA-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `EA-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-09-build-the-azure-cost-model-against-the-monthly-cap | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-121` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-107 |
| `STORY-121` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-121` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-121` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-121` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-121-show-the-monthly-cost-against-the-eur-1500-cap | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-108 |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r1.md | Release file azure-r1: scope, exit criteria and OPEN dependencies |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-122` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-122-define-the-database-and-invoice-migration-approach | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-112, FR-116 · **Added after the first review (A-59)** |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13, NFR-01) |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-15` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-15-host-the-order-desk-web-application-in-the-test-and-production-environments | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-109 |
| `EA-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-06-redesign-the-stockpilot-exchange-without-changing-the-file-contract | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-110 |
| `EA-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-07-design-invoice-storage-and-synchronisation | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-113 |
| `EA-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-09) |
| `EA-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-12-design-outbound-mail-to-replace-the-on-premises-relay | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-109 |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-140` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-140-keep-the-nightly-stockpilot-exchange-working-after-the-database-moves | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-141` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-110 |
| `STORY-141` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-141` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-141` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-141-decide-where-invoice-files-live-after-the-lease | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-144` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-113 |
| `STORY-144` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-09) |
| `STORY-144` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-144` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-144` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-144-replace-the-on-premises-mail-relay-for-outbound-e-mail | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-111, FR-119 |
| `EA-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-01) |
| `EA-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-04-build-observability-log-workspace-application-monitoring-and-alerts | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-142` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-111 |
| `STORY-142` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-01) |
| `STORY-142` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-142` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-142` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-142-monitor-availability-with-a-synthetic-probe-and-alerts | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-112 |
| `EA-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-10-define-the-tst-environment | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-143` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-112 |
| `STORY-143` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-143` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-143` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-143-define-a-test-environment-where-the-portal-pilot-can-run | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-114, FR-115 |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-06, NFR-08) |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-08-design-backup-long-term-retention-and-recovery | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-114 |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-08) |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-145` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-145-keep-order-change-records-for-7-years-in-azure | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-115 |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-06) |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r2.md | Release file azure-r2: scope, exit criteria and OPEN dependencies |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `STORY-146` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-146-design-backup-and-recovery-for-rpo-1-hour-and-rto-4-hours | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-106, FR-116 · **Added after the first review (A-59)** |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13, NFR-03, NFR-06) |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-01: decision before this item is committed; no result yet |
| `EA-16` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-16-migrate-the-northwindorders-database-to-the-chosen-data-tier-and-rehearse-the-move | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-116, FR-117, FR-119, FR-120 |
| `EA-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `EA-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `EA-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-13-write-cutover-rollback-and-decommission-runbooks | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-170` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-116 |
| `STORY-170` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `STORY-170` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-170` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `STORY-170` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-170-keep-staff-working-through-the-cutover-inside-the-sunday-window | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-171` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-117 |
| `STORY-171` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-13) |
| `STORY-171` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-171` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `STORY-171` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-171-define-rollback-and-rehearsal-for-every-cutover-step | Backlog (BACKLOG-NW-001): this item with its full text |
| `EA-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-118 · **New in this plan (split from `EA-08`)** |
| `EA-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-06) |
| `EA-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EA-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `EA-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#ea-14-write-the-first-recovery-test-plan-and-evidence-template | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-172` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-118 |
| `STORY-172` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-06) |
| `STORY-172` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-172` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `STORY-172` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-172-prove-recovery-against-rpo-1-hour-and-rto-4-hours | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-173` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-119 |
| `STORY-173` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-01) |
| `STORY-173` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-173` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `STORY-173` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-173-plan-the-availability-proof-for-the-first-weeks-in-azure | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-174` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-120 |
| `STORY-174` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-174` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/azure-r3.md | Release file azure-r3: scope, exit criteria and OPEN dependencies |
| `STORY-174` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-174-retire-the-old-web-and-database-servers-before-30-june-2027 | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201, FR-203 |
| `EN-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-01` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-01-convert-the-solution-to-sdk-style-projects-on-net100 | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201 |
| `EN-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-13` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-13-record-the-decision-on-portal-and-api-project-shape | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201 |
| `EN-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-03` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-03-replace-direct-configurationmanager-calls-with-the-options-pattern | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201 |
| `EN-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-05` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-05-replace-the-windows-event-log-logger-with-standard-logging | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-214 |
| `EN-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-06` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-06-replace-the-in-process-session-order-draft | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201, FR-204, FR-210, FR-220 |
| `EN-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-04) |
| `EN-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-08` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-08-port-the-web-layer-to-aspnet-core-mvc-with-entra-id-staff-sign-in | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-201 |
| `STORY-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-201` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-201-run-order-desk-on-net-10-with-unchanged-staff-screens | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-202 |
| `EN-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-02` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-02-replace-mstest-v1-so-all-tests-run-on-windows-macos-and-linux | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement all .NET releases |
| `EN-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-09` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-09-build-an-automated-build-and-test-pipeline | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement all local testing, MVE-02 |
| `EN-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-12` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-12-provide-local-test-data-with-orders-and-a-local-database-recipe | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-202, FR-206, FR-211, FR-218 |
| `EN-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-10` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-10-make-time-handling-explicit-and-tested | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-202 |
| `STORY-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-12) |
| `STORY-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-202` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-202-keep-pricing-identical-to-today-pricing-parity | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-203 |
| `STORY-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-06, BR-10) |
| `STORY-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-203` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-203-keep-the-order-channel-visible-to-staff-channel-parity | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-206 |
| `STORY-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-02, BR-12) |
| `STORY-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-206` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-206-keep-dates-and-price-validity-identical-in-any-time-zone-time-parity | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-204 |
| `STORY-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-04) |
| `STORY-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-204` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-204-sign-staff-in-with-microsoft-entra-id | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-205 |
| `EN-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-05) |
| `EN-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `EN-04` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-04-remove-windows-sign-in-and-server-names-from-database-configuration | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-205 |
| `STORY-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-05) |
| `STORY-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r1.md | Release file dotnet-r1: scope, exit criteria and OPEN dependencies |
| `STORY-205` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-205-keep-secrets-out-of-code-tests-and-configuration | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-210, FR-216 |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-01, BR-10) |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `EN-11` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-11-build-the-authorisation-foundation-for-customer-scoping-and-channel | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-230` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-210 |
| `STORY-230` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-01) |
| `STORY-230` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-230` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-230` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-230-sign-in-and-see-only-my-own-companys-orders | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-240` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-220 |
| `STORY-240` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-04) |
| `STORY-240` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-240` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-240` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-240-authenticate-customers-with-an-externally-managed-identity | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-239` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-219 |
| `STORY-239` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-03) |
| `STORY-239` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-239` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-239` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-239-keep-portal-hosting-identity-and-mail-data-in-the-eu | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-231` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-211 |
| `STORY-231` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-02) |
| `STORY-231` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-231` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-231` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-231-see-my-companys-orders-from-the-last-24-months | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-232` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-212 |
| `STORY-232` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-03) |
| `STORY-232` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-232` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-232` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-232-open-an-order-and-see-lines-prices-address-and-status | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-213 |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-04) |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `STORY-233` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-233-see-one-of-six-order-statuses-with-an-as-of-time | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-214 |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-05) |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `STORY-234` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-234-create-a-new-order-by-copying-a-previous-order | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-235` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-215 |
| `STORY-235` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-06) |
| `STORY-235` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-235` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-235` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-235-have-a-submitted-portal-order-appear-in-order-desk-as-received | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-216 |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-06, BR-10) |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `STORY-236` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-236-show-staff-whether-an-order-came-from-the-portal-or-from-staff | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-218 |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-12) |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `STORY-238` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-238-show-my-negotiated-prices-not-list-prices | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-237` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-217 |
| `STORY-237` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-11) |
| `STORY-237` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-237` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-237` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-237-use-the-portal-in-french-and-english | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-241` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-221 |
| `STORY-241` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-08) |
| `STORY-241` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-241` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-241` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-241-record-who-what-when-and-channel-for-every-order-change | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-242` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-222 |
| `STORY-242` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-07) |
| `STORY-242` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-242` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-242` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-242-check-every-pilot-screen-against-wcag-22-level-aa | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-243` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-223 |
| `STORY-243` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (NFR-02) |
| `STORY-243` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-243` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r2.md | Release file dotnet-r2: scope, exit criteria and OPEN dependencies |
| `STORY-243` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-243-respond-in-under-2-seconds-at-the-95th-percentile | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-230 |
| `EN-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `EN-07` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-07-abstract-the-invoice-store | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-260` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-230 |
| `STORY-260` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-07) |
| `STORY-260` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-260` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-260` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-260-download-the-pdf-invoice-of-a-delivered-order | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-261` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-231 |
| `STORY-261` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-08) |
| `STORY-261` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-261` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-261` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-261-invite-and-remove-users-of-my-own-company | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-262` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-232 |
| `STORY-262` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-09) |
| `STORY-262` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-262` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-262` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-262-receive-an-e-mail-when-an-order-changes-to-shipped | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-263` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-233 |
| `STORY-263` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/business-requirements.md | Business requirements (BRD-NW-001): business and quality requirements cited in the source line (BR-11) |
| `STORY-263` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-263` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-263` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-263-use-the-portal-in-dutch | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-264` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-234 |
| `STORY-264` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-264` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-264` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/experiments.md | Experiment designs (MVE-01 to MVE-03): experiment gate MVE-02: decision before this item is committed; no result yet |
| `STORY-264` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-264-record-data-to-compare-sm-01-to-sm-04-with-their-baselines | Backlog (BACKLOG-NW-001): this item with its full text |
| `EN-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-235, FR-240 |
| `EN-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `EN-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `EN-14` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#en-14-publish-the-read-only-order-desk-api-contract-openapi-20 | Backlog (BACKLOG-NW-001): this item with its full text |
| `STORY-265` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/product-requirements.md | Product requirements (PRD-NW-001): product functional requirement FR-235 |
| `STORY-265` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/traceability.md | Traceability (TRACE-NW-001): requirement-to-story traceability (ES-06) |
| `STORY-265` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/releases/dotnet-r3.md | Release file dotnet-r3: scope, exit criteria and OPEN dependencies |
| `STORY-265` | https://github.com/waelkdouh/northwind-workshop/blob/main/docs/product/backlog.md#story-265-let-another-track-build-against-the-published-order-contract | Backlog (BACKLOG-NW-001): this item with its full text |

## F. Read-only Azure DevOps checks

**Result: none of the checks could be run. All affected fields are `needs_review`.**

| Check wanted | Attempt | Result |
|---|---|---|
| Project `northwind-workshop` exists in `waelconsulting` | `ado-remote-mcp-core_list_projects` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |
| Work item query for existing `nw-workshop` or `wael-01` items (duplicate risk) | `ado-remote-mcp-wit_query` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |
| Search for `wael-01` or the backlog ids in existing work items | `ado-remote-mcp-search_workitem` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |
| Read a work item to learn its type and fields | `ado-remote-mcp-wit_work_item` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |
| Project teams (area and iteration paths) | `ado-remote-mcp-core_list_project_teams` | Failed: the host answered *Tool does not exist*, although the tool search had listed it. |

Cause (as far as I can see): `.mcp.json` declares the server `ado-remote-mcp` (type `http`), but its tools are not loaded in this session. I read `.mcp.json` only to list the server name; I did not print the URL or any header. I did not try any other route to Azure DevOps (no REST call, no CLI, no web fetch), because the scope was the MCP server.

**Not validated, so `needs_review`:**

* The project exists and my account can read it.
* The process template. Agile has Epic, Feature, User Story. Scrum has Product Backlog Item instead of User Story. Basic has no Feature. CMMI has Requirement. The payload assumes Agile (`adoTypeNeedsReview: true` on every item).
* The fields `Microsoft.VSTS.Common.AcceptanceCriteria`, `Microsoft.VSTS.Common.Priority`, `System.Tags` and `System.Description` exist on each of the three types. Epics and features in Agile have no acceptance criteria field, and the backlog gives none for them.
* The backlog levels allow Epic > Feature > User Story for the target team.
* Existing items already carrying `nw-workshop` or the `wael-01` prefix, or one of the 144 backlog ids in a title. **Duplicate risk is unknown.** Wanted query: `[System.TeamProject] = 'northwind-workshop' AND ([System.Tags] CONTAINS 'nw-workshop' OR [System.Title] CONTAINS 'wael-01')`.
* Permission to create the new tags `nw-workshop`, `track-azure`, `track-dotnet`, `azure-r1` to `azure-r3`, `dotnet-r1` to `dotnet-r3` (9 new tag names: `nw-workshop`, 2 track tags and 6 release tags). Contributors can normally do this. Not verified.
* Permission to add Hyperlink relations and hierarchy links.

**Other evidence I could read (not Azure DevOps):** `git ls-remote --tags origin` lists the six `product/<track>-r<n>` tags, all on commit `5ad7971`. `git diff 5ad7971 HEAD -- docs knowledge-docs` shows no change. Only `.mcp.json` is untracked in the working tree.

## G. Optional add-on: the 33 unplanned items

**Not in scope. Decision for you.** They carry only `nw-workshop` and their track tag, never a release tag (ES-31). They are not planned in any release (backlog section 5). Power Platform has no release and no team (G-08, O-07), and `EPIC-204` cannot take a release tag until O-01 is answered.

| Track | Epics | Features | User Stories (enablers `EP-` included) |
|---|---|---|---|
| `track-power-platform` | 4 | 10 | 16 |
| `track-dotnet` | 1 | 1 | 1 |

If you approve it: 33 creates, 28 parent links, 129 hyperlink operations (same rules as section E). Title form `wael-01 <id> <title>`; the payload holds the full text under `optionalAddOnUnplanned`. Its checks passed in the same script run (one track tag, no release tag, parents exist).

| localId | ADO type | Exact title | Tags | Parent |
|---|---|---|---|---|
| `EPIC-204` | Epic | wael-01 EPIC-204 Order Desk API implementation for other tracks | `nw-workshop; track-dotnet` | none |
| `EPIC-301` | Epic | wael-01 EPIC-301 Claims platform foundation: environments, solution, connector stub, licensing, roles | `nw-workshop; track-power-platform` | none |
| `EPIC-302` | Epic | wael-01 EPIC-302 Record, approve and hand off claims; claims history | `nw-workshop; track-power-platform` | none |
| `EPIC-303` | Epic | wael-01 EPIC-303 Warehouse causes and claims dashboard | `nw-workshop; track-power-platform` | none |
| `EPIC-304` | Epic | wael-01 EPIC-304 Customer claim notifications | `nw-workshop; track-power-platform` | none |
| `FEAT-215` | Feature | wael-01 FEAT-215 Order Desk read-only API service | `nw-workshop; track-dotnet` | `EPIC-204` |
| `FEAT-301` | Feature | wael-01 FEAT-301 Environments, data loss prevention and solution | `nw-workshop; track-power-platform` | `EPIC-301` |
| `FEAT-302` | Feature | wael-01 FEAT-302 Licensing, connector stub and finance contract | `nw-workshop; track-power-platform` | `EPIC-301` |
| `FEAT-303` | Feature | wael-01 FEAT-303 Identity and roles | `nw-workshop; track-power-platform` | `EPIC-301` |
| `FEAT-304` | Feature | wael-01 FEAT-304 Record a claim | `nw-workshop; track-power-platform` | `EPIC-302` |
| `FEAT-305` | Feature | wael-01 FEAT-305 Approve claims and audit decisions | `nw-workshop; track-power-platform` | `EPIC-302` |
| `FEAT-306` | Feature | wael-01 FEAT-306 Credit-note hand-off to Finance | `nw-workshop; track-power-platform` | `EPIC-302` |
| `FEAT-307` | Feature | wael-01 FEAT-307 Claims history migration | `nw-workshop; track-power-platform` | `EPIC-302` |
| `FEAT-308` | Feature | wael-01 FEAT-308 Warehouse cause recording | `nw-workshop; track-power-platform` | `EPIC-303` |
| `FEAT-309` | Feature | wael-01 FEAT-309 Weekly claims dashboard | `nw-workshop; track-power-platform` | `EPIC-303` |
| `FEAT-310` | Feature | wael-01 FEAT-310 Customer claim e-mail | `nw-workshop; track-power-platform` | `EPIC-304` |
| `STORY-280` | User Story | wael-01 STORY-280 Offer a read-only Order Desk service for orders and order lines | `nw-workshop; track-dotnet` | `FEAT-215` |
| `EP-01` | User Story (enabler) | wael-01 EP-01 Design environments and data loss prevention policy | `nw-workshop; track-power-platform` | `FEAT-301` |
| `EP-02` | User Story (enabler) | wael-01 EP-02 Design the NorthwindClaims solution | `nw-workshop; track-power-platform` | `FEAT-301` |
| `STORY-301` | User Story | wael-01 STORY-301 Keep claims data in dedicated Europe environments with a DLP policy | `nw-workshop; track-power-platform` | `FEAT-301` |
| `EP-04` | User Story (enabler) | wael-01 EP-04 Decide licensing and cost | `nw-workshop; track-power-platform` | `FEAT-302` |
| `EP-03` | User Story (enabler) | wael-01 EP-03 Define the stub custom connector contract | `nw-workshop; track-power-platform` | `FEAT-302` |
| `EP-05` | User Story (enabler) | wael-01 EP-05 Define the finance CSV contract and drop location | `nw-workshop; track-power-platform` | `FEAT-302` |
| `EP-06` | User Story (enabler) | wael-01 EP-06 Define identity and roles with no self-approval | `nw-workshop; track-power-platform` | `FEAT-303` |
| `STORY-302` | User Story | wael-01 STORY-302 Sign claims users in with Entra ID and assign roles | `nw-workshop; track-power-platform` | `FEAT-303` |
| `STORY-320` | User Story | wael-01 STORY-320 Record a delivery claim in under 2 minutes with up to 5 photos | `nw-workshop; track-power-platform` | `FEAT-304` |
| `STORY-321` | User Story | wael-01 STORY-321 Approve claims above EUR 500 without self-approval | `nw-workshop; track-power-platform` | `FEAT-305` |
| `STORY-323` | User Story | wael-01 STORY-323 Record every claim decision for 7 years | `nw-workshop; track-power-platform` | `FEAT-305` |
| `STORY-322` | User Story | wael-01 STORY-322 Send an approved claim to Finance as a credit-note request | `nw-workshop; track-power-platform` | `FEAT-306` |
| `STORY-324` | User Story | wael-01 STORY-324 Decide whether spreadsheet claims move to the new solution | `nw-workshop; track-power-platform` | `FEAT-307` |
| `STORY-350` | User Story | wael-01 STORY-350 Let warehouse supervisors see and record causes of their claims | `nw-workshop; track-power-platform` | `FEAT-308` |
| `STORY-351` | User Story | wael-01 STORY-351 Show a weekly claims dashboard | `nw-workshop; track-power-platform` | `FEAT-309` |
| `STORY-370` | User Story | wael-01 STORY-370 E-mail the customer when a claim is approved or rejected | `nw-workshop; track-power-platform` | `FEAT-310` |

Points to decide for the add-on: `STORY-324` (spreadsheet claims migration) has **no priority** until O-14 is answered (Lena Varga, Julien Moreau). The Q1 2027 claims pilot cannot be committed (A-25). Publishing the Power Platform items would show work that has no team, which can mislead a reader of the board.

## H. Risks, ASSUMPTION and OPEN items

### Risks

| Id | Risk | Detail | Handling |
|---|---|---|---|
| R1 | **Azure DevOps could not be checked** | Project, process, types, fields, duplicates and tag rights are all `needs_review` (section F). A create could fail, or land in the wrong type. | Load the `ado-remote-mcp` tools, run the section F checks, and regenerate this preview before approval. |
| R2 | **Duplicate items** | If earlier workshop runs left items tagged `nw-workshop` or titled `wael-01 ...`, a second create would duplicate them (ES-28). | Run the duplicate query. Classify matches as Match, Similar, Distinct or Uncertain. Do not create until that is done. |
| R3 | **Documents still say draft and not approved** | Every release file says `status: proposed`, an empty `approval_date`, and approver `OPEN: O-09`. The Azure files also say the Git tag is *not created*, yet the tags now exist on `origin`. The business case says *Approved for discovery. Not yet approved for build* (O-21). The backlog is v0.1.0 draft. ADO items will link to files that still read as drafts. | You told me the releases are approved. The documents do not record it. I changed nothing under `docs/`. The owner should record the approval (O-09, A-38, A-39) so the linked files match the board. |
| R4 | **O-06 named no tool until now** | Backlog O-06 (owner Lena Varga) asked *which backlog tool and which ES-28 prefix*. `tracker_published: false` and section 6 say nothing is validated. Your request now names Azure DevOps `waelconsulting/northwind-workshop` and prefix `wael-01`. | Treat this request as the answer to O-06. After a real publish, the owner updates O-06 and `tracker_published` in a separate, approved change. Not done here. |
| R5 | **Rank and priority mapping** | The backlog rank is per track (Azure 1 to 36, .NET 1 to 40) and exists for stories and enablers only. `StackRank` is one number across a whole project, so two tracks would interleave. The backlog uses MoSCoW (Must, Should, Could), not ADO's 1 to 4. | ASSUMPTION P-A1: Must=1, Should=2, Could=3 in `Microsoft.VSTS.Common.Priority`. Rank stays in the description and the creation order, and is not written to `StackRank` unless you ask. Owner: Lena Varga. |
| R6 | **Enablers look like stories** | `EA-`/`EN-` enablers become User Story (backlog 6.1). Only the id and the title tell them apart, because you asked for exactly three kinds of tag. | Accepted as asked. A tag such as `enabler` would break the tag rule (ES-31), so none is proposed. |
| R7 | **Gated items look committed** | 35 planned items sit behind experiment gates (all `pending`; no experiment has been run). Publishing them in a release can read as a commitment. Gate text is in each description. | Keep the Gate line and the EXP link on each item. Decisions go, adjust or stop are taken before commit (experiments.md). |
| R8 | **Link volume** | 499 hyperlinks on 111 items is a lot of repeated links. Four documents repeat on most stories. | Option: epics and features only (about 129 links), or drop TRC and BKL from stories. Your choice (question Q4). |
| R9 | **Links point at `main`** | If the docs change later, the links show newer text than the tagged release. | Option: link the release tag (`/blob/product/<track>-r<n>/...`) instead. Question Q5. |
| R10 | **Title length** | The longest published title is 96 characters. The backlog limit of 100 (BD-04) applies to the title without the prefix; ADO allows 255. | No action. |
| R11 | **Cross-track needs are open, not waits** | X-nn rows are OPEN in the descriptions. A release never waits for another track (ES-31, A-45). | No ADO predecessor links are proposed, so the board shows no false dependency. |
| R12 | **`azure-r3` window** | A-58 stretches the window to 27 June 2027, leaving 3 days before the lease ends (C-01). O-27 (Marc Dubois) is unanswered. | Shown as written. No date fields are set in ADO. |
| R13 | **Power Platform has no release** | BA-03 has no team (O-07), so it has no release tag and is not in this scope (section G). | Decision Q2. |
| R14 | **Scope check by me** | Counts were checked by parsing the backlog, not by hand. The parse equals the register (144), section 3 counts and section 6.2 titles. | Re-run `python3 build_ado_payload.py` after any backlog change. |

### New ASSUMPTION items made by this preview (ES-03)

| Id | ASSUMPTION | Owner who can confirm |
|---|---|---|
| P-A1 | Must, Should and Could map to ADO priority 1, 2 and 3. | Lena Varga |
| P-A2 | Experiment links (EXP) go only to items whose gate is an MVE; BRD links go to epics and to stories whose source line cites a `BR-` or `NFR-`. | Lena Varga |
| P-A3 | The target project uses the Agile process (Epic, Feature, User Story). Not verified. | Ahmed Benali |
| P-A4 | Documentation links point at `main`, not at the release tags. | Lena Varga |

These four are mine and are not in the backlog. They are not requirements.

### ASSUMPTION and OPEN ids that the planned items cite

Text and owner come from backlog section 7 (the register of record). "Cited by" is the number of planned items that cite the id.

| Id | Cited by | Text | Owner |
|---|---|---|---|
| A-02 | 6 | .NET owns Order Desk code changes. Azure owns hosting, IaC, disaster recovery, monitoring and the C-04 cost model. Shared items are split per ES-30. | Ahmed Benali |
| A-03 | 4 | `BR-04`: Received, Confirmed and Cancelled are current as of Order Desk. Picking and Shipped are current as of the last nightly run, shown with an "as of" time. Delivered is set by staff. `BR-09` follows the same rule. | Lena Varga |
| A-04 | 2 | "Portal launch" in SM-01 to SM-04 means general availability, not the 20-customer pilot. | Lena Varga |
| A-05 | 5 | `NFR-01` is measured by a synthetic probe at the hosting edge, in local Central European time with summer time. `NFR-02` is measured on the server at the 95th percentile, with a load model from CS-03 for staff and an agreed customer figure. | Ahmed Benali |
| A-10 | 5 | Customer sign-in is provider-neutral. A test identity is used in experiments and local builds. | Ahmed Benali |
| A-11 | 3 | Portal release 1 covers French and English. Dutch follows. | Sofie Peeters, Lena Varga |
| A-12 | 2 | A customer administrator role exists. Who gets it is **OPEN:**. | Lena Varga |
| A-15 | 5 | The invoice number on an order is filled by the finance process, and the invoice folder year equals the invoice year. | Julien Moreau |
| A-16 | 2 | 24 months is a display window over the complete history held in the database. | Ahmed Benali |
| A-17 | 2 | Pilot customer concurrency is small (20 customers). No customer load figure exists. | Ahmed Benali |
| A-18 | 1 | The warehouse for each claim line can be derived from StockPilot or product data. It is not on order lines. | Pieter Janssens |
| A-19 | 4 | In `dotnet-r2`, staff onboard customer users until `BR-08` is built. | Lena Varga |
| A-20 | 5 | If .NET slips, Azure may rehost the unchanged app on a Windows virtual machine as a contingency. | Ahmed Benali |
| A-21 | 4 | A managed database service (PaaS) is the preferred data-tier direction. A virtual machine is the fallback. | Ahmed Benali |
| A-24 | 3 | Azure runs in UTC by default. Order Desk stores local time. Parity needs explicit handling. (From the code, not in `knowledge-docs`.) | Ahmed Benali |
| A-27 | 3 | The StockPilot CSV contract and file pick-up stay as they are. | Ahmed Benali |
| A-29 | 5 | The unauthenticated on-premises e-mail relay is not usable after the lease. A replacement mail path is needed. | Ahmed Benali |
| A-30 | 6 | SQL Server Agent is not available on Azure SQL Database (general knowledge, not fetched). | Ahmed Benali |
| A-31 | 4 | Backup and long-term retention can cover the 7-year audit retention (feature limits not verified). | Ahmed Benali |
| A-32 | 2 | Managed Instance is the most expensive compatible managed tier. No prices are in the inputs. | Ahmed Benali |
| A-33 | 11 | A log-based restore from existing backups can fit the Sunday window for a database of about 48 GB plus growth. | Ahmed Benali |
| A-35 | 5 | MVE success thresholds are starting points. Lena Varga sets the final numbers. | Lena Varga |
| A-37 | 5 | The pilot reads the Azure-hosted database after `azure-r2` is approved, not the on-premises one. | Ahmed Benali |
| A-39 | 3 | Documents only: no deployment, no commit and no Git tags in this run. Tags and the commit follow approval. | Marc Dubois |
| A-45 | 1 | Cross-track needs are **OPEN:** rows in the release files of the needing track and never a wait. | Ahmed Benali |
| A-51 | 8 | Facts the research read from the Order Desk code and database scripts are not stated in `knowledge-docs`: the code has no company check on an order, no role check on changing a status, takes the order channel from the form, sends no e-mail, records the channel only on creation, and the sample data holds no orders. "Picking" means "exported to StockPilot" and "Delivered" is set only by a staff action. | Ahmed Benali |
| A-52 | 2 | `FR-234` (instrumentation for SM-01 to SM-04) is Should, because the business case gives the measures no priority and names no measurement source. | Lena Varga |
| A-53 | 8 | Release approval of `azure-r3` happens before the first rehearsal Sunday (before 6 June 2027) and covers the reviewed migration procedure, rehearsal plan, cutover and rollback runbooks, recovery test plan and decommission plan. The rehearsals (6 and 13 June 2027), the live cutover and fallback (20 and 27 June 2027) and the recovery test, and their evidence, are planned execution after that approval and are not claimed here (ES-27). | Ahmed Benali |
| A-54 | 4 | The measurement rules for `NFR-03` to `NFR-09` are the author's proposals, because the business case defines none. | Ahmed Benali, Lena Varga |
| A-58 | 2 | The `azure-r3` target window is extended to 27 June 2027 so that the rehearsals and the cutover and fallback Sundays (20 and 27 June 2027) fall inside it; this leaves 3 days before the lease ends (C-01). | Marc Dubois |
| A-59 | 4 | `EA-15` and `EA-16` were added after the first review because no earlier item built the hosting runtime or moved the database; their size is not estimated. | Ahmed Benali |
| G-01 | 4 | Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. | Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10) |
| G-03 | 2 | Intake-review gaps: no Order Desk API owner; unclear Azure and .NET boundary; no BA-03 team or release; enabler work has no `BR-` or `NFR-` to cite. | Ahmed Benali (G-01, G-03), Lena Varga and Marc Dubois (G-08), Lena Varga (G-10) |
| MVE-A-03 | 1 | Growth stays linear. From mid-November 2026 to 30 June 2027 is 7 to 7.5 months, so the database reaches about 56 GB (48 GB plus 7.5 months at 1 GB) and invoices about 135 GB (120 GB plus 7.5 months at 2 GB). The month count is itself an assumption. | Ahmed Benali |
| MVE-A-04 | 1 | A local SQL Server (Developer edition or container) is available to run the database scripts. | Ahmed Benali |
| MVE-O-05 | 2 | Where the SQL Server Agent job and the Windows scheduled task for the Antwerp transfer are defined. | Ahmed Benali |
| O-01 | 4 | Who owns the Order Desk API (an enabler under `track-dotnet`, or another owner)? | Ahmed Benali |
| O-03 | 13 | Does `azure-r1` rehost .NET Framework 4.8 or wait for `net10.0`? Is staff Entra sign-in in BA-01? | Ahmed Benali |
| O-04 | 2 | What status freshness is acceptable, given the nightly batch? | Lena Varga |
| O-05 | 2 | Does "portal launch" mean the pilot or general availability? | Lena Varga |
| O-08 | 4 | Order-to-invoice mapping, order retention, customer concurrency, and warehouse per order line. | Ahmed Benali |
| O-09 | 1 | Who is the named release approver for each track? | Marc Dubois |
| O-10 | 3 | Which identity provider do customer users use (OQ-01)? | Ahmed Benali |
| O-11 | 3 | Must Dutch be in the first release (OQ-02)? | Sofie Peeters, Lena Varga |
| O-12 | 2 | Do customer administrators exist for every customer or only for large ones (OQ-03)? | Lena Varga |
| O-15 | 15 | Where do the finance system, the `NWFS01` shares, the domain controllers and the Antwerp SFTP route live after 30 June 2027? | Ahmed Benali, Julien Moreau |
| O-16 | 5 | How does an order get the status Delivered, and can StockPilot's file pick-up run more than nightly without changing StockPilot? | Ahmed Benali, Pieter Janssens |
| O-17 | 5 | What sends order confirmations today? | Ahmed Benali |
| O-18 | 4 | Where do the customer e-mail address and language preference live? | Lena Varga |
| O-19 | 5 | Which build and deployment pipeline tool? | Ahmed Benali |
| O-20 | 4 | Decision record on the portal and API project shape (ES-13). | Ahmed Benali |
| O-21 | 3 | Approval and funding to build (the business case says "not yet approved for build"). | Marc Dubois |
| O-23 | 4 | Which database does the Q2 2027 portal pilot read (T-08)? | Ahmed Benali |
| O-24 | 8 | What does the customer identity service cost, and does it count toward C-04? | Ahmed Benali |
| O-26 | 2 | Name a measurement source and an owner for each goal and success measure (BG-01 to BG-05, SM-01 to SM-07); confirm the proposed goal owners in BRD section 4.1; name who speaks for customer users. | Lena Varga |
| O-27 | 5 | Confirm the extended `azure-r3` target window, which ends on 27 June 2027 (A-58), the margin of 3 days before the lease ends on 30 June 2027 (C-01), and that the product owner approves `azure-r3` before the first rehearsal Sunday, before 6 June 2027 (A-53). The rehearsals (6 and 13 June 2027) and the live cutover and fallback (20 and 27 June 2027) are planned execution after that approval. | Marc Dubois |
| O-28 | 1 | What happens to a line of a copied order whose product is no longer available (`STORY-234`)? Not stated in the sources. | Lena Varga |
| T-01 | 1 | `BR-04` says "always up to date" but Picking and Shipped change once a night (handled by A-03). | Lena Varga |
| T-03 | 1 | C-04 is a shared cap held only by BA-01 (handled by A-02, X-12). | Ahmed Benali |
| T-08 | 1 | The Q2 2027 portal pilot and C-05 versus the database migration (A-37, O-23). | Ahmed Benali |
| T-10 | 1 | ES-13 (one solution) and ES-19 versus a portal, an API and a re-platform (`EN-13`). | Ahmed Benali |
| T-13 | 1 | `NFR-08` asks for who, what, when and channel but today's audit rows may not record all (listed, not fixed silently). | Ahmed Benali |
| T-14 | 5 | The RPO of 1 hour is met on paper by 15-minute log backups but recovery was never tested (`EA-14`). | Ahmed Benali |
| T-15 | 1 | `NFR-03` and `NFR-04` apply "wherever relevant" but BA-02 does not list `NFR-03` and BA-01 does not list `NFR-04` (split per track, A-43). | Ahmed Benali |
| T-17 | 2 | `NFR-01` uses CET only but business hours cross the summer-time change (A-05). | Ahmed Benali |
| X-01 | 7 | Hosting target and pilot test environment for the modernised application (.NET needs Azure) | Ahmed Benali |
| X-02 | 12 | A `net10.0` application that follows a documented configuration and identity contract (Azure needs .NET) | Ahmed Benali |
| X-03 | 8 | Database sign-in moves from Windows-integrated to Entra or a managed identity (Both) | Ahmed Benali |
| X-04 | 8 | Staff sign-in moves to Entra ID; customer sign-in follows OQ-01 (the Azure side stays OPEN) (.NET needs Azure or IT) | Ahmed Benali |
| X-05 | 4 | StockPilot exchange redesign for a managed data tier; file contract fixed (.NET needs Azure) | Ahmed Benali |
| X-06 | 4 | Status freshness is bounded by the exchange cadence (.NET needs Azure and StockPilot) | Lena Varga |
| X-07 | 8 | The in-process session draft must be stateless before scale-out (Azure needs .NET) | Ahmed Benali |
| X-08 | 4 | Logging moves to Application Insights and Log Analytics (.NET needs Azure) | Ahmed Benali |
| X-09 | 6 | Invoice files move from a network path to Azure storage (Both) | Julien Moreau, Ahmed Benali |
| X-10 | 6 | Outbound mail replaces the on-premises relay (Both) | Ahmed Benali |
| X-11 | 6 | Build and test pipeline (.NET) and deployment pipeline (Azure) (Both) | Ahmed Benali |
| X-12 | 4 | The shared monthly cap C-04 covers Order Desk and the portal (Azure needs .NET sizing inputs) | Ahmed Benali |
| X-13 | 2 | An internet-facing entry for customers while data services use private endpoints (.NET needs Azure) | Ahmed Benali |
| X-14 | 6 | One solution and three projects versus a portal area and an API: a decision record is needed (Both) | Ahmed Benali |
| X-15 | 4 | Keeping the 7-year audit trail once the database is in Azure (.NET needs Azure) | Ahmed Benali |
| X-20 | 3 | An Order Desk API (read orders and lines) for the custom connector (Power Platform needs .NET) | Ahmed Benali |
| X-21 | 3 | An order data contract for claims: order number, lines, quantities, prices, customer, warehouse (Power Platform needs .NET) | Lena Varga, Pieter Janssens |
| X-23 | 1 | Connector sign-in (Entra app registration, OAuth) (Power Platform needs Azure or IT) | Ahmed Benali |
| X-25 | 1 | Warehouse for each order line, for `BR-17` (Power Platform needs .NET and StockPilot data) | Pieter Janssens |

Items that rely on an OPEN question stay publishable: the OPEN marker is in the description, with its owner, so nobody reads it as a requirement (ES-04).

## I. Nothing has been created. Approval needed.

**Status: nothing has been created, updated, linked or deleted in Azure DevOps.** No file under `docs/` or `knowledge-docs/` was changed. No `git push`, commit or tag was run. Only four files in `.copilot-tracking/plans/2026-11-17/` were written: the two scripts, the payload and this preview.

**What I need from you before any write:**

1. Load the `ado-remote-mcp` tools (or confirm another read path) so I can run the section F checks. Then I regenerate this preview with the real types, fields and duplicate results.
2. Approve the scope of 111 items and the exact text in sections C and D, or tell me what to change.
3. Approve the field mapping (section B) and answer the questions below.
4. Say, in words, something like *"Approved: create the 111 items in Azure DevOps"*. Without that, I stay read-only.

**Open questions (OPEN:, with who can answer):**

* **Q1** Is the target process Agile? (Ahmed Benali, after the read checks.)
* **Q2** Do you want the 33 unplanned items (section G) published too, with track tag only? (Lena Varga.)
* **Q3** Mapping Must/Should/Could to priority 1/2/3, and no `StackRank`: acceptable? (Lena Varga.)
* **Q4** Keep all 499 hyperlinks, or reduce them (risk R8)? (Lena Varga.)
* **Q5** Link `main` (as you asked) or the release tags (risk R9)? (Lena Varga.)
* **Q6** Who records the release approval in the release files (R3, O-09)? (Marc Dubois.)
* **Q7** Which area path and iteration path should items use? The backlog sets none; the default project root is assumed. (Ahmed Benali.)
