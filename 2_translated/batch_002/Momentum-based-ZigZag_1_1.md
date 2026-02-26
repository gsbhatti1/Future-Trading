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

if (momentum_select == 'MACD')
    if macdUP then
        momentum_direction := 1
    else if macdDOWN then
        momentum_direction := -1
else if (momentum_select == 'MovingAverage')
    src = input.source(title='Source', defval=close, group='if Moving Average selected', inline='movingaverage')
    ma = moving_average(src, ma_length, smoothing_type)
    if ma > nz(ma[1]) then
        momentum_direction := 1
    else if ma < nz(ma[1]) then
        momentum_direction := -1
else
    _qqefactor_factor = input.float(4.238, title='_qqefactor Factor', group='if QQE selected')
    rsi_length = input.int(14, title='RSI Length', minval=1, maxval=50, group='if QQE selected')
    rsi_smoothing = input.int(5, title='RSI Smoothing', minval=1, maxval=50, group='if QQE selected')
    
    rsi = ta.rsi(src, rsi_length)
    sma_rsi = ta.sma(rsi, rsi_smoothing)
    if sma_rsi > nz(sma_rsi[1]) then
        momentum_direction := 1
    else if sma_rsi < nz(sma_rsi[1]) then
        momentum_direction := -1

// Print ZigZag based on momentum direction
plotshape(series=zigzag(momentum_direction), title='ZigZag', location=location.abovebar, color=color_zigzag_lines ? na : color.new(color.blue, 0), style=shape.triangleup, size=size.small)
```

This Pine Script implements the described strategy, including the ZigZag function and conditional logic for selecting a momentum indicator. The code is kept intact as requested.