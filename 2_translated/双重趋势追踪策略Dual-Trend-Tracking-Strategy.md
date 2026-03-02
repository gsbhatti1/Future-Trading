## Overview

The Dual-Trend-Tracking Strategy combines two different strategy signals to more accurately capture market trends and generate excess returns. It first uses the 123 Reversal Strategy to determine price reversal signals, and then integrates the overbought/oversold indicator to determine position direction, tracking trends while avoiding being trapped.

## Strategy Logic

The strategy consists of two parts:

1. **123 Reversal Strategy**

   The 123 Reversal Strategy first evaluates the relationship between the closing prices of the previous two days. If there is a reversal in recent closing prices (e.g., the price rose yesterday and fell the day before), it suggests a potential turning point.

   It then integrates the Stoch indicator to determine optimal buy and sell times. When the Stoch fast line falls below a certain level (e.g., 50) while the slow line is above the fast line, it indicates an oversold condition and generates a buy signal. Conversely, when the Stoch fast line rises above a certain level (e.g., 50) while the slow line is below the fast line, it suggests an overbought condition and triggers a sell signal.

   Therefore, the 123 Reversal Strategy requires validation from the Stoch indicator to produce genuine trading signals.

2. **Overbought/Oversold Indicator**

   The Overbought/Oversold Indicator directly uses the Stoch indicator. If the Stoch level exceeds a certain threshold (e.g., 90), it deems the market overbought and issues a sell signal. Conversely, if the Stoch level falls below a certain threshold (e.g., 20), it deems the market oversold and signals a buy opportunity.

   This indicator directly assesses overbought/oversold levels via the Stoch indicator to track trends.

Finally, the strategy combines these two signals—only when both signals are in the same direction will final buy or sell decisions be made to more accurately capture market trends.

## Advantage Analysis

The main advantage of the Dual-Trend-Tracking Strategy lies in its ability to simultaneously verify price trends and overbought/oversold conditions, thus reducing the likelihood of erroneous trading signals. Specific advantages include:

1. **Combining Two Strategy Signals**: This provides a more robust verification mechanism, minimizing losses due to errors from a single strategy.

2. **Timely Detection of Trend Reversals**: The 123 Reversal Strategy can promptly capture potential trend reversal points.

3. **Verification Through Overbought/Oversold Indicator**: It validates current market conditions, avoiding the pitfalls of chasing highs and selling lows.

4. **Cross-Verification Between Strategies**: This mutual validation prevents erroneous signals and enhances strategy stability.

5. **Clear and Understandable Logic**: By combining simple yet effective indicators, the logic is straightforward and easy to apply in practice.

## Risk Analysis

While this strategy improves stability through combined verification, several risks still need attention:

1. The 123 Reversal Strategy may not perfectly identify reversal points, potentially missing some opportunities. Fine-tune parameters to lower the reversal signal threshold if necessary.

2. The Overbought/Oversold Indicator relies solely on one Stoch indicator and may generate false signals. Incorporate additional indicators like Moving Averages (MAs) for validation.

3. The two strategy signals might cancel each other out, leading to missed trading opportunities. Adjust parameters to reduce constraints.

4. The strategy is based on historical backtesting; real-time parameters require continuous optimization. Implement stop loss mechanisms to control losses.

5. Parameters should be independently tested and optimized for different products and trading periods, avoiding the direct use of generic parameters.

## Optimization Directions

Several areas can further refine this strategy:

1. **Parameter Optimization**: Fine-tune parameters for both strategies to find optimal combinations under various market conditions.
2. **Filter Conditions**: Introduce additional filters using indicators like Moving Averages (MAs) and Bollinger Bands to reduce false signals.
3. **Stop Loss Mechanisms**: Implement stop loss mechanisms such as trailing stops, moving stops, and time-based stops to control drawdowns.
4. **Volume/Position Filters**: Consider adding volume or position filters for different products to manage low liquidity trades.
5. **Parameter Evolution Study**: Analyze parameter changes over time using machine learning techniques for automatic optimization.
6. **Optimized Entry Frequency**: Adjust entry frequency to avoid frequent trading in trendless markets.

## Conclusion

The Dual-Trend-Tracking Strategy accurately identifies price trend reversals by combining the 123 Reversal Strategy with the Overbought/Oversold Indicator, thereby filtering out erroneous signals and capturing actual trends for excess returns. Compared to single-indicator strategies, this approach offers better stability and profitability. However, it is crucial to manage risks through appropriate stop loss mechanisms, continuous parameter optimization, and strategic entry frequency adjustments. Future improvements could include further parameter refinement, enhanced filter conditions, and automation techniques.