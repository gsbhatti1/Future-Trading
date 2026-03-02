``` pinescript
/*backtest
start: 2023-11-06 00:00:00
end: 2023-12-06 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 18/10/2019
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
// The related article is copyrighted material from Stocks & Commodities 2009 Oct 
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing)
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > Level, 1,
             iff(close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < Level, -1, nz(pos[1], 0)))
    pos

fFilter(xSeriesSum, xSeriesV, Filter) =>
    iff(xSeriesV > Filter, xSeriesSum, 0)

EMA_VW(Length) =>
    pos = 0.0
    xMAVolPrice = ema(volume * close, Length)
    xMAVol = ema(volume, Length)
    nRes = xMAVolPrice / xMAVol
    pos := iff(nRes < close[1], 1,
             iff(nRes > close[1], -1, nz(pos[1], 0)))
    pos

strategy("Comb-Reverse-EMA-Volume-Weighting-Optimization-Trading-Strategies", overlay = true)

longCondition = Reversal123(v_input_1, v_input_2, v_input_3, v_input_4) > 0 and fFilter(0, nRes, v_input_5)
shortCondition = Reversal123(v_input_1, v_input_2, v_input_3, v_input_4) < 0 and fFilter(0, nRes, v_input_5)

if (longCondition)
    strategy.entry("Long", strategy.long)
if (shortCondition)
    strategy.entry("Short", strategy.short)

plotshape(series = longCondition, location = location.belowbar, color = color.green, style = shape.labelup, title = "Long Entry")
plotshape(series = shortCondition, location = location.abovebar, color = color.red, style = shape.labeldown, title = "Short Entry")

```