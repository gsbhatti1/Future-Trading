> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|0|Scaling: Linear|Log|
|v_input_2|0|Presets: Cpt 20 60 120 30|Cpt 10 30 60 30|Std 18 52 104 26|Std 9 26 52 26|
|v_input_3|true|Drop first N candles|
|v_input_4|false|Show Clouds|
|v_input_5|true|Stop Loss|
|v_input_6|10|From Month|
|v_input_7|3|From Day|
|v_input_8|2017|From Year|
|v_input_9|true|To Month|
|v_input_10|true|To Day|
|v_input_11|9999|To Year|


> Source (PineScript)

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
presets = input(title="Presets", options=["Cpt 20 60 120 30", "Cpt 10 30 60 30", "Std 18 52 104 26", "Std 9 26 52 26"], defval="Std 18 52 104 26")
drop_first_n = input(title="Drop first N candles", type=bool, defval=true)
show_clouds = input(title="Show Clouds", type=bool, defval=false)
stop_loss = input(title="Stop Loss", type=bool, defval=true)
from_month = input(title="From Month", type=int, defval=10)
from_day = input(title="From Day", type=int, defval=3)
from_year = input(title="From Year", type=int, defval=2017)
to_month = input(title="To Month", type=bool, defval=true)
to_day = input(title="To Day", type=bool, defval=true)
to_year = input(title="To Year", type=int, defval=9999)

// Ichimoku Cloud Calculation
conversion_line = xlowest(hl2, ichiConversionPeriods(presets))
base_line = xhighest(high, ichiBasePeriods(presets))
lagging_span1 = xhighest(low, ichiLaggingSpan2Periods(presets))
lagging_span2 = (conversion_line + base_line) / 2
cloud_high = max(lagging_span1, lagging_span2)
cloud_low = min(lagging_span1, lagging_span2)

// Signal Generation
var float stopLossPrice = na
if change(time("M"))
    if to_month and to_day and to_year
        strategy.entry("Buy", strategy.long, when=above(conversion_line, base_line))
        strategy.exit("Stop Loss", "Buy", when=below(conversion_line, base_line) or below(close, stopLossPrice))
    else
        strategy.entry("Sell", strategy.short, when=below(conversion_line, base_line))
        strategy.exit("Stop Loss", "Sell", when=above(conversion_line, base_line) or above(close, stopLossPrice))

if drop_first_n and bar_index < n
    na
else
    plot(cloud_high, color=color.blue)
    plot(cloud_low, color=color.blue)

if show_clouds
    strategy.entry("Buy", strategy.long, when=above(conversion_line, base_line))
    strategy.exit("Stop Loss", "Buy", when=below(conversion_line, base_line) or below(close, stopLossPrice))

// Stop Loss Implementation
if stop_loss and not na(stopLossPrice)
    stopLossPrice := low[1]
    if close < stopLossPrice
        strategy.close("Buy")
```

This PineScript code defines the Ichimoku Kumo Twist Strategy (Presets) with various input parameters for customizing the trading behavior. The script calculates the Ichimoku Cloud and generates buy/sell signals based on specific conditions, incorporating a stop loss mechanism to manage risk.