> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|3|MACD fast moving average|
|v_input_2|9|MACD slow moving average|
|v_input_3|5|MACD signal line moving average|
|v_input_4|true|length|
|v_input_5|true|From Month|
|v_input_6|true|From Day|
|v_input_7|2002|From Year|
|v_input_8|3|To Month|
|v_input_9|true|To Day|
|v_input_10|2029|To Year|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-03-23 00:00:00
end: 2024-03-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("MACD trendfollow", shorttitle="MACD TF", overlay=true)

// Input parameters
fast_length = input(3, title="MACD fast moving average")
slow_length = input(9, title="MACD slow moving average")
signal_length = input(5, title="MACD signal line moving average")

// MACD calculation
[macd_line, macd_signal, _] = macd(close, fast_length, slow_length, signal_length)

// Long and short conditions
long_condition = macd_line > macd_signal and macd_line >= 0
short_condition = macd_line < macd_signal and macd_line <= 0

// Stop loss levels
long_stop_loss = lowest(low[1]) // Most recent low point for long positions
short_stop_loss = highest(high[1]) // Most recent high point for short positions

// Plotting MACD lines and stop loss levels
plot(macd_line, title="MACD Line", color=color.blue)
plot(macd_signal, title="Signal Line", color=color.red)
hline(0, "Zero Line", color=color.gray)

plotshape(series=long_condition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=short_condition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

// Trade logic
if (long_condition)
    strategy.entry("Long", strategy.long, stop=long_stop_loss)

if (short_condition)
    strategy.entry("Short", strategy.short, stop=short_stop_loss)

// Close positions when MACD crosses the signal line in the opposite direction
if (macd_line < macd_signal and not long_condition[1])
    strategy.close("Long")

if (macd_line > macd_signal and not short_condition[1])
    strategy.close("Short")
```

This Pine Script code implements the MACD trend following strategy as described. It calculates the MACD values, sets trading conditions based on golden cross and death cross signals, and uses recent significant highs and lows for stop loss levels.