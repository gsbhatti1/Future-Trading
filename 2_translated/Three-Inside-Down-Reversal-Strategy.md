``` pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_CME","currency":"ES"}]
*/

//@version=5
indicator("Three Inside Down Reversal Strategy", overlay=true)

// Strategy Arguments
takeProfitPips = input(40, title="Take Profit pip")
stopLossPips = input(20, title="Stop Loss pip")

// Function to check if the pattern matches Three Inside Down criteria
isThreeInsideDown() =>
    // Check for Candlestick 1: Long upper shadow bullish candle
    isCandle1 = highest(high, 3) - open[1] > (close[1] - open[1]) * 0.8 and close[1] > open[1]

    // Check for Candlestick 2: Bearish candle that engulfs the first one
    isCandle2 = close < open and open >= close[1] and close >= open[1] and close[1] <= open

    // Check for Candlestick 3: Opening price below previous closing, and lower than its own lowest
    isCandle3 = open < close[2] and close < open[2]

    isCandle1 and isCandle2 and isCandle3

// Strategy Logic
if (isThreeInsideDown())
    strategy.entry("Buy", strategy.long)
    
    // Set Stop Loss and Take Profit levels
    strategy.exit("Exit Long", "Buy", stop = close - stopLossPips * pointSize, limit = close + takeProfitPips * pointSize)

// Plotting the pattern on chart
plotshape(series=isThreeInsideDown() ? open : na, title="Pattern Found", location=location.belowbar, color=color.green, style=shape.labelup, text="3ID")

```
```