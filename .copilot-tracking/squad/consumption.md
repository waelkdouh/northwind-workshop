---
description: "Squad consumption ledger: members, models, estimated tokens, cost, and AI credits"
---

# Squad Consumption Ledger (Run: run-01)

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
| researcher | 14 | 32 | 1,440,041 | 182,879 | 65,769 | 1.2590 | 125.90 | exact-native |
| lead | 12 | 28 | 1,172,962 | 148,136 | 60,436 | 1.0921 | 109.21 | exact-native |
| tester | 96 | 198 | 17,852,814 | 670,414 | 273,498 | 1.8531 | 185.31 | exact-native |
| analyst | 14 | 32 | 1,585,168 | 142,951 | 40,618 | 0.9221 | 92.21 | exact-native |
| analyst | 102 | 212 | 22,134,773 | 889,807 | 193,887 | 6.3773 | 637.73 | exact-native |
| product-owner | 191 | 400 | 39,508,410 | 1,455,670 | 409,146 | 11.6823 | 1168.23 | exact-native |
| experimenter | 21 | 46 | 2,708,702 | 166,596 | 56,197 | 1.2494 | 124.94 | exact-native |
| intake-validator | 5 | 12 | 92,781 | 33,270 | 19,390 | 0.2864 | 28.64 | exact-native |
| orchestration | 79 | 166 | 10,704,208 | 1,424,138 | 61,687 | 5.2480 | 524.80 | exact-native |
| **Total** | **534** | **1,126** | **97,199,859** | **5,113,861** | **1,180,628** | **29.9696** | **2996.96** | **exact-native** |

### Derivation

```text
BRD Builder.md — 1 block(s) — identities: 5ecac769
BRD Quality Reviewer.md — 1 block(s) — identities: 9f4fbbb4
Experiment Designer.md — 1 block(s) — identities: 632a1fc9
Functional Planner.md — 5 block(s) — identities: 40f320b2,e71a6f24,fa5bd952,1a82c8fe,52ba32dd
PRD Builder.md — 2 block(s) — identities: 0c6a9778,96aeecf5
Squad Lead.md — 1 block(s) — identities: a3fe076e
Squad Researcher.md — 1 block(s) — identities: f0a8d5c3
Squad Reviewer.md — 2 block(s) — identities: a5f100fc,2330e5e8
Squad Scribe.md — 15 block(s) — identities: 5695bf00,9fe78ae7,cad0fee0,12dbd414,6ca2c06a,69f5d967,53612311,547e9950,7ba42eff,93002d50,eb329bc8,ff2c01c7,78dad352,a45f7fc2,26bfdafc
Native usage snapshots — sessions: 2; records: 534; through: 2026-11-16T01:20:09.349Z; digest: 995190EB10F33AA3044FDCFE589267E846C114CBA47C75A0C8C0F784B347F087
researcher         requests 14     input 32         cached 1440041    cache-write 182879     output 65769      nano-AIU 125895560000 = 125.90 credits / 1.2590 USD
lead               requests 12     input 28         cached 1172962    cache-write 148136     output 60436      nano-AIU 109205220000 = 109.21 credits / 1.0921 USD
tester             requests 96     input 198        cached 17852814   cache-write 670414     output 273498     nano-AIU 185309799000 = 185.31 credits / 1.8531 USD
analyst            requests 14     input 32         cached 1585168    cache-write 142951     output 40618      nano-AIU 92213830000 = 92.21 credits / 0.9221 USD
analyst            requests 102    input 212        cached 22134773   cache-write 889807     output 193887     nano-AIU 637728880000 = 637.73 credits / 6.3773 USD
product-owner      requests 191    input 400        cached 39508410   cache-write 1455670    output 409146     nano-AIU 1168227600000 = 1168.23 credits / 11.6823 USD
experimenter       requests 21     input 46         cached 2708702    cache-write 166596     output 56197      nano-AIU 124942220000 = 124.94 credits / 1.2494 USD
intake-validator   requests 5      input 12         cached 92781      cache-write 33270      output 19390      nano-AIU 28637710000 = 28.64 credits / 0.2864 USD
orchestration      requests 79     input 166        cached 10704208   cache-write 1424138    output 61687      nano-AIU 524796780000 = 524.80 credits / 5.2480 USD
total nano-AIU 2996957599000 = 2996.96 credits / 29.9696 USD
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
| Deliverables produced | 9 | derived |
| Accepted by an independent review | 0 | derived |
| Rejected | 0 | derived |
| Unreviewed | 9 | derived |
| Dispatches (excluding Scribe) | 14 | derived |
| Rework dispatches | 3 | derived |
| First-pass yield | n/a | derived |
| Exact credits per accepted deliverable | n/a | measured |
| Rework share of exact credits | n/a | unavailable without per-history-run identity |
| Orchestration share of exact credits | 17.5% | measured |

Value is counted only for deliverables an independent review-class verdict accepted; a produced but unaccepted deliverable adds cost and no value. A review that names deliverables covers only those it names. Rework counts a repeat of the same agent and deliverable path only: a fix by a different agent, to a different file, or with no deliverable path is not counted, so the rework figures are a floor. Compare runs only for like work, using medians of several runs. Source: FinOps Foundation unit-economics KPIs (cost per unit of value, error and retry waste).

## Cost Comparison (exact native actual)

| Scenario | Basis | AI Credits | USD |
| -------- | ----- | ----------: | --: |
| With HVE Squad through 2026-11-16T01:20:09.349Z | complete deduplicated native records; coordinator and descendants included | 2996.96 | 29.9696 |
| Without HVE Squad: same exact role-request token categories on `claude-sonnet-5.5`, no coordinator or Scribe | calculated counterfactual from exact request tokens | 2906.52 | 29.0652 |

HVE Squad is **0.9044 USD (3.1%) higher** than the same exact role traffic on `claude-sonnet-5.5`.

> The HVE Squad row is exact as of 2 accumulated native session snapshots: 534 complete accounting records, cumulative digest `995190EB10F33AA3044FDCFE589267E846C114CBA47C75A0C8C0F784B347F087`. The without-Squad row is not an observed alternate run; it holds every exact role request's uncached input, cache read, cache write, and output counts constant, reprices them on one model, and excludes coordinator/Scribe overhead. It therefore measures routing savings on identical traffic and does not invent context growth, rework, or behavioral differences for a hypothetical manual run.
