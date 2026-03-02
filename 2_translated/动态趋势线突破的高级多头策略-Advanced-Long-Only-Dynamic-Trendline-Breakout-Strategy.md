```pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-09 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Long Only Strategy with Dynamic Trend Lines, Fixed TP/SL, and Trailing SL+", overlay=true, 
         default_qty_type=strategy.percent_of_equity, default_qty_value=10, 
         pyramiding=0, // Prevent multiple entries
         calc_on_order_fills=true, 
         calc_on_every_tick=true)

// === Parameters ===
swingThreshold = input.int(5, title="Swing Detection Threshold")
tpPercent = input.float(2.0, title="Take Profit (%)")
slPercent = input.float(1.0, title="Stop Loss (%)")
trailPercent = input.float(1.0, title="Trailing Stop (%)")
volumeThresholdMultiplier = input.float(1.5, title="Volume Spike Threshold (x MA)")

// === Volume Indicator ===
avgVolume = ta.sma(volume, 20)
volumeSpike = volume > (avgVolume * volumeThresholdMultiplier)

// === Detect Swing High ===
isSwingHigh = ta.pivothigh(high, swingThreshold, swingThreshold)

// Variables to store swing highs
var float swingHigh1 = na
var float swingHigh2 = na
var int swingHighBar1 = na
var int swingHighBar2 = na

// Update swing highs
if (isSwingHigh)
    swingHigh2 := swingHigh1
    swingHighBar2 := swingHighBar1
    swingHigh1 := high[swingThreshold]
    swingHighBar1 := bar_index - swingThreshold

// === Calculate Upper Trend Line ===
var float upperSlope = na
var float upperIntercept = na

// Calculate slope and intercept for upper trend line if there are two swing highs
if (not na(swingHigh1) and not na(swi
```