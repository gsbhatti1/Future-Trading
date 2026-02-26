> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- Awesome Oscillator (AC) ----|
|v_input_7|34|Length Slow|
|v_input_8|5|Length Fast|
|v_input_9|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-01 00:00:00
end: 2023-10-31 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 09/08/2021
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than previous for 2 consecutive days and 9-day Slow Stochastic is below 50.
// It sells short when the close price is lower than previous for 2 consecutive days and 9-day Fast Stochastic is above 50.

//@version=4
strategy("Wealth-Creation-Composite-Strategy", overlay=true)

// 123 Reversal Strategy
length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")

longCondition123 = close[1] < close and close > close[1] and stoch(kSmoothing, dLength, length)[1] < level
shortCondition123 = close[1] > close and close < close[1] and stoch(kSmoothing, dLength, length) > level

// Awesome Oscillator Strategy
lengthSlow = input(34, title="Length Slow")
lengthFast = input(5, title="Length Fast")

ao = ta.ao(lengthSlow, lengthFast)
buyConditionAO = ao[1] > 0
sellConditionAO = ao[1] < 0

// Combined Signal Generation
longSignal = longCondition123 and buyConditionAO
shortSignal = shortCondition123 and sellConditionAO

if (longSignal) 
    strategy.entry("Long", strategy.long)

if (shortSignal)
    strategy.entry("Short", strategy.short)

if (v_input_9 == true)  // Trade reverse flag
{
    if (not longCondition123 and buyConditionAO)
        strategy.close("Long")
    
    if (not shortCondition123 and sellConditionAO)
        strategy.close("Short")
}
```