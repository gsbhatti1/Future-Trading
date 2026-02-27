```pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_CME","currency":"ES"}]
*/

//@version=5
indicator("Three Inside Down Reversal Strategy", overlay=false)

// Input Arguments
takeProfitPips = input(40, title="Take Profit pip")
stopLossPips = input(20, title="Stop Loss pip")

// Function to check Three Inside Down pattern
threeInsideDownCheck(c1, c2, c3) =>
    // Candle 1: Long upper shadow bullish candle
    longShadowBullish = (c1.high - c1.open > 0.5 * (c1.close - c1.open))
    
    // Candle 2: Bearish engulfing previous candle
    bearishEngulfing = (c2.close < c1.open and c2.open > c1.close)
    
    // Candle 3: Open below previous close, close below previous low
    openBelowPreviousClose = (c3.open < c2.close)
    closeBelowPreviousLow = (c3.low < c2.low)
    
    longShadowBullish and bearishEngulfing and openBelowPreviousClose and closeBelowPreviousLow

// Main logic
var float stopLossLevel = na
var bool entryConditionMet = false

if barstate.islast
    // Check for Three Inside Down pattern on the last three bars
    if threeInsideDownCheck(c1, c2, c3)
        // Set stop loss and entry condition
        stopLossLevel := close - stopLossPips * syminfo.mintick
        plotshape(series=stopLossLevel, title="Stop Loss", location=location.belowbar, color=color.red, style=shape.triangleup, size=size.small)
        label.new(x=bar_index, y=stopLossLevel, text="SL", textcolor=color.white, color=color.red, style=label.style_label_down)
        
        entryConditionMet := true

if entryConditionMet
    // Open long position at the opening price of the third candle
    strategy.entry("Three Inside Down", strategy.long, when=true)

    // Set stop loss and take profit levels
    strategy.exit("Take Profit", from_entry="Three Inside Down", limit=close + takeProfitPips * syminfo.mintick, stop=stopLossLevel)
```
```