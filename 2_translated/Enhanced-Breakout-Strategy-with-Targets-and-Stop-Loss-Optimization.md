```

```pinescript
//@version=5
strategy("Enhanced Breakout Strategy with Targets and Stop Loss Optimization", overlay=true, margin_long=100, margin_short=100)

// User-defined parameters
initialCandles = input.int(3, title="Initial Candles for Breakout")
entryLevelPercent = input.float(2.5, title="Entry Level Percent")
takeProfitPercent = input.float(5, title="Take Profit Percent")
stopLossPercent = input.float(1, title="Stop Loss Percent")

// Calculate initial highest and lowest prices
highArray = array.new_float(initialCandles)
lowArray = array.new_float(initialCandles)

for i = 0 to initialCandles - 1
    array.push(highArray, high[i])
    array.push(lowArray, low[i])

initialHigh = na ? na : max(array.slice(highArray, 0, initialCandles))
initialLow = na ? na : min(array.slice(lowArray, 0, initialCandles))

// Determine breakout level
breakoutLevel = ta.crossover(close, initialHigh) or ta.crossunder(close, initialLow)

// Entry and exit logic
if (breakoutLevel)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long", profit_target=takeProfitPercent, stop_loss=stopLossPercent)

plot(initialHigh, color=color.blue, title="Initial High")
plot(initialLow, color=color.red, title="Initial Low")

```

```pinescript
// endof backtest
```