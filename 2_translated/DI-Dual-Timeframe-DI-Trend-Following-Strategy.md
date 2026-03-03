> Name

Dual-Timeframe-DI-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/111c29d7c1aa9328a27.png)
[trans]

## Overview

This strategy is based on the Average Directional Index (DI+) and DI-. It uses two different timeframes of DI indicators to determine the trend direction, thereby enabling long or short positions. When DI+ in both larger and smaller timeframes are higher than DI-, it indicates an upward trend and a long position should be taken; when DI- is higher than DI+ in both timeframes, it indicates a downward trend and a short position should be taken.

## Principles

The strategy mainly relies on the following principles:

1. Calculate DI+ and DI-. By using high, close, and low prices, calculate DI+ and DI-.
2. Compare DI+ and DI- across two timeframes. Calculate DI+ and DI- respectively on the main chart timeframe (e.g., 1-hour) and a larger timeframe (e.g., daily), then compare their values.
3. Determine trend direction. When DI+ is greater than DI- in both larger and smaller timeframes, it indicates an upward trend; when DI- is greater than DI+ in both timeframes, it indicates a downward trend.
4. Trigger trading signals. A long signal is triggered when DI+ > DI- on both frames; a short signal is triggered when DI- > DI+ on both frames.
5. Set stop loss. Use Average True Range (ATR) to calculate the dynamic stop loss for trend following.
6. Exit conditions. Close positions when the stop loss is hit or price reverses.

## Advantages

The strategy has the following advantages:

1. Using dual timeframes of DI can filter out some false breakouts.
2. ATR trailing stop maximizes profit protection and avoids stops being too tight.
3. Timely stop loss controls single trade losses.
4. Trading with the trend allows for continuous capture of trends.
5. Simple and clear rules, easy to implement in live trading.

## Risks and Solutions

This strategy also has some risks:

1. The DI indicator can have a lagging effect, potentially missing entry timing. Parameters can be optimized or other indicators combined.
2. Dual timeframes may show divergences between larger and smaller timeframes. Additional timeframes can validate signals.
3. An overly aggressive stop loss might cause over-trading. ATR multiplier can be loosened.
4. In sideways markets, frequent trades due to whipsaw action can occur. Filters can reduce trade frequency.
5. Parameter optimization based on historical data may lead to overfitting. Robustness of parameters should be carefully evaluated.

## Optimization Directions

The strategy can be improved in the following areas:

1. Optimize DI calculation parameters for finding the best parameter set.
2. Add other indicator filters to improve signal accuracy, such as MACD and KDJ.
3. Enhance stop loss strategies to adapt to more market conditions, like trailing stops or pending orders.
4. Add trading session filters to avoid significant news events.
5. Test parameter robustness on different products to improve adaptability.
6. Introduce machine learning components using historical data to train judgment models.

## Summary

Overall, this is a typical trend-following strategy that uses DI indicators to determine the direction of trends and sets stop losses to lock in profits while trading with the trend. The advantages lie in its clear logic and ease of implementation for live trading. There are still areas for improvement through parameter optimization and adding filters. With further refinement and robustness testing, it can become a very practical trend-following strategy.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|14|(?Directional IndicatorDI+ DI-)adx_len|
|v_input_timeframe_1||DI +/- in Timeframe 1|
|v_input_timeframe_2|1D|DI +/- in Timeframe 2|
|v_input_string_1|Long entered|(?Alerts)Alert MSG for buying (Long position)|
|v_input_string_2|Long closed|Alert MSG for closing (Long position)|
|v_input_2|timestamp(01 Apr 2020 13:30 +0000)|(?Time horizon of backtests)Backtest Start Time|
|v_input_float_1|2|(?Stop loss)ATR Multiplier for trailing stoploss|
|v_input_int_1|14|Length of ATR for trailing stoploss|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-10-31 00:00:00
end: 2023-11-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © DojiEmoji

//@version=5
strategy("DI+/- multi TF Strat [KL]", overlay=true, pyramiding=1, initial_capital=1000000000, default_qty_type=strategy.percent_of_equity, default_qty_value=5)
var string GROUP_ALERT    = "Alerts"
var string GROUP_SL       = "Stop loss"
var string GROUP_ORDER    = "Order size"
var string GROUP_TP       = "Profit taking"
var string GROUP_HORIZON  = "Time horizon of backtests"
var string GROUP_IND      = "Directional IndicatorDI+ DI-"

// ADX Indicator {
adx_len = input(14, group=GROUP_IND, tooltip="Typically 14")
```