``` pinescript
/*backtest
start: 2022-12-18 00:00:00
end: 2023-12-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
//@author exlux99

strategy(title = "Pivot Reversal Upgraded long only", overlay = true, pyramiding=1, initial_capital = 100000, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.1)
/////////////
// time

fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2010, title = "From Year", minval = 1970)

// To Date Inputs
toDay = input(defval = 31, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 12, title = "To Month", minval = 1, maxval = 12)
toYear = input(defval = 2031, title = "To Year", minval = 1970)

startDate = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finishDate = timestamp(toYear, toMonth, toDay, 00, 00)
time_cond = true

length = input(title="Length MA", type=input.integer, defval=20)
offset = 0

// Calculate pivot points
pivotHigh = ta.highest(high, 3) - ta.highest(low, 16)
pivotLow = ta.lowest(low, 3) - ta.lowest(high, 16)

// Determine if the upper pivot point has been formed
upperPivotFormed = close >= pivotHigh

// Determine if the closing price is above the 20-day LSMA
lsma = ta.sma(close, length)
buyCond = upperPivotFormed and close > lsma

// Enter long position
if (buyCond)
    strategy.entry("Long", strategy.long)

// Exit long position
strategy.close("Long", when = ta.crossover(close, lsma))

// Risk management
risk = input(title="Risk", type=input.percent, defval=100)
leverage = input(title="Leverage", type=input.bool, defval=true)

// Set stop loss
stopLossLevel = close * (1 - (risk / 100))
strategy.exit("Stop Loss", from_entry="Long", stop=stopLossLevel)

// Debugging
label.new(x=bar_index, y=high, text=str.tostring(buyCond, format.milliseconds), color=color.green, textcolor=color.white, size=size.small)
```

This script implements the strategy described in the Chinese document, using the given parameters and logic. Adjustments have been made to match the original code snippet as closely as possible.