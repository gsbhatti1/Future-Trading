``` pinescript
/*backtest
start: 2023-09-02 00:00:00
end: 2023-09-09 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("Gunbot - Bbands", shorttitle="Strategy", overlay=true, pyramiding=100, default_qty_value=100000000, precision=8)

/////////////// Component Code Start ///////////////
testStartYear = input(2016, "Backtest Start Year") 
testStartMonth = input(8, "Backtest Start Month")
testStartDay = input(10, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0)

testStopYear = input(2020, "Backtest Stop Year")
testStopMonth = input(9, "Backtest Stop Month")
testStopDay = input(29, "Backtest Stop Day")
// testStopDay = testStartDay + 1
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay,0,0)

testPeriod() =>
    true
/////////////// Component Code Stop ///////////////

length = input(15, minval=1)
src = input(close, title="Source")
mult = input(2.0, minval=0.001, maxval=50)
low_bb = input(25, title="LOW_BB")
high_bb = input(25, title="HIGH_BB")

basis = sma(src, length * (15 / timeframe.multiplier))
dev = mult * stdev(src, length * (15 / timeframe.multiplier))
upper = basis + dev
upper_high_bb = upper - ((upper-basis) * (high_bb / 100))
lower = basis - dev
lower_low_bb = lower + ((basis-lower) * (low_bb / 100))

bb_percent = ((upper/lower)-1)*100
bb_diff = (upper-lower)

/////////////// STRATEGY ///////////////
tsi = input(0, "Activate TS") / 100000000
ts = input(99999, "Trailing Stop") / 100000000
tp = input(99999, "Take Profit") / 100000000
sl = input(99999, "Stop Loss") / 100000000

pyrl = input(0, "Pyramiding <")
pyre = input(1, "Pyramiding =")
pyrg = input(100, "Pyramiding >")

long = ohlc4 < lower_low_bb
short = ohlc4 > upper_high_bb

sectionLongs = 0
sectionLongs := nz(sectionLongs[1])
sectionShorts = 0
sectionShorts := nz(sectionShorts[1])

if long
    sectionLongs := sectionLongs + 1
    sectionShorts := 0

if short
    sectionLongs := 0
    sectionShorts := sectionShorts + 1

longCondition = long and sectionLongs <= pyrl or long and sectionLongs >= pyrg or long and sectionLongs == pyre
shortCondition = short and sectionShorts <= pyrl or short and sectionShorts >= pyrg or short and sectionShorts == pyre

last_open_longCondition = na
last_open_shortCondition = na
last_open_longCondition := longCondition ? close : nz(last_open_longCondition[1])
last_open_shortCondition := shortCondition ? close : nz(last_open_shortCondition[1])

sectionLongs2 = 0
sectionLongs2 := nz(sectionLongs2[1])
sectionShorts2 = 0
sectionShorts2 := nz(sectionShorts2[1])

if longCondition
    sectionLongs2 := sectionLongs2 + 1
    sectionShorts2 := 0

if shortCondition
    sectionLongs2 := 0
    sectionShorts2 := sectionShorts2 + 1

isAdding = input(false, "WIP Feature", bool)

stackingLongs = 100000000
stackingLongs := nz(stackingLongs[1])
stackingShorts = 100000000
stackingShorts := nz(stackingShorts[1])

if longCondition
    stackingLongs := stackingLongs * 2
    stackingShorts := 100000000
    
if shortCondition
    stackingLongs := 100000000 
    stackingShorts := stackingShorts * 2
    
totalLongs = 0.0
totalLongs := nz(totalLongs[1])
totalShorts = 0.0
totalShorts := nz(totalShorts[1])
totalMartingaleLongs = 0.0
totalMartingaleLongs := nz(totalMartingaleLongs[1])
totalMartingaleShorts = 0.0
totalMartingaleShorts := nz(totalMartingaleShorts[1])

if longCondition and sectionLongs2 >= 1
    totalMartingaleLongs := totalMartingaleLongs + (last_open_longCondition * stackingLongs)
    totalLongs := totalLongs + last_open_longCondition
    totalShorts := 0.0

if shortCondition and sectionShorts2 >= 1
    totalLongs := 0.0
    totalMartingaleShorts := totalMartingaleShorts + (last_open_shortCondition * stackingShorts)
```