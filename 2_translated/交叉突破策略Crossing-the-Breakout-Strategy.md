> Name

Crossing-the-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

The moving average crossover strategy is a very common quantitative trading strategy. It uses the golden cross and death cross of moving averages to determine trends, making profits accordingly. When the short-term moving average crosses above the long-term moving average, it indicates an uptrend, and a long position can be taken; when the short-term moving average crosses below the long-term moving average, it suggests a downtrend, and a short position can be taken.

## Strategy Logic

This strategy is based on the golden cross and death cross of moving averages to determine entry and exit points. The code uses two boolean input parameters `upOrDown` and `longOrShort` to determine whether to go long or short; `percentInput` to set the threshold percentage for price change; and `closePositionDays` to specify the number of days to hold the position.

The core logic is: calculate the increase/decrease of today relative to yesterday. If it reaches the input threshold percentage, a trading signal is triggered. If it's a long signal, when today's price increases more than the threshold relative to yesterday, go long; if it's a short signal, when today's price decreases more than the threshold relative to yesterday, go short.

After going long/short, the entry day and next 4 days will be marked with colors on the chart. The position will be closed automatically after 4 days.

## Advantages

- Using moving average crossovers to determine trends is a mature and reliable method.
- Simple and clear strategy logic, easy to understand and implement.
- The frequency can be controlled by adjusting parameters.
- The automatic stop loss mechanism effectively controls risks.

## Risks

- Moving averages have lagging effects, which may miss the best timing of rapid price changes.
- Significant price swings in the short term may generate unnecessary signals.
- Inappropriate parameter settings may affect strategy performance.
- Unable to respond effectively to unexpected events.

Risk management:

1. Optimize moving average parameters; longer periods help filter noise.
2. Increase threshold percentage to reduce unnecessary trades.
3. Test different holding periods to control single loss.
4. Combine with other indicators to further confirm signals.

## Optimization Directions

- Consider using EMA, DMA instead of SMA to make it more sensitive.
- Add stop loss mechanisms, such as stopping losses when breaking the average.
- Add other technical indicators like MACD, KDJ for combination, improving win rate.
- Try machine learning methods to auto-optimize parameters.
- Optimize entry and exit timing, e.g., breakout, etc.

## Summary

The moving average crossover strategy is a very simple and practical quantitative trading strategy. By judging the relationship between short-term and long-term trends, it profits from the trending nature of asset prices. This strategy is easy to implement with clear logic, forming the foundation of many quantitative trading strategies. We can obtain better performance through parameter tuning and optimizations. But we also need to manage risks and avoid misuse.

||


## Overview

The moving average crossover strategy is a very common quantitative trading strategy. It uses the golden cross and death cross of moving averages to determine trends and profit. When the short-term moving average crosses above the long-term moving average, it signals an uptrend, and a long position can be taken; when the short-term moving average crosses below the long-term moving average, it signals a downtrend, and a short position can be taken.

## Strategy Logic

This strategy is based on the golden cross and death cross of moving averages to determine entry and exit points. The code uses two boolean input parameters `upOrDown` and `longOrShort` to determine whether to go long or short; `percentInput` to set the threshold percentage for price change; `closePositionDays` to specify the number of days to hold the position.

The core logic is: calculate the increase/decrease of today relative to yesterday. If it reaches the input threshold percentage, a trading signal is triggered. If it's a long signal, when today's price increases more than the threshold relative to yesterday, go long; if it's a short signal, when today's price decreases more than the threshold relative to yesterday, go short.

After going long/short, the entry day and next 4 days will be marked with colors on the chart. The position will be closed automatically after 4 days.

## Advantages

- Using moving average crossovers to determine trends is a mature and reliable method.
- Simple and clear strategy logic, easy to understand and implement.
- The frequency can be controlled by adjusting parameters.
- The automatic stop loss mechanism effectively controls risks.

## Risks

- Moving averages have lagging effects, which may miss the best timing of rapid price changes.
- Significant price swings in the short term may generate unnecessary signals.
- Inappropriate parameter settings may affect strategy performance.
- Unable to respond effectively to unexpected events.

Risk management:

1. Optimize moving average parameters; longer periods help filter noise.
2. Increase threshold percentage to reduce unnecessary trades.
3. Test different holding periods to control single loss.
4. Combine with other indicators to further confirm signals.

## Optimization Directions

- Consider using EMA, DMA instead of SMA to make it more sensitive.
- Add stop loss mechanisms, such as stopping losses when breaking the average.
- Add other technical indicators like MACD, KDJ for combination, improving win rate.
- Try machine learning methods to auto-optimize parameters.
- Optimize entry and exit timing, e.g., breakout, etc.

## Summary

The moving average crossover strategy is a very simple and practical quantitative trading strategy. By judging the relationship between short-term and long-term trends, it profits from the trending nature of asset prices. This strategy is easy to implement with clear logic, forming the foundation of many quantitative trading strategies. We can obtain better performance through parameter tuning and optimizations. But we also need to manage risks and avoid misuse.

||


## Strategy Arguments



| Argument | Default | Description |
| -------- | ------- | ----------- |
| v_input_1 | true    | Long=Checked Short=Unchecked |
| v_input_2 | true    | Direction of Today vs. Previous day: Up=Checked Down=Unchecked |
| v_input_3 | 4.5     | Percent |
| v_input_4 | 4       | How Many Days to Close Position |


> Source (PineScript)

```pinescript
//@version=3
// Created by Leon Ross

strategy(title = "DaysAfterCertainPercentChangev1", shorttitle = "DACPCv1", overlay = true, 
  pyramiding = 0, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, 
  calc_on_every_tick=true, initial_capital=100000)
  
// Inputs
longOrShort = input(title="Long=Checked Short=Unchecked", type=bool, defval=true) // long=true, down=false
upOrDown = input(title="Direction of Today vs. Previous day: Up=Checked Down=Unchecked", type=bool, defval=true) // up=true, down=false: this is the direction of days vs previous day
percentInput = input(title="Percent", type=float, defval=4.5)
closePositionDays = input(title="How Many Days to Close Position", defval=4)

// Conditions
upValue = (close / close[1]) - 1
downValue = 1 - (close / close[1])
allConditions = if(upOrDown)
    upValue >= (percentInput/100.0)
else
    downValue >= (percentInput/100.0)

// Plots
bgcolor(allConditions ? (upOrDown ? green : red) : na, transp=70)
```