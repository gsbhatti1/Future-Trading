> Name

Triple-Moving-Average-Crossover-System

> Author

ChaoZhang

> Strategy Description

## Overview

The Triple Moving Average Crossover System is a typical trend-following stock trading strategy. It uses the crossover of three moving averages with different time lengths as buy and sell signals. When the short-term moving average crosses above the medium-term moving average, and the medium-term moving average crosses above the long-term moving average, it generates a buy signal. Conversely, when the short-term moving average crosses below the medium-term moving average, and the medium-term moving average crosses below the long-term moving average, it generates a sell signal.

## Strategy Logic

The strategy is based on three moving averages: the long-term moving average (ma1), the medium-term moving average (ma2), and the short-term moving average (ma3). First, it calculates these lines:

```pine
length1 = input(18, 'Long')
length2 = input(9, 'Medium')
length3 = input(4, 'Short')

ma1 := sma(close, length1)
ma2 := sma(close, length2) 
ma3 := sma(close, length3)
```

Where `length1`, `length2`, and `length3` define the time lengths of the three moving averages. The `sma` function calculates the simple moving average of the close price over the corresponding length.

It then uses the crossover of these moving averages to determine entry and exit points:

```pine
if ma2 > ma1 and ma3 > ma3[1]
    strategy.entry("Long", strategy.long)

if ma2 < ma1 and ma3 < ma3[1] 
    strategy.entry("Short", strategy.short)
```

When the medium-term `ma2` crosses above the long-term `ma1`, and the short-term `ma3` crosses above the previous period's `ma3`, a long signal is triggered. Conversely, when the medium-term `ma2` crosses below the long-term `ma1`, and the short-term `ma3` crosses below the previous period's `ma3`, a short signal is triggered.

## Advantages of the Strategy

- Using three moving averages can clearly identify trend changes.
- The combination of long and short periods filters out some short-term market noise, locking in longer-term trends.
- Simple rules make it easy to implement.
- Parameters can be adjusted to adapt to different market environments.

## Risks of the Strategy

- Entries and exits are identified with hindsight and cannot completely avoid losses.
- Whipsaws occur when the price oscillates around moving averages.
- A long-term line that is too long may miss trend turning points. A short-term line that is too short may trigger frequent trades due to noise.
- It does not handle ranging markets very well.

These risks can be reduced through appropriate parameter optimization, adding filters with other indicators, etc.

## Improvement Directions

- Backtest different parameter combinations to find optimal values.
- Add stop loss to control losses.
- Add other indicators to judge momentum and divergence to avoid false signals. For example, MACD, KD, etc.
- Choose suitable profit-taking strategy according to actual situation.

## Summary 

The Triple Moving Average Crossover strategy is a simple and practical trend-following strategy. It identifies changes in trend direction based on the crossover of three moving averages to generate trading signals. The advantages of this strategy are its simple rules and effective tracking of trends, making it suitable for medium to long-term trading. However, there are also risks of false signals and drawdowns. The strategy can be improved by optimizing parameters, adding supporting indicators, etc., to adapt to different market environments. Overall, the Triple Moving Average Crossover is a foundational algorithmic trading strategy that provides a good starting point for learning quantitative trading.

> Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|v_input_1|18|Long|
|v_input_2|9|Medium|
|v_input_3|4|Short|

> Source (PineScript)

```pinescript
//@version=4
strategy("Triple Moving Average Crossover System", overlay=true)
// strategy.risk.allow_entry_in(strategy.direction.long)
length1 = input(18, 'Long')
length2 = input(9, 'Medium')
length3 = input(4, 'Short')

ma1 = 0.0
ma2 = 0.0
ma3 = 0.0

ma1 := sma(close, length1)
ma2 := sma(close, length2) 
ma3 := sma(close, length3)

plot(ma1)
plot(ma2)
plot(ma3)

if ma2 > ma1 and ma3 > ma3[1]
    strategy.entry("Long", strategy.long, when=strategy.position_size <= 0)

if ma2 < ma1 and ma3 < ma3[1] 
    strategy.entry("Short", strategy.short)  
```