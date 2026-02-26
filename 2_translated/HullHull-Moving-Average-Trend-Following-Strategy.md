> Name

Hull Moving Average Trend Following Strategy Hull-Moving-Average-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/157eafa900f2fc0da45.png)

[trans]


## Overview

This strategy is based on the Hull Moving Average indicator to construct a trend-following trading system. It decides whether to go long or short based on the direction of the Hull curves, making it a typical trend-chasing strategy.

## Strategy Logic

The strategy uses the Hull Moving Average as the main technical indicator. The Hull Moving Average was proposed by American trader Alan Hull in 2005 and is an improvement over traditional moving averages using a square root function to reduce lag.

Specifically, the Hull Moving Average contains two average lines: one is the moving average MA(n) of period n, and the other is the moving average MA(n/2) of period n/2. The difference between these two moving averages forms the Hull difference curve. Taking the moving average of this Hull difference curve itself gives the Hull curve.

When the Hull curve slopes up, it indicates that the short-term moving average has crossed above the long-term moving average, triggering a buy signal. Conversely, when the Hull curve slopes down, it indicates that the short-term moving average has crossed below the long-term moving average, triggering a sell signal.

This strategy sets the Hull period n to 16 and calculates both the 8-period MA (n/2=8) and the 16-period MA. The difference between these two MAs is used to form the Hull curve, followed by taking its own 4-period moving average (square root of n=4). A long position is taken when the Hull curve crosses up, and a short position is taken when it crosses down.

## Advantage Analysis

Compared to ordinary moving averages, the Hull Moving Average has several advantages:

1. **Reduced Lag**: By using a square root function, the Hull curve better aligns with price action, allowing for quicker detection of price reversals.
2. **Fewer False Breakouts**: Traditional MAs tend to generate more false breakouts, whereas the Hull curve can filter out some noise and avoid unnecessary trades.
3. **Simplicity in Parameters**: The Hull curve only requires one parameter n, making optimization easier compared to a dual-MA system which needs to optimize two parameters.
4. **Customizability**: The n value of the Hull curve can be adjusted for different markets, allowing customization to suit various instruments.
5. **Systematic Approach**: The Hull system is robust and avoids manual selection, adhering to the consistency of mechanical trading systems.

## Risk Analysis

Despite its advantages over moving average systems, the Hull system still carries several risks:

1. **Trend Limitations**: As a trend-chasing strategy, it can be prone to stop-outs during drastic changes in trends.
2. **Increased Trading Frequency**: The fast response characteristics of Hull curves may increase trading frequency and lead to overtrading.
3. **Risk of Overoptimization**: With only one parameter n, there is a risk of overfitting the data.
4. **Performance Variability Across Instruments**: The Hull system may not work as well for instruments with high volatility and may require adjustments in parameters.

## Improvement Directions

To address the limitations mentioned above, improvements can be made in the following areas:

1. **Integration of Additional Indicators**: Add filters such as MACD or KD to avoid false breakouts.
2. **Stop Loss Strategies**: Implement stop loss strategies to control single trade losses, such as trailing stops or take profit stops.
3. **Optimized Parameter Selection**: Use methods like walk forward analysis for rolling optimization.
4. **Machine Learning Integration**: Employ machine learning models like RNNs to dynamically optimize parameter values.
5. **Parameter Optimization by Instrument**: Use machine learning to optimize parameters separately for different instruments.
6. **Position Sizing Optimization**: Optimize position sizing to reduce trade frequency, using methods such as fixed fractional position sizing.

## Conclusion

The Hull Moving Average strategy is a typical trend-following strategy. While it offers advantages over traditional moving averages, it also faces challenges like overoptimization and frequent trading. Improvements can be made through parameter optimization, stop losses, and position sizing. The Hull system is simple and practical, warranting further research and enhancement by incorporating additional indicators and techniques to build a robust trading system.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|100|Capital, %|
|v_input_4|16|HullMA period|
|v_input_5|1900|From Year|
|v_input_6|2100|To Year|
|v_input_7|true|From Month|