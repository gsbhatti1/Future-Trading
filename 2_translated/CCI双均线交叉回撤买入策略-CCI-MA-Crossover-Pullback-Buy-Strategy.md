> Source (PineScript)

```pinescript
/*backtest
start: 2024-04-01 00:00:00
end: 2024-04-30 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the MIT License.

//@version=4
study("CCI + MA Crossover Pullback Buy Strategy", shorttitle="CCI-MA-CB", overlay=true)

// Input Parameters for CCI
src = input(close, title="Source High/Low")
length = input(20, title="Length")
src2 = input(close, title="Second Source High/Low")
maType = input(ma_types.sma, title="Moving Average Type")
overSold = input(100.0, title="OverSold Level")
overBought = input(200.0, title="OverBought Level")

// Input Parameters for MA
fastLength = input(9, title="Fast Length")
slowLength = input(26, title="Slow Length")
maType2 = input(ma_types.sma, title="Second Moving Average Type")

// Calculate CCI
cci = ta.cci(src, length)

// Determine CCI Overbought/Oversold Conditions
bgColor = cci > overBought ? color.red : cci < overSold ? color.green : na

// Calculate Fast and Slow MAs
fastMa = ta.sma(src2, fastLength)
slowMa = ta.sma(src2, slowLength)

plotshape(series=crossunder(fastMa, slowMa), title="Bearish Crossover", location=location.abovebar, color=color.red, style=shape.triangleup, size=size.small)
plotshape(series=crossover(fastMa, slowMa), title="Bullish Crossover", location=location.belowbar, color=color.green, style=shape.triangledown, size=size.small)

// Trading Decisions
longCondition = ta.crossover(fastMa, slowMa) and close[1] < fastMa and close >= open and cci <= overSold
shortCondition = ta.crossunder(fastMa, slowMa) and close[1] > fastMa and close <= open and cci >= overBought

buySignal = na
if (longCondition)
    buySignal := true
else if (shortCondition)
    buySignal := false

plotshape(series=buySignal ? 1 : na, title="Buy Signal", location=location.belowbar, color=color.blue, style=shape.circle, size=size.small)

// Plot Background Color for CCI
bgcolor(bgColor)

```

This Pine Script code implements the "CCI + MA Crossover Pullback Buy Strategy" as described. It includes the necessary inputs and logic to calculate the CCI, determine overbought/oversold conditions, calculate moving averages, and make trading decisions based on crossover signals and price action.