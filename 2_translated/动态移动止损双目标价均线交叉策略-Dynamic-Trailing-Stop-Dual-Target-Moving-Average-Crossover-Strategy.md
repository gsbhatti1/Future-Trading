> Source (PineScript)

```pinescript
/* backtest
start: 2023-07-29 00:00:00
end: 2024-07-28 00:00:00
period: 1d
basePeriod: 1h
*/

//@version=5
indicator("Dynamic-Trailing-Stop-Dual-Target-Moving-Average-Crossover-Strategy", overlay=true)

// Input parameters
length = input.int(200, title="MA Length")
stopLoss = input.float(500, title="Initial Stop Loss (points)")
takeProfit1 = input.float(3000, title="First Target Profit (points)")
takeProfit2 = input.float(4000, title="Second Target Profit (points)")
positionSize = 100

// Calculate Moving Average
ma = ta.sma(close, length)

// Define entry and exit conditions
longCondition = ta.crossover(close, ma)
shortCondition = ta.crossunder(close, ma)

var float stopLossLevel = na
var bool isLongPositionOpen = false
var bool isShortPositionOpen = false

if (longCondition)
    strategy.entry("Long", strategy.long)
    if (!isLongPositionOpen)
        stopLossLevel := close - stopLoss
        isLongPositionOpen := true
    strategy.exit("Take Profit 1", "Long", limit=close + takeProfit1)
    strategy.exit("Take Profit 2", "Long", limit=close + takeProfit2)

if (shortCondition)
    strategy.entry("Short", strategy.short)
    if (!isShortPositionOpen)
        stopLossLevel := close + stopLoss
        isShortPositionOpen := true
    strategy.exit("Take Profit 1", "Short", stop=close - takeProfit1)
    strategy.exit("Take Profit 2", "Short", stop=close - takeProfit2)

if (isLongPositionOpen and ta.lowest(close, length) < stopLossLevel)
    isLongPositionOpen := false
    strategy.close("Long")
else if (isShortPositionOpen and ta.highest(close, length) > stopLossLevel)
    isShortPositionOpen := false
    strategy.close("Short")

// Plotting
plot(ma, color=color.blue, title="MA 200")
plot(stopLossLevel, color=color.red, title="Stop Loss Level")
```
```