```pinescript
/*backtest
start: 2024-02-25 00:00:00
end: 2024-03-17 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]
*/

//@version=5
strategy("RENTABLE Dual EMA Breakout TSLA", overlay=true)

// Inputs for EMA lengths and risk per trade
length = input(44, title="EMA Length")
longTermLength = input(200, title="Long-Term EMA Length")
riskPerTrade = input.float(1.0, title="Risk per Trade (%)", minval=0.1, maxval=10.0)

// Additional inputs for strategy customization
useFilter = input.bool(true, title="Use 200 EMA Filter")
tradeDirection = input.string("Both", title="Trade Direction", options=["Long", "Short", "Both"])

// EMAs based on the high and low prices and long-term EMA
emaHigh = ta.ema(high, length)
emaLow = ta.ema(low, length)
ema200 = ta.ema(close, longTermLength)

// Plotting EMAs on the chart
plot(emaHigh, color=color.green, title="High EMA")
plot(emaLow, color=color.red, title="Low EMA")
plot(ema200, color=color.blue, title="200 EMA")

// Entry conditions with optional EMA filter
longCondition = close > emaHigh and (useFilter ? close > ema200 : true)
shortCondition = close < emaLow and (useFilter ? close < ema200 : true)

// Calculating stop-loss and position size
longStop = emaLow
shortStop = emaHigh
riskPerShareLong = close - longStop
riskPerShareShort = shortStop - close
equity = strategy.equity

// Ensure risk per share is positive for calculations
riskPerShareLong := riskPerShareLong > 0 ? riskPerShareLong : 0.01
riskPerShareShort := riskPerShareShort > 0 ? riskPerShareShort : 0.01

positionSizeLong = (equity * riskPerTrade / 100) / riskPerShareLong
positionSizeShort = (equity * riskPerTrade / 100) / riskPerShareShort

// Ensure position sizes are positive before entering trades
if (longCondition and (tradeDirection == "Long" or tradeDirection == "Both") and positionSizeLong > 0)
    strategy.entry("Long Entry", strategy.long, size=positionSizeLong)

if (shortCondition and (tradeDirection == "Short" or tradeDirection == "Both") and positionSizeShort > 0)
    strategy.entry("Short Entry", strategy.short, size=positionSizeShort)

// Trailing stop-loss
trailPercent = input.float(2.5, title="Trailing Stop Percentage (%)")
longStopLoss = max(longStop, (1 - trailPercent / 100) * close)
shortStopLoss = min(shortStop, (1 + trailPercent / 100) * close)

strategy.exit("Long Exit", "Long Entry", stop=longStopLoss)
strategy.exit("Short Exit", "Short Entry", stop=shortStopLoss)
```

This code snippet translates the given Pine Script for the dynamic dual EMA trend following strategy, ensuring all numbers and formatting remain unchanged.