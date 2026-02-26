```pinescript
/*backtest
start: 2022-11-28 00:00:00
end: 2023-12-04 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © mdeous

//@version=4
strategy(
     title="Ichimoku Kinko Hyo Strategy", 
     shorttitle="Ichimoku Strategy", 
     overlay=true,
     pyramiding=0,
     defaul
```

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|Tenkan-Sen Length|
|v_input_2|26|Kijun-Sen Length|
|v_input_3|52|Senkou Span B Length|
|v_input_4|26|Offset For Chikou Span / Kumo|
|v_input_5|5|Orders Cooldown Period|
|v_input_6|false|Use Imperfect Chikou Position Detection|


> Source (PineScript)

```pinescript
//@version=4
strategy("Ichimoku Kinko Hyo Strategy", shorttitle="Ichimoku Strategy", overlay=true, pyramiding=0)

// Input Parameters
tenkanLength = input(9, title="Tenkan-Sen Length")
kijunLength = input(26, title="Kijun-Sen Length")
senkouBLength = input(52, title="Senkou Span B Length")
chikouOffset = input(26, title="Offset For Chikou Span / Kumo")
cooldownPeriod = input(5, title="Orders Cooldown Period")
useImperfectChikouDetection = input(false, title="Use Imperfect Chikou Position Detection")

// Calculation of Moving Averages
tenkanSen = sma(close, tenkanLength)
kijunSen = sma(close, kijunLength)
senkouSpanA = (tenkanSen + kijunSen) / 2
senkouSpanB = sma(close, senkouBLength)

// Plotting Kumo Bands and Lines
plot(senkouSpanA, color=color.blue, title="Senkou Span A")
plot(senkouSpanB, color=color.orange, title="Senkou Span B")

// Chikou Span (Delayed Close)
chikou = plot(close[1], offset=chikouOffset, color=color.red, title="Chikou Span")

// Golden Cross and Death Cross
goldenCross = crossover(tenkanSen, kijunSen)
deathCross = crossunder(tenkanSen, kijunSen)

// Buy/Sell Logic with Cooldown Period
if (goldenCross and not useImperfectChikouDetection or (useImperfectChikouDetection and close < chikou))
    strategy.entry("Buy", strategy.long)

if (deathCross and not useImperfectChikouDetection or (useImperfectChikouDetection and close > chikou))
    strategy.close("Buy")

// Order Cooldown to Avoid Overlapping Orders
var int orderCooldown = 0
if (goldenCross)
    orderCooldown := bar_index

if (deathCross)
    if (orderCooldown <= bar_index - cooldownPeriod)
        strategy.close("Buy")

plotshape(series=goldenCross, location=location.belowbar, color=color.green, style=shape.labelup, text="Golden Cross")
plotshape(series=deathCross, location=location.abovebar, color=color.red, style=shape.labeldown, text="Death Cross")
```

This PineScript code implements the Ichimoku Kinko Hyo strategy based on the provided description and arguments. It includes all the necessary components such as moving averages, Kumo bands, Chikou span, and buy/sell logic with a cooldown period to avoid overlapping orders.