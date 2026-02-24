> Source (PineScript)

``` pinescript
/*backtest
start: 2024-05-30 00:00:00
end: 2024-06-06 00:00:00
period: 1D
initialCapital: 10000
*/

//@version=5
indicator("VWAP Trading Strategy with Volume Anomaly Detection", shorttitle="VWAP-TS", overlay=true)

// Parameters
vwapLevels = input(array=[open, high, low], title="VWAP Levels")
highVolumeCandleReset = input.bool(true, title="Reset High Volume VWAP on Next Candle")
displacement = input.int(10, minval=1, title="Displacement Value")

// Helper function to calculate VWAP
calculateVWAP(candlePrices) =>
    var float vwap = na
    var int count = 0
    for i = 0 to bar_index - 1
        volume = security(syminfo.tickerid, "D", high * low / (high + low))
        vwap := ((vwap * count + candlePrices[i] * volume) / (count + volume))
        count := count + volume
    vwap

// Calculate VWAP levels
openVWAP = calculateVWAP(open)
highVWAP = calculateVWAP(high)
lowVWAP = calculateVWAP(low)

// Detect high volume candles and reset VWAP accordingly
var float prevHighVolumeVWAP = na
if (volume > input.float(100, title="High Volume Threshold"))
    if (prevHighVolumeVWAP != na)
        prevHighVolumeVWAP := openVWAP
    else
        highVolumeCandleReset ? openVWAP := 0 : na

// Generate trading signals
longSignal = crossover(open + displacement, openVWAP) and close > open
shortSignal = crossunder(open - displacement, openVWAP) and close < open

plot(openVWAP, title="Open VWAP", color=color.blue)
plot(highVWAP, title="High VWAP", color=color.red)
plot(lowVWAP, title="Low VWAP", color=color.green)

// Plot signals
plotshape(series=longSignal, location=location.belowbar, color=color.green, style=shape.labelup, text="Long")
plotshape(series=shortSignal, location=location.abovebar, color=color.red, style=shape.labeldown, text="Short")

// RSI for exit condition
rsiLength = input.int(14, title="RSI Length")
rsiOverbought = 70
rsiOversold = 30

rsiValue = rsi(close, rsiLength)

plot(rsiValue, title="RSI", color=color.orange)
alertcondition(rsiValue > rsiOverbought, "Exit Long Position", "RSI over 70")
alertcondition(rsiValue < rsiOversold, "Exit Short Position", "RSI under 30")

```