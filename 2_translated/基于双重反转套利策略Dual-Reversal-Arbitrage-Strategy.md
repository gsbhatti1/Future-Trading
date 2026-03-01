> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|5|LengthGSO|
|v_input_6|false|Trade reverse|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-02-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 04/11/2020
// This is a combined strategy for getting a cumulative signal.
//
// First sub-strategy
// The 123 Reversal System: It originates from the book "How I Tripled My Money in The Futures Market" by Ulf Jensen, Page 183. 
// Trading rules are as follows:
// - Buy when the closing price is higher than the previous close during 2 days and the slow K line is below 50.
// - Sell short when the closing price is lower than the previous close during 2 days and the fast K line is above 50.

//@version=4
strategy("Dual-Reversal-Arbitrage-Strategy", overlay=true)

length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")
lengthGSO = input(5, title="LengthGSO")
tradeReverse = input(false, title="Trade reverse")

// 123 Reversal System
longCondition = close > close[1] and close < close[2] and sMA(close, length) < level
shortCondition = close < close[1] and close > close[2] and fMA(close, length) > level

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Gann Swing Oscillator
gSO = security(syminfo.tickerid, "D", high - low[1], lookahead=true)
gSO := gSO + gSO[1] * kSmoothing

plot(gSO, title="Gann Swing Oscillator")

// Combined Signal
combinedSignal = longCondition and shortCondition ? 1 : na
if (combinedSignal == 1)
    strategy.entry("Combined", strategy.long if not tradeReverse else strategy.short)

```

This script defines the dual-reversal arbitrage strategy by integrating two sub-strategies: the 123 Reversal System and Gann Swing Oscillator. It generates trading signals based on the conditions defined for each sub-strategy, with a combined signal that triggers trades when both sub-strategies align.