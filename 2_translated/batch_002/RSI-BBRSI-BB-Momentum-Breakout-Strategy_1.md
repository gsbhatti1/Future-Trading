> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|50|length|
|v_input_2|0.2|Mult Factor|
|v_input_3|0.1|alertLevel|
|v_input_4|0.75|impulseLevel|
|v_input_5|false|showRange|
|v_input_6|250|TP|
|v_input_7|20|SL|
|v_input_8|false|TS|


> Source (PineScript)

```pinescript
//@version=4
// Based on Larry Connors RSI-2 Strategy - Lower RSI
strategy(title="RSI-BB Momentum Breakout", shorttitle="RSI-BBMBS", overlay=true)

length = input(50, title="Length")
multFactor = input(0.2, title="Multiplier Factor")
alertLevel = input(0.1, title="Alert Level")
impulseLevel = input(0.75, title="Impulse Level")
showRange = input(false, title="Show Range", type=checkbox)
takeProfit = input(250, title="Take Profit", minval=1)
stopLoss = input(20, title="Stop Loss", minval=1)
trailStop = input(false, title="Trail Stop", type=checkbox)

basis = sma(close, length)
dev = multFactor * stdev(close, length)
upper = basis + dev
lower = basis - dev

bbr = close > upper ? 1 : close < lower ? -1 : 0
bbi = bbr - bbr[1]

longCondition = rsi(close) > 52 and rsi(close) < 65 and bbi > alertLevel and bbi < impulseLevel
shortCondition = rsi(close) < 48 and rsi(close) > 35 and bbi < -alertLevel and bbi > -impulseLevel

plotshape(series=longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

if (longCondition)
    strategy.entry("Long", strategy.long)
    if (showRange)
        label.new(x=bar_index, y=high + takeProfit, text="TP: " + tostring(takeProfit), color=color.green, textcolor=color.white, style=label.style_label_down, size=size.small)

if (shortCondition)
    strategy.entry("Short", strategy.short)
    if (showRange)
        label.new(x=bar_index, y=low - stopLoss, text="SL: " + tostring(stopLoss), color=color.red, textcolor=color.white, style=label.style_label_up, size=size.small)

plot(basis, color=color.blue, title="Basis")
fill(basis, upper, color=color.blue)
fill(basis, lower, color=color.blue)
```