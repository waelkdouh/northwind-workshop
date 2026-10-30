---
description: "Squad consumption ledger: members, models, estimated tokens, cost, and AI credits"
---

# Squad Consumption Ledger (Run: nw-product-docs)

## Attribution

| Role | Member | Agent | Model | Model Source | Priced As | Tier |
| ---- | ------ | ----- | ----- | ------------ | --------- | ---- |
| researcher |  | Squad Researcher | claude-sonnet-5.5 | host-reported | native credits | default |
| lead |  | Squad Lead | claude-sonnet-5.5 | host-reported | native credits | default |
| tester |  | Squad Reviewer | claude-haiku-5.5 | host-reported | native credits | fast |
| analyst |  | BRD Builder | claude-sonnet-5.5 | host-reported | native credits | default |
| analyst |  | PRD Builder | claude-sonnet-5.5 | host-reported | native credits | default |
| product-owner |  | Functional Planner | claude-sonnet-5.5 | host-reported | native credits | default |
| experimenter |  | Experiment Designer | claude-sonnet-5.5 | host-reported | native credits | default |
| intake-validator |  | BRD Quality Reviewer | claude-sonnet-5.5 | host-reported | native credits | default |
| orchestration |  | Coordinator+Scribe | claude-sonnet-5.5 | host-reported | native credits | mixed |

## Usage & Cost

| Role | Requests | In Tokens | Cached | Cache Wr | Out Tokens | Exact Cost (USD) | Exact Credits | Basis |
| ---- | -------- | --------- | ------ | -------- | ---------- | ---------------- | ------------- | ----- |
| researcher | 16 | 36 | 1,649,093 | 175,039 | 60,625 | 1.2088 | 120.88 | exact-native |
| lead | 13 | 30 | 1,159,342 | 160,404 | 28,066 | 0.7977 | 79.77 | exact-native |
| tester | 208 | 422 | 42,784,576 | 975,791 | 339,583 | 3.3581 | 335.81 | exact-native |
| analyst | 8 | 18 | 860,080 | 110,060 | 27,728 | 0.6385 | 63.85 | exact-native |
| analyst | 21 | 44 | 2,293,713 | 314,384 | 52,802 | 1.5434 | 154.34 | exact-native |
| product-owner | 446 | 910 | 68,696,773 | 1,882,016 | 671,219 | 18.2887 | 1828.87 | exact-native |
| experimenter | 16 | 34 | 1,843,106 | 154,012 | 44,187 | 1.0113 | 101.13 | exact-native |
| intake-validator | 3 | 8 | 21,692 | 16,559 | 10,165 | 0.1452 | 14.52 | exact-native |
| orchestration | 101 | 208 | 13,057,335 | 3,828,828 | 59,742 | 11.4756 | 1147.56 | exact-native |
| **Total** | **832** | **1,710** | **132,365,710** | **7,617,093** | **1,294,117** | **38.4674** | **3846.74** | **exact-native** |

### Derivation

```text
BRD Builder.md — 1 block(s) — identities: 07b2ae3d
BRD Quality Reviewer.md — 1 block(s) — identities: 9541aff7
Experiment Designer.md — 1 block(s) — identities: 41d6b3fa
Functional Planner.md — 9 block(s) — identities: 8ce5959b,f73bc8d3,f3acae17,7b6a6fc2,f6508479,fc657cee,23dd411f,5d4cc46a,a435a4b4
PRD Builder.md — 1 block(s) — identities: 7145562f
Squad Lead.md — 1 block(s) — identities: 95906182
Squad Researcher.md — 1 block(s) — identities: 99238007
Squad Reviewer.md — 2 block(s) — identities: 366b0317,869a6798
Squad Scribe.md — 18 block(s) — identities: 8beb1013,eb24d5dc,245ff74a,7ce9dd37,7e6e9c87,fa35f720,ec24f937,f2541f50,98457dac,27cff3d8,cb3dd274,45ff8fe1,2bfedde6,c6baa259,04546ee0,9cf8234d,2265564c,d2e2cad2
Native usage snapshots — sessions: 2; records: 832; through: 2026-10-30T19:50:42.260Z; digest: CCF3CC52688C9A58EBC984934B69E89862C6024D86A839D058181219180FF566
researcher         requests 16     input 36         cached 1649093    cache-write 175039     output 60625      nano-AIU 120882880000 = 120.88 credits / 1.2088 USD
lead               requests 13     input 30         cached 1159342    cache-write 160404     output 28066      nano-AIU 79766420000 = 79.77 credits / 0.7977 USD
tester             requests 208    input 422        cached 42784576   cache-write 975791     output 339583     nano-AIU 335814659500 = 335.81 credits / 3.3581 USD
analyst            requests 8      input 18         cached 860080     cache-write 110060     output 27728      nano-AIU 63847400000 = 63.85 credits / 0.6385 USD
analyst            requests 21     input 44         cached 2293713    cache-write 314384     output 52802      nano-AIU 154343930000 = 154.34 credits / 1.5434 USD
product-owner      requests 446    input 910        cached 68696773   cache-write 1882016    output 671219     nano-AIU 1828872730000 = 1828.87 credits / 18.2887 USD
experimenter       requests 16     input 34         cached 1843106    cache-write 154012     output 44187      nano-AIU 101127860000 = 101.13 credits / 1.0113 USD
intake-validator   requests 3      input 8          cached 21692      cache-write 16559      output 10165      nano-AIU 14523270000 = 14.52 credits / 0.1452 USD
orchestration      requests 101    input 208        cached 13057335   cache-write 3828828    output 59742      nano-AIU 1147563950000.0 = 1147.56 credits / 11.4756 USD
total nano-AIU 3846743099500 = 3846.74 credits / 38.4674 USD
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
| Deliverables produced | 11 | derived |
| Accepted by an independent review | 0 | derived |
| Rejected | 0 | derived |
| Unreviewed | 11 | derived |
| Dispatches (excluding Scribe) | 17 | derived |
| Rework dispatches | 4 | derived |
| First-pass yield | n/a | derived |
| Exact credits per accepted deliverable | n/a | measured |
| Rework share of exact credits | n/a | unavailable without per-history-run identity |
| Orchestration share of exact credits | 29.8% | measured |

Value is counted only for deliverables an independent review-class verdict accepted; a produced but unaccepted deliverable adds cost and no value. A review that names deliverables covers only those it names. Rework counts a repeat of the same agent and deliverable path only: a fix by a different agent, to a different file, or with no deliverable path is not counted, so the rework figures are a floor. Compare runs only for like work, using medians of several runs. Source: FinOps Foundation unit-economics KPIs (cost per unit of value, error and retry waste).

## Cost Comparison (exact native actual)

| Scenario | Basis | AI Credits | USD |
| -------- | ----- | ----------: | --: |
| With HVE Squad through 2026-10-30T19:50:42.260Z | complete deduplicated native records; coordinator and descendants included | 3846.74 | 38.4674 |
| Without HVE Squad: same exact role-request token categories on `claude-sonnet-5.5`, no coordinator or Scribe | calculated counterfactual from exact request tokens | 3374.83 | 33.7483 |

HVE Squad is **4.7192 USD (14.0%) higher** than the same exact role traffic on `claude-sonnet-5.5`.

> The HVE Squad row is exact as of 2 accumulated native session snapshots: 832 complete accounting records, cumulative digest `CCF3CC52688C9A58EBC984934B69E89862C6024D86A839D058181219180FF566`. The without-Squad row is not an observed alternate run; it holds every exact role request's uncached input, cache read, cache write, and output counts constant, reprices them on one model, and excludes coordinator/Scribe overhead. It therefore measures routing savings on identical traffic and does not invent context growth, rework, or behavioral differences for a hypothetical manual run.
