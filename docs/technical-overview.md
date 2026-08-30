# Technical overview

The confidential delivery is a NinjaTrader 8 strategy for selective ES intraday research. Its public-safe architecture can be summarized as seven layers:

1. ES bar input with secondary context series;
2. application-time normalization to Eastern Time;
3. session and protected-news eligibility gates;
4. signal qualification;
5. managed entry, stop, target and exit lifecycle;
6. daily/consecutive-loss/account-level risk controls;
7. runtime evidence, provenance and deterministic candidate aggregation.

## Safety architecture

The strategy treats protective downside control as part of the order lifecycle, not as an optional reporting feature. Session cutoffs, hard flattening, daily loss/profit controls, consecutive-loss limits, trade caps and a permanent internal drawdown lock constrain new exposure.

A permanent drawdown lock can make a long backtest appear to “stop trading.” That behavior is an intentional safety state, not automatically evidence of missing data or a runtime crash.

## Research architecture

The registered neighbourhood changed one parameter at a time around a frozen baseline. Each candidate was evaluated across development, historical-validation and current-regime windows. A deterministic gate, rather than manual preference, controlled survivor selection.

The private NinjaScript and exact signal implementation are intentionally not published.
