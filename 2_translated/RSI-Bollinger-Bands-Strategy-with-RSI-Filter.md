> Name

Bollinger Bands Strategy with RSI Filter

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19fc9ce9aaf4188f7ae.png)

[trans]

## Overview

This strategy is named “Bollinger Bands Strategy with RSI Filter.” It leverages the principles of Bollinger Bands combined with the RSI indicator as a filter to determine entry points. This strategy can effectively identify market trends for low-buy and high-sell opportunities, achieving better profits.

## Strategy Principle

The core indicator of this strategy is Bollinger Bands, which consists of the middle band, upper band, and lower band. The middle band is the n-period moving average, the upper band is the middle band plus k times the n-period standard deviation, and the lower band is the middle band minus k times the n-period standard deviation. When the price approaches the upper band, it indicates that the market is overvalued, suggesting short positions should be considered. Conversely, when the price approaches the lower band, it suggests the market is undervalued, indicating long positions are suitable.

In addition to Bollinger Bands, this strategy incorporates the RSI indicator as an entry filter. The RSI can determine whether the market is overbought or oversold. Values above 70 indicate overbought conditions, while values below 30 indicate oversold conditions. This strategy only considers entering trades when both Bollinger Bands and RSI signals align with overbought or oversold levels.

Specifically, a buy signal is generated when the price breaks above the lower Bollinger Band from below while the RSI is below 30. Conversely, a sell signal is triggered when the price breaks below the upper Bollinger Band from above while the RSI is above 70.

## Advantage Analysis

This strategy combines Bollinger Bands and the RSI indicator to effectively identify overbought and oversold market conditions, reducing losses due to false breakouts. The RSI acts as a filter, removing some noise from trade signals, making entry timing more accurate.

The strategy requires few parameters and is straightforward to implement, suitable for traders of all skill levels. A mid-to-long-term holding strategy avoids interference from short-term market fluctuations.

In summary, the advantages are:

1. Stronger judgment by integrating Bollinger Bands and RSI
2. Reduces losses due to false breakouts
3. Simple parameters, easy to implement
4. Smaller drawdowns with mid-to-long-term holdings

## Risk Analysis

This strategy also has some risks that need attention:

1. Inappropriate Bollinger Bands parameter settings can degrade signal quality.
2. Bollinger Bands often follow price action in trending markets, making them less effective.
3. RSI divergences may affect the accuracy of trade signals.
4. Infrequent trading signals could lead to long-term losses.

To mitigate these risks:

1. Optimize parameters to find the best combinations.
2. Consider higher timeframes to avoid ranging markets.
3. Confirm RSI signals with other indicators to prevent false signals.
4. Adjust holding periods to minimize severe losses.

## Optimization Directions

Further improvements can be made by:

1. Testing different RSI parameter settings.
2. Incorporating stop-loss strategies to better control risk.
3. Combining this strategy with other indicators for confirmation.
4. Utilizing machine learning methods for automated parameter optimization.

These enhancements can improve stability, optimize parameters, and strengthen risk management.

## Conclusion

The "Bollinger Bands Strategy with RSI Filter" integrates Bollinger Bands’ overbought/oversold identification with the RSI’s momentum gauge to form a robust quantitative strategy. The strategy has unique advantages in determining market opportunities across different timeframes, capable of generating significant alpha.

Nonetheless, there is room for improvement via parameter optimization and risk control to adapt performance to diverse market conditions, an area warranting further research.

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|length|
|v_input_float_1|2.0|mult|
|v_input_1|14|RSI Length|
|v_input_2|70|RSI Overbought Level|
|v_input_3|30|RSI Oversold Level|


> Source (PineScript)

```pinescript
//@version=5
strategy("Bollinger Bands Strategy with RSI Filter", overlay=true)
source = close
length = input.int(20, minval=1)
mult = input.float(2.0, minval=0.001, maxval=50)
basis = ta.sma(source, length)
dev = mult * ta.stdev(source, length)
upper = basis + dev
lower = basis - dev

// RSI Filter
rsiLength = input.int(14, title="RSI Length")
rsiOverboug