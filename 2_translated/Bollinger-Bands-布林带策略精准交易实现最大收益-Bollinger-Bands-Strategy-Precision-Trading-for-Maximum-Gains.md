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
dev = mult * ta.stdev(src, length)
upperband = basis + dev
lowerband = basis - dev

// Buy and Sell Conditions
longCondition = ta.crossunder(src, lowerband)
shortCondition = ta.crossover(src, upperband)

// Long Strategy
when longCondition
    strategy.entry("Long", strategy.long)

// Short Strategy
when shortCondition
    strategy.entry("Short", strategy.short)

// Exit Strategies
exitLongCondition = ta.crossunder(src, basis)
exitShortCondition = ta.crossover(src, basis)

// Exit Long Position
when exitLongCondition
    strategy.close("Long")

// Exit Short Position
when exitShortCondition
    strategy.close("Short")
```

The provided Pine Script code defines a Bollinger Bands strategy with long and short positions. It calculates the Bollinger Bands using the specified length and multiplier, then uses the bands to generate buy and sell signals based on price crossing conditions.