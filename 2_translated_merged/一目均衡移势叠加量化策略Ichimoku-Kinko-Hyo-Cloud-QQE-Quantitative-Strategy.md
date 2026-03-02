> Name

One-Goal Balance Trend Overlay Quantitative Strategy Ichimoku-Kinko-Hyo-Cloud-QQE-Quantitative-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1c3ec1a8fa605c51caf.png)
[trans]

## Overview 

This strategy combines Ichimoku Kinko Hyo Cloud and QQE indicators to discover potential price trends and determine optimal entry and exit timing. It calculates Ichimoku Cloud lines and uses QQE indicator to judge trend direction and generate trading signals, while utilizing RSI indicator for filtration to control trading risk.

## Strategy Logic

The strategy consists of three main components:

1. **Ichimoku Cloud Indicator**: Ichimoku Cloud uses Tenkan-sen (Conversion Line) and Kijun-sen (Base Line) to form "Ichimoku" formation. Tenkan-sen represents short-term trend while Kijun-sen stands for medium-term trend. The crossing between Tenkan-sen and Kijun-sen generates buy and sell signals.

2. **QQE Indicator**: QQE calculates discrete relative value bands and smoothed relative values to determine the trend direction. It sends trading signals when price breaks out of outer bands into the middle band area.

3. **RSI Indicator**: RSI judges if the price is overbought or oversold. It sets overbought line and overbought zones, and uses QQE signals to decide final entry and exit signals.

Specifically, this strategy monitors if Conversion Line has golden cross (upward crossing) or dead cross (downward crossing) with Base Line to determine trading signals. It also uses QQE indicator to confirm overall trend direction. When both indicators give aligned signals, and RSI shows no overbought or oversold situation, the trading signals will be triggered.

## Advantages

This strategy combines different indicators to improve judgment accuracy and utilize complementary advantages to avoid bias from single indicator decision. The main advantages are:

1. **Conversion Line and Base Line of Ichimoku Cloud reflect both short-term and medium-term trends for better accuracy than single MA indicator**.
2. **QQE reliably determines overall trend direction and complements with Ichimoku Cloud**.
3. **RSI filtration efficiently filters out false breakouts and controls trading risks**.
4. This strategy has clear logic and is easy to understand and implement for quantitative trading.

## Risks

Although this strategy uses multiple indicators for robust decisions, main risks still exist:

1. **Parameter tuning risk**: Invalid parameter settings of Conversion Line, Base Line etc will lead to improper trading signals. Parameters need optimization for different products.
2. **Trend reversal risk**: Fake signals may occur during range-bound market. More indicators of trend reversal are needed.
3. **Too strict RSI filter risk**: Potential trading opportunities may be filtered out. RSI parameters can be tuned to allow more trades.

Solutions:

1. Optimize parameters on more historical data for different products to ensure proper parameter configuration.
2. Add stop loss mechanism in the strategy. Exit positions when price breaks stop loss line in opposite direction.
3. Optimize RSI parameters to moderately relax the filtration requirements and acquire more trading opportunities under risk control.

## Enhancement Directions

This strategy can be further improved from the following aspects:

1. Introduce machine learning algorithms to dynamically tune the strategy parameters adapting to evolving markets, improving adaptivity.
2. Modularize the strategy components for easier replacement and separate testing & optimization, improving development efficiency.
3. Build data integration module to collect market data from more sources and construct high-quality training set, enhancing machine learning performance.
4. Develop backtesting tools for comprehensive strategy validation, recording various metrics for parameter tuning.
5. Deploy the strategy system on cloud platform, utilize elastic computing power for faster parallel backtesting, accelerating parameters optimization at lower development costs.

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