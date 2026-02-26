``` pinescript
/*backtest
start: 2023-03-22 00:00:00
end: 2024-03-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © j0secyn

//@version=5
strategy("MA Cross", overlay=true, margin_long=100, margin_short=100, default_qty_value=100, default_qty_type=strategy.percent_of_equity, initial_capital=10000)

// === INPUT BACKTEST RANGE ===
fromDay   = input.int(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input.int(defval = 1, title = "From Month", minval = 1, maxval = 12)
fromYear  = input.int(defval = 2018,title = "From Year", minval = 1970)
thruDay   = input.int(defval = 30, title = "Thru Day", minval = 1, maxval = 31)
thruMonth = input.int(defval = 9, title = "Thru Month", minval = 1, maxval = 12)
thruYear  = input.int(defval = 2024,title = "Thru Year", minval = 1970)

// === INPUT MA LENGTHS ===
slowMAlen = input.int(title="Slow MA Length", defval=100, minval=1, maxval=500)
fastMAlen = input.int(title="Fast MA Length", defval=30, minval=1, maxval=200)

// === CALCULATE MAs ===
slowMA = sma(close, slowMAlen)
fastMA = sma(close, fastMAlen)

// === CHECK BACKTEST RANGE ===
var bool inBacktestRange = false
if (time >= timestamp(fromYear, fromMonth, fromDay, 0, 0) and time <= timestamp(thruYear, thruMonth, thruDay, 23, 59))
    inBacktestRange := true

// === CROSSOVER LOGIC ===
longCondition = inBacktestRange and crossover(fastMA, slowMA)
if (longCondition)
    strategy.entry("Long", strategy.long)

shortCondition = inBacktestRange and crossunder(fastMA, slowMA)
if (shortCondition)
    strategy.close("Long")

// === PLOTTING ===
plot(slowMA, title="Slow MA", color=color.blue)
plot(fastMA, title="Fast MA", color=color.red)
```