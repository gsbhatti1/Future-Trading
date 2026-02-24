> Name

MACD Moving Average Crossover Trend Following Strategy with Trailing Stop Loss  
MACD-Moving-Average-Crossover-Trend-Following-Strategy-with-Trailing-Stop-Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/16eb3d35d99a6630493.png)

[trans]

## Overview

This strategy uses MACD to determine the trend direction, combined with EMA and SMA crossovers as confirmation. The entry signal is when the MACD histogram crosses above the signal line and the trend is upward. Stop loss is set at the price level below an ATR-calculated floating stop-loss line. The strategy also exits in batches, first to take partial profits by closing a portion of the position, then selling more as prices rise significantly to ensure larger profits, and finally holding some positions with trailing stops until the stop loss is triggered.

## Logic

### Entry Signal

When faster EMA crosses above slower EMA, it indicates that the short-term trend is better than the long-term trend, signaling a buy. Meanwhile, the faster SMA crossing above the slower SMA suggests stronger upward momentum in the short term. So the combination of MACD line crossing above the signal and an uptrend based on EMA&SMA crossovers helps identify strong entry signals.

### Stop Loss

ATR is used to calculate the stop loss level. ATR can effectively measure the price fluctuation range. When price breaks below this range, the stop loss is triggered. The ATR period can be adjusted—smaller periods allow for more precise stops but are easier to breach, while larger periods give a wider stop that is less likely to be breached. Additionally, the stop level also trails the price upside, achieving trend following.

### Exit Signals 

Exit partially on small price increases to take profits. Exit more as prices rise significantly to lock in profits. Keep some positions with trailing stops until the stop loss is hit. This helps lock in profits while still holding positions for a certain period.

## Advantages

- Using MACD to judge trend direction, combined with EMA and SMA crossovers, allows for accurate entry timing.
- ATR-calculated floating stop losses allow effective stop-loss implementation while following trends.
- Partial exits help take profits, lock in gains, and hold positions for a duration.

## Risks & Solutions

- Risk of incorrect signals from MACD and trend indicators. Fine-tune parameters or add other indicators.
- Risk of ATR stop loss being hit. Can increase ATR period or stop-loss multiplier.
- Risk of trailing positions getting trapped. Reduce the size of trailing positions and cut losses in time.

## Enhancement Opportunities 

- Optimize MACD parameters for better trend judgment.
- Optimize ATR periods to get more suitable stop-loss levels.
- Optimize exit ratios and position sizing to reduce trapping risk.
- Consider adding moving take-profit or volatility index optimization to improve stop loss settings.

## Summary

The strategy integrates the use of MACD, EMA/SMA, and other indicators to determine trend direction and entry timing accurately. The floating ATR stop loss helps in locking in profits while following trends. Exits are staggered to take profits, ensure gains, and hold positions for a duration. Overall, it is stable with decent results but can be further optimized for better returns.

|||

## Overview

This strategy uses MACD to determine the trend direction, combined with EMA and SMA crossovers as confirmation. The entry signal is when the MACD histogram crosses above the signal line and the trend is up. The stop loss is set at the price level below the floating ATR trailing stop. The strategy also exits in batches, first to take partial profits by closing a portion of the position, then selling more on larger price surges to secure bigger gains, and finally holding some positions with trailing stops until the stop loss is triggered.

## Logic

### Entry Signal

When faster EMA crosses above slower EMA, it indicates that the short-term trend is better than the long-term trend, signaling a buy. Meanwhile, the faster SMA crossing above the slower SMA suggests stronger upward momentum in the short term. So the combination of MACD line crossing above the signal and an uptrend based on EMA&SMA crossovers helps identify strong entry signals.

### Stop Loss

ATR is used to calculate the stop loss level. ATR can effectively measure the price fluctuation range. When price breaks below this range, the stop loss is triggered. The ATR period can be adjusted—smaller periods allow for more precise stops but are easier to breach, while larger periods give a wider stop that is less likely to be breached. Additionally, the stop level also trails the price upside, achieving trend following.

### Exit Signals 

Exit partially on small price increases to take profits. Exit more as prices rise significantly to lock in profits. Keep some positions with trailing stops until the stop loss is triggered. This helps lock in profits while still holding positions for a certain period.

## Advantages

- Using MACD to judge trend direction, combined with EMA and SMA crossovers, allows for accurate entry timing.
- ATR-calculated floating stop losses allow effective stop-loss implementation while following trends.
- Partial exits help take profits, lock in gains, and hold positions for a duration.

## Risks & Solutions

- Risk of incorrect signals from MACD and trend indicators. Fine-tune parameters or add other indicators.
- Risk of ATR stop loss being hit. Can increase ATR period or stop-loss multiplier.
- Risk of trailing positions getting trapped. Reduce the size of trailing positions and cut losses in time.

## Enhancement Opportunities 

- Optimize MACD parameters for better trend judgment.
- Optimize ATR periods to get more suitable stop-loss levels.
- Optimize exit ratios and position sizing to reduce trapping risk.
- Consider adding moving take-profit or volatility index optimization to improve stop loss settings.

## Summary

The strategy integrates the use of MACD, EMA/SMA, and other indicators to determine trend direction and entry timing accurately. The floating ATR stop loss helps in locking in profits while following trends. Exits are staggered to take profits, ensure gains, and hold positions for a duration. Overall, it is stable with decent results but can be further optimized for better returns.

|||

> Strategy Arguments

|Argument  |Default   |Description                   |
|----------|----------|------------------------------|
|v_input_1 |34        |Period                        |
|v_input_2 |3         |Fast Length                   |
|v_input_3 |5         |Slow Length                   |
|v_input_4_close|0       |Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5  |2         |Signal Smoothing              |
|v_input_6  |false     |Simple MA (Oscillator)        |
|v_input_7  |true      |Simple MA (Signal Line)       |
|v_input_8  |true      |Long Take Profit 1 %          |
|v_input_9  |10        |Long Take Profit 1 Qty        |
|v_input_10 |5         |Long Take Profit 2%           |
|v_input_11 |50        |Long Take Profit 2 Qty        |
|v_input_12 |2.2       |SL Multiplier                 |
|v_input_13 |17        |ATR period                    |
|v_input_14 |2018      |Backtest Start Year           |
|v_input_15 |true      |Backtest Start Month          |
|v_input_16 |true      |Backtest Start Day            |
|v_input_17 |2020      |Backtest Stop Year            |
|v_input_18 |12        |Backtest Stop Month           |
|v_input_19 |31        |Backtest Stop Day             |

> Source (PineScript)

```pinescript
/*backtest
start: 2022-10-30 00:00:00
end: 2023-11-05 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Deobald

//@version=4
strategy("MACD Strategy", overlay=true)

// FUNCTIONS

Ema(src,p) =>
    ema = 0.
    sf = 2/(p+1)
    ema := nz(ema[1] + sf*(src - ema[1]),src)

Sma(src,p) => a = cum(src), (a - a[max(p,0)])/max(p,0)

Atr(p) =>
    atr = 0.
    Tr = max(high - low, max(abs(high - close[1]), abs(low - close[1])))
    atr := nz(atr[1] + (Tr - atr[1])/p,Tr)

/// TREND
ribbon_period = input(34, "Period", step=1)

leadLine1 = ema(close, ribbon_period)
leadLine2 = sma(close, ribbon_period)

p3 = plot(leadLine1, title="Faster EMA", color=color.blue)
p4 = plot(leadLine2, title="Slower EMA", color=color.red)
fill(p3, p4, color=color.new(color.blue, 90))

// MACD
fast_length = input(title="Fast Length", type=input.integer, defval=3)
slow_length = input(title="Slow Length", type=input.integer, defval=5)
```


This completes the translation and adjustment of your strategy description and source code. Let me know if you need any further modifications or additional details!