``` pinescript
/*backtest
start: 2023-04-20 00:00:00
end: 2024-04-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA Crossover Strategy", overlay=true)

// EMA 23 and EMA 50 calculation
ema23 = ta.ema(close, 23)
ema50 = ta.ema(close, 50)

// Main buy rule: EMA 23 crosses above EMA 50
buySignal = ta.crossover(ema23, ema50)

// Main sell rule: EMA 23 crosses below EMA 50
sellSignal = ta.crossunder(ema23, ema50)

// Long position stop level
longStopLoss = low < ema50 and close < ema50[1]
```