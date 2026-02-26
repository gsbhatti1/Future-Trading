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
   
2. **Parameter Sensitivity**: Strategy performance highly depends on the SMA period (20) and RSI period (8), as well as their thresholds (60/40). These fixed parameters may perform poorly in different market environments or instruments.

3. **Lack of Adaptability**: The strategy lacks market environment recognition capabilities, performing well in trend markets but potentially losing frequently in volatile ones.
   
4. **Basic Stop Loss Mechanism**: While the strategy tracks failures, it does not implement dynamic stop loss functionality, which could result in significant losses during volatile periods.
   
5. **Lack of Position Management**: The strategy employs fixed position sizing for entry and exit, without adjusting based on market volatility or signal strength to optimize capital utilization.
   
6. **Limited Performance Evaluation**: Success is defined as a price increase of 2%, which may not be suitable for all market environments; high-volatility instruments might require higher thresholds.

## Strategy Optimization Directions

1. **Add Market Environment Filter**: Introduce volatility indicators (like ATR) or trend strength indicators (like ADX) to help identify market conditions, reducing trading frequency in volatile markets or adjusting parameters accordingly.
   
2. **Dynamic Parameter Mechanism**: Implement dynamic adjustment of SMA and RSI parameters based on recent market performance for automatic optimization of periods and thresholds, enhancing adaptability.

3. **Optimize Position Management**: Design a dynamic position allocation system based on signal strength (such as RSI deviation), market volatility, or account risk to control single trade risks.
   
4. **Enhance Stop Loss Mechanism**: Implement ATR-based dynamic stop loss or trailing stop functionalities for finer-grained control over each trade's risk.

5. **Increase Time Filtering**: Consider market timing factors by avoiding trading during periods of abnormal volatility or low liquidity, improving signal quality.
   
6. **Multi-Period Confirmation**: Introduce multi-period analysis requiring alignment between larger time frame trend direction and transaction direction to filter out counter-trend trades.
   
7. **Improve Performance Evaluation**: Refine the definitions of success/failure; consider using risk-adjusted returns or return/risk ratios for more comprehensive performance evaluation.

## Summary

The Cross-Momentum Trend Following Strategy is a simple yet practical trading system that effectively combines SMA and RSI indicators to identify trend reversal points while confirming momentum. It efficiently filters out low-quality signals by utilizing price crossovers with the 20-period SMA and RSI confirmation. This strategy is particularly suitable for new quant traders, offering clear trade signals along with built-in performance tracking functions to help traders objectively evaluate strategy performance.

While the design of the strategy is relatively simple, it embodies key principles in quantitative trading: trend following, signal confirmation, and performance monitoring. By suggesting optimization directions such as market environment filtering, dynamic parameter adaptation, and enhanced stop loss mechanisms, traders can significantly enhance the robustness and adaptability of the strategy while maintaining its core logic.

This combination of classical technical indicators often proves more reliable and enduring than complex algorithms, especially when equipped with risk management and performance evaluation mechanisms. For traders seeking an entry-level quantitative strategy, this is an ideal starting point that provides both practical experience and a foundation for subsequent strategy development.