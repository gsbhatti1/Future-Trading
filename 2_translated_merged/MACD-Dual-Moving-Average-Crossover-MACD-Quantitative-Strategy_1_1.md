``` pinescript
/*backtest
start: 2024-02-14 00:00:00
end: 2024-02-21 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Hurmun

//@version=4
strategy("Simple MACD strategy", overlay=true, margin_long=100, margin_short=100)

fast_length = input(title="Fast Length", type=input.integer, defval=12)
slow_length = input(title="Slow Length", type=input.integer, defval=26)
src = input(title="Source", type=input.source, defval=close)
signal_length = input(title="Signal Smoothing", type=input.integer, minval=1, maxval=50, defval=9)
sma_source = input(title="Simple MA (Oscillator)", type=input.bool, defval=false)
sma_signal = input(title="Simple MA (Signal Line)", type=input.bool, defval=false)
movinga2_length = input(title="Movinga 2", type=input.integer, defval=200)
take_profit_short = input(title="% Short Take Profit", type=input.float, minval=1, maxval=10, defval=2)
take_profit_long = input(title="% Long Take Profit", type=input.float, minval=1, maxval=10, defval=2)
stop_loss_percent = input(title="Stoploss in %", type=input.float, minval=1, maxval=10, defval=2)

// Calculate MACD
macd_line = ema(src, fast_length) - ema(src, slow_length)
signal_line = sma(macd_line, signal_length)
histogram = macd_line - signal_line

// Determine entry signals
long_entry = crossover(macd_line, signal_line) and close > src(movinga2_length)
short_entry = crossunder(macd_line, signal_line) and close < src(movinga2_length)

// Plot MACD and Signal Line
plot(macd_line, title="MACD", color=color.blue)
plot(signal_line, title="Signal Line", color=color.red)
hline(0, "Zero Line", color=color.gray)

// Enter trades based on entry signals
if (long_entry)
    strategy.entry("Long", strategy.long)
    strategy.exit("Take Profit Long", "Long", profit_percent=take_profit_long)
    strategy.exit("Stop Loss Long", "Long", stop_percent=stop_loss_percent)

if (short_entry)
    strategy.entry("Short", strategy.short)
    strategy.exit("Take Profit Short", "Short", profit_percent=take_profit_short)
    strategy.exit("Stop Loss Short", "Short", stop_percent=stop_loss_percent)

// Optional trailing stoploss
trailing_stop = input(title="Trailing Stop (Percent)", type=input.float, minval=1, maxval=20, defval=5)
trail_price = na
if (strategy.position_size > 0 and not na(trail_price))
    trail_price := strategy.position_avg_price * (1 + trailing_stop / 100)
else if (strategy.position_size < 0 and not na(trail_price))
    trail_price := strategy.position_avg_price * (1 - trailing_stop / 100)

if (strategy.position_size > 0 and close < trail_price)
    strategy.exit("Trailing Stop Loss", "Long", stop=trail_price)
else if (strategy.position_size < 0 and close > trail_price)
    strategy.exit("Trailing Stop Loss", "Short", stop=trail_price)
```

This code defines a simple MACD strategy that uses dual moving average crossovers with price filtering to generate trading signals. It includes the necessary inputs, calculations for MACD and signal lines, and logic for entering long and short positions based on these signals. Additionally, it incorporates trailing stop loss mechanisms to manage risk effectively.