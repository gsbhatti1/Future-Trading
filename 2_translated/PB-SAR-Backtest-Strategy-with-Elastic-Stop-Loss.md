> Name

PB-SAR-Backtest-Strategy-with-Elastic-Stop-Loss

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

This strategy is based on the Parabolic SAR indicator to generate buy and sell signals for long and short positions. It also incorporates a trailing stop loss mechanism to effectively control risks.

## Principle

The core of this strategy is to identify trend reversal points using the Parabolic SAR indicator for counter-trend trading. The indicator uses the true range to detect extreme prices. When the price exceeds the extreme, it is considered a breakout and a sign of potential trend reversal. Specifically, the indicator maintains two variables: the Extreme Price (EP) and the Trigger Price (TP). The EP represents the highest/lowest price of the current trend, while the TP is derived from the EP.

In an uptrend, when the price is higher than the EP, it is considered a breakout. The EP is then updated to the highest price and the TP to the lowest price. When the price falls below the TP, a trend reversal is identified and a sell signal is generated. The same principle applies for a downtrend.

The strategy also incorporates a trailing stop loss mechanism. After opening a position, it will track the optimal stop loss price in real-time, locking in profits while controlling risks. Specifically, after long entry, the stop loss tracks the closing low; after short entry, it tracks the closing high.

## Advantages

The main advantages of this strategy are:

1. Identify trend reversal points with the indicator, avoiding being trapped in trends.
2. Trailing stop loss locks in profits and prevents wider losses.
3. Simple indicator parameters, easy to implement.
4. Configurable buy/sell signal alerts for convenience.
5. Flexible backtest period configuration for thorough evaluation.

## Risks

There are also some risks to consider:

1. Indicator lag may miss optimal reversal points.
2. Aggressive stops may be stopped out by short-term fluctuations.
3. Improper backtest period selection cannot fully evaluate the strategy.
4. Transaction costs may impair profits.

Some ways to address the risks are:

1. Optimize parameters to reduce lag.
2. Improve stop loss algorithm to avoid being stopped out unnecessarily.
3. Select appropriate backtest periods for reliability.
4. Optimize position sizing to lower transaction costs.

## Enhancement

Some ways to further optimize the strategy:

1. Incorporate trend indicators like MA to avoid being trapped in countertrends.
2. Optimize position sizing algorithms, e.g. fixed fractional, dynamic.
3. Add volume filter to avoid false signals from gaps.
4. Parameter optimization to find optimal combinations.
5. Implement profit taking strategies to lock in profits in trends.
6. Refine stop loss algorithms for smoother stops. Experiment with Chandelier Exit etc.
7. Optimize across products, time frames etc. to improve adaptability.
8. Incorporate machine learning for greater adaptability.

## Summary

In summary, this is a simple and robust strategy using the Parabolic SAR to identify reversals and trailing stop loss to control risk. It can work as a short-term mean-reversion strategy. But indicator lag and oversensitive stops need to be addressed. Further optimizations can lead to improved performance.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Start Month|
|v_input_2|true|Start Date|
|v_input_3|(2019)|Start Year|
|v_input_4|true|End Month|
|v_input_5|true|End Date|
|v_input_6|(2020)|End Year|


> Source (PineScript)

```pinescript
//@version=4
strategy("PB SAR BackTest - Colorbar", overlay=false)

// Full credit to Sawcruhteez, Lucid Investment Strategies LLC, Casey Bowman and Peter Brandt.
// This is a strategy version of the Peterbolic SAR indicator created by the above-mentioned parties.
// Original version of the indicator: https://www.tradingview.com/script/6nYrH3Vm-Peterbolic-SAR/

// SAR #1
// Lucid Sar
// Branded under the name "Lucid SAR"
// as agreed to with Lucid Investment Strategies LLC on July 9, 2019
// https://lucidinvestmentstrategies.com/
// see branch "lucid"

// SAR #2
// Peterbolic Sar
// Using the name "Peterbolic SAR"
// as agreed to by Peter Brandt on October 2, 2019
// - https://twitter.com/PeterLBrandt/status/1179365590668075008
// in response to request from Sawcruhteez
// - https://twitter.com/Sawcruhteez/status/1179213105705836544
// Sawcruhteez gives credit to @CrazyGabey for coming up with the name
// - https://twitter.com/Sawcruhteez/status/1179213196583940097
// see branch "peterbolic"

// SAR #3
// Saw