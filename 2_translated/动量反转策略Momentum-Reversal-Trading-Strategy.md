``` pinescript
/*backtest
start: 2023-09-06 00:00:00
end: 2023-10-06 00:00:00
period: 5m
*/

//@version=5
indicator("Momentum-Reversal-Trading-Strategy", overlay=false)

// Inputs
startDate = input.time(timestamp("2021-01-01 00:00:00"), title="Start date")
endDate = input.time(timestamp("2050-01-01 00:00:00"), title="End date")
allowLong = input.bool(true, title="Allow long positions")
allowShort = input.bool(true, title="Allow short positions")
keepRiskAboveSetPoint = input.bool(false, title="Keep risk at or above the set point")
stopLossMultiple = input.float(1.5, title="Stop loss multiple")
profitTargetMultiple = input.float(3, title="Profit target multiple")
useMoneyManagement = input.bool(false, title="Use money management")
percentRiskPerTrade = input.float(2, title="Percent risk per trade")

// RSI, Stoch and MACD
rsiValue = ta.rsi(close, 7)
stochValue = ta.stoch(close, high, low, 14, 3, 3)
macdLine, signalLine, _ = ta.macd(close, 12, 26, 9)
bullishCond = rsiValue > 50 and stochValue.k > 50 and macdLine > signalLine
bearishCond = rsiValue < 50 and stochValue.k < 50 and macdLine < signalLine

// Bar color
barColor = na
if bullishCond
    barColor := color.green
else if bearishCond
    barColor := color.red
else
    barColor := color.black

plotshape(series=barColor == color.green, title="Bullish Bar", location=location.belowbar, color=color.green, style=shape.labelup, text="Bullish", show_last=1)
plotshape(series=barColor == color.red, title="Bearish Bar", location=location.abovebar, color=color.red, style=shape.labeldown, text="Bearish", show_last=1)

// ATR
atrValue = ta.atr(7)

// Trading logic
longCondition = barColor == color.green and barColor[1] != color.green and allowLong
shortCondition = barColor == color.red and barColor[1] != color.red and allowShort

if longCondition
    strategy.entry("Long", strategy.long, when=longCondition, comment="Long entry")
    strategy.exit("Profit Target", from_entry="Long", limit=strategy.position_avg_price + atrValue * profitTargetMultiple, stop=strategy.position_avg_price - atrValue * stopLossMultiple)
    
if shortCondition
    strategy.entry("Short", strategy.short, when=shortCondition, comment="Short entry")
    strategy.exit("Stop Loss", from_entry="Short", stop=strategy.position_avg_price + atrValue * stopLossMultiple, limit=strategy.position_avg_price - atrValue * profitTargetMultiple)

// Money management
if useMoneyManagement
    r = percentRiskPerTrade / 100
    tradeSize = strategy.equity * r
    strategy.exit("Take Profit", from_entry="Long", limit=tradeSize + atrValue * profitTargetMultiple)
    strategy.exit("Stop Loss", from_entry="Long", stop=tradeSize - atrValue * stopLossMultiple)
    strategy.exit("Take Profit", from_entry="Short", limit=tradeSize - atrValue * profitTargetMultiple)
    strategy.exit("Stop Loss", from_entry="Short", stop=tradeSize + atrValue * stopLossMultiple)
```

This PineScript implements the described momentum-reversal trading strategy, including the use of RSI, Stoch, and MACD to determine trend direction, and ATR for stop loss and take profit levels. The strategy also includes logic for setting long and short positions, as well as money management rules.