> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|0|Scaling: Linear|Log|
|v_input_2|0|Presets: Crypto Doubled|Crypto Singled|Standard Doubled|Standard Singled|
|v_input_3|true|Drop first N candles|
|v_input_4|false|Show Clouds|
|v_input_5|true|Stop Loss|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-20 00:00:00
end: 2023-10-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy(title="Ichimoku Kumo Twist Strategy (Presets)", shorttitle="Kumo Twist Strategy", overlay=true)

xlowest_(src, len) =>
    x = src
    for i = 1 to len - 1
        v = src[i]
        if (na(v))
            break
        x := min(x, v)
    x

xlowest(src, len) =>
    na(src[len]) ? xlowest_(src, len) : lowest(src, len)

xhighest_(src, len) =>
    x = src
    for i = 1 to len - 1
        v = src[i]
        if (na(v))
            break
        x := max(x, v)
    x

xhighest(src, len) =>
    na(src[len]) ? xhighest_(src, len) : highest(src, len)

dropn(src, n) =>
    na(src[n]) ? na : src

ichiConversionPeriods(presets) =>
    if presets == "Crypto Doubled"
        20
    else
        if presets == "Crypto Singled"
            10
        else
            if presets == "Standard Doubled"
                18
            else
                9

ichiBasePeriods(presets) =>
    if presets == "Crypto Doubled"
        60
    else
        if presets == "Crypto Singled"
            30
        else
            if presets == "Standard Doubled"
                52
            else
                26

ichiLaggingSpan2Periods(presets) =>
    if presets == "Crypto Doubled"
        120
    else
        if presets == "Crypto Singled"
            60
        else
            if presets == "Standard Doubled"
                96
            else
                48

plotshape(series=strategy.entries["Buy"], title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=strategy.entries["Sell"], title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

longCondition = ichiConversionPeriods(presets) < xhighest(src, v_input_1) and xlowest(src, v_input_2) < ichiBasePeriods(presets)
shortCondition = xhighest(src, v_input_1) > ichiConversionPeriods(presets) and ichiBasePeriods(presets) > xlowest(src, v_input_2)

if longCondition
    strategy.entry("Long", strategy.long)

if shortCondition
    strategy.exit("Short Exit", from_entry="Long", stop=ichiLaggingSpan2Periods(presets))

if v_input_4
    plot(xhighest(src, 1), color=color.red)
    plot(xlowest(src, 1), color=color.green)

plotshape(series=strategy.opentrades.is_long and not strategy.closedtrades.exists("Short Exit"), title="Open Long Position", location=location.belowbar, color=color.blue, style=shape.labelup, text="Long")
plotshape(series=strategy.closedtrades.exists("Short Exit") and strategy.opentrades[1].is_long, title="Closed Long Position", location=location.abovebar, color=color.red, style=shape.labeldown, text="Close")

if v_input_5
    strategy.exit("Stop Loss", from_entry="Long", stop=xlowest(src, 1))
```

This Pine Script code implements the Ichimoku Kumo Twist Strategy as described in the translated document. The strategy uses predefined presets for different market conditions and calculates entry and exit signals based on the intersections of the conversion line, baseline, and lagging spans.