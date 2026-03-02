> Name

One-Goal Equilibrium Shift Combined Quantitative Strategy Ichimoku-Kinko-Hyo-Cloud-QQE-Quantitative-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1c3ec1a8fa605c51caf.png)
[trans]

## Overview

This strategy is a combination of the Ichimoku Kinko Hyo Cloud and QQE indicators, used to identify potential price trends and determine optimal entry and exit timing. It calculates Ichimoku Cloud lines and uses the QQE indicator to judge trend direction and generate trading signals, while employing the RSI indicator for filtration to control trading risk.

## Strategy Logic

The strategy mainly consists of three parts:

1. **Ichimoku Cloud Indicator**: The Ichimoku Cloud primarily uses Tenkan-sen (Conversion Line) and Kijun-sen (Base Line) lines to form an "Ichimoku" pattern. The Tenkan-sen represents the short-term trend, while the Kijun-sen stands for the medium-term trend. The crossing between these two lines generates buy and sell signals.

2. **QQE Indicator**: QQE calculates discrete relative value bands and smoothed relative values to determine the trend direction. It sends trading signals when price breaks out of outer bands into the middle band area.

3. **RSI Indicator**: RSI is used to judge if the price is overbought or oversold, setting overbought lines and zones. It combines with QQE signals to decide final buy and sell signals.

Specifically, this strategy monitors if the Conversion Line has a golden cross (upward crossing) or dead cross (downward crossing) with the Base Line to determine trading signals. It also uses the QQE indicator to confirm overall trend direction. When both indicators give aligned signals, and RSI shows no overbought or oversold situation, trading signals will be triggered.

## Advantages

This strategy combines different indicators to improve judgment accuracy and utilize complementary advantages to avoid bias from a single indicator decision. The main advantages are:

1. Conversion Line and Base Line of the Ichimoku Cloud reflect both short-term and medium-term trends for better accuracy than a single MA indicator.
2. QQE reliably determines overall trend direction and complements with Ichimoku Cloud.
3. RSI filtration efficiently filters out false breakouts and controls trading risks.
4. This strategy has clear logic and is easy to understand and implement for quantitative trading.

## Risks

Although this strategy uses multiple indicators for robust decisions, main risks still exist:

1. **Parameter Setting Risk**: Invalid parameter settings of Conversion Line, Base Line, etc., will lead to improper trading signals. Parameters need optimization for different products.
2. **Trend Reversal Risk**: Fake signals may occur during range-bound markets. More indicators of trend reversal are needed.
3. **Too Strict RSI Filter Risk**: Potential trading opportunities may be filtered out. RSI parameters can be tuned to allow more trades.

Solutions:

1. Optimize parameters on more historical data for different products to ensure proper parameter configuration.
2. Add a stop loss mechanism in the strategy. Exit positions when price breaks the stop loss line in the opposite direction.
3. Optimize RSI parameters to moderately relax the filtration requirements and acquire more trading opportunities under risk control.

## Enhancement Directions

This strategy can be further improved from the following aspects:

1. **Introduce Machine Learning Algorithms**: To dynamically tune strategy parameters adapting to evolving markets, improving adaptivity.
2. **Modularize Strategy Components**: For easier replacement and separate testing & optimization, improving development efficiency.
3. **Build Data Integration Module**: To collect market data from more sources and construct high-quality training sets, enhancing machine learning performance.
4. **Develop Backtesting Tools**: For comprehensive strategy validation, recording various metrics for parameter tuning.
5. **Deploy Strategy System on Cloud Platform**: Utilize elastic computing power for faster parallel backtesting, accelerating parameters optimization at lower development costs.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Standard Ichimoku Cloud|
|v_input_2|true|Ichimoku Cloud - no offset - no repaint|
|v_input_3|9|Conversion Line Period - Tenkan-Sen|
|v_input_4|27|Base Line Period - Kijun-Sen|
|v_input_5|52|Base Line Period - Kijun-Sen (auxiliary)|
|v_input_6|52|Lagging