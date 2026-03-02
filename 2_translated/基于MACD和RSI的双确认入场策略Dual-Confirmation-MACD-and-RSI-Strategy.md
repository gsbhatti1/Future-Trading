```pinescript
/*backtest
start: 2024-02-01 00:00:00
end: 2024-02-17 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Dual-Confirmation-MACD-and-RSI-Strategy", overlay=true)

// MACD (Moving Average Convergence Divergence)
[macdLine, signalLine, _] = ta.macd(close, 12, 26, 9)

// RSI (Relative Strength Index)
rsiValue = ta.rsi(close, 14)

// Volume
volumeAverage = ta.sma(volume, 20)

// RSI and MACD Filters
rsiOverbought = rsiValue > 70
rsiOversold = rsiValue < 30
macdBuySignal = ta.crossover(macdLine, signalLine) and not rsiOverbought
macdSellSignal = ta.crossunder(macdLine, signalLine) and not rsiOversold

// Buy-Sell Strategy
shouldBuy = ta.crossover(close, open) and not ta.crossover(close[1], open[1]) and macdBuySignal and volume > volumeAverage
shouldSell = ta.crossunder(close, open) and not ta.crossunder(close[1], open[1]) and macdSellSignal and volume > volumeAverage

strategy.entry("Buy", strategy.long, when=shouldBuy)
strategy.entry("Sell", strategy.short, when=shouldSell)

// Wait for the next bar to confirm
strategy.close("Buy", when=ta.crossover(close, open))
strategy.close("Sell", when=ta.crossunder(close, open))

// Disable the plot
plot(na)

// Buy-Sell Labels
plotshape(series=shouldBuy, title="Buy Signal", color=color.green, style=shape.triangleup, location=location.belowbar, size=size.small, text="Buy")
plotshape(series=shouldSell, title="Sell Signal", color=color.red, style=shape.triangledown, location=location.abovebar, size=size.small, text="Sell")

// Calculate the price of the next bar
nextBarClose = close[1]
plot(nextBarClose, color=color.blue, linewidth=2, title="Estimated Close Price")
```

> Detail

https://www.fmz.com/strategy/442019

> Last Modified

2024-02-18 16:24:06