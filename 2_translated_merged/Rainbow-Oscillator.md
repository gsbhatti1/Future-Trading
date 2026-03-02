```pinescript
/*backtest
start: 2022-04-12 00:00:00
end: 2022-05-06 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © businessduck

//@version=5
indicator("Rainbow Oscillator")

float w1 = input.float(0.33, 'RSI Weight', 0, 1, 0.01)
float w2 = input.float(0.33, 'CCI Weight', 0, 1, 0.01)
int period = input.int(24, 'Ocillograph Period', 4, 60, 1)
int oscillographSamplesPeriod = input.int(4, 'Oscillograph MA Period', 1, 30, 1)
int oscillographSamplesCount = input.int(1, 'Oscillograph Samples', 0, 4, 1)
string oscillographMAType = input.string("SMA", "Oscillograph MA type", options = ["EMA", "SMA", "RMA", "WMA"])
int levelPeriod = input.int(18, 'Level Period', 2, 30)
int levelOffset = input.int(0, 'Level Offset', 0, 200, 10)
float redunant = input.float(0.99, 'Level Redunant', 0, 1, 0.01)
int levelSampleCount = input.int(3, 'Level Smooth Samples', 0, 4, 1)
string levelType = input.string("RMA", "Level MA type", options = ["EMA", "SMA", "RMA", "WMA"])

perc(current, prev) => ((current - prev) / prev) * 100

smooth(value, type, period) =>
    float ma = switch type
        "EMA" => ta.ema(value, period)
        "SMA" => ta.sma(value, period)
        "RMA" => ta.rma(value, period)
        "WMA" => ta.wma(value, period)
    ma
```

> Strategy Arguments

|Argument|Default|Description|
|--------|-------|-----------|
|v_input_float_1|0.33|RSI Weight|
|v_input_float_2|0.33|CCI Weight|
|v_input_int_1|24|Ocillograph Period|
|v_input_int_2|4|Oscillograph MA Period|
|v_input_int_3|true|Oscillograph Samples|
|v_input_string_1|0|Oscillograph MA type: SMA|EMA|RMA|WMA|
|v_input_int_4|18|Level Period|
|v_input_int_5|false|Level Offset|
|v_input_float_3|0.99|Level Redunant|
|v_input_int_6|3|Level Smooth Samples|
|v_input_string_2|0|Level MA type: RMA|SMA|EMA|WMA|
|v_input_float_4|7.5|% Take profit|
|v_input_float_5|3.5|% Stop Loss|

> Source (PineScript)

```pinescript
//@version=5
indicator("Rainbow Oscillator")

float w1 = input.float(0.33, 'RSI Weight', 0, 1, 0.01)
float w2 = input.float(0.33, 'CCI Weight', 0, 1, 0.01)
int period = input.int(24, 'Ocillograph Period', 4, 60, 1)
int oscillographSamplesPeriod = input.int(4, 'Oscillograph MA Period', 1, 30, 1)
int oscillographSamplesCount = input.int(1, 'Oscillograph Samples', 0, 4, 1)
string oscillographMAType = input.string("SMA", "Oscillograph MA type", options = ["EMA", "SMA", "RMA", "WMA"])
int levelPeriod = input.int(18, 'Level Period', 2, 30)
int levelOffset = input.int(0, 'Level Offset', 0, 200, 10)
float redunant = input.float(0.99, 'Level Redunant', 0, 1, 0.01)
int levelSampleCount = input.int(3, 'Level Smooth Samples', 0, 4, 1)
string levelType = input.string("RMA", "Level MA type", options = ["EMA", "SMA", "RMA", "WMA"])

perc(current, prev) => ((current - prev) / prev) * 100

smooth(value, type, period) =>
    float ma = switch type
        "EMA" => ta.ema(value, period)
        "SMA" => ta.sma(value, period)
        "RMA" => ta.rma(value, period)
        "WMA" => ta.wma(value, period)
    ma

// Additional logic for the strategy can be added here
```