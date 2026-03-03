> Name

MACD-based-Dual-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a18abbf1dd0377e5ef.png)
[trans]

## Overview

This strategy implements a dual trading strategy based on the MACD indicator. It can go long when there is a golden cross on the MACD and go short when there is a death cross, with additional filters based on other indicators to eliminate some invalid signals.

## Strategy Principle 

The core of this strategy is utilizing the MACD indicator to realize dual-directional trading. Specifically, it calculates the fast moving average, slow moving average, and MACD signal line. When the fast moving average crosses above the slow moving average, a golden cross is generated for going long. When the fast moving average crosses below the slow moving average, a death cross is generated for going short.

To filter out some invalid signals, the strategy also sets a ±30 range as a filter, so that trade signals are only triggered when the MACD histogram exceeds this range. In addition, when closing positions, it also judges the direction of the MACD histogram - positions are closed only when the directions of two successive histogram bars change.

## Advantages

- The MACD indicator is used as the main trading signal, which is sensitive to price movements in both directions.
- Added filters help eliminate some invalid signals.
- The two-bar directional logic for closing positions avoids some false breakouts to some extent.

## Risks

- The MACD indicator tends to generate frequent trade signals, leading to high trading frequency.
- Relying solely on one indicator makes the strategy vulnerable to signal delays and potential losses.
- The closing logic based on histogram direction is not rigorous enough, risks missing some signals.

## Optimization Directions

- Consider combining with other indicators for signal confirmation, such as KDJ, Bollinger Bands, etc.
- Research more advanced indicators to replace MACD, such as KD.
- Optimize the closing logic by setting stop loss and take profit levels to control single trade losses.

## Conclusion

In summary, this is a basically feasible dual directional trading strategy. It utilizes the advantages of the MACD indicator and also adds some filters to control signal quality. However, the MACD itself has some issues as well. Further testing and optimization in live trading are still needed to make the strategy more reliable. Overall speaking, this strategy lays the foundation for dual-directional trading strategies, and can be further optimized incrementally to become a powerful quantitative trading strategy.

||


## Overview

This strategy implements a dual trading strategy based on the MACD indicator. It can go long when there is a golden cross on the MACD and go short when there is a death cross, with additional filters based on other indicators to eliminate some invalid signals.

## Strategy Principle 

The core of this strategy is utilizing the MACD indicator to realize dual-directional trading. Specifically, it calculates the fast moving average, slow moving average, and MACD signal line. When the fast moving average crosses above the slow moving average, a golden cross is generated for going long. When the fast moving average crosses below the slow moving average, a death cross is generated for going short.

To filter out some invalid signals, the strategy also sets a ±30 range as a filter, so that trade signals are only triggered when the MACD histogram exceeds this range. In addition, when closing positions, it also judges the direction of the MACD histogram - positions are closed only when the directions of two successive histogram bars change.

## Advantages

- The MACD indicator is used as the main trading signal, which is sensitive to price movements in both directions.
- Added filters help eliminate some invalid signals.
- The two-bar directional logic for closing positions avoids some false breakouts to some extent.

## Risks

- The MACD indicator tends to generate frequent trade signals, leading to high trading frequency.
- Relying solely on one indicator makes the strategy vulnerable to signal delays and potential losses.
- The closing logic based on histogram direction is not rigorous enough, risks missing some signals.

## Optimization Directions

- Consider combining with other indicators for signal confirmation, such as KDJ, Bollinger Bands, etc.
- Research more advanced indicators to replace MACD, such as KD.
- Optimize the closing logic by setting stop loss and take profit levels to control single trade losses.

## Conclusion

In summary, this is a basically feasible dual directional trading strategy. It utilizes the advantages of the MACD indicator and also adds some filters to control signal quality. However, the MACD itself has some issues as well. Further testing and optimization in live trading are still needed to make the strategy more reliable. Overall speaking, this strategy lays the foundation for dual-directional trading strategies, and can be further optimized incrementally to become a powerful quantitative trading strategy.

[/trans]]

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
|v_input_8|12|fastLength|
|v_input_9|26|slowLength|
|v_input_10|9|signalLength|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-30 00:00:00
end: 2023-12-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

// Created by user ChrisMoody updated 4-10-2014
// Regular MACD Indicator with Histogram that plots 4 Colors Based on Direction Above and Below the Zero Line
// Update allows Check Box Options, Show MacD & Signal Line, Show Change In color of MacD Line based on cross of Signal Line.
// Show Dots at Cross of MacD and Signal Line, Histogram can show 4 colors or 1, Turn on and off Histogram.
// Special Thanks to that incredible person in Tech Support whoem I won't say you r name so you don't get bombarded with emails
// Note the feature Tech Support showed me on how to set the default timeframe of the indicator to the chart Timeframe, but also allow you to choose a different timeframe.
// By the way I fully disclose that I completely STOLE the Dots at the MAcd Cross from "TheLark"

strategy("MACD Strategy", overlay=false)
// study(title="CM_MacD_Ult_MTF", shorttitle="CM_Ult_MacD_MTF")
source = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input(title="Use Different Timeframe? Uncheck Box Above", defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")

res = useCurrentRes ? timeframe.period : resCustom

fastLength = input(12, minval=1), slowLength=input(26,minval=1)
signalLength=input(9,minval=1)

fastMA = ema(source, fastLength)
slowMA = ema(source, slowLength)

macd = fastMA - slowMA
signal = sma(macd, signalLength)
hist = macd - signal

outMacD = request.security(syminfo.tickerid, res, macd)
outSignal = request.security(syminfo.tickerid, res, signal)
outHist = request.security(syminfo.tickerid, res,