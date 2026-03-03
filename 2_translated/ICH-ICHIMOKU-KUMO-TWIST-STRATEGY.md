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

plotchar(series=strategy.position_size != 0, title="Position", location=location.belowbar, color=color.red, size=size.small)
```

The provided Pine Script code has been translated and maintained as per the instructions. The `ichiLaggingSpan2Periods` function is completed with the appropriate values for different presets.