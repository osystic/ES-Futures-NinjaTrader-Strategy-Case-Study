# Validation methodology

## Registered Stage A

The primary robustness study used:

- 11 candidates;
- four fixed windows per candidate;
- 44 independent native NinjaTrader runs;
- one-factor-at-a-time parameter changes;
- commission enabled;
- fixed slippage assumptions;
- exact research tags and manifests;
- complete retention of poor and locked results.

The windows represented development, two historical validation years and a current-regime diagnostic period. Independent research windows were not presented as annual resets inside one continuous funded-account simulation.

## Evidence contract

A native run was expected to preserve:

- canonical manifest and research tag;
- runtime output;
- summary, trades, orders and executions;
- parameter screenshots;
- environment and data provenance;
- notes for data gaps, locks or anomalies.

Validation reconciled the identity, parameters, dates and summary information rather than trusting folder names alone.

## Eligibility logic

Promotion considered profitability, profit-factor stability, average trade, trade count, max drawdown, long/short participation, cost resistance, rule compliance and neighbouring-parameter stability.

Stage B was conditional. Because no Stage A candidate passed every gate, an external holdout was not opened.

## Additional research

After the registered matrix, additional bounded strategy families and walk-forward concepts were investigated. They increased the research surface beyond 115 candidate configurations but did not change the live/funded decision.

## Platform boundary

External analysis can reproduce research logic and aggregate results, but it cannot perfectly replace NinjaTrader's fill engine, managed-order lifecycle or provider-specific historical data. Native platform confirmation therefore remained part of the evidence contract.
