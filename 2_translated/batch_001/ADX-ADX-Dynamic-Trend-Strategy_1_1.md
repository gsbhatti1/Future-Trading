> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2019|From Year|
|v_input_2|true|From Month|
|v_input_3|true|From Day|
|v_input_4|9999|To Year|
|v_input_5|true|To Month|
|v_input_6|true|To Day|
|v_input_7|14|ADX Smoothing|
|v_input_8|14|DI Period|
|v_input_9|23|Keylevel for ADX|
|v_input_10|3|Lookback Period for Slope|
|v_input_11|true|Use MA for Filtering?|
|v_input_12|0|MA Type For Filtering: EMA|SMA|
|v_input_13|200|MA Period for Filtering|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-07 00:00:00
end: 2024-01-14 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © millerrh with inspiration from @9e52f12edd034d28bdd5544e7ff92e 
// The intent behind this study is to
```