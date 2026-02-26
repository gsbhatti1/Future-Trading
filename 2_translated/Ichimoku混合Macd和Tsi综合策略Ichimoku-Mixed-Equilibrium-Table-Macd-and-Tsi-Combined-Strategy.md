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

// MACD and Chaikin Money Flow
fast_len = input(8, title="Fast Length")
slow_len = input(28, title="Slow Length")

macd_line, signal_line, _ = macd(close, fast_len, slow_len)
cmf_length = input(5, minval=1, title="CMF Length")
cmf = chaikin_money_flow(high, low, close, volume, cmf_length)

// TSI
tsi_length1 = input(8, title="Long Length")
tsi_length2 = input(8, title="Short Length")

tsi_line = tsi(close, tsi_length1, tsi_length2)

// Entry Conditions
tenkan_kijun_cross = ta.crossover(tenkan, kijun)
bullish_signal = tenkan > kijun and close > ss_high
bearish_signal = tenkan < kijun and close < ss_low

macd_positive = macd_line > signal_line
cmf_pos = cmf > 0
tsi_pos = tsi_line > 0

// Strategy Logic
if (tenkan_kijun_cross and bullish_signal and macd_positive and cmf_pos and tsi_pos)
    strategy.entry("Long", strategy.long)

if (tenkan_kijun_cross and bearish_signal and not macd_positive or not cmf_pos or not tsi_pos)
    strategy.close("Long")

if (tenkan_kijun_cross and short_entry and bearish_signal and not macd_positive and not cmf_pos and not tsi_pos)
    strategy.entry("Short", strategy.short)

if (tenkan_kijun_cross and long_entry and bullish_signal and macd_positive and cmf_pos and tsi_pos)
    strategy.close("Short")
```

The provided code is translated while maintaining the original structure, formatting, and functionality.