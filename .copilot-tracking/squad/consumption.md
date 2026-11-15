---
description: "Squad consumption ledger: members, models, estimated tokens, cost, and AI credits"
---

# Squad Consumption Ledger (Run: northwind-planning-init-20261115)

## Attribution

| Role | Member | Agent | Model | Model Source | Priced As | Tier |
| ---- | ------ | ----- | ----- | ------------ | --------- | ---- |
| orchestration |  | Squad Scribe | unknown | unresolved | Claude Sonnet 4.6 | mixed |

## Usage & Cost

| Role | Turns | In Tokens | Cached | Cache Wr | Out Tokens | Est. Cost (USD) | Est. Credits | Basis |
| ---- | ----- | --------- | ------ | -------- | ---------- | ---------------- | ------------ | ----- |
| orchestration | 4 | 15,600 | 62,400 | 24,000 | 3,200 | 0.2035 | 20.35 | tier-default |
| **Total** | **4** | **15,600** | **62,400** | **24,000** | **3,200** | **0.2035** | **20.35** | |

### Derivation

```text
Squad Scribe.md — 1 block(s) — identities: 5695bf00
orchestration  turns 4            15600 × 3.00 + 62400 × 0.30 + 24000 × 3.75 + 3200 × 15.00 = 203520 / 1e6 = 0.2035
                                                                                        total = 0.2035
```

> This is the initialization and fallback shape. Exact mode replaces `Turns` with
> `Requests`, `Est. Cost` / `Est. Credits` with `Exact Cost` / `Exact Credits`, and
> every row's basis with `exact-native`. Its input column is uncached billed input;
> cache read and cache write remain separate, so the four token columns are
> disjoint and reproduce native token-detail charges. The exact Attribution table
> uses `host-reported` and `native credits`; fallback Attribution preserves the
> existing model-source ladder. 1 AI credit = 0.01 USD.
>
> The `<file>.md — <n> block(s) — identities: <hash>,<hash>,...` line uses the history file's basename, without a `history/` prefix. It is the ledger's own record of which `###` entries it has already folded in, one short deterministic hash per entry in file order. The initial Scribe-only seed records an empty prefix; the first ledger write replaces it with actual identities. A rewrite that finds this run's recorded identities are not an ordered prefix of the file's current identities — same count but different hashes, or fewer current entries than recorded — means an entry was overwritten, reordered, or removed since the last rewrite rather than only appended to, and `Measure-SquadLedger.ps1 -Check` (or render mode) refuses rather than silently accepting it. A pre-existing ledger with no recorded identities at all (an older-format entry) only warns when checked plainly; it never fails on that account alone. But the Scribe's own post-write self-check always runs `-Check` together with `-ExpectedHistoryCounts` (*scribe-procedure.md*'s Write-Completeness Self-Check Step 3), and in that combination a Derivation missing identities entirely, or missing them for only some of the touched files (a partial paste), FAILS instead of warning — that call always follows a fresh write, so a missing or partial paste there is this run's own defect, never a genuinely old ledger.

## Unit Economics (value)

| Measure | Value | Label |
| ------- | ----- | ----- |
| Deliverables produced | 0 | derived |
| Accepted by an independent review | 0 | derived |
| Rejected | 0 | derived |
| Unreviewed | 0 | derived |
| Dispatches (excluding Scribe) | 0 | derived |
| Rework dispatches | 0 | derived |
| First-pass yield | n/a | derived |
| Est. credits per accepted deliverable | n/a | estimated |
| Rework share of est. credits | 0.0% | estimated |
| Orchestration share of est. credits | 100.0% | estimated |

Value is counted only for deliverables an independent review-class verdict accepted; a produced but unaccepted deliverable adds cost and no value. A review that names deliverables covers only those it names. Rework counts a repeat of the same agent and deliverable path only: a fix by a different agent, to a different file, or with no deliverable path is not counted, so the rework figures are a floor. Compare runs only for like work, using medians of several runs. Source: FinOps Foundation unit-economics KPIs (cost per unit of value, error and retry waste).

## Cost Comparison (illustrative)

n/a (initialization). Setup spend is recorded above using the ledger basis; the first comparison follows the first work dispatch.
