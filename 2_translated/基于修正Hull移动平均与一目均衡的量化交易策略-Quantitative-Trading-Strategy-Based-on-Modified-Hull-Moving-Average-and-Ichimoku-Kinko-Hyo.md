``` pinescript
/*backtest
start: 2024-04-20 00:00:00
end: 2024-04-27 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Hull MA_X + Ichimoku Kinko Hyo Strategy", shorttitle="HMX+IKHS", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, pyramiding=0)

// Hull Moving Average Parameters
keh = input(12, title="Double HullMA")
n2ma = 2 * wma(close, round(keh/2)) - wma(close, keh)
sqn = round(sqrt(keh))
hullMA = wma(n2ma, sqn)

// Ichimoku Kinko Hyo Parameters
tenkanSenPeriods = input(9, title="Tenkan Sen Periods")
kijunSenPeriods = input(26, title="Kijun Sen Periods")
senkouSpanBPeriods = input(52, title="Senkou Span B Periods")
displacement = input(26, title="Displacement")

// Ichimoku Calculations
highestHigh = highest(high, max(tenkanSenPeriods, kijunSenPeriods))
lowestLow = lowest(low, max(tenkanSenPeriods, kijunSenPeriods))
tenkanSen = (highestHigh + lowestLow) / 2
kijunSen = sma(close, kijunSenPeriods)
senkouSpanAShift = na
if (barstate.islast)
    senkouSpanAShift := (tenkanSen + kijunSen) / 2
senkouSpanA = na
if (barstate.islast)
    senkouSpanA := plot(senkouSpanAShift, title="Senkou Span A", style=plot.style_line, color=color.blue)
senkouSpanB = hlc3(-displacement, hlc3(0, displacement))

// Generate Trading Signals
longCondition = crossover(hullMA, kijunSen) and close > senkouSpanA
shortCondition = crossunder(hullMA, kijunSen) and close < senkouSpanA

// Execute Trades
if (longCondition)
    strategy.entry("Long", strategy.long)
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Trades
if (barstate.islast)
    if (crossover(hullMA, kijunSen) and close > senkouSpanA)
        strategy.close("Long")
    if (crossunder(hullMA, kijunSen) and close < senkouSpanA)
        strategy.close("Short")
```

This Pine Script code defines a strategy that combines the modified Hull Moving Average (HMA) with the Ichimoku Kinko Hyo (IKHS) to generate trading signals. The strategy uses the provided inputs to calculate the necessary indicators and generate long and short positions based on the crossover and crossunder conditions between the HMA and the Kijun Sen, with additional filtering by the cloud (Kumo).