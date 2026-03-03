``` pinescript
/*backtest
start: 2023-08-27 00:00:00
end: 2023-09-26 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Coinrule

//@version=4
strategy(shorttitle='Short-term-Trading-Strategy-Based-on-Trend-Following', title='Short-term-Trading-Strategy-Based-on-Trend-Following (by ChaoZhang)', overlay=true, initial_capital = 1000, process_orders_on_close=true, default_qty_type = strategy.percent_of_equity, default_qty_value = 30, commission_type=strategy.commission.percent, commission_value=0.1)

//Backtest dates
fromMonth = input(defval = 1,    title = "From Month",      type = input.integer, minval = 1, maxval = 12)
fromDay   = input(defval = 10,    title = "From Day",        type = input.integer, minval = 1, maxval = 31)
fromYear  = input(defval = 2019, title = "From Year",       type = input.integer, minval = 1970)
thruMonth = input(defval = 1,    title = "Thru Month",      type = input.integer, minval = 1, maxval = 12)
thruDay   = input(defval = 1,    title = "Thru Day",        type = input.integer, minval = 1, maxval = 31)
thruYear  = input(defval = 2112, title = "Thru Year",       type = input.integer, minval = 1970)

showDate  = input(defval = true, title = "Show Date Range", type = input.bool)

start     = timestamp(fromYear, fromMonth, fromDay, 00, 00)        // backtest start window
finish    = timestamp(thruYear, thruMonth, thruDay, 23, 59)        // backtest finish window
window()  => true      // create function "within window of time"

//MA inputs and calculations
movingaverage_fast = sma(close, input(9))
movingaverage_mid  = sma(close, input(50))
movingaverage_slow = sma(close, input(100))

//Trend situation
Bullish = cross(close, movingaverage_fast)

Momentum = movingaverage_mid > movingaverage_slow

// RSI inputs and calculations
lengthRSI = 14
RSI = rsi(close, lengthRSI)

//Entry
strategy.entry(id="long", long=true, when = Bullish and Momentum and RSI > 50)

//Exit

TP = input(70)
SL = input(30)
longTakeProfit  = RSI > TP
longStopPrice   = RSI < SL

strategy.close("long", when = longStopPrice or longTakeProfit and window())

plot(movingaverage_fast, color=color.blue, title='9-day SMA')
plot(movingaverage_mid, color=color.green, title='50-day SMA')
plot(movingaverage_slow, color=color.red, title='100-day SMA')
```

This translation preserves the original code structure and formatting while translating the human-readable text into English.