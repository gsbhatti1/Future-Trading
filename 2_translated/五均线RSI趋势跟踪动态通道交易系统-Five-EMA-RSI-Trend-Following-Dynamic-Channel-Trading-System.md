```pinescript
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
plot(donchianUpper1, color=color.new(color.blue, 0), title="Donchian Upper Channel 1")
plot(donchianLower1, color=color.new(color.red, 0), title="Donchian Lower Channel 1")
plot(donchianMid1, color=color.new(color.gray, 0), title="Donchian Midline 1")
plot(donchianUpper2, color=color.new(color.blue, 0), title="Donchian Upper Channel 2")
plot(donchianLower2, color=color.new(color.red, 0), title="Donchian Lower Channel 2")
plot(donchianMid2, color=color.new(color.gray, 0), title="Donchian Midline 2")

// Trading logic
longCondition = ta.crossover(fastEma, midEma) and rsi > rsiOverbought
shortCondition = ta.crossunder(midEma, fastEma) and rsi < rsiOversold

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit logic with dynamic stop-loss and profit targets
longStopLoss = donchianLower1 - 3 * ta.stddev(close, 20)
longTakeProfit = donchianUpper1 + 3 * ta.stddev(close, 20)

shortStopLoss = donchianUpper1 + 3 * ta.stddev(close, 20)
shortTakeProfit = donchianLower1 - 3 * ta.stddev(close, 20)

if (strategy.position_size > 0)
    strategy.exit("Long Exit", "Long", stop=longStopLoss, limit=longTakeProfit)

if (strategy.position_size < 0)
    strategy.exit("Short Exit", "Short", stop=shortStopLoss, limit=shortTakeProfit)

// Plot the channels
plotshape(series=longCondition, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")

```
```