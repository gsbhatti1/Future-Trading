> Name

Rainbow-Oscillator

> Author

ChaoZhang

> Strategy Description

---------------
FEATURES
---------------

.:: Dynamic Levels ::.
The indicator consists of levels (price reversal zones) that correlate with each other with Fibonacci numbers. Each level causes the probability of a price reversal.
All levels are formed from existing non-smoothed oscillator values. This allows you not to fix turn zone thresholds, for example, -100 and 100, as done in CCI
or the values 30 and 70 for the reversal zone in the RSI indicator. Dynamic levels adjust to the spikes in oscillator values and allow you to find price reversal points more often and no less efficiently.

.:: Composite Oscillator (3 in 1) ::.
The oscillator line consists of three measurements of the RSI, CCI, Stoch indicators at once in a wide percentage range. At the same time, thanks to the settings, you can easily get rid of one of the indicators.

.:: CCI + RSI + Stoch Ratio Setting ::.
Each of the natural indicators has its own weight in the calculation formula: `w2 * cci ( + w1 * ( rsi - 50) + (1 - w2 - w1) * ( stoch - 50))`, this allows you to see an oscillator value for any of these various indicators or a sharpness weight for each.

.:: Smoothing Levels and Lines of the Oscillator ::.
Smoothing the oscillator values allows you to filter out noise and get more accurate data. Smoothing the levels allows you to adjust the delay of the inputs.

.:: Activity During APARTMENT ::.
Dynamic creation of levels allows you to find price reversal zones, even when the price is in a flat (horizontal).

----------------
SETTINGS
----------------

.:: RSI Weight / CCI Weight ::.
Control coefficients for the weight of the RSI and CCI indicators, respectively. When setting `RSI Weight = 0`, balance the combination of CCI and Stoch. When `RSI Weight` is zero and `CCI Weight` equals the oscillator value, only the `Stoch` will be plotted.
Intermediate values have a high degree of measurement for each of the three oscillators in percentage terms from 0 to 100. The calculation uses the formula: `w2 * cci + w1 * (rsi - 50) + (1 - w2 - w1) * (stoch - 50)`, where `w1` is RSI Weight and `w2` is CCI Weight, Stoch weight is calculated on the fly as `(1 - w2 - w1)`, so the sum of `w1 + w2` should not exceed 1; in this case, Stoch will work as opposed to CCI and RSI.

.:: Oscillator Period ::.
This is the period for all oscillators, set by one parameter for all. Perhaps, in future versions, the periods will be configured separately.

.:: Oscillator MA Period ::.
Periodic smoothing of the oscillator line. Serves for finer tuning to eliminate noise. If you select a value of 0, smoothing is disabled and the `Oscillograph Samples` setting will automatically stop working.

.:: Waveform Samples ::.
Setting allows you to set the amount of smoothing for the oscillator line. Oscillograph MA type

.:: Oscillator MA Type ::.
Moving average frequency type for the oscillator line sliding

.:: Level Period ::.
Periodic moving averages used to form the levels (zone) of the Rainbow Oscillator indicator

.:: Level Offset ::.
Additional setting for shifting levels from zero points. Can be useful for absorbing levels and filtering input signals. The default is 0.

.:: Redundant Level ::.
It characterizes the severity of the state at each iteration of the level. If set to 1, the levels will not decrease when the oscillator values fall. If it has a value of 0.99, the levels are reduced by 0.01 each time there is an oscillator drop in 1% of cases and are pressed to 0 by more aggressive ones.

.:: Samples of Smoothed Levels ::.
Setting allows you to set the number of strokes per level. Measuring the number of averages with the definition of the type of moving averages

.:: Type of MA Level ::.
Type of moving average for forming a smoothing overbought and oversold zone


**Backtest**

![IMG](https://www.fmz.com/upload/asset/e04e6f9a46dda5a36a.png)


> Strategy Arguments



|Argument|Default|Description|
|--------|-------|-----------|
|v_input_float_1|0.33|RSI Weight|
|v_input_float_2|0.33|CCI Weight|
|v_input_int_1|24|Oscillator Period|
|v_input_int_2|4|Oscillator MA Period|
|v_input_int_3|true|Oscillograph Samples|
|v_input_string_1|0|Oscillograph MA type: SMA, EMA, RMA, WMA|
|v_input_int_4|18|Level Period|
|v_input_int_5|false|Level Offset|
|v_input_float_3|0.99|Level Redundant|
|v_input_int_6|3|Level Smooth Samples|
|v_input_string_2|0|Level MA type: RMA, SMA, EMA, WMA|
|v_input_float_4|7.5|% Take Profit|
|v_input_float_5|3.5|% Stop Loss|


> Source (PineScript)

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
int period = input.int(24, 'Oscillator Period', 4, 60, 1)
int oscillographSamplesPeriod = input.int(4, 'Oscillator MA Period', 1, 30, 1)
int oscillographSamplesCount = input.int(1, 'Oscillograph Samples', 0, 4, 1)
string oscillographMAType = input.string("SMA", "Oscillator MA type", options = ["EMA", "SMA", "RMA", "WMA"])
int levelPeriod = input.int(18, 'Level Period', 2, 30)
int levelOffset = input.int(0, 'Level Offset', 0, 200, 10)
float redunant = input.float(0.99, 'Level Redundant', 0, 1, 0.01)
int levelSampleCount = input.int(3, 'Level Smooth Samples', 0, 4, 1)
string levelType = input.string("RMA", "Level MA type", options = ["EMA", "SMA", "RMA", "WMA"])

perc(current, prev) => ((current - prev) / prev) * 100

smooth(value, type, period) =>
    float ma = switch type
        "EMA" => ta.ema(value, period)
        "SMA" => ta.sma(value, period)
        "RMA" => ta.rma(value, period)
        "WMA" => ta.wma(value, period)
        =>
            run
```