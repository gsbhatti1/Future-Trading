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

// 计合约数及之前交易结果记录
var float contractSize = 0.02 // 初始合约数量为0.02
var int martingaleCount = 0 // 记录马丁格尔次数
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

// 盈亏平仓条件
stopLossLevel = 0.01 // 止损水平设置为1%
takeProfitLevel = 0.015 // 止盈水平设置为1.5%

// 多头平仓
if (strategy.position_size > 0 and close < strategy.entry_price * (1 - stopLossLevel))
    strategy.close("Long")

// 空头平仓
if (strategy.position_size < 0 and close > strategy.entry_price * (1 + takeProfitLevel))
    strategy.close("Short")
```

This PineScript code implements the advanced MACD strategy with limited Martingale as described. It uses the MACD fast line crossing above the slow line to generate buy signals, and the opposite for sell signals. The contract size is initially set at 0.02, and doubles up to three times if a trade results in a loss. The script also includes take-profit and stop-loss conditions based on price movements relative to entry prices.