> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|34|Length Slow|
|v_input_6|5|Length Fast|
|v_input_7|false|Trade reverse|


> Source (PineScript)

```pinescript
//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 25/04/2019
// This is combo strategies for get 
// a cumulative signal. Result signal will return 1 if two strategies 
// is long, -1 if all strategies is short and 0 if signals of strategies is not equal.
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market, if close price is lower than the previous close price 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Secon strategy
// The Accelerator Oscillator has been developed by Bill Williams 
// as the development of the Awesome Oscillator. It represents the 
// difference between the Awesome Oscillator and the 5-period moving 
// average, and as such it shows the speed of change of the Awesome 
// Oscillator, which can be useful to find trend reversals before the 
// Awesome Oscillator does.
//
// WARNING:
// - For purpose educate only
// - This is not a trading advice or recommendation. Use at your own risk.
//
strategy("Double Signal Quantitative Reversal Strategy", overlay=false)

length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")
lengthSlow = input(34, title="Length Slow")
lengthFast = input(5, title="Length Fast")
tradeReverse = input(false, title="Trade reverse")

// First Strategy
var float[] buySignals1 = array.new_float(0)
var float[] sellSignals1 = array.new_float(0)

longCondition1 = close[2] > close[3] and stoch(close, high, low, length)[2] < level
if (longCondition1)
    array.push(buySignals1, 1)
array.push(sellSignals1, 0)

shortCondition1 = close[2] < close[3] and stochS(low, high, close, length)[2] > level
if (shortCondition1)
    array.push(sellSignals1, -1)
array.push(buySignals1, 0)

// Second Strategy
var float[] buySignals2 = array.new_float(0)
var float[] sellSignals2 = array.new_float(0)

longCondition2 = change(close) > 0 and crossunder(stochO(high, low, close, lengthFast), stochD(high, low, close, dLength))
if (longCondition2)
    array.push(buySignals2, 1)
array.push(sellSignals2, 0)

shortCondition2 = change(close) < 0 and crossover(stochO(high, low, close, lengthFast), stochD(high, low, close, dLength))
if (shortCondition2)
    array.push(sellSignals2, -1)
array.push(buySignals2, 0)

// Combine Signals
combinedSignal = na
if (array.size(buySignals1) > 0 and array.size(buySignals2) > 0)
    combinedSignal := 1
else if (array.size(sellSignals1) > 0 and array.size(sellSignals2) > 0)
    combinedSignal := -1

// Plot Signals
plot(combinedSignal, "Combined Signal", color=color.blue, linewidth=1)

// Trade Logic
if (combinedSignal == 1 and not tradeReverse)
    strategy.entry("Buy", strategy.long)
else if (combinedSignal == -1 and not tradeReverse)
    strategy.close("Buy")

if (combinedSignal == -1 and tradeReverse)
    strategy.entry("Sell", strategy.short)
else if (combinedSignal == 1 and tradeReverse)
    strategy.close("Sell")
```

This Pine Script implements the double signal quantitative reversal strategy, combining the 123 reversal strategy with the Accelerator Oscillator. It uses multiple conditions to determine buy/sell signals and provides a combined signal for trading decisions.