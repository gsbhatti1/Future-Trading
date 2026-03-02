> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|40|Take Profit pip|
|v_input_2|20|Stop Loss pip|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_","currency":"BTCUSD"}]
*/

//@version=5
strategy("Three Inside Down Reversal Strategy", overlay=true)

// Input parameters for take profit and stop loss in pips
take_profit_pip = input(40, title="Take Profit pip")
stop_loss_pip = input(20, title="Stop Loss pip")

// Function to check if the candlestick pattern matches the Three Inside Down criteria
is_three_inside_down(c1, c2, c3) =>
    // Candle 1: Long upper shadow bullish candle
    is_candle_1 = hlc4[c1] < open[c1 + 1] and close[c1] > open[c1] and (close[c1] - open[c1]) / (high[c1] - low[c1]) > 0.5

    // Candle 2: Bearish candle that completely engulfs the previous bullish candle
    is_candle_2 = close[c2] < open[c1 + 1] and open[c2] >= close[c1 + 1] and (close[c2] - open[c2]) > (close[c1] - open[c1])

    // Candle 3: Open below previous closing, close also lower
    is_candle_3 = open[c3] < close[c2] and close[c3] < open[c2]

    is_candle_1 and is_candle_2 and is_candle_3

// Find the position of the third candle in the sequence
c1_idx = bar_index - 2
c2_idx = c1_idx + 1
c3_idx = c2_idx + 1

// Check if the pattern matches at the current bar index
if (is_three_inside_down(c1_idx, c2_idx, c3_idx))
    // Open long position at the opening price of candle 3
    strategy.entry("Long", strategy.long)

    // Set stop loss and take profit levels in pips
    stop_loss_price = close[c1_idx] - stop_loss_pip * syminfo.mintick
    take_profit_price = close[c1_idx] + take_profit_pip * syminfo.mintick
    
    strategy.exit("Take Profit", "Long", stop=stop_loss_price, limit=take_profit_price)
```

This Pine Script code defines a trading strategy based on the Three Inside Down Reversal pattern. It uses input parameters for setting the Take Profit and Stop Loss levels in pips and applies this to a specified time frame of 1-hour bars with a base period of 15 minutes. The strategy opens long positions when the Three Inside Down Reversal pattern is detected, setting corresponding stop loss and take profit orders.