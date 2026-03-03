``` pinescript
/*backtest
start: 2023-11-12 00:00:00
end: 2023-12-12 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 15/04/2021
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
// The Performance indicator or a more familiar term, KPI (key performance indicator), 
// is an industry term that measures the performance. Generally used by organizations, 
// they determine whether the company is successful or not, and the degree of success. 
// It is used on a business’ different levels, to quantify the progress or regress of a 
// department, of an employee or even of a certain program or activity. For a manager 
// it’s extremely important to determine which KPIs are relevant for his activity, and 
// what is important almost always depends on which department he wants to measure the 
// performance for.  So the indicators set for the financial team will be different than 
// the ones for the marketing department and so on.
//
// Similar to the KPIs companies use to measure their performance on a monthly, quarterly 
// and yearly basis, the stock market makes use of a performance indicator as well, although 
// on the market, the performance index is calculated on a daily basis. The stock market 
// performance indicates the direction of the stock market and can be used to guide trading 
// decisions.
//
// This strategy uses a performance index calculated over the past 14 days to generate 
// buy and sell signals. If the performance index is positive, it generates a bullish signal, 
// and if negative, a bearish signal.
//
// The final signal is the combination of both signals. That is, same direction bullish/bearish 
// signals are required to generate actual buy/sell operations.
//
// This can filter out some noise and make the signals more reliable.
//
// Advantages of the strategy:
// 1. More reliable signals by combining dual factors
// 2. Can effectively filter market noise and avoid false signals
// 3. 123 pattern is classic and practical, easy to judge and reproduce
// 4. Performance index can judge future trend direction
// 5. Flexible parameter combination, can be further optimized
//
// Risks of the strategy:
// 1. May miss sudden reversals, cannot fully capture trends
// 2. Dual signal combinations lead to fewer signals, which may affect profitability
// 3. Requires consistent judgment, easily affected by individual stock fluctuations
// 4. Parameter setting problems may lead to signal deviations
//
// Optimizations can be considered:
// 1. Adjust parameters like K-line length, Stochastic cycle etc.
// 2. Optimize the logic for dual signal judgment
// 3. Incorporate more factors like volume etc.
// 4. Add stop loss mechanism
//
// Summary
// The strategy integrates dual reversal judgments to effectively discover price inflection points. 
// Although the probability of signal occurrence decreases, the reliability is higher, suitable for 
// capturing medium and long term trends. The strategy effect can be further enhanced through 
// parameter adjustment and multi-factor optimization.
*/
strategy("Dual-Reversal-Trend-Tracking-Strategy", overlay=true)

// Inputs
input_1 = input(true, title="123 Reversal")
input_2 = input(14, title="Length")
input_3 = input(true, title="KSmoothing")
input_4 = input(3, title="DLength")
input_5 = input(50, title="Level")
input_6 = input(true, title="Performance Index")
input_7 = input(14, title="Period")
input_8 = input(false, title="Trade reverse")

// Variables
var float bull_signal = na
var float bear_signal = na

// 123 Reversal Strategy
if (input_1)
    if (close[2] < close[1] and close < close[1] and stochslow(9, 3, 3)[1] < 50)
        bull_signal := 1
    else if (close[2] > close[1] and close > close[1] and stochfast(9, 3, 3)[1] > 50)
        bear_signal := -1

// Performance Index Strategy
if (input_6)
    perf_index = (close - close[14]) / close[14]
    if (perf_index > 0)
        bull_signal := 1
    else if (perf_index < 0)
        bear_signal := -1

// Final Signal
if (bull_signal == 1 and bear_signal == 1 and not input_8)
    strategy.entry("Buy", strategy.long)
if (bull_signal == -1 and bear_signal == -1 and not input_8)
    strategy.close("Buy")

// Plot signals
plot(bull_signal, color=color.green, title="Bullish Signal", style=plot.style_circles)
plot(bear_signal, color=color.red, title="Bearish Signal", style=plot.style_circles)
```

This Pine Script implements the described dual-reversal trend tracking strategy. The script first defines the input parameters, then calculates the signals based on the 123 reversal strategy and the performance index strategy, and finally combines these signals to generate buy and sell orders.