``` pinescript
/*backtest
start: 2022-04-12 00:00:00
end: 2022-05-11 23:59:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5


// Original Script > @DonovanWall

// Previous Version > @guikroth
// Ultimate Oscillator > @PineCoders

// Updated by > @jwelmac


//////////////////////////////////////////////////////////////////////////
// Range Filter x 2, EMA and UO
//////////////////////////////////////////////////////////////////////////


indicator(title='FTL - Range Filter X2 + EMA + UO', overlay=true)

// Groups

string groupLeadingRange = "Leading Range Filter"
string groupTriggerRange = "Trigger Range Filter"
string groupEMA = "EMA"
string groupUO = "Ultimate Oscillator (UO)"
string GROUP_BUY_OPTIONS = "Buy Options"
string GROUP_SELL_OPTIONS = "Sell Options"


//-------  *********  --------  *********  ---------
// Range Filter (Leader) {

// Source
src = input(defval=hl2, title='Source', group=groupLeadingRange)

// Sampling Period
per = input.int(defval=30, minval=1, title='Sampling Period', group=groupLeadingRange)

// Range Multiplier
mult = input.float(defval=2.6, minval=0.1, title='Range Multiplier', group=groupLeadingRange)

// Smooth Average Range {
smoothrng(x, t, m) =>
    wper = t * 2 - 1
    avrng = ta.ema(math.abs(x - x[1]), t)
    _smoothrng = ta.ema(avrng, wper) * m
    _smoothrng
// }
smrng = smoothrng(src, per, mult)

// Range Filter {
rngfilter(x, r) =>
    rngfilt = x
    rngfilt := x > nz(rngfilt[1]) ? x - r < nz(rngfilt[1]) ? nz(rngfilt[1]) : x - r : x + r > nz(rngfilt[1]) ? nz(rngfilt[1]) : x + r
    rngfilt
//}
filt = rngfilter(src, smrng)

// Filter Direction

upward = 0.0
upward := filt > filt[1] ? nz(upward[1]) + 1 : filt < filt[1] ? 0 : nz(upward[1])

downward = 0.0
downward := filt < filt[1] ? nz(downward[1]) + 1 : filt > filt[1] ? 0 : nz(downward[1])


// Colors

filtcolor = upward > 0 ? color.lime : downward > 0 ? color.red : color.orange

filtplot = plot(filt, color=filtcolor, linewidth=1, title='Range Filter (Leader)')

// }
//-------  *********  --------  *********  ---------

//-------  *********  --------  *********  ---------
// Range Filter (Trigger){
// Source
src2 = input(defval=ohlc4, title='Source', group=groupTriggerRange)

// Sampling Period
// Settings for 1min chart, US 100.

per2 = input.int(defval=48, minval=1, title='Sampling Period', group=groupTriggerRange)

// Range Multiplier

mult2 = input.float(defval=3.4, minval=0.1, title='Range Multiplier', group=groupTriggerRange)

// Smooth Average Range

smrng2 = smoothrng(src2, per2, mult2)

// Range Filter

rngfilt2(x, r) =>
    rngfilt = x
    rngfilt := x > nz(rngfilt[1]) ? x - r < nz(rngfilt[1]) ? nz(rngfilt[1]) : x - r : x + r > nz(rngfilt[1]) ? nz(rngfilt[1]) : x + r
    rngfilt
filt2 = rngfilt2(src2, smrng2)

// Filter Direction

upward2 = 0.0
upward2 := filt2 > filt2[1] ? nz(upward2[1]) + 1 : filt2 < filt2[1] ? 0 : nz(upward2[1])
downward2 = 0.0
downward2 := filt2 < filt2[1] ? nz(downward2[1]) + 1 : filt2 > filt2[1] ? 0 : nz(downward2[1])

// Colors

filtcolor2 = upward2 > 0 ? color.lime : downward2 > 0 ? color.red : color.orange

filtplot2 = plot(filt2, color=filtcolor2, linewidth=3, title='Range Filter (Trigger)')

barcolor = src2 > filt2 and upward2 > 0
   ? color.green 
   : src2 < filt2 and downward2 > 0 
     ? color.red 
     : color.rgb(120, 123, 134)
// Bar Color
//barcolor(barcolor)

// }
//-------  *********  --------  *********  ---------


//-------  *********  --------  *********  ---------
// Default EMA 144 {
len4 = input.int(144, minval=1, title='Length', group=groupEMA)
src4 = input(close, title='Source')
ema = ta.ema(src4, len4)

// UO
fast_length = input.int(defval=7, title='Fast Length', group=groupUO)
middle_length = input.int(defval=14, title='Middle Length', group=groupUO)
slow_length = input.int(defval=28, title='Slow Length', group=groupUO)
uoa = ta.uo(fast_length, middle_length, slow_length)

// Buy/Sell Options
buy_overbought_value = input.float(defval=60.0, minval=0.0, maxval=100.0, title='UO Overbought Value', group=GROUP_BUY_OPTIONS)
show_buy_only_when_not_overbought = input.bool(defval=true, title='Show BUY only when not overbought (UO)', group=GROUP_BUY_OPTIONS)
show_buy_only_above_ema = input.bool(defval=true, title='Show BUY only above the EMA', group=GROUP_BUY_OPTIONS)

sell_oversold_value = input.float(defval=40.0, minval=0.0, maxval=100.0, title='UO Oversold Value', group=GROUP_SELL_OPTIONS)
show_sell_only_when_not_oversold = input.bool(defval=true, title='Show SELL only when not oversold (UO)', group=GROUP_SELL_OPTIONS)
show_sell_only_below_ema = input.bool(defval=true, title='Show SELL only below the EMA', group=GROUP_SELL_OPTIONS)

// Buy/Sell Conditions
buy_condition = show_buy_only_when_not_overbought and uoa < buy_overbought_value and (show_buy_only_above_ema ? ema > src4 : true)
sell_condition = show_sell_only_when_not_oversold and uoa > sell_oversold_value and (show_sell_only_below_ema ? ema < src4 : true)

// Plot Buy/Sell Signals
plotshape(series=buy_condition, title='Buy Signal', location=location.belowbar, color=color.green, style=shape.labelup)
plotshape(series=sell_condition, title='Sell Signal', location=location.abovebar, color=color.red, style=shape.labeldown)

// }
```