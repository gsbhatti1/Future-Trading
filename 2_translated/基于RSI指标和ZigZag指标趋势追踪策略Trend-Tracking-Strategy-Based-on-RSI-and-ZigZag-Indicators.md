``` pinescript
/*backtest
start: 2024-01-22 00:00:00
end: 2024-02-21 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © SoftKill21
//@version=4
strategy("Crypto ZigZag RSI strategy 15min", overlay=true)

// Input parameters
v_input_1 = input(5, title="RSI Length")
v_input_2 = input(25, title="overSold")
v_input_3 = input(75, title="overBought")
v_input_4 = input(true, title="Minimum % Change")
v_input_5 = input(true, title="longa")
v_input_6 = input(false, title="shorta")

// RSI calculation
rsi_length = v_input_1
overSold = v_input_2
overBought = v_input_3
rsi = rsi(close, rsi_length)

// ZigZag calculation
min_zigzag_percent_change = v_input_4 ? 1 : 0
longa = v_input_5
shorta = v_input_6

zigzag = ta.zigzang(close, min_zigzag_percent_change)

// Trend tracking logic
var float trend_value = na
if rsi < overSold and not na(trend_value)
    trend_value := -1
else if rsi > overBought and not na(trend_value)
    trend_value := 1

long_condition = ta.crossover(rsi, overSold) and zigzag == true and longa
short_condition = ta.crossunder(rsi, overBought) and zigzag == false and shorta

// Trading signals
if long_condition
    strategy.entry("Long", strategy.long)
elif short_condition
    strategy.entry("Short", strategy.short)

// Plotting indicators
plot(rsi, title="RSI", color=color.blue)
hline(overSold, "OverSold Level", color=color.red)
hline(overBought, "OverBought Level", color=color.green)
zigzag_line = plotshape(series=zigzag, location=location.belowbar, color=color.orange, style=shape.triangleup, title="ZigZag Signal")
```