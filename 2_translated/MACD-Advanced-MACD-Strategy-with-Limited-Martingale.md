> Source (PineScript)

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

// MACD 설정 변경
fastLength = 12
slowLength = 26
signalSmoothing = 9
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// 计约数及前一次交易结果记录
var float contractSize = 0.02 // 初始合同数量为0.02
var int martingaleCount = 0 // 马丁格尔次数计数器
var float lastTradeResult = 0

// 买卖条件
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// 买入信号
if (longCondition)
    strategy.entry("Long", strategy.long, qty=contractSize)
    lastTradeResult := strategy.netprofit

// 卖出信号
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=contractSize)
    lastTradeResult := strategy.netprofit

// 设置止盈和止损条件
if (strategy.position_size > 0 and close >= strategy.opentrades.entry_price(1) * 1.015) // 多头平仓条件
    strategy.close("Long")

if (strategy.position_size < 0 and close <= strategy.opentrades.entry_price(1) * 0.99) // 空头平仓条件
    strategy.close("Short")

// 设置马丁格尔机制，最多加倍三次
while (martingaleCount < 3 and lastTradeResult < 0)
    if (strategy.position_size > 0)
        contractSize := contractSize * 2 // 多头加码
    else if (strategy.position_size < 0)
        contractSize := contractSize * 2 // 空头加码
    
    martingaleCount := martingaleCount + 1

if (martingaleCount >= 3 and lastTradeResult < 0) // 如果三次加倍后仍未盈利，重置合同数量
    strategy.close_all()
    contractSize := 0.02

```

Note: The Pine Script code has been translated while maintaining the original logic and structure as closely as possible, including variable declarations and conditions.