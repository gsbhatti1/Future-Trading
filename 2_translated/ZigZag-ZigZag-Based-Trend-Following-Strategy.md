> Name

ZigZag-Based-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/195b667574c43be95b7.png)

[trans]


## Overview

This strategy uses the ZigZag indicator to determine trend direction and follows the trend once confirmed. It belongs to the trend following strategy.

## Strategy Logic

The strategy mainly uses the ZigZag indicator to determine the price trend direction. The ZigZag can filter market noise and identify major price fluctuation directions. It generates trading signals when prices reach new highs or lows.

Specifically, the strategy first calculates the ZigZag values. When prices reach a higher high, the ZigZag value becomes the high price; when prices reach a lower low, the ZigZag value becomes the low price. Thus, ZigZag can clearly reflect the main price fluctuation direction.

The strategy determines the trend direction based on ZigZag values. When ZigZag rises, it indicates an upward trend; when ZigZag falls, it indicates a downward trend. The strategy opens positions when ZigZag turns around to follow the trend direction.

In particular, the strategy goes long when ZigZag turns to a new high, and goes short when ZigZag turns to a new low. The exit condition is when ZigZag turns around again. This achieves auto trading based on ZigZag for trend identification.

## Advantage Analysis

- ZigZag can effectively filter market noise and accurately determine the major trend direction.
- ZigZag turn timing is precise, allowing optimal entry opportunities.
- It implements a pure trend following strategy without other complex indicators or models.
- The logic is simple and clear, easy to understand and modify.
- The trading frequency can be freely controlled via parameter tuning.

## Risk Analysis

- ZigZag is insensitive to medium-term trend reversals, potentially missing faster reversals.
- Trend following strategies cannot handle losses from trend reversals.
- It does not limit the loss size of single trades, posing large single loss risks.
- The strategy relies solely on one indicator, risking overfitting.

Risks can be reduced by:

- Combining other indicators to detect trend reversal risks.
- Shortening holding period, timely stop loss.
- Adding risk management to limit single loss size. 
- Adding machine learning models to improve robustness.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Add stop loss to control single loss risk, e.g., trailing stop or stop limit orders.
2. Add trend reversal detection mechanisms, e.g., MACD, moving averages. Close positions when reversal is detected.
3. Add re-entry module. Pyramid positions when trend continues.
4. Add machine learning models like LSTM to assist trend detection.
5. Optimize capital management based on drawdown or correlation theories.
6. Comprehensively optimize parameters like ZigZag period by backtesting and referencing expertise.

## Summary

The strategy identifies trend direction by ZigZag and trades the trend. The logic is simple and easy to implement. But risks like single indicator reliance and trend reversal exist. We can optimize via stop loss, auxiliary indicators, re-entry, machine learning models etc., to make it more robust and rational. With proper parameters and risk controls, it can effectively track medium-long term trends.

||


## Overview

This strategy uses the ZigZag indicator to determine trend direction and follows the trend once confirmed. It belongs to the trend following strategy.

## Strategy Logic

The strategy mainly uses the ZigZag indicator to determine the price trend direction. The ZigZag can filter market noise and identify major price fluctuation directions. It generates trading signals when prices reach new highs or lows.

Specifically, the strategy first calculates the ZigZag values. When prices reach a higher high, the ZigZag value becomes the high price; when prices reach a lower low, the ZigZag value becomes the low price. Thus, ZigZag can clearly reflect the main price fluctuation direction.

The strategy determines the trend direction based on ZigZag values. When ZigZag rises, it indicates an upward trend; when ZigZag falls, it indicates a downward trend. The strategy opens positions when ZigZag turns around to follow the trend direction.

In particular, the strategy goes long when ZigZag turns to a new high, and goes short when ZigZag turns to a new low. The exit condition is when ZigZag turns around again. This achieves auto trading based on ZigZag for trend identification.

## Advantage Analysis

- ZigZag can effectively filter market noise and accurately determine the major trend direction.
- ZigZag turn timing is precise, allowing optimal entry opportunities.
- It implements a pure trend following strategy without other complex indicators or models.
- The logic is simple and clear, easy to understand and modify.
- The trading frequency can be freely controlled via parameter tuning.

## Risk Analysis

- ZigZag is insensitive to medium-term trend reversals, potentially missing faster reversals.
- Trend following strategies cannot handle losses from trend reversals.
- It does not limit the loss size of single trades, posing large single loss risks.
- The strategy relies solely on one indicator, risking overfitting.

Risks can be reduced by:

- Combining other indicators to detect trend reversal risks.
- Shortening holding period, timely stop loss.
- Adding risk management to limit single loss size. 
- Adding machine learning models to improve robustness.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Add stop loss to control single loss risk, e.g., trailing stop or stop limit orders.
2. Add trend reversal detection mechanisms, e.g., MACD, moving averages. Close positions when reversal is detected.
3. Add re-entry module. Pyramid positions when trend continues.
4. Add machine learning models like LSTM to assist trend detection.
5. Optimize capital management based on drawdown or correlation theories.
6. Comprehensively optimize parameters like ZigZag period by backtesting and referencing expertise.

## Summary

The strategy identifies trend direction by ZigZag and trades the trend. The logic is simple and easy to implement. But risks like single indicator reliance and trend reversal exist. We can optimize via stop loss, auxiliary indicators, re-entry, machine learning models etc., to make it more robust and rational. With proper parameters and risk controls, it can effectively track medium-long term trends.

---

## Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Long|
|v_input_2|false|Short|
|v_input_3|100|Capital, %|
|v_input_4|W|Timeframe for ZigZag|
|v_input_5|false|Show ZigZag|
|v_input_6|false|Show Background|
|v_input_7|1900|From Year|
|v_input_8|2100|To Year|
|v_input_9|true|From Month|
|v_input_10|12|To Month|
|v_input_11|true|From day|
|v_input_12|31|To day|

---

## Source (PineScript)

```pinescript
/*backtest
start: 2022-10-23 00:00:00
end: 2023-04-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Noro
//2018

//@version=2
strategy(title = "Noro's ZZ Strategy v1.0", shorttitle = "ZZ str 1.0", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 0)

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(false, defval = false, title = "Short")
capital = input(100, defval = 100, minval = 1, maxval = 10000, title = "Capital, %")
tf = input('W', title='Timeframe for ZigZag')
showzz = input(false, defval = false, title = "Show ZigZag")
showbg = input(false, defval = false, title = "Show Background")
fromyear = input(1900, defval = 1900, minval = 1900, maxval = 2100, title = "From Year")
toyear = input(2100, defval = 2