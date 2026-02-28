> Name

RSI Mean Reversion Price Fluctuation Strategy RSI-Mean-Reversion-Price-Fluctuation-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy identifies oversold opportunities using the RSI indicator and takes positions in batches when prices fall to gradually lower the cost basis and achieve long-term profits. It also incorporates a DCA mechanism to further manage risks.

## Strategy Logic

The strategy first calculates the RSI indicator to determine if the market is oversold. When the RSI is below 30, it signals an oversold opportunity. In this case, if the price is below the 100-period moving average, a long position will be opened.

After opening the position, the strategy sets up 6 mean reversion price levels at 98%, 97%, 95%, 90%, 84%, and 70% of the current price. When the price hits these levels, more positions will be added. By constantly averaging down, the cost basis of the position can be lowered.

In addition, the average price of the position is calculated. Profit taking starts when the price rises more than 5% above the average price. Also, if the price continues to rise above the 5% take profit price of the average price, all positions will be closed.

Finally, a DCA mechanism is incorporated into the strategy. Every Monday, if there are open positions and the price is below the average price, a fixed amount will be added to the position. This further reduces the cost basis.

## Advantage Analysis

The biggest advantage of this strategy is the utilization of averaging down and DCA mechanisms to control risks. Specifically:

1. Taking positions in batches diversifies the opening risk and avoids missing the lowest point.
2. Setting multiple mean reversion price levels steadily lowers the cost basis and manages the downside risk.
3. Calculating the average position price allows for timely profit taking and locking in profits when in the green.
4. Applying DCA further reduces the cost basis and controls risk.
5. Using the RSI indicator prevents opening positions at tops.
6. The moving average filter avoids reversal trades.

## Risk Analysis

The strategy also has some risks:

1. The strategy cannot determine market reversal points, which means persistent long positions during prolonged market bottoms will increase losses.
2. There is no stop loss mechanism to effectively control single trade loss.
3. There is no limit on the number of positions, which can lead to runaway additions if the market crashes violently.
4. DCA carries timing risk and does not guarantee opening positions at the lowest point.

Possible solutions:

1. Incorporate other indicators to judge market structure instead of purely relying on RSI.
2. Add moving or staggered stop loss.
3. Limit the number of position additions.
4. Optimize DCA entry logic to a more stable mechanism.

## Optimization Directions

The strategy can be improved in the following ways:

1. Optimize the mean reversion algorithm to a more scientific approach.
2. Enhance profit taking mechanisms, such as trailing stop or layered take profit.
3. Add stop loss for better single trade risk control.
4. Incorporate other indicators for market structure analysis instead of purely RSI.
5. Optimize DCA logic to avoid fixed time entry risks.
6. Add position sizing to optimize total position size.
7. Optimize parameters to suit market statistical characteristics.
8. Add switching logic to adapt to different market regimes.

## Conclusion

In summary, this is a long-term investment strategy utilizing RSI for timing and averaging down with multiple entries to lower cost basis. It is well suited for the current volatile cryptocurrency market to manage position costs during ranging periods. There is also room for improving the mechanisms to incorporate more indicators for market analysis and risk management to enable the strategy to thrive in more complex environments.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|15|Portfolio %|
|v_input_2|++++|+++++ Long Positions VA Layers +++++|
|v_input_3|2|2nd Long Entry %|
|v_input_4|3|3rd Long Entry %|
|v_input_5|5|4th Long Entry %|
|v_input_6|10|5th Long Entry %|
|v_input_7|16|6th Long Entry %|
|v_input_8|++++|+++++ Moving Average Filter +++++|
|v_input_9|false|Plot Moving Average|
|v_input_10|100|v_input_10|
|v_input_11|++++|+++++ RSI Inputs +++++|
|v_input_12|14|length|
|v_input_13|30|oversold, entry trigger long position|
|v_input_14|70|overbought, has no specific function|
|v_input_15|++++|+++++ Take Profit +++++|
|v_input_16|5|ProfitTarget_Percent|
|v_input_17|++++|+++++ Open DCA order once every week +++++|
|v_input_18|false|Buy a fixed amount on Monday if open positions exist and price is below average price|