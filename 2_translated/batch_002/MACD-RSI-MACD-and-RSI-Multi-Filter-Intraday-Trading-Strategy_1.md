``` pinescript
/*backtest
start: 2024-05-07 00:00:00
end: 2024-06-06 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Day Trading Strategy", overlay=true)

// MACD Parameters
macdLength = input.int(12, title="MACD Length")
signalSmoothing = input.int(9, title="MACD Signal Smoothing")
src = input(close, title="Source")

// Calculate MACD
[macdLine, signalLine, _] = ta.macd(src, macdLength, 26, signalSmoothing)
macdHist = macdLine - signalLine

// RSI Parameters
rsiLength = input.int(14, title="RSI Length")
overboughtLevel = input.int(70, title="Overbought Level")
oversoldLevel = input.int(30, title="Oversold Level")

// Calculate RSI
rsiValue = ta.rsi(src, rsiLength)

// SMA Parameters
smaShortLength = input.int(50, title="SMA Short Length")
smaLongLength = input.int(200, title="SMA Long Length")

// Calculate SMAs
smaShort = ta.sma(close, smaShortLength)
smaLong = ta.sma(close, smaLongLength)

// Entry and Exit Conditions

// Long Entry Condition
longCondition = ta.crossover(macdLine, signalLine) and rsiValue < overboughtLevel and smaShort > smaLong
strategy.entry("Buy", when=longCondition)

// Long Exit Condition
shortCondition1 = ta.crossunder(macdLine, signalLine)
shortCondition2 = rsiValue >= overboughtLevel
exitCondition = shortCondition1 or shortCondition2
strategy.close("Buy", when=exitCondition)

// Short Entry Condition
shortCondition = ta.crossover(signalLine, macdLine) and rsiValue > oversoldLevel and smaShort < smaLong
strategy.entry("Sell", when=shortCondition)

// Short Exit Condition
longExitCondition1 = ta.crossunder(macdLine, signalLine)
longExitCondition2 = rsiValue <= oversoldLevel
exitShortCondition = longExitCondition1 or longExitCondition2
strategy.close("Sell", when=exitShortCondition)
```

This Pine Script implements the described strategy using the MACD, RSI, and SMA indicators to generate buy and sell signals. It includes detailed input parameters for each indicator and clear conditions for entering and exiting trades based on the specified criteria.