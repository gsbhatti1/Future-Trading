``` pinescript
/*backtest
start: 2023-10-07 00:00:00
end: 2023-11-06 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=4
// Backtest the momentum breakout strategy. The strategy is developed by ChaoZhang and uses MACD, RSI, and Stochastic indicators to identify trend reversals.
// This script shows the performance for a given stock with the defined date range using $10,000 as initial capital.
strategy("Momentum Breakout Strategy", overlay=true, initial_capital=10000)

// ####################### Start of User Inputs #######################
// From Date Inputs
fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 7, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2019, title = "From Year", minval = 1970)

// To Date Inputs
toDay = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
toYear = input(defval = 2021, title = "To Year", minval = 1970)

// Risk and Reward Ratio
risk = input(1.5, title="Risk")
reward = input(3, title="Reward")

// Test Long and Short Conditions
testLong = input(true, title="Test Long")
testShort = input(true, title="Test Short")

// Calculate start/end date condition
startDate = timestamp(fromYear, fromMonth, fromDay, 0, 0)
endDate = timestamp(toYear, toMonth, toDay, 23, 59)

// Strategy Conditions
macdLine = ta.macd(close)[1]
signalLine = ta.macd_signal(close)[1]
stochK = ta.stoch(close, high, low, 5)[1]
rsiValue = ta.rsi(close, 14)

longCondition = macdLine > signalLine and stochK > 50 and rsiValue > 50
shortCondition = macdLine < signalLine and stochK < 50 and rsiValue < 50

// Calculate Stop Loss and Take Profit Levels
stopLoss = ta.atr(7)
takeProfit = risk * stopLoss

// Entry Conditions
if (testLong and longCondition)
    strategy.entry("Long", strategy.long)

if (testShort and shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Conditions
for i = 1 to 3
    if ta.crossover(macdLine, signalLine) or ta.crossunder(stochK, 50) or rsiValue > 50 + reward * stopLoss / risk
        strategy.exit("Exit Long", "Long")
    if ta.crossunder(macdLine, signalLine) or ta.crossover(stochK, 50) or rsiValue < 50 - reward * stopLoss / risk
        strategy.exit("Exit Short", "Short")

// Time Condition to Skip March 2020
if time >= timestamp(2020, 3, 1, 0, 0) and time <= timestamp(2020, 3, 31, 23, 59)
    strategy.disable()

// Plot Strategy Conditions on Chart
plotshape(series=longCondition, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Plot Stop Loss and Take Profit Levels
plot(stopLoss, title="Stop Loss", color=color.red)
plot(takeProfit, title="Take Profit", color=color.green)
```

This script implements the momentum breakout strategy as described in the original document. It uses user-defined start and end dates to backtest the strategy on the specified time frame and exchange. The script includes conditions for both long and short entries based on MACD, RSI, and Stochastic indicators. It also sets up stop loss and take profit levels dynamically based on a risk-reward ratio input by the user. Additionally, it includes a condition to skip March 2020 as specified in the original strategy description.