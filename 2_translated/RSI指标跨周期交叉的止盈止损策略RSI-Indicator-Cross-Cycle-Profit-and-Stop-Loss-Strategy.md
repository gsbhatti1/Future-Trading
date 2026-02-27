> Name

RSI Indicator Cross Cycle Profit and Stop Loss Strategy RSI-Indicator-Cross-Cycle-Profit-and-Stop-Loss-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1684ed6cea6bb3d35f2.png)
[trans]

## Overview

This strategy uses the RSI indicator to determine entry timing through cross-cycle judgments and employs the ATR mechanism for profit-taking and stop-loss, making it a type of trend-following strategy. It determines market trend turning points by crossing different cycle RSI indicators and combines closing prices to filter long and short positions. The profit-taking and stop-loss mechanisms effectively control risks and lock in profits.

## Strategy Principle

The strategy first uses SMA smoothing technology to calculate the 26-week moving average as a benchmark for judging the bull market. Then, it calculates the 4-week RSI indicator value; when it crosses below 30 in the oversold area, it is considered that the market may rebound. At this time, it judges whether the new high of the shortdays parameter can break through the recent new high of the longdays parameter, indicating a strengthening short-term trend. If all these conditions are met simultaneously, a long signal is issued.

After entering the market, use ATR indicator multiples as profit range and stop loss at a certain percentage of the closing price high point.

## Advantages of the Strategy

The strategy has the following advantages:

1. Use the RSI indicator to determine reversal points with good timing ability.
2. Apply the new highs and lows mechanism to avoid false signals.
3. Utilize ATR for profit-taking and stop-loss, automatically tracking optimal exit points.
4. Flexible parameter settings can be adjusted to optimal levels.
5. The strategy idea is clear and easy to understand, with strong stability.

## Risks of the Strategy

The strategy also has the following risks:

1. The RSI indicator may issue a wrong signal, leading to improper entry timing. Adjusting RSI parameters or adding other indicators for filtering can help.
2. The ATR profit range may be set too large or too small, failing to lock in maximum profits. Testing better parameter combinations can improve this.
3. Stop loss points are too close and may be broken by market movements. Appropriately relaxing the stop loss distance is recommended.
4. Insufficient backtest data may overestimate the strategy’s returns. Increasing the backtest period and testing different market environments are necessary.

## Strategy Optimization

The strategy can be optimized in the following aspects:

1. Test and optimize RSI parameters and profit/loss multiples to find the best parameter combination.
2. Increase other indicators to improve accuracy, such as MACD, KD, etc.
3. Optimize stop loss mechanisms by dynamically adjusting based on ATR fluctuation ranges.
4. Test performance across different trading instruments. Choose liquid and highly volatile varieties.
5. Compare the performance of different types of stop losses, including proportional stops and moving stops.

## Summary

Overall, this strategy operates clearly and smoothly with reasonable indicator selection and parameter settings, making it highly practical. Further improvements through parameter optimization and mechanism refinement are still possible. In summary, the strategy has a relatively high ability to generate stable profits. It is worth debugging in real trading environments and implementing for use.

||

## Overview

This strategy uses the RSI indicator to determine entry timing through cross-cycle judgments and employs the ATR mechanism for profit-taking and stop-loss, making it a type of trend-following strategy. It determines market trend turning points by crossing different cycle RSI indicators and combines closing prices to filter long and short positions. The profit-taking and stop-loss mechanisms effectively control risks and lock in profits.

## Strategy Principle

The strategy first uses SMA smoothing technology to calculate the 26-week moving average as a benchmark for judging the bull market. Then, it calculates the 4-week RSI indicator value; when it crosses below 30 in the oversold area, it is considered that the market may rebound. At this time, it judges whether the new high of the shortdays parameter can break through the recent new high of the longdays parameter, indicating a strengthening short-term trend. If all these conditions are met simultaneously, a long signal is issued.

After entering the market, use ATR indicator multiples as profit range and stop loss at a certain percentage of the closing price high point.

## Advantages of the Strategy

The strategy has the following advantages:

1. Use the RSI indicator to determine reversal points with good timing ability.
2. Apply the new highs and lows mechanism to avoid false signals.
3. Utilize ATR for profit-taking and stop-loss, automatically tracking optimal exit points.
4. Flexible parameter settings can be adjusted to optimal levels.
5. The strategy idea is clear and easy to understand, with strong stability.

## Risks of the Strategy

The strategy also has the following risks:

1. The RSI indicator may issue a wrong signal, leading to improper entry timing. Adjusting RSI parameters or adding other indicators for filtering can help.
2. The ATR profit range may be set too large or too small, failing to lock in maximum profits. Testing better parameter combinations can improve this.
3. Stop loss points are too close and may be broken by market movements. Appropriately relaxing the stop loss distance is recommended.
4. Insufficient backtest data may overestimate the strategy’s returns. Increasing the backtest period and testing different market environments are necessary.

## Strategy Optimization

The strategy can be optimized in the following aspects:

1. Test and optimize RSI parameters and profit/loss multiples to find the best parameter combination.
2. Increase other indicators to improve accuracy, such as MACD, KD, etc.
3. Optimize stop loss mechanisms by dynamically adjusting based on ATR fluctuation ranges.
4. Test performance across different trading instruments. Choose liquid and highly volatile varieties.
5. Compare the performance of different types of stop losses, including proportional stops and moving stops.

## Summary

Overall, this strategy operates clearly and smoothly with reasonable indicator selection and parameter settings, making it highly practical. Further improvements through parameter optimization and mechanism refinement are still possible. In summary, the strategy has a relatively high ability to generate stable profits. It is worth debugging in real trading environments and implementing for use.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|26|long week|
|v_input_2|21|short days high period|
|v_input_3|50|long days high period|
|v_input_4|4|rsi period|
|v_input_5|30|rsi thresh|
|v_input_6|3|profit target|
|v_input_7|2|stop target|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-02-05 00:00:00
end: 2024-01-18 05:20:00
period: 2d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
//A translation from info found at http://backtestwizard.com/swing-trading-system-for-stocks/
strategy("Swing Trading System RSI", overlay=true)
source = close[1]

longperiod = input(26,"long week",minval=2,maxval=500,step=1)
s = request.security(syminfo.tickerid, "W", sma(close[1], longperiod)) // 1 Day
plot(s)

shortdays = input(21,"short days high period",minval=2,maxval=500,step=1)
longdays = input(50,"long days high period",minval=2,maxval=500,step=1)
rsiperiod = input(4,"rsi period",minval=2,maxval=500,step=1)
rsithresh = input(30,"rsi thresh",minval=2,maxval=500,step=1)

highcheck = highest(source,shortdays) == highest(source,longdays)
rsicheck = crossunder(rsi(source,rsiperiod),rsithresh)

longCondition = (highcheck) and (rsicheck) and source > s
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long)

profittarget = input(3,"profit target",minval=2,maxval=500,step=1)
stoploss = input(2,"stop target",minval=2,maxval=500,step=1)

exitCondition1 =