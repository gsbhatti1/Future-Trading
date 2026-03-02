> Name

Dual-Moving-Average-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy uses the combination of a fast moving average and a slow moving average to determine trend direction, generating trading signals when the fast line crosses above the slow line. This is part of a dual-moving-average trading system.

## Principles

The strategy employs a shorter fast moving average and a longer slow moving average.

The slow MA defines the main trend direction. Prices above the MA indicate an uptrend; prices below it suggest a downtrend.

During an uptrend, if the fast MA crosses above the slow MA, a long signal is generated; during a downtrend, if the fast MA crosses below the slow MA, a short signal is generated.

After generating a trading signal, trailing stops can optionally be enabled for continued tracking.

## Advantages

1. The combination of fast and slow MAs effectively identifies trends.
2. The fast MA produces sensitive trading signals.
3. The slow MA filters out noise to prevent false breakouts.
4. Various MA types such as EMA, DEMA can be used.
5. Trailing stop loss can be enabled.

## Risks and Mitigations

1. MAs may lag, causing delayed signals. More sensitive parameters can be tested.
2. Stop losses may be too tight, leading to premature exits. Adequate wiggle room should be allowed.
3. Volume is ignored, posing a risk of price manipulation. Volume confirmation can be added.
4. Indicator-only systems are prone to false signals. Additional confirmation is required.
5. Parameter optimization is difficult. Stepwise optimization or genetic algorithms can find optimal parameters.

## Enhancement Opportunities

1. Test different MA types and parameters for the best results.
2. Research adaptive MAs for better sensitivity.
3. Add other indicators or factors for signal filtering.
4. Build dynamic stop-loss mechanisms for more flexible stops.
5. Optimize money management strategies like dynamic position sizing with ATR.

## Summary

The strategy trades dual MA crossovers to identify trends, with trailing stops limiting risk. The logic is simple and clear but suffers from parameter selection challenges. Enhancements through optimization, filtering, and stop-loss strategies can improve robustness. It serves as a reasonable baseline trend-following system.

||

## Overview 

This strategy uses fast and slow moving averages to identify trend direction and generate signals when the fast MA crosses above the slow MA, creating a dual MA system.

## Principles

The strategy employs a shorter fast moving average and a longer slow moving average. 

The slow MA defines the main trend direction. Prices above the MA indicate an uptrend; prices below it suggest a downtrend.

During an uptrend, if the fast MA crosses above the slow MA, a long signal is generated. During a downtrend, if the fast MA crosses below the slow MA, a short signal is generated.

After generating a trading signal, trailing stops can optionally be enabled for continued tracking.

## Advantages

1. The combination of fast and slow MAs effectively identifies trends.
2. The fast MA produces sensitive trading signals.
3. The slow MA filters out noise to prevent false breakouts.
4. Various MA types such as EMA, DEMA can be used.
5. Trailing stop loss can be enabled.

## Risks and Mitigations

1. MAs may lag, causing delayed signals. More sensitive parameters can be tested.
2. Stop losses may be too tight, leading to premature exits. Adequate wiggle room should be allowed.
3. Volume is ignored, posing a risk of price manipulation. Volume confirmation can be added.
4. Indicator-only systems are prone to false signals. Additional confirmation is required.
5. Parameter optimization is difficult. Stepwise optimization or genetic algorithms can find optimal parameters.

## Enhancement Opportunities

1. Test different MA types and parameters for the best results.
2. Research adaptive MAs for better sensitivity.
3. Add other indicators or factors for signal filtering.
4. Build dynamic stop-loss mechanisms for more flexible stops.
5. Optimize money management strategies like dynamic position sizing with ATR.

## Summary

The strategy trades dual MA crossovers to identify trends, with trailing stops limiting risk. The logic is simple and clear but suffers from parameter selection challenges. Enhancements through optimization, filtering, and stop-loss strategies can improve robustness. It serves as a reasonable baseline trend-following system.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|long|
|v_input_2|true|short|
|v_input_3|false|stops|
|v_input_4|5|Stop, %|
|v_input_5|7|Type of Slow MA|
|v_input_6_close|0|Source of Slow MA: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_7|true|Use fast MA Filter|
|v_input_8|5|fast MA Period|
|v_input_9|20|slow MA Period|
|v_input_10|2|Bars Q|
|v_input_11|false|Need trend Background?|
|v_input_12|false|Need entry arrows?|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-08-18 00:00:00
end: 2023-09-17 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy(title = "Noro's Trend MAs Strategy v1.7", shorttitle = "Trend MAs str 1.7", overlay=true, default_qty_type = strategy.percent_of_equity, default_qty_value=100.0, pyramiding=0)

//Settings
needlong = input(true, "long")
needshort = input(true, "short")
needstops = input(false, "stops")
stoppercent = input(5, defval = 5, minval = 1, maxval = 50, title = "Stop, %")
type = input(7, defval = 7, minval = 1, maxval = 7, title = "Type of Slow MA")
src = input(close, defval = close, title = "Source of Slow MA")
usefastsma = input(true, "Use fast MA Filter")
fastlen = input(5, defval = 5, minval = 1, maxval = 50, title = "fast MA Period")
len = input(20, defval = 20, minval = 2, maxval = 200, title = "slow MA Period")
bars = input(2, defval = 2, minval = 0, maxval = 3, title = "Bars Q")
needbg = input(false, defval = false, title = "Need trend Background?")
needarr = input(false, defval = false, title = "Need entry arrows?")

fastsma = ema(src, fastlen)

//DEMA
dema = 2 * ema(src, len) - ema(ema(close, len), len)

//TEMA
xPrice = close
xEMA1 = ema(src, len)
xEMA2 = ema(xEMA1, len)
xEMA3 = ema(xEMA2, len)
tema = 3 * xEMA1 - 3 * xEMA2 + xEMA3

//KAMA
xvnoise = abs(src - src[1])
nfastend = 0.20
nslowend = 0.05
nsignal = abs(src - src[len])
nnoise = sum(xvnoise, len)
nefratio = iff(nnoise != 0, nsignal / nnoise, 0)
nsmooth = pow(nefratio * (nfastend - nslowend) + nslowend, 2) 
kama = nz(kama[1]) + nsmooth * (src - nz(kama[1]))

//PriceChannel
lasthigh = highest(src, len)
lastlow = lowest(src, len)
center = (lasthigh + lastlow) / 2

//Trend
ma = type == 1 ? sma(src, len) : type == 2 ? ema(src, len) : type == 3 ? vwma(src, len) : type == 4 ? dema : type == 5 ? tema : type == 6 ? kama : type == 7 ? center : 0
trend = low > ma and low[1] > ma[1] and low[2] > ma[2] ? 1 : 0
dn = trend == -1 and (high > fastsma or usefastsma == false) and greenbars == 1 ? 1 : 0

```