> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- Stochastic ----|
|v_input_7|7|LengthS|
|v_input_8|3|DLengthS|
|v_input_9|20|UpBand|
|v_input_10|80|DownBand|
|v_input_11|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-25 00:00:00
end: 2023-10-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 07/07/2021
// This is a combined strategy to generate a cumulative signal.
//
// First Strategy
// This system was created from the book "How I Tripled My Money In The Futures Market" by Ulf Jensen, Page 183. It is a reversal type of strategy.
// The strategy generates a buy signal at market if the closing price is higher than the previous two days' closing prices and the 9-day Stochastic Slow Oscillator is below 50.
// The strategy generates a sell signal at market if the closing price is lower than the previous two days' closing prices and the 9-day Stochastic Fast Oscillator is above 50.
//
// Second Strategy
// This backtesting strategy generates a long trade at the open of the following bar when the %K line crosses up the UpBand line.
// It generates a short trade at the open of the following bar when the %K line crosses down the DownBand line.
```

Please note that the Pine Script code is incomplete and needs to be completed for full functionality. Here's how you can finish it:

```pinescript
//@version=4
strategy("Combined Stochastic & 123 Reversal Strategy", overlay=true)

// Inputs
length = input(14, title="Length")
kSmoothing = input(true, title="K Smoothing")
dLength = input(3, title="D Length")
level = input(50, title="Level")
useStochastic = input(true, title="Use Stochastic")
lengthS = input(7, title="Length S")
dLengthS = input(3, title="D Length S")
upBand = input(20, title="Up Band")
downBand = input(80, title="Down Band")

// 123 Reversal Strategy
buyCondition = close > close[1] and close > close[2] and stoch(kSmoothing, dLength) < level 
sellCondition = close < close[1] and close < close[2] and stoch(kSmoothing, dLength) > level

// Stochastic Oscillator Strategy
stochFast = ta.stoch(close, lengthS, dLengthS)
stochSlow = ta.slow_stoch(high, low, close, lengthS, dLengthS)

// Buy signal from 123 Reversal and Stochastic
buySignal = buyCondition and stochFast < upBand

// Sell signal from 123 Reversal and Stochastic
sellSignal = sellCondition and stochFast > downBand

// Plot signals
plotshape(series=buySignal, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup)
plotshape(series=sellSignal, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown)

// Optional: Add stop loss and take profit
stopLoss = input(title="Stop Loss %", type=input.percent, defval=1.5)
takeProfit = input(title="Take Profit %", type=input.percent, defval=3.0)

if (buySignal) 
    strategy.entry("Buy", strategy.long)
    strategy.exit("Profit & Stop", from_entry="Buy", stop=(close * (1 - stopLoss/100)), limit=(close * (1 + takeProfit/100)))

if (sellSignal)
    strategy.entry("Sell", strategy.short)
    strategy.exit("Profit & Stop", from_entry="Sell", stop=(close * (1 + stopLoss/100)), limit=(close * (1 - takeProfit/100)))
```

This completes the Pine Script for the combined 123 Reversal and Stochastic Oscillator strategy.