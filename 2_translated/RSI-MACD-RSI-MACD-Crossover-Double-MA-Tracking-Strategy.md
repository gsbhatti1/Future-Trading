> Name

RSI-MACD交叉双均线跟踪策略 RSI-MACD-Crossover-Double-MA-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/db2e387bf1c19ccd85.png)

## Overview

This strategy integrates the use of RSI, MACD indicators, and double moving averages to achieve trend tracking and volatility market positioning. It uses the RSI indicator to judge overbought and oversold conditions, MACD to determine entry and exit points through fast and slow moving average crossovers, and double moving averages to filter out some noisy trading opportunities during the trend.

## Strategy Logic

1. Calculate RSI for overbought and oversold levels

  - Calculate price changes in up and down trends

  - Compute RSI based on these price changes

  - Determine overbought and oversold levels

2. Calculate MACD for crossovers

  - Compute fast MA, slow MA, and signal line

  - Enter long position on golden cross and exit on death cross

  - Plot crossover situations

3. Implement double MA filter

  - Compute fast and slow moving averages

  - Only consider trading when the fast MA crosses above the slow MA

  - Filter out noise and track the trend

4. Combine indicators for entry

  - Filter entry signals with RSI, MACD, and double MAs

  - Improve strategy accuracy and stability

## Advantage Analysis

- Combination of multiple indicators enhances accuracy

- Trend following filters noise and improves stability

- RSI helps identify potential turning points

- MACD crossovers provide simple and effective buy/sell signals

- Double MA filtering removes most countertrend trades

- Easy to understand with few parameters, suitable for beginners

## Risk Analysis

- Overfitting risk from multiple indicators

- Double MA may sacrifice flexibility and miss opportunities

- Careful selection of RSI and MACD parameters needed

- Attention required on stop loss points based on the trading symbol

- Periodic parameter tuning is necessary to adapt to market conditions over time

## Optimization Directions

- Adjust RSI parameters for different symbols

- Optimize double MA periods for better trend tracking 

- Add stop loss mechanisms to control single trade losses

- Incorporate more indicators to enrich criteria combinations

- Develop adaptive parameter models for automatic adjustment

## Summary

This strategy combines the use of RSI, MACD, and double moving averages to identify and track trends, filtering signals through multiple layers. It is very suitable for beginners to learn and improve upon. The key advantage lies in its simplicity and adaptability. Fine-tuning parameters can generate decent stable returns. Future improvements may include adding more indicators, developing adaptive parameter models to automatically optimize for different market environments.

---

## Overview

This strategy combines the RSI indicator, MACD indicator, and double moving averages to achieve trend tracking and volatility positioning effects in the market. Using the RSI indicator to judge overbought and oversold conditions, MACD to determine entry and exit points via fast and slow MA crossovers, and double MAs to filter out some noisy trading opportunities during trends.

## Strategy Logic

1. Calculate RSI for overbought/oversold levels

  - Compute price changes in up/down trends
  
  - Compute RSI based on the above calculations

  - Determine overbought/oversold levels
  
2. Calculate MACD for crossovers

  - Compute fast MA, slow MA, and signal line

  - Enter long position on golden cross, exit on death cross

  - Plot crossover situations

3. Implement double MA filter

  - Compute fast and slow moving averages

  - Consider trading only when the fast MA crosses above the slow MA

  - Filter out noise and track trends

4. Combine indicators for entry

  - Use RSI, MACD, and double MAs to determine combined signals

  - Improve strategy accuracy and stability

## Advantage Analysis

- Combination of multiple indicators enhances precision

- Trend following filters noise and increases stability

- RSI helps identify potential turning points

- MACD crossovers provide simple effective buy/sell signals

- Double MA filtering removes most countertrend trades

- Easy to understand with few parameters, good for learning

## Risk Analysis

- Overfitting risk from multiple indicators

- Double MA may sacrifice flexibility and miss opportunities

- Careful selection of RSI and MACD parameters needed

- Attention required on stop loss points based on the trading symbol

- Requires periodic parameter tuning 

## Optimization Directions

- Adjust RSI parameters for different symbols

- Optimize double MA periods to improve trend tracking

- Add stop loss mechanisms to control single trade losses

- Incorporate more indicators to enrich criteria combinations

- Develop adaptive parameter models for automatic adjustment

## Summary

This strategy combines the use of RSI, MACD, and double moving averages to identify and track trends, filtering signals through multiple layers. It is very suitable for beginners to learn and improve upon. The key advantage lies in its simplicity and adaptability. Fine-tuning parameters can generate decent stable returns. Future improvements may include adding more indicators, developing adaptive parameter models to automatically optimize for different market environments.

||

## Source (PineScript)

```pinescript
/*backtest
start: 2023-09-22 00:00:00
end: 2023-10-22 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

// Component Code Start
// Example usage:
// if testPeriod()
//   strategy.entry("LE", strategy.long)
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

// Standard RSI template
src = ohlc4, len = input(14, minval=1, title="Length")
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
plot(rsi, color=#87ff1a)
band1 = hline(80)
band = hline(50)
band0 = hline(20)
fill(band1, band0, color=purple, transp=90)

// MACD
fast_length = input(title="Fast Length", defval=9)
slow_length = input(title="Slow Length", defval=72)
signal_length = input(title="Signal Length", defval=9)

fast_ma = sma(rsi, fast_length) 
slow_ma = sma(rsi, slow_length) 
```