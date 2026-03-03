> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|50|Fast MA Length|
|v_input_2|200|Slow MA Length|
|v_input_3|2|Risk-Reward Ratio|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-24 00:00:00
end: 2024-01-31 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0

//@version=5
strategy("Moving-Average-Trend-Following-Strategy", overlay=true)

// Input parameters
fast_ma_len = input.int(50, title="Fast MA Length")
slow_ma_len = input.int(200, title="Slow MA Length")
risk_reward_ratio = input.float(2.0, title="Risk-Reward Ratio")

// Calculate the moving averages
fast_ma = ta.sma(close, fast_ma_len)
slow_ma = ta.sma(close, slow_ma_len)

// Plot the moving averages on the chart
plot(fast_ma, color=color.blue, title="Fast MA")
plot(slow_ma, color=color.red, title="Slow MA")

// Define entry conditions
long_condition = ta.crossover(fast_ma, slow_ma)
short_condition = ta.crossunder(fast_ma, slow_ma)

// Execute trades based on the conditions
if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

// Set stop loss and take profit levels
stop_loss_level = risk_reward_ratio * strategy.point_size * close / risk_reward_ratio - close
take_profit_level = risk_reward_ratio * strategy.point_size * close + close

// Apply trailing stops
strategy.exit("Long Exit", "Long", stop=stop_loss_level, limit=take_profit_level)
strategy.exit("Short Exit", "Short", stop=stop_loss_level, limit=take_profit_level)

// Plot the exit levels on the chart
plot(stop_loss_level, color=color.green, title="Stop Loss")
plot(take_profit_level, color=color.orange, title="Take Profit")
```

This Pine Script code implements a moving average trend-following strategy that uses fast and slow moving averages to identify trading opportunities. The script sets up entry conditions based on crossovers of these moving averages and manages risk through trailing stop losses and take profits.