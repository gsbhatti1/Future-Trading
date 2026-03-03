> Name

Myo_LS_D Quantitative Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1349a0e28875de1ec72.png)

[trans]
# Myo_LS_D Quantitative Strategy

## Overview
The Myo_LS_D quantitative strategy is a dual-track tracking stop-profit strategy based on long and short positions. The strategy combines multiple indicators such as moving averages, price breaks, and risk-return ratios to build trading signals. It achieves a high win rate and profit rate on the premise of accurate trend judgment.

## Principle  
The strategy consists mainly of a trend judgment module, long position module, short position module, tracking stop profit module, etc.

1. The trend judgment module uses the Donchain channel to determine the overall trend direction. The prerequisite for going long is an upward trend, while going short requires a downward trend.

2. The long position module takes into account factors such as new highs, lows, long-term moving average positions, etc. The short position module considers new highs, lows, short-term moving average positions, and other factors. This ensures the opening of positions when breaking through critical price points upwards or downwards.

3. The tracking stop profit module uses two SMA moving averages of different cycles to track price changes in real time. When the price breaks through the moving average line, the position is closed for profit. This kind of real-time tracking can maximize profits from the trend.

4. Stop loss setting considers enlarged stop loss to keep the stop loss point far away from the support level to avoid being knocked out.

## Advantage Analysis 
The biggest advantage of this strategy is the separate long and short position building and tracking stop profit strategy. Specifically, it is mainly embodied in:

1. Separate long and short positions can maximize profit opportunities by capturing one-sided trend trading opportunities.

2. Tracking stop profit can obtain higher profit margin through real-time adjustment. Compared with traditional stop profit methods, income can be significantly improved.

3. Enlarged stops can reduce the probability of being knocked out and reduce the risk of losses.

## Risk and Solutions
The main risks of this strategy are concentrated in the following points:

1. Incorrect trend judgment may result in contrarian positions and losses. Optimization can be achieved by appropriately adjusting Donchain parameters or adding other indicators for judgment.

2. Tracking stop profit is too aggressive and may prematurely stop profit without being able to sustain gains. Optimization can be achieved by appropriately increasing the spacing between stop profit moving averages.

3. The stop loss range is too small, which may increase the probability of being knocked out. Appropriately expanding the stop loss magnitude can mitigate risks.

## Optimization Directions
The main optimization directions for this strategy are:

1. Optimize the trend judgment module to improve judgment accuracy. Consider combining more indicators such as MACD.

2. Adjust the tracking stop profit method to further expand profit space. For example, moving stop profit lines in proportion.

3. Expanding the stop loss range or considering shrinkage stops can further reduce the probability of being knocked out.

4. Different varieties have different parameters. Optimal parameter combinations can be obtained through training to further improve strategy returns.

## Summary 
In general, the Myo_LS_D strategy is a relatively mature and stable dual-track tracking stop-profit quantitative strategy. It has obvious advantages and controllable risks. It is one of the quantitative solutions worth holding for the long term. Future optimizations can enable continuous performance improvement to make it an even more superior quantitative strategy.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|100|Long position stop loss length|
|v_input_int_2|100|Short position stop loss length|
|v_input_int_3|0|Long position tracking stop profit SMA length 1: 10|5|40|60|80|
|v_input_int_4|0|Long position tracking stop profit SMA length 2: 20|10|5|40|60|80|
|v_input_int_5|0|Short position tracking stop profit SMA length 1: 5|10|20|40|60|80|
|v_input_int_6|0|Short position tracking stop profit SMA length 2: 10|5|20|40|60|80|
|v_input_int_7|0|Long trend line: 400|200|300|100|500|
|v_input_int_8|0|Short trend line: 300|200|100|400|500|
|v_input_int_9|20|Short-term moving average K-line number|
|v_input_int_10|60|Medium-term moving average K-line number|
|v_input_int_11|120|Long-term moving average K-line number|
|v_input_int_12|8|Trend benchmark line|
|v_input_int_13|26|Short position benchmark line|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-15 00:00:00
end: 2024-01-14 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © agresiynin

//@version=5
// ©Myo_Pionex
strategy(
    title                  = "Myo_LS_D Simple Strategy",
    shorttitle             = "Myo_LS_D",
    overlay                 = false
)
```