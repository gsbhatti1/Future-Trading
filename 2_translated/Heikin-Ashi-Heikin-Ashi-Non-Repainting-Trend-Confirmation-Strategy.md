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
hideStandard = input.bool(title="Hide Standard Candles", defval=true)

// Function to calculate non-repainting Heikin-Ashi candles
heikinashiNonRepainting(c) =>
    openPrice = (open[c] + close[c]) / 2
    highPrice = math.max(high[c], openPrice, close[c])
    lowPrice = math.min(low[c], openPrice, close[c])
    nextClose = (close[c - 1] + openPrice + highPrice + lowPrice) / 4

// Main strategy logic
for i = 0 to barssince(starttime)
    // Calculate Heikin-Ashi candles
    haOpen[i+1] := heikinashiNonRepainting(i)
    haHigh[i+1] := high[i]
    haLow[i+1] := low[i]
    haClose[i+1] := close[i]

    // Determine entry and exit conditions based on trend confirmation
    if (tradeMode == "Only Long" or tradeMode == "Long & Short")
        longCondition = ta.crossover(haOpen[1], haClose[2]) and ta.crossover(haOpen[1], haClose[3])
        if (longCondition and not invertTrades)
            strategy.entry("Long Entry", strategy.long, when=barssince(starttime) >= openThreshold - 1)
    if (tradeMode == "Only Short" or tradeMode == "Long & Short")
        shortCondition = ta.crossunder(haOpen[1], haClose[2]) and ta.crossunder(haOpen[1], haClose[3])
        if (shortCondition and not invertTrades)
            strategy.entry("Short Entry", strategy.short, when=barssince(starttime) >= exitThreshold - 1)

    // Manage exits based on trend reversal
    for j = 0 to barssince(starttime)
        if (tradeMode == "Only Long" or tradeMode == "Long & Short")
            if (haOpen[j + 2] > haClose[j + 1])
                strategy.close("Long Entry", when=barssince(starttime) >= exitThreshold - 1)
        if (tradeMode == "Only Short" or tradeMode == "Long & Short")
            if (haOpen[j + 2] < haClose[j + 1])
                strategy.close("Short Entry", when=barssince(starttime) >= openThreshold - 1)

// Hide standard candles
if hideStandard
    plotshape(series=close, title="Candle Body", location=location.belowbar, color=color.new(color.black, 0), style=shape.labeldown, text="", size=size.small)
```

This PineScript code implements the Heikin-Ashi Non-Repainting Trend Confirmation Strategy described in the document. The strategy uses non-repainting Heikin-Ashi candles and multiple trend confirmations to reduce false signals and provide a more reliable trading approach.