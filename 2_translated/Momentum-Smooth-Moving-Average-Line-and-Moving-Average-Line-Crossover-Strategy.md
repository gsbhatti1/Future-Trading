> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_4|3|K|
|v_input_int_5|15|D|
|v_input_int_6|14|RSI Length|
|v_input_int_7|8|Stochastic Length|
|v_input_1_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_source_1_close|0|(?Dominant ALMA)Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|130|Period|
|v_input_float_1|0.775|Offset|
|v_input_float_2|4.5|Sigma|
|v_input_color_1|#66bb6a|Going Up!|
|v_input_color_2|#ef5350|Going Down :(|
|v_input_bool_1|true|(?Strategy Inputs)-----------CHEATC0DE1------------|
|v_input_int_2|49|Slow Ema Length|
|v_input_int_3|9|Fast Ema Length|
|v_input_float_3|3|(?Take Profit and Stop Loss)Take Profit|
|v_input_float_4|5.49|Stop Loss|


> Source (PineScript)

```pinescript
//@version=5
strategy("Momentum-Smooth-Moving-Average-Line-and-Moving-Average-Line-Crossover-Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

length = input.int(3, minval=2, title="K")
d_length = input.int(15, minval=2, title="D")
rsi_length = input.int(14, minval=2, title="RSI Length")
stoch_length = input.int(8, minval=2, title="Stochastic Length")

source_rsi = input.source(close, title="RSI Source")
source_ema = input.source(close, title="(?Dominant ALMA)Source")

period = input.int(130)
offset = input.float(0.775)
sigma = input.float(4.5)

up_color = input.color(#66bb6a, title="Going Up!")
down_color = input.color(#ef5350, title="Going Down :(")

cheatcode = input.bool(true, title="?Strategy Inputs")
slow_ema_length = input.int(49)
fast_ema_length = input.int(9)

take_profit = input.float(3, minval=0.1, title="?Take Profit and Stop Loss Take Profit")
stop_loss = input.float(5.49, minval=0.1, title="Stop Loss")

// Calculate ALMA
alma = ta.alma(source_ema, period, offset, sigma)

// Calculate EMAs
slow_ema = ta.ema(close, slow_ema_length)
fast_ema = ta.ema(close, fast_ema_length)

// Plot ALMA and EMAs
plot(alma, title="ALMA", color=alma > 0 ? up_color : down_color, linewidth=2)
plot(slow_ema, title="Slow EMA", color=color.blue, linewidth=1)
plot(fast_ema, title="Fast EMA", color=color.red, linewidth=1)

// Stochastic RSI
rsi = ta.rsi(source_rsi, rsi_length)
stoch = ta.stoch(rsi, rsi_length, stoch_length)

// Trading logic based on EMA crossover and ALMA signal
if (crossed_above(fast_ema, slow_ema) and not na(alma[1]) and alma > 0)
    strategy.entry("Buy", strategy.long)
if (crossed_below(fast_ema, slow_ema) and not na(alma[1]) and alma < 0)
    strategy.close("Buy")

// Stochastic RSI overbought/oversold filter
long_condition = stoch > 80
short_condition = stoch < 20

if (long_condition and not na(alma[1]) and alma > 0)
    strategy.exit("Take Profit", "Buy", profit=take_profit * close, loss=stop_loss * close)

if (short_condition and not na(alma[1]) and alma < 0)
    strategy.entry("Short", strategy.short)
```