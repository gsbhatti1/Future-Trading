> Name

SSL Momentum Indicator Combination Trading Strategy SSL-Momentum-Combo-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

### Overview

This strategy integrates the SSL channel indicator with the QQE momentum indicator, forming a comprehensive trend assessment system. It enters when price breaks the SSL channel, confirmed by QQE signals. Stops and exits are implemented for risk management.

### Strategy Logic

The key components are:

1. **SSL Channel**: Identifying the direction of price trends.
2. **QQE Indicator**: Confirming momentum.
3. **Breakout Entry**: Entering when price breaks through SSL bands, combined with QQE signals.
4. **Stops and Exits**: ATR-based stop and exit levels to control risk/reward per trade.
5. **Scaling in**: Gradually building positions, taking profits, and re-allocating.

The combination of trend and momentum tools forms a strategy that has both trend-following capabilities and risk management features.

### Advantages

Compared to single indicator strategies, the advantages are:

1. **SSL for Trend, QQE for Reversals** - Good complementarity between indicators.
2. **Breakout Entries**: Avoid buying at highs.
3. **Reasonable Stops and Exits**: Control risk/reward per trade.
4. **Scaling in**: Lower overall risk, locking in gains through partial exits.
5. **Large Optimization Space**: Ability to find optimal parameters.
6. **Flexible Application Across Different Markets and Timeframes**.
7. **Potential for Machine Learning**: For smarter optimizations.
8. **Overall More Stable with Better Risk-Adjusted Returns Than Single Indicators**.

### Risks

However, the main risks are:

1. **Challenging Multi-parameter Optimization with Overfitting Risks**.
2. **SSL and QQE Have Some Lagging**.
3. **Increased Complexity With Multiple Indicators**.
4. **Scaling in May Increase Slippage Costs**.
5. **Need to Monitor Maximum Drawdown**.
6. **Performance Subject to Changing Market Regimes**.
7. **Robustness Across Periods and Instruments Needs Verification**.
8. **High Trade Frequency Increases Transaction Costs**.

### Enhancements

Based on the analysis, enhancements may involve:

1. **Evaluating Parameter Robustness Across Different Markets and Timeframes**.
2. **Implementing Dynamic Stops and Exits**.
3. **Optimizing Risk Management Strategies**.
4. **Constructing Dynamic Position Sizing Models**.
5. **Incorporating Machine Learning for Smarter Entries**.
6. **Rolling Window Backtests to Verify Stability**.
7. **Assessing Transaction Cost Impact and Adjusting Frequency**.
8. **Optimizing Scaling Size Proportions**.
9. **Continual Improvements for Market Adaptiveness**.

### Conclusion

In summary, the tight integration of SSL and QQE forms a stable trend-following system. But continual optimizations and iterations are crucial for any strategy to stay adaptive. Only through persistent learning and validation can quant strategies achieve sustainable success.

---

> Strategy Arguments


| Argument | Default | Description |
| --- | --- | --- |
| v_input_27 | 6 | RSI Length |
| v_input_28 | 5 | RSI Smoothing |
| v_input_29 | 3 | Fast QQE Factor |
| v_input_30 | 3 | Threshold |
| v_input_31_close | 0 | RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4 |
| v_input_32 | 50 | Bollinger Length |
| v_input_33 | 0.35 | BB Multiplier |
| v_input_34 | 6 | RSI Length |
| v_input_35 | 5 | RSI Smoothing |
| v_input_36 | 1.61 | Fast QQE2 Factor |
| v_input_37 | 3 | Threshold |
| v_input_38_close | 0 | RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4 |
| v_input_1 | true | (?SSL Hybrid Indicator Settings) Show Baseline |
| v_input_2 | true | Show SSL1 |
| v_input_3 | false | Show ATR Bands |
| v_input_4 | 14 | ATR Period |
| v_input_5 | true | ATR Multi |
| v_input_6 | 0 | ATR Smoothing: WMA|SMA|EMA|RMA |
| v_input_7 | 0 | SSL1 / Baseline Type: HMA|EMA|DEMA|TEMA|LSMA|WMA|MF|VAMA|TMA|SMA|JMA|Kijun v2|EDSMA|McGinley |
| v_input_8 | 60 | SSL1 / Baseline Length |
| v_input_9 | 0 | SSL2 / Continuation Type: JMA|EMA|DEMA|TEMA|WMA|MF|VAMA|TMA|HMA|SMA|McGinley |
| v_input_10 | 5 | SSL 2 Length |
| v_input_11 | 0 | EXIT Type: HMA|TEMA|LSMA|VAMA|TMA|DEMA|JMA|Kijun v2|McGinley|MF |
| v_input_12 | 15 | EXIT Length |
| v_input_13_close | 0 | Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4 |
| v_input_14 | true | Kijun MOD Divider |
| v_input_15 | 3 | * Jurik (JMA) Only - Phase |
| v_input_16 | true | * Jurik (JMA) Only - Power |
| v_input_17 | 10 | * Volatility Adjusted (VAMA) Only - Volatility lookback length |
| v_input_18 | 0.8 | Modular Filter, General Filter Only - Beta |
| v_input_19 | false | Modular Filter Only - Feedback |
| v_input_20 | 0.5 | Modular Filter Only - Feedback Weighting |
| v_input_21 | 20 | EDSMA - Super Smoother Filter Length |
| v_input_22 | 0 | EDSMA - Super Smoother Filter Poles: 2|3 |
| v_input_23 | true | useTrueRange |
| v_input_24 | 0.2 | Base Channel Multiplier |
| v_input_25 | true | Color Bars |
| v_input_26 | 0.9 | Continuation ATR Criteria |
| v_input_39 | 14 | (?Strategy Back Test Settings) ATR Length |
| v_input_40 | timestamp(01 Aug 2021 00:00 +0100) | (?Date Range) From |
| v_input_41 | timestamp(01 Sep 2021 00:00 +0100) | To |
| v_input_42 | true | (?Exit Settings) Use TP & SL |
| v_input_43 | 1.6 | SL ATR Multiplier |
| v_input_44 | true | Move SL on TP1 |
| v_input_45 | 1.8 | TP1 ATR Multiplier |
| v_input_46 | 20 | TP1 Exit Percentage |