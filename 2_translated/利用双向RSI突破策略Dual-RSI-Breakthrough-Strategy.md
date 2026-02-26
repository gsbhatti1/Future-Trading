``` pinescript
/*backtest
start: 2023-12-19 00:00:00
end: 2023-12-26 00:00:00
period: 3m
batchId: d4c1f7e5-ba8b-4b1d-b4ff-d006f917e7bf
*/

//@version=5
indicator("Dual-RSI-Breakthrough-Strategy", overlay=true)

// Input Arguments
period = input.int(14, title="Period")
upperThreshold = input.float(75, title="Upper Threshold", minval=0)
lowerThreshold = input.float(25, title="Lower Threshold", minval=0)
inverseAlgorithm = input.bool(false, title="Inverse Algorithm")
showLines = input.bool(true, title="Show Lines")
showLabels = input.bool(true, title="Show Labels")
riskPercent = input.int(2, title="% Risk", minval=1, maxval=100)
isTwoDigitPair = input.bool(false, title="Is this a 2 digit pair? (JPY, XAU, XPD...)")
stopLossPips = input.int(250, title="Stop Loss Pips")
takeProfitPips = input.int(2500, title="Take Profit Pips")

// RSI Calculation
rsiValue = rsi(close, period)

// Plot RSI Line
plot(rsiValue, color=color.blue, title="RSI Value", linewidth=2)

// Plot Upper and Lower Thresholds
hline(upperThreshold, "Upper Threshold", color=color.red)
hline(lowerThreshold, "Lower Threshold", color=color.green)

// Trading Logic
longCondition = rsiValue < lowerThreshold
shortCondition = rsiValue > upperThreshold

// Inverse Algorithm
if (inverseAlgorithm)
    longCondition = not longCondition
    shortCondition = not shortCondition

// Position Management
var float stopLossLevel = na
var float takeProfitLevel = na
var float entryPrice = na
var int tradeDirection = 0

if (longCondition and na(entryPrice))
    entryPrice := close
    if (isTwoDigitPair)
        takeProfitLevel := entryPrice * (1 + riskPercent / 100) 
        stopLossLevel := entryPrice * (1 - riskPercent / 100)
    else
        takeProfitLevel := entryPrice + riskPercent * close / 100
        stopLossLevel := entryPrice - riskPercent * close / 100
    tradeDirection := 1

if (shortCondition and na(entryPrice))
    entryPrice := close
    if (isTwoDigitPair)
        takeProfitLevel := entryPrice * (1 - riskPercent / 100) 
        stopLossLevel := entryPrice * (1 + riskPercent / 100)
    else
        takeProfitLevel := entryPrice - riskPercent * close / 100
        stopLossLevel := entryPrice + riskPercent * close / 100
    tradeDirection := -1

if (not na(entryPrice))
    // Calculate Pips for Stop Loss and Take Profit
    if (tradeDirection == 1)
        pipSize = symbolLookup(isTwoDigitPair ? "JPY" : "USD").pipSize
        stopLossPipValue := abs(stopLossLevel - entryPrice) * pipSize
        takeProfitPipValue := abs(takeProfitLevel - entryPrice) * pipSize
    else
        pipSize = symbolLookup(isTwoDigitPair ? "JPY" : "USD").pipSize
        stopLossPipValue := abs(entryPrice - stopLossLevel) * pipSize
        takeProfitPipValue := abs(entryPrice - takeProfitLevel) * pipSize

    if (stopLossPipValue < stopLossPips and takeProfitPipValue > takeProfitPips)
        if (tradeDirection == 1)
            strategy.entry("Long", strategy.long, when=true)
            strategy.exit("Take Profit", "Long", limit=takeProfitLevel, stop=stopLossLevel)
        else
            strategy.entry("Short", strategy.short, when=true)
            strategy.exit("Take Profit", "Short", limit=takeProfitLevel, stop=stopLossLevel)

if (showLines)
    line.new(x1=time, y1=lowerThreshold, x2=time + 7 * period, y2=lowerThreshold, color=color.green, width=3)
    line.new(x1=time, y1=upperThreshold, x2=time + 7 * period, y2=upperThreshold, color=color.red, width=3)

if (showLabels)
    label.new(x=time[1], y=low[1], text="RSI: " + tostring(rsiValue), style=label.style_label_down, color=color.white)
```
```