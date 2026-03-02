> Name

Three-Inside-Up-Reversal-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10fc9d799add7abfc1e.png)

[trans]


## Overview

The Three-Inside-Up-Reversal-Strategy is a reversal trading strategy that aims to buy low and sell high by identifying specific three-bar candlestick patterns. It consists of three bars where the first two form a bullish harami pattern, and the third bar opens above the previous close and closes above the highs of the first two bars. This candlestick combination indicates a potential reversal from a downtrend to an uptrend, signaling an opportunity to enter a reversal trade.

## Strategy Logic

The key conditions for this strategy are:

1. Bar 1: Bearish candle, open higher than close
2. Bar 2: Bullish candle, close higher than open and lower than the previous bar's open
3. Bar 3: Bullish candle, open higher than the second bar's close and close higher than the highs of Bars 1 and 2

When this pattern is detected, we take a short position and set profit and stop loss levels. The trading logic is as follows:

1. Enter short at the open of Bar 3 when the Three-Inside-Up pattern is identified
2. Set profit target: Close trade and flatten position if price rises by the input number of profit points  
3. Set stop loss: Close trade and flatten if price declines by the input number of loss points
4. Clear position when target or stop is hit, await next signal

This allows us to quickly enter a short when an uptrend reversal signal is identified, and realize gains or limit losses using predefined profit and stop levels, implementing a low buy high sell reversal strategy.

## Advantages

- Captures reversal points for reversal trading
- Shorts tops and buys bottoms aligning with trends  
- Clear entry, profit take, and stop loss mechanics
- Simple 3-bar pattern, easy to identify and implement
- Customizable profit take and stop loss points to control risk
- Code is simple, clean, easy to understand and optimize

In summary, this strategy leverages pattern recognition, risk management, simplicity, and reliability making it an effective short-term reversal trading strategy.

## Risks

- Pattern may be misidentified, leading to false signals
- Inadequate profit take or stop loss levels could lead to premature exit or missed profits
- Frequent trading increases overtrading risk 
- Entry, position sizing, and management can be further optimized
- Careful stock selection required, better for volatile stocks
- Impact of commissions and slippage on profits
- Requires ongoing monitoring and tuning for changing markets

Proper parameter optimization, stock selection, monitoring, and other measures can help control the risks.

## Enhancement Opportunities

- Optimize pattern parameters to improve accuracy
- Refine profit take and stop loss for better risk-reward
- Add filters using other indicators to improve signal reliability 
- Incorporate dynamic position sizing aligned to market conditions
- Optimize capital allocation for better profit balancing
- Test different holding periods to determine optimal duration
- Streamline code with comments for clarity
- Backtest versus live performance to validate efficacy
- Adjust stock universe and test sector and name fit
- Continuously track performance and tune as required

## Conclusion

The Three-Inside-Up-Reversal-Strategy aims to profit from shorting tops when an uptrend reversal signal is identified based on a specific three-candlestick pattern. With clear logic, risk controls, ease of use, and optimization potential, it is a reliable and practical short-term reversal trading strategy. But uncertainties exist requiring ongoing optimizations, risk management, and monitoring to generate consistent excess returns in live trading.

||


## Overview

The Three Inside Up Reversal Strategy is a reversal trading strategy that identifies specific three-bar candlestick patterns to achieve low buy high sell reversals. It consists of three bars where the first two form a bullish harami pattern, then followed by an up bar with a higher close than the prior close. This candlestick combination indicates a potential short-term price reversal from decline to ascent and signals an opportunity for a reversal operation.

## Strategy Logic

Key conditions for this strategy are:

1. Bar 1: Bearish candle, open above close
2. Bar 2: Bullish candle, close above open and below the previous bar's open
3. Bar 3: Bullish candle, open above the second bar's close and close above the highs of Bars 1 and 2

When this signal is detected, we establish a short position with predefined profit and stop loss levels. The trading logic:

1. Enter short at the open of Bar 3 when Three Inside Up pattern is identified
2. Set profit target: Close trade if price rises by the input number of points  
3. Set stop loss: Close trade if price declines by the input number of points
4. Clear position when target or stop is hit, await next signal

This allows timely short entries on reversal signals and using predefined levels to limit losses or capture gains in a low buy high sell reversal strategy.

## Advantages

- Captures potential reversal points for reversals trading
- Shorting tops and buying bottoms align with trend trading logic  
- Clear entry, profit take, and stop loss mechanisms 
- Simple 3-bar pattern, easy to recognize and implement
- Customizable profit and stop levels to manage risk
- Code is simple and clean, easy to understand and optimize

In summary, this strategy relies on recognizing patterns, managing risks through predefined rules, being straightforward, and reliable making it an effective short-term reversal trading strategy.

## Risks

- Incorrect pattern identification can lead to false signals
- Inappropriate profit or stop levels may result in premature exits or missed profits
- Frequent trading increases overtrading risk 
- Further optimization is needed for entry, position sizing, and management strategies
- Careful stock selection required, works better with volatile stocks
- Commissions and slippage impact profitability  
- Ongoing monitoring and adjustment are necessary for changing market conditions

Proper parameter tuning, cautious stock selection, ongoing monitoring, and other measures can help manage these risks.

## Enhancement Opportunities

- Optimize candle pattern parameters to improve accuracy 
- Refine profit take and stop loss mechanisms for better risk-reward ratio
- Integrate filters using other technical indicators to enhance signal reliability  
- Incorporate dynamic position sizing aligned with market conditions
- Optimize capital allocation for balanced performance
- Test different holding periods to find the optimal duration
- Streamline code with comments for clarity 
- Backtest versus live trading to validate effectiveness
- Adjust stock universe and test sector and name fit 
- Continuously monitor performance and adjust as needed

## Conclusion

The Three Inside Up Reversal Strategy aims to profit from shorting tops when an uptrend reversal signal is detected based on specific three-candlestick patterns. With clear logic, risk management mechanisms, ease of implementation, and optimization potential, it is a reliable and practical short-term reversal trading strategy. However, uncertainties exist that require ongoing optimizations, risk control measures, and continuous monitoring to achieve consistent excess returns in live trading.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Take Profit pip|
|v_input_2|20|Stop Loss pip|


> Source (PineScript)

```pinescript
//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 12/02/2019
//    This is a three candlestick bullish reversal pattern consisting of a 
//    bullish harami pattern formed by the first 2 candlesticks then followed 
//    by up candlestick with a higher close than the prior candlestick.
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
/////////////////////////////////////////
```