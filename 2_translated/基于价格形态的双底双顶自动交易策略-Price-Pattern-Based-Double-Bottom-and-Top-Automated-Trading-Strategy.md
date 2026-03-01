``` pinescript
/*backtest
start: 2024-12-04 00:00:00
end: 2024-12-11 00:00:00
period: 3m
basePeriod: 3m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Double Bottom and Top Hunter", overlay=true)

// Parameters
length = input.int(100, title="Monitoring Period", defval=100)
lookback = input.int(100, title="Lookback Period", defval=100)

// Double Bottom and Top Detection
low1 = ta.lowest(low, length)
high1 = ta.highest(high, length)

low2 = ta.valuewhen(low == low1, low, 1)
high2 = ta.valuewhen(high == high1, high, 1)

doubleBottom = (low == low1 and ta.lowest(low, lookback) == low1 and low == low2)
doubleTop = (high == high1 and ta.highest(high, lookback) == high1 and high == high2)

// Entry Conditions
longCondition = doubleBottom
shortCondition = doubleTop

// Exit Conditions
closeLongCondition = ta.highest(high, length) > high1 and low < low1
closeShortCondition = ta.lowest(low, length) < low1 and high > high1

// Enter Long Position
if (longCondition)
    strategy.entry("Long", strategy.long, qty=1)

// Enter Short Position
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=1)

// Exit Positions
if (closeLongCondition)
    strategy.close("Long")

if (closeShortCondition)
    strategy.close("Short")

// Plot Indicators and ZigZag Line on Chart
plotshape(series=longCondition, title="Double Bottom Found", location=location.belowbar, color=color.green, style=shape.labelup, text="LONG")
plotshape(series=shortCondition, title="Double Top Found", location=location.abovebar, color=color.red, style=shape.labeldown, text="SHORT")
```

This Pine Script code defines a trading strategy for detecting double bottom and top patterns on the chart. The script sets up entry conditions based on these patterns and includes logic to close positions when exit conditions are met. The `plotshape` function is used to visually indicate the presence of double bottoms and tops on the chart, making it easier to analyze and validate the strategy.