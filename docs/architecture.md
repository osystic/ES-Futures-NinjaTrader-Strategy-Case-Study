# Public architecture

## Purpose

This repository presents a sanitized architecture of a completed ES futures NinjaTrader engineering and research engagement. It does not contain the confidential signal implementation.

## Public system view

1. ES market data enters a controlled NinjaTrader environment.
2. Timezone, session and protected-news gates determine whether new risk is allowed.
3. Confidential signal qualification feeds a managed-order lifecycle.
4. Protective exits and daily/account-level risk locks constrain exposure.
5. Native runtime evidence is captured with provenance.
6. A pre-registered multi-window matrix feeds a deterministic decision gate.
7. No eligible survivor produces an honest NO-GO; an eligible survivor alone could enter untouched holdout testing.

See [the architecture diagram](../assets/architecture.svg) and [technical overview](technical-overview.md).

## Deliberate omissions

Entry logic, exact private topology, account identifiers, raw datasets, private evidence and implementation source are excluded. The private project remains the engineering source of truth.

## Decision records

Public architecture and publication-boundary decisions are recorded in [docs/adr](adr/README.md).
