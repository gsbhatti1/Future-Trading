> Name

Dynamic-Pyramiding-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1868726b948a33b1dd7.png)

[trans]

## Overview

The dynamic pyramiding strategy aims to lower the average holding cost through adding positions when price drops. This can help mitigate losses and gain additional profits when the price bounces back. The strategy will open additional positions with a certain quantity and interval when pyramiding conditions are triggered, while setting a maximum number of pyramiding times to limit the risk.

## Strategy Logic

The core logic of this strategy includes:

1. **Open Position**: Open long position with specified price if current position is 0.
2. **Pyramiding Condition**: Trigger pyramiding if current pyramiding times are less than the maximum value and the price drops below the last entry price by a preset percentage.
3. **Pyramiding Way**: Increase pyramiding quantity at a scaling factor of the previous one, and reduce interval at a scaling factor.
4. **Take Profit Condition**: Close all positions if the profit target based on average holding price is triggered.

By pyramiding with dropping prices, this strategy lowers the average cost dynamically. It stops loss efficiently and leaves more room for profits when trends reverse. When the take profit condition is triggered, all positions are exited with profit.

## Advantage Analysis

The biggest advantage of this strategy lies in gaining greater profit potential while accepting certain losses by lowering average holding costs through pyramiding. The main benefits include:

1. **Significantly reduce holding cost**: By adding additional buy orders at lower prices during drawdowns, the strategy "dilutes" previous higher entries and lowers overall cost.
2. **Increase profit range after reducing cost**: If price bounces back, the profit potential expands, paving the way for take profit.
3. **Flexible customization of pyramiding logic by setting related parameters such as increment, quantity, and interval**.
4. **Control risk by capping maximum pyramiding times**: It prevents unlimited pyramiding.

## Risk Analysis

While this strategy allows greater profit potential through pyramiding, some risks need to be acknowledged:

1. **Loss risk**: The premise is accepting certain losses from pyramiding. If the trend continues negatively, losses may increase.
2. **Cliff dive risk**: In extreme cases like a cliff-like drop in prices, losses might exceed acceptable ranges. Reasonable pyramiding settings and stop loss points are crucial.
3. **Late or missing take profit**: Price rebound might not always trigger the take profit condition, which is a shortcoming of the strategy.
4. **Parameter tuning risk**: Unsuitable settings on parameters like pyramiding coefficient and take profit percentage may lead to failure.

Below measures can help mitigate these risks:

1. **Lower increment scale** to control single entry loss amount.
2. **Narrow down pyramiding interval** to achieve faster cost reduction.
3. **Set stop loss point appropriately** rather than too loosely.

## Optimization Directions

Considering the nature of gaining higher profit potential through pyramiding, optimization directions mainly focus on better risk control and profitability enhancement:

1. **Improve pyramiding logic** to make entries more intelligent and adaptive to market conditions. Entry signals can rely on volatility, price gaps, and other metrics.
2. **Optimize take profit mechanisms** for higher efficiency, such as trailing take profit or partial closing, to reduce the chance of missing a price rebound.
3. **Introduce machine learning algorithms** to enable parameter auto-tuning. Key parameters become dynamic based on real-time feedback.
4. **Add stop loss mechanism** to limit maximum losses, such as using trailing stops and order-based stops. It prevents losses from running out of control during extreme market events.

## Conclusion

The dynamic pyramiding strategy lowers average holding cost by additional entries, enabling higher profit potential given acceptable loss tolerance. This type of strategy is particularly favored by investors with relatively high risk appetite. Future optimization directions will focus on more intelligent pyramiding logic and higher efficiency take profit mechanisms.

||

## Overview

The dynamic pyramiding strategy aims to lower the average holding cost through adding positions when price drops. It can help mitigate losses and gain additional profits when the price bounces back. The strategy will open additional positions with a certain quantity and interval when pyramiding conditions are triggered, while setting a maximum number of pyramiding times to limit the risk.

## Strategy Logic

The core logic of this strategy includes:

1. **Open Position**: Open long position with specified price if current position is 0.
2. **Pyramiding Condition**: Trigger pyramiding if current pyramiding times are less than the maximum value, and the price drops below the last entry price by a preset percentage.
3. **Pyramiding Way**: Increase pyramiding quantity at a scaling factor of the previous one, and reduce interval at a scaling factor.
4. **Take Profit Condition**: Close all positions if the profit target based on average holding price is triggered.

By pyramiding with dropping prices, this strategy lowers the average cost dynamically. It stops loss efficiently and leaves more room for profits when trends reverse. When the take profit condition is triggered, all positions are exited with profit.

## Advantage Analysis

The biggest advantage of this strategy lies in gaining greater profit potential while accepting certain losses by lowering average holding costs through pyramiding. The main benefits include:

1. **Significantly reduce holding cost**: By adding additional buy orders at lower prices during drawdowns, the strategy "dilutes" previous higher entries and lowers overall cost.
2. **Increase profit range after reducing cost**: If price bounces back, the profit potential expands, paving the way for take profit.
3. **Flexible customization of pyramiding logic by setting related parameters such as increment, quantity, and interval**.
4. **Control risk by capping maximum pyramiding times**: It prevents unlimited pyramiding.

## Risk Analysis

While this strategy allows greater profit potential through pyramiding, some risks need to be acknowledged:

1. **Loss risk**: The premise is accepting certain losses from pyramiding. If the trend continues negatively, losses may increase.
2. **Cliff dive risk**: In extreme cases like a cliff-like drop in prices, losses might exceed acceptable ranges. Reasonable pyramiding settings and stop loss points are crucial.
3. **Late or missing take profit**: Price rebound might not always trigger the take profit condition, which is a shortcoming of the strategy.
4. **Parameter tuning risk**: Unsuitable settings on parameters like pyramiding coefficient and take profit percentage may lead to failure.

Below measures can help mitigate these risks:

1. **Lower increment scale** to control single entry loss amount.
2. **Narrow down pyramiding interval** to achieve faster cost reduction.
3. **Set stop loss point appropriately** rather than too loosely.

## Optimization Directions

Considering the nature of gaining higher profit potential through pyramiding, optimization directions mainly focus on better risk control and profitability enhancement:

1. **Improve pyramiding logic** to make entries more intelligent and adaptive to market conditions. Entry signals can rely on volatility, price gaps, and other metrics.
2. **Optimize take profit mechanisms** for higher efficiency, such as trailing take profit or partial closing, to reduce the chance of missing a price rebound.
3. **Introduce machine learning algorithms** to enable parameter auto-tuning. Key parameters become dynamic based on real-time feedback.
4. **Add stop loss mechanism** to limit maximum losses, such as using trailing stops and order-based stops. It prevents losses from running out of control during extreme market events.

## Conclusion

The dynamic pyramiding strategy lowers average holding cost by additional entries, enabling higher profit potential given acceptable loss tolerance. This type of strategy is particularly favored by investors with relatively high risk appetite. Future optimization directions will focus on more intelligent pyramiding logic and higher efficiency take profit mechanisms.

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2021|From Year|
|v_input_4|true|To Month|
|v_input_5|true|To Day|
|v_input_6|9999|To Y