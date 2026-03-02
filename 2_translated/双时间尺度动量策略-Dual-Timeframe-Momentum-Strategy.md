> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|Moving Average Period|
|v_input_source_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_timeframe_1|240|Resolution|
|v_input_int_2|5|Pivot Let Bars|
|v_input_int_3|2|Pivot Right Bars|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-04-19 00:00:00
end: 2024-04-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Riester

//@version=5
strategy("Dual Timeframe Momentum", overlay=true, precision=6, pyramiding=0, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=25.0, commission_value=0.05)

n = input.int(20, "Moving Average Period", minval=1)
src = input.source(close, "Source")
high_tf = input.timeframe("240", "Resolution")
pivot_l = input.int(5, "Pivot Let Bars")
pivot_r = input.int(2, "Pivot Right Bars")

//-------
```