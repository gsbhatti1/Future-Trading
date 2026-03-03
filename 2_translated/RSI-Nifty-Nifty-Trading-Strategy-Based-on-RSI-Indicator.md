``` pinescript
/*backtest
start: 2023-01-18 00:00:00
end: 2024-01-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RSI Strategy", overlay=true, pyramiding = 1000)
rsi_period = 2
rsi_lower = 20
rsi_upper = 70

rsi_value = rsi(close, rsi_period)
buy_signal = crossover(rsi_value, rsi_lower)
sell_signal = crossunder(rsi_value, rsi_upper)
current_date1 = input(defval=timestamp("01 Nov 2009 00:00 +0000"), title="stary Time", group="Time Settings")

current_date = input(defval=timestamp("01 Nov 2023 00:00 +0000"), title="End Time", group="Time Settings")
investment_amount = 100000.0
start_time = input(defval=timestamp("01 Dec 2018 00:00 +0000"), title="Start Time", group="Time Settings") 
end_time = input(defval=timestamp("30 Nov 2023 00:00 +0000"), title="End Time", group="Time Settings")

in_time = time >= start_time and time <= end_time
// Variable to track accumulation.
var accumulation = 0.0
out_time = time >= end_time 

if (buy_signal)
    strategy.entry("long", strategy.long, qty=1) 
    accumulation += 1
if (out_time)
    strategy.close(id="long")

plotshape(series=buy_signal, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup)
plotshape(series=sell_signal, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown)

plot(rsi_value, title="RSI", color=color.blue)
hline(rsi_lower, title="Lower Level", color=color.red)

plot(strategy.opentrades, style=plot.style_columns, 
     color=#2300a1, title="Profit first entry")
plot(strategy.openprofit, style=plot.style_line, 
     color=#147a00, title="Profit first entry")
// plot(strategy.position_avg_price, style=plot.style_columns,
```