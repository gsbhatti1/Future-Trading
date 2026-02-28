``` pinescript
/*backtest
start: 2022-04-08 00:00:00
end: 2022-05-07 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © platsn

//@version=5
strategy("MACD Willy Strategy", overlay=true, pyramiding=1, initial_capital=10000) 

// ******************** Trade Period **************************************
startY = input(title='Start Year', defval=2011, group = "Trading window")
startM = input.int(title='Start Month', defval=1, minval=1, maxval=12, group = "Trading window")
startD = input.int(title='Start Day', defval=1, minval=1, maxval=31, group = "Trading window")
finishY = input(title='Finish Year', defval=2050, group = "Trading window")
finishM = input.int(title='Finish Month', defval=12, minval=1, maxval=12, group = "Trading window")
finishD = input.int(title='Finish Day', defval=31, minval=1, maxval=31, group = "Trading window")
//timestart = timestamp(startY, startM, startD, 00, 00)
//timefinish = timestamp(finishY, finishM, finishD, 23, 59)
// t1 = time(timeframe.period, "0945-1545:23456") 
// window = time >= timestart and time <= timefinish and t1 ? true : false 
// t2 = time(timeframe.period, "0930-1555:23456")
// window2 = time >= timestart and time <= timefinish and t2 ? true : false 

leverage = input.float(1, title="Leverage (if applicable)", step=0.1, group = "Trading Options")
reinvest = input.bool(defval=false,title="Reinvest profit", group = "Trading Options")
reinvest_percent = input.float(defval=20, title = "Reinvest percentage", group="Trading Options")
// entry_lookback = input.int(defval=10, title="Lookback period for entry condition", group = "Trading Options")

// -------------------------------------------- Data Source --------------------------------------------

src = input(title="Source", defval=close)

// ***************************************************************************************************** Daily ATR *****************************************************
atrlen = input.int(14, minval=1, title="ATR period", group = "Daily ATR")
iPercent = input.float(5, minval=1, maxval=100, step=0.1, title="% ATR to use for SL / PT", group = "Daily ATR")
 
percentage = iPercent * 0.01
datr = request.security(syminfo.tickerid, "1D", ta.rma(ta.tr, atrlen))
datrp = datr * percentage

// plot(datr,"Daily ATR")
// plot(datrp, "Daily % ATR")

//*********************************************************** VIX volatility index ****************************************

//VIX = request.security("VIX", timeframe.period, close)
//vix_thres = input.float(20.0, "VIX Threshold for entry", step=0.5, group="VIX Volatility Index")

// ************************************************ Volume ******************************************************

vol_len = input(50, 'Volume MA Period')
avg_vol = ta.sma(volume, vol_len)

//-------------------------------------------------------- Moving Average ------------------------------------

emalen1 = input.int(200, minval=1, title='EMA', group= "Moving Averages")
ema1 = ta.ema(src, emalen1)

// ------------------------------------------ MACD ------------------------------------------
// Getting inputs
fast_length = input(title="Fast Length", defval=12)
slow_length = input(title="Slow Length", defval=26)
signal_smoothing = input.int(9, minval=1, title="Signal Smoothing")
oscillator_matype = input.string("EMA", options=["EMA", "SMA"], title="Oscillator MA Type", group="Moving Averages")
signal_matype = input.string("EMA", options=["EMA", "SMA"], title="Signal Line MA Type", group="Moving Averages")

// Calculate MACD
[macd_line, signal_line, _] = ta.macd(src, fast_length, slow_length, signal_smoothing)

// ------------------------------------------ William %R ------------------------------------------
smoothed_r = input.int(34, minval=1, title="w_length")
fast_ma_william = ta.ema(ta.willr(src, smoothed_r), 9)
slow_ma_william = ta.sma(ta.willr(src, smoothed_r), 13)

// Plot
plot(macd_line, "MACD Line", color=color.rgb(41, 98, 255))
plot(signal_line, "Signal Line", color=color.rgb(255, 109, 0))
hline(0, "Zero Line")
plotshape(series=crossover(fast_ma_william, slow_ma_william), title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=crossunder(fast_ma_william, slow_ma_william), title="Short Exit", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Entry and exit conditions
long_condition = (close > ema1) or (macd_line > signal_line) or (fast_ma_william > slow_ma_william)
short_condition = (close < ema1) or (macd_line < signal_line) or (fast_ma_william < slow_ma_william)

// Execute long entry
if (long_condition and window)
    strategy.entry("Long", strategy.long)

// Execute short entry
if (short_condition and window)
    strategy.entry("Short", strategy.short)

// Exit conditions
exit_long = macd_line <= signal_line or fast_ma_william <= -20
exit_short = macd_line >= signal_line or fast_ma_william >= -80

// Execute long exit
if (exit_long and window)
    strategy.close("Long")

// Execute short exit
if (exit_short and window)
    strategy.close("Short")
```

This Pine Script translates the original Chinese document to English, maintaining all code blocks, numbers, and formatting as specified.