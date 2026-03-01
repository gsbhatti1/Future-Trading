``` pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 5m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"NIFTY"}]
*/

//@version=4
strategy("Dual-Moving-Average-Bollinger-Band-MACD-Trading-Strategy", shorttitle="DMABBB_MACD", overlay=true)

var bool open_buy_position = na
var bool open_sell_position = na

// MACD settings
fast_length = input(12, title="Fast Length")
slow_length = input(26, title="Slow Length")
signal_length = input(9, title="Signal Length")
src = close

// Bollinger Bands settings
bb_len = input(20, title="Bollinger Band Length")
bb_mult = input(2.0, title="Bollinger Band Multiplier")

// Calculate MACD values
macd_line, signal_line, _ = macd(src, fast_length, slow_length, signal_length)
hist_value = macd_line - signal_line

// Calculate Bollinger Bands upper and lower lines
bb_middle = sma(close, bb_len)
bb_stddev = stdev(close, bb_len)
upper_band = bb_middle + bb_mult * bb_stddev
lower_band = bb_middle - bb_mult * bb_stddev

// Buy condition: Golden cross with MACD and close above upper band
if (macd_line > signal_line and hist_value > 0) and close > upper_band
    strategy.entry("Buy", strategy.long)
    open_buy_position := true

// Sell condition: Death cross with MACD and close below lower band
if (macd_line < signal_line and hist_value < 0) and close < lower_band
    strategy.entry("Sell", strategy.short)
    open_sell_position := true

// Close positions based on take profit and stop loss conditions
take_profit_points = input(60, title="Take Profit (Points)")
stop_loss_points = input(30, title="Stop Loss (Points)")

if is_long_position and close < upper_band - take_profit_points * point_size
    strategy.close("Buy")

if is_short_position and close > lower_band + stop_loss_points * point_size
    strategy.close("Sell")

// Support functions for position management
is_long_position = open_buy_position and not open_sell_position
is_short_position = open_sell_position and not open_buy_position

point_size = point_size()
```