> Name

Crossing-the-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

The moving average crossover strategy is a very common quantitative trading strategy. It uses the golden cross and death cross of moving averages to determine trends, allowing profits to be made. When the short-term moving average crosses above the long-term moving average, it signals an uptrend, indicating that prices are starting to rise, and a long position can be taken; when the short-term moving average crosses below the long-term moving average, it signals a downtrend, indicating that prices are starting to fall, allowing for a short position.

## Strategy Logic

This strategy is based on the golden cross and death cross of moving averages to determine entry and exit points. The code uses two boolean input parameters `upOrDown` and `longOrShort` to determine long or short positions; `percentInput` to set the threshold percentage of price change; `closePositionDays` to set the number of days to hold the position.

The core logic is: calculate today's increase/decrease relative to yesterday. If it reaches the input threshold percentage, a trading signal is triggered. For a long signal, if today's price increases more than the threshold compared to yesterday, go long; for a short signal, if today's price decreases more than the threshold compared to yesterday, go short.

After going long/short, the entry day and next 4 days will be marked with colors on the chart. The position is automatically closed after 4 days.

## Advantages

- Using moving average crossovers to determine trends is a mature and reliable method.
- Simple and clear strategy logic, easy to understand and implement.
- The frequency can be controlled by adjusting parameters.
- An automatic stop loss mechanism effectively controls risks.

## Risks

- Moving averages have lagging effects, which may miss the best timing of rapid price changes.
- Significant price swings in the short term may generate unnecessary crossover signals.
- Inappropriate parameter settings may affect strategy performance.
- The strategy is unable to respond effectively to unexpected events.

Risk management measures:

1. Optimize moving average parameters by using longer periods to filter out noise.
2. Increase the threshold percentage for price changes to reduce unnecessary trades.
3. Test different holding periods to control single losses.
4. Combine with other indicators to further confirm signals.

## Optimization Directions

- Consider replacing simple moving averages (SMA) with exponential moving averages (EMA), double-moving averages (DMA), etc., to make them more sensitive to price changes.
- Add stop loss mechanisms, such as immediately stopping when breaking the average.
- Integrate other technical indicators like MACD and KDJ for combination, which can improve the win rate of the strategy.
- Try machine learning methods to automatically optimize parameters.
- Optimize entry and exit timing, such as breakout strategies.

## Summary

The moving average crossover strategy is a very simple and practical quantitative trading strategy. By judging the relationship between short-term and long-term trends, it profits from the trending nature of asset prices. This strategy is easy to implement with clear logic and forms the foundation of many quantitative trading strategies. We can obtain better performance through parameter tuning and optimizations. However, we also need to manage risks and avoid misusing the strategy.

||

## Overview

The moving average crossover strategy is a very common quantitative trading strategy. It uses the golden cross and death cross of moving averages to determine trends and profit. When the short-term moving average crosses above the long-term moving average, it signals an uptrend, indicating that prices are starting to rise, and a long position can be taken; when the short-term moving average crosses below the long-term moving average, it signals a downtrend, indicating that prices are starting to fall, allowing for a short position.

## Strategy Logic

This strategy is based on the golden cross and death cross of moving averages to determine entry and exit points. The code uses two boolean input parameters `upOrDown` and `longOrShort` to determine long or short positions; `percentInput` to set the threshold percentage of price change; `closePositionDays` to set the number of days to hold the position.

The core logic is: calculate today's increase/decrease relative to yesterday. If it reaches the input threshold percentage, a trading signal is triggered. For a long signal, if today's price increases more than the threshold compared to yesterday, go long; for a short signal, if today's price decreases more than the threshold compared to yesterday, go short.

After going long/short, the entry day and next 4 days will be marked with colors on the chart. The position is automatically closed after 4 days.

## Advantages

- Using moving average crossovers to determine trends is a mature and reliable method.
- Simple and clear strategy logic, easy to understand and implement.
- The frequency can be controlled by adjusting parameters.
- An automatic stop loss mechanism effectively controls risks.

## Risks

- Moving averages have lagging effects, which may miss the best timing of rapid price changes.
- Significant price swings in the short term may generate unnecessary crossover signals.
- Inappropriate parameter settings may affect strategy performance.
- The strategy is unable to respond effectively to unexpected events.

Risk management measures:

1. Optimize moving average parameters by using longer periods to filter out noise.
2. Increase the threshold percentage for price changes to reduce unnecessary trades.
3. Test different holding periods to control single losses.
4. Combine with other indicators to further confirm signals.

## Optimization Directions

- Consider replacing simple moving averages (SMA) with exponential moving averages (EMA), double-moving averages (DMA), etc., to make them more sensitive to price changes.
- Add stop loss mechanisms, such as immediately stopping when breaking the average.
- Integrate other technical indicators like MACD and KDJ for combination, which can improve the win rate of the strategy.
- Try machine learning methods to automatically optimize parameters.
- Optimize entry and exit timing, such as breakout strategies.

## Summary

The moving average crossover strategy is a very simple and practical quantitative trading strategy. By judging the relationship between short-term and long-term trends, it profits from the trending nature of asset prices. This strategy is easy to implement with clear logic, and forms the foundation of many quantitative trading strategies. We can obtain better performance through parameter tuning and optimizations. However, we also need to manage risks and avoid misusing the strategy.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long=Checked Short=Unchecked|
|v_input_2|true|Direction of Today vs. Previous day: Up=Checked Down=Unchecked|
|v_input_3|4.5|Percent|
|v_input_4|4|How Many Days to Close Position|


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

>