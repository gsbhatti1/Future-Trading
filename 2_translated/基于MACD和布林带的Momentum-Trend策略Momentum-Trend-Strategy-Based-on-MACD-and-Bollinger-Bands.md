> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|8|Fast MA period|
|v_input_2|21|Slow MA period|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|true|Moving Average Calculation: (1 = SMA), (2 = EMA), (3 = WMA), (4 = Linear)|
|v_input_5|40|length|
|v_input_6|2|BB multiplier|


> Source (PineScript)

```pinescript
//@version=4
// Simple strategy based on MACD and Bollinger Bands

strategy("Momentum Trend", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=50)

// Input parameters
fast_ma_period = input(8, title="Fast MA period")
slow_ma_period = input(21, title="Slow MA period")
source = input(close, title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4")
calculation_method = input(True, title="Moving Average Calculation: (1 = SMA), (2 = EMA), (3 = WMA), (4 = Linear)")
length = input(40, title="Length")
bb_multiplier = input(2.0, title="BB multiplier")

// Calculate MACD
[macd_line, signal_line, _] = macd(source, fast_ma_period, slow_ma_period, 9)

// Bollinger Bands
src = close
basis = sma(src, length)
dev = bb_multiplier * ta.stdev(src, length)
upper_band = basis + dev
lower_band = basis - dev

// Plotting
plot(macd_line, color=color.blue, title="MACD Line")
plot(signal_line, color=color.orange, title="Signal Line")
fill(macd_line, signal_line, color=color.rgb(255, 0, 0, 100), title="MACD Histogram")

// Entry conditions
long_condition = ta.crossover(macd_line, signal_line) and close > lower_band
short_condition = ta.crossunder(macd_line, signal_line) and close < upper_band

if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

// Plot Bollinger Bands
plot(basis, color=color.blue, title="Bollinger Bands")
hline(upper_band, "Upper Band", color=color.red)
hline(lower_band, "Lower Band", color=color.green)

```

This PineScript code defines a simple momentum-trend strategy using MACD and Bollinger Bands. The strategy uses the default settings provided in the arguments to calculate the MACD and Bollinger Bands, and then enters long or short positions based on the crossover of the MACD line with the signal line relative to the Bollinger Bands.