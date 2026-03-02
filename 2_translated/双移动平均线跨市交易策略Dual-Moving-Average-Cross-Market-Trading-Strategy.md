``` pinescript
/*backtest
start: 2023-09-23 00:00:00
end: 2023-10-23 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © exlux99

//@version=4


strategy(title="Swing HULL + T3 avg", shorttitle="Swing HULL T3 AVG", overlay=true)

fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2000, title = "From Year", minval = 1970)

// To Date Inputs
toDay = input(defval = 31, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 12, title = "From Month", minval = 1, maxval = 12)
toYear = input(defval = 2021, title = "To Year", minval = 1970)

startDate = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finishDate = timestamp(toYear, toMonth, toDay, 00, 00)
time_cond = true


////////////////////////////GENERAL INPUTS//////////////////////////////////////

length_Ma= input(defval=50, title="Length MAs", minval=1)

//==========HMA
getHULLMA(src, len) =>
    hullma = wma(2*wma(src, len/2)-wma(src, len), round(sqrt(len)))
    hullma

//==========T3 MA
t3ma(source, length, factor, order) =>
    t3 = 0.0
    for i = 1 to (order * 2 + 1)
        mul = ((factor / (length * 2)) * (i - 1))
        tmp = wma(source, length * pow(2, (order - i)))
        t3 := t3 + (mul * tmp)
    t3

hullMAMa = getHULLMA(close, length_Ma)
t3MaVal = t3ma(close, length_Ma, 0.5, 7)

avgLine = (hullMAMa + t3MaVal) / 2
plot(avgLine, title="Average Line", color=color.blue)


// Entry and Exit Logic

longEntry = crossover(avgLine, hullMAMa)
shortEntry = crossunder(avgLine, hullMAMa)

tpLong = input(0.08, title="TP Long")
slLong = input(true, title="SL Long")
tpShort = input(0.03, title="TP Short")
slShort = input(0.06, title="SL Short")

longOrder = order(entry=true, amount=parameters.amount.long, limit=(avgLine * (1 + tpLong)))
if (longEntry)
    strategy.entry("Long", strategy.long)

if (slLong and longOrder)
    strategy.exit(id="Long SL", from_entry="Long", stop=(avgLine * (1 - slLong)))

shortOrder = order(entry=true, amount=parameters.amount.short, limit=(avgLine * (1 - tpShort)))
if (shortEntry)
    strategy.entry("Short", strategy.short)

if (slShort and shortOrder)
    strategy.exit(id="Short SL", from_entry="Short", stop=(avgLine * (1 + slShort)))

```

This Pine Script translates the provided Chinese text into English, keeping all code blocks and formatting intact.