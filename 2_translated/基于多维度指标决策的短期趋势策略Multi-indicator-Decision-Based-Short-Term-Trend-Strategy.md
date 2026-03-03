> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|(?Pivot Points)Plot Close Price Crossing Pivot Points?|
|v_input_2|false|Plot Pivot Points?|
|v_input_3|0|Pivot Points type: Fibonacci|Traditional|
|v_input_4|2|Width of Pivot Point circles|
|v_input_5|true|(?VWAP)Plot VWAP?|
|v_input_6|true|Plot Average Price?|
|v_input_7|false|Plot Price Crossing VWAP?|
|v_input_8|D|Period|
|v_input_9|14|VWAP Cumulative Period|
|v_input_10|false|(?StochRSI)Plot StochRSI Cross?|
|v_input_11|3|K|
|v_input_12|3|D|
|v_input_13|14|(?Stochastic-RSI)RSI Length|
|v_input_14|14|Stochastic Length|
|v_input_15_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_16|true|(?Strategy only)Plot Long Opportunity?|
|v_input_17|true|Plot Short Opportunity?|
|v_input_18|0|Strategy trading Direction: : L&S|L|S|
|v_input_19|true|Take Profit %|
|v_input_20|true|Plot Take Profit?|
|v_input_21|true|(?Backtesting range)Start Date|
|v_input_22|true|Start Month|
|v_input_23|2017|Start Year|
|v_input_24|31|End Date|
|v_input_25|12|End Month|
|v_input_26|2050|End Year|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-24 00:00:00
end: 2023-10-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Multi-indicator-Decision-Based-Short-Term-Trend-Strategy
//              v2.1
// 
//      coded by ChaoZhang

// This strategy was created after 
```