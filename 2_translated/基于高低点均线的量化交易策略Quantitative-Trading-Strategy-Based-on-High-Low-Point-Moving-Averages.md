```pinescript
/*backtest
start: 2023-09-11 00:00:00
end: 2023-09-13 00:00:00
Period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("HiLo", overlay=true)

// Testing a specific period
testStartYear = input(2017, "Backtest Start Year")
testStartMonth = input(4, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0)

testStopYear = input(2017, "Backtest Stop Year")
testStopMonth = input(5, "Backtest Stop Month")
testStopDay = input(1, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay,0,0)

// A switch to control background coloring of the test period
testPeriodBackground = input(title="Color Background?", type=bool, defval=true)
testPeriodBackgroundColor = testPeriodBackground and (time >= testPeriodStart) and (time <= testPeriodStop) ? #00FF00 : na
bgcolor(testPeriodBackgroundColor, transp=97)

testPeriod() =>
    time >= testPeriodStart and time <= testPeriodStop ? true : false


// HiLo Strategy
length = input(4, minval=0)
displace = input(0, minval=0)
highsma = sma(high, length)
lowsma = sma(low, length)

longCondition = close > highsma[displace]
if(longCondition)
    strategy.entry("long", true)

shortCondition = close < lowsma[displace]
if(shortCondition)
    strategy.entry("short", false)

// Exit seems with a problem. it keeps saying the order's limit (2000) was
```