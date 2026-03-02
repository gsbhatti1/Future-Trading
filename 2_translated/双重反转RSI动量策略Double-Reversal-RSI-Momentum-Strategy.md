``` pinescript
/*backtest
start: 2023-08-26 00:00:00
end: 2023-09-25 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 17/06/2021
// This is a combo strategy for getting a cumulative signal.
//
// First Strategy
// This system was created from the book "How I Tripled My Money in the Futures Market" by Ulf Jensen, Page 183. It is a reversal-type strategy.
// The strategy goes long if the close price is higher than the previous close on two consecutive days and the value of the 9-day Stochastic Slow Oscillator is below 50.
// The strategy goes short if the close price is lower than the previous close on two consecutive days and the value of the 9-day Stochastic Fast Oscillator is above 50.
//
// Second Strategy
// This is a new-age indicator which calculates RSI based on the Rate-of-Change (ROC) indicator.
// The name "Relative Strength Index" might be misleading as the RSI does not compare the relative strength of two securities but rather the internal strength of a single security. A more appropriate name might be "Internal Strength Index." Relative strength charts that compare two market indices are often referred to as Comparative Relative Strength.
// In turn, the Rate-of-Change (ROC) indicator shows the difference between the current price and the price x-time periods ago. This difference can be displayed in points or as a percentage. The Momentum indicator displays the same information but expresses it as a ratio.
//
// WARNING:
// - For educational purposes only
// - This script is used to change bar colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2]