> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|true|From Day|
|v_input_int_2|true|From Month|
|v_input_int_3|2018|From Year|
|v_input_int_4|30|Thru Day|
|v_input_int_5|9|Thru Month|
|v_input_int_6|2024|Thru Year|
|v_input_int_7|100|Slow MA length|
|v_input_int_8|30|Fast MA length|


> Source (PineScript)

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
slowMAlen = input.int(defval = 100, title = "Slow MA length", minval = 1)
fastMAlen = input.int(defval = 30, title = "Fast MA length", minval = 1)

// === CALCULATE MOVING AVERAGES ===
smaSlow = ta.sma(close, slowMAlen)
smaFast = ta.sma(close, fastMAlen)

// === BACKTEST RANGE CHECK ===
var datetime startDate = na
if bar_index == 0
    startDate := timestamp(fromYear, fromMonth, fromDay, 0, 0)
if time >= startDate and time < timestamp(thruYear, thruMonth, thruDay, 23, 59)
    // === CROSSOVER LOGIC ===
    if ta.crossover(smaFast, smaSlow)
        strategy.entry("Long", strategy.long)
    else if ta.crossunder(smaFast, smaSlow)
        strategy.close("Long")
```

This Pine Script code implements the SMA moving average crossover strategy with customizable backtest ranges and MA lengths.