``` pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-10-12 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title="Ichimoku Crypto Breakout", shorttitle="Ichimoku Breakout", overlay=true)

Ten = input(18, minval=1, title="Tenkan")
Kij = input(52, minval=1, title="Kijun")
LeadSpan = input(104, minval=1, title="Senkou B")
Displace = input(52, minval=1, title="Senkou A")
SpanOffset = input(52, minval=1, title="Span Offset")

sts = input(true, title="Show Tenkan")
sks = input(true, title="Show Kijun")
ssa = input(true, title="Show Span A")
ssb = input(true, title="Show Span B")

source = close

//Script for Ichimoku Indicator
donchian(len) => avg(lowest(len), highest(len))
TS = donchian(Ten)
KS = donchian(Kij)
SpanA = avg(TS, KS)
SpanB = donchian(LeadSpan)

CloudTop = max(TS, KS)

Chikou = source[Displace]
SpanAA = avg(TS, KS)[SpanOffset]
SpanBB = donchian(LeadSpan)[SpanOffset]

//Kumo Breakout (Long)
SpanA_Top = SpanAA >= SpanBB ? 1 : 0
SpanB_Top = SpanBB >= SpanAA ? 1 : 0

SpanA_Top2 = SpanA >= SpanB ? 1 : 0
SpanB_Top2 = SpanB >= SpanA ? 1 : 0

SpanA1 = SpanA_Top2 ? SpanA : na
SpanA2 = SpanA_Top2 ? SpanB : na

SpanB1 = SpanB_Top2 ? SpanA : na
SpanB2 = SpanB_Top2 ? SpanB : na

//plot for Tenkan and Kijun (Current Timeframe)
p1= plot(sts and TS ? TS : na, title="Tenkan", linewidth = 2, color = gray)
p2 = plot(sks and KS ? KS : na, title="Kijun", linewidth = 2, color = black)
p5 = plot(close, title="Chikou", linewidth = 2, offset=-Displace, color = orange)

//Plot for Kumo Cloud (Dynamic Color)
p3 = plot(ssa and SpanA ? SpanA : na, title="SpanA", linewidth=2, offset=-SpanOffset, color=color.new(color.blue, 0))
p4 = plot(ssb and SpanB ? SpanB : na, title="SpanB", linewidth=2, offset=-SpanOffset, color=color.new(color.red, 0))
```

This completes the translation while maintaining all code blocks, numbers, and formatting as specified.