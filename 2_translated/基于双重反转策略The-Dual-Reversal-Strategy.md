```pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 17/04/2019
// This is a combo strategy for getting 
// a cumulative signal. The result signal will return 1 if two strategies 
// are both long, -1 if all strategies are short, and 0 if signals of the strategies are not equal.
//
// First Strategy
// This system was created from the book "How I Tripled My Money In The Futures Market" by Ulf Jensen, Page 183. This is a reverse type of strategy.
// The strategy buys at market if the close price is higher than the previous close during two days and 
// the meaning of the 9-day Stochastic Slow Oscillator is lower than 50.
// The strategy sells at market if the close price is lower than the previous close for two days and
// the meaning of the 9-day Stochastic Fast Oscillator is higher than 50.

study("Dual Reversal Strategy", shorttitle="DualReversal")

length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")
tradeReverse = input(false, title="Trade reverse")

// 9-day Stochastic Oscillator
k = sma(close, 14) - sma(sma(close, 14), 14)
d = sma(k, dLength)

longCondition = crossover(d, level)
shortCondition = crossunder(d, level)

// 123 Reversal Strategy
var int buySignal = na
buySignal := close[2] > close[1] and (high[dLength+2] < high[dLength+1] or low[dLength+2] < low[dLength+1]) ? 1 : na
buySignal := buySignal and close[1] > close[0] ? 1 : na

var int sellSignal = na
sellSignal := close[2] < close[1] and (high[dLength+2] > high[dLength+1] or low[dLength+2] > low[dLength+1]) ? -1 : na
sellSignal := sellSignal and close[1] < close[0] ? -1 : na

// Cumulative Signal
long = buySignal == 1 and shortCondition
short = sellSignal == -1 and longCondition

plotshape(series=long, title="Long Entry", location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")
plotshape(series=short, title="Short Entry", location=location.abovebar, color=color.red, style=shape.labeldown, text="SELL")

// Strategy Execution
if (long)
    strategy.entry("Long", strategy.long)

if (short)
    strategy.close("Long")

```