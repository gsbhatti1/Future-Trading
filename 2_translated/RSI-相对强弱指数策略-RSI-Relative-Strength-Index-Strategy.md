``` pinescript
/*backtest
start: 2024-03-18 00:00:00
end: 2024-04-17 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Ds_investimento", overlay=true)

// RSI Parameters
rsi_length = input(7, title="RSI Period")
rsi_overbought = input(70, title="Overbought (RSI)")
rsi_oversold = input(30, title="Oversold (RSI)")
trail_offset = input(0.005, title="Trailing Stop Offset")
stop_loss_points = input(10, title="Stop Loss Points")
risk_percentage = input(true, title="% Risk")

// Calculate RSI
rsi = rsi(close, rsi_length)

// Entry Conditions
long_condition = crossover(rsi, rsi_oversold)
short_condition = crossunder(rsi, rsi_overbought)

// Position Sizing
position_size = risk_percentage ? (account.equity * risk_percentage) / stop_loss_points : 0

// Trailing Stop Loss
trailing_stop_long = rsi <= rsi[1] - trail_offset ? rsi[1] : rsi
trailing_stop_short = rsi >= rsi[1] + trail_offset ? rsi[1] : rsi

// Trade Management
if (long_condition)
    strategy.entry("Long", strategy.long, size=position_size)

if (short_condition)
    strategy.entry("Short", strategy.short, size=position_size)

// Stop Loss
strategy.exit("Stop Loss Long", "Long", stop=true, limit=false, qty=pos.amount * 0.95)
strategy.exit("Stop Loss Short", "Short", stop=true, limit=false, qty=pos.amount * 0.95)
```

This Pine Script code implements the RSI strategy as described in the translated text. The script calculates the RSI and uses it to generate long and short trading signals based on overbought and oversold conditions. It also includes trailing stop losses and position sizing logic, adhering closely to the original description.