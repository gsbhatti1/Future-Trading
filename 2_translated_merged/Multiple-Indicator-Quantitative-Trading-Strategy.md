``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='Multiple-Indicator-Quantitative-Trading-Strategy', overlay=true)

fromMonth = input.int(defval=1, title='From Month', minval=1, maxval=12)
fromDay = input.int(defval=1, title='From Day', minval=1, maxval=31)
fromYear = input.int(defval=2021, title='From Year', minval=1970)
thruMonth = input.int(defval=1, title='Thru Month', minval=1, maxval=12)
thruDay = input.int(defval=1, title='Thru Day', minval=1, maxval=31)
thruYear = input.int(defval=2112, title='Thru Year', minval=1970)

showDate = input(defval=true, title='Show Date Range')

start = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finish = timestamp(thruYear, thruMonth, thruDay, 23, 59)

window() => true

// EMA Crossover
length1 = input.int(10, title='EMA1 Length')
length2 = input.int(20, title='EMA2 Length')
ema1 = ta.ema(close, length1)
ema2 = ta.ema(close, length2)
buySignalEma = ta.crossover(ema1, ema2)
sellSignalEma = ta.crossunder(ema1, ema2)

// VWMA
VWMA_len = input.int(20, title='VWMA Length')
vWma = ta.vwma(close, VWMA_len)
buySignalVWMA = close > vWma
sellSignalVWMA = close < vWma

// SuperTrend
STR_Period = input.int(22, title='SuperTrend Period')
STR_Multiplier = input.float(5.0, title='SuperTrend Multiplier')
[upperband, lowerband] = ta.supertrend(STR_Period, STR_Multiplier)
buySignalST = close > upperband
sellSignalST = close < lowerband

// RSI
rsiPeriod = input.int(14, title='RSI Period')
overSold = input.int(56, title='Over Sold Level')
overBought = input.int(70, title='Over Bought Level')
rsi = ta.rsi(close, rsiPeriod)
buySignalRsi = rsi < overSold
sellSignalRsi = rsi > overBought

// MACD
slow_len_macd = input.int(12, title='Slow Len MACD')
fast_len_macd = input.int(26, title='Fast Len MACD')
signal_len_macd = input.int(9, title='Signal Len MACD')
[macdLine, signalLine] = ta.macd(close, fast_len_macd, slow_len_macd, signal_len_macd)
buySignalMacd = macdLine > signalLine
sellSignalMacd = macdLine < signalLine

// Combine signals with AND logic
multipleSignals = input.bool(true, title='Multiple Signals')
combinedBuySignal = buySignalEma and buySignalVWMA and buySignalST and buySignalRsi and buySignalMacd
combinedSellSignal = sellSignalEma or sellSignalVWMA or sellSignalST or sellSignalRsi or sellSignalMacd

// Stop Loss and Profit
stopLossPercent = input.float(0.5, title='Stop Loss %')
profitPercent = input.float(1.5, title='Profit %')

// Position Sizing and Reverse Limit
reverseLimit = input.int(1024, title='Reverse Limit')
avrgPos = input.bool(true, title='Averaging position?')

if combinedBuySignal
    strategy.entry("Long", strategy.long)
    strategy.exit(id="Exit Long", limit=close * (1 + profitPercent / 100), stop=close * (1 - stopLossPercent / 100))

if combinedSellSignal and strategy.opentrades > 0
    for i = 0 to strategy.opentrades - 1
        if strategy.position_size[i] > 0
            strategy.close(id="Exit Long", comment="Stop Loss or Take Profit")

```

Note: The code has been adjusted to reflect the proper use of Pine Script syntax, including the correct calculation and usage of indicators.