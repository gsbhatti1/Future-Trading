``` pinescript
/*backtest
start: 2022-04-11 00:00:00
end: 2022-05-10 23:59:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/ - © José Manuel Gassin Pérez-Traverso
// Credit for each indicator belongs to its author.

//@version=5
indicator(title="HALFTREND + HEMA + SMA (FALSE SIGNAL)", shorttitle="HALFTREND + HEMA + SMA (FALSE SIGNAL)", overlay=true)


//== Constants
c_black               = color.rgb(0, 0, 0, 0)
c_green_radiative     = color.rgb(0, 255, 0, 0)
c_green               = color.rgb(0, 128, 0, 0)
c_dark_green          = color.rgb(0, 80, 0, 0)
c_red_radiative       = color.rgb(255, 0, 0, 0)
c_red                 = color.rgb(128, 0, 0, 0)
c_dark_red            = color.rgb(80, 0, 0, 0)
c_red_t               = color.new(color.red, 90)
c_yellow              = color.rgb(255, 255, 0, 0)
noneColor             = color.new(color.white, 100)


//== Strategy
GROUP_STRATEGY = "Strategy"
STRATEGY_complete_candle_outside_hema = input.bool(title="Full candle must be outside the HEMA / Wicks can touch the HEMA but body must be out", defval=false, group=GROUP_STRATEGY)

//== Simple Moving Average (SMA)
GROUP_SMA = "Simple Moving Average (SMA)"
length = input.int(150, minval=1, title="Length", group=GROUP_SMA)
src = input(close, title="Source", group=GROUP_SMA)
offset = input.int(title="Offset", defval=6, minval=-500, maxval=500, group=GROUP_SMA)
sma = ta.sma(src, length)


//== Hull Estimate (HEMA) - Source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/ - © alexgrover
GROUP_HEMA = "Hull Estimate (HEMA)"
length = input.int(title="Length", defval=50, minval=1, group=GROUP_HEMA)
hema = 3 * ta.wma(close, length / 2) - 2 * ta.ema(close, length / 2)


//== HALFTREND - Copyright (c) 2021-present, Alex Orekhov (everget)
GROUP_HT = "Halftrend"
amplitude = input(title='Amplitude', defval=1, group=GROUP_HT)
channel_deviation = input(title='Channel Deviation', defval=2, group=GROUP_HT)
show_arrows = input(title='Show Arrows', defval=true, group=GROUP_HT)
show_channels = input(title='Show Channels', defval=false, group=GROUP_HT)

var int trend = 0
var int next_trend = 0
var float max_low_price = nz(low[1], low)
var float min_high_price = nz(high[1], high)

var float up = 0.0
var float down = 0.0
float atr_high = 0.0
float atr_low = 0.0
float arrow_up = na
float arrow_down = na

atr2 = ta.atr(100) / 2
deviation = channel_deviation * atr2

high_price = high[math.abs(ta.highestbars(amplitude))]
low_price = low[math.abs(ta.lowestbars(amplitude))]
high_ma = ta.sma(high, amplitude)
low_ma = ta.sma(low, amplitude)

if next_trend == 1
    max_low_price := math.max(low_price, max_low_price)

    if high_ma < max_low_price and close < nz(low[1], low)
        trend := 1
        next_trend := 0
        min_high_price := high_price
else
    min_high_price := math.min(high_price, min_high_price)

    if low_ma > min_high_price and close > nz(high[1], high)
        trend := 0
        next_trend := 1
        max_low_price := low_price

if trend == 0
    if not na(trend[1]) and trend[1] != 0
        up := na(down[1]) ? down : down[1]
        arrow_up := up - atr2
        arrow_up
    else
        up := na(up[1]) ? max_low_price : math.max(max_low_price, up[1])
        up
    atr_high := up + deviation
    atr_low := up - deviation
    atr_low
else
    if not na(trend[1]) and
```