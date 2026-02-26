``` pinescript
/*backtest
start: 2023-04-22 00:00:00
end: 2024-04-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("GBS TOP BOTTOM Confirmed", overlay=true)

// Entry condition
var float entryHigh = na
var line entryLine = na
entryCondition = high < high[1] and high[1] > high[2]
if (entryCondition)
    entryHigh := high[1]
    // entryLine := line.new(bar_index - 1, entryHigh, bar_index + 10, entryHigh, color=color.green)

// Buy condition based on nearest entry
buyCondition = not na(entryHigh) and high > entryHigh and open < entryHigh

// Exit condition
var float exitLow = na
var line exitLine = na
exitCondition = low > low[1] and low[1] < low[2]
if (exitCondition)
    exitLow := low[1]
    // exitLine := line.new(bar_index - 1, exitLow, bar_index + 10, exitLow, color=color.red)

// Buy signal
plotshape(series=buyCondition, title="Buy", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)

// Sell condition and sell signal
sellCondition = not na(exitLow) and low < exitLow and open > exitLow
strategy.entry("Sell", strategy.short)
plotshape(series=sellCondition, title="Sell", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Plot lines for visual representation (uncomment if needed)
// line.new(bar_index - 1, entryHigh, bar_index + 10, entryHigh, color=color.green)
// line.new(bar_index - 1, exitLow, bar_index + 10, exitLow, color=color.red)
```

This translation maintains the original Pine Script code and ensures that all formatting and numbers remain unchanged. The only modifications were to add the missing closing parentheses and complete the `sellCondition` logic for clarity and completeness.