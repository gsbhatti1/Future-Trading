``` pinescript
/*backtest
start: 2024-04-01 00:00:00
end: 2024-04-30 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy('CCI Strategy with Trend Filter AUDNZD, GBPNZD', overlay=true, default_qty_type=strategy.cash, default_qty_value=50000, commission_value=0.0005, slippage=2, initial_capital=10000)

// State variables to ensure one entry per signal
var bool isLongOpen = false
var bool isShortOpen = false

// Input Parameters for allowing long and short trades
allowLong = input(true, title='Allow Long Trades')
allowShort = input(true, title='Allow Short Trades')

// Trend Filter Inputs
maType = input.string(title='MA Type', options=['OFF', 'SMA', 'EMA', 'SMMA', 'CMA', 'TMA'], defval='OFF')
trendFilterMethod = input.string(title='Trend Filter Method', options=['OFF', 'Normal', 'Reversed'], defval='OFF')
maLength = input(14, title='MA Length')

// Other Input Parameters
lengthKC = input(30, title='Keltner Channels Length')
multKC = input(0.7, title='Keltner Channels Multiplier')
lengthCCI = input(5, title='CCI Length')
overboughtCCI = input(75, title='CCI Overbought Level')
oversoldCCI = input(-75, title='CCI Oversold Level')
rsiPeriod = input(30, title='RSI Period')

// Calculate CCI and KC
kcUpperLine = ta.highest(high, lengthKC) + multKC * ta.atr(lengthKC)
kcLowerLine = ta.lowest(low, lengthKC) - multKC * ta.atr(lengthKC)
cci = ta.cci(lengthCCI)

// RSI calculation
rsi = ta.rsi(close, rsiPeriod)

// Define moving average
ma = ta.ema(close, maLength) when maType == 'EMA' else 
     ta.sma(close, maLength) when maType == 'SMA' else 
     ta.smma(close, maLength) when maType == 'SMMA' else 
     ta.cma(close, maLength) when maType == 'CMA' else 
     ta.tma(close, maLength)

// Long entry condition
longCondition = allowLong and cci < oversoldCCI and close < kcLowerLine and rsi < oversoldCCI and volume > volume[1] * 2 * multKC and not isLongOpen

// Short entry condition
shortCondition = allowShort and cci > overboughtCCI and close > kcUpperLine and rsi > overboughtCCI and volume > volume[1] * 2 * multKC and not isShortOpen

// Trend filter conditions
if (trendFilterMethod == 'Normal')
    longCondition := ma < ma[-1]
    shortCondition := ma > ma[-1]

// Execute trades
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit conditions
exitLong = cci > 0
exitShort = cci < 0

if (exitLong)
    strategy.close("Long")

if (exitShort)
    strategy.close("Short")

// Alert when opening and closing positions
alertcondition(longCondition, title='Long Entry', message='Long entry signal generated')
alertcondition(shortCondition, title='Short Entry', message='Short entry signal generated')
alertcondition(exitLong, title='Long Exit', message='Long exit signal generated')
alertcondition(exitShort, title='Short Exit', message='Short exit signal generated')
```

This script implements the described strategy with Pine Script. The input parameters allow flexibility in choosing moving average types and trend filter methods. It also includes conditions for entering and exiting trades based on CCI, RSI, and KC levels.