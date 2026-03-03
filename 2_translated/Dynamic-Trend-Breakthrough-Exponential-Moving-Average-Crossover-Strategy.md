``` pinescript
/*backtest
start: 2024-02-22 00:00:00
end: 2025-02-19 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © GlenMabasa

//@version=6
strategy("33 EMA Crossover Strategy", overlay=true)

// Input for the EMA length
ema_length = input.int(33, title="EMA Length")

// Calculate the 33-day Exponential Moving Average
ema_33 = ta.ema(close, ema_length)

// Plot the 33 EMA
plot(ema_33, color=color.blue, title="33 EMA", linewidth=2)

// Buy condition: Price crosses and closes above the 33 EMA
buy_condition = ta.crossover(close, ema_33) and close > ema_33

// Sell condition: Price crosses or closes below the 33 EMA
sell_condition = ta.crossunder(close, ema_33) or close < ema_33

// Swing high and swing low calculations
swing_high_length = input.int(14, title="Swing High Lookback")
swing_low_length = input.int(14, title="Swing Low Lookback")
swing_high = ta.highest(high, swing_high_length) // Previous swing high
swing_low = ta.lowest(low, swing_low_length)    // Previous swing low

// Profit target and stop loss for buys
buy_profit_target = swing_high
buy_stop_loss = swing_low

// Profit target and stop loss for sells
sell_profit_target = swing_low
sell_stop_loss = swing_high

// Plot buy and sell signals
plotshape(series=buy_condition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")
plotshape(series=sell_condition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown, text="SELL")

// Long trade logic
long_entry = buy_condition
strategy.entry("Long", strategy.long, when=long_entry)
strategy.exit("Take Profit & Stop Loss for Long", "Long", limit=buy_profit_target, stop=buy_stop_loss)

// Short trade logic
short_entry = sell_condition
strategy.entry("Short", strategy.short, when=short_entry)
strategy.exit("Take Profit & Stop Loss for Short", "Short", limit=sell_profit_target, stop=sell_stop_loss)
```

This Pine Script implements the described 33-period EMA crossover strategy with appropriate buy and sell conditions. It also includes logic to set profit targets and stop losses based on previous swing highs and lows. The script plots buy and sell signals visually for easy identification.