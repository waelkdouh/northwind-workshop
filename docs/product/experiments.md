# Northwind Traders — Experiments: Platform and data-centre exit (BA-01) and Ordering and customer self-service (BA-02)

| Field | Value |
|---|---|
| Document | Experiments, deliverable D3 (one Minimum Viable Experiment per business area) |
| Status | Draft - for review. Not approved for build. (A-16) |
| Date | 2026-10-30 |
| Scope | **BA-01** Platform and data-centre exit (Azure track, `track-azure`): `MVE-BA01`. **BA-02** Ordering and customer self-service (.NET track, `track-dotnet`): `MVE-BA02`. **BA-03** is out of scope. |
| Experiment owners (proposed) | `MVE-BA01`: Ahmed Benali, IT Manager. `MVE-BA02`: Lena Varga, Head of Customer Operations. (A-30) |
| Builds on | `docs/product/business-requirements.md` (BRD, D1) and `docs/product/product-requirements.md` (PRD, D2). Their IDs and wording are reused. |
| Sources | `knowledge-docs/business-case.md` (version 2.0), `knowledge-docs/current-state.md`, `knowledge-docs/engineering-standards.md` (ES-01 to ES-07, ES-17, ES-20 to ES-27, ES-30, ES-31). Findings from reading `src/` and `database/` are used only to explain risk and are marked **ASSUMPTION:** (A-22, A-23, A-32). |
| Boundary | This document **designs** two small tests. It runs none of them. Nothing is deployed, built, committed or tagged. No change to `src/`, `database/`, `infra/` or Power Platform. No production data is moved (ES-27). |

How to read this document:

* **MVE** means Minimum Viable Experiment: the smallest, cheapest test that can show whether one risky belief is true, **before** the team commits to build.
* An MVE is **not implementation**. It produces a decision and a short note, not a product. Test code, if any, is thrown away.
* IDs such as `BR-04`, `NFR-03`, `C-03`, `SM-02` and `P-03` come from the business case. `CS-` IDs come from `current-state.md`. `ES-` IDs come from the engineering standards. `FT-`, `EN-` and `R-` IDs come from the PRD. Release names (`azure-r1`, `dotnet-r2`) are the PRD release names.
* Every claim cites its source in the form `(source: BR-04, CS-10)` (ES-02).
* **ASSUMPTION:** marks anything not stated in `knowledge-docs`. All are in section 8 with a person who can confirm them (ES-03). Numbers used as pass or fail marks are all assumptions under **A-06**. The cost figure of EUR 1,350 is **A-45**.
* **OPEN:** marks an unanswered question. All are in section 9 with the person who can answer (ES-04).

## 1. Summary

| | `MVE-BA01` | `MVE-BA02` |
|---|---|---|
| Business area and track | BA-01 Platform and data-centre exit. `track-azure` | BA-02 Ordering and customer self-service. `track-dotnet` |
| Riskiest assumption | The nightly StockPilot exchange can be rebuilt for Azure and still produce and accept **the same files**, at 02:00, in the same folders, with **no change to StockPilot** | A status that is only as fresh as the 02:00 update is **enough** for customers, and cuts "where is my order?" calls |
| Why it is the riskiest | If wrong, shipments stop silently after cutover, or the move needs a more costly design, close to the 30 June 2027 lease end | If wrong, the portal's main value (410 calls per week, 35 % of inbound calls) is not reached, and we learn it only after the pilot |
| Cheapest test | One-page design, a throw-away proof on a **local developer SQL Server**, byte comparison on 3 sample runs, one 30-minute call with Antwerp | Desk check of call records, then a **manual** daily status e-mail for 2 weeks to about 10 customers, compared with their earlier 4 weeks, plus a 2-question survey |
| Owner | Ahmed Benali (A-30) | Lena Varga (A-30) |
| Time and effort | About 2 weeks elapsed, about 6 person-days (A-31) | About 8 weeks elapsed (4 baseline weeks, 1 prepare week, 2 test weeks, 1 analysis week), about 8 person-days (A-31, A-44) |
| Success mark (A-06) | Files identical on 3 of 3 runs, Antwerp details named in writing, no SQL server on a virtual machine needed | At least 30 % fewer such calls **and** at least 70 % of customers say the status was enough |
| Informs | `azure-r1` (`FT-AZ-04`, `EN-AZ-03`, `EN-AZ-12`) and `azure-r2` (`EN-AZ-09`, `EN-AZ-14`, `FT-AZ-08`) | `dotnet-r2` (`FT-DN-11`, `FT-DN-09`, `FT-DN-10`), `dotnet-r4` (`FT-DN-21`, `FT-DN-22`) |
| Needs explicit human approval before this step | A real sample file from the live exchange folder (touches production data). Any real Azure resource (not planned). | Contacting real customers by e-mail and survey. Use of call records. |

Both MVEs were chosen from the research list and confirmed. The reasons are in sections 2 and 3. The assumptions considered and **not** chosen are in section 6.

## 2. `MVE-BA01` — The StockPilot exchange works in an Azure-compatible form with identical files

**Business area:** BA-01 Platform and data-centre exit. **Track tag:** `track-azure`.

### 2.1 The riskiest assumption and why

**Assumption.** The nightly exchange with StockPilot (the warehouse system in Antwerp) can be rebuilt so that it runs in Azure and still:

* writes the **same order file** (`orders_YYYYMMDD.csv`) that Antwerp reads today,
* reads the **same shipment file** (`shipments.csv`) that Antwerp writes today,
* runs at **02:00** and uses the **same folders**, and
* needs **no change to StockPilot**.

(source: CS-10, C-03, BR-13, A-23)

**What the exchange does today.** At 02:00 a database job on `NWSQL01` runs two procedures. The first writes confirmed orders to a file with a command-line tool and sets those orders to Picking. The second reads the shipment file from a local `D:` drive and sets those orders to Shipped. A Windows scheduled task on the same server copies the folder to the Antwerp file-transfer (SFTP) server. (source: CS-10, `database/003-stockpilot-exchange.sql` read as **ASSUMPTION:** A-22.)

**Why it is the riskiest.** If the assumption is wrong:

* Orders do not reach the Antwerp warehouse, or shipments do not come back. Picking and shipping stop **without an obvious error** (source: CS-10, R-02).
* The only fix would be to change StockPilot. That is forbidden until at least 2028 (source: C-03, business case §6).
* Or the database has to stay on a virtual machine, which raises the monthly cost towards the EUR 1,500 ceiling (source: C-04, R-05, A-09).
* The team would find this in the `azure-r2` rehearsal, with little time left before the lease ends on 30 June 2027 (source: C-01, R-01).

Four things make this the riskiest in BA-01:

1. The current design uses two database-server features that Azure SQL Managed Instance does not offer: command-line calls from the database and a bulk load from a local disk. This comes from a search summary of the Microsoft page, not from the page itself (source: A-23, research W1).
2. The files must stay **identical** because StockPilot cannot change (source: C-03).
3. The network path from Azure to the Antwerp file-transfer host is not known (source: OPEN-07).
4. The PRD rates this risk High likelihood and High impact (source: R-02, A-25).

**Alternatives considered.** Cost fit (EUR 1,500) and the 48 GB move in a Sunday window are also risky. They are **not** chosen as the MVE. Reasons are in section 6.

### 2.2 Hypothesis

**If** the exchange is rebuilt without the command-line call and without the local-disk bulk load, **then** it can still write byte-for-byte identical order files and ingest the same shipment files, with the same result in the database, **because** the file contents depend only on the query and on a small number of format settings (separator, line ending, character set, row order) that can be set on purpose. (**ASSUMPTION:** A-32)

### 2.3 Source IDs

(source: CS-10, C-03, C-01, C-04, BR-13, NFR-03, NFR-05, A-19, A-22, A-23, OPEN-07, OPEN-20)

### 2.4 Cheapest test design

**Rules for this test.** Design and local proof only.

* No deployment. No Azure resource is created or used.
* No change to `src/`, `database/`, `infra/` or Power Platform.
* The server `NWSQL01`, StockPilot and the Antwerp file-transfer server are **not touched**.
* No production data is used. Sample data only (section 2.8).
* No secret, password, account name or server address is written in any note or in this repository (NFR-05, ES-17).

**Steps.**

| Step | What is done | Who | Effort |
|---|---|---|---|
| 1. Desk read | Read the official Microsoft page on T-SQL differences for Managed Instance in full. Confirm or correct A-23. Write a one-page design of two or three ways to rebuild the exchange (an outside-the-database step that writes and reads the files; a cloud file store; SQL Server on a virtual machine). Say which one the local proof tests. | Developer from the IT team, reviewed by Ahmed Benali | 0.5 day |
| 2. Legacy baseline | On a **local developer SQL Server** (a throw-away instance on a developer's PC, not `NWSQL01`), load `001-schema.sql` and `002-sample-data.sql`. Add made-up orders for three sample runs (section 2.8). Run the two existing procedures as they are. Keep the output files and their SHA-256 fingerprints. | Developer | 1 day |
| 3. Replacement proof | Build a throw-away replacement that does not use the command-line call or the local-disk bulk load. Run it on the same three samples. Compare each output file with the legacy file, byte by byte. Run the shipment ingest on the same sample `shipments.csv` and compare the final order status and audit rows, row by row. | Developer, Ahmed Benali reviews | 2 days |
| 4. Extra checks (recorded, not counted in the 3 runs) | (a) A day with **zero** confirmed orders: does the legacy job create an empty file? (b) A **replay**: ingest the same shipment file twice. Count the repeated "Shipped" audit rows (A-19, research C4). (c) Run with the clock set to UTC and to CET: does the date in the file name change? (A-10, OPEN-23) | Developer | 0.5 day |
| 5. Antwerp call | One 30-minute call with the Antwerp StockPilot contact: where the file-transfer host is, which account type is used, when the files are picked up and dropped, character set and line ending of `shipments.csv`, whether a file is expected on a day with no orders. Ask for a **sanitised** real example of each file (needs approval, section 2.9). | Ahmed Benali with Pieter Janssens (OPEN-30) | 0.5 day |
| 6. Decide and write up | One-page result against section 2.7. If the proof needs SQL Server on a virtual machine, re-run the cost check (`EN-AZ-12`) with that cost. | Ahmed Benali | 0.5 day |

**Time box.** The build in step 3 stops after 4 working days. If the thresholds are not met by then, the result is "pivot" or "stop", not "extend".

**What this test cannot show.** A pass proves the file contents can be reproduced. It does **not** prove the exchange runs in Azure, and it does not test the Azure file-transfer service. That is tested in the `azure-r2` rehearsal (`EN-AZ-09`, `EN-AZ-14`). A test on a real Azure resource needs explicit approval first (section 2.9).

### 2.5 Participants and owner

| Person | Role in the test | Source |
|---|---|---|
| Ahmed Benali, IT Manager | **Owner** (A-30). Reviews the design and the result. Sets the decision. | (source: business case §5) |
| A developer from the 6-person IT team | Builds the local proof. | (source: C-06) |
| Pieter Janssens, Warehouse Supervisor (Antwerp), and the Antwerp StockPilot contact | Answer the file-transfer questions (OPEN-07, OPEN-30). | (source: business case §5, CS-10) |
| Lena Varga, product owner | Informed. Agrees the effect on the backlog. | (source: business case §5, A-29) |

### 2.6 Duration and effort

About 2 weeks elapsed and about 6 person-days. Proposed window: late November to mid-December 2026, so the result is known well before the `azure-r1` target of end of January 2027 (A-07, A-31).

### 2.7 Success metrics and decision thresholds (all **ASSUMPTION:** A-06, and A-45 for the EUR 1,350 figure in M4; owner Ahmed Benali, confirmed by Lena Varga)

| # | Metric | Persevere (all four needed) | Pivot | Stop |
|---|---|---|---|---|
| M1 | Order file identical to the legacy file on the 3 sample runs (SHA-256 equal) | 3 of 3 identical | 1 or 2 of 3 identical, and every difference traced to a named setting that can be changed inside the time box | 0 of 3 identical, or a difference that only a StockPilot change could remove |
| M2 | Shipment ingest gives the same final status and the same audit rows as the legacy procedure on the 3 sample runs | 3 of 3 the same | Differences traced to a named cause (for example the repeated audit rows, A-19) with a proposed decision record (ES-19) | Cannot reproduce the same statuses |
| M3 | Antwerp details: file-transfer host location, account type, pick-up window and the empty-day rule are named and confirmed **in writing** | All four confirmed | Some confirmed. OPEN-07 stays open for the rest | Antwerp says the files must change (a C-03 conflict) |
| M4 | Server features needed | No command-line call, no local-disk bulk load and **no SQL Server on a virtual machine** | A virtual machine is needed, **and** the re-run cost check (`EN-AZ-12`) shows at least one full option at or under **EUR 1,350 per month** (10 % under the ceiling, C-04, A-45) | A virtual machine is needed and **no** option is at or under EUR 1,350. Escalate to Marc Dubois (OPEN-04) |

**Overall result = the weakest of M1 to M4.** Persevere only if all four are persevere. Stop if any one is stop. Otherwise pivot.

### 2.8 Data to collect

* SHA-256 fingerprint, size and row count of each legacy file and each new file, and a list of every differing byte position.
* Final `Orders.Status` and `OrderAudit` rows after each ingest, legacy and new, side by side.
* The format settings found: separator, line ending, character set, row order, header row, date format.
* Result of the extra checks (empty day, replay, clock).
* Antwerp answers, with date and name of who answered.
* Hours spent per step.

**Sample data.** Made-up only. The three runs:

| Run | Content | Why |
|---|---|---|
| S1 | 5 orders, about 12 lines, standard addresses | The normal case |
| S2 | Orders for customers with accents in the name and address (the sample customers `Épicerie Fine Lumière` and `Hôtel du Parc` already have them), a very long address, and one address that contains a semicolon | Accents depend on the character set. A semicolon would break a `;`-separated file. The legacy job does not quote values (**ASSUMPTION:** A-32). Record what it does. Do **not** fix it in this test, because identical files are the goal. |
| S3 | About 300 orders and 2,000 lines, the size of a normal day (source: CS-05) | Volume and row order |

### 2.9 Risks, ethics and data handling

| Topic | Note |
|---|---|
| EU data (NFR-03) | The proof runs on a local machine in the EU. No cloud service is used. No data leaves the machine. |
| No secrets (NFR-05, ES-17) | No connection string, password or account is written down. The file-transfer account type and host are noted as "held by IT, not in this repository". |
| Production data | Sample data only. A **real** sample file from the live exchange folder would touch production data. **Needs explicit approval from Ahmed Benali before anyone asks for it.** The file is sanitised first (order numbers and addresses replaced) and kept outside this repository. |
| Real Azure resource | **Not part of this experiment.** Nothing is deployed (ES-27). If the owner later wants a real Azure test, for example the Blob bulk load or an Azure file-transfer endpoint, **explicit approval from Ahmed Benali and Marc Dubois is needed first** (cost, ES-27). |
| Local SQL Server setting | The legacy procedure only runs if the command-line call is switched on. Switch it on **only** on the throw-away local instance. Never on any shared or production server. |
| False comfort | A pass does not prove the Azure run works. The `azure-r2` rehearsal still has to prove it. The result note says so. |
| Third-party time | The Antwerp call is a request for a colleague's time. Ahmed Benali arranges it. |

### 2.10 Decision it informs and what happens next

Which stories change (release names; backlog IDs are the PRD baseline, A-26):

| Outcome | What happens in the Azure track | Effect on releases |
|---|---|---|
| **Persevere** | Record the result in `FT-AZ-04` (`azure-r1`). `EN-AZ-09` (`azure-r2`) is built from the proven design. `EN-AZ-14` uses the named Antwerp path. A-23 is confirmed or corrected. | `azure-r1` and `azure-r2` keep their contents. Risk R-02 is lowered. |
| **Pivot** | `EN-AZ-03` (hosting and data decision, `azure-r1`) is reopened with the new constraint. `EN-AZ-12` (cost model) is re-run. `EN-AZ-09` is resized. Differences found are listed as stories for `azure-r2`. | `azure-r1` gains a short re-check. `azure-r2` content and size change. Dates (A-07) are reviewed by Marc Dubois and Lena Varga. |
| **Stop** | The plan "identical files, same cadence, no StockPilot change" is stopped. Lena Varga and Marc Dubois decide the next step. Options include a larger exchange change, asking for a StockPilot change (a C-03 conflict), or a different hosting target. | `azure-r2` is **not** approved until the decision is made. `azure-r1` continues with its other enablers (`EN-AZ-01`, `02`, `04`, `05`, `07`, `12`). |

**The Azure track does not wait for the .NET track.** If the result touches status freshness (BR-04) or a database change in Order Desk, that goes to OPEN-01 and OPEN-20 for the .NET track to read. The Azure track keeps the 02:00 cadence and the identical files until those items are answered (source: ES-31, PRD §8.2).

## 3. `MVE-BA02` — Nightly-fresh status ("as of 02:00") is acceptable to customers

**Business area:** BA-02 Ordering and customer self-service. **Track tag:** `track-dotnet`.

### 3.1 The riskiest assumption and why

**Assumption.** A status view that is only as fresh as the nightly 02:00 update is **enough** for customers. They stop phoning "where is my order?" (source: BR-04, CS-10, C-03, P-03, SM-02, A-04).

**Where the conflict is.** BR-04 says the status is "always up to date". But StockPilot exchanges data once per night, and StockPilot cannot change (source: CS-10, C-03). So Picking and Shipped can only be as fresh as 02:00. Staff update the other statuses by hand during the day (**ASSUMPTION:** A-05, A-22; status source is OPEN-02).

**Why it is the riskiest.** If the assumption is wrong:

* The portal's main value is not reached. Today there are about **410 "where is my order?" calls per week**, roughly 35 % of all inbound calls (source: P-03).
* SM-02 (250 calls or fewer per week) will not move (source: SM-02).
* BR-04 is a **Must**. The team would build it, pilot it with 20 customers in Q2 2027, and learn the answer only when SM-02 is measured, six months after launch (source: business case §8, SM-02).

**Why not the other BA-02 assumptions.** Section 6 lists the others. This one decides whether the main promise of the portal can be kept at all. Most others can be settled by a one-day desk check or must wait for a decision that is still open.

### 3.2 Hypothesis

**If** pilot customers receive a daily status that says "as of 02:00", **then** they will make at least 30 % fewer "where is my order?" calls, and at least 70 % will say the status was enough, **because** most of these calls ask whether an order was received, picked or shipped, and the status can answer that. (**ASSUMPTION:** A-33)

### 3.3 Source IDs

(source: BR-04, BR-10, CS-10, C-03, P-03, SM-02, A-04, A-05, A-33, A-34, OPEN-01, OPEN-02, OPEN-28, OPEN-29)

### 3.4 Cheapest test design

**Rules for this test.** Design and a **manual** pilot. There is no portal, no code and no deployment.

* No change to `src/`, `database/`, `infra/` or Power Platform.
* Staff read order status from the existing Order Desk screens. **Read only.** Nothing is written to Order Desk.
* The e-mails are sent by hand from a named staff mailbox. They do **not** use the internal mail relay (OPEN-18).
* Staff answer every call as normal. A call is never refused or redirected to the e-mail.
* **Real customers are involved. This needs explicit approval (section 3.9) before step 3.**

**The test is a stand-in for the portal status view.** The portal would show the same Order Desk data. Picking and Shipped change only at 02:00. The staff-entered statuses are as fresh as the last staff entry. A status e-mail built from the Order Desk screens at 08:00 shows the same thing (**ASSUMPTION:** A-34). The e-mail tests whether the information is **enough**. It does not test whether customers will sign in to a portal (that belongs to SM-01).

**Steps.**

| Step | What is done | Who | Effort |
|---|---|---|---|
| 1. Desk check (no customers) | Find out whether "where is my order?" calls are already counted by customer and by week (OPEN-28). If not, start a simple tally sheet: date, customer code, reason (status question yes or no). No call content is recorded. Find the top callers. Choose the test group (step 2). | Lena Varga with the Order Desk team lead | 1 day |
| 2. Baseline | Collect **4 weeks** of tally for **all** customers, in total and per customer. If call records already exist, take the last 4 normal weeks from them instead. | Order Desk team | 0.5 day plus tally time |
| 3. Prepare the pilot (approval needed) | Get approval to contact about **10 customers** (OPEN-29). Write a short plain e-mail template with the fixed line "Status as of 02:00 today. Picking and Shipped are updated once per night." (wording set by Lena Varga). Write the 2-question survey. | Lena Varga, with Sofie Peeters for Belgian customers | 1 day |
| 4. Run 2 weeks | Each working day at 08:00, one staff member reads the open orders of each pilot customer in Order Desk and sends one e-mail per customer. Contents: order number, order date, status, nothing else. Staff keep tallying all calls. | One Order Desk staff member | About 30 minutes per day (A-31) |
| 5. Survey | At the end of week 2, ask each pilot customer two questions (section 3.7) by phone or by e-mail reply. | Order Desk team lead | 1 day |
| 6. Analyse and decide | Compare the group's calls in the 2 test weeks with its own 4 baseline weeks. Compare with all other customers over the same weeks. Count survey answers. Write a one-page result. | Lena Varga | 1 day |

**Why a baseline group of heavier callers.** About 410 calls per week for 1,150 customers is about 0.36 calls per customer per week. A random group of 10 would give about 3 to 4 calls per week, so a 30 % change would be about one call and cannot be measured. A group chosen from customers who already call about status gives a baseline that can be measured (A-33). The group is therefore **not typical**. The result is stated for heavier callers only (section 3.9).

**Time box.** If the baseline has fewer than 20 status calls for the group (section 3.7, M1), the call measure is "not evaluable". The survey then decides alone, with the note "low confidence".

### 3.5 Participants and owner

| Person | Role in the test | Source |
|---|---|---|
| Lena Varga, Head of Customer Operations | **Owner** (A-30). Approves contacting customers. Writes the wording. Decides. | (source: business case §5) |
| Order Desk team lead and one staff member (from the 38 staff) | Tally calls, build and send the daily e-mail, run the survey. | (source: CS-03) |
| Sofie Peeters, Key Account Manager (Belgium) | Helps choose and contact Belgian customers. Language advice (OPEN-27). | (source: business case §5, BR-11) |
| Ahmed Benali, IT Manager | Checks the data-protection side of the e-mails (OPEN-29, OPEN-10). Confirms that no system is changed. | (source: business case §5) |
| About 10 customer contacts (grocers, delicatessens, restaurant and hotel kitchens) | Receive the e-mail. Answer the survey. | (source: business case §1, §5) |

### 3.6 Duration and effort

About 8 weeks elapsed: 4 weeks baseline (can run in parallel with step 1 and 3), 1 week to prepare, 2 weeks of daily e-mails, 1 week to survey and analyse. About 8 person-days in total (A-31). Proposed window: baseline in January 2027, test in the first half of February 2027. This avoids the year-end peak and ends well before the `dotnet-r2` pilot start in April 2027 (A-07, A-31). **Difference from the plan.** The plan for this experiment compared the pilot group with its own earlier 2 weeks. This document uses 4 weeks on purpose. Call volume is low (about 410 calls per week for 1,150 customers, or 0.36 calls per customer per week), so 2 weeks would give a group of about 10 customers too few calls to compare (**ASSUMPTION:** A-44).

### 3.7 Success metrics and decision thresholds (all **ASSUMPTION:** A-06; owner Lena Varga, confirmed by Ahmed Benali)

**Call definition.** A "where is my order?" call is any call or e-mail from a customer asking for the status or timing of an existing order (**ASSUMPTION:** A-33).

| # | Metric | Persevere | Pivot | Stop |
|---|---|---|---|---|
| M1 | Calls per customer-week from the pilot group in the 2 test weeks, against the group's own 4 baseline weeks. Valid only if the baseline has **at least 20** status calls for the group | At least **30 % fewer** | **10 % to 29 %** fewer | **Less than 10 %** fewer, or more calls |
| M1c | Control: calls from **all other customers** over the same weeks | Fell by less than 15 % (so the drop is not a seasonal effect) | — | If the others fell by **15 % or more**, M1 is not trusted. Extend the test by 2 weeks and repeat. |
| M2 | Survey question 1: "Was the status in the e-mail enough for you to know where your order is? Yes / Partly / No". At least **8 of 10** must answer | **70 % or more** answer Yes (7 of 10) | **50 % to 69 %** answer Yes | **Under 50 %** answer Yes |
| M3 | Survey question 2: "Is a status that is updated once per night good enough? Yes / No, I need it within the hour / No, I need it the same day" | Under 30 % need it faster (fewer than 3 of 10) | **30 % or more** need it faster. This is a pivot signal even if M1 and M2 pass. | — |

**Overall result = the weakest of M1, M2 and M3.** If M1 is not evaluable, M2 and M3 decide, and the result is marked "low confidence".

### 3.8 Data to collect

* Weekly counts of status calls per customer code, for the group and for all other customers, for 4 baseline weeks and 2 test weeks. No call content, no names.
* Number of e-mails sent, and the staff time spent per day.
* Survey answers to question 1 and question 2, and one optional free-text line.
* Number of times a pilot customer phoned **after** receiving an e-mail, and the reason the customer gave (for example "it said Picking, when will it arrive?").
* Which statuses the e-mails showed. This tells us how many questions were about Picking or Shipped (updated at 02:00) and how many about the staff-entered statuses (A-05, OPEN-02).
* Any customer who asked to stop.

### 3.9 Risks, ethics and data handling

| Topic | Note |
|---|---|
| Real customers | **Needs explicit approval from Lena Varga before any customer is contacted** (OPEN-29). A data-protection check by Ahmed Benali is part of that approval (OPEN-10). Customers are told it is a short trial of a daily status e-mail. They can stop at any time. |
| Service to customers | Staff keep answering calls as normal. A customer who phones is never asked to wait for the e-mail. |
| Data minimisation | The e-mail shows order number, order date and status only. No prices, no addresses, no invoice data. Each e-mail goes only to the customer's own existing contact, about that customer's own orders. |
| EU data (NFR-03) | Order data stays in the Northwind systems and the Northwind mailbox. The tally sheet is kept only in a Northwind location whose data stays in the European Union. The data-protection check in OPEN-29 confirms the location (source: NFR-03). No new tool or outside service is used. |
| No secrets (NFR-05) | No password, key or connection string is needed or written. |
| Not a portal test | The test shows whether the status information is enough. It does not show whether customers will sign in to a portal, or reach the 35 % portal share (SM-01). |
| Not typical customers | The group is chosen from heavier callers (A-33). The result may be stronger or weaker for the other customers. |
| Small group | 10 customers is a small sample. Treat the result as strong evidence for a decision on the build, not as a statistic. The control (M1c) and the survey reduce the risk of a false result. |
| Language | The e-mail is sent in the language the customer normally uses with Northwind. Note which language was used. It informs OPEN-27. |
| Staff effort | The daily e-mail is manual and only possible because the group is small. It is a test, not a service. |

### 3.10 Decision it informs and what happens next

Which stories change (release names; backlog IDs are the PRD baseline, A-26):

| Outcome | What happens in the .NET track | Effect on releases |
|---|---|---|
| **Persevere** | `FT-DN-11` (status "as of the 02:00 batch") is built as written in `dotnet-r2`. Lena Varga can close OPEN-01 as "nightly is acceptable". A-04 is confirmed. The call figures become the starting point for `FT-DN-22` (measure SM-02) in `dotnet-r4`. | `dotnet-r2` and `dotnet-r4` keep their contents. R-04 is lowered. |
| **Pivot** | `FT-DN-11` stays, with added stories: show the time each status last changed, and explain Picking and Shipped in plain words. Lena Varga decides whether to move `FT-DN-21` (Shipped e-mail, BR-09, now Could in `dotnet-r4`) earlier, and whether to split `dotnet-r2` into a read-only slice first (OPEN-26). If M3 shows customers need faster than nightly, raise it under OPEN-01 and OPEN-20. | `dotnet-r2` grows a little. `dotnet-r4` may lose `FT-DN-21` to an earlier release. The decision is Lena Varga's. |
| **Stop** | The promise "status always up to date" (BR-04) cannot be kept with nightly data. Lena Varga and Marc Dubois decide whether the portal pilot leads with status, or with reorder (BR-05) and invoices, and whether the SM-02 target of 250 is still realistic. A faster exchange would need a StockPilot change, which is out of scope (C-03). It is stated as OPEN-20, not as a build item. | `dotnet-r2` is re-ordered or re-sized. The `dotnet-r2` approval waits for Lena Varga's decision. `dotnet-r1` is not affected. |

**The .NET track does not wait for the Azure track.** `dotnet-r1` (modernised Order Desk) goes ahead whatever the result. Only the shape of the status stories in `dotnet-r2` depends on it. A faster refresh would involve the exchange, which the Azure track owns (A-03). That is OPEN-01 and OPEN-20. The Azure track keeps the nightly cadence until those items are answered (source: ES-31, PRD §8.2).

## 4. What these experiments are not

* **They are not implementation.** No code is added to `src/`. No database script is changed. No infrastructure file is written. No story is built because of them.
* **They are not deployments.** Nothing is created in Azure, in Power Platform or in any real environment (ES-27).
* **They do not replace the releases.** Their results change the content or order of some stories. The releases still need the product owner's approval before any Git tag is created (A-29).
* **They do not touch real systems.** The only real-world steps are the Antwerp call, the call-record and customer steps in `MVE-BA02`, and the optional real sample file. All of them need the approvals named in sections 2.9 and 3.9.
* **They do not run in a set order.** `MVE-BA01` and `MVE-BA02` can run at the same time, or one after the other.

## 5. Each track proceeds on its own

* The Azure track starts `azure-r1` whether or not `MVE-BA02` is finished. `MVE-BA02` changes nothing in `azure-r1` or `azure-r2`.
* The .NET track starts `dotnet-r1` whether or not `MVE-BA01` is finished. `MVE-BA01` changes nothing in `dotnet-r1` or `dotnet-r2`.
* **No release waits for the other track** (ES-31). Where one result may matter to the other track, it is written as **OPEN:** and each release states what it does without the answer (A-28):

| Cross-track OPEN item | Why an experiment result can touch it | What each side does without the answer |
|---|---|---|
| OPEN-01 Acceptable freshness for BR-04 (nightly?) | `MVE-BA02` may show that nightly is not enough. The exchange cadence belongs to the Azure track. | `azure-r2` keeps the 02:00 cadence and identical files. `dotnet-r2` shows "as of the 02:00 batch". |
| OPEN-20 StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | `MVE-BA01` may show that shipment date and carrier handling or the repeated audit rows (A-19) need a database change. `MVE-BA02` may ask for a faster refresh. | `azure-r2` assumes no schema change. `dotnet-r2` plans no schema change. Any change goes through a migration-impact check (ES-19). |
| OPEN-18 SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | `MVE-BA02` sends e-mail by hand and does not use the relay. If customers like the e-mail, `FT-DN-21` may move earlier. | `azure-r2` replaces the relay for today's e-mail only. `dotnet-r4` keeps BR-09 as planned. |

## 6. Assumptions considered and not chosen

These are **not** third experiments. Each has a cheaper way to settle it, or a reason it is less risky than the two chosen. (source: research §6, BR-13, C-04, BR-05, OQ-01, SM-01)

| Ref | Assumption | Why not chosen as the MVE | How it is settled instead |
|---|---|---|---|
| A2 | The 48 GB database can be moved and cut over inside the 6-hour Sunday window, with RPO 1 hour and RTO 4 hours | Real and Must (BR-13), but the **rehearsal** is already planned in `azure-r2`, and one spare Sunday is kept before 30 June 2027 (A-07). The cost of being wrong is a re-run, not a silent failure. | A desk calculation of upload time from Lyon at the start of `EN-AZ-08` (success mark in A-06: 3 hours or less, which leaves half the window to check and roll back). Then the rehearsal. |
| A3 | Production plus one test environment, with private endpoints, backup and monitoring, fits EUR 1,500 per month | Important, but it is an estimate, not an experiment. It takes about a day with the Azure pricing calculator. | `EN-AZ-12` in `azure-r1`: compare 3 options (managed database, database service, SQL on a virtual machine). Success mark in A-06: one option at or under EUR 1,350 (threshold: A-45). **Run it first.** `MVE-BA01` re-runs it if a virtual machine is needed. Owner of the ceiling is OPEN-04. |
| A4 | The legacy app can run on the target platform with a configuration-only change until the .NET track delivers | If false, `azure-r2` would depend on a .NET release. That is not allowed (ES-31). It is a question of **who owns the code change**, not a test. | OPEN-03. Meanwhile `azure-r1` lists, read-only, the points where the current app would break on the new platform (PRD §8.1). |
| B2 | 70 % of orders repeat a previous order with small changes, so copy and edit (BR-05) is the right first order feature | The 70 % has no data source in the business case (P-04). But BR-05 stays a Must even if the real figure is lower. It only needs a read-only database query. | A one-off read-only query by Ahmed Benali on the last 12 months of order lines. Success mark in A-06: at least 60 % of orders have at least 70 % of lines from the customer's previous order. No build. |
| B3 | Customers accept the chosen sign-in method, and a customer administrator can manage users (BR-01, BR-08) | Cannot be tested before the sign-in choice is made (OPEN-13). Testing a mock of an undecided option wastes effort. | After `EN-DN-11` records the choice: a clickable mock with 5 to 8 pilot customers, counting how many finish unaided. Part of `dotnet-r2`, not before. |
| B4 | The 20-customer pilot reaches enough orders to learn from (SM-01) | **ASSUMPTION:** A-46: 35 % of all orders is not expected to come from 20 of about 1,150 customers (R-11). It depends on how many orders the pilot customers place, and no source gives that. | OPEN-05 (meaning of "portal launch"; order volume of the pilot customers). A desk calculation using the order query from B2. |

## 7. Results

No experiment has been run. When an owner runs one, they add the date, the measured values against the thresholds in sections 2.7 and 3.7, the overall result (persevere, pivot or stop), and the decision, to this section, and tell the product owner. Until then:

| MVE | Run on | Result | Decision | Recorded by |
|---|---|---|---|---|
| `MVE-BA01` | Not run | — | — | — |
| `MVE-BA02` | Not run | — | — | — |

## 8. Assumptions (ES-03)

Every assumption has a person who can confirm it. Wording is identical in every product document. The master register is in `docs/product/README.md`. Entries not used by this document are in the master register only.

| ID | ASSUMPTION | Owner who can confirm |
|---|---|---|
| A-03 | The .NET track owns Order Desk code modernisation; the Azure track owns hosting, data and the exchange | Ahmed Benali |
| A-04 | BR-04 stories state "as of the 02:00 batch" freshness | Lena Varga |
| A-05 | Confirmed, Delivered and Cancelled are manual staff actions today | Order Desk team via Lena Varga |
| A-06 | Experiment success thresholds and pivots in `experiments.md` | Lena Varga, Ahmed Benali |
| A-07 | Release target dates (azure-r1 end Jan 2027; azure-r2 rehearsal by end Apr, cutover May 2027; azure-r3 by 30 Jun 2027; dotnet-r1 end Feb 2027; dotnet-r2 pilot start Apr 2027; dotnet-r3, dotnet-r4 not dated) | Marc Dubois, Lena Varga |
| A-09 | The cost model assumes SQL and private endpoints are the main spend | Ahmed Benali |
| A-10 | Time zone behaviour on Azure may differ from the Lyon servers (UTC vs CET) | Ahmed Benali |
| A-16 | These drafts are discovery outputs, not approved for build | Lena Varga |
| A-19 | The import's repeated "Shipped" audit rows (research C4) are unintended; the exchange redesign decides to keep or fix them, with a decision record (ES-19) | Ahmed Benali |
| A-22 | Code and database findings from the research (C1 to C17, read from `src/` and `database/` on 2026-10-30) are not in `knowledge-docs`. They are used here only to explain risk. They include: no limit of data to the signed-in customer's company (C5), invoice folder year follows the order date (C7), no mail-sending code (C14), and English-only screens (C15) | Ahmed Benali |
| A-23 | The StockPilot exchange is built on database-server features (command-line calls and a local-disk bulk load) that Azure SQL Managed Instance does not offer. The source is a search summary of the official Microsoft page (research W1), not the page itself, so it must be confirmed before a hosting decision | Ahmed Benali |
| A-24 | The people named as owners of OPEN items (BRD section 5) are proposals taken from the stakeholder list; Lena Varga, as backlog owner, confirms them | Lena Varga |
| A-25 | Risk likelihood and impact ratings in BRD section 13 are judgements for discussion and not figures from the business case | Lena Varga |
| A-26 | The feature IDs `FT-AZ-01`..`FT-AZ-11` and `FT-DN-01`..`FT-DN-25` in PRD section 5 are the baseline for `backlog.md`. The backlog reuses them, may add new numbers, and never renumbers. The unplanned parent epic `EP-DN-08` is a proposed name | Lena Varga |
| A-28 | The "what this release does without the answer" position stated for each cross-track OPEN item (`backlog.md` section 8, PRD section 10 and section 7.2 of each release file) is the working position until the person who can answer decides | Lena Varga, Ahmed Benali |
| A-29 | Lena Varga, who owns the product backlog, acts as product owner and approves each release before its Git tag `product/<track>-r<n>` is created | Marc Dubois |
| A-30 | The owner of `MVE-BA01` is Ahmed Benali and the owner of `MVE-BA02` is Lena Varga. The owner runs the test, records the result and proposes the decision. The product owner agrees any change to the backlog | Lena Varga |
| A-31 | The elapsed times, effort in person-days, group size of about 10 customers, daily staff time of about 30 minutes and proposed run windows (late November to mid-December 2026 for `MVE-BA01`; January to February 2027 for `MVE-BA02`) are planning estimates. The owners set the real dates. The year-end is assumed to be a busy period for customers | Lena Varga, Ahmed Benali |
| A-32 | The format of the exchange files is taken from reading `database/003-stockpilot-exchange.sql` and from how the command-line tool normally behaves, not from a real file. Assumed: the order file uses `;` as separator, has no header row, does not put quotes around values, uses the database server's default character set, and has no defined row order. The shipment file has a header row and `;` as separator. Real files from Antwerp may differ | Ahmed Benali |
| A-33 | "Where is my order?" calls are unevenly spread across customers, so a group of about 10 heavier callers gives a baseline that can be measured. Most of these calls ask whether an order was received, picked or shipped. The call reasons are not recorded in the business case | Lena Varga |
| A-34 | A status e-mail built by hand from the Order Desk screens at 08:00 is a fair stand-in for the portal status view for this test: the portal would show the same data with the same 02:00 freshness for Picking and Shipped | Lena Varga |
| A-44 | `MVE-BA02` compares the pilot group's calls with its own earlier 4 weeks, not the 2 weeks first planned. Call volume is low (about 0.36 calls per customer per week), so 2 weeks would give too few calls to compare | Lena Varga |
| A-45 | The cost "at risk" threshold is EUR 1,350 per month, 10 % under the EUR 1,500 ceiling (C-04). A full option above it is flagged "at risk" | Lena Varga, Ahmed Benali |
| A-46 | A 35 % portal share of orders (SM-01) is not expected to be reached with a pilot of 20 customers out of about 1,150. This is a judgement, not a fact: it depends on how many orders the pilot customers place, which is not in `knowledge-docs` (OPEN-05) | Lena Varga |

## 9. OPEN items (ES-04)

Wording is identical in every product document. Items marked "Azure and .NET" are cross-track. None is a blocker for this document, and none is a prerequisite for a release.

| ID | OPEN question or dependency | Person who can answer | Track(s) affected |
|---|---|---|---|
| OPEN-01 | Acceptable freshness for BR-04 (nightly?) | Lena Varga | .NET, Azure (exchange) |
| OPEN-02 | Source of Confirmed, Delivered, Cancelled status | Lena Varga with the Order Desk team | .NET |
| OPEN-03 | Who modernises Order Desk code (CS-13..CS-17, .NET 10, staff Entra sign-in) | Ahmed Benali with Lena Varga | Azure and .NET |
| OPEN-04 | Accountable owner and split of the EUR 1,500 ceiling | Marc Dubois | Azure and .NET |
| OPEN-05 | Meaning of "portal launch"; does the pilot run on Azure before 30 June 2027; how many orders do the 20 pilot customers place (decides whether SM-01 can be shown) | Marc Dubois, Lena Varga | Azure and .NET |
| OPEN-07 | Network path from Azure to Antwerp and the SFTP host location | Ahmed Benali with Pieter Janssens | Azure |
| OPEN-10 | Data-protection requirement for customer users (Ahmed Benali); mobile expectations (Sofie Peeters) | Ahmed Benali, Sofie Peeters | .NET |
| OPEN-13 | Customer identity provider vs the Entra tenant and platform sign-in plumbing (business case OQ-01) | Ahmed Benali | Azure and .NET |
| OPEN-18 | SMTP relay replacement (azure) vs BR-09 and confirmation e-mail; who sends today (no mail code in `src/`) | Ahmed Benali | Azure and .NET |
| OPEN-20 | StockPilot exchange redesign vs BR-04 freshness and any .NET schema change (migration-impact check) | Lena Varga (freshness), Ahmed Benali (schema) | Azure and .NET |
| OPEN-23 | Time zone and clock for batch times, order dates, audit | Ahmed Benali | Azure and .NET |
| OPEN-26 | Split `dotnet-r2` into a read-only slice and a reorder slice? | Lena Varga | .NET |
| OPEN-27 | Which language do pilot customers see in `dotnet-r2`, because French and English (BR-11) are planned for `dotnet-r3`? Option: pull BR-11 into `dotnet-r2` | Lena Varga with Sofie Peeters | .NET |
| OPEN-28 | Are "where is my order?" calls already counted by customer and by week (phone system or Order Desk records)? If not, who keeps the 4-week tally for `MVE-BA02`? | Lena Varga | .NET |
| OPEN-29 | Which about 10 customers take part in `MVE-BA02`, who approves contacting them, and is a data-protection or consent step needed before sending a trial status e-mail? | Lena Varga with Sofie Peeters; data-protection check by Ahmed Benali | .NET |
| OPEN-30 | Who in Antwerp (Pieter Janssens or the StockPilot contact) can confirm the file-transfer host, account type, pick-up window, file format and empty-day rule, and can provide a sanitised real example of `orders_YYYYMMDD.csv` and `shipments.csv`? Who approves taking a copy from the live folder? | Ahmed Benali with Pieter Janssens | Azure |

Business-case open questions kept in scope: OQ-01 is OPEN-13. OQ-04 and OQ-05 belong to BA-03 and are out of scope.
