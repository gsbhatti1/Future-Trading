``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Kaspricci

//@version=5
strategy(
     title = "Double Inside Bar & Trend Strategy - Kaspricci", 
     shorttitle = "Double Inside Bar & Trend", 
     overlay=true, 
     initial_capital = 100000, 
     currency = currency.USD, 
     default_qty_type = strategy.percent_of_equity, 
     default_qty_value = 100, 
     calc_on_every_tick = true, 
     close_entries_rule = "ANY")

// ================================================ Entry Inputs ======================================================================
headlineEntry   = "Entry Settings"

maSource        = input.source(defval = close,             group = headlineEntry, title = "MA Source")
maType          = input.string(defval = "HMA",             group = headlineEntry, title = "MA Type", options = ["EMA", "HMA", "SMA", "SWMA", "VWMA", "WMA"])
maLength        = input.int(   defval = 45,    minval = 1, group = headlineEntry, title = "HMA Length")

float ma = switch maType 
    "EMA"  => ta.ema(maSource,  maLength)
    "HMA"  => ta.hma(maSource,  maLength)
    "SMA"  => ta.sma(maSource,  maLength)
    "SWMA" => ta.swma(maSource)
    "VWMA" => ta.vwma(maSource,
```