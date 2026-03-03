> Name

Momentum-Breakthrough-Golden-Cross-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/8a0cbeb83994166356.png)
[trans]
## Overview

This is a quantitative trading strategy that combines MACD, RSI, and EMA moving averages. It uses the MACD golden cross for long entry, RSI overbought reversal, and price breakout below EMA as stop loss exit to track the market's middle-to-long term trends.

## Principles

The strategy mainly uses the following three indicators for trading signal judgment and strategy implementation:

1. **MACD**: Calculate the fast line, slow line, and MACD histogram. The strategy judges the timing of entry by the golden cross of the fast and slow lines.
2. **RSI**: Calculate the 14-period RSI and set the overbought/oversold level. The strategy utilizes the RSI overbought reversal on a weekly timeframe to avoid the risk of being overbought.
3. **EMA**: Calculate the 50-day EMA line. The strategy sets the stop loss point by the price breaking below this line to control the risk of loss.

A buy signal is generated when the MACD fast line crosses above the slow line from below forming a golden cross. At the same time, require the weekly RSI indicator to be above 50, indicating an overbought state, which helps to grasp the upward trend of this round of market. Finally, a long entry will only be executed when the price is above the 50-day EMA line.

If the price breaks below the 50-day EMA or a MACD dead cross occurs, a stop loss exit will be executed.

## Advantage Analysis

The advantage of this strategy combines MACD, RSI, and EMA indicators to achieve good breakthrough tracking capability:

1. **MACD Golden Cross** has some lead characteristic that can capture the buy timing of the market earlier.
2. **Based on Weekly RSI**, it can effectively filter out short-term overbought scenarios and grasp the middle-to-long term uptrend.
3. The EMA stop loss can make timely stop losses on sudden down trends, effectively controlling DD (Drawdown).
4. Overall, this strategy can smoothly capture middle-to-long term breakthrough opportunities and gain decent returns after the market breaks out upwards.

## Risk Analysis

Pay attention to the following risks:

1. **MACD Golden Cross** has some lagging properties that may miss the optimal entry point of the market.
2. The parameter settings of RSI and EMA need repeated testing and optimization, otherwise they may become invalid.
3. The best buying point of a breakthrough market does not necessarily appear at the moment of golden cross; there is some timing risk.
4. A stop loss set too loose may lead to larger DD, while a stop loss set too tight may easily be broken by a breakthrough yang line.

## Optimization Directions

There are still several optimization directions for this strategy:

1. Test and optimize the MACD parameter combination to find a better balance point.
2. The RSI cycle and overbought/oversold level can also be optimized.
3. The moving cycle of EMA can also be adjusted appropriately to find better parameters.
4. Secondary confirmation of the entry timing can be made based on advanced technical indicators, such as the KDJ indicator.
5. Test stop loss exit strategies by adopting percentage-based moving stop loss or quantitative stop loss to make the stop loss smarter.

## Conclusion

In general, this strategy is a typical mid-to-long term tracking strategy. It combines multiple indicators such as MACD, RSI, and EMA to judge the timing of entry in order to obtain a better entry point. It also adopts stop loss measures to control trading risks. The strategy suits middle-to-long term tracking investors, and there is still room for further optimization. With proper parameter tuning, decent returns can be obtained.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|5|Fast Length|
|v_input_2|13|Slow Length|
|v_input_3|9|Signal Length|
|v_input_4|21|EMA Length|
|v_input_5|14|RSI Length|
|v_input_6|50|RSI Overbought Level|

> Source (PineScript)

```pinescript
//@version=5
strategy("MACD, EMA, and RSI Strategy", overlay=true)

// Input for MACD
fastLength = input(5, title="Fast Length")
slowLength = input(13, title="Slow Length")
signalLength = input(9, title="Signal Length")

// Input for EMA
emaLength = input(21, title="EMA Length")

// Input for RSI
rsiLength = input(14, title="RSI Length")
rsiOverbought = input(50, title="RSI Overbought Level")

// Calculate MACD on the weekly timeframe
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalLength)

// Calculate EMA
ema = ta.ema(close, emaLength)

// Calculate RSI
rsi = ta.rsi(close, rsiLength)

// Generate buy signals based on MACD golden cross and RSI overbought reversal conditions
if (ta.crossover(macdLine, signalLine) and rsi > rsiOverbought)
    strategy.entry("Buy", strategy.long)

// Set stop loss below 50-day EMA
stopLoss = ema < close ? true : false
if (stopLoss)
    strategy.exit("Stop Loss Exit", "Buy")

```

Note: The Pine Script provided is a simplified version to illustrate the concept. Further testing and optimization might be necessary for practical use.