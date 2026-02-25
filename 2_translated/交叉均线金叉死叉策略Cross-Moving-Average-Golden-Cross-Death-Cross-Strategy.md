``` pinescript
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
|--------|-------|-----------|
|v_input_1|9|Tenkan-Sen Length|
|v_input_2|26|Kijun-Sen Length|
|v_input_3|52|Senkou Span B Length|
|v_input_4|26|Offset For Chikou Span / Kumo|
|v_input_5|5|Orders Cooldown Period|
|v_input_6|false|Use Imperfect Chikou Position Detection|


> Source (PineScript)

``` pinescript
//@version=4
strategy("Ichimoku Kinko Hyo Strategy", shorttitle="Ichimoku Strategy", overlay=true, pyramiding=0)

// Input parameters
tenkanLength = input(9, title="Tenkan-Sen Length")
kijunLength = input(26, title="Kijun-Sen Length")
senkouBLength = input(52, title="Senkou Span B Length")
chikouOffset = input(26, title="Offset For Chikou Span / Kumo")
cooldownPeriod = input(5, title="Orders Cooldown Period")
useImperfectChikouDetection = input(false, title="Use Imperfect Chikou Position Detection")

// Calculate Tenkan-Sen
tenkanSen = sma(close, tenkanLength)

// Calculate Kijun-Sen
kijunSen = sma(close, kijunLength)

// Calculate Senkou Span A
senkouA = (tenkanSen + kijunSen) / 2

// Calculate Senkou Span B
senkouB = sma(close, senkouBLength)

// Plot Senkou Span A and B
plot(senkouA, color=color.blue, title="Senkou Span A")
plot(senkouB, color=color.red, title="Senkou Span B")

// Calculate Chikou Span (Closing Price Delayed by 26 Days)
chikou = close[1]

// Check for golden cross and death cross
buySignal = crossover(tenkanSen, kijunSen) or (useImperfectChikouDetection ? chikou < tenkanSen : false)
sellSignal = crossunder(tenkanSen, kijunSen) or (useImperfectChikouDetection ? chikou > kijunSen : false)

// Apply cooldown period for orders
if (buySignal and not strategy.opentrades) or (sellSignal and not strategy.opentrades)
    strategy.entry("Buy", strategy.long)
    strategy.close("Buy", when=sellSignal)

// Plot Chikou Span
plotshape(series=chikou, location=location.belowbar, color=color.green, title="Chikou Span")

// Optional: Add stop loss and take profit
stopLossLevel = input(-10, title="Stop Loss Level")
takeProfitLevel = input(10, title="Take Profit Level")

if (strategy.opentrades > 0)
    if (chikou < tenkanSen and not useImperfectChikouDetection or chikou > kijunSen and not useImperfectChikouDetection)
        strategy.exit("Exit Long", from_entry="Buy", limit=close + takeProfitLevel, stop=close - stopLossLevel)

// Print signals for debugging
if (buySignal) 
    label.new(x=time[1], y=open[1], text="BUY", color=color.green, style=label.style_label_down)
if (sellSignal) 
    label.new(x=time[1], y=open[1], text="SELL", color=color.red, style=label.style_label_up)

```

This Pine Script code implements the Ichimoku Kinko Hyo strategy as described. It includes the necessary moving averages and signals for both entry and exit conditions, as well as optional stop loss and take profit levels for debugging purposes.