``` pinescript
/*backtest
start: 2023-10-01 00:00:00
end: 2023-10-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © exlux99

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

// MACD
fast_length = input(17, title="Fast Length")
slow_length = input(28, title="Slow Length")
macd_source = input(close, title="Source: close/high/low/open/hl2/hlc3/hlcc4/ohlc4")
signal_smoothing = input(5, title="Signal Smoothing")

[macd_line, signal_line, _] = macd(macd_source, fast_length, slow_length, signal_smoothing)

// Chaikin Money Flow
cmf_length = input(8, minval=1, title="CMF Length")
chikou_span = close[cs_offset]

// TSI Oscillator
long_len = input(8, minval=1, title="Long Length")
short_len = input(8, minval=1, title="Short Length")
tsi_line = tsi(close, long_len, short_len)

// Buy and Sell Conditions
buy_condition = tenkan > kijun and ss_high > close[0] and macd_line > 0 and signal_line > 0 and cmf_length > 0 and tsi_line > 0
sell_condition = tenkan < kijun and ss_low < close[0] and macd_line < 0 and signal_line < 0 and cmf_length < 0 and tsi_line < 0

if (buy_condition)
    strategy.entry("Buy", strategy.long)

if (sell_condition)
    strategy.exit("Sell", "Buy")

// Plot indicators
plot(tenkan, color=color.blue, title="Tenkan-Sen")
plot(kijun, color=color.red, title="Kijun-Sen")
plot(senkouA, color=color.green, title="Senkou Span A")
plot(senkouB, color=color.orange, title="Senkou Span B")
plot(macd_line, color=color.purple, title="MACD Line")
plot(signal_line, color=color.aqua, title="Signal Line")
plot(chikou_span, color=color.black, title="Chikou Span")

// Optional Plot for TSI
plot(tsi_line, color=color.magenta, title="TSI Oscillator")

```

This updated Pine Script implements the strategy based on the provided parameters and descriptions.