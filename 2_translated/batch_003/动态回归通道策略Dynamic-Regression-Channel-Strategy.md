``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Dynamic Regression Channel Strategy", shorttitle="DRCS", overlay=true, initial_capital = 100, default_qty_value = 10, default_qty_type = strategy.percent_of_equity)

// Exponential Moving Average for defining the regression line slope
var SlopeEMASize = input.int(defval = 21, title = "Slope EMA" )
slope_ema = ta.ema(close, SlopeEMASize)

// Exponential Moving Average for defining the stop level
var StopEMASize = input.int(defval = 13, title = "Stop EMA" )
stop_ema = ta.ema(close, StopEMASize)

// Variables for position control
var float long_stop_level = na
var float long_entry_level = na
var bool long_signal = false
var bool long_order_open = false
var int long_order_id = 0

var float short_stop_level = na
var float short_entry_level = na
var bool short_signal = false
var bool short_order_open = false
var int short_order_id = 0

// Linear regression for use as an entry signal 
var SlopeLenght = input.int(defval = 21, title = "Slope Lenght" )
entry_signal = ta.linreg(slope_ema, SlopeLenght, 0)

// Variables indicating the pivot of the regression
long_entry_signal = ta.crossover(entry_signal, entry_signal[1])
short_entry_signal = ta.crossunder(entry_signal, entry_signal[1])

// Conditions for entering long position
if (long_entry_signal)
    long_stop_level := stop_ema
    long_entry_level := close
    long_signal := true
    if not long_order_open
        long_order_id := strategy.entry("Long", strategy.long)

// Conditions for exiting long position
if (close < long_stop_level and long_signal)
    strategy.exit("Long Exit", "Long")
    long_order_open := false

// Conditions for entering short position
if (short_entry_signal)
    short_stop_level := stop_ema
    short_entry_level := close
    short_signal := true
    if not short_order_open
        short_order_id := strategy.entry("Short", strategy.short)

// Conditions for exiting short position
if (close > short_stop_level and short_signal)
    strategy.exit("Short Exit", "Short")
    short_order_open := false

```