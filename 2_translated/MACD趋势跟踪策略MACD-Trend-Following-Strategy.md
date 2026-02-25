> Name

MACD Trend Following Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/830b1dca0535cb6a50.png)
[trans]

## Overview

The MACD Trend Following Strategy is a quantitative trading strategy based on the MACD indicator. This strategy identifies MACD golden cross and death cross signals to determine market trends, aiming to track price trends.

## Strategy Logic

The core logic of the MACD Trend Following Strategy is:

1. Calculate the MACD line and signal line.
2. When the MACD line crosses above 0 from bottom up, record the highest point, then wait for a death cross signal.
3. When the MACD line crosses below 0 from top down, record the lowest point, then wait for a golden cross signal.
4. When a golden cross happens, record the current closing price as the long entry point, set stop loss point, and open a long position.
5. When a death cross happens, record the current closing price as the short entry point, set stop loss point, and open a short position.
6. For holding long positions: if profit ratio reaches preset target or drawdown reaches stop loss point, close position to realize profits.
7. For holding short positions: if profit ratio reaches preset target or drawdown reaches stop loss point, close position to realize profits.

Through this trend following mechanism, the strategy can timely capture market trend turns and achieve profitable outcomes.

## Advantage Analysis

The MACD Trend Following Strategy has the following advantages:

1. The source of strategy signals is singular and clear, generated directly by the MACD indicator, avoiding signal interference.
2. Utilizing the golden cross and death cross characteristics of the MACD indicator to determine market trend directions with accurate judgements.
3. Timely tracking turns of trends, with strong profit tracking capability.
4. Proper risk control in place, with a stop loss mechanism.

## Risk Analysis

The MACD Trend Following Strategy also has the following risks:

1. The MACD indicator tends to generate false signals, which may lead to losses in ultra-short-term operations.
2. Improper stop loss point settings can expand single losses.
3. Balancing between profit tracking ratio and stop loss point is difficult, posing a risk of overtracking leading to losses.

To address these risks, the following optimization measures can be adopted:

1. Combining with other indicators to filter out false signals.
2. Dynamically adjusting stop loss points.
3. Optimizing parameters for profit tracking ratio and stop loss points.

## Optimization Directions

The MACD Trend Following Strategy can be optimized in the following aspects:

1. Optimize MACD indicator parameters to reduce false signal rates. Different cycle parameters of MACD can be tested.
2. Adding other indicators like trading volume to filter signals, setting minimum trading volume conditions.
3. Setting up a dynamic trailing stop loss mechanism where stop loss points adjust based on volatility.
4. Optimizing the signal determination logic for opening positions by setting more rigorous trigger conditions.
5. Incorporating machine learning models to filter signals, training models to judge the reliability of signals.

## Conclusion

In general, the MACD Trend Following Strategy is a relatively mature quantitative strategy. It utilizes the MACD indicator to determine market trend directions and controls risks with stop loss mechanisms, effectively tracking price trends. However, the MACD indicator itself has some flaws, easily generating false signals. Thus, there are spaces for further optimization of this strategy, mainly focusing on aspects like indicator parameters, stop loss mechanisms, signal filtering, etc.

[/trans]

## Source (PineScript)

```pinescript
//@version=5
strategy("MACD Cross Strategy", overlay=true)

// Get MACD values
[macdLine, signalLine, _] = ta.macd(close, 12, 26, 9)
var float entryLongPrice = na
var float entryShortPrice = na

var float highestLongProfit = 0
var float highestShortProfit = 0

var float highestMACD = 0
var float lowestMACD = 0
var bool haveOpenedLong = false
var bool haveOpenedShort = false

var float stoploss = 0.04 // To be adjusted for different investments
var float minProfit = 0.05 // To be adjusted for different investments

if macdLine > 0
    lowestMACD := 0
    highestMACD := math.max(highestMACD, macdLine)
    haveOpenedShort := false
else
    highestMACD := 0
    lowestMACD := math.min(lowestMACD, macdLine)
    haveOpenedLong := false

// Enter long position when MACD line crosses above the signal line
if ta.crossover(macdLine, signalLine) and macdLine < highestMACD and macdLine > 0 and haveOpenedLong == false
    strategy.entry("Long", strategy.long)
    
    entryLongPrice := close
    stoploss := entryLongPrice * (1 - stoploss)
    minProfit := entryLongPrice * (1 + minProfit)

// Enter short position when MACD line crosses below the signal line
if ta.crossunder(macdLine, signalLine) and macdLine > lowestMACD and macdLine < 0 and haveOpenedShort == false
    strategy.entry("Short", strategy.short)
    
    entryShortPrice := close
    stoploss := entryShortPrice * (1 + stoploss)
    minProfit := entryShortPrice * (1 - minProfit)

// Close long position when profit target is reached or drawdown reaches stop loss point
if macdLine > 0 and (close / entryLongPrice >= 1 + minProfit or close / entryLongPrice <= 1 - stoploss)
    strategy.close("Long")
    
// Close short position when profit target is reached or drawdown reaches stop loss point
if macdLine < 0 and (entryShortPrice / close >= 1 + minProfit or entryShortPrice / close <= 1 - stoploss)
    strategy.close("Short")
```

Note: The Pine Script has been updated to complete the `strategy.entry` and added conditions for closing long and short positions based on profit targets and stop loss levels.