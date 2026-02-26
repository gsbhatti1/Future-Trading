> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|10|short ema|
|v_input_int_2|50|long ema|
|v_input_int_3|200|hourly 10 ema|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_4|false|Offset|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-22 00:00:00
end: 2023-12-22 00:00:00
symbol: ^GSPC
interval: 15
*/

//@version=5
strategy("10EMA Double Cross Trend Tracking Strategy", overlay=true)

short_ema = input.int(10, title="Short EMA")
long_ema = input.int(50, title="Long EMA")
hourly_short_ema = input.int(200, title="Hourly 10 EMA")

source = input(close, title="Source", options=[close, high, low, open, hl2, hlc3, hlcc4, ohlc4])
offset = input.bool(false, title="Offset")

// Calculate EMAs
short_ema_value = ta.ema(source, short_ema)
long_ema_value = ta.ema(source, long_ema)
hourly_short_ema_value = ta.sma(source, hourly_short_ema)

// Plot EMAs
plot(short_ema_value, color=color.blue, title="Short EMA")
plot(long_ema_value, color=color.red, title="Long EMA")
plot(hourly_short_ema_value, color=color.green, title="Hourly 10 EMA")

// Define signals
long_signal = ta.crossover(short_ema_value, long_ema_value)
short_signal = ta.crossunder(short_ema_value, long_ema_value)

if (offset == false and long_signal and not na(hourly_short_ema_value))
    strategy.entry("Long", strategy.long)

if (offset == false and short_signal and not na(hourly_short_ema_value))
    strategy.entry("Short", strategy.short)

// Trailing Stop Loss
stop_loss = 0.5 * point_size
trail_deviation = 2

long_stop = strategy.position_avg_price - stop_loss
short_stop = strategy.position_avg_price + stop_loss

strategy.exit("Long Exit", "Long", trail=True, stop=long_stop, deviation=trail_deviation)
strategy.exit("Short Exit", "Short", trail=True, stop=short_stop, deviation=trail_deviation)
```

[/trans]

This Pine Script defines a trend tracking strategy based on the double cross of 10EMA and 50EMA with hourly 10EMA as an auxiliary indicator. It includes the calculation and plotting of EMAs, signal definition for entering long and short positions, and trailing stop loss mechanism to manage exits.