``` pinescript
/*backtest
start: 2024-04-01 00:00:00
end: 2024-04-30 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Bollinger Bands Strategy with Long and Short", overlay=true)

// Bollinger Bands settings
length = input.int(20, title="BB Length")
src = input(close, title="Source")
mult = input.float(2.0, title="BB Multiplier")

// Calculate Bollinger Bands
basis = ta.sma(src, length)
deviation = mult * ta.stdev(src, length)
upper_band = basis + deviation
lower_band = basis - deviation

// Buy and Sell Logic
buy_signal = ta.crossunder(src, lower_band) or ta.crossunder(src, basis)
sell_signal = ta.crossover(src, upper_band) or ta.crossover(src, basis)

// Short Signals
short_signal = ta.crossunder(src, upper_band) or ta.crossunder(src, basis)

// Cover Signals
cover_signal = ta.crossabove(src, lower_band) or ta.crossabove(src, basis)

// Execute trades based on signals
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.exit("Sell", "Buy")

if (short_signal)
    strategy.entry("Short", strategy.short)

if (cover_signal)
    strategy.close("Short")

// Plotting Bollinger Bands and Signals
plot(basis, color=color.blue, title="Basis")
hline(upper_band, "Upper Band", color=color.red)
hline(lower_band, "Lower Band", color=color.green)
plotshape(series=buy_signal, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=sell_signal, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")
```

This Pine Script code implements the described Bollinger Bands strategy with long and short positions. It includes settings for calculating the Bollinger Bands, generating buy and sell signals based on price crossing the bands, and executing trades accordingly. The script also plots the Bollinger Bands and signals directly on the chart for easy visualization.