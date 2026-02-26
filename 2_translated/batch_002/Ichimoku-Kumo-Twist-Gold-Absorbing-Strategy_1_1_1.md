``` pinescript
/*backtest
start: 2023-11-20 00:00:00
end: 2023-11-27 00:00:00
period: 3m
basePeriod: 1m
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
    if presets == "Cpt 20 60 120 30"
        20
    else
        if presets == "Cpt 10 30 60 30"
            10
        else
            if presets == "Std 18 52 104 26"
                18
            else
                9

ichiBasePeriods(presets) =>
    if presets == "Cpt 20 60 120 30"
        60
    else
        if presets == "Cpt 10 30 60 30"
            30
        else
            if presets == "Std 18 52 104 26"
                52
            else
                26

ichiLaggingSpan2Periods(presets) =>
    if presets == "Cpt 20 60 120 30"
        120
    else
        if presets == "Cpt 10 30 60 30"
            60
        else
            if presets == "Std 18 52 104 26"
                104
            else
                52

ichiDisplacement(presets) =>
    if presets == "Cpt 20 60 120 30"
        30
    else
        if presets == "Cpt 10 30 60 30"
            30
        else
            if presets == "Std 18 52 104 26"
                26
            else
                26

scaling = input(title="Scaling", options=["Linear", "Log"], defval="Linear")
presets = input(title="Presets", options=["Cpt 20 60 120 30", "Cpt 10 30 60 30", "Std 18 52 104 26"])
cloudshow = input(title="Show Clouds", defval=true)
stoploss = input(title="Stop Loss", defval=false)
frommonth = input(title="From Month", type=input.integer, defval=10)
fromday = input(title="From Day", type=input.integer, defval=3)
fromyear = input(title="From Year", type=input.integer, defval=2017)
tomonth = input(title="To Month", type=input.integer, defval=true)
today = input(title="To Day", type=input.integer, defval=true)
toyear = input(title="To Year", type=input.integer, defval=9999)

// Define variables for the Ichimoku Cloud
conversionline = ichiConversionPeriods(presets)
baseperiod = ichiBasePeriods(presets)
laggingspan2 = ichiLaggingSpan2Periods(presets)
displacement = ichiDisplacement(presets)
highprice = xhighest(high, conversionline)
lowprice = xlowest(low, conversionline)
conversionline = (highprice + lowprice) / 2
baseperiod1 = xhighest(close, baseperiod)
baseperiod2 = xlowest(close, baseperiod)
laggingspan1 = (baseperiod1 + baseperiod2) / 2

// Plot the Ichimoku Cloud
plot(laggingspan1, title="Leading Span A", color=color.blue, linewidth=1)
plot(laggingspan2, title="Leading Span B", color=color.red, linewidth=1)
hline(0, "Zero Line")

// Generate signals
longcondition = crossover(conversionline, baseperiod1) and (not stoploss or close > laggingspan2)
shortcondition = crossunder(conversionline, baseperiod1) and (not stoploss or close < laggingspan2)

if longcondition
    strategy.entry("Long", strategy.long)
if shortcondition
    strategy.exit("Short", "Long")

// Date range filter
fromdate = timestamp(fromyear, frommonth, fromday, 0, 0)
todate = timestamp(toyear, tomonth, today, 23, 59)
isintraderange = time >= fromdate and time <= todate

if isintraderange
    if cloudshow
        plotshape(series=longcondition, title="Long Signal", location=location.belowbar, color=color.green, style=shape.triangleup, text="BUY")
    else
        strategy.entry("Long", strategy.long)
else
    strategy.close("Long")

```
```