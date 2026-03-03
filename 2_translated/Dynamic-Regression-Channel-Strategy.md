``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Dynamic Regression Channel Strategy", shorttitle="DRC Strategy", overlay=true, initial_capital = 100, default_qty_value = 10, default_qty_type = strategy.percent_of_equity)

// Exponential moving average for defining the regression line
var SlopeEMASize = input.int(defval = 21, title = "Slope EMA" )
slope_ema = ta.ema(close, SlopeEMASize)

// Exponential moving average for defining the stop level
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

// Linear regression for use as entry signal 
var SlopeLenght = input.int(defval = 21, title = "Slope Lenght" )
entry_signal = ta.linreg(slope_ema, SlopeLenght, 0)

// Variables indicating the pivot of the regression
long_entry_signal = ta.crossover(entry_signal, entry_signal[1])
short_entry_signal = ta.crossunder(entry_signal, entry_signal[1])

// Conditions for opening long and short positions based on the entry signals
if (long_entry_signal)
    long_stop_level := stop_ema
    if not long_order_open
        long_order_id := strategy.order("Long", strategy.long, comment="Long Order")
        long_order_open := true

if (short_entry_signal)
    short_stop_level := stop_ema
    if not short_order_open
        short_order_id := strategy.order("Short", strategy.short, comment="Short Order")
        short_order_open := true

// Real-time tracking of price breaking through the stop loss line
long_position = strategy.position_size > 0
short_position = strategy.position_size < 0

if (long_position and ta.crossover(close, long_stop_level))
    strategy.close("Long", comment="Stop Loss Long")
    long_order_open := false

if (short_position and ta.crossunder(close, short_stop_level))
    strategy.close("Short", comment="Stop Loss Short")
    short_order_open := false
```

This Pine Script implements the dynamic regression channel strategy as described in the document. It uses exponential moving averages to define both the slope of the regression line and the stop levels. The script generates buy and sell signals based on the linear regression analysis, and updates the stop loss levels dynamically to lock in profits.