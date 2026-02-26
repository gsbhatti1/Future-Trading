> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|RSI Length|
|v_input_2|30|Oversold Level|
|v_input_3|70|Overbought Level|
|v_input_float_1|20|Trailing Profit (%)|
|v_input_float_2|true|Take Profit (%)|
|v_input_float_3|true|Stop Loss (%)|


> Source (PineScript)

``` pinescript
//@version=5
strategy("RSI Strategy with Manual TP and SL", overlay=true)

// Strategy Parameters
length = input(14, title="RSI Length")
overSold = input(30, title="Oversold Level")
overBought = input(70, title="Overbought Level")
trail_profit_pct = input.float(20, title="Trailing Profit (%)")

// RSI Calculation
vrsi = ta.rsi(close, length)

// Entry Conditions for Long Position
rsi_crossed_below_30 = vrsi > overSold and ta.sma(vrsi, 2) <= overSold // RSI crossed above 30
daily_close_above_threshold = close > (ta.highest(close, 50) * 0.7) // Daily close above 70% of the highest close in the last 50 bars

// Entry Conditions for Short Position
rsi_crossed_above_70 = vrsi < overBought and ta.sma(vrsi, 2) >= overBought // RSI crossed below 70
daily_close_below_threshold = close < (ta.lowest(close, 50) * 1.3) // Daily close below 130% of the lowest close in the last 50 bars

// Additional Conditions for Entering Positions
long_condition_met = rsi_crossed_below_30 and daily_close_above_threshold
short_condition_met = rsi_crossed_above_70 and daily_close_below_threshold

if (long_condition_met)
    strategy.entry("Long", strategy.long)

if (short_condition_met)
    strategy.entry("Short", strategy.short)

// Stop Loss and Take Profit Calculation
trail_stop = trail_profit_pct / 100 * close
stop_loss_price = close - (trailing_stop < 0 ? abs(trail_stop) : 0)
take_profit_price = close + (trailing_stop > 0 ? abs(trail_stop) : 0)

// Manual Stop Loss and Take Profit
if (strategy.position_size != 0)
    strategy.exit("Long Exit", from_entry="Long", stop=stop_loss_price, limit=take_profit_price)
```

This completes the translation of your trading strategy document into English.