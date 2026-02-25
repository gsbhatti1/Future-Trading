> Name

Dynamic-Pyramiding-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1868726b948a33b1dd7.png)

[trans]

## Overview

The dynamic pyramiding strategy achieves cost averaging through adding positions when the price drops, thereby achieving the purpose of stop loss recovery. When the market triggers the pyramiding condition, this strategy will add positions in a certain quantity and interval until reaching the maximum number of additions to prevent infinite pyramiding.

## Strategy Principle

The core logic of this strategy is as follows:

1. Opening Position: If the current position is zero, place an order at the specified price to open a new position.
2. Pyramiding Condition: When the current number of pyramiding times is less than the maximum allowed and the price drops below the previous entry price by a predefined percentage, this condition will be triggered.
3. Pyramiding Method: The added quantity increases in proportion to the previous one, while the interval between additions decreases in proportion to the previous one.
4. Take Profit Condition: When the profit target based on the average holding cost is reached, all positions are closed for a take profit.

This way, when market conditions are unfavorable, the strategy can lower the overall cost by continuously adding positions during a drawdown and achieving additional profits through stop loss recovery. When the market trend reverses upward, the take profit condition will be triggered, allowing all open positions to be closed with gains.

## Advantages Analysis

The biggest advantage of this strategy lies in its ability to achieve higher profit potential at an acceptable level of risk by lowering average holding cost using pyramiding. The main benefits include:

1. Significantly reducing the overall holding cost and enhancing stop loss capabilities. When a drawdown occurs, additional positions are added at lower prices, "diluting" previous higher entries and reducing the total cost.
2. Expanding profit potential after cost reduction. If the price bounces back, the expanded profit range paves the way for take profit opportunities.
3. Flexibility in customizing pyramiding logic by setting parameters such as increment, quantity, interval, etc., to suit individual preferences.
4. Controlling risk through setting a maximum number of additions to prevent infinite pyramiding.

## Risk Analysis

While this strategy provides greater profit potential with pyramiding, several risks need careful consideration:

1. Loss Risk - The premise is that the strategy can tolerate certain losses from adding positions during drawdowns. If market conditions remain unfavorable, losses could increase.
2. Cliff Divergence Risk - In extreme market events like a sudden drop (cliff divergence), the risk of incurring losses beyond acceptable levels may arise. Reasonable pyramiding settings and stop loss points are crucial to mitigate this risk.
3. Late or Missed Take Profit - A price rebound might not always trigger the take profit condition, which is a shortcoming of the strategy.
4. Parameter Tuning Risk - Unsuitable settings for parameters such as the pyramiding coefficient and take profit percentage may lead to failure.

To mitigate these risks:

1. Scale down the increment size to control the single entry loss amount.
2. Shorten the interval between additions to achieve faster cost reduction.
3. Set appropriate stop loss points rather than overly loose ones.

## Optimization Directions

Considering the nature of this strategy, which seeks higher profit potential through pyramiding, the main optimization directions focus on better risk management and profitability enhancement:

1. Improve the logic for triggering additional positions to make it more intelligent and adaptive to market conditions. Entry signals could be based on volatility, price gaps, and other metrics.
2. Optimize take profit mechanisms for greater efficiency, such as trailing stop losses or partial closeouts, to lower the risk of missing a rebound.
3. Introduce machine learning algorithms to enable dynamic parameter tuning based on real-time market feedback.
4. Add a stop loss mechanism to limit maximum potential losses, using features like trailing stops and conditional orders.

## Conclusion

The dynamic pyramiding strategy lowers average holding cost by continuously adding positions during drawdowns, enabling higher profit potential given an acceptable level of risk. This type of strategy is particularly favored by investors with relatively high risk tolerance. Future optimization efforts will focus on more intelligent pyramiding logic, more efficient take profit mechanisms, and other improvements.

||

## Overview

The dynamic pyramiding strategy aims to lower the average holding cost through adding additional positions when the price drops, thereby achieving stop loss recovery and gaining additional profits during market rebounds. The strategy opens new positions with a certain quantity and interval when pyramiding conditions are triggered, up until reaching the maximum number of additions to avoid unlimited pyramiding.

## Strategy Logic

The core logic of this strategy includes:

1. Opening Position: Open a long position at the specified price if there is no current position.
2. Pyramiding Condition: Trigger additional positions when the current number of pyramiding times is less than the maximum allowed and the price drops below the previous entry price by a predefined percentage.
3. Pyramiding Method: Increase the added quantity in proportion to the previous one, and reduce the interval between additions in proportion to the previous one.
4. Take Profit Condition: Close all positions if the profit target based on the average holding cost is reached.

By continuously adding positions during price drops, this strategy lowers the overall average cost dynamically. It effectively stops losses and leaves more room for profits when market trends reverse. Once a take profit condition is triggered, all open positions are closed to secure gains.

## Advantage Analysis

The main advantages of this strategy lie in its ability to achieve higher profit potential with an acceptable level of risk by lowering the average holding cost using pyramiding. The primary benefits include:

1. Significantly reducing overall holding costs and enhancing stop loss capabilities. When a drawdown occurs, additional positions are added at lower prices, "diluting" previous higher entries and reducing total costs.
2. Expanding profit potential after cost reduction. If the price bounces back, the expanded profit range paves the way for take profit opportunities.
3. Flexibility in customizing pyramiding logic by setting parameters such as increment, quantity, interval, etc., to suit individual preferences.
4. Controlling risk through setting a maximum number of additions to prevent unlimited pyramiding.

## Risk Analysis

While this strategy provides greater profit potential with pyramiding, several risks need careful consideration:

1. Loss Risk - The premise is that the strategy can tolerate certain losses from adding positions during drawdowns. If market conditions remain unfavorable, losses could increase.
2. Cliff Divergence Risk - In extreme market events like a sudden drop (cliff divergence), the risk of incurring losses beyond acceptable levels may arise. Reasonable pyramiding settings and stop loss points are crucial to mitigate this risk.
3. Late or Missed Take Profit - A price rebound might not always trigger the take profit condition, which is a shortcoming of the strategy.
4. Parameter Tuning Risk - Unsuitable settings for parameters such as the pyramiding coefficient and take profit percentage may lead to failure.

To mitigate these risks:

1. Scale down the increment size to control the single entry loss amount.
2. Shorten the interval between additions to achieve faster cost reduction.
3. Set appropriate stop loss points rather than overly loose ones.

## Optimization Directions

Considering the nature of this strategy, which seeks higher profit potential through pyramiding, the main optimization directions focus on better risk management and profitability enhancement:

1. Improve the logic for triggering additional positions to make it more intelligent and adaptive to market conditions. Entry signals could be based on volatility, price gaps, and other metrics.
2. Optimize take profit mechanisms for greater efficiency, such as trailing stop losses or partial closeouts, to lower the risk of missing a rebound.
3. Introduce machine learning algorithms to enable dynamic parameter tuning based on real-time market feedback.
4. Add a stop loss mechanism to limit maximum potential losses, using features like trailing stops and conditional orders.

## Conclusion

The dynamic pyramiding strategy lowers average holding cost by continuously adding positions during drawdowns, enabling higher profit potential given an acceptable level of risk. This type of strategy is particularly favored by investors with relatively high risk tolerance. Future optimization efforts will focus on more intelligent pyramiding logic, more efficient take profit mechanisms, and other improvements.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2021|From Year|
|v_input_4|true|To Month|
|v_input_5|true|To Day|
|v_input_6|9999|To Y