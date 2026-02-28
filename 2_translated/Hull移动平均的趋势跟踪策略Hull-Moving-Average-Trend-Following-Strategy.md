> Name

Hull Moving Average Trend Following Strategy Hull-Moving-Average-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/157eafa900f2fc0da45.png)

[trans]


## Overview

This strategy is based on the Hull Moving Average indicator to construct a trend-following trading system. It decides whether to go long or short based on the direction of the Hull curve, making it a typical trend-chasing strategy.

## Strategy Logic

This strategy uses the Hull Moving Average as the main technical indicator. The Hull Moving Average was proposed by American trader Alan Hull in 2005. It improves upon moving averages by using a square root function to reduce lag.

Specifically, the Hull Moving Average consists of two moving averages: one with period \( n \) (MA(n)) and another with period \( n/2 \) (MA(n/2)). The difference between these two moving averages forms the Hull difference curve. Taking the moving average of this Hull difference curve itself results in the Hull curve.

When the Hull curve is rising, it indicates that the short-term moving average has crossed above the long-term moving average, triggering a buy signal. Conversely, when the Hull curve is falling, it suggests that the short-term moving average has crossed below the long-term moving average, triggering a sell signal.

This strategy sets the Hull period \( n \) to 16. It calculates the 8-period MA (\( n/2 = 8 \)), the 16-period MA, and their difference to form the Hull curve. Then it computes the 4-period MA (square root of \( n=4 \)) of this Hull curve itself. A buy signal is triggered when the Hull curve crosses up, while a sell signal is triggered when it crosses down.

## Advantage Analysis

Compared to ordinary moving averages, the Hull Moving Average has the following advantages:

1. Reduces lag. By using a square root function, the Hull curve more closely follows price action and can catch trend reversals faster.
2. Reduces false breakouts. Traditional MAs tend to generate more false crossovers. The Hull curve can filter out some noise, avoiding unnecessary trades.
3. Fewer parameters. The Hull curve only requires one parameter \( n \), making optimization simpler. A dual-MA system needs to optimize two parameters.
4. Customizable. The \( n \) value of the Hull curve can be adjusted according to market conditions and customized for different instruments.
5. Systematic. The Hull system is robust and avoids manual selection, adhering to the consistency of mechanical trading systems.

## Risk Analysis

While the Hull system has many advantages over moving average systems, it still carries certain risks:

1. Limitations of trend following itself. As a trend-chasing strategy, Hull systems are prone to stop-outs during significant changes in trends.
2. Potential for frequent trading. The fast response characteristic of Hull curves can increase trade frequency and lead to overtrading.
3. Risk of over-optimization. Having just one parameter \( n \) can result in curve fitting issues from excessive optimization.
4. Different effectiveness across instruments. The Hull system may not perform well on highly volatile instruments, requiring adjustments to parameters.

## Improvement Directions

Based on the limitations above, improvements can be made to the Hull Moving Average strategy as follows:

1. Incorporate additional indicators to filter trade signals and avoid false breakouts. MACD, RSI, etc., can help gauge trends.
2. Add stop loss strategies to control single trade losses, such as using trailing stops or take profit limits.
3. Optimize parameter \( n \) selection to prevent over-optimization. Walk forward analysis can be used for rolling optimization.
4. Utilize machine learning models like RNNs to dynamically optimize parameter values.
5. Perform separate parameter optimizations for different instruments using machine learning fitting techniques.
6. Improve position sizing to reduce trade frequency. Fixed fractional position sizing methods can help.

## Conclusion

The Hull Moving Average strategy is a typical trend-following trading system. While it has advantages over moving averages, issues like over-optimization and frequent trading still exist. We can improve the strategy through parameter optimization, stop loss strategies, and position management techniques. The Hull system is simple and practical, warranting further research and refinement to create a robust trading system by integrating more indicators and techniques.

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | true | Long |
| v_input_2 | true | Short |
| v_input_3 | 100 | Capital, % |
| v_input_4 | 16 | HullMA period |
| v_input_5 | 1900 | From Year |
| v_input_6 | 2100 | To Year |
| v_input_7 | true | From Month |