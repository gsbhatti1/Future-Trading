``` pinescript
```pinescript
/// Getting inputs
dyear = input(title="Year", type=input.integer, defval=2017, minval=1950, maxval=2500)
fast_length = input(title="Fast Length", type=input.integer, defval=12)
slow_length = input(title="Slow Length", type=input.integer, defval=26)
hist_trend_num = input(title="Trend of Histogram Number", type=input.int, defval=1, minval=1)
source = input(title="Source:", type=input.source, defval=close)
signal_smooth = input(title="Signal Smoothing", type=input.integer, defval=9)
simple_oscillator_ma = input(title="Simple MA(Oscillator)", type=input.bool, defval=false)
simple_signal_ma = input(title="Simple MA(Signal Line)", type=input.bool, defval=false)

/// Calculating MACD
fast_ema = ema(close, fast_length)
slow_ema = ema(close, slow_length)
macd_line = fast_ema - slow_ema
signal_line = sma(macd_line, signal_smooth)
histogram = macd_line - signal_line

/// Strategy Logic
long_condition = crossover(histogram, 0) and hist_trend_num >= 2
short_condition = crossunder(histogram, 0) and hist_trend_num >= 2

/// Entering the market
if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

/// Exit conditions
exit_long_condition = in_range(macd_line, signal_line - 10 * point_size, signal_line + 10 * point_size) and hist_trend_num < 2
exit_short_condition = in_range(macd_line, signal_line - 10 * point_size, signal_line + 10 * point_size) and hist_trend_num < 2

if (exit_long_condition)
    strategy.close("Long")

if (exit_short_condition)
    strategy.close("Short")
```
```