> Name

Dynamic-Average-Price-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1633f4a00aec7199bfc.png)
[trans]

## Overview

The main idea of this strategy is to gradually increase the position when the stock price falls to a certain percentage, thereby reducing the average cost of the holding position. When prices rebound, higher returns can be obtained due to the lower average holding cost.

## Strategy Principle  

When the stock price first crosses above the 20-day simple moving average, go long to open a position. If the stock then falls by the target loss percentage set, such as 10%, add to the position at a specified percentage, such as 50% of the current position. This lowers the average cost of the holding position. When the stock price reaches the set take profit point, such as 10% above the average holding cost, close all positions to take profit.

Specifically, the strategy function sets parameters such as allowing up to 4 additional purchases, with position sizing set as a percentage of equity, and the initial position size at 10% of equity. It gets the 20-day simple moving average line. When the closing price crosses above that average and there is no current position, it opens a long position. It then calculates the floating profit/loss percentage of the position. If it reaches the target loss percentage, it continues pyramiding at the target additional purchase percentage until the stock rebounds to hit the profit target.

## Advantage Analysis

The biggest advantage of this type of strategy is that when market conditions are unfavorable, the average cost of the holding position can be reduced through pyramiding additional purchases. This allows greater profits to be obtained when market conditions improve, achieving the "lose less, earn more" effect. Compared to simple stop losses, this strategy can better capture market movements rather than being forced to stop loss when prices continue falling.

At the same time, the strategy allows multiple additional purchases, making maximum use of timing differences in market reversals to gradually adjust positions. This has lower cost than making one large additional purchase, and also fits better with most investors' capital strengths.

## Risk Analysis

Of course, if prices continue falling, this strategy also faces the risk of major losses. Especially in bear markets, the extent of price declines may far exceed our imagination. Therefore, the proportion and number of additional purchases must be reasonably set to control risk within an acceptable range.

At the same time, we must realize that if all investors adopt such a strategy, when a lot of investors reach their loss percentage target there could be a collective adding to positions scenario. This would drive up prices and form an irrational short-term rebound. If we fail to assess the situation properly, we could wrongly judge the market trend and continue increasing our position. The result would be even greater losses when prices plunge again.

## Optimization Directions

There are several ways this strategy can be optimized:

1. Dynamically adjust the additional purchase percentage. This could be adjusted in real time based on market conditions.
2. Incorporate quantitative indicators. For example, monitor surges in volume to confirm reversal signals and avoid false signals.
3. Adopt trailing stop losses. After additional purchases, use a progressive stop loss system to ensure losses are kept within a certain range.

## Summary

The dynamic average price tracking strategy makes use of the average price effect by adjusting positions through additional purchases. Within the premise of having sufficient capital support, it can effectively capture above average returns when prices reverse. The key is properly judging timing and proportions to keep risks within acceptable ranges. If applied appropriately, this can be a very effective method in quantitative trading.

||

## Overview

The main idea of this strategy is that when the stock price falls to a certain percentage, positions can be gradually increased to lower the average cost of the holding position. When prices rebound, higher returns can be obtained due to the lower average holding cost.

## Strategy Principle  

When the stock price first crosses above the 20-day simple moving average, go long to open a position. If the stock then falls by the target loss percentage set, such as 10%, add to the position at a specified percentage, such as 50% of the current position. This lowers the average cost of the holding position. When the stock price reaches the set take profit point, such as 10% above the average holding cost, close all positions to take profit.

Specifically, the strategy function sets parameters such as allowing up to 4 additional purchases, with position sizing set as a percentage of equity, and the initial position size at 10% of equity. It gets the 20-day simple moving average line. When the closing price crosses above that average and there is no current position, it opens a long position. It then calculates the floating profit/loss percentage of the position. If it reaches the target loss percentage, it continues pyramiding at the target additional purchase percentage until the stock rebounds to hit the profit target.

## Advantage Analysis

The biggest advantage of this type of strategy is that when market conditions are unfavorable, the average cost of the holding position can be reduced through pyramiding additional purchases. This allows greater profits to be obtained when market conditions improve, achieving the "lose less, earn more" effect. Compared to simple stop losses, this strategy can better capture market movements rather than being forced to stop loss when prices continue falling.

At the same time, the strategy allows multiple additional purchases, making maximum use of timing differences in market reversals to gradually adjust positions. This has lower cost than making one large additional purchase, and also fits better with most investors' capital strengths.

## Risk Analysis

Of course, if prices continue falling, this strategy also faces the risk of major losses. Especially in bear markets, the extent of price declines may far exceed our imagination. Therefore, the proportion and number of additional purchases must be reasonably set to control risk within an acceptable range.

At the same time, we must realize that if all investors adopt such a strategy, when a lot of investors reach their loss percentage target there could be a collective adding to positions scenario. This would drive up prices and form an irrational short-term rebound. If we fail to assess the situation properly, we could wrongly judge the market trend and continue increasing our position. The result would be even greater losses when prices plunge again.

## Optimization Directions

There are several ways this strategy can be optimized:

1. Dynamically adjust the additional purchase percentage. This could be adjusted in real time based on market conditions.
2. Incorporate quantitative indicators. For example, monitor surges in volume to confirm reversal signals and avoid false signals.
3. Adopt trailing stop losses. After additional purchases, use a progressive stop loss system to ensure losses are kept within a certain range.

## Summary

The dynamic average price tracking strategy makes use of the average price effect by adjusting positions through additional purchases. Within the premise of having sufficient capital support, it can effectively capture above average returns when prices reverse. The key is properly judging timing and proportions to keep risks within acceptable ranges. If applied appropriately, this can be a very effective method in quantitative trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2010|From Year|
|v_input_4|true|To Month|
|v_input_5|true|To Day|
|v_input_6|9999|To Year|
|v_input_7|-10|Target Loss to Average Down (%)|
|v_input_8|10|Target Take Profit|
|v_input_9|50|% Of Current Holdings to Buy|
|v_input_10|20|SMA Period|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

// ########################################################################## // 
//
// This script is intended to demonstrate how pyramiding can be used to average
// down a position.
//
// We will buy when a stock closes above its 20 day MA and Add