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
movinga_2 = input(200, title="movinga 2")
short_take_profit_percent = input(2, title="Short Take Profit (%)", minval=1)
long_take_profit_percent = input(2, title="Long Take Profit (%)", minval=1)
stoploss_percent = input(2, title="Stoploss in %", minval=1)

// Calculate MACD
fast_ma = sma(src, fast_length)
slow_ma = sma(src, slow_length)
macd_line = fast_ma - slow_ma

// Calculate Signal Line
signal_line = sma(macd_line, signal_length)

// Calculate Histogram
histogram = macd_line - signal_line

// Generate Long and Short Signals
long_condition = crossover(macd_line, signal_line) and close > sma(close, movinga_2)
short_condition = crossunder(macd_line, signal_line) and close < sma(close, movinga_2)

// Place Orders
if (long_condition)
    strategy.entry("Long", strategy.long)
    
if (short_condition)
    strategy.entry("Short", strategy.short)

// Trailing Stop Loss
trail_stoploss = input(2, title="Trailing Stop Loss (%)", minval=1)
strategy.exit("Exit Long", "Long", stop=stop_price(close - trail_stoploss/100 * close))
strategy.exit("Exit Short", "Short", stop=stop_price(close + trail_stoploss/100 * close))

// Plot Indicators
plot(macd_line, color=color.blue, title="MACD Line")
plot(signal_line, color=color.red, title="Signal Line")
hline(0, "Zero Line")
fill(hline(0), macd_line > 0 ? macd_line : na, color=color.green, transp=90)
fill(hline(0), macd_line < 0 ? macd_line : na, color=color.red, transp=90)

// Strategy Logic
long_condition = crossover(macd_line, signal_line) and close > sma(close, movinga_2)
short_condition = crossunder(macd_line, signal_line) and close < sma(close, movinga_2)

// Take Profit Conditions
take_profit_long = input(2, title="Take Profit (%)", minval=1)
take_profit_short = input(2, title="Take Profit (%)", minval=1)
strategy.exit("Exit Long", "Long", limit=limit_price(close + take_profit_long/100 * close))
strategy.exit("Exit Short", "Short", limit=limit_price(close - take_profit_short/100 * close))

// Plot Take Profit and Stop Loss Levels
plot(take_profit_long/100 * close, color=color.green, title="Long Take Profit Level")
plot(take_profit_short/100 * close, color=color.red, title="Short Take Profit Level")

plot(stoploss_percent/100 * close, color=color.orange, title="Stop Loss Level")

// Strategy Summary
strategy.summary()
```

This script captures the essence of the described strategy while ensuring that all code blocks and formatting remain unchanged.