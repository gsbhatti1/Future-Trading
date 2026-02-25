> Name

Ichimoku Cloud Trend Following Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/cf603d9a4b31ba3f47.png)
[trans]
## Overview  

The Ichimoku Cloud trend following strategy is a technical analysis strategy. It uses the five indicator lines of the Ichimoku Cloud to determine market trend direction, support/resistance levels, and entry timing.

## Principle  

The core indicator lines include:

1. Conversion Line: The 9-day average of highest high and lowest low, reflecting short-term trend.
2. Base Line: The 26-day average of highest high and lowest low, reflecting medium to long term trend.
3. Leading Span A: The average between the conversion and base lines, shifted forward 26 days, judging medium-term support and resistance.
4. Leading Span B: The 52-day average of highest high and lowest low, shifted forward 26 days, judging long-term support and resistance.
5. Lagging Span: The price shifted backward 26 days, reflecting trend momentum.

A buy signal is triggered when the conversion line crosses above the base line. A sell signal is triggered when it crosses below the base line. The lagging span above the price with a green cloud color indicates a bull trend. Otherwise, it suggests a bear trend.

The strategy judges trend direction based on the relationship between the conversion and base lines. For example, if the conversion line breaks out the base line upwards, it signals an entry into a bullish trend. If the lagging span is also above the price, a long position can be triggered.

Stop loss or take profit are set based on Leading Span A or Base Line. If the Base Line is chosen for stop loss, close the position when the price breaks below the Base Line.

## Advantage Analysis  

The advantages include:

1. Utilize multiple indicators for higher accuracy.
2. Leading Span anticipates support and resistance levels.
3. Lagging Span verifies momentum to avoid false breakouts.
4. Base Line as a medium/long term indicator reduces noise.

## Risks and Improvements  

The main risk is the potential for false signals. Suggested optimizations:

1. Adjust average periods to fine-tune sensitivity.
2. Add other filters like MACD, Bollinger Bands.
3. Lower trading frequency to follow mid/long term trend.

## Conclusion  

Ichimoku Cloud combines indicators to judge market trends, considering both short-term momentum and medium/long term trends. The relationship between the conversion and base lines determines entry signals. The base line sets stop loss levels to lock in profits and control risks. This strategy is suitable for medium/long term trend following.

||

## Overview  

The Ichimoku Cloud trend following strategy is a technical analysis strategy. It uses the five indicator lines of the Ichimoku Cloud to determine market trend direction, support/resistance levels, and entry timing.

## Principle  

The core indicator lines include:

1. Conversion Line: The 9-day average of highest high and lowest low, reflecting short-term trend.
2. Base Line: The 26-day average of highest high and lowest low, reflecting medium to long term trend.
3. Leading Span A: The average between the conversion and base lines, shifted forward 26 days, judging medium-term support and resistance.
4. Leading Span B: The 52-day average of highest high and lowest low, shifted forward 26 days, judging long-term support and resistance.
5. Lagging Span: The price shifted backward 26 days, reflecting trend momentum.

Buy signal triggered when conversion line crosses above base line. Sell signal triggered when crossing below base line. Lagging span above price and green cloud color indicates bull trend. Otherwise, it suggests a bear trend.

It judges trend direction based on the relationship between conversion and base lines. For example, when conversion line breaks out base line upwards, it signals a bullish trend. If lagging span is also above price, long entry triggered.

Set stop loss or take profit based on Leading Span A or Base Line. If Base Line is chosen for stop loss, close position when price breaks below Base Line.

## Advantage Analysis  

The advantages include:

1. Utilize multiple indicators for higher accuracy.
2. Leading Span anticipates support and resistance levels.
3. Lagging Span verifies momentum to avoid false breakouts.
4. Base Line as a medium/long term indicator reduces noise.

## Risks and Improvements  

Main risk is false signals. Suggested optimizations:

1. Adjust average periods to fine tune sensitivity.
2. Add other filters like MACD, Bollinger Bands.
3. Lower trading frequency to follow mid/long term trend.

## Conclusion  

Ichimoku Cloud combines indicators to judge market trends. It considers both short-term momentum and medium/long term trends. Conversion and Base Lines determine trading signals. Base Line sets stop loss to lock in profits and control risks. This strategy suits mid/long term trend following.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|9|Conversion Line Length|
|v_input_int_2|26|Base Line Length|
|v_input_int_3|52|Leading Span B Length|
|v_input_int_4|26|Lagging Span|
|v_input_string_1|0|Choose Trail Line: ConversionLine|BaseLine|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title="Ichimoku Cloud - BitBell", shorttitle="Ichimoku Cloud - BitBell", overlay=true)
conversionPeriods = input.int(9, minval=1, title="Conversion Line Length")
basePeriods = input.int(26, minval=1, title="Base Line Length")
laggingSpan2Periods = input.int(52, minval=1, title="Leading Span B Length")
displacement = input.int(26, minval=1, title="Lagging Span")
donchian(len) => math.avg(ta.lowest(len), ta.highest(len))
conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadLine1 = math.avg(conversionLine, baseLine)
leadLine1bbbbb = math.avg(conversionLine, baseLine)[displacement - 1]
plot(leadLine1bbbbb)
leadLine2 = donchian(laggingSpan2Periods)
leadLine2bbbbbb = donchian(laggingSpan2Periods)[displacement - 1]
plot(leadLine2bbbbbb)

support = leadLine1bbbbb > leadLine2bbbbbb
Resistance = leadLine1bbbbb < leadLine2bbbbbb

TrailStop = input.string(title='Choose Trail Line', options=["ConversionLine", "BaseLine"], defval="ConversionLine")

var stopLong = 0.0
var stopShort = 0.0
var TagetLong = 0.0
var TargetShort = 0.0

if close > leadLine1bbbbb and close > leadLine2bbbbbb and conversionLine[1] <= baseLine[1] and conversionLine > baseLine and close > conversionLine and support
    strategy.entry("Long",strategy.long)
    stopLong := conversionLine
// if close < stopLong and strategy.position_size > 0 
//     strategy.close("Long")
//     stopLong := 0.0
if (close < conversionLine and strategy.position_size > 0) and (TrailStop == 'ConversionLine')
    strategy.close("Long")
    stopLong := 0.0
if (close < baseLine and strategy.position_size > 0) and (TrailStop == 'BaseLine')
    strategy.close("Long")
    stopLong := 0.0

if close < leadLine1bbbbb and close < leadLine2bbbbbb and conversionLine[1] >= baseLine[1] and conversionLine < baseLine and close < conversionLine and Resistance
    strategy.entry("Short",strategy.short)
    stopShort := conversionLine
// if close > stopShort and strategy.position_size < 0 
//     strategy.close("Short")
//     stopShort := 0.0
if (close > conversionLine and strategy.position_size < 0) and (TrailStop == 'ConversionLine')
    strategy.close("Short")
    stopShort := 0.0
if (close > baseLine and strategy.pos