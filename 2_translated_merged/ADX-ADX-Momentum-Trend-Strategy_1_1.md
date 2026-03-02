``` pinescript
/*backtest
start: 2024-01-08 00:00:00
end: 2024-01-15 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © millerrh with inspiration from @9e52f12edd034d28bdd5544e7ff92e 
// The intent behind this study is to look at ADX when it has an increasing slope and is above a user-defined key level (23 default). 
// This is to identify when it is trending.
// It then looks at the DMI levels.  If D+ is above D- and the ADX is sloping upwards and above the key level, it triggers a buy condition.  Opposite for short.
// Can use a user-defined moving average to filter long/short if desired.
// NOTE: THIS IS MEANT TO BE USED IN CONJUNCTION WITH MY "ATX TRIGGER" INDICATOR FOR VISUALIZATION. MAKE SURE SETTINGS ARE THE SAME FOR BOTH.

strategy("ADX | DMI Trend", overlay=true, initial_capital=10000, currency='USD', 
   default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.04)

// === BACKTEST RANGE ===
From_Year  = input(defval = 2019, title = "From Year")
From_Month = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
From_Day   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
To_Year    = input(defval = 9999, title = "To Year")
To_Month   = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
To_Day     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
Start  = timestamp(From_Year, From_Month, From_Day, 00, 00)  // backtest start window
Finish = timestamp(To_Year, To_Month, To_Day, 23, 59)        // backtest finish window

// == INPUTS ==
// ADX Info
adxlen = input(14, title="ADX Smoothing")
dilen = input(14, title="DI Period")
keyLevel = input(23, title="Keylevel for ADX")
adxLookback = input(3, title="Lookback Period for Slope")

// == FILTERING ==
// Inputs
useMaFilter = input(title = "Use MA for Filtering?", type = input.bool, defval = true)
maType = input(defval="EMA", options=["EMA", "SMA"], title = "MA Type For Filtering")
maLength   = input(defval = 200, title = "MA Period for Filtering", minval = 1)

// Declare function to be able to swap out EMA/SMA
ma(maType, src, length) =>
    maType == "EMA" ? ema(src, length) : sma(src, length) //Ternary Operator (if maType equals EMA, then do ema calc, else do sma calc)
maFilter = ma(maType, close, maLength)
plot(maFilter, title = "Trend Filter MA", color = color.green, linewidth = 3, style = plot.style_line, transp = 50)

// Check to see if ADX is above keyLevel and has a positive slope
adxSlopeUp = ta.slope(adxlen, adxLookback) > 0
adxAboveKey = ta.adx(adxlen, dilen) > keyLevel

// Determine buy/sell conditions based on DMI and ADX criteria
if (adxAboveKey and adxSlopeUp and not na(ta.dmi(dilen).di_plus) and ta.dmi(dilen).di_plus > ta.dmi(dilen).di_minus)
    strategy.entry("Buy", strategy.long)

if (adxAboveKey and adxSlopeUp and not na(ta.dmi(dilen).di_minus) and ta.dmi(dilen).di_minus < ta.dmi(dilen).di_plus)
    strategy.entry("Sell", strategy.short)

// Close positions when ADX slope is negative or close is below MA
if (adxSlopeUp == false or (useMaFilter and close <= maFilter))
    if (strategy.position_size > 0)
        strategy.close("Buy")
    else if (strategy.position_size < 0)
        strategy.close("Sell")

// Plot ADX line for visualization
plot(ta.adx(adxlen, dilen), title="ADX Line", color=color.orange, linewidth=2)

```

This script completes the translation and maintains the original code structure and comments.