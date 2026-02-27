``` pinescript
/*backtest
start: 2022-05-09 00:00:00
end: 2022-05-15 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Peter_O

//@version=5
indicator('Momentum-based ZigZag', overlay=true)

var int momentum_direction = 0
color_zigzag_lines = input(true, title='Color ZigZag lines to show force direction')
momentum_select = input.string(title='Select Momentum Indicator:', defval='QQE', options=['MACD', 'MovingAverage', 'QQE'])


// ZigZag function {
zigzag(_momentum_direction) =>
    zz_goingup = _momentum_direction == 1
    zz_goingdown = _momentum_direction == -1
    var float zz_peak = na
    var float zz_bottom = na
    zz_peak := high > zz_peak[1] and zz_goingup or zz_goingdown[1] and zz_goingup ? high : nz(zz_peak[1])
    zz_bottom := low < zz_bottom[1] and zz_goingdown or zz_goingup[1] and zz_goingdown ? low : nz(zz_bottom[1])
    zigzag = zz_goingup and zz_goingdown[1] ? zz_bottom[1] : zz_goingup[1] and zz_goingdown ? zz_peak[1] : na
    zigzag
// } End of ZigZag function

// MACD  {
fast_length = input.int(title='Fast Length', defval=12, group='if MACD Selected', inline='macd')
slow_length = input.int(title='Slow Length', defval=26, group='if MACD Selected', inline='macd')
src = input.source(title='Source', defval=close, group='if MACD Selected', inline='macd')
signal_length = input.int(title='Signal Smoothing', minval=1, maxval=50, defval=9, group='if MACD Selected', inline='macd')
sma_source = input.string(title='Oscillator MA Type', defval='EMA', options=['SMA', 'EMA'], group='if MACD Selected', inline='macd')
sma_signal = input.string(title='Signal Line MA Type', defval='EMA', options=['SMA', 'EMA'], group='if MACD Selected', inline='macd')

fast_ma = sma_source == 'SMA' ? ta.sma(src, fast_length) : ta.ema(src, fast_length)
slow_ma = sma_source == 'SMA' ? ta.sma(src, slow_length) : ta.ema(src, slow_length)
macd = fast_ma - slow_ma
signal = sma_signal == 'SMA' ? ta.sma(macd, signal_length) : ta.ema(macd, signal_length)

macdUP = ta.crossover(macd, signal)
macdDOWN = ta.crossunder(macd, signal)
// } End of MACD

// Moving Averages {
smoothing_type = input.string(title='Average type', defval='SMA', options=['EMA', 'SMA', 'WMA', 'VWMA', 'HMA', 'RMA', 'DEMA'], inline='movingaverage', group='if Moving Average selected')
ma_length = input.int(20, title='Length', inline='movingaverage', group='if Moving Average selected')
moving_average(_series, _length, _smoothing) =>
    _smoothing == 'EMA' ? ta.ema(_series, _length) : _smoothing == 'SMA' ? ta.sma(_series, _length) : _smoothing == 'WMA' ? ta.wma(_series, _length) : _smoothing == 'VWMA' ? ta.vwma(_series, _length) : _smoothing == 'HMA' ? ta.hma(_series, _length) : _smoothing == 'RMA' ? ta.rma(_series, _length) : _smoothing == 'DEMA' ? ta.dema(_series, _length) : na
// } End of Moving Averages

if momentum_select == 'MACD'
    // MACD-related code as defined earlier
else if momentum_select == 'MovingAverage'
    ma = moving_average(src, ma_length, smoothing_type)
    maUP = src > ma and ta.crossover(src, ma)
    maDOWN = src < ma and ta.crossunder(src, ma)
// } End of Moving Averages

// QQE {
qqefactor_factor = input.float(title='_qqefactor Factor', defval=4.238, group='if _qqefactor selected')
qqefactor_length = input.int(title='RSI Length', minval=1, maxval=50, defval=14, group='if _qqefactor selected')
qqe_rsi = ta.rsi(src, qqefactor_length)
qqefactor = ta.qqe(qqe_rsi, factor=qqefactor_factor)
qqeUP = ta.crossover(qqefactor, 0)
qqeDOWN = ta.crossunder(qqefactor, 0)
// } End of QQE

up_zigzag = na
down_zigzag = na
if momentum_select == 'MACD'
    up_zigzag := macdUP ? high : na
    down_zigzag := macdDOWN ? low : na
else if momentum_select == 'MovingAverage'
    up_zigzag := maUP ? high : na
    down_zigzag := maDOWN ? low : na
else if momentum_select == '_qqefactor'
    up_zigzag := qqeUP ? high : na
    down_zigzag := qqeDOWN ? low : na

plotshape(series=up_zigzag, title='Up ZigZag', location=location.abovebar, color=color_zigzag_lines ? color.green : na, style=shape.triangleup, size=size.small)
plotshape(series=down_zigzag, title='Down ZigZag', location=location.belowbar, color=color_zigzag_lines ? color.red : na, style=shape.triangledown, size=size.small)

// TakeProfitLevel
take_profit = input.float(title='TakeProfitLevel', defval=200)
plot(take_profit, title='Take Profit Level', color=color.blue)

// Thresh-hold
threshold = input.int(title='Thresh-hold', defval=10)
```

> Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|`v_input_1`|`true`|Color ZigZag lines to show force direction|
|`v_input_string_1`|`0`|Select Momentum Indicator:: _qqefactor, MACD, MovingAverage|
|`v_input_2`|`200`|TakeProfitLevel|
|`v_input_int_1`|`12`|(?if MACD Selected)Fast Length|
|`v_input_int_2`|`26`|Slow Length|
|`v_input_source_1_close`|`0`|Source: close, high, low, open, hl2, hlc3, hlcc4, ohlc4|
|`v_input_int_3`|`9`|Signal Smoothing|
|`v_input_string_2`|`0`|Oscillator MA Type: EMA, SMA|
|`v_input_string_3`|`0`|Signal Line MA Type: EMA, SMA|
|`v_input_string_4`|`0`|(?if Moving Average selected)Average type: SMA, EMA, WMA, VWMA, HMA, RMA, DEMA|
|`v_input_int_4`|`20`|Length|
|`v_input_int_5`|`14`|(?if _qqefactor selected)RSI Length|
|`v_input_float_1`|`4.238`|_qqefactor Factor|
|`v_input_int_6`|`5`|RSI Smoothing|
|`v_input_int_7`|`10`|Thresh-hold|

> Strategy Description

I spent a lot of time searching for the best ZigZag indicator. The difficulty with all of them is that they are always betting on some pre-defined rules which identify or confirm pivot points. Usually, it is a time factor - a pivot point gets confirmed after a particular number of candles. This methodology works best when the market moves relatively slow but fails when price starts chopping up and down. On the other hand, if you set it too tight (for example, pivot confirmation after only 2 or even 1 candle), you will get hundreds of zigzag lines and they will tell you nothing.

My point of view is to follow the market. If a reversal has occurred, then it has occurred, and there is no need to wait for a pre-defined number of candles for confirmation. Such reversals are always visible on momentum indicators such as the most popular MACD. But a single-line moving average can be also good enough to notice reversals. Or my favourite one - QQE (Quantitative Qualitative Estimation), which I borrowed and improved from JustUncleL, who borrowed it from Glaz, who borrowed it from... I don't even know where QQE originates from. Thanks to all these guys for their input and code.

So whichever momentum indicator you choose - yes, there is a pick-your-poison-type selector as in infamous Moving Average indicators - once it reverses, the highest (or lowest) point from the impulse is caught and ZigZag gets printed.

One thing I need to emphasize. This indicator DOES NOT REPAINT. It might look like the lines are a bit delayed, especially when compared to all the other ZigZag indicators on TradingView, but they are actually TRUE. There is value in this - my indicator prints pivot points and Zigzag exactly on the moment they have been noticed, not earlier faking to be faster than they could be.

As a bonus, the indicator marks which impulse had strength in it. It is very nice to see a progressing impulse, but without force - a very likely that reversal on a bigger move is happening.

This strategy uses MACD, Moving Average (MA), and QQE as momentum indicators. The selected momentum indicator determines the points where ZigZag lines are plotted based on up and down movements in price. The `TakeProfitLevel` and `Thresh-hold` parameters can be adjusted according to your trading strategy.
```