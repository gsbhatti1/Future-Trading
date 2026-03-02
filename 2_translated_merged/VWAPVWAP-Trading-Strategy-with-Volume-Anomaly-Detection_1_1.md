> Source (PineScript)

``` pinescript
/*backtest
start: 2024-05-30 00:00:00
end: 2024-06-06 00:00:00
period: 1D
*/

//@version=5
indicator("VWAP Trading Strategy with Volume Anomaly Detection", shorttitle="VWAP Strat", overlay=true)

// Parameters
vwapOpenLevel = input.float(0.0, title="Opening Price VWAP Level")
vwapHighLevel = input.float(0.0, title="High Price VWAP Level")
vwapLowLevel = input.float(0.0, title="Low Price VWAP Level")
highVolumeCandleVWAP = input.float(0.0, title="VWAP of Candles with Abnormally High Volume")
displacement = input.int(10, title="Displacement Value")

// RSI Settings
rsiLength = input.int(14, title="RSI Length", minval=1)
overboughtLevel = input.int(70, title="Overbought Level", minval=30)
oversoldLevel = input.int(30, title="Oversold Level", maxval=70)

// VWAP Calculations
openVWAP = ta.vwap(open)
highVWAP = ta.vwap(high)
lowVWAP = ta.vwap(low)
abnormalVolumeCandleVWAP = na

for i = 1 to barssince(ta.vwap(volume) > ta.vwap(volume[1]) * 2 ? true : false)
    abnormalVolumeCandleVWAP := ta.vwap(close[i])

// Check for gaps
gapAboveVWAP = close < open and high > vwapHighLevel + displacement
gapBelowVWAP = close > open and low < vwapLowLevel - displacement

// Crossover signals
wickSignal = low < vwapLowLevel and high > vwapHighLevel
crossoverSignal = ta.crossover(close, vwapHighLevel) or ta.crossunder(close, vwapLowLevel)

// RSI Calculation
rsiValue = ta.rsi(close, rsiLength)
exitLong = rsiValue > overboughtLevel
exitShort = rsiValue < oversoldLevel

// Plot signals
plotshape(series=gapAboveVWAP, title="Gap Above VWAP", location=location.abovebar, color=color.red, style=shape.labelup, text="Gap")
plotshape(series=gapBelowVWAP, title="Gap Below VWAP", location=location.belowbar, color=color.green, style=shape.labeldown, text="Gap")
plotshape(series=crossoverSignal, title="Crossover Signal", location=location.middle, color=color.blue, style=shape.triangledown)
plotshape(series=wickSignal, title="Wick Signal", location=location.middle, color=color.orange, style=shape.triangleup)

// Exit conditions
exitLongTrade = exitLong and ta.close >= vwapHighLevel
exitShortTrade = exitShort and ta.close <= vwapLowLevel

// Plot VWAP levels
plot(openVWAP, title="Opening Price VWAP", color=color.blue)
plot(highVWAP, title="High Price VWAP", color=color.green)
plot(lowVWAP, title="Low Price VWAP", color=color.red)
plot(abnormalVolumeCandleVWAP, title="Abnormally High Volume VWAP", color=color.orange)

```
```