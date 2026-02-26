``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-04 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA RSI Donchian Strategy", overlay=true)

// Input parameters
fastEmaLength = input(9, title="Fast EMA Length")
midEmaLength = input(21, title="Mid EMA Length")
slowEmaLength = input(55, title="Slow EMA Length")
ema89Length = input(89, title="89 EMA Length")
ema144Length = input(144, title="144 EMA Length")
rsiPeriod = input(14, title="RSI Period")
rsiOverbought = input(60, title="RSI Overbought Level")
rsiOversold = input(40, title="RSI Oversold Level")
donchianLength1 = input(21, title="Donchian Channel Length 1")
donchianLength2 = input(74, title="Donchian Channel Length 2")

// EMA calculations
fastEma = ta.ema(close, fastEmaLength)
midEma = ta.ema(close, midEmaLength)
slowEma = ta.ema(close, slowEmaLength)
ema89 = ta.ema(close, ema89Length)
ema144 = ta.ema(close, ema144Length)

// RSI calculation
rsi = ta.rsi(close, rsiPeriod)

// Donchian Channel calculations
donchianUpper1 = ta.highest(high, donchianLength1)
donchianLower1 = ta.lowest(low, donchianLength1)
donchianUpper2 = ta.highest(high, donchianLength2)
donchianLower2 = ta.lowest(low, donchianLength2)
donchianMid1 = (donchianUpper1 + donchianLower1) / 2
donchianMid2 = (donchianUpper2 + donchianLower2) / 2

// Plot EMAs
plot(fastEma, color=color.green, linewidth=2, title="Fast EMA")
plot(midEma, color=color.blue, linewidth=2, title="Mid EMA")
plot(slowEma, color=color.orange, linewidth=2, title="Slow EMA")
plot(ema89, color=color.red, linewidth=2, title="89 EMA")
plot(ema144, color=color.purple, linewidth=2, title="144 EMA")

// Plot Donchian Channels
plot(donchianUpper1, color=color.new(color.blue, 0), title="Donchian Channel Upper 1")
plot(donchianLower1, color=color.new(color.red, 0), title="Donchian Channel Lower 1")
plot(donchianUpper2, color=color.new(color.blue, 0), title="Donchian Channel Upper 2")
plot(donchianLower2, color=color.new(color.red, 0), title="Donchian Channel Lower 2")

// Plot RSI
hline(rsiOverbought, "RSI Overbought", color=color.new(color.orange, 90))
hline(rsiOversold, "RSI Oversold", color=color.new(color.green, 90))

// Strategy Logic
longCondition = ta.crossover(fastEma, midEma) and rsi > rsiOverbought and high >= donchianUpper1 and close < donchianMid1
shortCondition = ta.crossunder(midEma, fastEma) and rsi < rsiOversold and low <= donchianLower1 and close > donchianMid2

// Open long position
if (longCondition)
    strategy.entry("Long", strategy.long)

// Close long position
if (close >= donchianUpper1 or ta.rsi(close, 14) < rsiOversold or low <= donchianLower1)
    strategy.close("Long")

// Open short position
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Close short position
if (close <= donchianLower1 or ta.rsi(close, 14) > rsiOverbought or high >= donchianUpper2)
    strategy.close("Short")
```

This Pine Script code implements the described trading system using multiple EMA and RSI indicators along with Donchian Channels. It includes conditions for entering long and short positions based on the crossovers of EMAs, RSI levels, and Donchian Channel boundaries.