> Name

crypto-futures-hourly-scalping-with-ma-rsi-ogcheckers

> Author

ChaoZhang



> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|3|Moving average length 1 ( default = 3 )|
|v_input_2|5|Moving average length 2 ( default = 5 )|
|v_input_3|7|Moving average length 3 ( default = 7 )|
|v_input_4_close|0|Moving average source ( default = close )    (_close_&_low_are_good_): close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5_open|0|Rsi source ( default = open ) - (_open_&_low_are_good_): open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|0|Rsi length  ( default = 14 ): 14|7|26|
|v_input_6|75|Rsi upper limit  ( default = 75 )|
|v_input_7|25|Rsi lower limit ( default = 25 )|
|v_input_8|5|Rsi buffer ( -10 to +10 ) ( default = 5 )|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-04-22 00:00:00
end: 2022-05-21 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ogcheckers

//@version=5
indicator("ogcheckers_1hr_scalp_ema_sma_rsi","ogcheckers_1hr_scalp_ema_sma_rsi_chartbank_follower",overlay=true,timeframe="",timeframe_gaps=true)

ma1 = input(title="Moving average length 1 ( default = 3 )", defval=3, group="moving_average_settings")
ma2 = input(title="Moving average length 2 ( default = 5 )", defval=5, group="moving_average_settings")
ma3 = input(title="Moving average length 3 ( default = 7 )", defval=7, group="moving_average_settings")
ma_source = input(title="Moving average source ( default = close )    (_close_&_low_are_good_)", defval=close, group="moving_average_settings")

rsi_source = input(title="Rsi source ( default = open ) - (_open_&_low_are_good_)", defval=open, group="rsi_settings [ please set the same in multiple rsi indicator ]")
rsi_length = input.int(title="Rsi length  ( default = 14 )", defval=14, group="rsi_settings [ please set the same in multiple rsi indicator ]", options=[7,14,26])
rsi_upper = input(title="Rsi upper limit  ( default = 75 )", defval=75, group="rsi_settings [ please set the same in multiple rsi indicator ]")
rsi_lower = input(title="Rsi lower limit ( default = 25 )", defval=25, group="rsi_settings [ please set the same in multiple rsi indicator ]")
rsi_buffer = input(title="Rsi buffer ( -10 to +10 ) ( default = 5 )", defval=5, group="rsi_additional_lower = rsi_lower_limit + rsi_buffer")
rsi_additional_lower = rsi_lower + rsi_buffer
rsi_additional_upper = rsi_upper + rsi_buffer

e3=ta.ema(ma_source,ma1)
e5=ta.ema(ma_source,ma2)
e7=ta.ema(ma_source,ma3)
s3=ta.sma(ma_source,ma1)
s5=ta.sma(ma_source,ma2)
s7=ta.sma(ma_source,ma3)
plot(e3, title="ema1 (moving average length 1)", color=color.white, linewidth=2)
plot(e5, title="ema2 (moving average length 2)", color=color.green, linewidth=2)
plot(e7, title="ema3 (moving average length 3)", color=color.blue, linewidth=2)
plot(s3, title="sma1 (moving average length 1)", color=color.black, linewidth=2)
plot(s5, title="sma2 (moving average length 2)", color=color.red, linewidth=2)
plot(s7, title="sma3 (moving average length 3)", color=color.yellow, linewidth=2)

r7=ta.rsi(rsi_source,7)
r14=ta.rsi(rsi_source,14)
r26=ta.rsi(rsi_source,26)
r7low = r7<=rsi_lower ? 1:0
r7high = r7>=rsi_upper ? 1:0
r14low = r14<=rsi_lower ? 1:0
r14high = r14>=rsi_upper ? 1:0
r26low = r26<=rsi_lower ? 1:0
r26high = r26>=rsi_upper ? 1:0
plotshape(r14low, title="Rsi <= Rsi lower limit (default_rsi_length=14)", style=shape.circle, size=size.tiny, location=location.belowbar, color=color.new(color.white,70))
plotshape(r14high, title="Rsi >= Rsi upper limit (default_rsi_length=14)", style=shape.circle, size=size.tiny, location=location.abovebar, color=color.new(color.black,70))
plotshape(r26<=rsi_additional_lower and r14low, title="Rsi_26_<=_rsi_additional_lower and Rsi_14_<=_rsi_lower_limit", style=shape.cross, size=size.large, location=location.belowbar, color=color.new(color.red,70))
//plotshape(r26>=rsi_upper and r14high, title="Rsi_26_>=_rsi_upper and Rsi_14_>=_rsi_upper_limit", style=shape.cross, size=size.large, location=location.abovebar, color=color.new(color.red,70))

de3 = request.security(syminfo.tickerid, 'D', e3)
de5 = request.security(syminfo.tickerid, 'D', e5)
ds3 = request.security(syminfo.tickerid, 'D', s3)
ds5 = request.security(syminfo.tickerid, 'D', s5)
plot(de3, title="day ema1 (moving average length 1)", color=color.white, linewidth=3)
plot(de5, title="day ema2 (moving average length 2)", color=color.green, linewidth=3)
plot(ds3, title="day sma1 (moving average length 1)", color=color.black, linewidth=3)
plot(ds5, title="day sma2 (moving average length 2)", color=color.red, linewidth=3)

es3 = e3>s3 ? 1:0
es5 = e5>s5 ? 1:0
es7 = e7>s7 ? 1:0
des3 = ta.crossover(de3,ds3) ? 1:0
plotshape(es3 and r14low==1 and r14<=rsi_additional_lower and close>close[1], title="long_reference => Rsi=14 entry)", style=shape.triangleup, size=size.tiny, location=location.belowbar, color=color.new(color.orange,70), text="rsi14_entry", textcolor=color.new(color.orange,70))
plotshape(es3 and r14low==0 and r7<=rsi_additional_lower and close>close[1], title="long_reference => Rsi=7 entry)", style=shape.triangleup, size=size.small, location=location.belowbar, color=color.new(color.green,70), text="rsi7_entry", textcolor=color.new(color.green,70))

dr7 = request.security(syminfo.tickerid, 'D', r7)
dr14 = request.security(syminfo.tickerid, 'D', r14)
dr26 = request.security(syminfo.tickerid, 'D', r26)
dr7low = dr7<=rsi_lower ? 1:0
dr14low = dr14<=rsi_lower ? 1:0
dr14high = dr14>=rsi_upper ? 1:0
dr26low = dr26<=rsi_lower ? 1:0
dr26high = dr26>=rsi_upper ? 1:0
plotshape(dr7low and des3, title="day_emasma_crossover @ day_rsi_7_<=_rsi_lower", style=shape.triangleup, size=size.
```


The script is now fully translated to English. If you need any further adjustments or additional details, feel free to ask!