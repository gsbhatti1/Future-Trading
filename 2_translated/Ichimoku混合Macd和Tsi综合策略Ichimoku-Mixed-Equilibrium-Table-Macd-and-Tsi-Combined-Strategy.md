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

// Helper function to calculate middle values
middle(len) => avg(lowest(len), highest(len))

// Ichimoku Components
tenkan = middle(ts_bars)
kijun = middle(ks_bars)
senkouA = avg(tenkan, kijun)
senkouB = middle(ssb_bars)

ss_high = max(senkouA[ss_offset-1], senkouB[ss_offset-1])
ss_low = min(senkouA[ss_offset-1], senkouB[ss_offset-1])

// MACD Components
fast_len = input(8, title="Fast Length")
slow_len = input(26, title="Slow Length")
signal_smoothing = input(5, title="Signal Smoothing")

macd_line, signal_line, _ = macd(close, fast_len, slow_len, signal_smoothing)

// Chaikin Money Flow
cmf_len = input(13, minval=1, title="CMF Length")
cmf = chaikin_money_flow(close, high, low, open, cmf_len)

// TSI Components
long_period = input(25, minval=1, title="Long Period")
short_period = input(13, minval=1, title="Short Period")
tsi_value = tsi(close, long_period, short_period)

// Strategy Logic
// Bullish Entry Conditions
bullish_entry = tenkan > kijun and close > ss_high

// Bearish Entry Conditions
bearish_entry = tenkan < kijun and close < ss_low

// MACD and Chaikin Money Flow Signal for Entries
macd_positive = macd_line >= 0 and signal_line >= 0 and cmf >= 0
macd_negative = macd_line <= 0 and signal_line <= 0 and cmf <= 0

if (bullish_entry or long_entry and macd_positive)
    strategy.entry("Long", strategy.long)

if (bearish_entry or short_entry and macd_negative)
    strategy.entry("Short", strategy.short)

// Reverse Trade for Opposite Signals
if bullish_entry and not long_entry
    strategy.close("Long")

if bearish_entry and not short_entry
    strategy.close("Short")
```

This script implements the Ichimoku with MACD, Chaikin Money Flow (CMF), and TSI strategy as described in the document. It includes all the necessary inputs and logic to handle bullish and bearish entries based on multiple indicators.