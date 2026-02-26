``` pinescript
/*backtest
start: 2024-02-19 00:00:00
end: 2025-02-16 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=6
strategy("KON SET By Sai", overlay=true, max_lines_count=40)

// INPUTS
length = input.int(10, "Trend Length")
target_multiplier = input.int(0, "Set Targets") // Target adjustment
max_bars = 30  // Number of bars to display the lines after signal

// VARIABLES
var bool inTrade = false
var float entryPrice = na
var float stopLoss = na
var float targetPrice = na
var int barCount = na  // Counter to track how many bars have passed since signal

// ATR for stop-loss and target calculation
atr_value = ta.sma(ta.atr(200), 200) * 0.8

// Moving averages for trend detection
sma_high = ta.sma(high, length) + atr_value
sma_low = ta.sma(low, length) - atr_value

// Signal conditions for trend changes
signal_up = ta.crossover(close, sma_high)
signal_down = ta.crossunder(close, sma_low)

// Entry conditions
if not inTrade and signal_up
    entryPrice := close
    stopLoss := close - atr_value * 2
    targetPrice := close + atr_value * (5 + target_multiplier)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long", stop=stopLoss, limit=targetPrice)
    inTrade := true
    barCount := 0  // Reset bar count when signal occurs

```