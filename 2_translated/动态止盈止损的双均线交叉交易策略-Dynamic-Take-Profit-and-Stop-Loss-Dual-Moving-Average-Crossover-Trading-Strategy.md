``` pinescript
/*backtest
start: 2024-05-01 00:00:00
end: 2024-05-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Pubgentleman

//@version=5
strategy("TSLA 1-Hour SMA Crossover Strategy with Buy/Sell Signals", overlay=true)

// Parameters
shortSmaLength = input.int(50, title="Short SMA Length")
longSmaLength = input.int(100, title="Long SMA Length")
takeProfitPercent = input.float(2.0, title="Take Profit Percentage (%)")
stopLossPercent = input.float(1.5, title="Stop Loss Percentage (%)")

// Calculate SMAs
shortSMA = ta.sma(close, shortSmaLength)
longSMA = ta.sma(close, longSmaLength)

// Plot SMAs on the chart
plot(shortSMA, color=color.blue, title="Short SMA")
plot(longSMA, color=color.red, title="Long SMA")

// Generate buy and sell signals
buySignal = crossover(shortSMA, longSMA)
sellSignal = crossunder(shortSMA, longSMA)

// Calculate take-profit and stop-loss levels
takeProfitLevel = close * (1 + takeProfitPercent / 100)
stopLossLevel = close * (1 - stopLossPercent / 100)

// Place orders
if (buySignal)
    strategy.entry("Buy", strategy.long)
    strategy.exit("Take Profit/Stop Loss", "Buy", stop=stopLossLevel, limit=takeProfitLevel)

if (sellSignal)
    strategy.close("Buy")

// Plot take-profit and stop-loss levels on the chart
plot(takeProfitLevel, color=color.green, title="Take-Profit Level")
plot(stopLossLevel, color=color.red, title="Stop-Loss Level")
```

This Pine Script™ code implements a dynamic take-profit and stop-loss dual moving average crossover trading strategy for TSLA with 1-hour intervals. It includes parameters for the short and long SMA lengths, as well as the take-profit and stop-loss percentages. The script generates buy/sell signals based on the crossover of the two SMAs and exits the position when either the take-profit or stop-loss level is reached.