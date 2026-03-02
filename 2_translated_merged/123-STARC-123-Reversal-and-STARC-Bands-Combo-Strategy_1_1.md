> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- STARC Bands ----|
|v_input_7|5|LengthMA|
|v_input_8|15|LengthATR|
|v_input_9|1.33|K|
|v_input_10|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-26 00:00:00
end: 2023-12-03 00:00:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 28/07/2021
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous closing price for two consecutive days and the 9-day moving average of the slow K-line is below 50.
// It sells short, if close price is lower than the previous closing price for two consecutive days and the 9-day moving average of the fast K-line is above 50.
//
// Second strategy
// This system judges trend direction by plotting bands around a short-term simple moving average of the price. 
// The upper band is constructed by adding average true range (ATR) to the moving average, while the lower band is constructed by subtracting ATR from the moving average. 
// Breaking above the upper band indicates an uptrend, and breaking below the lower band indicates a downtrend.
//
// STARC stands for Stoller Average Range Channels. The indicator is named after its creator, Manning Stoller.

//@input v_input_1 = true
//@input v_input_2 = 14
//@input v_input_3 = true
//@input v_input_4 = 3
//@input v_input_5 = 50
//@input v_input_6 = true
//@input v_input_7 = 5
//@input v_input_8 = 15
//@input v_input_9 = 1.33
//@input v_input_10 = false

// Define variables for the 123 Reversal strategy
var int count_123_reversal = na
var bool is_123_buy = na
var bool is_123_sell = na

if close > close[1] and close > close[2] and sma(close, v_input_2) < v_input_5
    is_123_buy := true
else if close < close[1] and close < close[2] and sma(close, v_input_2 * 9 / v_input_4) > v_input_5
    is_123_sell := true

// Define variables for the STARC Bands strategy
var float upper_band = na
var float lower_band = na

src = close
lengthma = v_input_7
lengthatr = v_input_8
k = v_input_9

sma(src, lengthma) => sma
atr_length = lengthatr
trange = highest(high - low, atr_length) + lowest(low - high, atr_length)

upper_band := sma + k * atr
lower_band := sma - k * atr

strategy.entry("123 Reversal Buy", strategy.long, when=is_123_buy)
strategy.exit("123 Reversal Sell", "123 Reversal Buy", when=is_123_sell)

if v_input_6 and is_123_buy
    upper_band := sma(close, lengthma) + k * atr_length(src, atr_length)
    lower_band := sma(close, lengthma) - k * atr_length(src, atr_length)

plot(upper_band, color=color.red, title="Upper Band")
plot(lower_band, color=color.blue, title="Lower Band")

if v_input_10
    strategy.close("123 Reversal Buy", when=is_123_sell)
```

This script combines the 123 Reversal and STARC Bands strategies to generate more reliable trading signals.