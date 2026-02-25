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
// The strategy buys at market, if close price is higher than the previous day's closing price for two consecutive days and the 9-day moving average of slow K-line is below 50.

strategy("123 Reversal & STARC Bands Combo Strategy", overlay=false)

if (v_input_1)
    // 123 Reversal Logic
    var bool long_signal = false
    var bool short_signal = false
    
    if (close > close[1] and close > close[2] and sma(close, v_input_2) < v_input_5)
        long_signal := true
    else if (close < close[1] and close < close[2] and sma(close, v_input_2) > v_input_5)
        short_signal := true

if (v_input_6)
    // STARC Bands Logic
    lenMA = input(5, minval=1, title="Length MA")
    lenATR = input(15, minval=1, title="Length ATR")
    k = input(1.33, minval=0.01, title="K")

    src = close
    upper_band = sma(src, lenMA) + (atr(lenATR) * k)
    lower_band = sma(src, lenMA) - (atr(lenATR) * k)

    if (cross(close, upper_band))
        strategy.entry("Buy", strategy.long)
    
    if (cross(lower_band, close))
        strategy.exit("Sell", "Buy")
```

Please note that the Pine Script code needs to be further refined and tested for practical usage. The provided script is a basic implementation of the described strategies combined in a single script.