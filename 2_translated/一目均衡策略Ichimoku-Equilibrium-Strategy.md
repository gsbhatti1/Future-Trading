> Name

Ichimoku Equilibrium Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/8d3efce40b7970e027.png)

[trans]


## Overview

The Ichimoku Equilibrium strategy is based on the Ichimoku technical indicator and combines moving average systems to generate trading signals. It uses Tenkan, Kijun, and Senkou lines to determine price trends and directions, generating buy and sell signals.

## Strategy Logic  

This strategy employs the `middleDonchian` function to calculate the Tenkan and Kijun lines. The Tenkan line calculates the average of the highest and lowest prices over the past 9 bars, representing the short-term equilibrium price. The Kijun line calculates the average of the highest and lowest prices over the past 26 bars, representing the medium-term equilibrium price.

The Senkou A line computes the average of the highest and lowest prices over the past 52 bars, then shifts forward by 26 bars to represent long-term future leading. The Senkou B line calculates the average of the Tenkan and Kijun lines, representing the current value midpoint.

Buy signals are generated when the close price rises above the Senkou A line, while sell signals are triggered when it falls below the Senkou B line.

The `pos` variable tracks the current position direction. The `possig` variable adjusts the signal direction based on the `reverse` input parameter. Finally, entry and exit decisions are made based on the values of `pos` and `possig`.

## Advantage Analysis

1. Utilizes two sets of moving averages with different parameter lengths to capture trend changes across various timeframes.

2. The Senkou A line provides early signals for long-term trends, while the Senkou B line indicates short-term equilibrium shifts, forming a leading system.

3. Identifies significant trend reversals by price breakouts at cloud boundaries.

4. Suitable for both trending and ranging markets. The `reverse` parameter allows quick adaptation to changes in market sentiment.

5. Cloud twist phenomena help filter out false breakout signals.

## Risk Analysis

1. Potential false signals when long and short moving averages cross over.

2. Frequent opening of positions during consolidations as prices oscillate around cloud boundaries.

3. Failed breakout risk due to cloud twists.

4. Chasing high purchases and low sales in trending markets can lead to poor performance.

5. Reversals require careful consideration and an understanding of the major trend direction.

Optimization through adjusting moving average combinations, adding filters, etc., can reduce unnecessary trading frequency and prevent being trapped by false signals.

## Optimization Directions

1. Optimize moving average combinations to find the best equilibrium point.

2. Add volume filter to avoid low volume false breakouts.

3. Incorporate other indicators for additional confirmation, e.g., MACD, KDJ, etc.

4. Optimize entry timing, such as requiring a close breakout after a cloud breakout.

5. Optimize stop loss methods, such as trailing stops or staggered stops.

6. Optimize reverse trading rules based on major trends.

## Conclusion

The Ichimoku Equilibrium strategy integrates the strengths of moving average trading and cloud analysis for unique trend reversal identification. Simple and practical for both trending and ranging markets, it can be adapted via optimization for different instruments and trading styles. However, false breakout risks remain; therefore, continuous monitoring of major trends is crucial for making decisions. With ongoing optimization, it can generate stable returns as a systematic strategy.

||


## Overview

The Ichimoku Equilibrium strategy is based on the Ichimoku indicator and combines moving average systems to generate trading signals. It uses Tenkan, Kijun, and Senkou lines to determine price trends and directions, generating buy and sell signals.

## Strategy Logic  

This strategy employs the `middleDonchian` function to calculate the Tenkan and Kijun lines. The Tenkan line calculates the average of the highest and lowest prices over the past 9 bars, representing the short-term equilibrium price. The Kijun line calculates the average of the highest and lowest prices over the past 26 bars, representing the medium-term equilibrium price.

The Senkou A line computes the average of the highest and lowest prices over the past 52 bars, then shifts forward by 26 bars to represent long-term future leading. The Senkou B line calculates the average of the Tenkan and Kijun lines, representing the current value midpoint.

Buy signals are generated when the close price rises above the Senkou A line, while sell signals are triggered when it falls below the Senkou B line.

The `pos` variable tracks the current position direction. The `possig` variable adjusts the signal direction based on the `reverse` input parameter. Finally, entry and exit decisions are made based on the values of `pos` and `possig`.

## Advantage Analysis

1. Utilizes two sets of moving averages with different parameter lengths to capture trend changes across various timeframes.

2. The Senkou A line provides early signals for long-term trends, while the Senkou B line indicates short-term equilibrium shifts, forming a leading system.

3. Identifies significant trend reversals by price breakouts at cloud boundaries.

4. Suitable for both trending and ranging markets. The `reverse` parameter allows quick adaptation to changes in market sentiment.

5. Cloud twist phenomena help filter out false breakout signals.

## Risk Analysis

1. Potential false signals when long and short moving averages cross over.

2. Frequent opening of positions during consolidations as prices oscillate around cloud boundaries.

3. Failed breakout risk due to cloud twists.

4. Chasing high purchases and low sales in trending markets can lead to poor performance.

5. Reversals require careful consideration and an understanding of the major trend direction.

Optimization through adjusting moving average combinations, adding filters, etc., can reduce unnecessary trading frequency and prevent being trapped by false signals.

## Optimization Directions

1. Optimize moving average combinations to find the best equilibrium point.

2. Add volume filter to avoid low volume false breakouts.

3. Incorporate other indicators for additional confirmation, e.g., MACD, KDJ, etc.

4. Optimize entry timing, such as requiring a close breakout after a cloud breakout.

5. Optimize stop loss methods, such as trailing stops or staggered stops.

6. Optimize reverse trading rules based on major trends.

## Conclusion

The Ichimoku Equilibrium strategy integrates the strengths of moving average trading and cloud analysis for unique trend reversal identification. Simple and practical for both trending and ranging markets, it can be adapted via optimization for different instruments and trading styles. However, false breakout risks remain; therefore, continuous monitoring of major trends is crucial for making decisions. With ongoing optimization, it can generate stable returns as a systematic strategy.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|conversionPeriods|
|v_input_2|26|basePeriods|
|v_input_3|52|laggingSpan2Periods|
|v_input_4|26|displacement|
|v_input_5|false|Trade reverse|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-29 00:00:00
end: 2023-10-29 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 26/09/2018
//  Ichimoku Strategy
//
// You can change long to short in the Input Settings
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
middleDonchian(Length) =>
    lower = lowest(Length)
    upper = highest(Length)
    avg(upper, lower)

strategy(title="Ichimoku2c Backtest", shorttitle="Ichimoku2c", overlay=true)
conversionPeriods = input(9, minval=1),
basePeriods = input(26, minval=1)
laggingSpan2Periods = input(52, minval=1),
displacement = input(26, minval=1)
reverse = input(false, title="Trade reverse")
Tenkan = middleDonchian(conversionPeriods)
Kijun = middleDonchian(basePeriods)
SenkouA = na
if bar_index > displacement
    SenkouA := (highest(basePeriods) + lowest(basePeriods)) / 2
SenkouB = (Tenkan + Kijun) / 2

plot(SenkouA, color=color.blue)
plot(SenkouB, color=color.red)

pos = 0
possig = if reverse
    -1
else
    1

if close > SenkouA
    pos := possig
    strategy.entry("Buy", strategy.long)
elif close < SenkouB
    pos := -possig
    strategy.close("Sell")
```

