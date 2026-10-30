# Release azure-r3: Stabilise and decommission (Azure track)

| Field | Value |
|---|---|
| Document | Release file, deliverable D6 (ES-31) |
| Track | Azure, business area BA-01 Platform and data-centre exit |
| Release name | Stabilise and decommission |
| Release tag | `azure-r3` |
| Track tag | `track-azure` |
| Git tag | `product/azure-r3`. Approved 2026-10-30; the tag is created on the commit that holds this file (ES-31, A-08, A-29). |
| Status | Approved — product owner approval recorded 2026-10-30; Git tag product/azure-r3 |
| Product owner | Lena Varga, Head of Customer Operations (A-29) |
| Proposed target date | By 30 June 2027 (C-01). **ASSUMPTION:** A-07 (a target, not a commitment). |
| Date of this file | 2026-10-30 |
| Items in this release | 8: 1 epic, 2 features, 0 enablers, 5 stories (section 3) |
| Sources | `docs/product/backlog.md` (register in section 11 is the list of members), `docs/product/traceability.md`, `docs/product/product-requirements.md` (section 8.3), `docs/product/business-requirements.md`, `knowledge-docs/business-case.md`, `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01, ES-27, ES-30, ES-31, ES-39) |
| Boundary | This is a planning document. Nothing is deployed, switched off, published, committed or tagged (ES-27). |

## 1. Words used

* **BA-01** is the business area "Platform and data-centre exit". **BR-** is a business requirement, **NFR-** a quality target (non-functional requirement), **C-** a constraint and **SM-** a success measure, all from the business case. **CS-** is a fact about today's system. **ES-** is an engineering standard.
* **Order Desk** is the internal web application staff use to enter and manage orders. **`NWWEB01`** is the old web server, **`NWSQL01`** the old database server and **`NWFS01`** the old file server that holds the invoice PDFs, all in the Lyon data centre (CS-06, CS-07, CS-08).
* **SM-07** is the success measure "production servers past end of support": 2 now, 0 by 30 June 2027.
* **`tst`** is the test environment and **`prd`** the production environment (ES-23).
* **RPO** (recovery point objective) is how much data may be lost. **RTO** (recovery time objective) is how long recovery may take. **Runbook** is a short, numbered, plain-language guide for one operating task.
* **Decommission** means to switch a server off and remove it from service.
* **MoSCoW** is the priority scale: Must, Should, Could.
* **ASSUMPTION:** marks anything that is not stated in `knowledge-docs`. **OPEN:** marks a question nobody has answered yet. Neither is a requirement (ES-03, ES-04).

## 2. Release goal

Retire the old servers so that production servers past end of support go from 2 to 0 by 30 June 2027. Confirm that the real run cost is within the EUR 1,500 per month ceiling. Prove the recovery targets on the real production setup. Hand over runbooks the six-person IT team can follow without the people who built the platform (source: SM-07, C-04, NFR-06, C-06).

This is its own release so that the closing measure, SM-07, can be approved on its own. SM-07 has no value until the cutover in `azure-r2` is done (inside the Azure track, section 7.1).

## 3. Items planned in this release

The list below is every item that carries the tags `track-azure` and `azure-r3`. It equals the rows of the register in `docs/product/backlog.md` section 11 for `azure-r3`: 8 items. Each item carries exactly one track tag and exactly one release tag. Parent and child share the same track and release. Rows are in the register order. The build order is in section 7.1.

| ID | Type | Parent | Title | Priority | Tags | Sources |
|---|---|---|---|---|---|---|
| `EP-AZ-03` | Epic | - | Stabilise and decommission | Must | `track-azure`, `azure-r3` | SM-07, C-04, NFR-06 |
| `FT-AZ-10` | Feature | `EP-AZ-03` | Retire the old servers | Must | `track-azure`, `azure-r3` | SM-07, C-01, C-02, CS-06, CS-07 |
| `FT-AZ-11` | Feature | `EP-AZ-03` | Closing cost check, recovery test report and runbooks | Must | `track-azure`, `azure-r3` | C-04, NFR-06, CS-23, ES-09 |
| `US-AZ-018` | Story | `FT-AZ-11` | Recovery test and report on production | Must | `track-azure`, `azure-r3` | NFR-06, CS-23, ES-09 |
| `US-AZ-017` | Story | `FT-AZ-11` | Closing cost check against the ceiling | Must | `track-azure`, `azure-r3` | C-04, ES-09 |
| `US-AZ-019` | Story | `FT-AZ-11` | Runbooks the IT team can follow | Must | `track-azure`, `azure-r3` | C-06, CS-22, CS-23, ES-09, ES-01 |
| `US-AZ-015` | Story | `FT-AZ-10` | Retire the old web and database servers | Must | `track-azure`, `azure-r3` | SM-07, C-01, C-02, CS-06, CS-07 |
| `US-AZ-016` | Story | `FT-AZ-10` | Decide whether the file server counts and report SM-07 | Must | `track-azure`, `azure-r3` | SM-07, CS-08, CS-11, C-02 |

Counts: 1 epic, 2 features, 0 enablers and 5 stories (`US-AZ-015` to `US-AZ-019`). Total 8. All are priority Must.

## 4. Requirements covered

**Business requirements (BR-):** none. BR-13 (staff keep working through the move) is carried by `azure-r2`.

**Quality targets (NFR-).** An NFR has no priority in the business case. It is treated as Must because it gates a release that carries a Must outcome (A-12).

| ID | What it says (short) | Source | Carried in this release by | Note |
|---|---|---|---|---|
| NFR-06 | Recovery point of 1 hour and recovery time of 4 hours for order data | NFR-06, CS-07, CS-23 | `US-AZ-018` (recovery test and report on production), `FT-AZ-11`, `EP-AZ-03` | This is the "tested" part. The backup and restore method and the first restore test are in `azure-r2`. |

**Constraints (C-) carried.**

| ID | What it says (short) | Carried by |
|---|---|---|
| C-01 | The data-centre lease ends on 30 June 2027 | `US-AZ-015`, `FT-AZ-10` |
| C-02 | The web and database servers are past end of support | `US-AZ-015`, `US-AZ-016`, `FT-AZ-10` |
| C-04 | Azure run cost of at most EUR 1,500 per month (shared by both tracks, A-14) | `US-AZ-017` (closing cost check), `FT-AZ-11`, `EP-AZ-03` |
| C-06 | Small IT team, no Kubernetes | `US-AZ-019` (runbooks) |

**Success measure (SM-) moved.** **SM-07: production servers past end of support, 2 now, 0 by 30 June 2027.** Carried by `US-AZ-015`, `US-AZ-016`, `FT-AZ-10` and `EP-AZ-03`. Whether `NWFS01` counts is OPEN-12 (source: SM-07, CS-06, CS-07, CS-08).

## 5. What this release leaves out

| Left out | Where it goes |
|---|---|
| Production environment, data move, nightly exchange, mail relay replacement, backup method, first restore test, cutover runbook and cutover itself | `azure-r2` (already planned there) |
| Foundation, network, hosting decision, cost model and exchange proof | `azure-r1` (already planned there) |
| New functions of any kind | Not planned. This release adds none. |
| Customer portal and ordering features (BR-01 to BR-12, NFR-02, NFR-07, NFR-08) | The .NET track (BA-02) |
| Decommissioning `NWFS01` unless OPEN-12 says it counts | Held back until the question is answered (`US-AZ-016`) |
| Any change to StockPilot (C-03) and any change to the finance system | Out of scope |
| A split of the EUR 1,500 ceiling between the tracks | Not planned. See OPEN-04. |
| A retrieval target for 7-year audit data | Not planned. See OPEN-22. |
| BA-03 Delivery claims and credit notes | Out of scope for the whole product backlog. |
| Business case section 6 exclusions: online payment, a native mobile app, changes to StockPilot, replacing the finance system, customers recording claims themselves | Out of scope. |
| Deploying or switching off anything from this workshop | Never done from this workshop (ES-27). |

## 6. Business outcome

When this release is accepted, the product owner can read: a recovery test report on production against the RPO of 1 hour and the RTO of 4 hours; a closing cost report that says "met" or "not met" against EUR 1,500; runbooks that a second team member has walked through; a decommissioning record for `NWWEB01` and `NWSQL01`; and an SM-07 report that shows the count with and without `NWFS01`.

## 7. Dependencies

### 7.1 Order inside the Azure track

Inside the Azure track, this release uses the production environment, data move and cutover from `azure-r2`. The cutover (`US-AZ-014`) is in place first, because the recovery test, cost check, runbooks and decommissioning all start from a running production. If the cutover is stopped, this release does not start. The product owner may change the order inside a release without changing any tag (A-43). The "Depends on" column names items of the Azure track only.

| Rank | ID | Title | Depends on (same track) |
|---|---|---|---|
| 29 | `US-AZ-018` | Recovery test and report on production | `US-AZ-014` |
| 30 | `US-AZ-017` | Closing cost check against the ceiling | `US-AZ-014` |
| 31 | `US-AZ-019` | Runbooks the IT team can follow | `US-AZ-014` |
| 32 | `US-AZ-015` | Retire the old web and database servers | `US-AZ-014`, `US-AZ-018` |
| 33 | `US-AZ-016` | Decide whether the file server counts and report SM-07 | `US-AZ-011`, `US-AZ-015` |

The ranks continue from `azure-r2` (ranks 13 to 28). Why this order: decommissioning is last because it removes the rollback path. The servers are retired only once the recovery test report is accepted by the product owner (source: C-01, SM-07, `US-AZ-015`). A final backup of the Lyon database is kept as the product owner agrees, and its date and place are recorded.

### 7.2 Cross-track dependencies (all written as OPEN:)

This release never waits for another track. Each cross-track question below is an **OPEN:** item with the person who can answer it, and the release states what it does without the answer. That position is an **ASSUMPTION:** (A-28) until the person decides.

| ID | OPEN question or dependency | Person who can answer | What this release does without the answer |
|---|---|---|---|
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Reports the whole-platform cost against the ceiling. Applies no split (`US-AZ-015`, `US-AZ-017`). |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Retires `NWWEB01` and `NWSQL01`. Reports SM-07 with and without `NWFS01`. `NWFS01` stays in service until the answer is given (`US-AZ-015`, `US-AZ-016`). |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Used by `US-AZ-016`. Changes nothing in the finance system. `NWFS01` is retired only when the invoice files are verified in Azure and Finance has confirmed where it writes new invoices. |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Used by `US-AZ-018`. Backs up audit data on the same schedule as other order data and sets no retrieval target. |

OPEN-06 and OPEN-22 are used by items in this release but are not in the plan's list of cross-track items for `azure-r3` (OPEN-04 and OPEN-12). They are shown here because the items cite them (section 11, difference 1).

## 8. Assumptions used in this release (ES-03)

IDs and wording are the same in every product document. Each has a person who can confirm it. None is a requirement. A-07 and A-08 name both tracks and are copied unchanged.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-08 | Release names `azure-r<n>`, `dotnet-r<n>` and Git tags `product/azure-r<n>`, `product/dotnet-r<n>` | Lena Varga |
| A-12 | NFR-01..NFR-08 have no priority in the business case. The backlog orders them by the release they gate and shows the release | Lena Varga |
| A-14 | The EUR 1,500 per month ceiling (C-04) is shared by both tracks | Marc Dubois |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-43 | The order of items inside a release (`backlog.md` section 4 and section 7.1 of each release file) is a proposed build order. The product owner may change it without changing any tag | Lena Varga |

## 9. OPEN items used in this release (ES-04)

| ID | OPEN question or dependency | Person who can answer | Track(s) affected | Used in this release by |
|---|---|---|---|---|
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET | `EP-AZ-03`, `US-AZ-015`, `US-AZ-017` |
| OPEN-06 | How finance invoice output reaches Azure; where Order Desk reads it | Julien Moreau | Azure and .NET | `US-AZ-016` |
| OPEN-11 | Backlog publishing tool (ES-39) | Lena Varga | Azure and .NET | Section 10 |
| OPEN-12 | NWFS01 operating system and whether it counts in SM-07 | Ahmed Benali | Azure | `EP-AZ-03`, `FT-AZ-10`, `US-AZ-015`, `US-AZ-016` |
| OPEN-22 | 7-year audit retention: sizing, backup and retrieval vs RPO/RTO | Lena Varga, Ahmed Benali | Azure and .NET | `US-AZ-018` |

## 10. Tag publication reminder (ES-39)

Nothing is published now. The publishing tool is **OPEN:** OPEN-11 (Lena Varga). When the backlog is published, the track tag and the release tag travel with every one of the 8 items above, so this release stays identifiable in the tool:

| Tool | What to set for this release |
|---|---|
| Azure DevOps | Work-item tags `track-azure` and `azure-r3` on every item. A query on the tag `azure-r3` lists the release. |
| GitHub | Issue labels `track-azure` and `azure-r3`, and the milestone `azure-r3`. |
| Jira | Labels `track-azure` and `azure-r3`, and the fix version `azure-r3`. |

Titles start with the item ID. Descriptions hold the source identifiers (ES-28, ES-29). The Git tag `product/azure-r3` is separate from these tool tags. It is created by the product owner only once the release is approved and its commit is made.

## 11. Differences found between the plan, the backlog and the other documents

These are for the product owner. None leaves a requirement uncovered for this release. The member list in section 3 follows the backlog register.

| # | Difference | Items or identifiers |
|---|---|---|
| 1 | Items in this release cite OPEN-06 and OPEN-22, which are not in the plan's list of cross-track items for `azure-r3`. They are shown in section 7.2 with what the release does without the answer. | `US-AZ-016`, `US-AZ-018` |
| 2 | The plan lists "decommission NWWEB01 and NWSQL01 (NWFS01 only if OPEN-12 says it counts)" as release contents. The backlog turns this into two stories: `US-AZ-015` for the two servers and `US-AZ-016` for the decision on `NWFS01` and the SM-07 report. The plan's "cost check", "DR test report" and "runbooks" are `US-AZ-017`, `US-AZ-018` and `US-AZ-019`. | `US-AZ-015` to `US-AZ-019` |
## 12. Entry criteria and definition of done (business level)

**Entry criteria.** The product owner has read this file and the backlog. The members in section 3 match the backlog register. The `azure-r2` cutover is complete and production runs in Azure (inside the Azure track). Each cross-track OPEN item in section 7.2 is visible to the person named, and the release can proceed without an answer.

**Definition of done.** The release is done when the acceptance criteria of its 8 items are met by tests and validation only (ES-27):

* *Recovery.* A restore run against a production backup in an isolated place loses at most 1 hour of data and takes at most 4 hours in total. The report in `docs/migration/` lists steps, times, result against targets and each gap. Production data used in the test stays in the EU and is deleted after the test, with Ahmed Benali's explicit approval.
* *Cost.* One full month of cost data for `prd` and `tst` is compared with EUR 1,500, per service and in total, and the report says "met" or "not met". If it is not met, the report lists options with their savings and their effect on availability and recovery.
* *Runbooks.* Runbooks exist for daily checks, restore, a failed nightly exchange and rollback. Each has a trigger, numbered steps, an owner and a check that shows success, in plain language. A second team member who did not write each runbook has walked through it, and any gap is fixed.
* *Retirement.* Once the recovery test report is accepted by the product owner and the decommissioning checklist is complete, `NWWEB01` and `NWSQL01` are recorded as switched off and removed. A final backup of the Lyon database is kept as the product owner agrees, with its date and place recorded. SM-07 is reported with the count and the date, with and without `NWFS01`. `NWFS01` is retired only if OPEN-12 says it counts.
* *Review.* All of the above is reviewed by a named person. **Nothing is deployed from this workshop. Infrastructure code is validated locally and reviewed, not applied (ES-27).** The recovery test and the switching off of servers are carried out by the IT team in its own controlled environment and change process, not from this workshop. This file does not start or authorise any of them.

## 13. Approval

Approval was recorded on 2026-10-30; the Git tag `product/azure-r3` is created on the commit that holds the approved files.

| Field | Entry |
|---|---|
| Approver (product owner, A-29) | Approved in the Squad session by the requesting user (@waelkdouh) acting as product owner. Lena Varga remains the assumed product owner (A-29, to be confirmed). |
| Date of decision | 2026-10-30 |
| Approval status | [x] Approved  [ ] Approved with changes  [ ] Not approved |
| Changes asked for | None |
| Git tag `product/azure-r3` created (date and person) | [x] Created on the approval commit, 2026-10-30 (see `git show product/azure-r3`) |
| Tool tags published (OPEN-11) | [ ] Not yet published |

Status now: **Approved on 2026-10-30. Git tag `product/azure-r3` is created on the commit that holds this file.**
