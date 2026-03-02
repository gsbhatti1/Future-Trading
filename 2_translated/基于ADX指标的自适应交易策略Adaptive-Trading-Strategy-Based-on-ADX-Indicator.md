``` pinescript
/*backtest
start: 2023-01-10 00:00:00
end: 2024-01-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © MAURYA_ALGO_TRADER

//@version=5
strategy("Monthly Performance by Dr. Maurya", overlay=true, default_qty_value = 15, commission_type = strategy.commission.percent, commission_value = 0.1)

len = input(14)
th = input(20)

TrueRange = math.max(math.max(high - low, math.abs(high - nz(close[1]))), math.abs(low - nz(close[1])))
DirectionalMovementPlus = high - nz(high[1]) > nz(low[1]) - low ? math.max(high - nz(high[1]), 0) : 0
DirectionalMovementMinus = nz(low[1]) - low > high - nz(high[1]) ? math.max(nz(low[1]) - low, 0) : 0

SmoothedTrueRange = 0.0
SmoothedTrueRange := nz(SmoothedTrueRange[1]) - nz(SmoothedTrueRange[1]) / len + TrueRange

SmoothedDirectionalMovementPlus = 0.0
SmoothedDirectionalMovementPlus := nz(SmoothedDirectionalMovementPlus[1]) - nz(SmoothedDirectionalMovementPlus[1]) / len + DirectionalMovementPlus

SmoothedDirectionalMovementMinus = 0.0
SmoothedDirectionalMovementMinus := nz(SmoothedDirectionalMovementMinus[1]) - nz(SmoothedDirectionalMovementMinus[1]) / len + DirectionalMovementMinus

DIplus = SmoothedDirectionalMovementPlus / SmoothedTrueRange * 100
DIminus = SmoothedDirectionalMovementMinus / SmoothedTrueRange * 100
DX = math.abs(DIplus - DIminus)
ADX = sma(DX, th)

longCondition = DIplus > ADX + input(10) and ADX < DIplus
shortCondition = DIminus > ADX + input(10) and ADX < DIminus

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

plotshape(series=longCondition, location=v_input_5, style=shape.triangleup, color=v_input_color_1, title="Long Entry")
plotshape(series=shortCondition, location=v_input_5, style=shape.triangledown, color=v_input_color_1, title="Short Entry")

// Optional: Plot ADX and DI lines
plot(ADX, color=color.blue, title="ADX", linewidth=2)
plot(DIplus, color=color.green, title="DI+", linewidth=1)
plot(DIminus, color=color.red, title="DI-", linewidth=1)

// Optional: Stop Loss/Trailing Stop
stopLossLevel = input.float(50, minval=0.0)
trailDistance = input.float(20, minval=0.0)

if (strategy.position_size > 0 and close < strategy.position_avg_price - stopLossLevel * TrueRange[1])
    strategy.close("Close Long")

if (strategy.position_size < 0 and close > strategy.position_avg_price + stopLossLevel * TrueRange[1])
    strategy.close("Close Short")

trailStop = trailDistance * TrueRange
if (strategy.position_size > 0)
    strategy.exit("Trailing Stop", from_entry="Long", trail_offset=trailStop)

if (strategy.position_size < 0)
    strategy.exit("Trailing Stop", from_entry="Short", trail_offset=trailStop)
```

This Pine Script implementation covers the core logic of the described trading strategy, including the calculation of True Range and Directional Movement indicators, and the use of ADX to generate trading signals. The script also includes optional features for visualizing the DI+ and DI- lines, as well as setting up stop loss and trailing stops.