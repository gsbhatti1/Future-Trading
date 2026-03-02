> Name

RSI-MACD交叉双均线跟踪策略 RSI-MACD-Crossover-Double-MA-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/db2e387bf1c19ccd85.png)

## Overview

This strategy integrates the RSI indicator, MACD indicator, and double moving averages to achieve trend tracking and position standard deviation trends. The strategy uses the RSI indicator to determine overbought and oversold conditions, the MACD for crossover to decide entry and exit points, and double MAs to filter out some noisy trading opportunities during a trend.

## Strategy Logic

1. Calculate RSI for determining overbought/oversold levels

  - Calculate price changes in an uptrend and downtrend
  - Compute RSI based on the calculated price changes
  - Provide overbought/oversold judgments

2. Calculate MACD for crossovers

  - Compute fast MA, slow MA, and signal line
  - Enter long positions on golden cross and exit on death cross
  - Plot crossover situations

3. Implement double MA filter

  - Compute fast and slow moving averages
  - Only consider trading when the fast MA crosses above the slow MA
  - Filter noise to follow the trend

4. Combine indicators for entry signals

  - Use RSI, MACD, and double MAs as multiple conditions for filtering entries
  - Improve the accuracy and stability of the strategy

## Advantage Analysis

- Combination of multiple indicators enhances accuracy

- Trend following filters out noise and improves stability

- RSI helps identify potential reversal points

- MACD crossovers provide simple and effective buy/sell signals

- Double MAs remove most countertrend trades

- Easy to understand with few parameters, suitable for beginners

## Risk Analysis

- Overfitting risk from multiple indicators combination

- Double MAs sacrifice flexibility and may miss some opportunities

- Careful selection of RSI and MACD parameters is needed

- Pay attention to stop loss levels based on the trading symbol

- Periodic retuning of parameters required for adapting to market changes

## Optimization Directions

- Adjust RSI parameters for different symbols

- Optimize double MA periods for better trend tracking

- Add stop losses to control single trade losses

- Incorporate more indicators to enrich entry conditions

- Develop an adaptive parameter model for automatic tuning

## Summary

This strategy combines the use of RSI, MACD, and double MAs to identify and track trends, filtering through multiple layers. It is very suitable for beginners to learn and improve upon. The main advantage lies in its simplicity and adaptability. Fine-tuning parameters can generate decent and stable returns. Future improvements could include adding more indicators, developing an adaptive parameter model to automatically adjust to different market environments.

---

## Overview

This strategy combines the RSI indicator, MACD indicator, and double moving averages to achieve trend tracking and volatility positioning effects. It uses the RSI indicator to determine overbought/oversold conditions, the MACD for crossover signals to decide entry and exit points, and the double MAs to filter out some noisy trading opportunities during a trend.

## Strategy Logic

1. Calculate RSI for overbought/oversold levels

  - Calculate price changes in uptrend and downtrend
  - Compute RSI based on the calculated price changes
  - Determine overbought/oversold levels
  
2. Calculate MACD for crossovers

  - Compute fast MA, slow MA, and signal line
  - Enter long positions on golden cross and exit on death cross
  - Plot crossover situations

3. Implement double MA filter

  - Compute fast and slow moving averages
  - Only consider trading when the fast MA crosses above the slow MA
  - Filter noise to follow the trend

4. Combine indicators for entry signals

  - Use RSI, MACD, and double MAs as multiple conditions for filtering entries
  - Improve accuracy and stability of the strategy

## Advantage Analysis

- Combination of multiple indicators enhances accuracy

- Trend following filters out noise and improves stability

- RSI helps identify potential reversal points

- MACD crossovers provide simple and effective buy/sell signals

- Double MAs remove most countertrend trades

- Easy to understand with few parameters, suitable for beginners

## Risk Analysis

- Overfitting risk from multiple indicators combination

- Double MAs sacrifice flexibility and may miss some opportunities

- Careful selection of RSI and MACD parameters is needed

- Pay attention to stop loss levels based on the trading symbol

- Periodic retuning of parameters required for adapting to market changes

## Optimization Directions

- Adjust RSI parameters for different symbols

- Optimize double MA periods for better trend tracking

- Add stop losses to control single trade losses

- Incorporate more indicators to enrich entry conditions

- Develop an adaptive parameter model for automatic tuning

## Summary

This strategy combines the use of RSI, MACD, and double MAs to identify and track trends, filtering through multiple layers. It is very suitable for beginners to learn and improve upon. The main advantage lies in its simplicity and adaptability. Fine-tuning parameters can generate decent and stable returns. Future improvements could include adding more indicators, developing an adaptive parameter model to automatically adjust to different market environments.

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 2017 | Backtest Start Year |
| v_input_2 | true | Backtest Start Month |
| v_input_3 | 2 | Backtest Start Day |
| v_input_4 | 2019 | Backtest Stop Year |
| v_input_5 | 7 | Backtest Stop Month |
| v_input_6 | 30 | Backtest Stop Day |
| v_input_7 | true | Color Background? |
| v_input_8 | 14 | Length |
| v_input_9 | 9 | Fast Length |
| v_input_10 | 72 | Slow Length |
| v_input_11 | 9 | Signal Length |
| v_input_12 | 234 | Control MA |
| v_input_13 | true | Buy on crossover control MA? |

```pinescript
/*backtest
start: 2023-09-22 00:00:00
end: 2023-10-22 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3

// strategy(title="RSI MACD", precision = 6, pyramiding = 1, default_qty_type = strategy.percent_of_equity, default_qty_value = 99, commission_type = strategy.commission.percent, commission_value = 0.25, initial_capital = 1000)

// Component Code Start
// Example usage:
// if testPeriod()
//   strategy.entry("LE", strategy.long)
testStartYear = input(2017, "Backtest Start Year")
testStartMonth = input(01, "Backtest Start Month")
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