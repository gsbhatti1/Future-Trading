```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-18 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Smart Money Concept Strategy", overlay=true)

// Indicators
obv = ta.cum(ta.volume)
long_condition = ta.slope(obv, 2) > 0
short_condition = ta.slope(obv, 2) < 0

// Plot signals
plotshape(series=long_condition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=short_condition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

// Entry and Exit Logic
if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

if (not na(ta.valuewhen(long_condition, close, 0)))
    strategy.close("Long")

if (not na(ta.valuewhen(short_condition, close, 0)))
    strategy.close("Short")
```

Note: The Pine Script has been updated to include the entry and exit logic based on the conditions described.