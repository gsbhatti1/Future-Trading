``` pinescript
/*backtest
start: 2024-05-01 00:00:00
end: 2024-05-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Advanced MACD Strategy with Limited Martingale", overlay=true, initial_capital=500)

// MACD settings
fastLength = 12
slowLength = 26
signalSmoothing = 9
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// Contract size and previous trade result recording
var float contractSize = 0.02 // Initial contract size is 0.02
var int martingaleCount = 0 // Martingale count
var float lastTradeResult = 0

// Buy and sell conditions
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// Long trade entry
if (longCondition)
    strategy.entry("Long", strategy.long, qty=contractSize)
    martingaleCount := 0
    lastTradeResult := strategy.netprofit

// Short trade entry
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=contractSize)
    martingaleCount := 0
    lastTradeResult := strategy.netprofit

// Take-profit and stop-loss conditions
```

(Note: The original code snippet was cut off. Here are the initial parts of the script, including contract size setup and trade entry conditions.)