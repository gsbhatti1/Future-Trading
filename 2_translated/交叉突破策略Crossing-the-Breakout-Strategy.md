> Name

Crossing-the-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

The moving average crossover strategy is a very common quantitative trading strategy. It uses the golden cross and death cross of moving averages to determine trends, enabling profits. When the short-term moving average crosses above the long-term moving average, it indicates an uptrend, suggesting a long position can be taken; when the short-term moving average crosses below the long-term moving average, it indicates a downtrend, indicating a short position should be initiated.

## Strategy Logic

This strategy relies on the golden cross and death cross of moving averages to determine entry and exit points. The code uses two boolean input parameters `upOrDown` and `longOrShort` to decide whether to go long or short; `percentInput` to set the threshold percentage for price change; `closePositionDays` to define how many days to hold the position.

The core logic involves calculating the increase/decrease of today's closing price relative to yesterday's. If this change reaches the input threshold percentage, a trading signal is triggered. For long signals, going long occurs when today’s price increases more than the threshold from yesterday; for short signals, selling happens when today’s price decreases more than the threshold from yesterday.

After initiating a long or short position, the entry day and the next four days will be marked with different colors on the chart. Positions are automatically closed after four days.

## Advantages

- Using moving average crossovers to determine market trends is a mature and reliable method.
- The strategy logic is simple and clear, making it easy to understand and implement.
- The frequency of trades can be controlled by adjusting parameters.
- An automatic stop loss mechanism effectively manages risks.

## Risks

- Moving averages have lagging effects and may miss the best timing for rapid price changes.
- Significant short-term price fluctuations might generate unnecessary signals.
- Improper parameter settings could affect strategy performance.
- The strategy is not effective in responding to unexpected events.

Risk Management:

1. Optimize moving average parameters, using longer periods to filter out noise.
2. Increase the threshold percentage to reduce unnecessary trades.
3. Test different holding periods to control single-loss amounts.
4. Combine with other indicators to further confirm signals.

## Optimization Directions

- Consider switching from simple moving averages (SMA) to exponential moving averages (EMA), double-moving averages (DMA), or other types of moving averages for increased sensitivity.
- Add stop loss mechanisms, such as setting a stop loss when the price breaks through the average.
- Integrate additional technical indicators like MACD and KDJ for combination, potentially increasing the strategy's win rate.
- Explore machine learning methods to automatically optimize parameters.
- Optimize entry and exit timing, including breakout strategies.

## Summary

The moving average crossover strategy is a very simple yet practical quantitative trading strategy. By assessing the relationship between short-term and long-term trends, it exploits trending price movements for profit. This strategy is easy to implement with clear logic and forms the basis of many other quantitative trading strategies. Through parameter tuning and optimizations, better performance can be achieved. However, risk management should also be considered to avoid misinterpretation or misuse.

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long=Checked Short=Unchecked|
|v_input_2|true|Direction of Today vs. Previous day: Up=Checked Down=Unchecked|
|v_input_3|4.5|Percent|
|v_input_4|4|How Many Days to Close Position|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-10-11 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

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