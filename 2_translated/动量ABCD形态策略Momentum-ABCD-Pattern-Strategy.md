> Name

Momentum ABCD Pattern Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy utilizes the Williams Fractal indicator to identify price highs and lows, and combines ABCD patterns to determine trend direction. It enters a position after confirming the trend to track medium-term trends for profit.

## Strategy Logic

1. Use the Williams Fractal indicator to identify price highs and lows. Different patterns are used to determine bullish or bearish ABCD patterns.
2. ABCD pattern identification criteria:
    - The distance between AB and CD is similar, and the distance between BC and CD meets certain proportional requirements (0.382-0.886 and 1.13-2.618).
    - D point lower than C point is a bullish pattern; D point higher than C point is a bearish pattern.
3. Use the `barssince` function to determine which direction's Fractal is closest to current, to judge the overall trend direction.
4. Enter long/short after identifying ABCD pattern and set stop loss and take profit to track medium-term trends.

## Advantage Analysis

1. The Williams Fractal indicator helps identify turning points more accurately.
2. ABCD pattern criteria are simple and reliable, easy to automate.
3. Judging major trend direction with `barssince` avoids losses from false breakouts.
4. Following trends with stop loss and take profit after entry.

## Risk Analysis

1. Williams Fractal may lag and miss turning points causing losses.
2. Multiple overlapping ABCD patterns may cause misidentification on medium-term charts.
3. Wrong major trend direction increases the risk of being trapped in medium-term trades.
4. Stop loss set too tight may get stopped out easily; stop loss set too wide may have poor tracking.

Possible solutions:

1. Test other indicators to assist in identifying turning points more effectively.
2. Optimize ABCD pattern parameters to make identification more strict and reliable.
3. Improve major trend identification methods to avoid wrong directional bias.
4. Test different stop loss/take profit ratios to find optimal levels.

## Optimization Directions

1. Test MACD, KDJ, and other indicators to improve entry signal accuracy.
2. Optimize parameters based on different products and timeframes to find the best stop loss/take profit levels.
3. Optimize bar lookback periods according to changing market conditions to find the best parameter combinations.
4. Add moving averages or similar indicators to filter signals and enhance stability.
5. Introduce machine learning algorithms using more data to improve pattern recognition accuracy.

## Summary

The strategy's overall logic is clear and reliable, using Williams Fractal and ABCD patterns to determine medium-term trend direction, combining with trend filtering and stop loss/take profit settings to track trends for profit. There is still significant room for optimization in areas such as entry signals, parameter tuning, and trend identification to make it adaptable to different market conditions. As a discretionary + quant hybrid model, this strategy has strong practical value.

---

## Overview

This strategy uses the Williams Fractal indicator to identify price peaks and troughs and combines ABCD patterns to determine trend direction. It enters a position after confirming the trend in order to follow medium-term trends for profit.

## Strategy Logic

1. Use the Williams Fractal indicator to identify price highs and lows, distinguishing between bullish or bearish ABCD patterns.
2. ABCD pattern identification criteria:
    - The distance between AB and CD is similar, and the distance between BC and CD meets certain proportional requirements (0.382-0.886 and 1.13-2.618).
    - D point lower than C point indicates a bullish pattern; D point higher than C point indicates a bearish pattern.
3. Use the `barssince` function to determine which direction's Fractal is closest to current, thus judging the overall trend direction.
4. Enter long/short after identifying ABCD pattern and set stop loss and take profit to follow medium-term trends.

## Advantage Analysis

1. The Williams Fractal indicator aids in accurately identifying turning points.
2. Simple and reliable ABCD pattern criteria that can be easily automated.
3. Using the `barssince` function to assess major trend direction helps minimize losses from false breakouts.
4. Follows trends with stop loss and take profit after entry.

## Risk Analysis

1. Williams Fractal may lag, potentially missing turning points leading to losses.
2. Multiple overlapping ABCD patterns could result in misidentification on medium-term charts.
3. Inaccurate major trend direction increases the risk of being trapped in medium-term trades.
4. Stop loss set too tight could result in easy stopouts; too wide would limit tracking effectiveness.

Possible solutions:

1. Test other indicators to better identify turning points.
2. Optimize ABCD pattern parameters for stricter and more reliable identification.
3. Improve major trend identification methods to avoid incorrect directional bias.
4. Experiment with different stop loss/take profit ratios to find the optimal settings.

## Optimization Directions

1. Test MACD, KDJ, or other indicators to enhance entry signal accuracy.
2. Optimize parameters based on different products and timeframes for optimal stop loss/take profit levels.
3. Adjust lookback periods according to market changes to find the best parameter combinations.
4. Incorporate moving averages or similar tools to filter signals and improve stability.
5. Introduce machine learning algorithms with more data to enhance pattern recognition accuracy.

## Summary

The strategy logic is clear and reliable overall, utilizing Williams Fractal and ABCD patterns to determine medium-term trend direction, combining trend filtering and stop loss/take profit settings to track trends for profit. There are many opportunities for further optimization in areas such as entry signals, parameter tuning, and trend identification, making it adaptable to various market conditions. As a combination of discretionary and quantitative approaches, this strategy offers strong practical value.

---

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|filter Bill Williams Fractals?|
|v_input_2|100|Backtest Profit Goal (in USD)|
|v_input_3|20|Backtest STOP Goal (in USD)|


> Source (PineScript)

``` pinescript
//@version=4
// @author=Daveatt - BEST

StrategyName        = "BEST ABCD Pattern Strategy"
ShortStrategyName   = "BEST ABCD Pattern Strategy" 

// strategy(title=StrategyName, shorttitle=ShortStrategyName, overlay=true, 
//  pyramiding=2, default_qty_value=100, precision=7, currency=currency.USD,
//  commission_value=0.2,commission_type=strategy.commission.percent, initial_capital=1000000,
//  default_qty_type=strategy.fixed)

filterBW = input(false, title="filter Bill Williams Fractals?")

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////// UTILITIES ///////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

isRegularFractal(mode, _high, _low) =>
    ret = mode == 1 ? _high[4] < _high[3] and _high[3] < _high[2] and _high[2] > _high[1] and _high[1] > _hi
```