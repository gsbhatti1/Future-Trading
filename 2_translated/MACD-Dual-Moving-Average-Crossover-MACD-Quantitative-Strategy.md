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

fast_length = input(12, title="Fast Length")
slow_length = input(26, title="Slow Length")
src = input(close, title="Source")
signal_length = input(9, title="Signal Smoothing", minval=1, maxval=50)
sma_source = input(false, title="Simple MA (Oscillator)")
sma_signal = input(false, title="Simple MA (Signal Line)")
movinga_2 = input(200, title="Moving Average 2")
take_profit_short = input(2, title="Short Take Profit (%)", type=input.percent)
take_profit_long = input(2, title="Long Take Profit (%)", type=input.percent)
stop_loss_percent = input(2, title="Stoploss in %", type=input.percent)

// Calculate MACD
fast_ma = sma(src, fast_length)
slow_ma = sma(src, slow_length)
macd = fast_ma - slow_ma

// Signal Line and Histogram
signal_line = sma(macd, signal_length)
histogram = macd - signal_line

// 200-day MA
moving_a_2 = sma(src, movinga_2)

// Golden Cross Condition
golden_cross = crossover(macd, signal_line) and macd < 0

// Dead Cross Condition
dead_cross = crossunder(macd, signal_line) and macd > 0

// Buy Conditions
long_condition = golden_cross and src > moving_a_2

// Sell Conditions
short_condition = dead_cross and src < moving_a_2

// Place Orders
if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

// Take Profit and Stop Loss
long_tp = strategy.position_avg_price * (1 + take_profit_long / 100)
short_tp = strategy.position_avg_price * (1 - take_profit_short / 100)
stop_loss = strategy.position_avg_price * (1 - stop_loss_percent / 100)

// Trailing Stop Loss
trail_amount = input(5, title="Trailing Amount (%)", type=input.percent)
trailing_stop = strategy.position_avg_price + (strategy.position_size > 0 ? trail_amount : -trail_amount) * strategy.position_avg_price

if (long_condition)
    strategy.exit("Long TP/SL", "Long", limit=long_tp, stop=stop_loss)

if (short_condition)
    strategy.exit("Short TP/SL", "Short", limit=short_tp, stop=stop_loss)
```

This Pine Script implements the described dual-moving-average crossover MACD strategy with additional take profit and stop loss conditions.