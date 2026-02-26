> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|0|MA Type: SMA|EMA|WMA|VWMA|HMA|SMMA|DEMA|
|v_input_2|5|Short MA Length|
|v_input_3_close|0|Short MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|20|Medium MA Length|
|v_input_5_close|0|Medium MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|100|Long MA Length|
|v_input_7_close|0|Long MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_8|false|SL Level % (0 - Off)|
|v_input_9|false|PT Level % (0 - Off)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-08 00:00:00
end: 2024-01-15 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("Kozlod - 3 MA strategy with SL/PT", shorttitle="kozlod_3ma", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 5)

// 
// author: Kozlod
// date: 2018-03-25
// 

////////////
// INPUTS //

```