# ES Futures NinjaTrader Strategy

Anonymous engineering case study | Futures strategy research | NinjaTrader 8 / NinjaScript

| Field | Value | Field | Value |
|---|---|---|---|
| Domain | Systematic futures research | Platform | NinjaTrader 8 |
| Market | ES futures | Status | Completed engineering/research delivery |
| Delivery boundary | SIM research candidate | Live decision | NO-GO |

## Executive summary

A selective intraday ES strategy was engineered and evaluated through three controlled phases. The work began with platform-compatible order and risk architecture, expanded into multi-year cost-aware evidence collection, and ended with a pre-registered robustness matrix plus additional bounded strategy-family research.

The system was technically functional: it compiled and ran in NinjaTrader, generated orders, armed protective exits, applied session/news controls and enforced daily/account-level risk limits. Profitability was a different question. The registered 44-run matrix produced no candidate that met every robustness gate. The closest candidate was therefore delivered for frozen-parameter SIM observation only.

The case study demonstrates disciplined completion: the engineering system and evidence package were delivered, while live/funded promotion was withheld because the data did not justify it.

## Client objective translated into engineering requirements

The original objective emphasized low drawdown, a high profit factor and NinjaTrader backtest evidence. Those commercial goals were converted into testable engineering requirements:

- NinjaTrader-compatible strategy implementation;
- immediate protective downside control;
- deterministic trading hours and hard flattening;
- protected-news blackout with schedule provenance;
- one-contract risk profile;
- realistic commission and slippage;
- daily and cumulative risk locks;
- multi-year validation, not a single attractive window;
- repeatable evidence exports and machine-readable manifests;
- explicit promotion gates and an honest NO-GO path.

A high profit factor remained a research target, never a guarantee.

## Three-phase delivery

### Phase 1 — functional architecture

The first phase established the core NinjaTrader strategy and corrected managed-order behavior. Validation focused on long/short paths, immediate protective stops, delayed targets, sibling-order cleanup, session restrictions, news controls and risk locks.

### Phase 2 — evidence and cost realism

The second phase expanded instrumentation and gathered multi-year evidence. Runtime tags, parameter snapshots, gate counters and exit reasons made results traceable. Commission/slippage stress showed that the candidate should not be promoted.

### Phase 3 — robustness and closeout

The third phase froze the maintained baseline and registered an 11-candidate, four-window Stage A matrix. Parameters were changed one factor at a time. Development, historical validation and current-regime windows were kept distinct.

All 44 native runs were completed. No candidate passed every gate, so the untouched Stage B holdout was not opened. Additional bounded strategy families were explored, but none supported a live/funded recommendation.

## Architecture

![Architecture](assets/architecture.svg)

The private implementation combined signal qualification, multi-series context, managed order handling and account-safety controls. The public diagram stays at an architectural level and does not disclose entry logic.

## Validation protocol

The registered matrix required:

1. fixed candidate definitions before result review;
2. fixed date windows and exact research tags;
3. commission and slippage assumptions;
4. fresh evidence folders with manifests and runtime outputs;
5. no omission of losing, zero-trade or globally locked runs;
6. deterministic validation of tags, roles, parameters and exported summaries;
7. candidate-level aggregation across windows;
8. Stage B only if exactly one eligible survivor emerged.

This protocol prevented rescue tuning after weak validation.

## Results

| Evidence item | Outcome |
|---|---:|
| Native registered runs | 44 / 44 |
| Registered candidates | 11 |
| Eligible registered candidates | 0 |
| Stage B | Not opened |
| Closest candidate | STOP_L |
| Closest validation net | +$46.56 |
| Closest validation PF | 1.0075 |
| Closest validation trades | 44 |
| Closest development result | -$1,014.34 |
| Final live/funded decision | NO-GO |

The closest candidate produced positive 2024 and 2026 diagnostic results but a negative 2025 window and negative 2021–2023 development result. Its combined validation edge was too small to support deployment after considering stability, drawdown and average-trade quality.

## Final handover boundary

The completed client delivery included the maintained source, exact configuration, setup guidance, focused evidence, broader Phase 3 evidence and a monthly P&L breakdown. The selected candidate was labelled:

> **RESEARCH / PAPER-TRADING ONLY**

Prospective monitoring requires exact frozen parameters, a NinjaTrader SIM account, and reassessment only after at least 50 new trades or 3–6 months, whichever takes longer.

## What this demonstrates

- NinjaScript lifecycle and managed-order engineering;
- risk-first futures strategy architecture;
- time-zone, session and news-event controls;
- evidence provenance and result reconciliation;
- parameter-neighbourhood and multi-window validation;
- commission/slippage-aware evaluation;
- clear separation between technical functionality and trading viability;
- client delivery that remains useful without overstating performance.

## Disclosure and claims boundary

No confidential source, client identity, private messages, account/machine identifiers, raw NT8 exports, screenshots, market datasets, news files, delivery archives, hashes, private repository links or commercial information are included.

No live profitability or future-performance claim is made.
