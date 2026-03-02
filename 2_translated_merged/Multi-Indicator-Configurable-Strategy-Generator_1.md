> Name

Multi-Indicator-Configurable-Strategy-Generator

> Author

ChaoZhang

> Strategy Description


``` pinescript
/*backtest
start: 2023-08-11 00:00:00
end: 2023-08-25 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// By Jordan Hall
// finished: 3/28/2023
strategy("Strategy Creator", overlay=true, margin_long=100, margin_short=100, pyramiding=10, default_qty_type=strategy.percent_of_equity)

///////////////////////////////////////////////////////////////////////////////////////////////////////
/// PERIOD /// 
testStartYear = input(2023, "Backtest Start Year") 
testStartMonth = input(1, "Backtest Start Month") 
testStartDay = input(1, "Backtest Start Day") 
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0) 
 
testStopYear = input(2023, "Backtest Stop Year") 
testStopMonth = input(12, "Backtest Stop Month") 
testStopDay = input(31, "Backtest Stop Day") 
testPeriodStop = timestamp(testStopYear,testStartMonth,testStopDay,0,0) 
 
testPeriod() => 
    time >= testPeriodStart and time <= testPeriodStop ? true : false
///////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////EMA INPUTS//////////////////////////////////////////////////
EMAON = input.bool(true, "EMA ON?", group = "EMA Settings", tooltip = "Check box for on")
IS1EMA = input.bool(false,"Only 1 EMA", " USE EMA FAST LENGTH FOR INPUT", group = "EMA Settings")
IS2EMA = input.bool(false, "Only 2 EMAs", "Only leave this box checked for 2 EMAs. USE EMA MIDDLE LENGTH AND FAST LENGTH", group = "EMA Settings")
EMAFAST = input.int(50,title = "EMA Fast Length", minval = 1, maxval = 2000, group = "EMA Settings")
EMAMIDDLE = input.int(100, title= "EMA middle Length", minval = 1, maxval = 2000, group = "EMA Settings")
EMASLOW = input.int(200, title= "EMA Slow Length", minval = 1, maxval = 2000, group = "EMA Settings")
///////////////////////////////////////////////////////////////////////////////////////////////////////
```


> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|2023|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2023|Backtest Stop Year|
|v_input_5|12|Backtest Stop Month|
|v_input_6|31|Backtest Stop Day|
|v_input_bool_1|true|(?EMA Settings)EMA ON?|
|v_input_bool_2|false|Only 1 EMA|
|v_input_bool_3|false|Only 2 EMAs|
|v_input_int_1|50|EMA Fast Length|
|v_input_int_2|100|EMA middle Length|
|v_input_int_3|200|EMA Slow Length|
|v_input_bool_4|true|(?RSI Settings)RSI ON?|
|v_input_float_1|52|RSI SHORT|
|v_input_float_2|48|RSI LONG|
|v_input_int_4|14|RSI Length|
|v_input_source_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_string_1|0|MA Type: SMA|Bollinger Bands|EMA|SMMA (RMA)|WMA|VWMA|
|v_input_int_5|14|MA Length|
|v_input_bool_5|true|(?Stochastic Settings)STOCHASTIC ON?|
|v_input_int_6|14|%K Length|
|v_input_int_7|true|%K Smoothing|
|v_input_int_8|3|%D Smoothing|
|v_input_bool_6|true|By Crossover?|
|v_input_float_3|50|k is greater than|
|v_input_float_4|50|k is less than|
|v_input_bool_7|true|(?MACD Settings)MACD ON?|
|v_input_timeframe_1|1|Time Frame MACD|
|v_input_7|12|Fast Length|
|v_input_8|26|Slow Length|
|v_input_9_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_9|9|Signal Smoothing|
|v_input_string_2|0|Oscillator MA Type: EMA|SMA|
|v_input_string_3|0|Signal Line MA Type: EMA|SMA|
|v_input_10|false|Add average positve histogram value?|
|v_input_11|false|Subtract average negative histogram value?|
|v_input_float_5|false| + (absolute val)|
|v_input_float_6|false| - (absolute val)|
|v_input_bool_8|true|(?ADX Settings)ADX ON?|
|v_input_12|14|ADX Smoothing|
|v_input_13|14|DI Length|
|v_input_float_7|25|ADX signal strength > |
|v_input_float_8|0.4|(?Take Profit and Stop Loss)Long Stop Loss (%)|
|v_input_float_9|0.4|Short Stop Loss (%)|
|v_input_float_10|0.5|Long Take Profit (%)|
|v_input_float_11|0.5|Short Take Profit (%)|
|v_input_int_10|0|(?Strategy Settings)How Many Trades Allowed In One Direction?: 3|2|1|4|5|6|7|8|9|10|
```