``` pinescript
/*backtest
start: 2023-05-28 00:00:00
end: 2024-06-02 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © DD173838

//@version=5
strategy("MACD Convergence Strategy with R:R, Daily Limits, and Tighter Stop Loss", overlay=true, default_qty_type=strategy.fixed, default_qty_value=1)

// MACD settings
fastLength = input.int(12, title="Fast Length", minval=1)
slowLength = input.int(26, title="Slow Length", minval=1)
signalSmoothing = input.int(9, title="Signal Smoothing", minval=1)
source = input(close, title="Source")

// Calculate MACD
[macdLine, signalLine, _] = ta.macd(source, fastLength, slowLength, signalSmoothing)

// Define thresholds for long and short signals
longThreshold = 1.5
shortThreshold = -1.5

// Determine trading signals based on MACD line and signal line crossover
longSignal = ta.crossover(macdLine, signalLine) and macdLine > longThreshold
shortSignal = ta.crossunder(macdLine, signalLine) and macdLine < shortThreshold

// Define take-profit and stop-loss levels
takeProfitLong = close + 600 * syminfo.minmove
stopLossLong = close - 100 * syminfo.minmove
takeProfitShort = close - 600 * syminfo.minmove
stopLossShort = close + 100 * syminfo.minmove

// Define trailing stop-loss logic
trailStopLong = ta.valuewhen(macdLine > signalLine, macdLine, 1) + (close - ta.valuewhen(macdLine > signalLine, macdLine, 1) - 300)
trailStopShort = ta.valuewhen(macdLine < signalLine, macdLine, 1) - (ta.valuewhen(macdLine < signalLine, macdLine, 1) - close - 300)

// Set daily maximum loss and profit limits
dailyMaxLoss = 600 * syminfo.minmove
dailyMaxProfit = 1800 * syminfo.minmove

// Trading logic
if (longSignal)
    strategy.entry("Long", strategy.long, when=true)
    strategy.exit(id="Take Profit Long", from_entry="Long", limit=takeProfitLong, stop=stopLossLong)

if (shortSignal)
    strategy.entry("Short", strategy.short, when=true)
    strategy.exit(id="Take Profit Short", from_entry="Short", limit=takeProfitShort, stop=stopLossShort)

// Trailing Stop Loss logic
if (strategy.position_size > 0) // Long position
    strategy.exit(id="Trailing Stop Long", from_entry="Long", stop=trailStopLong)
if (strategy.position_size < 0) // Short position
    strategy.exit(id="Trailing Stop Short", from_entry="Short", stop=trailStopShort)

// Exit all positions based on daily limits
if (strategy.netprofit > dailyMaxProfit or strategy.netloss > dailyMaxLoss)
    strategy.close("All Positions")
```

This Pine Script defines a trading strategy using MACD for generating buy and sell signals, incorporating risk-reward ratio, trailing stop-loss logic, and daily profit/loss limits. The script uses the Binance Futures BTC_USDT market as an example exchange.