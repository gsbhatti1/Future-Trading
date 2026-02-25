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

// MACD 设置更改
fastLength = 12
slowLength = 26
signalSmoothing = 9
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// 合约数量及上次交易结果记录
var float contractSize = 0.02 // 初始合约数量为0.02
var int martingaleCount = 0 // 马丁格尔计数器
var float lastTradeResult = 0

// 多头和空头条件
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// 多头信号
if (longCondition)
    strategy.entry("Long", strategy.long, qty=contractSize)
    lastTradeResult := strategy.netprofit

// 空头信号
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=contractSize)
    lastTradeResult := strategy.netprofit

// 设置止盈和止损条件
takeProfitLevel = 0.015 // 多头平仓价差为1.5%
stopLossLong = -0.01 // 多头止损价差为-1%
stopLossShort = 0.01 // 空头止损价差为1%

// 止盈和止损执行
if (strategy.position_size > 0) 
    strategy.exit("Take Profit Long", from_entry="Long", limit=close * (1 + takeProfitLevel))
    if (martingaleCount < 3)
        martingaleCount := martingaleCount + 1
        contractSize := contractSize * 2
else if (strategy.position_size < 0) 
    strategy.exit("Take Profit Short", from_entry="Short", limit=close * (1 - takeProfitLevel))
    if (martingaleCount > 0)
        martingaleCount := 0
        contractSize := 0.02

// 止损执行
if (strategy.position_size > 0) 
    strategy.exit("Stop Loss Long", from_entry="Long", stop=close * (1 + stopLossLong))
else if (strategy.position_size < 0)
    strategy.exit("Stop Loss Short", from_entry="Short", stop=close * (1 - stopLossShort))

```

This Pine Script code implements the advanced MACD strategy with limited Martingale as described. It includes setting up the MACD indicator, defining entry conditions based on crossover and crossunder of fast and slow lines, and managing position sizes through a limited number of Martingale doublings. Additionally, it incorporates take-profit and stop-loss levels to control risks effectively.