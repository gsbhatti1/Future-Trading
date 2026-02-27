``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-09-24 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA and MACD Strategy for 5-Min Chart", overlay=true)

// Inputs for EMAs
fastLength = input.int(9, title="Fast EMA Length")
slowLength = input.int(21, title="Slow EMA Length")

// Inputs for MACD
macdShortLength = input.int(12, title="MACD Short Length")
macdLongLength = input.int(26, title="MACD Long Length")
macdSignalLength = input.int(9, title="MACD Signal Length")

// Inputs for ATR
atrLength = input.int(14, title="ATR Length")
atrMultiplier = input.float(1.5, title="ATR Multiplier")

// Calculate EMAs
fastEMA = ta.ema(close, fastLength)
slowEMA = ta.ema(close, slowLength)

// Calculate MACD
[macd, macdsignal, _] = ta.macd(close, macdShortLength, macdLongLength, macdSignalLength)

// Define entry and exit conditions
bullishCrossCondition = ta.crossover(fastEMA, slowEMA)
bearishCrossCondition = ta.crossunder(fastEMA, slowEMA)

buyCondition = bullishCrossCondition and ta.gt(macd, 0) and ta.gt(macdsignal, 0)
sellCondition = bearishCrossCondition or (not ta.gt(macd, macdsignal))

// Set up stop-loss and take-profit levels using ATR
stopLoss = atr(atrLength) * atrMultiplier
takeProfit = atr(atrLength) * 2

// Execute trades based on conditions
if (buyCondition)
    strategy.entry("Buy", strategy.long)

if (sellCondition)
    strategy.exit("Sell", "Buy", stop=stopLoss, limit=takeProfit)

// Plot EMAs and MACD lines
plot(fastEMA, title="Fast EMA", color=color.blue)
plot(slowEMA, title="Slow EMA", color=color.red)
hline(0, "Zero Line")
```

This Pine Script code defines the strategy for trading on 5-minute charts using EMA and MACD indicators. It includes input parameters for EMAs and MACD, calculates these indicators, sets up trade entry conditions based on crossovers of EMAs and positive MACD values, and uses ATR to determine stop-loss and take-profit levels.