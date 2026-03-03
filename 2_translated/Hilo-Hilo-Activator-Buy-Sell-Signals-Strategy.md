```pinescript
/*backtest
start: 2024-01-10 00:00:00
end: 2024-01-17 00:00:00
Period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Hilo Activator with Buy and Sell Signals", overlay=true)

// Custom inputs
period = input(8, title="Period")
shift = input(1, title="Shift")
exp = input(false, title="Exponential Moving Average")
max = exp ? ema(high[shift], period) : sma(high[shift], period)
min = exp ? ema(low[shift], period) : sma(low[shift], period)
pos = close > max ? -1 : close < min ? 1 : 0
pos := pos == 0 ? na(pos[1]) ? 0 : pos[1] : pos
hilo = pos == 1 ? max : min

// Conditions for buy and sell signals
buySignal = crossover(close, hilo)
sellSignal = crossunder(close, hilo)

plotshape(buySignal, style=shape.triangl
```

The code block has been preserved with the exact formatting and content as in the original document. The human-readable text describing the strategy and its advantages, risks, and optimization directions has been translated to English as requested.