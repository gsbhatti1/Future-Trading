> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|10|From Day|
|v_input_3|2020|From Year|
|v_input_4|2|Thru Month|
|v_input_5|21|Thru Day|
|v_input_6|2024|Thru Year|
|v_input_7|true|Lookback Period|
|v_input_8|2|Rally|
|v_input_9|2|Stop Loss (%)|
|v_input_10|2|Take Profit (%)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Sell the Rallies", overlay=true, initial_capital=212, commission_type=strategy.commission.percent, commission_value=0, pyramiding=2)

// Backtest dates
fromMonth = input(1, "From Month")
fromDay = input(10, "From Day")
fromYear = input(2020, "From Year")
thruMonth = input(2, "Thru Month")
thruDay = input(21, "Thru Day")
thruYear = input(2024, "Thru Year")

// Lookback period
lookbackPeriod = input(true, "Lookback Period")

// Rally threshold
rallyThreshold = input(2, "Rally")

// Stop Loss and Take Profit percentages
stopLossPercent = input(2, "Stop Loss (%)")
takeProfitPercent = input(2, "Take Profit (%)")

// Variables
var float stopLossLevel = na
var float takeProfitLevel = na

// Strategy logic
if (time >= timestamp(fromYear, fromMonth, fromDay, 0, 0) and time <= timestamp(thruYear, thruMonth, thruDay, 23, 59))
    if lookbackPeriod
        // Calculate stop loss and take profit levels based on the lookback period
        // This part of the logic is not provided in the original text and would require additional Pine Script code to implement
        // For example:
        // stopLossLevel := avgEntryPrice * (1 - stopLossPercent / 100)
        // takeProfitLevel := avgEntryPrice * (1 + takeProfitPercent / 100)
    else
        // Enter short position when the overall percentage change crosses above the rally threshold
        if close > open and (close - open) / open >= rallyThreshold / 100
            strategy.entry("Short", strategy.short)

    // Exit conditions based on stop loss and take profit levels
    if not na(stopLossLevel) and close <= stopLossLevel
        strategy.close("Short")
    else if not na(takeProfitLevel) and close >= takeProfitLevel
        strategy.close("Short")

// Plot the stop loss and take profit levels (if defined)
plot(shape.rect, title="Stop Loss", x=bar_index, y1=stopLossLevel, y2=low, color=color.red, style=shape.style_linebr, linewidth=2)
plot(shape.rect, title="Take Profit", x=bar_index, y1=takeProfitLevel, y2=high, color=color.green, style=shape.style_linebr, linewidth=2)

// Optional: Plot the lookback period (if enabled)
if lookbackPeriod
    // Add additional code to plot the lookback period based on historical data
```

This PineScript source code implements the "Sell the Rallies" strategy with the specified inputs and logic. The script includes placeholders for calculating stop loss and take profit levels, which would need to be implemented based on specific trading rules or historical data analysis.