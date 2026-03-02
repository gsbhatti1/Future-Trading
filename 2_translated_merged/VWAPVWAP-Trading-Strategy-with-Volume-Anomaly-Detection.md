> Source (PineScript)

``` pinescript
/*backtest
start: 2024-05-30 00:00:00
end: 2024-06-06 00:00:00
period: 1D
*/

//@version=5
indicator("VWAP Trading Strategy with Volume Anomaly Detection", overlay=true)

// Variables for VWAP Levels
open_vwap = ta.vwma(close, ta.barssince(open) + 1)
high_vwap = ta.vwma(high, ta.barssince(high) + 1)
low_vwap = ta.vwma(low, ta.barssince(low) + 1)

// Threshold for Abnormally High Volume
high_volume_threshold = 1000 // Example threshold value

// Detecting Candles with Abnormally High Volume and Resetting VWAP Variables
high_volume_candles = na
for i = 0 to (bar_index - 1)
    if volume[i] > high_volume_threshold
        high_volume_candles := i

if not na(high_volume_candles)
    abnormal_high_vwap = ta.vwma(close, bar_index - high_volume_candles + 1)

// Setting Displacement Values for VWAP Levels
vwap_displacement = 0.5 * (high_vwap - low_vwap)

// Gaps on the Opposite Side of VWAP
gap_above_vwap = na
gap_below_vwap = na

if close > open and high < vwap + vwap_displacement and low > vwap - vwap_displacement
    gap_below_vwap := true
else if close < open and low > vwap + vwap_displacement and high < vwap - vwap_displacement
    gap_above_vwap := true

// Trading Signals Based on VWAP Position and Close/Open Price Relationship
wicks = array.new_float(0)
crossovers = array.new_float(0)

if close > open
    if close > vwap + vwap_displacement
        array.push(wicks, high - low) // Long Wick Signal
else
    if close < vwap - vwap_displacement
        array.push(wicks, high - low) // Short Wick Signal

// Crossover Signals
if close > open and high_vwap < low and low_vwap > high
    array.push(crossovers, 1)
else if close < open and low_vwap < high and high_vwap > low
    array.push(crossovers, -1)

// RSI for Exit Condition
rsi_length = input.int(14, minval=1)
rsi_threshold = input.float(70, minval=30, maxval=100)
exit_signal = ta.rsi(close, rsi_length) > rsi_threshold or ta.rsi(close, rsi_length) < (100 - rsi_threshold)

// Plotting VWAP Levels and Signals
plot(open_vwap, title="Open VWAP", color=color.blue)
plot(high_vwap, title="High VWAP", color=color.red)
plot(low_vwap, title="Low VWAP", color=color.green)
plot(abnormal_high_vwap, title="Abnormal High Volume VWAP", color=color.orange)

plotshape(series=gap_above_vwap, location=location.abovebar, color=color.blue, style=shape.triangledown, size=size.small)
plotshape(series=gap_below_vwap, location=location.belowbar, color=color.red, style=shape.triangleup, size=size.small)

```
```