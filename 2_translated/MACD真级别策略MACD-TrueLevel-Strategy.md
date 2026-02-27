> Name

MACD TrueLevel Strategy MACD-TrueLevel-Strategy

> Author

ChaoZhang

> Strategy Description

<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

## Overview

The MACD TrueLevel strategy uses the MACD indicator and TrueLevel bands to determine buy and sell signals. It adds TrueLevel bands on top of MACD to more accurately locate the start and end of trends.

## Principle

The strategy first calculates the MACD indicator, then computes 14 TrueLevel bands of different periods. The TrueLevel bands are calculated based on the linear regression line and standard deviation of prices over different length periods. It then picks the highest upper band and lowest lower band for breakout signals.

Specifically, the entry signal is a MACD line crossover above the signal line, or price breakout above the selected TrueLevel lower band. The exit signal is a MACD line crossover below the signal line, or price breakout below the selected TrueLevel upper band.

The advantage of using TrueLevel bands is that it combines the trend direction and volatility range to more precisely determine the start and end of trends. Compared to just MACD, adding TrueLevel band filter can reduce false signals.

## Advantage Analysis

1. Using MACD judges trend direction effectively and tracks trends well.
2. Adding TrueLevel bands can filter false breakouts and confirm trends. TrueLevel bands consider both trend and volatility, making the judgment more accurate.
3. TrueLevel bands include multiple periods, judging trend changes comprehensively.
4. Adjustable TrueLevel band parameters fit different market environments.
5. Support long and short positions to fully capture trend opportunities.

## Risk Analysis

1. MACD alone may generate more false signals, needing TrueLevel filter.
2. Improper TrueLevel band parameter setting may cause missed entries or exits. Parameters need adjustment based on markets.
3. Long and short positions require sufficient capital support, otherwise may cause margin call.
4. Breakout trading itself has the risk of being stopped out, requiring timely stop loss.
5. Any indicator strategy has the risk of not working well on high volatile products like commodities and crypto.

## Optimization Directions

1. Test more period parameters to find optimal values for the market.
2. Add stop loss strategy to reduce loss risk.
3. Add other indicator filters like volume, KDJ etc. to reduce false breakouts.
4. Optimize entry points like breaking previous highs/lows to improve profit rate.
5. Add machine learning models to judge trend probability, reducing manual parameter tuning.

## Summary

The MACD TrueLevel strategy integrates trend and range analysis. It adds TrueLevel bands on top of MACD to more accurately locate the start and end of trends compared to just MACD. It can effectively filter false signals and catch trends. There are still risks that need parameter and stop loss optimization. Overall, it suits trend trading and steadily catches market trends over the medium to long term.

|||

## Overview

The MACD TrueLevel strategy uses the MACD indicator and TrueLevel bands to determine buy and sell signals. It adds TrueLevel bands on top of MACD to more accurately locate the start and end of trends.

## Principle

First, calculate the MACD indicator. Then compute 14 TrueLevel bands for different periods. The TrueLevel bands are calculated based on the linear regression line and standard deviation over different length periods. Pick the highest upper band and lowest lower band for breakout signals.

Specifically, the entry signal is a MACD line crossover above the signal line, or price breakout above the selected TrueLevel lower band. The exit signal is a MACD line crossover below the signal line, or price breakout below the selected TrueLevel upper band.

The advantage of using TrueLevel bands is that it combines trend direction and volatility range to more precisely determine the start and end of trends. Compared to just MACD, adding TrueLevel band filter can reduce false signals.

## Advantage Analysis

1. Using MACD judges trend direction effectively and tracks trends well.
2. Adding TrueLevel bands can filter false breakouts and confirm trends. TrueLevel bands consider both trend and volatility, making the judgment more accurate.
3. TrueLevel bands include multiple periods, judging trend changes comprehensively.
4. Adjustable TrueLevel band parameters fit different market environments.
5. Support long and short positions to fully capture trend opportunities.

## Risk Analysis

1. MACD alone may generate more false signals, needing TrueLevel filter.
2. Improper TrueLevel band parameter setting may cause missed entries or exits. Parameters need adjustment based on markets.
3. Long and short positions require sufficient capital support, otherwise may cause margin call.
4. Breakout trading itself has the risk of being stopped out, requiring timely stop loss.
5. Any indicator strategy has the risk of not working well on high volatile products like commodities and crypto.

## Optimization Directions

1. Test more period parameters to find optimal values for the market.
2. Add stop loss strategy to reduce loss risk.
3. Add other indicator filters like volume, KDJ etc. to reduce false breakouts.
4. Optimize entry points like breaking previous highs/lows to improve profit rate.
5. Add machine learning models to judge trend probability, reducing manual parameter tuning.

## Summary

The MACD TrueLevel strategy integrates trend and range analysis. It adds TrueLevel bands on top of MACD to more accurately locate the start and end of trends compared to just MACD. It can effectively filter false signals and catch trends. There are still risks that need parameter and stop loss optimization. Overall, it suits trend trading and steadily catches market trends over the medium to long term.

|||

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|12|Fast Length|
|v_input_2|26|Slow Length|
|v_input_3|9|Signal Length|
|v_input_4|12|Entry TrueLevel Band|
|v_input_5|12|Exit TrueLevel Band|
|v_input_6|false|Enable Long and Short|
|v_input_7|126|Length 1|
|v_input_8|189|Length 2|
|v_input_9|252|Length 3|
|v_input_10|378|Length 4|
|v_input_11|504|Length 5|
|v_input_12|630|Length 6|
|v_input_13|756|Length 7|
|v_input_14|1008|Length 8|
|v_input_15|1260|Length 9|
|v_input_16|1638|Length 10|
|v_input_17|2016|Length 11|
|v_input_18|2646|Length 12|
|v_input_19|3276|Length 13|
|v_input_20|4284|Length 14|
|v_input_21|#00bfff|Fill Color|
|v_input_22|0|Multiple: 1|0.8|0.6|1.2|1.4|
|v_input_23_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-06 00:00:00
end: 2023-10-06 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Julien_Eche

//@version=4
strategy("MACD TrueLevel Strategy", shorttitle="MACD TL", overlay=true)

// Input parameters for MACD
fastLength = input(12, title="Fast Length", type=input.integer)
slowLength = input(26, title="Slow Length", type=input.integer)
signalLength = input(9, title="Signal Length", type=input.integer)

// Inputs for selecting bands
entry_band = input(12, title="Entry TrueLevel Band", type=input.integer, minval=1, maxval=14)
exit_band = input(12, title="Exit TrueLevel Band", type=input.integer, minval=1, maxval=14)

// Input for long and short mode
long_and_short = input(false, title="Enable Long and Short", type=input.bool)

// Calculate the MACD
[macdLine, signalLine, _] = macd(close, fastLength, slowLength, signalLength)


// User inputs
len1 = input(title="Length 1", type=input.integer, defval=126)
len2 = input(title="Length 2",