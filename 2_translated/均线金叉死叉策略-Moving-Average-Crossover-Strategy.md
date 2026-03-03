``` pinescript
//@version=4
strategy("Moving-Average-Crossover-Strategy", overlay=true)

// Strategy Parameters
fastLength = input(10, title="Fast Moving Average Period")
slowLength = input(30, title="Slow Moving Average Period")

// Calculate the moving averages
fastMA = sma(close, fastLength)
slowMA = sma(close, slowLength)

// Entry conditions
enterLong = crossover(fastMA, slowMA)
enterShort = crossunder(fastMA, slowMA)

// Exit conditions
exitLong = crossunder(fastMA, slowMA)
exitShort = crossover(fastMA, slowMA)

// Position management
if (enterLong)
    strategy.entry("Long", strategy.long)

if (enterShort)
    strategy.entry("Short", strategy.short)

if (exitLong)
    strategy.close("Long")

if (exitShort)
    strategy.close("Short")

// Stop loss and take profit
stopLossLevel = strategy.position_avg_price * (1 - 0.01)
takeProfitLevel = strategy.position_avg_price * (1 + 0.03)
strategy.exit("Stop Loss/Take Profit", "Long", stop=stopLossLevel, limit=takeProfitLevel)
strategy.exit("Stop Loss/Take Profit", "Short", stop=stopLossLevel, limit=takeProfitLevel)
```