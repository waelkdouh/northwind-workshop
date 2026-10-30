# Intake validation: BA-01 and BA-02

**Verdict: Ready-With-Gaps.** I found 0 blocking gaps and 16 non-blocking gaps (G-01 to G-16). Each can be carried as an `ASSUMPTION:` or `OPEN:` item under ES-03, ES-04 and ES-31.

**I did not write the review file.** My tools here are read-only (`view`, `grep`, `glob`), and my instructions forbid creating or editing files. The review below is ready to save as `C:\demos\northwind-workshop\.copilot-tracking\reviews\intake-validation-ba01-ba02.md`. Please have an agent with write access do that.

- **Model identity:** I can't verify this from inside the session, so I won't state one.
- **Tool calls:** 5, all `view`. That was three initial reads, plus two ranged re-reads of `business-case.md` because it was too large to read at once.
- **Paths written:** none.
- **BRD payloads:** `BRD_STANDARD_FINDINGS_V1` and `BRD_QUALITY_REPORT_V1` were not produced, because there is no BRD draft to grade yet.

## Scope boundary

| Area | Status | Identifiers (business case §4) |
|---|---|---|
| BA-01 Platform and data-centre exit (`track-azure`) | In scope | BR-13, NFR-01, NFR-03, NFR-05, NFR-06, C-01 to C-04, C-06, SM-07 |
| BA-02 Ordering and customer self-service (`track-dotnet`) | In scope | BR-01 to BR-12, NFR-02, NFR-04, NFR-05, NFR-07, NFR-08, C-05, SM-01 to SM-04 |
| BA-03 Delivery claims and credit notes (`track-power-platform`) | **Out of scope** | BR-14 to BR-19, NFR-09, C-07, C-08, SM-05, SM-06 |

- **Coverage:** every BR-01 to BR-19 and NFR-01 to NFR-09 is assigned to at least one area, so the ES-06 traceability table can be built.
- **Shared requirements:** NFR-03, NFR-04 and NFR-05 are shared across areas (G-03). NFR-03 and NFR-04 are also in BA-03's list.
- **Out-of-scope items (§6):** online payment, a native mobile app, changes to StockPilot, replacing the finance system, and customer-recorded claims.

## Assessment by dimension

- **Completeness:** Strong. Every requirement has an ID and a MoSCoW priority, except NFRs and constraints, which have none. Current-state facts have IDs. Gaps are listed in G-01 to G-16.
- **Clarity:** Good overall. The unclear items are BR-04 "always up to date" and the "Order Desk upgrade" boundary between the two tracks.
- **Testability:** Most BRs can be turned into Given/When/Then. The weak ones are BR-04, NFR-01 (measurement method), NFR-02 (load basis) and SM-01.
- **Consistency:** One real conflict, BR-04 against CS-10 and the StockPilot constraint. There are also overlaps between the tracks and a timeline tension.
- **Scope boundaries:** Clear at area level. They need confirming for Order Desk modernisation, cost and the shared NFRs.

## Blocking gaps

None. Nothing prevents drafting the BRD, PRD, MVEs, backlog, releases or traceability table. The conflicts below can be drafted around with explicit `OPEN:` items, which ES-31 expects for cross-track dependencies.

## Non-blocking gaps (carry as ASSUMPTION: or OPEN:)

| ID | Gap | Source | Carry as |
|---|---|---|---|
| G-01 | **BR-04 conflicts with the current state.** BR-04 says status is "always up to date". Picking and Shipped only update once a night (CS-10), and StockPilot changes are out of scope (§6, C-03). "Always up to date" has no measurable freshness. | BR-04, CS-10, C-03 | `OPEN:` What freshness is acceptable (for example, as of the 02:00 batch)? Draft BR-04 stories with the nightly freshness as an `ASSUMPTION:`. |
| G-02 | **No source for the "Delivered" status.** CS-10 only mentions Picking and Shipped from StockPilot. Where Delivered, Confirmed and Cancelled come from is not stated. | BR-04, CS-10 | `OPEN:` Status-to-source mapping. |
| G-03 | **Shared NFRs across tracks.** NFR-05 is in both BA-01 and BA-02, so ES-30 forces one story per track. NFR-03 is in BA-01 but not BA-02, although the portal stores EU customer data. | §4 note, ES-30, ES-06 | `ASSUMPTION:` NFR-03, NFR-04 and NFR-05 are cross-cutting. Split stories per track and show both in the traceability table. |
| G-04 | **Order Desk modernisation boundary.** BA-01 means "run Order Desk in Azure" and the timeline says "lift and modernise". BA-02 includes "the upgrade of Order Desk that the portal depends on". Who fixes CS-13 to CS-17 (SSPI, UNC path, Event Log, InProc session, ConfigurationManager) and moves to .NET 10 (ES-14 to ES-19) is unassigned. The same applies to staff sign-in moving from Windows Integrated Authentication (CS-04) to Entra ID (NFR-04, BA-02). | §4, CS-04, CS-13 to CS-17 | `OPEN:` Track ownership, written as a cross-track dependency in each release (ES-31). Neither track may wait for the other. |
| G-05 | **Owners for OQ-01 to OQ-05 are not named.** ES-04 requires a person for each. | §7, ES-04 | `ASSUMPTION:` Proposed owners are in the table below. |
| G-06 | **Cost allocation.** C-04 (EUR 1,500 per month) is owned by BA-01 but covers the portal, which belongs to BA-02. | C-04, §4 | `ASSUMPTION:` The budget is shared. `OPEN:` Who is accountable? |
| G-07 | **Timeline tension.** The portal pilot is in Q2 2027, which ends 30 June 2027, the same day as the lease end (C-01). The portal depends on the upgraded Order Desk. Whether the pilot runs on Azure is unclear. | §8, C-01, C-05 | `OPEN:` Target dates per release. Release sequencing is an assumption. |
| G-08 | **SM-01 definition.** A 35 % portal share of orders is not reachable with a 20-customer pilot out of 1,150 customers. "Portal launch" is not defined. | SM-01, §8 | `OPEN:` Does launch mean pilot or general availability? |
| G-09 | **Items with no BR or NFR that the move needs:** the SMTP relay (CS-12), the invoice share (CS-08, CS-11), monitoring (CS-22), the untested disaster recovery (CS-23) and the build and deploy pipeline (CS-19). The finance system writes to `\\NWFS01\invoices`, so that write target changes after the exit, and the finance system is out of scope. | CS-08, CS-11, CS-12, CS-19, CS-22, CS-23 | `ASSUMPTION:` These become enabler stories tagged by track, with sources cited. `OPEN:` The Finance dependency, with Julien Moreau. |
| G-10 | **StockPilot connectivity after the exit.** The SFTP server's location and where the 02:00 job runs are not stated. The Lyon to Antwerp VPN (CS-09) disappears with the data centre. | CS-09, CS-10, C-03 | `OPEN:` Network path from Azure to Antwerp and the SFTP host. |
| G-11 | **NFR measurability.** NFR-01 has no measurement method or scope (Order Desk only, or the portal too). NFR-02 has no load profile; CS-03 gives 60 staff users, but the number of portal users is unknown. NFR-08 does not say how audit history is retained or retrieved. NFR-01 to NFR-09 have no priority. | NFR-01, NFR-02, NFR-08 | `ASSUMPTION:` Measurement basis and priorities. Product owner to confirm. |
| G-12 | **Data completeness.** BR-02 needs 24 months of orders (not confirmed in the database). BR-07 needs a link from an order to an invoice number (CS-11). Neither mapping is stated. | BR-02, BR-07, CS-11 | `OPEN:` Both. |
| G-13 | **Implied requirements with no identifier.** Sofie Peeters asks for mobile access. §6 says a responsive web portal is enough. No supported browsers or devices are stated. There is no data-protection requirement for customer users. | §5, §6 | `ASSUMPTION:` Responsive web, current browsers. Data protection is `OPEN:` with Ahmed Benali. |
| G-14 | **Release naming and publishing tool.** The `.NET` release tag form is inferred as `dotnet-r1` from ES-31. "First release" in §6 is not mapped to specific tracks. The publishing tool is unnamed, and ES-28 only applies to Azure DevOps and is optional. | ES-30, ES-31, ES-39 | `ASSUMPTION:` `dotnet-r<n>` and `azure-r<n>`. `OPEN:` Backlog tool. |
| G-15 | **Identifier mismatch.** The business case uses `C-01` to `C-08` for constraints, not `CON-###`. | §3.3, ES-21 | `ASSUMPTION:` Keep `C-` identifiers in the BRD and map them to the constraint category. |
| G-16 | **Document status and unconfirmed facts.** The status is "Approved for discovery. Not yet approved for build." SM-07 counts 2 servers, but the OS of the file-share host (NWFS01) is not stated. | Header, SM-07, CS-08 | `ASSUMPTION:` The drafts are discovery outputs. `OPEN:` The NWFS01 OS and whether it counts toward SM-07. |

## Open questions OQ-01 to OQ-05

Carry all five as `OPEN:` items, not blockers. The owners below are my proposals, taken from the stakeholder list. They are `ASSUMPTION:` items for the product owner to confirm.

| ID | Question | Proposed owner | Scope |
|---|---|---|---|
| OQ-01 | Identity provider for customer users | Ahmed Benali | BA-02. Affects BR-01, BR-08 and NFR-04. |
| OQ-02 | Dutch in the first release (BR-11) | Sofie Peeters, with Lena Varga | BA-02 |
| OQ-03 | Customer administrators for all customers or only large ones (BR-08) | Lena Varga | BA-02 |
| OQ-04 | Who approves claims of EUR 500 or less (BR-15) | Julien Moreau | **BA-03, out of scope.** Carry as an informational `OPEN:` only. |
| OQ-05 | Migrate existing spreadsheet claims | Lena Varga | **BA-03, out of scope.** Carry as an informational `OPEN:` only. |

## Clarifying questions

1. **BR-04 freshness (G-01):** can Lena Varga accept the nightly freshness for Picking and Shipped, or must it be faster? Faster would need a StockPilot change, which is out of scope.
2. **Order Desk upgrade ownership (G-04):** which track owns the work on CS-13 to CS-17, the .NET 10 move and staff sign-in through Entra ID?
3. **Launch definition (G-07, G-08):** does "portal launch" mean the 20-customer pilot or general availability? Will the pilot run on Azure before 30 June 2027?
4. **Finance dependency (G-09):** can Julien Moreau confirm how the finance system's invoice output will reach Azure?
5. **StockPilot connectivity (G-10):** who can describe the post-exit network path to Antwerp and the SFTP server location?
6. **Backlog tool and release names (G-14):** which tool will the backlog be published to (Azure DevOps, GitHub or Jira)? Is `dotnet-r1` the intended release tag?
7. **Cost ownership (G-06):** who is accountable for the EUR 1,500 per month ceiling that covers both tracks?