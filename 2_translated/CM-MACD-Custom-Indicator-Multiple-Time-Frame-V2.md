```pinescript
/*backtest
start: 2022-04-19 00:00:00
end: 2022-05-18 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//------New V2 Update 07-28-2021----------
//Thanks to @SKTennis for help in Updating code to V2
//Added Groups to Settings Pane.
//Added Color Plots to Settings Pane
//Switched MTF Logic to turn ON/OFF automatically w/ TradingView's Built-in Feature
//Updated Color Transparency plots to work in future update
//Added Ability to Turn ON/OFF Show MacD & Signal Line
//Added Ability to Turn ON/OFF Show Histogram
//Added Ability to Change MACD Line Colors Based on Trend
//Added Ability to Highlight Price Bars Based on Trend
//Added Alerts to Settings Pane.
//Customized how Alerts work.  Must keep Checked in Settings Pane, and...
//When you go to Alerts Panel, Change Symbol to Indicator (CM_Ult_MacD_MTF_V2)
//Customized Alerts to Show Symbol, TimeFrame, Closing Price, MACD Crosses Up & MACD Crosses Down Signals in Alert 
//Alerts are Pre-Set to only Alert on Bar Close

//------New V2.1 Update 08-03-2021----------
//Added back in ability to show Dots when MACD Crosses.
//Added Ability to Change Plot Widths in Settings Pane
//Added in Alert Feature where Cross Up if above 0 or cross down if below 0 (OFF By Default) user Request. @creid58
//FIXED - Plot Orders to Default what Plots are on top of each other
//FIXED - Two of the histogram colors were backwards

//------New V2.1 Update 12-07-2021----------
//Updated to PineScript V5

//------Minor Update 02-16-2022----------
//Per user request...Increased the Maxval for Signal Smoothing
//Next Add in Plot Types to Settings Pane.
//Next Add in more Moving Average types.
//See Video for Detailed Overview

//@version=5
indicator(title="_CM_MacD_Ult_MTF_V2.1", shorttitle="_CM_Ult_MacD_MTF_V2.1")
//Plot Inputs
res           = input.timeframe("",  "Indicator TimeFrame")
fast_length   = input.int(title="Fast Length", defval=12)
slow_length   = input.int(title="Slow Length", defval=26)
src           = input.source(title="Source", defval=close)
signal_length = input.int(title="Signal Smoothing", minval = 1, maxval = 999, defval = 5)
sma_source    = input.string(title="Oscillator MA Type", defval="EMA", options=["SMA", "EMA"])
sma_signal    = input.string(title="Signal Line MA Type", defval="EMA", options=["SMA", "EMA"])
// Show Plots T/F
show_macd     = input.bool(true, title="Show MACD Lines", group="Show Plots?")
show_macd_LW  = input.int(3, minval=0, maxval=5, title="MACD Width", group="Show Plots?")
show_signal_LW= input.int(2, minval=0, maxval=5, title="Signal Width", group="Show Plots?")
show_Hist     = input.bool(true, title="Show Histogram", group="Show Plots?")
show_hist_LW  = input.int(5, minval=0, maxval=5, title="-- Width", group="Show Plots?")
show_trend    = input.bool(true, title="Show MACD Lines w/ Trend Color", group="Show Plots?")
show_HB       = input.bool(false, title="Show Highlight Price Bars", group="Show Plots?")
show_cross    = input.bool(false, title="Show BackGround on Cross", group="Show Plots?")
show_dots     = input.bool(true, title="Show Circle on Cross", group="Show Plots?")
show_dots_LW  = input.int(5, minval=0, maxval=5, title="-- Width", group="Show Plots?")

// MACD Lines colors
col_macd      = input(#FF6D00, "MACD Line  ",  group="Color Settings")
col_signal    = input(#2962FF, "Signal Line  ",  group="Color Settings")
col_trnd_Up   = input(#4BAF4F, "Trend Up      ", group="Color Settings")
col_trnd_Down = input(#B71D1C, "Trend Down    ", group="Color Settings")
col_hist_Above= input(#26A69A, "Above   Grow",  group="Histogram Colors")
col_hist_Below= input(#FF5252, "Below Grow",    group="Histogram Colors")
// Alerts
alert1 = input.bool(true, title="MACD Cross Up", group="Alerts")
alert2 = input.bool(true, title="MACD Cross Down", group="Alerts")
alert3 = input.bool(true, title="MACD Cross Up & > 0", group="Alerts")
alert4 = input.bool(true, title="MACD Cross Down & < 0", group="Alerts")
```