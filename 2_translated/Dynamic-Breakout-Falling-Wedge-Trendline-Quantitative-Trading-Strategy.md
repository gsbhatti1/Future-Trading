```pinescript
/*backtest
start: 2024-02-22 00:00:00
end: 2025-02-19 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/

//@version=6
strategy("Falling Wedge Strategy by Nitin", overlay=true, margin_long=100, margin_short=100)

// Input parameters
leftBars = input.int(5, "Left Bars for Pivot", minval=1, maxval=20)
rightBars = input.int(5, "Right Bars for Pivot", minval=1, maxval=20)
takeProfitPercent = input.float(20, "Take Profit %", minval=0.1, maxval=100)/100
stopLossPercent = input.float(2, "Stop Loss %", minval=0.1, maxval=100)/100

// Global variables
var float buyPrice = na
var line upperLine = na
var line lowerLine = na

// Detect pivot highs and lows
ph = ta.pivothigh(leftBars, rightBars)
pl = ta.pivotlow(leftBars, rightBars)

// Track last two pivot highs
var float[] highs = array.new_float()
var int[] highIndices = array.new_int()
if not na(ph)
    array.unshift(highs, ph)
    array.unshift(highIndices, bar_index[rightBars])
    if array.size(highs) > 2
        array.pop(highs)
        array.pop(highIndices)

// Track last two pivot lows
var float[] lows = array.new_float()
var int[] lowIndices = array.new_int()
if not na(pl)
    array.unshift(lows, pl)
    array.unshift(lowIndices, bar_index[rightBars])
    if array.size(lows) > 2
        array.pop(lows)
        array.pop(lowIndices)

// Calculate trendlines
if array.size(highs) == 2 and array.size(lows) == 2
    upperLine = line.new(bar_index[highIndices[1]], highs[1], bar_index[highIndices[0]], highs[0], xloc=xloc.bar_index)
    lowerLine = line.new(bar_index[lowIndices[1]], lows[1], bar_index[lowIndices[0]], lows[0], xloc=xloc.bar_index)

// Breakout condition
if not na(upperLine) and close > upperLine
    buyPrice := close
    strategy.entry("Long Entry", strategy.long)
    
// Set take profit and stop loss
strategy.exit("Take Profit", "Long Entry", profit=takeProfitPercent * close, loss=stopLossPercent * close)

// Plot trendlines on chart
plot(upperLine, color=color.red, linewidth=2)
plot(lowerLine, color=color.blue, linewidth=2)
```

This code completes the Pine Script for the dynamic breakout falling wedge strategy. It includes the necessary logic to track pivot highs and lows, calculate trend lines, and generate entry signals based on a price break above the upper trendline. The script also sets up take profit and stop loss levels as specified in the input parameters.