> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Take Profit pip|
|v_input_2|10|Stop Loss pip|
|v_input_3|true|Enter the number of bars over which to look for a new high in prices.|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2024-05-01 00:00:00
symbol: ETH/USD
currency: USD
 TickDataFrequency: 1
BarsCount: 7986
*/

//@version=5
strategy("Key Reversal Backtest Strategy", overlay=true)

// Input parameters
takeProfitPip = input.float(20, title="Take Profit pip")
stopLossPip = input.float(10, title="Stop Loss pip")
lookbackPeriod = input.int(34, title="Enter the number of bars over which to look for a new high in prices")

// Get the highest price in the last n periods
xHH = ta.highest(high, lookbackPeriod)

// Check if today's high is above xHH and yesterday's close was below the day before yesterday's close
C1 = (high >= xHH) and (close < close[1])

// Plot a triangle to indicate potential key reversal pattern today
plotshape(series=C1 ? true : na, title="Key Reversal", location=location.abovebar, color=color.red, style=shape.triangleup)

// Set stop loss and take profit levels based on pips
stopLossLevel = close - (stopLossPip * syminfo.mintick)
takeProfitLevel = close + (takeProfitPip * syminfo.mintick)

if (C1)
    strategy.entry("Short", strategy.short, when=C1)
    strategy.exit("Take Profit/Stop Loss", "Short", limit=takeProfitLevel, stop=stopLossLevel)

// Plot the stop loss and take profit levels
plot(stopLossLevel, color=color.blue, title="Stop Loss Level")
plot(takeProfitLevel, color=color.green, title="Take Profit Level")
```
```