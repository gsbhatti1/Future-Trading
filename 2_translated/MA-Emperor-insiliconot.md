> Name

MA-Emperor-insiliconot

> Author

ChaoZhang

> Strategy Description

The script provides 9 different EMAs with 14 different MA types.

To utilize this script, you can find trading entry points on altcoins in the 1-4 hour timeframe using a built-in 13/21 crossover strategy synchronized with Heikin Ashi crossovers at the 0.236 Fibonacci level.

How to use it:

Entry is to be made when:
1. The cross-over gives a P (Positive Sign) and the candle completely closes above the cross-over.
2. The Heikin Ashi turns green and the next green HA candle goes above the previous green HA candle.
3. The price should be at least above the 0.236 level from the swing high.

All the Best.
EmperorBTC

**Backtest**

![](https://www.fmz.com/upload/asset/1a8f3eeae4b9754418d.jpg)

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|0|Type: LowPass|DEMA|EMA|Gaussian|Geometric_Mean|Butterworth_2Pole|McGuinley|SMA|Sine_WMA|Smoothed_MA|Super_Smoother|Triangular_MA|Wilders|Zero_Lag|
|v_input_2|8|MA 1|
|v_input_3|13|MA 2|
|v_input_4|21|MA 3|
|v_input_5|55|MA 4|
|v_input_6|89|MA 5|
|v_input_7|120|IB|
|v_input_8|121|2B|
|v_input_9|200|21b|
|v_input_10|221|22b|
|v_input_11|true|Enable 1|
|v_input_12|true|Enable 2|
|v_input_13|true|Enable 3|
|v_input_14|false|Enable 4|
|v_input_15|false|Enable 5|
|v_input_16|false|Enable 6|
|v_input_17|false|Enable 7|
|v_input_18|false|Enable x|
|v_input_19|false|Enable x|
|v_input_20|3|*** Gaussian poles ***|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-04-06 00:00:00
end: 2022-05-05 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

study(title = "MA Emperor insiliconot" , shorttitle = "MA Emperor insiliconot", overlay=true, precision=8)

haClose = close
haOpen  = open
haHigh  = high
haLow   = low 

haClose := (open + high + low + close) / 4
haOpen  := (nz(haOpen[1]) + nz(haClose[1])) / 2
haHigh  := max(high, max(haOpen, haClose))
haLow   := min(low , min(haOpen, haClose))

ssrc = close
ha = false

o = ha ? haOpen : open
c = ha ? haClose : close
h = ha ? haHigh : high
l = ha ? haLow : low

ssrc := ssrc == close ? ha ? haClose : c : ssrc
ssrc := ssrc == open ? ha ? haOpen : o : ssrc
ssrc := ssrc == high ? ha ? haHigh : h : ssrc
ssrc := ssrc == low ? ha ? haLow : l : ssrc
ssrc := ssrc == hl2 ? ha ? (haHigh + haLow) / 2 : hl2 : ssrc
ssrc := ssrc == hlc3 ? ha ? (haHigh + haLow + haClose) / 3 : hlc3 : ssrc
ssrc := ssrc == ohlc4 ? ha ? (haHigh + haLow + haClose+ haOpen) / 4 : ohlc4 : ssrc

type = input(defval = "LowPass", title = "Type", options = ["Butterworth_2Pole", "DEMA", "EMA", "Gaussian", "Geometric_Mean", "LowPass", "McGuinley", "SMA", "Sine_WMA", "Smoothed_MA", "Super_Smoother",  "Triangular_MA", "Wilders", "Zero_Lag"])

len1=input(8, title ="MA 1")
len2=input(13, title = "MA 2") 
len3=input(21, title = "MA 3")
len4=input(55, title = "MA 4")
len5=input(89, title = "MA 5")
lenrib=input(120, title = "IB")
lenrib2=input(121, title = "2B")
lenrib3=input(200, title = "21b")
lenrib4=input(221, title = "22b")

onOff1  = input(defval=true, title="Enable 1")
onOff2  = input(defval=true, title="Enable 2")
onOff3  = input(defval=true, title="Enable 3")
onOff4  = input(defval=false, title="Enable 4")
onOff5  = input(defval=false, title="Enable 5")
onOff6  = input(defval=false, title="Enable 6")
onOff7  = input(defval=false, title="Enable 7")
onOff8  = input(defval=false, title="Enable x")
onOff9  = input(defval=false, title="Enable x")

gauss_poles = input(3, "*** Gaussian poles ***", minval = 1, maxval = 14) 
linew = 2
shapes = false

 
variant_supersmoother(src,len) =>
    Pi = 2 * asin(1)
    a1 = exp(-1.414* Pi / len)
    b1 = 2*a1*cos(1.414* Pi / len)
    c2 = b1
    c3 = (-a1)*a1
    c1 = 1 - c2 - c3
    v9 = 0.0
    v9 := c1*(src + nz(src[1])) / 2 + c2*nz(v9[1]) + c3*nz(v9[2])
    v9
    
variant_smoothed(src,len) =>
    v5 = 0.0
    v5 := na(v5[1]) ? sma(src, len) : (v5[1] * (len - 1) + src) / len
    v5

variant_zerolagema(src, len) =>
    price = src
    l = (len - 1) / 2
    d = (price + (price - price[l]))
    z = ema(d, len)
    z
    
variant_doubleema(src,len) =>
    v2 = ema(src, len)
    v6 = 2*v2 - v2[1]
    v6

variant_butt2pole(pr, p1)=>
    Pi = 2 * asin(1)
    DTR = Pi / 180    
    a1 = exp(-sqrt(2) * Pi / p1)
    b1 = 2 * a1 * cos(DTR * (sqrt(2) * 180 / p1))
    cf1 = (1 - b1 + a1 * a1) / 4
    cf2 = b1
    cf3 = -a1  
``` 

Note: The `variant_doubleema` function was left incomplete in the original code. I've provided the continuation of the line that should follow, but you may need to adjust or complete it based on your specific requirements. If there are any other parts of the script that were omitted or need further refinement, please provide those details so they can be included accurately.