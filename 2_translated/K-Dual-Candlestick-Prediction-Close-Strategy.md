> Name

Dual-Candlestick-Prediction-Close-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c0255ff8649abe9773.png)
[trans]

## Overview

The purpose of this strategy is to predict the close price of the next 15-minute candlestick by analyzing the open and close prices of the past two 30-minute candlesticks. It judges whether the trend of the next 15-minute candlestick will continue going up, down or sideways based on the trend.

## Strategy Principle

The core logic of this strategy lies in the `predictNextCandleClose` function. This function takes the open and close prices of the previous two 30-minute candlesticks as input parameters.

If the close price of the last 30-minute candlestick is higher than the open price, it is judged as a bullish trend; if the close price is lower than the open price, it is judged as a bearish trend. If the second last 30-minute candlestick also shows the same bullish or bearish trend, it is considered that the trend is stronger and the next 15-minute candlestick will likely continue the trend.

Specifically, if both of the most recent two 30-minute candlesticks are bullish (close price higher than open price), the predicted close price of the next 15-minute candlestick will be higher than the current candlestick's close price by the difference between the last 30-minute candlestick's close price and open price.

If both of the most recent two 30-minute candlesticks are bearish (close price lower than open price), the predicted close price of the next 15-minute candlestick will be lower than the current candlestick's close price by the difference between the last 30-minute candlestick's open price and close price.

If one of the most recent two 30-minute candlesticks is bullish and the other is bearish, it indicates there is no clear trend, and in this case the predicted close price of the next 15-minute candlestick will be the same as the close price of the last 30-minute candlestick.

In this way, it predicts the short-term price movement in the future based on past candlestick information, serving as a reference for trading decisions.

## Advantage Analysis

This dual candlestick prediction strategy has the following advantages:

1. It is simple, intuitive and easy to understand and implement, suitable for quant trading beginners.
2. By judging the trend using dual candlesticks, it can filter out some noise and improve the accuracy.
3. The 15-minute level prediction has a short time span, which helps adjust positions in a timely manner.
4. Combined with current price and predicted price to determine trading signals, it can respond quickly to unexpected events.
5. It requires less historical data, reducing data needs and making it suitable for incomplete data or live trading scenarios.

## Risk Analysis

However, there are also some risks with this strategy:

1. It only considers open and close prices, lacking more candlestick details as auxiliary judgement, thus may miss important signals.
2. The interval between the two candlesticks is long, unable to respond timely to short-term price fluctuations, posing time lag risks.
3. The prediction relies solely on historical data, unable to judge the impact of significant unexpected events, with higher risks.
4. The bullish/bearish rules are quite simple, prone to generating false signals and the signal quality needs improvement.
5. Real trading data often has gaps, which could also interfere with the accuracy of the judgement logic.

## Optimization Directions

In light of the above risks, the strategy can be optimized from the following aspects:

1. Add more auxiliary indicators like MACD, KD etc to improve prediction accuracy.
2. Combine more candlestick details like shadows, real body etc to determine critical price levels and refine bullish/bearish rules.
3. Increase sample size, expand the time range of judgement candlesticks to avoid interference from short-term noises.
4. Add stop loss mechanisms like moving stop loss, timed stop loss etc to control single trade loss.
5. Optimize entry rules to only open positions when the trend is clear, avoiding uncertain market fluctuations.
6. Backtest with real trading data, modify logic that does not match actual price moves to make the strategy parameters closer to the real market.

## Conclusion

This strategy predicts short-term trends by analyzing the open and close prices of dual candlesticks, and generates trading signals based on it. It belongs to a predictive strategy that uses historical data. This strategy is simple and easy to use, suitable for quant trading beginners, but also has limitations such as single judgment rules and limited signal quality. We can optimize this strategy from aspects like auxiliary indicators, candlestick details, stop loss mechanisms, etc., to make the practical effect better. Overall, the dual candlestick prediction strategy provides a basis that is worth optimizing and iterating.