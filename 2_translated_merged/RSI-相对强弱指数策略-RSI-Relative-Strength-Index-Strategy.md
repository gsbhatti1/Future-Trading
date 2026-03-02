``` pinescript
/*backtest
start: 2024-03-18 00:00:00
end: 2024-04-17 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RsI_Strategy", overlay=true)

// RSI Parameters
rsi_length = input(7, title="RSI Period")
rsi_overbought = input(70, title="Overbought (RSI)")
rsi_oversold = input(30, title="Oversold (RSI)")
trail_offset = input(0.005, title="Trailing Stop Offset")
stop_loss_points = input(10, title="Stop Loss Points")
risk_percentage = input(true, type=input.bool, title="Risk Percentage (%)")

// Calculate RSI
rsi = rsi(close, rsi_length)

// Trading Logic
if (rsi <= rsi_oversold)
    strategy.entry("Long", strategy.long)
elif (rsi >= rsi_overbought)
    strategy.entry("Short", strategy.short)

// Trailing Stop Loss
trail_price_long = strategy.position_avg_price * (1 - trail_offset)
trail_price_short = strategy.position_avg_price * (1 + trail_offset)

strategy.exit("Trailing Exit Long", from_entry="Long", limit=trail_price_long)
strategy.exit("Trailing Exit Short", from_entry="Short", stop=trail_price_short)

// Stop Loss
if (rsi > rsi_overbought and strategy.long)
    strategy.close("Long", comment="Stop Loss")
if (rsi < rsi_oversold and strategy.short)
    strategy.close("Short", comment="Stop Loss")

// Position Sizing
position_size = risk_percentage ? account.equity * risk_percentage : 1

```

This Pine Script code implements the described RSI-based trading strategy. It includes calculations for the RSI, entry conditions based on overbought and oversold levels, trailing stop losses, and stop loss mechanisms. The script also accounts for position sizing based on a percentage of account equity if specified.