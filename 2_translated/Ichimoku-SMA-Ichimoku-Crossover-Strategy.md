> Name

SMA Ichimoku Crossover Strategy

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

The SMA Ichimoku crossover strategy is a common trading strategy. This strategy utilizes the golden cross and dead cross principles of moving averages, combined with the Ichimoku cloud and SMA smooth moving average, to form a relatively complete trading system. The strategy can automatically open and close stock positions.

## Strategy Principle

This strategy primarily judges buying and selling stocks by comparing the conversion line and base line in the Ichimoku indicator and the crossovers of short-term and long-term SMA moving averages.

Specifically, the code defines the conversion line, base line, leading line 1, and leading line 2 of the Ichimoku indicator. At the same time, the long-term SMA moving average `ma1` and short-term SMA moving average `ma2` are defined.

When judging for buying, the conversion line needs to be lower than the base line, and the short-term moving average lower than the long-term moving average, that is, a golden cross occurs.

When judging for selling, the conversion line needs to be higher than the base line, and the short-term moving average higher than the long-term moving average, that is, a dead cross occurs.

In addition, the code also defines some auxiliary conditions, such as the closing price being higher than the previous day, and using the difference and division of moving average values to judge the slope. This can determine the momentum and direction of moving average crossovers.

## Advantage Analysis

This strategy combines the advantages of multiple technical indicators and has the following advantages:

1. The Ichimoku cloud itself contains trend judgment, combined with SMA moving averages can form a powerful trend judgment.
2. SMA moving averages themselves can determine price trends and momentum. Fast MA crossing slow MA can determine trading points.
3. Adding closing price judgment can avoid unnecessary opening and closing of positions.
4. The calculation of moving average slope increases judgment on the momentum of moving average crossovers and can filter false crossovers.
5. Overall, this strategy has relatively accurate trend judgment, can reduce unnecessary trading, and has some room for optimization.

## Risk Analysis

This strategy also has some risks:

1. Both Ichimoku and SMA may lag and fail to reflect price changes in time.
2. The combination of multiple conditions increases complexity and probability of errors.
3. The strategy is solely based on technical indicators and cannot judge the impact of major news.
4. The strategy does not set stop loss conditions, with the risk of enlarging losses.
5. The strategy does not consider special market conditions such as consolidation.
6. Improper parameter settings can also affect strategy performance.

## Optimization

This strategy can be optimized in the following aspects:

1. Set stop loss conditions to automatically stop loss when losses enlarge.
2. Increase judgment on major news events to avoid their impact.
3. Increase judgment on special market conditions such as increasing trading range or adjusting parameters.
4. Test and optimize parameter combinations to find optimal parameters.
5. Introduce machine learning algorithms for parameter optimization and market judgment.
6. Add momentum indicators to avoid false breakouts.
7. Combine more fundamentals such as changes in volume.

## Conclusion

In summary, this SMA Ichimoku crossover strategy integrates the advantages of Ichimoku and SMA moving averages to form a relatively complete stock trading strategy. This strategy has strong ability to determine trends and can effectively capture trend opportunities. But there are also problems like lag, high complexity, lack of stop loss. This gives great room for optimizing this strategy. By setting stop loss, judging major news events, optimizing parameters and more, this strategy can be continuously improved to become a stable and reliable quantitative trading strategy.

||


## Overview

The SMA Ichimoku crossover strategy is a common trading strategy. This strategy utilizes the golden cross and dead cross principles of moving averages, combined with the Ichimoku cloud and SMA smooth moving average, to form a relatively complete trading system. The strategy can automatically open and close stock positions.

## Strategy Principle

This strategy primarily judges buying and selling stocks by comparing the conversion line and base line in the Ichimoku indicator and the crossovers of short-term and long-term SMA moving averages.

Specifically, the code defines the conversion line, base line, leading line 1, and leading line 2 of the Ichimoku indicator. At the same time, the long-term SMA moving average `ma1` and short-term SMA moving average `ma2` are defined.

When judging for buying, the conversion line needs to be lower than the base line, and the short-term moving average lower than the long-term moving average, that is, a golden cross occurs.

When judging for selling, the conversion line needs to be higher than the base line, and the short-term moving average higher than the long-term moving average, that is, a dead cross occurs.

In addition, the code also defines some auxiliary conditions, such as the closing price being higher than the previous day, and using the difference and division of moving average values to judge the slope. This can determine the momentum and direction of moving average crossovers.

## Advantage Analysis

This strategy combines the advantages of multiple technical indicators and has the following advantages:

1. The Ichimoku cloud itself contains trend judgment, combined with SMA moving averages can form a powerful trend judgment.
2. SMA moving averages themselves can determine price trends and momentum. Fast MA crossing slow MA can determine trading points.
3. Adding closing price judgment can avoid unnecessary opening and closing of positions.
4. The calculation of moving average slope increases judgment on the momentum of moving average crossovers and can filter false crossovers.
5. Overall, this strategy has relatively accurate trend judgment, can reduce unnecessary trading, and has some room for optimization.

## Risk Analysis

This strategy also has some risks:

1. Both Ichimoku and SMA may lag and fail to reflect price changes in time.
2. The combination of multiple conditions increases complexity and probability of errors.
3. The strategy is solely based on technical indicators and cannot judge the impact of major news.
4. The strategy does not set stop loss conditions, with the risk of enlarging losses.
5. The strategy does not consider special market conditions such as consolidation.
6. Improper parameter settings can also affect strategy performance.

## Optimization

This strategy can be optimized in the following aspects:

1. Set stop loss conditions to automatically stop loss when losses enlarge.
2. Increase judgment on major news events to avoid their impact.
3. Increase judgment on special market conditions such as increasing trading range or adjusting parameters.
4. Test and optimize parameter combinations to find optimal parameters.
5. Introduce machine learning algorithms for parameter optimization and market judgment.
6. Add momentum indicators to avoid false breakouts.
7. Combine more fundamentals such as changes in volume.

## Conclusion

In summary, this SMA Ichimoku crossover strategy integrates the advantages of Ichimoku and SMA moving averages to form a relatively complete stock trading strategy. This strategy has strong ability to determine trends and can effectively capture trend opportunities. But there are also problems like lag, high complexity, lack of stop loss. This gives great room for optimizing this strategy. By setting stop loss, judging major news events, optimizing parameters and more, this strategy can be continuously improved to become a stable and reliable quantitative trading strategy.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|Conversion Line Periods|
|v_input_2|26|Base Line Periods|
|v_input_3|52|Leading Line 2 Periods|
|v_input_4|26|Displacement|
|v_input_5|21|SMA LONG|
|v_input_6|19|SMA SHORT|


> Source (PineScript)

```pinescript
//@version=3
// strategy("Ichimoku+SMAsmoothed", overlay=true, default_qty_type=s
```