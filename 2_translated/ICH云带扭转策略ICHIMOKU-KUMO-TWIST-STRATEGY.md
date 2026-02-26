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

plotshape(series=chiKumo, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=crossKumo, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

ichimoku = ichiConversionPeriods(v_input_2) < 10 ? true : false

if ichimoku
    conversionLine = xhighest(high, ichiConversionPeriods(v_input_2))
    baseLine = xlowest(low, ichiBasePeriods(v_input_2))
    laggingSpan1 = (conversionLine + baseLine) / 2
    laggingSpan2 = xhighest(low, ichiLaggingSpan2Periods(v_input_2))

    buySignal = crossover(laggingSpan1, laggingSpan2)
    sellSignal = crossunder(laggingSpan1, laggingSpan2)

    if v_input_4
        plotchiKumo(conversionLine)
        plotchiKumo(baseLine)
        plotchiKumo(laggingSpan1)
        plotchiKumo(laggingSpan2)
    
    strategy.entry("Buy", strategy.long, when=buySignal)
    if (v_input_5 and buySignal)
        strategy.exit("Stop Loss", "Buy", stop=laggingSpan2)

else
    conversionLine = xhighest(high, 9)
    baseLine = xlowest(low, 26)
    laggingSpan1 = (conversionLine + baseLine) / 2
    laggingSpan2 = xhighest(low, 52)

    buySignal = crossover(laggingSpan1, laggingSpan2)
    sellSignal = crossunder(laggingSpan1, laggingSpan2)

    if v_input_4
        plotchiKumo(conversionLine)
        plotchiKumo(baseLine)
        plotchiKumo(laggingSpan1)
        plotchiKumo(laggingSpan2)
    
    strategy.entry("Buy", strategy.long, when=buySignal)
    if (v_input_5 and buySignal)
        strategy.exit("Stop Loss", "Buy", stop=laggingSpan2)

plotchiKumo(conversionLine, title="Conversion Line")
plotchiKumo(baseLine, title="Base Line")
plotchiKumo(laggingSpan1, title="Lagging Span 1")
plotchiKumo(laggingSpan2, title="Lagging Span 2")

// Drop the first N candles
if v_input_3
    high := dropn(high, 9)
    low := dropn(low, 9)

```

Note: The code was carefully translated and formatted to preserve the original structure and functionality.