``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-20 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Supply and Demand Zones with EMA and Trailing Stop", shorttitle="SD Zones", overlay=true)

showBuySignals = input(true, title="Show Buy Signals", group="Signals")
showSellSignals = input(true, title="Show Sell Signals", group="Signals")
showHLZone = input(true, title="Show HL Zone", group="Zones")
showLHZone = input(true, title="Show LH Zone", group="Zones")
showHHZone = input(true, title="Show HH Zone", group="Zones")
showLLZone = input(true, title="Show LL Zone", group="Zones")

emaLength = input(200, title="EMA Length", group="EMA Settings")
atrLength = input(14, title="ATR Length", group="Trailing Stop")
atrMultiplier = input(2, title="ATR Multiplier", group="Trailing Stop")

// Function to identify supply and demand zones
get_zone(highs, lows, period) =>
    hh = ta.highest(highs, period)
    ll = ta.lowest(lows, period)
    hh > prev(hh[1]) ? hh : na
    ll < prev(ll[1]) ? ll : na

// Calculate EMA
ema = ta.ema(close, emaLength)

// Calculate ATR
atr = ta.atr(atrLength)

// Determine entry and exit conditions
longCondition = ta.crossover(close, ema) and get_zone(highs, lows, 2)[1] < get_zone(highs, lows, 2)
shortCondition = ta.crossunder(close, ema) and get_zone(highs, lows, -2)[1] > get_zone(highs, lows, -2)

// Plot zones
if (showHHZone)
    plotshape(series=get_zone(highs, lows, 2), title="HH Zone", location=location.belowbar, color=color.red, style=shape.triangleup, size=size.small)
if (showLLZone)
    plotshape(series=get_zone(highs, lows, -2), title="LL Zone", location=location.abovebar, color=color.green, style=shape.triangledown, size=size.small)
if (showHLZone)
    plotshape(series=get_zone(highs, lows, 1)[0] > get_zone(highs, lows, -1)[0], title="HL Zone", location=location.belowbar, color=color.orange, style=shape.labelup, text="HL")
if (showLHZone)
    plotshape(series=get_zone(highs, lows, -1)[0] < get_zone(highs, lows, 1)[0], title="LH Zone", location=location.abovebar, color=color.blue, style=shape.labeldown, text="LH")

// Plot signals
plotchar(showBuySignals ? longCondition : na, "Long Signal", "▲", location.top, color=color.green)
plotchar(showSellSignals ? shortCondition : na, "Short Signal", "▼", location.bottom, color=color.red)

// Trailing stop loss
stopLossPrice = na
if (longCondition and not na(stopLossPrice))
    stopLossPrice := close - atr * atrMultiplier
if (close <= stopLossPrice)
    strategy.close("Main")
```
```