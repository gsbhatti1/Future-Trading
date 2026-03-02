> Name

Momentum Dual Moving Average Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1564f2c0a8f2cc6bfdf.png)
[trans]

## Overview

The Momentum Dual Moving Average Trading Strategy is a short-term trading strategy that leverages both price momentum and trend indicators. The strategy employs multiple indicators such as closing prices, opening prices, price channels, and fast RSI to generate trading signals. Positions are established when price breakouts or indicator signals occur. Additionally, the strategy includes stop loss conditions to forcibly close positions if losses reach a certain level.

## Strategy Principle

The strategy is based on several judgment criteria:

1. **Price Channel**: Calculate the highest and lowest prices of the past 30 candlesticks to determine the channel range. Closing price above the channel midpoint indicates bullish sentiment, while closing below it suggests bearish sentiment.
2. **Fast RSI**: Calculate the RSI value for the latest two candlesticks. An RSI below 25 is considered oversold, and an RSI above 75 is seen as overbought.
3. **Yin Yang Line Judgment**: Analyze the body size of the last two candlesticks. Two red candles signal a bearish trend, while two green candles indicate a bullish trend.
4. **Stop Loss Condition**: Force liquidation if losses reach a predetermined percentage.

By combining these multiple judgment criteria, the strategy aims to capture both trends and momentum changes, generating trading signals at potential reversal points, making it a typical short-term strategy.

## Advantage Analysis

This strategy offers several advantages:

1. **Enhanced Signal Accuracy**: By using multiple indicators, false signals are better filtered out.
2. **Faster Response to Turning Points**: The use of Fast RSI allows for quicker detection of turning points compared to regular RSI.
3. **High Reliability Across Different Products and Timeframes**: Rigorous backtesting has optimized the strategy parameters for consistent performance across various products and time periods.
4. **Automatic Stop Loss Mechanism**: This feature helps control potential losses beyond expectations.

## Risk Analysis

Several risks associated with this strategy include:

1. **Incorrect Channel Parameters**: Setting narrow channel parameters may lead to false breakouts.
2. **Extended Unilateral Position Holding Time**: During strong trends, holding positions for longer than expected can be a risk.
3. **Inappropriate Stop Loss Point Settings**: Improperly configured stop loss points can exacerbate losses.

These risks can be mitigated by adjusting the channel parameters, optimizing entry timing, and dynamically adjusting the stop loss points.

## Optimization Directions

There are several areas where this strategy can be further optimized:

1. **Machine Learning Algorithms**: Incorporating machine learning to automatically optimize parameters for better adaptability.
2. **Additional Data Sources**: Combining more data sources like news to enhance decision-making accuracy.
3. **Dynamic Position Sizing Mechanism**: Developing mechanisms to adjust positions based on market conditions to better manage risk.
4. **Futures Arbitrage Trading**: Expanding the strategy’s application to futures arbitrage for higher absolute returns.

## Conclusion

This strategy combines multiple techniques including price breakouts, indicator signals, and stop loss mechanisms. It has demonstrated good stability and performance in both backtests and live trading scenarios. As algorithm and data technologies advance, there is significant room for further optimization and improvement of the strategy.

||

## Overview

The Momentum Dual Moving Average Trading Strategy is a short-term trading strategy that leverages both price momentum and trend indicators. The strategy employs multiple indicators such as closing prices, opening prices, price channels, and fast RSI to generate trading signals. Positions are established when price breakouts or indicator signals occur. Additionally, the strategy includes stop loss conditions to forcibly close positions if losses reach a certain level.

## Strategy Principle

The strategy is based on several judgment criteria:

1. **Price Channel**: Calculate the highest and lowest prices of the past 30 candlesticks to determine the channel range. Closing price above the channel midpoint indicates bullish sentiment, while closing below it suggests bearish sentiment.
2. **Fast RSI**: Calculate the RSI value for the latest two candlesticks. An RSI below 25 is considered oversold, and an RSI above 75 is seen as overbought.
3. **Yin Yang Line Judgment**: Analyze the body size of the last two candlesticks. Two red candles signal a bearish trend, while two green candles indicate a bullish trend.
4. **Stop Loss Condition**: Force liquidation if losses reach a predetermined percentage.

With the combinational signals from trend, momentum, and overbought/oversold indicators, this short-term strategy can effectively identify reversals and generate timely trading signals.

## Advantage Analysis

The advantages of this strategy include:

1. **Improved Signal Accuracy**: By combining multiple indicators, false signals are better filtered out.
2. **Faster Responses to Turning Points**: The use of Fast RSI allows for quicker detection of turning points compared to regular RSI.
3. **High Reliability Across Different Products and Timeframes**: Rigorous backtesting has optimized the strategy parameters for consistent performance across various products and time periods.
4. **Automatic Stop Loss Mechanism**: This feature helps control potential losses beyond expectations.

## Risk Analysis

Some risks of this strategy include:

1. **Incorrect Channel Parameters Setting**: Narrow channel parameters may trigger false breakouts.
2. **Extended Unilateral Position Holding Time**: During strong trends, holding positions for longer than expected can be a risk.
3. **Improper Stop Loss Point Settings**: Improperly configured stop loss points can exacerbate losses.

These risks can be mitigated by adjusting the channel parameters, optimizing entry timing, and dynamically adjusting the stop loss points.

## Optimization Directions

There are several directions where this strategy can be further optimized:

1. **Incorporate Machine Learning Algorithms**: To achieve automatic parameter optimization and enhance adaptability.
2. **Combine More Data Sources**: Including news to improve decision-making accuracy.
3. **Develop Dynamic Position Sizing Mechanisms**: Based on market conditions to better control risks.
4. **Expand Application to Futures Arbitrage Trading**: For higher absolute returns.

## Conclusion

This strategy combines various techniques including price breakouts, indicator signals, and stop loss mechanisms. It has demonstrated good stability and performance in backtests and live trading scenarios. As algorithm and data technologies progress, significant upside remains for this strategy. Continuous improvements can be expected.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|100|capital, %|
|v_input_4|true|Use trend entry|
|v_input_5|true|Use counter-trend entry|
|v_input_6|true|Use RSI strategy|
|v_input_7|30|Price Channel Period|
|v_input_8|true|Price Channel|
|v_input_9|2018|From Year|
|v_input_10|2100|To Year|
|v_input_11|true|From Month|
|v_input_12|12|To Month|
|v_input_13|true|From day|
|v_input_14|31|To day|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-23 00:00:00
end: 2023-11-30 00:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Noro
// 2018

//@version=2
strategy(title = "Noro's Price Channel Strategy v1.2", shorttitle = "Price Channel str 1.2", overlay=true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 0)

// Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
capital = input(100, defval = 100, minval = 1, maxval = 100000, title = "capital, %")
uset = input(true, defval = true, title = "Use trend entry")
usect = input(true, defval = true, title = "Use counter-trend entry")
usersi = input(true, defval = true, title = "Use RSI strategy")
pch = input(30, defval = 30, minval = 2,