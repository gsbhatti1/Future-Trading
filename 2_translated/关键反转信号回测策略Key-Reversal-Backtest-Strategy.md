> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Enter the number of bars over which to look for a new low in prices.|
|v_input_2|20|Take Profit pip|
|v_input_3|10|Stop Loss pip|


> Source (PineScript)
```pinescript
//@version=5
strategy("Key Reversal Backtest Strategy", overlay=true)

// Input parameters
newLowBars = input(true, title="Look for new low over bars")
takeProfitPips = input(20, title="Take Profit in pips")
stopLossPips = input(10, title="Stop Loss in pips")

// Helper function to find key reversal day
isKeyReversalDay(upTrend) =>
    if (upTrend)
        // For uptrend: lowest price of the day is a new low but close near previous low
        na(lowest(low, newLowBars)) or (low == lowest(low, newLowBars) and close > (close[1] - 0.001))
    else
        // For downtrend: lowest price of the day is a new low but close near previous high
        na(lowest(low, newLowBars)) or (low == lowest(low, newLowBars) and close < (high[1] + 0.001))

// Determine trend direction based on recent bars
upTrend = ta.crossover(close, highest(high, 2))
downTrend = ta.crossunder(close, lowest(low, 2))

// Check for key reversal day
keyReversalDay = isKeyReversalDay(upTrend) or isKeyReversalDay(downTrend)

// Enter long if downTrend and keyReversalDay
if (downTrend and keyReversalDay)
    strategy.entry("Long", strategy.long, when=keyReversalDay)

// Enter short if upTrend and keyReversalDay
if (upTrend and keyReversalDay)
    strategy.entry("Short", strategy.short, when=keyReversalDay)

// Set Take Profit and Stop Loss for each trade
strategy.exit("TakeProfitLong", "Long", profit=takeProfitPips * syminfo.mintick, loss=stopLossPips * syminfo.mintick)
strategy.exit("TakeProfitShort", "Short", profit=takeProfitPips * syminfo.mintick, loss=stopLossPips * syminfo.mintick)
```

This PineScript code implements the key reversal backtest strategy as described. It uses inputs for take profit and stop loss levels in pips, and identifies potential key reversal days based on price action over a specified number of bars.