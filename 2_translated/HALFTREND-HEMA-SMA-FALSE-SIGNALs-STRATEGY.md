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
c_negro               = color.rgb(0, 0, 0, 0)
c_verde_radiactivo    = color.rgb(0, 255, 0, 0)
c_verde               = color.rgb(0, 128, 0, 0)
c_verde_oscuro        = color.rgb(0, 80, 0, 0)
c_rojo_radiactivo     = color.rgb(255, 0, 0, 0)
c_rojo                = color.rgb(128, 0, 0, 0)
c_rojo_oscuro         = color.rgb(80, 0, 0, 0)
c_red_t               = color.new(color.red, 90)
c_amarillo            = color.rgb(255, 255, 0, 0)
noneColor             = color.new(color.white, 100)


//== Strategy
GRUPO_ESTRATEGIA = "Strategy"
ESTRATEGIA_vela_completa_fuera_hema = input.bool(title="Full candle must be outside the HEMA / Wicks can touch the HEMA but body must be out", defval=false, group=GRUPO_ESTRATEGIA)

//== Simple Moving Average (SMA)
GRUPO_SMA = "Simple Moving Average (SMA)"
len = input.int(150, minval=1, title="Length", group=GRUPO_SMA)
src = input(close, title="Source", group=GRUPO_SMA)
offset = input.int(title="Offset", defval=6, minval=-500, maxval=500, group=GRUPO_SMA)
sma = ta.sma(src, len)


//== Hull Estimate (HEMA) - Source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/ - © alexgrover
GRUPO_HEMA = "Hull Estimate (HEMA)"
length = input.int(title="Length", defval=50, minval=1, group=GRUPO_HEMA)
hema = 3 * ta.wma(close, length / 2) - 2 * ta.ema(close, length / 2)


//== HALFTREND - Copyright (c) 2021-present, Alex Orekhov (everget)
GRUPO_HT = "Halftrend"
amplitude = input(title='Amplitude', defval=1, group=GRUPO_HT)
channelDeviation = input(title='Channel Deviation', defval=2, group=GRUPO_HT)
showArrows = input(title='Show Arrows', defval=true, group=GRUPO_HT)
showChannels = input(title='Show Channels', defval=false, group=GRUPO_HT)

var int trend = 0
var int nextTrend = 0
var float maxLowPrice = nz(low[1], low)
var float minHighPrice = nz(high[1], high)

var float up = 0.0
var float down = 0.0
float atrHigh = 0.0
float atrLow = 0.0
float arrowUp = na
float arrowDown = na

atr2 = ta.atr(100) / 2
dev = channelDeviation * atr2

highPrice = high[math.abs(ta.highestbars(amplitude))]
lowPrice = low[math.abs(ta.lowestbars(amplitude))]
highma = ta.sma(high, amplitude)
lowma = ta.sma(low, amplitude)

if nextTrend == 1
    maxLowPrice := math.max(lowPrice, maxLowPrice)

    if highma < maxLowPrice and close < nz(low[1], low)
        trend := 1
        nextTrend := 0
        minHighPrice := highPrice
else
    minHighPrice := math.min(highPrice, minHighPrice)

    if lowma > minHighPrice and close > nz(high[1], high)
        trend := 0
        nextTrend := 1
        maxLowPrice := lowPrice

if trend == 0
    if not na(trend[1]) and trend[1] != 0
        up := na(down[1]) ? down : down[1]
        arrowUp := up - atr2
        arrowUp
    else
        up := na(up[1]) ? maxLowPrice : math.max(maxLowPrice, up[1])
        up
    atrHigh := up + dev
    atrLow := up - dev
    atrLow
else
    if not na(trend[1]) and
```