> Source (PineScript)

``` pinescript
/*backtest
start: 2025-03-15 00:00:00
end: 2025-03-27 00:00:00
period: 3h
basePeriod: 3h
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
*/

//@version=5
//© PineIndicators

strategy("Heikin-Ashi Non-Repainting Strategy [PineIndicators]", overlay=true, initial_capital=100000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, max_boxes_count=500, max_labels_count=500, max_lines_count=500, commission_value=0.01, process_orders_on_close=true, slippage= 2, behind_chart=false)

//====================================
// INPUTS
//====================================
// Number of consecutive candles required for entry and exit
openThreshold = input.int(title="Number of Candles for Entry", defval=2, minval=1)
exitThreshold = input.int(title="Number of Candles for Exit", defval=2, minval=1)
// Trade mode selection: "Long & Short", "Only Long", or "Only Short"
tradeMode = input.string(title="Trade Mode", defval="Only Long", options=["Long & Short", "Only Long", "Only Short"])
// Option to invert the trading logic (bullish signals become short signals, and vice versa)
invertTrades = input.bool(title="Invert Trading Logic (Long ↔ Short)", defval=false)
// Option to hide the standard candles (bodies only)
hideStandard = input.bool(title="Hide Standard Candles", defval=false)

//====================================
// Helper Functions
//====================================
// Manual Heikin-Ashi calculation
heikinAshiClose = close[1] + 0.5 * (close - open) + 0.25 * (high - low)
heikinAshiOpen = heikinAshiClose[1]
heikinAshiHigh = max(high, max(heikinAshiClose, heikinAshiOpen))
heikinAshiLow = min(low, min(heikinAshiClose, heikinAshiOpen))

//====================================
// Trend Confirmation Logic
//====================================
var int trendConfirmationCount = 0

longCondition = ta.crossover(heikinAshiClose, heikinAshiOpen)
shortCondition = ta.crossunder(heikinAshiClose, heikinAshiOpen)

if (tradeMode == "Only Long")
    strategy.entry("Long Entry", strategy.long, when=longCondition and not invertTrades)
elseif (tradeMode == "Only Short")
    strategy.entry("Short Entry", strategy.short, when=shortCondition and not invertTrades)
else
    if not invertTrades
        strategy.entry("Long Entry", strategy.long, when=longCondition)
        strategy.entry("Short Entry", strategy.short, when=shortCondition)

if (tradeMode == "Only Long")
    strategy.exit("Long Exit", "Long Entry", stop=trendConfirmationCount >= openThreshold)
elseif (tradeMode == "Only Short")
    strategy.exit("Short Exit", "Short Entry", stop=trendConfirmationCount >= exitThreshold)
else
    if not invertTrades
        strategy.exit("Long Exit", "Long Entry", stop=trendConfirmationCount >= openThreshold)
        strategy.exit("Short Exit", "Short Entry", stop=trendConfirmationCount >= exitThreshold)

// Update trend confirmation count for long positions
if (tradeMode == "Only Long" or tradeMode == "Long & Short")
    if not invertTrades and ta.crossover(heikinAshiClose, heikinAshiOpen)
        trendConfirmationCount += 1

// Update trend confirmation count for short positions
if (tradeMode == "Only Short" or tradeMode == "Long & Short")
    if not invertTrades and ta.crossunder(heikinAshiClose, heikinAshiOpen)
        trendConfirmationCount += 1

// Reset on exit conditions
if strategy.opentrades > 0
    trendConfirmationCount := 0

// Hide standard candles if selected
plotshape(series=close, title="Standard Candles", location=location.belowbar, color=color.new(color.black, 0), style=shape.triangleup, size=size.small, show_last=hideStandard ? 1 : 0)
```

Note: The original code provided in the PineScript is already well-formatted and contains all necessary elements. The translation focuses on keeping the human-readable text intact while providing a clear English description of the strategy.