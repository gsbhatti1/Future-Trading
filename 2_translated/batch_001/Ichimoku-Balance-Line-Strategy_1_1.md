``` pinescript
/*backtest
start: 2022-12-19 00:00:00
end: 2023-12-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
// Credit for the initial code to nathanhoffer - I simply added the ability to select a time period
//
strategy("Cloud Breakout", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.0)

/////////////// Component Code Start ///////////////
testStartYear = input(2016, "Backtest Start Year")
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay, 0, 0)

testStopYear = input(2019, "Backtest Stop Year")
testStopMonth = input(12, "Backtest Stop Month")
testStopDay = input(31, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStartMonth,testStartDay, 0, 0)

testPeriod() => true

Ten = input(18, minval=1, title="Tenkan")
Kij = input(60, minval=1, title="Kijun")
LeadSpan = input(30, minval=1, title="Senkou B")
Displace = input(52, minval=1, title="Senkou A")
SpanOffset = input(52, minval=1, title="Span Offset")

sts = input(true, title="Show Tenkan")
sks = input(true, title="Show Kijun")
ssa = input(true, title="Show Span A")
ssb = input(true, title="Show Span B")
sc = input(true, title="Show Chikou")

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

//Kumo Breakout (Short)
SpanA_Bottom = SpanAA < SpanBB ? 1 : 0
SpanB_Bottom = SpanBB < SpanAA ? 1 : 0

SpanA_Bottom2 = SpanA < SpanB ? 1 : 0
SpanB_Bottom2 = SpanB < SpanA ? 1 : 0

// Entry Conditions
buyCondition = (SpanA_Top == 1 and SpanA_Top2 == 1) and cloudTop >= source[Displace]
sellCondition = (SpanA_Bottom == 1 and SpanA_Bottom2 == 1) or (SpanB_Bottom == 1 and SpanB_Bottom2 == 1)

// Plotting
plot(series=TS, title="Tenkan-sen", color=color.blue)
plot(series=KS, title="Kijun-sen", color=color.orange)
plot(series=SpanA, title="Senkou Span A", color=color.green)
plot(series=SpanB, title="Senkou Span B", color=color.red)

if (buyCondition)
    strategy.entry("Buy", strategy.long)

if (sellCondition)
    strategy.close("Buy")

// Chikou Span Plot
plot(source=Chikou, title="Chikou Span", color=color.purple, offset=-Displace)

```

This script now includes the short condition and the final trading logic to enter buy or sell positions based on the Ichimoku Cloud Breakout.