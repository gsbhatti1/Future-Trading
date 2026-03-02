```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 19/09/2019
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
// This strategy uses CMO (Chande Momentum Oscillator) to determine price momentum over different time frames. The moving averages of CMO values are calculated over periods of 5, 10, and 20 days. If the average CMO value is above 70, a buy signal is generated; if below -70, a sell signal is generated.
//
// Combination strategy
// This strategy generates combined trading signals by performing an AND operation on the signals from both strategies. Only when both strategies give buy or sell signals simultaneously are actual trades triggered.

//@input v_input_1 = 14, "Length"
//@input v_input_2 = true, "KSmoothing"
//@input v_input_3 = 3, "DLength"
//@input v_input_4 = 50, "Level"
//@input v_input_5 = 5, "Length1"
//@input v_input_6 = 10, "Length2"
//@input v_input_7 = 20, "Length3"
//@input v_input_8 = 70, "TopBand"
//@input v_input_9 = -70, "LowBand"
//@input v_input_10 = false, "Trade reverse"

study("Momentum-Reversal-Combo-Strategy", shorttitle="MRC", overlay=true)

// First strategy: 123 Reversal
var long123 = na
var short123 = na

if (close[1] < close and close > close[2])
    if (stoch(close, high, low, v_input_4)[0] < v_input_4)
        long123 := not long123
if (close[1] > close and close < close[2])
    if (stochf(close, high, low, v_input_4)[0] > v_input_4)
        short123 := not short123

// Second strategy: CMO moving average
cmo = chaikin_momentum_index(close, v_input_1)
cmo_ma5 = sma(cmo, v_input_5)
cmo_ma10 = sma(cmo, v_input_6)
cmo_ma20 = sma(cmo, v_input_7)

average_cmo = (cmo_ma5 + cmo_ma10 + cmo_ma20) / 3

buy_signal = average_cmo > v_input_8
sell_signal = average_cmo < v_input_9

// Combination strategy: AND operation on signals
long_comb = long123 and buy_signal
short_comb = short123 and sell_signal

plotshape(series=long_comb, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")
plotshape(series=short_comb, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown, text="SELL")

// Optional: Trade reverse
if (v_input_10)
    strategy.entry("Long", strategy.long, when=long_comb)
    strategy.exit("Short", "Long", loss=v_input_9 * close)
else
    if (long_comb)
        strategy.entry("Long", strategy.long)
    if (short_comb)
        strategy.close("Long")
```

This script combines the 123 Reversal and CMO moving average strategies to generate combined trading signals. The first part of the script implements the 123 Reversal strategy, while the second part uses CMO values over different time frames to determine price momentum. The final section combines these signals using an AND operation to trigger actual trades.