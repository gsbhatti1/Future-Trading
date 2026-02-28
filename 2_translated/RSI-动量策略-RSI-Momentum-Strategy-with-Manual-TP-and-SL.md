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
rsi_crossed_above_130 = vrsi < overBought and ta.sma(vrsi, 2) >= overBought // RSI crossed below 70
daily_close_below_threshold = close < (ta.lowest(close, 50) * 1.3) // Daily close below 130% of the lowest close in the last 50 bars

// Trading Logic
if (rsi_crossed_below_30 and daily_close_above_threshold)
    strategy.entry("Long", strategy.long)

if (rsi_crossed_above_130 and daily_close_below_threshold)
    strategy.entry("Short", strategy.short)

// Take Profit and Stop Loss Levels
trail_profit = input.float(20, title="Take Profit (%)")
stop_loss = input.float(25, title="Stop Loss (%)")

trail_price_long = na(strategy.position_avg_price) ? close : strategy.position_avg_price + (strategy.position_avg_price * trail_profit_pct / 100)
trail_price_short = na(strategy.position_avg_price) ? close : strategy.position_avg_price - (strategy.position_avg_price * stop_loss / 100)

// Trailing Stop for Long Position
if (strategy.opentrades > 0 and strategy.position_size > 0)
    strategy.exit("Trailing Long", "Long", limit=trail_price_long, stop=strategy.position_avg_price + (strategy.position_avg_price * stop_loss / 100))

// Trailing Stop for Short Position
if (strategy.opentrades > 0 and strategy.position_size < 0)
    strategy.exit("Trailing Short", "Short", limit=trail_price_short, stop=strategy.position_avg_price - (strategy.position_avg_price * stop_loss / 100))
```

> Strategy Arguments

| Argument        | Default  | Description                                                                                          |
|-----------------|----------|------------------------------------------------------------------------------------------------------|
| v_input_1       | 14      | RSI Length                                                                                            |
| v_input_2       | 30      | Oversold Level                                                                                        |
| v_input_3       | 70      | Overbought Level                                                                                     |
| v_input_float_1 | 20      | Trailing Profit (%)                                                                                  |
| v_input_float_2 | true    | Take Profit (%)                                                                                      |
| v_input_float_3 | true    | Stop Loss (%)                                                                                        |