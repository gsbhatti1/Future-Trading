> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|false|Close early if price crosses outer VWAP band|
|v_input_string_1|0|(?VWAP Settings)Anchor Period: Session|Week|Month|Quarter|Year|
|v_input_1_close|0|Inner VWAP Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|true|Inner Bands Multiplier|
|v_input_3|2|Outer Bands Multiplier|
|v_input_int_1|14|(?ADX Settings)ADX Smoothing|
|v_input_int_2|14|DI Length|
|v_input_int_3|40|ADX Threshold|
|v_input_float_1|2|(?Entry Settings)Stop Loss (%)|
|v_input_float_2|6|Take Profit (%)|
|v_input_int_4|true|Long Entry Limit Lookback|
|v_input_int_5|true|Short Entry Limit Lookback|
|v_input_float_3|3|Start Trailing After (%)|
|v_input_float_4|2|Trail Behind (%)|
|v_input_bool_2|true|(?Limit Entries)Use EMA Filter|
|v_input_timeframe_1||    Timeframe|
|v_input_int_6|300|    Length|
|v_input_source_1_hl2|0|    Source: hl2|high|low|open|close|hlc3|hlcc4|ohlc4|
|v_input_bool_3|false|Use Time Session Filter|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-23 00:00:00
end: 2023-11-22 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © jordanfray

//@version=5
strategy(title="Double VWAP Strategy", overlay=true, scale=scale.none, max_bars_back=500, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=100000, commission_type=strategy.commission.percent, commission_value=0.05, backtest_fill_limits_assumption=2)

// Indenting Cl
```