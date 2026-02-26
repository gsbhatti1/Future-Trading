> Source (PineScript)

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

// Plot entry and exit points
plotshape(series=buyCondition, location=location.belowbar, style=shape.triangleup, title="Buy Signal", color=color.green, size=size.small)
plotshape(series=sellCondition, location=location.abovebar, style=shape.triangledown, title="Sell Signal", color=color.red, size=size.small)

// Strategy logic
if (buyCondition)
    strategy.entry("Long Entry", strategy.long)

if (exitCondition)
    strategy.close("Long Entry")
```

Note: The commented-out lines for drawing the green and red lines were left as they are to maintain the original formatting.