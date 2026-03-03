``` pinescript
/*backtest
start: 2023-01-10 00:00:00
end: 2024-01-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © TradingAmmo

//@version=4
strategy("Linear Channel", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.075, currency='USD')
startP = timestamp(input(2017, "Start Year"), input(12, "Month"), input(17, "Day"), 0, 0)
end   = timestamp(input(9999, "End Year"),  1, 1,  0, 0)
_testPeriod() => true

//linreg
length = input(55)
linreg = linreg(close, length, 0)
plot(linreg, color=color.white) 

//calc band
Value = input(-2)
sub = (Value/100)+1
Band2 = linreg*sub
plot(Band2, color=color.red)

//HMA as a filter
HMA = input(400) // Adjusted from input(4) to match the strategy description
hma = hma(close, HMA)
plot(hma, color=color.blue)

// Strategy Logic
longCondition = close < Band2 and close < hma
if (longCondition)
    strategy.entry("Long", strategy.long)

// Exit Condition
exitCondition = close > linreg
if (exitCondition)
    strategy.close("Long")

// Plotting
plotshape(series=longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labeldown, text="Buy")
```

This Pine Script code implements the Linear Regression Channel strategy with the added Hull Moving Average (HMA) filter as described. The script includes the necessary logic to enter and exit trades based on the conditions specified.