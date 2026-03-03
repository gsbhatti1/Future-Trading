``` pinescript
/*backtest
start: 2024-03-26 00:00:00
end: 2024-04-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © catikur

//@version=5
strategy("Advanced MACD-V and Fibonacci Strategy with EMA Trailing TP", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=1000, margin_long=1./10*50, margin_short=1./10*50, slippage=0, commission_type=strategy.commission.percent, commission_value=0.05)

// Parameters
fast_len = input.int(12, "Fast EMA Length", minval=1)
slow_len = input.int(26, "Slow EMA Length", minval=1)
signal_smooth = input.int(9, "Signal Smoothing", minval=1)
atr_mult = input.float(3.0, "ATR Multiplier for MACD-V", minval=0.1, maxval=5.0)
fibo_levels = input.array([0.236, 0.382, 0.5, 0.618, 0.786], "Fibonacci Retracement Levels")

// MACD-V Calculation
fast_ema = ta.ema(close, fast_len)
slow_ema = ta.ema(close, slow_len)
macd_line = fast_ema - slow_ema
signal_line = ta.sma(macd_line, signal_smooth)
hist = macd_line - signal_line

atr_period = input.int(14, "ATR Period", minval=1)
atr_value = ta.atr(atr_period)

macd_v = (macd_line / atr_value) * atr_mult

// Fibonacci Levels
[fib_high_5m, fib_low_5m] = [high[9], low[9]]
[fib_high_30m, fib_low_30m] = [ta.highest(high, 9), ta.lowest(low, 9)]

fib_382 = (fib_high_30m - fib_low_30m) * 0.382 + fib_low_30m
fib_500 = (fib_high_30m - fib_low_30m) * 0.5 + fib_low_30m

// Trading Logic
if (close < fib_382 and macd_v < -50 and ta.crossover(macd_line, signal_line))
    strategy.entry("Short", strategy.short)
    
if (close > fib_382 or close > fib_500 or macd_v > 150 or ta.crossunder(macd_line, signal_line))
    strategy.close("Short")

// Trailing Stop
trailing_stop = input.float(2.0, "Trailing Stop Percentage", minval=0.01)
strategy.exit("Exit Short", "Short", stop=close - (atr_value * trailing_stop))

```

This Pine Script defines a trading strategy using MACD-V and Fibonacci retracement levels across multiple timeframes, including dynamic trailing stops to manage profits and risks. The script includes the necessary parameters for customization, such as EMA lengths, ATR multipliers, and Fibonacci levels.