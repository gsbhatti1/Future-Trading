> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|11|Length|
|v_input_2_open|0|Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|true|From Day|
|v_input_4|true|From Month|
|v_input_5|2020|From Year|
|v_input_6|true|To Day|
|v_input_7|12|To Month|
|v_input_8|2021|To Year|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-12-11 00:00:00
end: 2023-12-17 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © armigoldman

//@version=3
strategy(title="Galileo Galilei", shorttitle="Galileo Galilei", overlay=true, initial_capital = 100000, default_qty_type=strategy.cash, default_qty_value = 100000)
len = input(11, minval=1, title="Length")
src = input(open, title="Source")
out = ema(src, len)
plot(out, title="EMA", color=color.yellow)
//last8h = highest(close, 8)
//lastl8 = lowest(close, 8)

//plot(last8h, color=color.red, linewidth=2)
//plot(lastl8, color=color.green, linewidth=2)

////////////////////////////////////////////////////////////////////////////////
// BACKTESTING RANGE

// From Date Inputs
fromDay = input(defval=1, title="From Day", minval=1, maxval=31)
fromMonth = input(defval=1, title="From Month", minval=1, maxval=12)
fromYear = input(defval=2020, title="From Year", minval=1970)

// To Date Inputs
toDay = input(defval=1, title="To Day", minval=1, maxval=31)
toMonth = input(defval=12, title="To Month", minval=1, maxval=12)
toYear = input(defval=2021, title="To Year", minval=1970)

// Calculate start/end date and
```