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

// Calculation of MACD
[macdLine, signalLine, _] = ta.macd(src, macdLength, 26, signalSmoothing)
macdHist = macdLine - signalLine

// RSI Parameters
rsiLength = input.int(14, title="RSI Length")
overboughtLevel = 70
oversoldLevel = 30

// Calculation of RSI
rsiValue = ta.rsi(src, rsiLength)

// SMA Parameters
smaShortLength = 50
smaLongLength = 200

// Calculation of SMAs
smaShort = ta.sma(close, smaShortLength)
smaLong = ta.sma(close, smaLongLength)

// Long Entry Condition
longEntryCond = ta.crossover(macdLine, signalLine) and rsiValue < overboughtLevel and smaShort > smaLong

// Long Exit Condition
longExitCond = ta.crossunder(macdLine, signalLine) or rsiValue >= overboughtLevel

// Short Entry Condition
shortEntryCond = ta.crossunder(macdLine, signalLine) and rsiValue > oversoldLevel and smaShort < smaLong

// Short Exit Condition
shortExitCond = ta.crossover(macdLine, signalLine) or rsiValue <= oversoldLevel

// Place orders based on conditions
if (longEntryCond)
    strategy.entry("Long", strategy.long)

if (longExitCond)
    strategy.close("Long")

if (shortEntryCond)
    strategy.entry("Short", strategy.short)

if (shortExitCond)
    strategy.close("Short")
```

This Pine Script code defines the trading strategy as described, using MACD, RSI, and SMA to generate buy and sell signals. The script sets up conditions for entering and exiting trades based on these indicators and their respective levels.