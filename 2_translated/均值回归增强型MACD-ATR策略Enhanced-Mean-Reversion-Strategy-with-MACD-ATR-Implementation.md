``` pinescript
/*backtest
start: 2024-11-12 00:00:00
end: 2024-12-11 08:00:00
period: 3h
basePeriod: 3h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Enhanced Mean Reversion with MACD and ATR", overlay=true)

// Bollinger Bands Settings
bbLength = input(20, title="Bollinger Bands Length")
bbMult = input(2, title="Bollinger Bands Multiplier")
basis = ta.sma(close, bbLength)
dev = ta.stdev(close, bbLength)
upperBand = basis + bbMult * dev
lowerBand = basis - bbMult * dev

// MACD Indicator
macdShort = input(12, title="MACD Short Length")
macdLong = input(26, title="MACD Long Length")
macdSignal = input(9, title="MACD Signal Length")
[macdLine, signalLine, _] = ta.macd(close, macdShort, macdLong, macdSignal)

// ATR for Dynamic Stop Loss and Take Profit
atrLength = input(14, title="ATR Length")
atrMultiplier = input(1.5, title="ATR Multiplier")
atrValue = ta.atr(atrLength)

// Long Entry Conditions
longCondition = ta.crossover(close, lowerBand) and macdLine > signalLine
if (longCondition)
    strategy.entry("Long", strategy.long)

// Short Entry Conditions
shortCondition = ta.crossunder(close, upperBand) and macdLine < signalLine
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Dynamic Stop Loss and Take Profit based on ATR
longSL = strategy.position_avg_price - atrValue * atrMultiplier
longTP = strategy.position_avg_price + atrValue * atrMultiplier * 2
shortSL = strategy.position_avg_price + atrValue * atrMultiplier
shortTP = strategy.position_avg_price - atrValue * atrMultiplier * 2

// Adding Stop Loss and Take Profit
if (strategy.position_size > 0)
    strategy.exit("Take Profit/Stop Loss", "Long", stop=longSL, limit=longTP)

if (strategy.position_size < 0)
    strategy.exit("Take Profit/Stop Loss", "Short", stop=shortSL, limit=shortTP)

// Visualization of Bollinger Bands and MACD
plot(upperBand, color=color.red, title="Upper Bollinger Band")
plot(lowerBand, color=color.blue, title="Lower Bollinger Band")
hline(0, "Zero Line", color=color.gray)
plot(macdLine, color=color.green, title="MACD Line")
plot(signalLine, color=color.orange, title="Signal Line")
```