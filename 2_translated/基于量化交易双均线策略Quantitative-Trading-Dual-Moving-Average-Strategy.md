> Name

Based on the Dual Moving Average Strategy for Quantitative Trading

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1c9df4eacc2995275c2.png)
[trans]

## Overview

This strategy is designed based on the technical indicators of moving average and trading volume, to create a long-term trend-following quantitative strategy. When the stock price stands above the 20-day line, and the buying volume for that day is greater than the selling volume and larger than the average trading volume over the past n days, it is considered that the market is in a bullish state and one should buy; when the stock price breaks below the lower track, and the selling volume for that day is greater than the buying volume and larger than the average trading volume over the past n days, it is considered that the market is in a bearish state and one should sell.

## Strategy Principle

The strategy mainly relies on two indicators for judgment:

1. Dual Moving Average: Calculate the 20-day line and 60-day line; when the 20-day line crosses above the 60-day line, the market is considered to be in an uptrend; when the 20-day line crosses below the 60-day line, the market is considered to be in a downtrend.

2. Trading Volume: Calculate the daily buying volume and selling volume. If the buying volume is greater than the selling volume and larger than the average trading volume over the past n days, it is determined that the market is bullish; if the selling volume is greater than the buying volume and larger than the average trading volume over the past n days, it is determined that the market is bearish.

The specific trading strategy and logic are as follows:

Go Long: When the closing price stands above the 20-day line, and the buying volume for that day is greater than the selling volume and larger than the average trading volume over the past n days, consider the market to be bullish. Calculate the Bollinger Bands based on volatility; if the closing price is between the midline and lower track of the Bollinger Bands, enter a long position.

Go Short: When the closing price breaks below the lower track, and the selling volume for that day is greater than the buying volume and larger than the average trading volume over the past n days, consider the market to be bearish. Calculate the Bollinger Bands based on volatility; if the closing price is below the lower track of the Bollinger Bands, enter a short position.

Profit Taking and Stop Loss: Set reasonable profit taking and stop loss levels to lock in profits or reduce losses. For example, when the price rises 5% above the entry price, take profit; when the loss reaches 10%, stop loss; or when the price hits a recent new high and then pulls back to some extent, take profit.

## Advantage Analysis

The strategy has the following advantages:

1. Combining dual moving average lines with trading volume indicators avoids the blind spots of single technical indicator judgment.
2. Using Bollinger Bands with different parameters determines more precise entry prices.
3. The profit taking and stop loss strategy is reasonable, which helps lock in profits and control risks.
4. Good backtesting results with stable returns, making it suitable for practical application in quantitative trading.

## Risk Analysis

The strategy also has some risks:

1. Dual moving average strategies tend to produce false signals and need to be filtered by volume indicators.
2. Improper Bollinger Bands parameter settings may lead to overly frequent or sparse entries.
3. Fixed profit taking and stop loss points set improperly may affect the overall performance of the strategy.
4. A large amount of historical data is required for backtesting, but unexpected losses can still occur in live trading.

## Optimization Direction

The strategy can be optimized in the following aspects:

1. Optimize the parameters of the moving average system to find the optimal combination of moving averages.
2. Optimize Bollinger Bands parameters for more precise entry points.
3. Dynamically adjust profit taking and stop loss levels based on market conditions to set reasonable risk-reward ratios.
4. Increase judgment using other technical indicators such as MACD, KD, etc., to improve strategy accuracy.
5. Use machine learning methods to automatically find optimal parameters to make strategies more robust.

## Summary

Overall, this is a very practical quantitative trading strategy with good backtesting performance. It is easy to implement and has controllable risks, making it a stable strategy suitable for live trading. This approach is worth learning for quantitative traders. Of course, there is still much room for further optimization, and I look forward to more Quantitative trading experts improving upon it.