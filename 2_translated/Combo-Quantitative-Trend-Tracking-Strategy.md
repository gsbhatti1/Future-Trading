``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 25/05/2021
// This is combo strategies for get a cumulative signal.
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market, if close price is lower than the previous close price 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Second strategy
// Ever since the people concluded that stock market price movements are not 
// random or chaotic, but follow specific trends that can be forecasted, they 
// tried to develop different tools or procedures that could help them identify 
// those trends. And one of those financial indicators is the Rainbow Oscillator 
// Indicator. The Rainbow Oscillator Indicator is relatively new, originally 
// introduced in 1997, and it is used to forecast the changes of trend direction.
// As market prices go up and down, the oscillator appears as a direction of the 
// trend, but also as the safety of the market and the depth of that trend. As 
// the rainbow grows in width, the current trend gives signs of continuity, and 
// if the value of the oscillator goes beyond 80, the market becomes more and more 
// unstable, being prone to a sudden reversal. When prices move towards the rainbow 
// and the oscillator becomes more and more flat, the market tends to remain more 
// stable and the bandwidth decreases. Still, if the oscillator value goes below 20, 
// the market is again, prone to sudden reversals. The safest bandwidth value where 
// the market is stable is between 20 and 80, in the Rainbow Oscillator indicator value. 
// The depth a certain price has on a chart and into the rainbow can be used to judge 
// the strength of the move.
//
// WARNING:
// - For purpose educate only
*/

study("双重趋势追踪量化策略", shorttitle="Combo-Quantitative-Trend-Tracking-Strategy", overlay=true)

// Input parameters
var input1 = input(true, title="---- 123 Reversal ----")
length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")
input6 = input(true, title="---- Rainbow Oscillator ----")
lengthRO = input(2, title="LengthRO")
hhvllvLookback = input(10, title="HHV/LLV Lookback")
tradeReverse = input(false, title="Trade reverse")

// 123 Reversal Strategy
longCondition = close[2] < close and close > close[1] and stochs(kSmoothing, dLength)[9] < level
shortCondition = close[2] > close and close < close[1] and stochf(kSmoothing, dLength)[9] > level

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Rainbow Oscillator Strategy
rsi = rsi(close, lengthRO) / 100
oscillatorValue = vwap(hhv(close, hhvllvLookback), llv(close, hhvllvLookback)) - close

if (oscillatorValue > 80 or oscillatorValue < 20)
    if (tradeReverse and strategy.is_long)
        strategy.close("Long")
    else
        strategy.close("Short")

// Plotting
plot(rsi, title="RSI", color=color.blue)
plot(oscillatorValue, title="Rainbow Oscillator", color=color.red)

// Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- Rainbow Oscillator ----|
|v_input_7|2|LengthRO|
|v_input_8|10|HHV/LLV Lookback|
|v_input_9|false|Trade reverse|
```