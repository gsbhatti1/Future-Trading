> Name

Ichimoku Cloud and RSI Combination Strategy

> Author

ChaoZhang

> Strategy Description

### Overview

This strategy integrates the use of Ichimoku Cloud and Relative Strength Index (RSI) indicators to determine trend direction, entering positions when a trend is initiated. It generates trading signals when the three lines of Ichimoku Cloud form valid combinations in conjunction with RSI signals.

### Strategy Logic 

1. Calculate Tenkan-sen, Kijun-sen, and Chikou Span lines of Ichimoku Cloud.
2. Calculate RSI values.
3. Go long when Tenkan-sen crosses above Kijun-sen, Chikou Span is above the cloud, price breaks out above the cloud, and RSI is below 50.
4. Go short when Tenkan-sen crosses below Kijun-sen, Chikou Span is below the cloud, price breaks down through the cloud, and RSI is above 50.
5. Close position when a reverse signal occurs.

Specifically, it combines Ichimoku Cloud's trend analysis with RSI's overbought/oversold gauge. Entry signals are generated when Ichimoku lines form a trend start pattern and RSI indicates no overbought/oversold condition. The RSI filter helps avoid false breakouts during consolidation. Exits follow the reverse formation of Ichimoku Cloud completely.

### Advantage Analysis

1. Combining RSI improves entry accuracy.
2. Ichimoku Cloud has strong trend following capability.
3. Signals are simple and intuitive.
4. Customizable parameters fit different time cycles.
5. Risk managed by stop profit/loss strategies.

### Risk Analysis

1. Ichimoku Cloud may lag, causing false breakouts.
2. Requires parameter optimization; otherwise, signals may be inaccurate.
3. Long holding introduces overnight risk.
4. RSI prone to false signals.
5. Risks of being trapped on reversals.

Risks can be managed through parameter optimization, stop profit/loss tuning, limiting holding periods, etc.

### Optimization Directions

1. Test different line and RSI parameters for the best combinations.
2. Introduce trailing stop loss.
3. Evaluate limiting trading hours.
4. Study parameter preferences across products.
5. Test adding re-entry and pyramiding rules.
6. Compare different stop profit/loss strategies.

### Summary

This strategy combines Ichimoku Cloud and RSI for trend analysis and trading. Pros are simple intuitive signals and high return on investment (ROI); cons include lags and trapped risks. Performance can be improved and risks controlled through parameter optimization, stop profit/loss tuning, and limiting holding periods. This allows comprehensive understanding of the application of Ichimoku Cloud.

||

### Overview

This strategy combines Ichimoku Cloud and Relative Strength Index (RSI) indicators to determine trend direction and enter positions when a trend starts. It generates trading signals when the three lines of Ichimoku Cloud align in valid combinations together with RSI signals.

### Strategy Logic 

1. Calculate Tenkan-sen, Kijun-sen, and Chikou Span lines of Ichimoku Cloud.
2. Calculate RSI values.
3. Go long when Tenkan-sen crosses above Kijun-sen, Chikou Span is above the cloud, price breaks out above the cloud, and RSI is below 50.
4. Go short when Tenkan-sen crosses below Kijun-sen, Chikou Span is below the cloud, price breaks down through the cloud, and RSI is above 50.
5. Close position when a reverse signal occurs.

Specifically, it combines Ichimoku Cloud's trend analysis with RSI's overbought/oversold gauge. Entry signals are generated when Ichimoku lines form a trend start pattern, and RSI indicates no overbought/oversold condition. The RSI filter helps avoid false breakouts during consolidation. Exits follow the reverse formation of Ichimoku Cloud completely.

### Advantage Analysis

1. Combining RSI improves entry accuracy.
2. Ichimoku Cloud has strong trend following capacity.
3. Signals are simple and intuitive.
4. Customizable parameters fit different cycles.
5. Risk managed by stop profit/loss strategies.

### Risk Analysis

1. Ichimoku Cloud may lag, causing false breakouts.
2. Requires parameter optimization; otherwise, signals may be inaccurate.
3. Long holding introduces overnight risk.
4. RSI prone to false signals.
5. Risks of being trapped on reversals.

Risks can be managed through parameter optimization, stop profit/loss tuning, limiting holding periods, etc.

### Optimization Directions

1. Test different line and RSI parameters for the best combinations.
2. Introduce trailing stop loss.
3. Evaluate limiting trading hours.
4. Study parameter preferences across products.
5. Test adding re-entry and pyramiding rules.
6. Compare different stop profit/loss strategies.

### Summary

This strategy combines Ichimoku Cloud and RSI for trend analysis and trading. Pros are simple intuitive signals and high return on investment (ROI); cons include lags and trapped risks. Performance can be improved and risks controlled through parameter optimization, stop profit/loss tuning, and limiting holding periods. This allows comprehensive understanding of the application of Ichimoku Cloud.

|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Show Date Range|
|v_input_int_1|9|Tenkan-Sen Bars|
|v_input_int_2|26|Kijun-Sen Bars|
|v_input_int_3|52|Senkou-Span B Bars|
|v_input_int_4|26|Chikou-Span Offset|
|v_input_int_5|26|Senkou-Span Offset|
|v_input_2|true|Long Entry|
|v_input_3|true|Short Entry|

```pinescript
/*backtest
start: 2022-09-14 00:00:00
end: 2023-09-20 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Coinrule

//@version=5
strategy("Ichimoku Cloud with RSI (By Coinrule)",
         overlay=true,
         initial_capital=1000,
         process_orders_on_close=true,
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=30,
         commission_type=strategy.commission.percent,
         commission_value=0.1)

showDate = input(defval=true, title='Show Date Range')
timePeriod = time >= timestamp(syminfo.timezone, 2022, 6, 1, 0, 0)


// RSI inputs and calculations
lengthRSI = 14
RSI = ta.rsi(close, lengthRSI)


//Inputs
ts_bars = input.int(9, minval=1, title="Tenkan-Sen Bars")
ks_bars = input.int(26, minval=1, title="Kijun-Sen Bars")
ssb_bars = input.int(52, minval=1, title="Senkou-Span B Bars")
cs_offset = input.int(26, minval=1, title="Chikou-Span Offset")
ss_offset = input.int(26, minval=1, title="Senkou-Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

middle(len) => math.avg(ta.lowest(len), ta.highest(len))


// Components of Ichimoku Cloud
tenkan = middle(ts_bars)
kijun = middle(ks_bars)
senkouA = math.avg(tenkan, kijun)
senkouB = middle(ssb_bars)


// Plot Ichimoku Cloud
plot(tenkan, color=#0496ff, title="Tenkan-Sen")
plot(kijun, color=#991515, title="Kijun-Sen")
plot(close, offset=-cs_offset+1, color=#459915, title="Chikou-Span")
sa=plot(senkouA, offset=ss_offset-1, color=color.green, title="Senkou-Span A")
sb=plot(senkouB, offset=ss_offset-1, color=color.red, title="Senkou-Span B")
fill(sa, sb, color = senkouA > senkouB ? color.green : color.red, title="Cloud color")

ss_high = math.max(senkouA[ss_offset-1], senkouB[ss_offset-1])
ss_low = math.min(senkouA[ss_offset-1], senkouB[ss_offset-1])


// Entry/Exit Conditions
tk_cross_bull = tenkan > kijun
tk_cross_bear = tenkan < kijun
cs_cross_bull = ta.mom(close, cs_offset-1) > 0
cs_cross_bear = ta.mom(close, cs_offset-1) < 0
price_above_kumo = close > ss_high
price_below_kumo = close < ss_low

bullish = tk_cross_bu