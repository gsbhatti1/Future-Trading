> Name

Dual-Moving-Average-Reversal-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/f75c2cfe80a4a1e673.png)
[trans]
## Overview

This strategy mainly utilizes the golden cross and death cross formed by the 14-day and 28-day simple moving averages to make reversal operations. When the fast moving average crosses above the slow moving average from below, it indicates the market is starting to reverse and a long position can be established. When the fast moving average crosses below the slow moving average from above, it also signals the market is reversing and a short position can be taken.

Since it uses the principle of using simple moving averages to determine changes in market trends, I named this strategy "Dual Moving Average Reversal Strategy".

## Strategy Logic

The core logic of this strategy is to use 14-day and 28-day simple moving averages with different periods to determine market trends. The specific rules are as follows:

1. The fast line is defined as the 14-day simple moving average, and the slow line is defined as the 28-day simple moving average.

2. When the fast line crosses above the slow line from below, it gives a bullish signal to go long.

3. When the fast line crosses below the slow line from above, it gives a bearish signal to go short.

4. After going long/short, when the fast line crosses below/above the slow line again, it gives the signal to close positions.

This strategy also incorporates stop loss, take profit, and trailing stop loss for risk management. For long and short positions, stop loss price, long take profit price, short take profit, and trailing stop loss price are defined separately in percentage form to make the strategy more flexible.

## Advantage Analysis

- The strategy judges market main trends using dual moving averages, with simple and clear principles easy to understand and verify.
- The moving average periods are set at 14 and 28 days, representing short-term and medium-term trend changes respectively, which can better discover reversal opportunities.
- By incorporating take profit, stop loss, and trailing stop loss to control risks, it allows profits to be locked in and avoids loss magnification.
- It can go both long and short to meet the needs of different market environments.

## Risks and Improvements

- Dual moving average crossovers have some laggingness, possibly missing the best entry timing.
- Crossovers between short and long moving averages are prone to generating false signals. Avoid setting very short moving average periods.
- If the stop loss distance is set too small, it may increase the probability of stops being hit. Reasonable stop loss distances should be set according to different products.
- More indicators can be introduced to form a combination and improve the strategy's robustness. For example, adding Bollinger Bands to judge trends, or introducing MACD to verify entry timing.

## Optimization Directions

- Test different moving average parameter combinations to find periods that match the characteristics of the product better.
- Test different stop loss distance settings to find the optimal stop loss location.
- Test the addition of other indicators for optimization to find the optimal parameter combination to reduce false signals.
- Optimize position sizing rules for more sizable profits.

## Conclusion

Overall, this is a very classic strategy based on dual moving averages to determine trend reversals. It has advantages like simple operating principles and relatively easy to grasp. At the same time, there are also some directions that can be continuously optimized afterwards. In general, this strategy is quite mature in terms of principles and operations, making it a very good introductory quantitative trading strategy.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|(ZIG) Enable Alert message {True}|
|v_input_2|0|(ZIG) Integration type: _ZIGTVONLYINTEGRATION_|_$3,_ZIGTVONLYINTEGRATION_|
|v_input_3|0|(ZIG) Provider type: _ZIGCOPYTRADERPROVIDER_|_$6,_ZIGCOPYTRADERPROVIDER_|
|v_input_4|0|(STRAT) Strategy Type: _L_|_$9,_L_|_S_|
|v_input_5|true|(DEBUG) Enable debug on order comments {True}|
|v_input_6|false|(STOPTAKE) Take Profit? {false}|
|v_input_7|true|(STOPTAKE) Stop Loss? {True}|
|v_input_8|true|(TRAILING) Enable Trailing Take Profit (%) {True}|
|v_input_9|1.1|(STOPTAKE) Take Profit % {3.0}|
|v_input_10|2|(STOPTAKE) Stop Loss % {2.0}|
|v_input_11|1.2|(TRAILING) Trailing Take Profit Trigger (%) {2.5}|
|v_input_12|25|(TRAILING) Trailing Take Profit as a percentage of Trailing Take Profit Trigger (%) {25.0}|
|v_input_13|0|(ZIG) Zignaly Alert Type {WebHook}: _ZIGNALYW_|\$21,_ZIGNALYW_
|v_input_14|0|(ZIG) Exchange: Binance,_ZIGEXKUCOIN_|_ZIGEXKUCOIN_
|v_input_15|0|(ZIG) Exchange Type {Spot}: spot,_ZIGEXFUTURES_|_Z