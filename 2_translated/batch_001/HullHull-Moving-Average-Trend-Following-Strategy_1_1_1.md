> Name

Hull Moving Average Trend Following Strategy Hull-Moving-Average-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/157eafa900f2fc0da45.png)

[trans]


## Overview

This strategy is based on the Hull Moving Average indicator to construct a trend following trading system. It decides to go long or short based on the direction of the Hull curves, making it a typical trend chasing strategy.

## Strategy Logic

This strategy uses the Hull Moving Average as the main technical indicator. The Hull Moving Average was proposed by American trader Alan Hull in 2005. It improves upon moving averages by using a square root function to reduce lag.

Specifically, the Hull Moving Average contains two averages: one is the moving average MA(n) of period n, and the other is the moving average MA(n/2) of period n/2. The difference between these two moving averages forms the Hull difference curve. Taking the moving average of this Hull difference curve itself gives the Hull curve.

When the Hull curve slopes up, it indicates that the shorter period moving average has crossed above the longer period one, triggering a long signal. When the Hull curve slopes down, it means the shorter MA has crossed below the longer MA, triggering a short signal.

This strategy sets the Hull period n to 16. It calculates the 8-period MA (n/2=8), the 16-period MA, and the difference between them to generate the Hull curve. It then takes the 4-period MA (square root of n=4) of this Hull curve itself. When the Hull curve crosses up, it goes long; when it crosses down, it goes short.

## Advantage Analysis

Compared to ordinary moving averages, the Hull Moving Average has the following advantages:

1. Reduces lag. By using a square root function, the Hull curve hugs price action closer and is quicker to catch trend reversals.
2. Reduces false breaks. Traditional moving averages tend to generate more false crosses, while the Hull curve can filter out some noise and avoid unnecessary trades.
3. Fewer parameters. The Hull curve only needs one parameter n, making optimization easier. A dual-MA system requires optimizing two parameters.
4. Customizable. The n value of the Hull curve can be adjusted for different markets and customized to suit different instruments.
5. Systematic. The Hull system is robust and avoids manual selection, adhering to the consistency of mechanical trading systems.

## Risk Analysis

Despite its advantages over moving average systems, the Hull system still carries the following risks:

1. Limitations of trend following itself. As a trend chasing strategy, Hull systems are prone to stop outs during drastic trend changes.
2. Potential for overtrading. The fast response of Hull curves may increase trade frequency and lead to overtrading.
3. Overoptimization of parameters. Having just one parameter n can lead to curve fitting risks from overoptimization.
4. Varying effectiveness across instruments. The Hull system works less well for instruments with high volatility, requiring parameter adjustments.

## Improvement Directions

Based on the limitations above, improvements to the Hull moving average strategy can be made in the following aspects:

1. Add filters with additional indicators to avoid false breaks. MACD, KD, etc., can help gauge the trend.
2. Add stop loss strategies to control single trade losses, such as trailing stops or take profit orders.
3. Optimize parameter n selection to prevent overoptimization. Walk forward analysis can be used for rolling optimization.
4. Use machine learning models like RNNs to dynamically optimize parameter values.
5. Optimize parameters separately for different instruments using machine learning fitting.
6. Optimize position sizing to lower trade frequency. Fixed fractional position sizing can help.

## Conclusion

The Hull Moving Average strategy is a typical trend following strategy. Despite its advantages over moving averages, it still faces issues like overoptimization and frequent trading. We can improve the strategy through parameter optimization, stop losses, position sizing, etc. The Hull system is simple and practical; it deserves further research and enhancement by incorporating more indicators and techniques to build a robust trading system.

||

## Overview

This strategy is based on the Hull Moving Average indicator to construct a trend following trading system. It decides to go long or short based on the direction of the Hull curves, making it a typical trend chasing strategy.

## Strategy Logic

This strategy uses the Hull Moving Average as the main technical indicator. The Hull Moving Average was proposed by American trader Alan Hull in 2005. It improves upon moving averages by using a square root function to reduce lag.

Specifically, the Hull Moving Average contains two averages: one is the moving average MA(n) of period n, and the other is the moving average MA(n/2) of period n/2. The difference between these two moving averages forms the Hull difference curve. Taking the moving average of this Hull difference curve itself gives the Hull curve.

When the Hull curve slopes up, it indicates that the shorter period moving average has crossed above the longer period one, triggering a long signal. When the Hull curve slopes down, it means the shorter MA has crossed below the longer MA, triggering a short signal.

This strategy sets the Hull period n to 16. It calculates the 8-period MA (n/2=8), the 16-period MA, and the difference between them to generate the Hull curve. It then takes the 4-period MA (square root of n=4) of this Hull curve itself. When the Hull curve crosses up, it goes long; when it crosses down, it goes short.

## Advantage Analysis

Compared to ordinary moving averages, the Hull Moving Average has the following advantages:

1. Reduces lag. By using a square root function, the Hull curve hugs price action closer and is quicker to catch trend reversals.
2. Reduces false breaks. Traditional moving averages tend to generate more false crosses, while the Hull curve can filter out some noise and avoid unnecessary trades.
3. Fewer parameters. The Hull curve only needs one parameter n, making optimization easier. A dual-MA system requires optimizing two parameters.
4. Customizable. The n value of the Hull curve can be adjusted for different markets and customized to suit different instruments.
5. Systematic. The Hull system is robust and avoids manual selection, adhering to the consistency of mechanical trading systems.

## Risk Analysis

Despite its advantages over moving average systems, the Hull system still carries the following risks:

1. Limitations of trend following itself. As a trend chasing strategy, Hull systems are prone to stop outs during drastic trend changes.
2. Potential for overtrading. The fast response of Hull curves may increase trade frequency and lead to overtrading.
3. Overoptimization of parameters. Having just one parameter n can lead to curve fitting risks from overoptimization.
4. Varying effectiveness across instruments. The Hull system works less well for instruments with high volatility, requiring parameter adjustments.

## Improvement Directions

Based on the limitations above, improvements to the Hull moving average strategy can be made in the following aspects:

1. Add filters with additional indicators to avoid false breaks. MACD, KD, etc., can help gauge the trend.
2. Add stop loss strategies to control single trade losses, such as trailing stops or take profit orders.
3. Optimize parameter n selection to prevent overoptimization. Walk forward analysis can be used for rolling optimization.
4. Use machine learning models like RNNs to dynamically optimize parameter values.
5. Optimize parameters separately for different instruments using machine learning fitting.
6. Optimize position sizing to lower trade frequency. Fixed fractional position sizing can help.

## Conclusion

The Hull Moving Average strategy is a typical trend following strategy. Despite its advantages over moving averages, it still faces issues like overoptimization and frequent trading. We can improve the strategy through parameter optimization, stop losses, position sizing, etc. The Hull system is simple and practical; it deserves further research and enhancement by incorporating more indicators and techniques to build a robust trading system.

| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_1 | true | Long |
| v_input_2 | true | Short |
| v_input_3 | 100 | Capital, % |
| v_input_4 | 16 | HullMA period |
| v_input_5 | 1900 | From Year |
| v_input_6 | 2100 | To Year |
| v_input_7 | true | From Month |