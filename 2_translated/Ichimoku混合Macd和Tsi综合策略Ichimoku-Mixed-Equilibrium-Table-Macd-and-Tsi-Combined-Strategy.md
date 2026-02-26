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
fast_length = input(8, title="Fast Length")
slow_length = input(28, title="Slow Length")
macd_line, signal_line, _ = macd(close, fast_length, slow_length, 9)

// Chaikin Money Flow (CMF)
cmf_length = input(17, title="CMF Length")
cmf = chaikin_money_flow(close, high, low, open, cmf_length)

// TSI Oscillator
tsi_length = input(14, title="TSI Length")
tsi = tsi(5, 3, close)

long_condition = (cross(tenkan, kijun) and ss_high > high and long_entry)
short_condition = (cross(kijun, tenkan) and ss_low < low and short_entry)

if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)


```

### Explanation of the Code
- **Inputs**: The script defines several inputs for customizing the Ichimoku Kinko Hyo, MACD, Chaikin Money Flow, and TSI Oscillator.
  - `ts_bars`, `ks_bars`, and `ssb_bars` set the number of bars for the Tenkan-Sen, Kijun-Sen, and Senkou Span B lines respectively.
  - `cs_offset` sets the offset for the Chikou Span line.
  - `ss_offset` sets the offset for the Senkou Span A/B lines.
  - `long_entry` and `short_entry` control whether to enter long or short positions based on the Ichimoku conditions.

- **Ichimoku Components**: The script calculates the Tenkan-Sen, Kijun-Sen, and Senkou Span A/B lines using the inputs provided.

- **MACD**: The MACD line, signal line, and histogram are calculated with customizable fast and slow lengths.

- **Chaikin Money Flow (CMF)**: The Chaikin Money Flow is calculated based on the close, high, low, and open prices over a specified period.

- **TSI Oscillator**: The TSI Oscillator is calculated using a customizable length.

- **Trading Conditions**: Long and short entries are triggered based on the Ichimoku conditions combined with the Chaikin Money Flow and TSI Oscillator signals.

This script allows for automated trading based on these multiple technical indicators.