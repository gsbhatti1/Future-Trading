``` pinescript
/*backtest
start: 2023-11-20 00:00:00
end: 2023-12-20 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 31/05/2021
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
// The indicator represents the relative convergence/divergence of the moving 
// averages of the financial asset, increased a hundred times. It is based on 
// a different principle than the ADX. Chande suggests a 13-week SMA as the 
// basis for the indicator. It represents the quarterly (3 months = 65 working days) 
// sentiments of the market participants concerning prices. The short moving average 
// comprises 10% of the one and is rounded to seven.
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing)
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] < close[1] and close > close[1] and vFast < vSlow, 1, pos)
    pos := iff(close[2] > close[1] and close < close[1] and vFast > vSlow, -1, pos)

RAVI(LengthMAFast, LengthMASlow, TradeLine) =>
    maFast = sma(close, LengthMAFast)
    maSlow = sma(close, LengthMASlow)
    pos := iff((maFast - maSlow) > TradeLine, 1, pos)
    pos := iff((maFast - maSlow) < -TradeLine, -1, pos)

//@inputs
v_input_1 = input(true, title="123 Reversal")
v_input_2 = input(14, title="Length")
v_input_3 = input(true, title="KSmoothing")
v_input_4 = input(3, title="DLength")
v_input_5 = input(50, title="Level")
v_input_6 = input(true, title="RAVI")
v_input_7 = input(7, title="Length MA Fast")
v_input_8 = input(65, title="Length MA Slow")
v_input_9 = input(0.14, title="TradeLine")
v_input_10 = input(false, title="Trade reverse")

// Strategy logic
longCondition = v_input_1 ? (Reversal123(v_input_2, v_input_3, v_input_4, v_input_5) == 1 and RAVI(v_input_7, v_input_8, v_input_9) == 1) : false
shortCondition = v_input_1 ? (Reversal123(v_input_2, v_input_3, v_input_4, v_input_5) == -1 and RAVI(v_input_7, v_input_8, v_input_9) == -1) : false

strategy("Dual-Indicator-Quantitative-Strategy", overlay=true)
plotshape(series=longCondition, title="Long Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Short Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

if (v_input_10) and longCondition
    strategy.entry("Long", strategy.long)
if not(v_input_10) and shortCondition
    strategy.close("Long")
```