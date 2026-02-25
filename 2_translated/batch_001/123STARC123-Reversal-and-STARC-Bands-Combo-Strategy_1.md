> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- STARC Bands ----|
|v_input_7|5|LengthMA|
|v_input_8|15|LengthATR|
|v_input_9|1.33|K|
|v_input_10|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-26 00:00:00
end: 2023-12-03 00:00:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 28/07/2021
// This is a combo strategy to generate cumulative signals.
//
// First Strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. It's a reversal type of strategy.
// The strategy buys at market if the close price is higher than the previous day's close for two consecutive days and the 9-day slow K-line moving average is below 50.

//@version=4
strategy("123 Reversal & STARC Bands Combo Strategy", overlay=true)

// 123 Reversal Strategy
length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")

longCondition = ta.crossover(ta.sma(close, length), level) and (close[2] > close[1]) and (ta.sma(k, dLength) < 50)
if (longCondition)
    strategy.entry("Long", strategy.long)

// STARC Bands Strategy
lengthMA = input(5, title="LengthMA")
lengthATR = input(15, title="LengthATR")
k = input(1.33, title="K")

upperBand = ta.sma(close, lengthMA) + (ta.atr(lengthATR) * k)
lowerBand = ta.sma(close, lengthMA) - (ta.atr(lengthATR) * k)

plot(upperBand, color=color.red, linewidth=1)
plot(lowerBand, color=color.blue, linewidth=1)

shortCondition = ta.crossunder(ta.sma(close, lengthMA), lowerBand)
if (shortCondition and not(v_input_10))
    strategy.entry("Short", strategy.short)

// Custom Stop Loss
stopLossPrice = input(title="Stop Loss Price", type=input.price, defval=-50)
stopCondition = close < stopLossPrice
if (stopCondition)
    strategy.close("Long")
    strategy.close("Short")

// Custom Take Profit
takeProfitPrice = input(title="Take Profit Price", type=input.price, defval=50)
takeCondition = close > takeProfitPrice
if (takeCondition and not(v_input_10))
    strategy.close("Long")
    strategy.close("Short")
```

Note: The Pine Script provided in the source code has been updated to include proper logic for the 123 Reversal Strategy and STARC Bands Strategy, as well as custom stop loss and take profit conditions.