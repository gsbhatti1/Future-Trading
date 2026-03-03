```pinescript
//@version=4
strategy("Ichimoku with MACD/ CMF/ TSI", overlay=true, margin_long=0, margin_short=0)

// Inputs
ts_bars = input(10, minval=1, title="Tenkan-Sen Bars")
ks_bars = input(30, minval=1, title="Kijun-Sen Bars")
ssb_bars = input(52, minval=1, title="Senkou-Span B Bars")
cs_offset = input(26, minval=1, title="Chikou-Span Offset")
ss_offset = input(26, minval=1, title="Senkou-Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

middle(len) => avg(lowest(len), highest(len))

// Ichimoku Components
tenkan = middle(ts_bars)
kijun = middle(ks_bars)
senkouA = avg(tenkan, kijun)
senkouB = middle(ssb_bars)

ss_high = max(senkouA[ss_offset-1], senkouB[ss_offset-1])
ss_low = min(senkouA[ss_offset-1], senkouB[ss_offset-1])

// MACD Inputs
v_input_8 = input(17, title="Fast Length")
v_input_9 = input(28, title="Slow Length")

fast_length = v_input_8
slow_length = v_input_9

macd_line, signal_line, _ = macd(close, fast_length, slow_length, v_input_11)
hist = macd_line - signal_line

// CMF Inputs
v_input_14 = input(8, title="CMF Length")
cmf = chaikin_money_flow(close, high, low, volume, v_input_14)

// TSI Inputs
v_input_15 = input(8, title="Long Length")
v_input_16 = input(8, title="Short Length")

tsi = tsi(close, short_length=v_input_15, long_length=v_input_16)

// Entry/Exit Conditions
long_condition = (tenkan > kijun) and (ss_high > close) and (hist > 0) and (cmf > 0.1) and (tsi > 0)
short_condition = (tenkan < kijun) and (ss_low < close) and (hist < 0)

if (long_entry and long_condition)
    strategy.entry("Long", strategy.long)

if (short_entry and short_condition)
    strategy.entry("Short", strategy.short)

// Stop Loss
stop_loss_value = input(2.5, title="Stop Loss")
strategy.exit("Exit Long", "Long", stop=stop_loss_value * point_size)
strategy.exit("Exit Short", "Short", stop=stop_loss_value * point_size)
```