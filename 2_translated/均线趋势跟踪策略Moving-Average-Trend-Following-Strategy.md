> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|50|Fast MA Length|
|v_input_2|200|Slow MA Length|
|v_input_3|2|Risk-Reward Ratio|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-24 00:00:00
end: 2024-01-31 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0

//@version=5
strategy("Moving-Average Trend Following Strategy", overlay=true)

// Input Parameters
fast_length = input(50, title="Fast MA Length")
slow_length = input(200, title="Slow MA Length")
rr_ratio = input(2, title="Risk-Reward Ratio")

// Calculate Moving Averages
src = close
fast_ma = ta.sma(src, fast_length)
slow_ma = ta.sma(src, slow_length)

// Buy Condition: Fast MA crosses above Slow MA
cross_above = ta.crossover(fast_ma, slow_ma)
buy_price = na
if (cross_above)
    buy_price := close

// Sell Condition: Fast MA crosses below Slow MA
cross_below = ta.crossunder(fast_ma, slow_ma)
sell_price = na
if (cross_below)
    sell_price := close

// Enter Long or Short based on conditions
long_enter = na(buy_price) == false and cross_above
short_enter = na(sell_price) == false and cross_below

if long_enter
    strategy.entry("Long", strategy.long)

if short_enter
    strategy.entry("Short", strategy.short)

// Stop Loss and Take Profit Levels
stop_loss_level = rr_ratio * (strategy.position_avg_price - close)
take_profit_level = rr_ratio * (close - strategy.position_avg_price)

// Trail Stop
trail_stop = ta.valuewhen(strategy.opentrades.exists(), stop_loss_level, 0) < 
             ta.valuewhen(strategy.opentrades.exists(), take_profit_level, 0) ? 
             strategy.opentrades.entry_price(strategy.opentrades.id(1)) : 
             na

if long_enter and not na(trail_stop)
    strategy.exit("Trail Stop Long", "Long", stop=trail_stop)

if short_enter and not na(trail_stop)
    strategy.exit("Trail Stop Short", "Short", stop=trail_stop)

// Plot Moving Averages
plot(fast_ma, color=color.blue, title="Fast MA")
plot(slow_ma, color=color.red, title="Slow MA")

// Output Buy/Sell Signals
alertcondition(cross_above, title="Buy Signal", message="Cross Above Detected")
alertcondition(cross_below, title="Sell Signal", message="Cross Below Detected")
```

This Pine Script implements the Moving-Average Trend Following Strategy with customizable inputs for moving average lengths and risk-reward ratios. It calculates the strategy based on the crossovers of fast and slow moving averages and uses trailing stop to manage positions.