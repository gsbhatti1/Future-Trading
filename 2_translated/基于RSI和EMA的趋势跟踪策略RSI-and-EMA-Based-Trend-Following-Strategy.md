``` pinescript
/*backtest
start: 2023-10-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RSI and EMA-Based Trend Following Strategy with Risk Management", overlay=true)

// Strategy Parameters
rsiLength = input(14, "RSI Length")
rsiOverbought = input(70, "RSI Overbought Level")
rsiOversold = input(30, "RSI Oversold Level")

// RSI Calculation
rsiValue = rsi(close, rsiLength)

// EMA Parameters
ema20 = ema(close, 20)
ema50 = ema(close, 50)
ema200 = ema(close, 200)

// Trade Risk Parameter
riskPerTrade = input(0.03, "Risk per Trade (3%)")

// Stop Loss Distance in pips (adjust according to your strategy)
stopLossPips = input(1, "Stop Loss Distance in pips")

// Position Size and Stop Loss Calculation
calculatePositionSize(entryPrice, stopLossPips) =>
    stopLossPrice = entryPrice - stopLossPips * syminfo.mintick
    riskPerTradeValue = strategy.equity * riskPerTrade
    positionSize = riskPerTradeValue / (entryPrice - stopLossPrice)
    positionSize

// Entry Conditions
longCondition = (rsiValue < rsiOversold) and (close > ema20 or close > ema50 or close > ema200)
if longCondition
    strategy.entry("Long", strategy.long, qty=1)

// Exit Conditions
exitCondition = (rsiValue > 
```