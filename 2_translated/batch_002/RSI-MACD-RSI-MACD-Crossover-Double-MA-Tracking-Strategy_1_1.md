> Name

RSI-MACD交叉双均线跟踪策略RSI-MACD-Crossover-Double-MA-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/db2e387bf1c19ccd85.png)

[trans]

## Overview

This strategy combines the use of RSI, MACD indicators, and double moving averages to achieve trend tracking and volatility positioning. It uses the RSI indicator to identify overbought or oversold conditions, the MACD for fast and slow MA crossovers to determine entry and exit points, and the double MAs to filter out some noisy trading opportunities during trends.

## Strategy Logic

1. Calculate RSI to Identify Overbought/Oversold Conditions:

  - Calculate price changes over a certain period
  - Compute RSI based on these price changes
  - Determine overbought or oversold levels

2. Calculate MACD for Crossover:

  - Calculate the fast MA, slow MA, and signal line
  - Enter long positions on golden cross (when the fast MA crosses above the slow MA) and exit short positions on death cross (when the fast MA crosses below the slow MA)
  - Plot crossover situations

3. Implement Double Moving Average Filter:

  - Calculate both fast and slow moving averages
  - Only consider trading when the fast MA crosses above the slow MA
  - Filter out noise and follow trends

4. Combine Multiple Indicators for Entry:

  - Use a combination of RSI, MACD, and double MAs to filter entry signals
  - Enhance accuracy and stability of the strategy

## Advantage Analysis

- Combination of multiple indicators improves accuracy 
- Trend following helps filter out noise and enhances overall stability
- RSI helps identify potential reversal points  
- MACD crossovers provide simple and effective buy/sell signals
- Double MAs remove most countertrend trades
- Easy to understand with few parameters, suitable for beginners

## Risk Analysis

- Multiple indicators can lead to overfitting of the strategy
- Double MA sacrifice some flexibility and may miss opportunities
- Careful selection of RSI and MACD parameters is required
- Pay attention to stop loss levels based on symbol
- Periodic re-tuning of parameters is necessary for long-term use

## Optimization Directions

- Adjust RSI parameters for different symbols
- Optimize double MA periods for better trend tracking 
- Add stop loss rules to control single trade losses
- Incorporate more indicators to enrich the combination
- Develop adaptive parameter models for automatic tuning

## Summary

This strategy combines RSI, MACD, and double MAs to identify and track trends while filtering out signals through multiple layers. It is very suitable for beginners to learn and improve upon. The advantage lies in its simplicity and adaptability. Fine-tuning of parameters can generate decent stable returns. Further improvements could include adding more indicators, developing adaptive parameter models, etc., to better suit various market environments.

||

## Overview

This strategy combines the RSI indicator, MACD indicator, and double moving averages to achieve trend tracking and volatility positioning in the market. It uses the RSI indicator to determine overbought or oversold conditions, the MACD for fast and slow MA crossovers to decide on entry and exit points, and the double MAs to filter out some noisy trading opportunities during trends.

## Strategy Logic

1. Calculate RSI to Identify Overbought/Oversold Conditions:

  - Calculate price changes over a certain period
  - Compute RSI based on these price changes
  - Determine overbought or oversold levels

2. Calculate MACD for Crossover:

  - Calculate the fast MA, slow MA, and signal line
  - Enter long positions on golden cross (when the fast MA crosses above the slow MA) and exit short positions on death cross (when the fast MA crosses below the slow MA)
  - Plot crossover situations

3. Implement Double Moving Average Filter:

  - Calculate both fast and slow moving averages
  - Only consider trading when the fast MA crosses above the slow MA
  - Filter out noise and follow trends

4. Combine Multiple Indicators for Entry:

  - Use a combination of RSI, MACD, and double MAs to filter entry signals
  - Enhance accuracy and stability of the strategy

## Advantage Analysis

- Combination of multiple indicators improves accuracy 
- Trend following helps filter out noise and enhances overall stability
- RSI helps identify potential reversal points  
- MACD crossovers provide simple and effective buy/sell signals
- Double MAs remove most countertrend trades
- Easy to understand with few parameters, suitable for beginners

## Risk Analysis

- Multiple indicators can lead to overfitting of the strategy
- Double MA sacrifice some flexibility and may miss opportunities
- Careful selection of RSI and MACD parameters is required
- Pay attention to stop loss levels based on symbol
- Periodic re-tuning of parameters is necessary for long-term use

## Optimization Directions

- Adjust RSI parameters for different symbols
- Optimize double MA periods for better trend tracking 
- Add stop loss rules to control single trade losses
- Incorporate more indicators to enrich the combination
- Develop adaptive parameter models for automatic tuning

## Summary

This strategy combines RSI, MACD, and double MAs to identify and track trends while filtering out signals through multiple layers. It is very suitable for beginners to learn and improve upon. The advantage lies in its simplicity and adaptability. Fine-tuning of parameters can generate decent stable returns. Further improvements could include adding more indicators, developing adaptive parameter models, etc., to better suit various market environments.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2017|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|2|Backtest Start Day|
|v_input_4|2019|Backtest Stop Year|
|v_input_5|7|Backtest Stop Month|
|v_input_6|30|Backtest Stop Day|
|v_input_7|true|Color Background?|
|v_input_8|14|Length|
|v_input_9|9|Fast Length|
|v_input_10|72|Slow Length|
|v_input_11|9|Signal Length|
|v_input_12|234|Control MA|
|v_input_13|true|Buy on crossover control MA?|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-22 00:00:00
end: 2023-10-22 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

// Component Code Start
testStartYear = input(2017, "Backtest Start Year")
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(2, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0)

testStopYear = input(2019, "Backtest Stop Year")
testStopMonth = input(7, "Backtest Stop Month")
testStopDay = input(30, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay,0,0)

// A switch to control background coloring of the test period
testPeriodBackground = input(title="Color Background?", type=bool, defval=true)
testPeriodBackgroundColor = testPeriodBackground and (time >= testPeriodStart) and (time <= testPeriodStop) ? #00FF00 : na
bgcolor(testPeriodBackgroundColor, transp=97)

testPeriod() => true
// Component Code Stop

//standard rsi template
src = ohlc4, len = input(14, minval=1, title="Length")
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
plot(rsi, color=#87ff1a)
band1 = hline(80)
band = hline(50)
band0 = hline(20)
fill(band1, band0, color=purple, transp=90)

//macd

fast_length = input(title="Fast Length",  defval=9)
slow_length = input(title="Slow Length",  defval=72)
signal_length = input(title="Signal Length",  defval=9)

fast_ma = sma(rsi, fast_length) 
slow_ma = sma(rsi, slow_length) 
```