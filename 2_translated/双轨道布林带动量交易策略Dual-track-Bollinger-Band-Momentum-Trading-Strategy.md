## Overview

This strategy is based on the concept of Bollinger Bands, setting upper and lower rails for the price channel and using them for trend judgment and trade signal generation. Specifically, it calculates the average absolute deviation of the price as the channel bandwidth. The middle rail of the channel is the simple moving average of the price, and the upper and lower rails are the middle rail plus or minus 1 or 2 times the channel bandwidth. When the price breaks through the upper rail, go long. When it breaks through the lower rail, go short.

## Principle 

The main points of this strategy include:

1. Calculate the middle rail of the price, which is the simple moving average of the price.
2. Calculate the simple moving average of the absolute deviation of the price as the channel bandwidth.
3. Determine the upper and lower rails according to the middle rail and bandwidth. The upper rail is the middle rail plus 1 or 2 times the bandwidth. The lower rail is the middle rail minus 1 or 2 times the bandwidth.
4. Calculate the trend judgment indicator for long and short. When the price is above the upper rail 2, it is long. When the price is below the lower rail 2, it is short.
5. Generate trading signals. When the price crosses above the upper rail 2, go long. When it crosses below the lower rail 2, go short.
6. Set stop loss line. The stop loss line for long orders is the lower rail 1, and for short orders it is the upper rail 1.
7. Calculate the position size according to capital management requirements.

The strategy integrates the ideas of using moving averages to judge trends, Bollinger Bands to judge overbought and oversold, and breakouts to make reversals. The difference between the double rails is used to judge the strength of the trend, while the regression function of Bollinger Bands is utilized to form a relatively stable trading system.

## Advantage Analysis

The main advantages of this strategy are:

1. The dual-rail system can better judge the strength of the trend.
2. Bollinger Bands have a strong regression function to effectively avoid false breakouts.
3. The difference between the dual rails combined with the regression of Bollinger Bands forms relatively stable trading signals.
4. There is a clear stop loss/exit logic to control risks.
5. The position sizing follows capital management requirements, avoiding super leverage.
6. The strategy idea is clear and easy to understand and optimize.
7. Flexible parameter settings make it adaptable for different markets.

## Risk Analysis

The strategy also has some risks:

1. Improper Bollinger Bands parameters may cause ditching effects, failing to effectively track prices.
2. The difference between dual rails cannot completely avoid erroneous trend judgments.
3. It may generate more invalid signals in range-bound markets.
4. Losses may occur in false breakout situations.
5. There is some time lag, possibly missing cycle turning points.
6. The risk/reward ratio is limited by the stop loss point, unable to unlimitedly chase trends.

Corresponding risk management measures:

1. Optimize parameters to make Bollinger Bands adaptable to different cycles.
2. Combine other indicators for confirmation to avoid misjudgment.
3. Reduce position size to control single loss.
4. Optimize stop loss points to ensure risk/reward ratio.
5. Appropriately shorten cycle to reduce lag.
6. Risk control should be robust, no unlimited chasing.

## Optimization Directions

The strategy can be optimized in the following directions:

1. Optimize Bollinger Bands parameters for better price tracking. Adaptive parameters can be introduced.
2. Try different moving averages like EMA, DWMA, etc.
3. Add trend filtering to avoid trading in range-bound markets. MACD can be considered.
4. Add aggressive exit methods to capture more trend profits. Trailing stop loss, exit signals, etc., can be considered.
5. Introduce multiple time frames for combination, suitable for different market conditions.
6. Add additional conditions like volume surges to avoid false breakouts.
7. Consider reverse Bollinger Bands, selling upper band, buying lower band.
8. Perform parameter optimization for best parameter combinations.

## Summary

The overall idea of this strategy is clear and stable. There is also room for improvement via parameter optimization, logical refinement, and risk management measures. With further development, it can become a highly practical quantitative trading strategy. This strategy provides a good reference point for beginners in quantitative trading.