``` pinescript
/*backtest
start: 2022-09-30 00:00:00
end: 2023-10-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © abdllhatn

//@version=5
strategy("Alpha RSI Breakout Strategy", overlay=true, initial_capital=10000, default_qty_value=100)

// Inputs
sma_length = input(200, title="SMA Length")
rsi_length = input(14, title="RSI Length")
rsi_entry = input(34, title="RSI Entry Level")
rsi_stop_loss = input(30, title="RSI Stop Loss Level")
rsi_take_profit = input(50, title="RSI Take Profit Level")

// Indicators
sma_value = ta.sma(close, sma_length)
rsi_value = ta.rsi(close, rsi_length)

var bool trailing_stop_activate = false
var float trailingStop = na
var float lastClose = na

// Conditions
longCondition = ta.crossover(rsi_value, rsi_entry) and close > sma_value
shortCondition = ta.crossunder(rsi_value, rsi_entry) and close < sma_value

// Entry Logic
if (longCondition)
    strategy.entry("Long", strategy.long)
    
// Trailing Stop
trailing_stop_activate := not na(trailingStop) and (close < trailingStop)
trail_distance = 0.5 * (sma_length / rsi_length)
stop_loss_price = max(sma_value, lastClose)

if (longCondition or shortCondition)
    strategy.exit("Long Exit", "Long", stop=trailingStop, limit=rsi_take_profit)
    
// Update trailing stop
if (not na(trailingStop) and not trailing_stop_activate and close > trailingStop)
    trailingStop := max(trail_distance + sma_value, lastClose)
lastClose := close
```