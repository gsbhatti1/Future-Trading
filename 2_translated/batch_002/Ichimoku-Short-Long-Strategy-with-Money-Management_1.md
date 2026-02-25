> Name

One-Goal Balance Multi-directional Strategy Ichimoku-Short-Long-Strategy-with-Money-Management

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/148fc207613687fd124.png)

[trans]

### Overview

This strategy is an improvement based on the Ichimoku trading system. The main idea is to combine the Moving Average theory with the Ichimoku indicator and money management rules, aiming to identify short-term and long-term trading opportunities.

### Strategy Principles

The strategy uses the classic Ichimoku system as a basic reference. The main components include:

- **Tenkan-Sen**: Conversion Line. Reflecting medium-term trends.
- **Kijun-Sen**: Base Line. Reflecting long-term trends.
- **Senkou Span A & B**: Leading and Future Lines. Reflecting future and past trends, respectively.

On this basis, the strategy has made the following improvements:

1. Time parameters follow the odd square theory to better match market patterns.
2. Money management rules are added, including stop loss, take profit, position sizing, etc., to control trading risks.
3. Adjustable backtesting range for more comprehensive testing.

Specifically, long entry conditions include Tenkan-Sen crossing above Kijun-Sen, Senkou Span B above price, and price above the cloud with a future bullish signal. Short entry requires Tenkan-Sen crossing below Kijun-Sen and Senkou Span B below price.

Money management rules require 30% profit taking and 5% stop loss for long positions; stop loss if more than 3 ATR from Tenkan-Sen for short positions.

### Advantage Analysis

The main advantages of combining Ichimoku with money management are:

1. The Ichimoku system itself reflects short, medium, and long-term trends, providing reasonable entry/exit points.
2. The odd square theory optimizes parameters to match market statistics.
3. Money management effectively controls single trade stop loss while ensuring profits exceed losses.
4. Adjustable backtesting range enables more comprehensive testing.

In summary, this strategy comprehensively considers trend identification, parameter selection, risk control, and is effective in identifying short-long opportunities and controlling trading risks, with strong practicality.

### Risk Analysis

The main risks of this strategy come from:

1. Ichimoku can be prone to false breakouts leading to unnecessary entries. More filters are needed.
2. Fixed profit-taking and stop-loss rules can be vulnerable to traps; dynamic rules should be implemented.
3. Incomplete backtesting data may overestimate the performance of the strategy. Comprehensive testing across more markets is required for longer periods.
4. The strategy works well in trending markets but may underperform in ranging markets. Optimized entry conditions are needed to identify trends.

### Optimization Directions

The main areas for optimization include:

1. Adding indicator filters to improve the quality of entries, such as MACD and KDJ.
2. Implementing dynamic profit-taking and stop-loss rules, like taking profits after an N ATR breakout or stopping out below support levels.
3. Multi-asset backtesting across longer data sets for stability verification.
4. Distinguishing between trending and ranging markets by optimizing entry mechanisms to adapt to different market conditions.

### Conclusion

This strategy comprehensively considers trends, money management, etc., uses Ichimoku to identify long opportunities, and applies risk control rules to limit single trade losses. It is a significant improvement over the original Ichimoku system. Further optimizations can potentially make it a very practical short-long trading strategy.

||

### Overview

This strategy builds on the Ichimoku trading system by integrating Moving Average theory with money management rules to identify both short and long-term trading opportunities.

### Strategy Principles

The strategy utilizes the classic Ichimoku system as its foundational reference. Key components include:

- **Tenkan-Sen**: Conversion Line, reflecting medium-term trends.
- **Kijun-Sen**: Base Line, reflecting long-term trends.
- **Senkou Span A & B**: Leading and Future Lines, reflecting future and past trends, respectively.

Based on this foundation, the strategy has made the following improvements:

1. Time parameters follow the odd square theory to better align with market patterns.
2. Money management rules are added, including stop loss, take profit, position sizing, etc., to manage trading risks.
3. Adjustable backtesting period for more comprehensive testing.

Specifically, long entry conditions include Tenkan-Sen crossing above Kijun-Sen, Senkou Span B above price, and price above the cloud with a future bullish signal. Short entry requires Tenkan-Sen crossing below Kijun-Sen and Senkou Span B below price.

Money management rules require 30% profit taking for long positions; stop loss if more than 3 ATR from Tenkan-Sen for short positions.

### Advantage Analysis

The main advantages of combining Ichimoku with money management include:

1. The Ichimoku system reflects short, medium, and long-term trends, providing reasonable entry/exit points.
2. The odd square theory optimizes parameters to align with market statistics.
3. Money management effectively controls single trade stop loss while ensuring profits exceed losses.
4. Adjustable backtesting period enables more comprehensive testing.

In summary, this strategy comprehensively considers trend identification, parameter selection, and risk control, making it effective in identifying short-long opportunities and controlling trading risks, with strong practicality.

### Risk Analysis

The main risks of this strategy come from:

1. Ichimoku can be prone to false breakouts leading to unnecessary entries. More filters are needed.
2. Fixed profit-taking and stop-loss rules can be vulnerable to traps; dynamic rules should be implemented.
3. Incomplete backtesting data may overestimate the performance of the strategy. Comprehensive testing across more markets is required for longer periods.
4. The strategy works well in trending markets but may underperform in ranging markets. Optimized entry conditions are needed to identify trends.

### Optimization Directions

The main areas for optimization include:

1. Adding indicator filters to improve the quality of entries, such as MACD and KDJ.
2. Implementing dynamic profit-taking and stop-loss rules, like taking profits after an N ATR breakout or stopping out below support levels.
3. Multi-asset backtesting across longer data sets for stability verification.
4. Distinguishing between trending and ranging markets by optimizing entry mechanisms to adapt to different market conditions.

### Conclusion

This strategy comprehensively considers trends, money management, etc., uses Ichimoku to identify long opportunities, and applies risk control rules to limit single trade losses. It is a significant improvement over the original Ichimoku system. Further optimizations can potentially make it a very practical short-long trading strategy.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|8|Tenkan-Sen Period|
|v_input_int_2|16|Kijun-Sen Period|
|v_input_int_3|24|Senkou-Span B Period|
|v_input_int_4|16|Chikou-Span Offset|
|v_input_int_5|8|Senkou-Span Offset|
|v_input_1|true|Long Entry|
|v_input_2|true|Short Entry|
|v_input_int_6|true|Start Date|
|v_input_int_7|true|Start Month|
|v_input_int_8|1980|Start Year|
|v_input_int_9|true|End Date|
|v_input_int_10|true|End Month|
|v_input_int_11|2100|End Year|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-27 00:00:00
end: 2023-12-27 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Author Obarut
//@version=5
strategy("Ichimoku Strategy With MM Short-Long", overlay=true, process_orders_on_close=true)

// Ichimoku Inputs
ts_period = input.int(8, minval=1, title="Tenkan-Sen Period")
ks_period = input.int(16, minval=1, title="Kijun-Sen Period")
ssb_period = input.int(24, minval=1, title="Senkou-Span B Period")
cs_offset = input.int(16, minval=1, title="Chikou-Span Offset")
ss_offset = input.int(8, minval=1, title="Senkou-Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

// Back Testing Period Inputs

fromday = input.int(defval=1, title="Start Date", minval=1, maxval=31) 
frommonth = input.int(defval=1, title="Start Month", minval=1, maxval=12)
fromyear = input.int(defval=1980, title="Start Year")
endday = input.int(defval=1, title="End Date", minval=1, maxval=31) 
endmonth = input.int(defval=1, title="End Month", minval=1, maxval=12)
endyear = input.int(defval=2100, title="End Year")
```