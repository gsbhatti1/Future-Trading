> Name

Three-Color-Cross-Trend-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/9012c0d4b2e95ac656.png)
[trans]
## Overview

The three-color cross trend following strategy is a trend-following trading strategy based on candlestick patterns. It identifies the direction of the current trend by recognizing specific three-color candlestick patterns and selectively goes long or short when the patterns are identified.

## Strategy Principle

The core logic of this strategy is: When three consecutive candlesticks of the same color (three red or three green) appear, followed by one candlestick of a different color, and then reverse back to the original three candlesticks' color, it indicates that the original trend is continuing. Therefore, this is the time to track the trend by entering into a position.

Specifically, the strategy detects the situation of the most recent five candlesticks to determine if the entry criteria are met. If the most recent five candlesticks are: 
- The fifth candle has a lower low than the previous one (higher high for long), 
- The fourth candle is a bullish candle (bearish for long), 
- The third candle is a bearish candle (bullish for long), 
- The second candle is a bearish candle (bullish for long), 
- The first candle is a bearish candle (bullish for long), 

then a short tracking position is opened. On the contrary, if the most recent five candlesticks are: 
- The fifth candle has a higher high than the previous one, 
- The fourth candle is a bearish one, 
- The third candle is a bullish one, 
- The second candle is a bullish one, 
- And the first candle is a bullish one, 

then a long tracking position is opened. By judging the trend direction through such specific candlestick patterns, additional profits can be made when the trend persists.

## Strategic Advantages

- Use candlestick patterns to determine the trend direction, easy to operate
- Can profit during the continuation phase of the trend
- The policy rules are simple and clear

## Strategy Risk

- Misjudgment of candlestick shape may lead to losses
- Unable to determine the trend reversal point, you may lose money following the trend.
- Positions may be opened frequently, increasing transaction costs

## Strategy Optimization Direction

- Combine with other indicators to determine the reliability of the candlestick pattern
- Set stop loss points to control single losses
- Optimize position opening conditions and reduce the probability of incorrect judgments
- Consider adjusting position size to reduce risk

## Summary

The three-color cross trend following strategy determines the current trend direction by identifying specific candlestick patterns and selectively opens positions when the trend continues. This strategy is simple, clear, easy to operate, and can obtain additional income during the trend stage. However, there are certain risks and further optimization is needed to improve stability. Overall, this strategy is an effective complementary component in a quantitative trading strategy portfolio.

||

## Overview

The Three Color Cross Trend Tracking Strategy is a trend-following trading strategy based on candlestick patterns. It identifies the direction of the current trend by recognizing specific three-color candlestick patterns and selectively goes long or short when the patterns are identified.

## Strategy Principle

The core logic of this strategy is: When three consecutive candlesticks of the same color (three red or three green) appear, followed by one candlestick of the opposite color, and then reverse back to the original three candlesticks' color, it indicates that the original trend is continuing. Therefore, this is the time to track the trend by entering into a position.

Specifically, the strategy detects the situation of the most recent five candlesticks to determine if the entry criteria are met. If the most recent five candlesticks are: 
- The fifth candle has a lower low than the previous one (higher high for long), 
- The fourth candle is a bullish candle (bearish for long), 
- The third candle is a bearish candle (bullish for long), 
- The second candle is a bearish candle (bullish for long), 
- And the first candle is a bearish candle (bullish for long), 

then a short tracking position is opened. On the contrary, if the most recent five candlesticks are: 
- The fifth candle has a higher high than the previous one, 
- The fourth candle is a bearish one, 
- The third candle is a bullish one, 
- The second candle is a bullish one, 
- And the first candle is a bullish one, 

then a long tracking position is opened. By judging the trend direction through such specific candlestick patterns, additional profits can be made when the trend persists.

## Advantages of the Strategy

- Determine trend direction easily using candlestick patterns
- Make profits during trend persistence stages
- Simple and clear strategy rules

## Risks of the Strategy

- Incorrect judgments of candlestick patterns may lead to losses
- Unable to determine trend reversal points, may suffer losses following the trend
- May frequently open positions, increasing trading costs

## Directions for Strategy Optimization

- Incorporate other indicators to judge reliability of candlestick patterns
- Set stop loss points to control single trade loss
- Optimize entry criteria to reduce probability of incorrect judgments
- Consider adjusting position sizing to lower risks

## Summary

The Three Color Cross Trend Tracking Strategy identifies current trend direction by recognizing specific candlestick patterns, and selectively opens positions when the trend persists. This strategy is simple, clear, easy to operate, and capable of gaining additional profits during trend stages. But it also carries some risks, and needs further optimization to improve stability. Overall, it serves as an effective complementary component in quantitative trading strategy portfolios.

[/trans]


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-20 00:00:00
end:
```