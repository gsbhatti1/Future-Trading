``` pinescript
/*backtest
start: 2023-11-14 00:00:00
end: 2023-12-14 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 30/06/2020
// This is a combination strategy to generate a cumulative signal. 
//
// First strategy
// This system is based on the 123 Reversal System from the book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is a reversal type of strategy.
// The strategy goes long when the close price is higher than the previous close for 2 consecutive days 
// and the 9-day slow stochastic is below 50. 
// The strategy goes short when the close price is lower than the previous close for 2 consecutive days 
// and the 9-day fast stochastic is above 50.
//
// Second strategy
// The related article is copyrighted material from Stocks & Commodities Mar 2010
//
// WARNING:
// - This script is for educational purposes only.
// - It is intended to change bar colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
```