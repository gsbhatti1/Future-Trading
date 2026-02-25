## Overview

The Cross-Momentum Trend Following Strategy is a simple yet effective trading system that cleverly combines two technical indicators - Simple Moving Average (SMA) and Relative Strength Index (RSI) - to form an automated buy and sell signal generation system. The strategy utilizes price crossovers with the 20-period SMA as the primary signal trigger condition, while incorporating RSI momentum confirmation to filter out low-quality trading signals. The strategy also includes a performance tracking module that monitors success and failure rates in real-time, providing traders with decision-making reference.

## Strategy Principles

The core principle of this strategy is to capture trend reversal points through price and moving average crossovers, while using the RSI momentum indicator for signal confirmation:

1. **Buy Condition**: When price crosses above the 20-period SMA and the RSI value is greater than 60, the system generates a buy signal. This condition combines two dimensions: price breaking above the moving average indicates a potential uptrend formation, while an RSI value above 60 confirms the presence of upward momentum.

2. **Sell Condition**: When price crosses below the 20-period SMA and the RSI value is less than 40, the system generates a sell signal. Similarly, this condition identifies potential trend reversals and confirms downward momentum through the sub-40 RSI value.

3. **Performance Tracking Mechanism**: The strategy has a built-in trade performance monitoring system that tracks the following metrics:
   - Total Signal Count: Records the number of all generated buy signals
   - Success Count: Number of times price rises more than 2% after buying
   - Failure Count: Number of times price falls below the buy candle's low within 7 periods

4. **Visualization**: The strategy marks buy and sell points on the chart with "B" (Buy) and "S" (Sell), and displays performance statistics in real-time through a table.

## Strategy Advantages

1. **Simplicity and Efficiency**: Uses only two common technical indicators (SMA and RSI) to build a complete trading system, reducing the risk of over-optimization and overfitting.
2. **Dual Confirmation Mechanism**: Combines trend indicator (SMA) and momentum indicator (RSI), improving signal reliability. Price must not only break through the moving average but also have sufficient momentum to trigger a trade.
3. **High Degree of Automation**: The strategy completely automates the generation of buy and sell signals, reducing emotional interference and is suitable for systematic traders.
4. **Built-in Performance Evaluation**: Real-time tracking of key performance metrics allows traders to objectively assess strategy performance and timely adjust parameters or exit underperforming strategies.
5. **Risk Control Awareness**: By monitoring price behavior within 7 periods after buying, it helps identify potential stop-loss points and cultivates risk management awareness.
6. **Intuitive Visualization**: Through chart markers and performance tables, traders can intuitively understand strategy execution, facilitating backtesting analysis and strategy improvement.

## Strategy Risks

1. **False Breakout Risk**: Despite using RSI for filtering, the strategy may still produce numerous false breakout signals in consolidating markets, leading to frequent trading and unnecessary transaction costs.
2. **Parameter Sensitivity**: Strategy performance highly depends on the 20-period SMA cycle and 8-period RSI cycle, as well as their thresholds (60/40). These fixed parameters might not perform well in different market environments or asset classes.
3. **Lack of Adaptability**: The strategy lacks market condition recognition capabilities, performing well in trending markets but potentially losing frequently in volatile ones.
4. **Simple Stop-Loss Mechanism**: While the strategy tracks failures, it does not implement dynamic stop-loss functions, which could result in significant losses during sharp market movements.
5. **Lack of Position Sizing Management**: The strategy adopts fixed position sizing for entry and exit, without adjusting position size based on market volatility or signal strength to optimize capital utilization.
6. **Limited Performance Evaluation**: Success is defined as a 2% price increase after buying, which might not be suitable for all market environments; higher-volatility assets may require different thresholds.

## Strategy Optimization Directions

1. **Add Market Environment Filter**: Introduce volatility indicators (e.g., ATR) or trend strength indicators (e.g., ADX) to help identify market conditions and reduce trading frequency in volatile markets or adjust parameters accordingly.
2. **Parameter Adaptive Mechanism**: Implement dynamic adjustment of SMA and RSI parameters based on recent market performance for automatic optimization, improving adaptability.
3. **Optimize Position Sizing Management**: Design a dynamic position allocation system based on signal strength (e.g., RSI deviation), market volatility, or account risk to control single trade risks.
4. **Refine Stop-Loss Mechanism**: Implement ATR-based dynamic stop-loss or trailing stop functions for more precise control over each trade.
5. **Increase Time Filtering**: Consider market time factors by avoiding abnormal volatile periods or low liquidity times for trading, improving signal quality.
6. **Multi-Period Confirmation**: Introduce multi-period analysis to require consistent trend direction across larger time frames and filter out counter-trend signals.
7. **Enhance Performance Evaluation**: Improve the definition of success/failure criteria; consider using risk-adjusted returns or return/risk ratio for a more comprehensive evaluation.

## Summary

The Cross-Momentum Trend Following Strategy is a simple yet practical trading system that combines SMA and RSI indicators to effectively capture trend reversal points while confirming momentum. This strategy provides clear trade signals and includes performance tracking features to help traders objectively evaluate strategy performance. 

Although the design of this strategy is relatively straightforward, it embodies key principles in quantitative trading such as trend following, signal confirmation, and performance monitoring. By incorporating suggested optimizations like market environment filtering, parameter adaptation, and enhanced stop-loss mechanisms, traders can significantly enhance the robustness and adaptability of the strategy while maintaining its core logic.

Such a simple strategy that integrates classic technical indicators often proves more reliable and enduring when equipped with risk management and performance evaluation mechanisms. For traders seeking an entry-level quantitative strategy, this is an ideal starting point, offering both practical experience and a foundation for further strategy development.