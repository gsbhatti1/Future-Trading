> Name

One-Goal Equilibrium Short-Long Strategy with Money Management Ichimoku-Short-Long-Strategy-with-Money-Management

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/148fc207613687fd124.png)

[trans]

### Overview

This strategy is an improvement based on the Ichimoku trading system. The main idea is to combine the Moving Average theory with the Ichimoku indicator and money management rules to identify short and long trading opportunities.

### Strategy Principles

The strategy uses the classic Ichimoku system as a basic reference. The main components include:

- Tenkan-Sen: Conversion Line. Reflects medium-term trends.
- Kijun-Sen: Base Line. Reflects long-term trends.
- Senkou Span A and B: Leading Lines. Reflect future and long-term trends.
- Chikou Span: Lagging Line. Reflects past trends.

On this basis, the strategy has made the following improvements:

1. The time parameters follow the odd square theory to better match market patterns.
2. Money management rules are added, including stop loss, take profit, position sizing, etc., to control trading risks.
3. Backtesting period is adjustable for more comprehensive testing.

Specifically, long entry conditions include Tenkan-Sen crossing above Kijun-Sen, Chikou Span above price, price above Kumo (cloud), and future Kumo indicating a bullish trend. Short entry requires Tenkan-Sen crossing below Kijun-Sen, Chikou Span below price, etc.

Money management rules require 30% profit taking for longs and 5% stop loss; stop loss if more than 3 ATR (Average True Range) from Tenkan-Sen for shorts.

### Advantage Analysis

The main advantages of combining Ichimoku with money management are:

1. Ichimoku itself reflects short, medium, and long-term trends, making entry/exit points reasonable.
2. The odd square theory optimizes parameters to match market statistics.
3. Money management rules effectively control single trade stop loss while ensuring profits exceed losses.
4. Adjustable backtesting period enables more comprehensive testing.

In summary, this strategy comprehensively considers trend, parameter selection, risk control, etc., and is effective in identifying short-long opportunities and controlling trading risks, with strong practicality.

### Risk Analysis

The main risks of this strategy come from:

1. Ichimoku is prone to false breakouts causing unnecessary entries; more filters are needed.
2. Fixed profit taking and stop loss rules can be vulnerable to traps; dynamic rules should be introduced.
3. Incomplete backtesting data may overestimate performance; longer testing across more markets is required.
4. The strategy performs better in trending markets, possibly underperforming in ranging markets; entry conditions need optimization for trend identification.

### Optimization Directions

The main areas of enhancements include:

1. Add indicator filters to improve entry quality. Such as MACD, KDJ, etc.
2. Introduce dynamic profit taking and stop loss rules. For example, take profit after N ATR (Average True Range) breakouts; stop loss below supports.
3. Multi-asset testing across longer data for stability verification.
4. Differentiate between trending and ranging markets. Optimize entries to adapt to varying market conditions.

### Conclusion

This strategy comprehensively considers trend, money management, etc., uses Ichimoku to identify long opportunities, and applies risk control rules to limit single trade loss. Significant improvements over the original Ichimoku system. Further optimizations can potentially make it a very practical short-long trading strategy.

|| 

### Overview

This strategy is an improvement based on the Ichimoku trading system. The main idea is to combine the Moving Average theory with the Ichimoku indicator and money management rules to identify short and long trading opportunities.

### Strategy Principles

The strategy uses the classic Ichimoku system as a basic reference. The main components include:

- Tenkan-Sen: Conversion Line. Reflects medium-term trends.
- Kijun-Sen: Base Line. Reflects long-term trends.
- Senkou Span A and B: Leading Lines. Reflect future and long-term trends.
- Chikou Span: Lagging Line. Reflects past trends.

On this basis, the strategy has made the following improvements:

1. The time parameters follow the odd square theory to better match market patterns.
2. Money management rules are added, including stop loss, take profit, position sizing, etc., to control trading risks.
3. Backtesting period is adjustable for more comprehensive testing.

Specifically, long entry conditions include Tenkan-Sen crossing above Kijun-Sen, Chikou Span above price, price above Kumo (cloud), and future Kumo indicating a bullish trend. Short entry requires Tenkan-Sen crossing below Kijun-Sen, Chikou Span below price, etc.

Money management rules require 30% profit taking for longs and 5% stop loss; stop loss if more than 3 ATR (Average True Range) from Tenkan-Sen for shorts.

### Advantage Analysis

The main advantages of combining Ichimoku with money management are:

1. Ichimoku itself reflects short, medium, and long-term trends, making entry/exit points reasonable.
2. The odd square theory optimizes parameters to match market statistics.
3. Money management rules effectively control single trade stop loss while ensuring profits exceed losses.
4. Adjustable backtesting period enables more comprehensive testing.

In summary, this strategy comprehensively considers trend, parameter selection, risk control, etc., and is effective in identifying short-long opportunities and controlling trading risks, with strong practicality.

### Risk Analysis

The main risks of this strategy come from:

1. Ichimoku is prone to false breakouts causing unnecessary entries; more filters are needed.
2. Fixed profit taking and stop loss rules can be vulnerable to traps; dynamic rules should be introduced.
3. Incomplete backtesting data may overestimate performance; longer testing across more markets is required.
4. The strategy performs better in trending markets, possibly underperforming in ranging markets; entry conditions need optimization for trend identification.

### Optimization Directions

The main areas of enhancements include:

1. Add indicator filters to improve entry quality. Such as MACD, KDJ, etc.
2. Introduce dynamic profit taking and stop loss rules. For example, take profit after N ATR (Average True Range) breakouts; stop loss below supports.
3. Multi-asset testing across longer data for stability verification.
4. Differentiate between trending and ranging markets. Optimize entries to adapt to varying market conditions.

### Conclusion

This strategy comprehensively considers trend, money management, etc., uses Ichimoku to identify long opportunities, and applies risk control rules to limit single trade loss. Significant improvements over the original Ichimoku system. Further optimizations can potentially make it a very practical short-long trading strategy.

|| 

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|8|Tenkan-Sen Period|
|v_input_int_2|16|Kijun-Sen Period|
|v_input_int_3|24|Senkou Span B Period|
|v_input_int_4|16|Chikou-Span Offset|
|v_input_int_5|8|Senkou Span Offset|
|v_input_1|true|Long Entry|
|v_input_2|true|Short Entry|
|v_input_int_6|true|Start Date|
|v_input_int_7|true|Start Month|
|v_input_int_8|1980|Start Year|
|v_input_int_9|true|End Date|
|v_input_int_10|true|End Month|
|v_input_int_11|2100|End Year|

> Source (PineScript)

```pinescript
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
ssb_period = input.int(24, minval=1, title="Senkou Span B Period")
cs_offset = input.int(16, minval=1, title="Chikou Span Offset")
ss_offset = input.int(8, minval=1, title="Senkou Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

// Back Testing Period Inputs
fromday = input.int(defval=1, title="Start Date", minval=1, maxval=31)
frommonth = input.int(defval=1, title="Start Month", minval=1, maxval=12)
fromyear = input.int(defval=1980, title="Start Year")
endday = input.int(defval=1, title="End Date", minval=1, maxval=31)
endmonth = input.int(defval=12, title="End Month", minval=1, maxval=12)
endyear = input.int(defval=2024, title="End Year")
```