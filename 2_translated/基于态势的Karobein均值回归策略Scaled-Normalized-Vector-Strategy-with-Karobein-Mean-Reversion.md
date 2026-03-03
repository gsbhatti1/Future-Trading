> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Price Data: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|34|Timeframe|
|v_input_3|14|Threshold|
|v_input_4|0|Divisor: 1000000|10|100|1000|10000|100000|1|10000000|100000000|
|v_input_5|false|Volume|
|v_input_6|true|Use Old System|
|v_input_7|8|Karobein Osc Lookback|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-27 00:00:00
end: 2023-11-02 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// author: capissimo
strategy("Normalized Vector Strategy, ver.3 (sc)", precision=2, overlay=false)
// This is a scaled Normalized Vector Strategy with a Karobein Oscillator
// original: Drkhodakarami (https://www.tradingview.com/script/Fxv2xFWe-Normalized-Vector-Strategy-By-Drkhodakarami-Opensource/)

// Repainting: in general there two types of repainting:
// * when the last candle is constantly being redrawn
// * when the indicator draws a different configuration after it has been deactivated/reactivated, i.e. refreshed

// The former is a natural behaviour, which presents a constant source of frustration, 
// when a signal directly depends on the current market situation and can be overcome 
// with various indirect techniques like divergence.

// The latter suggests a flaw in the indicator design.
// Unfortunately, the Normalized Vector Strategy is repainting in the latter sense, although being
```