> Name

Dynamic-Slope-Trend-Line-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/cd3fba91d2e3a0d066.png)
[trans]
## Overview

The core idea of this strategy is to use dynamic slope to determine the price trend direction and generate trading signals by combining breakout judgments. Specifically, it tracks new highs and lows in real time based on price changes over different time periods to calculate the dynamic slope, and then determines long and short signals according to the price breaking through the trend lines.

## Strategy Principle

The main steps of this strategy are:

1. **Determine Highs and Lows**: Track the highest and lowest prices within a certain period (e.g., 20 bars) to determine whether a new high or low has been reached.
2. **Calculate Dynamic Slope**: Record the bar number when a new high or low is reached, and calculate the dynamic slope from this point to another point after a certain period (e.g., 9 bars).
3. **Plot Trend Lines**: Plot ascending and descending trend lines based on these dynamic slopes.
4. **Extend and Update Trend Lines**: When price breaks through the trend lines, extend and update the trend lines.
5. **Trading Signals**: Determine long and short signals based on the breakout of prices against the trend lines.

## Advantages of the Strategy

The advantages of this strategy include:

1. Dynamically determine the trend direction for flexibility in response to market changes.
2. Reasonably control stops and minimize drawdowns.
3. Clear breakout trading signals that are easy to implement.
4. Customizable parameters for strong adaptability.
5. Clean code structure that is easy to understand and develop further.

## Risks and Solutions

This strategy also has some risks:

1. Frequent longs and shorts when the trend is range-bound. Add filter conditions.
2. Potentially more false signals on breakouts. Adjust parameters or add filters.
3. Stop loss risks when market moves violently. Expand stop loss range.
4. Limited optimization space and profit potential, suitable for short-term trading.

## Optimization Directions

Areas for optimizing the strategy include:

1. Add more technical indicators as filter signals.
2. Optimize parameter combinations to find the best parameters.
3. Try to improve stop loss strategies to lower risks.
4. Add functionality to automatically adjust entry price range.
5. Try combining with other strategies to discover more opportunities.

## Summary

Overall, this is an efficient short-term strategy based on using dynamic slope to determine trends and trading breakouts. It has accurate judgments, controllable risks, and is suitable for capturing short-term market opportunities. Further optimizations on parameters and adding filters can improve the win rate and profitability.

||

## Overview

The core idea of this strategy is to use dynamic slope to determine the price trend direction and generate trading signals by combining breakout judgments. Specifically, it tracks new highs and lows in real time based on price changes over different periods to calculate the dynamic slope, and then determines long and short signals according to the price breaking through the trend lines.

## Strategy Principle

The main steps of this strategy are:

1. **Determine Highs and Lows**: Track the highest and lowest prices within a certain period (e.g., 20 bars) to determine whether a new high or low has been reached.
2. **Calculate Dynamic Slope**: Record the bar number when a new high or low is reached, and calculate the dynamic slope from this point to another point after a certain period (e.g., 9 bars).
3. **Plot Trend Lines**: Plot ascending and descending trend lines based on these dynamic slopes.
4. **Extend and Update Trend Lines**: When price breaks through the trend lines, extend and update the trend lines.
5. **Trading Signals**: Determine long and short signals based on the breakout of prices against the trend lines.

## Advantages of the Strategy

The advantages of this strategy include:

1. Dynamically determine the trend direction for flexibility in response to market changes.
2. Reasonably control stops and minimize drawdowns.
3. Clear breakout trading signals that are easy to implement.
4. Customizable parameters for strong adaptability.
5. Clean code structure that is easy to understand and develop further.

## Risks and Solutions

This strategy also has some risks:

1. Frequent longs and shorts when the trend is range-bound. Add filter conditions.
2. Potentially more false signals on breakouts. Adjust parameters or add filters.
3. Stop loss risks when market moves violently. Expand stop loss range.
4. Limited optimization space and profit potential, suitable for short-term trading.

## Optimization Directions

Areas for optimizing the strategy include:

1. Add more technical indicators as filter signals.
2. Optimize parameter combinations to find the best parameters.
3. Try to improve stop loss strategies to lower risks.
4. Add functionality to automatically adjust entry price range.
5. Try combining with other strategies to discover more opportunities.

## Summary

Overall, this is an efficient short-term strategy based on using dynamic slope to determine trends and trading breakouts. It has accurate judgments, controllable risks, and is suitable for capturing short-term market opportunities. Further optimizations on parameters and adding filters can improve the win rate and profitability.

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 20 | length1 |
| v_input_2 | 9 | check |
| v_input_3 | 0.2 | Take Profit |
| v_input_4 | 0.2 | Stop Loss |
| v_input_5 | 0 | What trades should be taken : : BOTH | SHORT | LONG | NONE |
| v_input_6 | false | Initial Stop Loss Points (zero to disable) |
| v_input_7 | false | Initial Target Profit Points (zero for disable) |
| v_input_8 | 2019 | Backtest Start Year |
| v_input_9 | true | Backtest Start Month |
| v_input_10 | true | Backtest Start Day |
| v_input_11 | 9999 | Backtest Stop Year |
| v_input_12 | 12 | Backtest Stop Month |
| v_input_13 | 31 | Backtest Stop Day |

## Source (PineScript)

```pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-01-19 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © pune3tghai

// Originally posted by matsu_bitmex

// Tried adding alerts on plots and cleared the chart for a cleaner view.
// Publishing the script in hope of getting it improved by someone else.

// Added strategy code for easier calculations

// Needs work on TP and SL part.

// P.S - THE ORIGINAL CODE IS MUCH BETTER BUT I have tried to be more usable and understandable.

//@version=4
strategy("TrendLines with Alerts", overlay=true)     //study("TrendLines with Alerts", overlay=true)
//update

length1 = input(20)
check = input(9)
// length2 = input(200)

u = 0.0
u := u[1]

l = 0.0
l := l[1]

y = 0.0
y := y[1]

yl = 0.0
yl := yl[1]

angle = 0.0
angle := angle[1]

anglel = 0.0
anglel := anglel[1]

if (highest(length1) == high[check] and highest(length1) == highest(length1)[check] and barssince(barstate.isfirst) > check)
    u := high[check]
    
if (lowest(length1) == low[check] and lowest(length1) == lowest(length1)[check] and barssince(barstate.isfirst) > check)
    l := low[check]
    

p = round(barssince(u == high[check]))

pl = round(barssince(l == low[check]))

if p == 0 and barssince(barstate.isfirst) > check
    y := high[abs(p[1]+1+check)]
    
if pl == 0 and barssince(barstate.isfirst) > check
    yl := low[abs(pl[1]+1+check)]    

if p == 0
    angle := (u-y)/p[1]

if pl == 0
    anglel := (l-yl)
```