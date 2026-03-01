``` pinescript
/*backtest
start: 2022-09-14 00:00:00
end: 2023-06-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
// @CoinDigger
//
// Credits for the base strategy go to HPotter
//
// I've just added a trail stop, basic leverage simulation and stop loss
//
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 28/01/2021
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
// MACD – Moving Average Convergence Divergence. The MACD is calculated 
// by subtracting a 26-day moving average of a security's price from a 
// 12-day moving average of its price. The result is an indicator that 
// oscillates above and below zero. When the MACD is above zero, it means 
// the 12-day moving average is higher than the 26-day moving average. 
// This is bullish as it shows that current expectations (i.e., the 12-day 
// moving average) are more bullish than previous expectations (i.e., the 
// 26-day average). This implies a bullish, or upward, shift in the supply/demand 
// lines. When the MACD falls below zero, it means
```