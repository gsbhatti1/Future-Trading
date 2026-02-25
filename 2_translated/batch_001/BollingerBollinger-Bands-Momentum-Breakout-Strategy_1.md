```pinescript
/*backtest
start: 2023-11-18 00:00:00
end: 2023-12-18 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy(title="Bollinger Bands Momentum Breakout Strategy", shorttitle="BB-Momentum-BS", overlay=true)

// Input Parameters
length = input(20, title="Period")
stdDev = input(1.5, title="Standard Deviation")

// Calculate Bollinger Bands
middle = sma(close, length)
upper = middle + stdDev * atr(length)
lower = middle - stdDev * atr(length)

// Buy Condition: Price Breaks Above Upper Band
buySignal = ta.crossover(close, upper)
if (buySignal)
    strategy.entry("Buy", strategy.long)

// Sell Condition: Price Breaks Below Lower Band
sellSignal = ta.crossunder(close, lower)
if (sellSignal)
    strategy.exit("Sell", "Buy")

// Plot Bollinger Bands on the chart
plot(middle, color=color.gray, title="Middle Band")
plot(upper, color=color.blue, title="Upper Band")
plot(lower, color=color.red, title="Lower Band")
```

The provided Pine Script code is now included in the document. Note that the `strategy` name and some descriptive text have been adjusted to match the strategy being described while ensuring all original content remains intact.