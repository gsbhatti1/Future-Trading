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
                104
            else
                52

# Define the strategy based on the Ichimoku Kumo Twist logic
plotshape(series=cross(lead2, conv), location=location.abovebar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=cross(conv, lead2), location=location.belowbar, color=color.red, style=shape.triangledown, title="Sell Signal")

# Calculate the Ichimoku Cloud
conv = (high + low) / 2
base = (xhighest(high, ichiBasePeriods(presets)) + xlowest(low, ichiBasePeriods(presets))) / 2

laggingSpan1 = (conv + base) / 2
lead1 = (high[9] + low[9]) / 2
lead2 = (high[52] + low[52]) / 2

# Plot the Ichimoku Cloud
plot(series=base, title="Baseline", color=color.blue)
plot(series=laggingSpan1, title="Leading Span 1", color=color.orange)
plot(series=lead1, title="Leading Span 1", color=color.green, style=plot.style_linebr)
plot(series=lead2, title="Leading Span 2", color=color.red, style=plot.style_linebr)

# Optional cloud display
if v_input_4
    plot(series=base, title="Baseline", color=color.blue)
    plot(series=laggingSpan1, title="Leading Span 1", color=color.orange)
    plot(series=lead1, title="Leading Span 1", color=color.green, style=plot.style_linebr)
    plot(series=lead2, title="Leading Span 2", color=color.red, style=plot.style_linebr)

# Optional stop loss
if v_input_5 and not na(high[1])
    strategy.exit("Stop Loss", from_entry="Buy Signal")
    strategy.exit("Stop Loss", from_entry="Sell Signal")

# Drop N candles
src := close
src := dropn(src, input(v_input_3 ? v_input_3 : 0))

// Plot the closing price
plot(series=close, title="Close Price", color=color.black)
```