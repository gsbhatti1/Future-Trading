``` pinescript
/*backtest
start: 2025-02-13 00:00:00
end: 2025-02-20 00:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Dynamic EMA Crossover with RSI Momentum and ATR Volatility Multi-Level Confirmation Trading Strategy", overlay=true, margin_long=100, margin_short=100, pyramiding=1)

// Inputs
emaFastLength = input.int(9, "Fast EMA Length")
emaSlowLength = input.int(21, "Slow EMA Length")
rsiLength = input.int(14, "RSI Length")
rsiOverbought = input.int(70, "RSI Overbought")
rsiOversold = input.int(30, "RSI Oversold")
atrLength = input.int(14, "ATR Length")
riskPercent = input.float(1, "Risk Percentage", step=0.5)

// Calculate Indicators
emaFast = ta.ema(close, emaFastLength)
emaSlow = ta.ema(close, emaSlowLength)
rsi = ta.rsi(close, rsiLength)
atr = ta.atr(atrLength)

// Entry Conditions
longCondition = ta.crossover(emaFast, emaSlow) and rsi < rsiOverbought
shortCondition = ta.crossunder(emaFast, emaSlow) and rsi > rsiOversold

// Exit Conditions
takeProfitLevelLong = close + (atr * 3)
stopLossLevelLong = close - (atr * 1.5)
takeProfitLevelShort = close - (atr * 3)
stopLossLevelShort = close + (atr * 1.5)

// Position Sizing
positionSize = riskPercent / atr

// Order Logic
if (longCondition)
    strategy.entry("Long", strategy.long, size=positionSize)
    
if (shortCondition)
    strategy.entry("Short", strategy.short, size=positionSize)
    
// Exit Logic
if (strategy.position_size > 0 and close < stopLossLevelLong)
    strategy.exit("Take Profit Long", "Long")
    
if (strategy.position_size < 0 and close > takeProfitLevelShort)
    strategy.exit("Take Profit Short", "Short")
```

This Pine Script code implements the described trading strategy, including inputs for EMA lengths, RSI settings, ATR length, and risk percentage. It also includes logic for entering positions based on EMA crossovers and RSI conditions, as well as exit logic based on stop-loss and take-profit levels adjusted by ATR.