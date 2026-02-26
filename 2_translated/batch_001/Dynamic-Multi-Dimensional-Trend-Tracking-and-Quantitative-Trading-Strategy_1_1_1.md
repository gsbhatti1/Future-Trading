``` pinescript
/*backtest
start: 2025-03-24 00:00:00
end: 2025-03-27 00:00:00
period: 3m
basePeriod: 3m
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
*/

//@version=6
strategy("SOL Scalper - Supertrend + EMA + RSI (One Position at a Time)", overlay=true, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=10, commission_type=strategy.commission.percent, commission_value=0.075)

// Inputs
atrLength = input.int(7, title="ATR Length", minval=1)
atrMultiplier = input.float(0.8, title="ATR Multiplier", minval=0.1)
emaLength = input.int(9, title="EMA Length", minval=1)
rsiLength = input.int(14, title="RSI Length", minval=1)
slPercent = input.float(1, title="Stop Loss (%)", minval=0.1, step=0.1) / 100
tpMultiplier = input.float(3.0, title="Take Profit Multiplier", minval=1.0)

// Supertrend Calculation
atr = ta.atr(atrLength)
[supertrend, direction] = ta.supertrend(atrMultiplier, atrLength)
plot(supertrend, color=direction == 1 ? color.green : color.red, linewidth=2, title="Supertrend")

// EMA Calculation
ema = ta.ema(close, emaLength)
plot(ema, color=color.blue, title="EMA")

// RSI Calculation
rsi = ta.rsi(close, rsiLength)
rsiOverbought = 60 // Adjusted to allow more trades
rsiOversold = 40   // Adjusted to allow more trades

// Entry Conditions
longCondition = direction == 1 and close > ema and rsi > rsiOversold
shortCondition = direction == -1 and close < ema and rsi < rsiOverbought

// Risk Management
stopLoss = close * slPercent
takeProfit = atr * tpMultiplier

// Ensure Only One Position at a Time
var float positionPrice = na
if (longCondition)
    strategy.entry("Long", strategy.long, when=longCondition)
    positionPrice := close
else if (shortCondition)
    strategy.entry("Short", strategy.short, when=shortCondition)
    positionPrice := -close

// Exit Conditions
if (strategy.position_size > 0 and close < stopLoss or close > takeProfit * positionPrice)
    strategy.close("Long")

if (strategy.position_size < 0 and close > stopLoss or close < takeProfit * positionPrice.abs())
    strategy.close("Short")
```

This Pine Script code is designed to implement the dynamic multi-dimensional trend tracking and quantitative trading strategy described earlier. It uses Supertrend, EMA, and RSI indicators for generating trading signals and managing risks. The script ensures only one position at a time and includes stop-loss and take-profit mechanisms based on ATR values.