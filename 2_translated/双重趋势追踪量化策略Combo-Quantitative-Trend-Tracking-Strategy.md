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

study("Combo-Quantitative-Trend-Tracking-Strategy", shorttitle="CQTTS")

// Input parameters for 123 Reversal Strategy
var bool input_1 = true
var int input_2 = 14
var bool input_3 = true
var int input_4 = 3
var int input_5 = 50

// Input parameters for Rainbow Oscillator Indicator
var bool input_6 = true
var int input_7 = 2
var int input_8 = 10
var bool input_9 = false

// Stochastic K and D lines
slowk, slowd = stoch(close, high, low, input_4)
fastk, fastd = stoch(high, low, close, input_4)

// Rainbow Oscillator Indicator values
ro_length = input(input_7, title="LengthRO")
ro_lookback = input(input_8, title="HHV/LLV Lookback")

highs = high[ro_lookback]
lows = low[ro_lookback]

ro = (highs + lows) / 2

// Buy condition
buy_condition = close[1] < close[2] and slowk < input_5 and not(input_9)
if buy_condition
    strategy.entry("Buy", strategy.long)

// Sell condition
sell_condition = close[1] > close[2] and fastd > input_5 and input_9
if sell_condition
    strategy.exit("Sell", "Buy")

```