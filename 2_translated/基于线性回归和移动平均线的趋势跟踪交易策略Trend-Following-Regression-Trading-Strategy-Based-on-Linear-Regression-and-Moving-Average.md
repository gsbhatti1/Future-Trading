``` pinescript
/*backtest
start: 2023-11-17 00:00:00
end: 2023-12-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy(title="Regression Trading Strategy", shorttitle="RTS", overlay=true)

// Input parameters
n = input(14, title="SMA Period")
stop_loss_percentage = input(2, title="Stop Loss Percentage")
take_profit_percentage = input(2, title="Take Profit Percentage")

// Calculate the SMA
sma = sma(close, n)

// Linear regression function
linear_regression(src, length) =>
    sumX = 0.0
    sumY = 0.0
    sumXY = 0.0
    sumX2 = 0.0
    for i = 0 to length - 1
        sumX := sumX + i
        sumY := sumY + src[i]
        sumXY := sumXY + i * src[i]
        sumX2 := sumX2 + i * i
    slope = (length * sumXY - sumX * sumY) / (length * sumX2 - sumX * sumX)
    intercept = (sumY - slope * sumX) / length
    slope, intercept

// Calculate the linear regression line
regression_line = na
if barstate.islast
    reg_slope, reg_intercept = linear_regression(close, n)
    regression_line := reg_slope * n + reg_intercept

// Long and short conditions
long_condition = crossover(regression_line, sma) and close > regression_line
short_condition = crossunder(regression_line, sma) and close < regression_line

// Plot the SMA and regression line
plot(sma, color=color.blue, title="SMA")
plot(regression_line, color=color.red, title="Regression Line")

// Trading logic
if long_condition
    strategy.entry("Long", strategy.long)
    strategy.exit("Take Profit", "Long", stop=sma + (sma * take_profit_percentage / 100), limit=sma + (sma * take_profit_percentage / 100))
    strategy.exit("Stop Loss", "Long", stop=sma - (sma * stop_loss_percentage / 100))

if short_condition
    strategy.entry("Short", strategy.short)
    strategy.exit("Take Profit", "Short", stop=sma - (sma * take_profit_percentage / 100), limit=sma - (sma * take_profit_percentage / 100))
    strategy.exit("Stop Loss", "Short", stop=sma + (sma * stop_loss_percentage / 100))
```

This Pine Script code translates the Chinese document into English while preserving the original code structure and formatting.