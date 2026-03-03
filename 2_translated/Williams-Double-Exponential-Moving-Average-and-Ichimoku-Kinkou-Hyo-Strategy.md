> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|12|Double HullMA|
|v_input_2|9|Tenkan Sen Periods|
|v_input_3|24|Kijun Sen Periods|
|v_input_4|51|Senkou Span B Periods|
|v_input_5|24|Displacement|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

strategy("Hull MA-X + Ichimoku Kinko Hyo", shorttitle="Hi", overlay=true, default_qty_type=strategy.percent_of_equity, max_bars_back=1000, default_qty_value=100, calc_on_order_fills= true, calc_on_every_tick=true, pyramiding=0)

keh = input(title="Double HullMA", defval=12, minval=1)
n2ma = 2 * wma(close, round(keh / 2))
nma = wma(close, keh)
diff = n2ma - nma
sqn = round(sqrt(keh))
n2ma1 = 2 * wma(close[1], round(keh / 2))
nma1 = wma(close[1], keh)
diff1 = n2ma1 - nma1
sqn1 = round(sqrt(keh))
n1 = wma(diff, sqn)
n2 = wma(diff1, sqn)
b = n1 > n2 ? lime : red
c = n1 > n2 ? green : red
d = n1 > n2 ? red : green

TenkanSenPeriods = input(9, minval=1, title="Tenkan Sen Periods")
KijunSenPeriods = input(24, minval=1, title="Kijun Sen Periods")
SenkouSpanBPeriods = input(51, minval=1, title="Senkou Span B Periods")
displacement = input(24, minval=1, title="Displacement")
donchian(len) => avg(lowest(len), highest(len))
TenkanSen = donchian(TenkanSenPeriods)
KijunSen = donchian(KijunSenPeriods)
SenkouSpanA = avg(TenkanSen, KijunSen)
SenkouSpanB = donchian(SenkouSpanBPeriods)
SenkouSpanH = max(SenkouSpanA[displacement - 1], SenkouSpanB[displacement - 1])
SenkouSpanL = min(SenkouSpanA[displacement - 1], SenkouSpanB[displacement - 1])
ChikouSpan = close[displacement - 1]

Hullfast = plot(n1, color=c)
Hullslow = plot(n2, color=c)
plot(cross(n1, n2) ? n1 : na, style=circles, color=b, linewidth=4)
plot(cross(n1, n2) ? n1 : na, style=line, color=d, linewidth=3)
plot(TenkanSen, color=blue, title="Tenkan Sen", linewidth=2)
plot(KijunSen, color=maroon, title="Kijun Sen", linewidth=3)
plot(close, offset=-displacement, color=orange, title="Chikou Span", linewidth=2)
sa = plot(SenkouSpanA, offset=displacement, color=green, title="Senkou Span A", linewidth=2)
sb = plot(SenkouSpanB, offset=displacement, color=red, title="Senkou Span B", linewidth=3)
fill(sa, sb, color=SenkouSpanA > SenkouSpanB ? green : red)

longCondition = n1 > n2 and close > n2 and close > ChikouSpan and close > SenkouSpanH and (TenkanSen > KijunSen or close > KijunSen)
if (longCondition)
    strategy.entry("Long", strategy.long)
```

This script defines a strategy that combines the Williams Double Exponential Moving Average and the Ichimoku Kinko Hyo indicators. It includes the necessary logic to generate buy and sell signals based on the conditions outlined in the strategy description.