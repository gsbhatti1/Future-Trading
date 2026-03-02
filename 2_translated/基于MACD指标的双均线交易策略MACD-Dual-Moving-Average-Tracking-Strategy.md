> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Use Current Chart Resolution?|
|v_input_2|60|Use Different Timeframe? Uncheck Box Above|
|v_input_3|true|Show MacD & Signal Line? Also Turn Off Dots Below|
|v_input_4|true|Show Dots When MacD Crosses Signal Line?|
|v_input_5|true|Show Histogram?|
|v_input_6|true|Change MacD Line Color-Signal Line Cross?|
|v_input_7|true|MacD Histogram 4 Colors?|
|v_input_8|true|Vender cuando closing price < previous day low?|
|v_input_9|5|fastLength|
|v_input_10|8|slowLength|
|v_input_11|3|signalLength|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-10 00:00:00
end: 2023-12-13 02:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
// macd/cam v1 strategizing Chris Moody Macd indicator https://www.tradingview.com/script/OQx7vju0-MacD-Custom-Indicator-Multiple-Time-Frame-All-Available-Options/
// macd/cam v2 changing to macd 5,8,3
// macd/cam v2.1 
//      Sell when lower than previous day low. 
//      Initial capital of $2k. Buy/sell quantity of initial capital / close price
//      Quitar short action
//      Note: custom 1-week resolution seems to put AMD at 80% profitable

strategy(title="MACD/CAM 2.1", shorttitle="MACD/CAM 2.1") //
source = close
//get inputs from options
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input(title="Use Different Timeframe? Uncheck Box Above", defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")
venderLowerPrev = input(true,title="Vender cuando closing price < previous day low?")

res = useCurrentRes ? timeframe.period : resCustom

fastLength = input(5, minval=1), slowLength=input(8,minval=1)
signalLength=input(3,minval=1)

// find exponential moving average of price as x and fastLength var as y
fastMA = ema(source, fastLength)
slowMA = ema(source, slowLength)

macd = fastMA - slowMA
// simple moving average
signal = sma(macd, signalLength)
hist = macd - signal

outMacD = request.security(syminfo.tickerid, res, macd)
outSignal = request.security(syminfo.tickerid, res, signal)
outHist = request.security(syminfo.tickerid, res, hist)

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0

//MacD Color Definitions
macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? aqua : histA_IsDown ? blue : histB_IsDown ? red : histB_IsUp ? maroon :yellow :gray
macd_color = macd_colorChange ? macd_IsAbove ? lime : red : red
signal_color = macd_colorChange ? macd_IsAbove ? yellow : yellow : lime

circleYPosition = outSignal
 
plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=line)
```