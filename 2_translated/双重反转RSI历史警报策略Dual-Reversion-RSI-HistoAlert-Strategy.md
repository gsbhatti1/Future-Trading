> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- RSI HistoAlert ----|
|v_input_7|13|RSIPeriod|
|v_input_8|-10|BuyAlertLevel|
|v_input_9|10|SellAlertLevel|
|v_input_10|1.5|RSIHistoModify|
|v_input_11|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-28 00:00:00
end: 2024-01-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 28/06/2021
// This is a combination strategy for generating cumulative signals.
//
// First Strategy
// This system was created from the book "How I Tripled My Money In The Futures Market" by Ulf Jensen, Page 183. This is a reverse type of strategies.
// The strategy buys at market if the close price on the current day is higher than the previous close during two days and the
```