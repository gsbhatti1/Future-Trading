```pinescript
```pinescript
/// Getting inputs
dyear = input(title="Year", type=input.integer, defval=2017, minval=1950, maxval=2500)
fast_length = input(title="Fast Length", type=input.integer, defval=12)
slow_length = input(title="Slow Length", type=input.integer, defval=26)
trend_number = input(title="Trend of Histogram Number", type=input.integer, defval=4)
source = input(title="Source", type=input.source, defval close)
signal_smoothing = input(title="Signal Smoothing", type=input.integer, defval=9)
simple_ma_oscillator = input(title="Simple MA (Oscillator)", type=input.bool, defval=false)
simple_ma_signal_line = input(title="Simple MA (Signal Line)", type=input.bool, defval=false)

/// Calculating MACD and Signal
[macdline, signal_line, _] = macd(source, fast_length, slow_length, signal_smoothing)
histogram = macdline - signal_line

/// Defining Buy/Sell Conditions
long_conditions = crossover(histogram, trend_number)
short_conditions = crossunder(histogram, trend_number)

/// Plotting MACD and Signal Lines
plot(macdline, color=color.blue, title="MACD Line")
plot(signal_line, color=color.red, title="Signal Line")

/// Executing Trades
if (long_conditions)
    strategy.entry("Long", strategy.long)
if (short_conditions)
    strategy.close("Long")

```
```