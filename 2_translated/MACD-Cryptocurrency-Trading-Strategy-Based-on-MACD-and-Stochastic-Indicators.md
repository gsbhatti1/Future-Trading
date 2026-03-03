> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|23|MACD Fast Length|
|v_input_2|50|MACD Slow Length|
|v_input_3|10|Cycle Length|
|v_input_4|3|1st %D Length|
|v_input_5|3|2nd %D Length|
|v_input_6_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_7|true|Highlight Breakouts ?|
|v_input_8|75|upper|
|v_input_9|25|lower|


> Source (PineScript)

```pinescript
//@version=5
strategy("Cryptocurrency Trading Strategy Based on MACD and Stochastic Indicators", shorttitle="MACD-Stoch Strategy", default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// Input Parameters
var int fastLength = input.int(23, minval=1, title="MACD Fast Length")
var int slowLength = input.int(50, minval=1, title="MACD Slow Length")
var int cycleLength = input.int(10, minval=1, title="Cycle Length")
var int fastK = input.int(3, minval=1, title="1st %K Length")
var int slowK = input.int(3, minval=1, title="2nd %K Length")

// Source Selection
var string sourceType = input.string("close", title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4")

// MACD Calculation
[macdLine, signalLine, _] = macd(close)

// Stochastic %K and %D Calculation
k = stoch(macdLine, signalLine, cycleLength)
[d1, d2, _] = stochrsi(k, fastK, slowK)

// Buy Signal
buySignal = k > 20 and d1 > 20

// Sell Signal
sellSignal = k < 80 and d1 < 80

if (buySignal)
    strategy.entry("Buy", strategy.long)

if (sellSignal)
    strategy.exit("Sell", "Buy")

// Plotting Breakout Highlights
plotshape(series=buySignal, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=sellSignal, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Plot MACD and Stochastic
hline(20, "Stochastic 20")
hline(80, "Stochastic 80")

plot(macdLine, title="MACD Line", color=color.blue)
plot(signalLine, title="Signal Line", color=color.red)
```