> Name

EMA Golden Cross Short-term Trading Strategy EMA-Golden-Cross-Short-term-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1e9c30f6d9c309cc0fe.png)
[trans]

## Overview

The EMA golden cross short-term trading strategy is a short-term trading strategy based on the EMA indicator. It uses EMA lines of different periods to judge golden cross and dead cross trading signals, adopts shorter period EMA lines as entry signals, and longer period EMA lines as stop loss signals to realize a fast in and fast out short-term trading mode.

## Strategy Principles

The strategy uses 4 EMA lines with different periods: specifically, 9-period, 26-period, 100-period, and 55-period EMA lines. The trading entry signal is generated when the 9-period EMA line crosses above the 26-period EMA line; the stop-loss exit signal occurs when the 100-period EMA line crosses below the 55-period EMA line. This fast in and out approach helps to avoid being trapped.

## Advantage Analysis

1. Using the EMA indicator to determine trends is reliable, reducing false signals.
2. Utilizing different period EMA combinations can capture short-term trading opportunities.
3. The fast in and fast out method minimizes long-term losses.

## Risk Analysis

1. The EMA lines themselves have lag, which may miss the best entry opportunity.
2. Frequent short-term trades tend to increase transaction frequency and handling fee burdens.
3. Short-term trading requires higher psychological control abilities from traders.

## Optimization Direction

1. Adjusting the period parameters of the EMA line can optimize profitability.
2. Adding other indicators can filter signals and improve winning rates.
3. Setting stop-loss and stop-profit conditions can control risks associated with individual trades.

## Summary

This EMA golden cross short-term trading strategy is generally simple, easy to operate, and quick to respond. Through parameter optimization and signal filtering, its stability and profitability can be further improved. However, short-term trading also places higher demands on traders' control capabilities. In general, this strategy is suitable for investors with some trading experience to use in real trading.

||


## Overview

The EMA golden cross short-term trading strategy is a short-term trading strategy based on the EMA indicator. It uses EMA lines of different cycles to judge golden cross and dead cross trading signals, adopts shorter cycle EMA lines as entry signals, and longer cycle EMA lines as stop loss signals to realize a fast in and fast out short-term trading mode.

## Strategy Principle

The strategy uses 4 EMA lines with different cycles: specifically, 9, 26, 100, and 55 cycle EMA lines. The entry signal is generated when the 9 cycle EMA line crosses above the 26 cycle EMA line; the exit stop loss signal occurs when the 100 cycle EMA line crosses below the 55 cycle EMA line. This allows fast entry and fast exit to avoid being trapped.

## Advantage Analysis

1. Using the EMA indicator to determine trends is reliable, reducing false signals.
2. Utilizing EMA combinations of different cycles can capture short-term trading opportunities.
3. The fast in and fast out method minimizes long-term losses.

## Risk Analysis

1. EMA lines themselves have lag, which may miss the best entry timing.
2. Frequent short-term trades can easily increase transaction frequency and commission burdens.
3. Short-term trading requires higher psychological control skills from traders.

## Optimization Directions

1. Adjusting the cycle parameters of the EMA line can optimize profitability.
2. Adding other indicators can filter signals and improve win rate.
3. Setting stop loss and take profit conditions can control single trade risks.

## Summary

In general, the EMA golden cross short-term trading strategy has the characteristics of simplicity, ease of operation, and quick response. Through parameter optimization and signal filtering, its stability and profitability can be further improved. But short-term trading also raises higher requirements for traders' control capabilities. In conclusion, this strategy is suitable for investors with some trading experience to use in live trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|9|EMA_L|
|v_input_int_2|26|EMA_L2|
|v_input_int_3|100|EMA_S|
|v_input_int_4|55|EMA_S2|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-07 00:00:00
end: 2023-12-14 00:00:00
Period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © YukalMoon

//@version=5
strategy(title="EMA SCALPEUR", overlay=true, initial_capital = 1000)


//// input controls

EMA_L = input.int (title = "EMA_L", defval = 9, minval = 1, maxval = 100, step =1)
EMA_L2 = input.int (title = "EMA_L2", defval = 26, minval = 1, maxval = 100, step =1)
EMA_S = input.int (title = "EMA_S", defval = 100, minval = 1, maxval = 100, step =1)
EMA_S2 = input.int (title = "EMA_S2", defval = 55, minval = 1, maxval = 100, step =1)


/// mise en place de ema

shortest = ta.ema(close, 9)
short = ta.ema(close, 26)
longer = ta.ema(close, 100)
longest = ta.ema(close, 55)

plot(shortest, color = color.red)
plot(short, color = color.orange)
plot(longer, color = color.aqua)
plot(longest, color = color.yellow)

plot(close)

//// trading indicators

EMA1 = ta.ema (close, EMA_L)
EMA2 = ta.ema (close, EMA_L2)
EMA3 = ta.ema (close, EMA_S)
EMA4 = ta.ema (close, EMA_S2)


buy = ta.crossover(EMA1, EMA2)
//sell = ta.crossunder(EMA1, EMA2)

buyexit = ta.crossunder(EMA3, EMA4)
//sellexit = ta.crossover(EMA3, EMA4)

/////strategy

strategy.entry ("long", strategy.short, when = buy, comment = "ENTER-SHORT")
```