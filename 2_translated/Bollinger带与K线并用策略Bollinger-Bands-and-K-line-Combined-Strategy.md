> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|length|
|v_input_2_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|2|StdDev|
|v_input_4|false|Offset|
|v_input_5|true|Start Date|
|v_input_6|true|Start Month|
|v_input_7|2018|Start Year|
|v_input_8|true|End Date|
|v_input_9|11|End Month|
|v_input_10|2030|End Year|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-07 00:00:00
end: 2024-01-14 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("BB策略", overlay=true)
length = input(20, minval=1)
src = input(close, title="Source")
mult = input(2.0, minval=0.001, maxval=50, title="StdDev")
basis = sma(src, length)
dev = mult * stdev(src, length)
upper = basis + dev
lower = basis - dev
offset = input(0, "Offset", type=input.integer, minval=-500, maxval=500)
plot(basis, "Basis", color=#872323, offset=offset)
p1 = plot(upper, "Upper", color=color.teal, offset=offset)
p2 = plot(lower, "Lower", color=color.teal, offset=offset)
fill(p1, p2, title="Background", color=#198787, transp=95)
diff = upper - lower
//plot(upper * 0.9985, "Upper", color=color.white, offset=offset)
//plot(lower * 1.0015, "Lower", color=color.white, offset=offset)

// Engulfing Candles
openBarPrevious = open[1]
closeBarPrevious = close[1]
openBarCurrent = open
closeBarCurrent = close
bullishEngulfing = openBarCurrent <= closeBarPrevious and openBarCurrent < openBarPrevious and 
   closeBarCurrent > openBarPrevious
bearishEngulfing = openBarCurrent >= closeBarPrevious and openBarCurrent > openBarPrevious and 
   closeBarCurrent < openBarPrevious

// Long Upper Shadow - Bearish
C_Len = 14 // EMA depth for bodyAvg
C_ShadowPercent = 5.0 // Size of shadows
C_ShadowEqualsPercent = 100.0
C_DojiBodyPercent = 5.0
C_Factor = 2.0 // Shows the number of times the shadow dominates the candlestick body
C_BodyHi = max(close, open)
C_BodyLo = min(close, open)
C_Body = 
```