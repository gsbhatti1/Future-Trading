> Name

Double Moving Average Cross - Golden Cross Trading Strategy Golden-Cross-SMA-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/5d2bf237e941dc850a.png)
[trans]
## Overview

The double moving average cross (golden cross) trading strategy uses the crossover between two moving averages of different periods as buy and sell signals. Specifically, when the short-term moving average crosses above the long-term moving average from below, it generates a golden cross signal, indicating a bullish trend reversal. Conversely, when the short-term moving average crosses below the long-term moving average from above, it generates a death cross signal, indicating a bearish trend reversal.

## Principles

The strategy is based on two principles:

1. Moving averages can reflect market trends and momentum. The short-term moving average captures recent price movements and turning points, while the long-term moving average represents the overall trend of the market.

2. The formation of a golden cross between the short-term and long-term moving averages indicates that short-term momentum has surpassed long-term trends, suggesting the potential for a new uptrend. Conversely, a death cross indicates that the long-term downtrend is dominant, suggesting a continuation of the downtrend.

Specifically, this strategy uses 13-period and 30-period simple moving averages, and trades based on their crossovers. The crossover logic is as follows:

1. When the short-term moving average crosses above the long-term moving average, a golden cross signal is generated, indicating a long opportunity. The viability of the signal is evaluated by ensuring an ongoing uptrend for a certain period to confirm the bull trend.

2. When the short-term moving average crosses below the long-term moving average, a death cross signal is generated, indicating a short opportunity. Similarly, an ongoing downtrend is required to confirm the viability of the signal for shorting.

3. The slope difference between the moving averages is used to gauge the strength of the crossover signals. Only when the difference exceeds a certain threshold is the signal considered strong enough to trade on. This helps eliminate false signals.

4. The stop loss is set at 20%, and the take profit is set at 100%.

## Advantages

The double moving average cross strategy has the following advantages:

1. The logic is simple and easy to understand, making it suitable for beginners.

2. Utilizes price averaging to filter out noise and avoid being misled by short-term fluctuations.

3. Evaluates the strength of trends instead of blindly following crossover signals, ensuring a more thorough market confirmation.

4. Incorporates a slope momentum factor on the moving averages to make signals more reliable.

5. Backtesting and optimization are straightforward, requiring only a few key parameters such as moving average periods and trend duration.

## Risks

The strategy also has the following risks:

1. The crossovers are inherently lagging and cannot perfectly predict market reversals, leading to some delay. Shorter moving average periods or combining with predictive indicators can mitigate this risk.

2. Mechanical trading systems may trigger simultaneous trades, exacerbating momentum and invalidating stop losses or take profits. Staged exits or manual overrides can address this issue.

3. It may not perform well in choppy sideways markets. Avoid such instruments and focus on trending pairs.

4. The performance heavily depends on properly calibrated parameters like trend duration. Iterative testing is necessary to find the optimal values.

## Optimization Directions

The strategy can be further optimized by:

1. Adding higher-timeframe trend evaluation to avoid counter-trend trades. For example, using weekly or monthly prices.

2. Requiring trading volume confirmation to eliminate false signals. Only trade signals with increasing volume.

3. Optimizing moving average parameters to find the best period combinations. Consider adaptive moving average parameters.

4. Incorporating popular indicators like MACD and KD to assist in signal confirmation and accuracy.

5. Adopting staged stop loss and take profit levels to better control risk.

## Conclusion

The double moving average cross strategy is highly intuitive and easy to interpret. It combines the noise-filtering property of moving averages with the simple trend identification capability of crossover signals. The additional signal confirmation provides greater practicality and stability. Beyond the improvements mentioned, there remains significant room for further optimization, making it a worthwhile strategy to research.

||

## Overview

The golden cross SMA trading strategy generates buy and sell signals based on the crossover between two moving averages of different timeframes. Specifically, when the faster moving average crosses above the slower moving average from below, a golden cross is formed, indicating a bullish trend reversal. When the faster MA crosses below the slower MA from above, a death cross is formed, indicating a bearish trend reversal.

## Principles

The strategy is based on two principles:

1. Moving averages can reflect market trend and momentum. The shorter-term MA captures recent price movements and turning points; the longer-term MA represents the prevailing trend.

2. When the faster MA forms a golden cross with the slower MA, it indicates that the short-term momentum has gained strength over the long-term trend, hence likely the start of an uptrend. The death cross indicates that the long-term downtrend is dominant, thus likely a continued downtrend.

Specifically, this strategy uses 13 and 30-period simple moving averages, and trades their crossovers to generate signals. The crossover logic is:

1. The golden cross between the MAs generates a long signal, indicating a buying opportunity. The viability of the signal is evaluated by requiring an ongoing uptrend over some minimum period to confirm the bull trend.

2. The death cross between the MAs generates a short signal. Similarly, an ongoing downtrend is required to confirm the viability of the signal for shorting.

3. The slope difference between the MAs is used to gauge the strength of the crossover signals. Only when the difference exceeds a threshold would the signal be considered strong enough to trade on. This helps eliminate false signals.

4. Stop loss is set at 20%, and take profit is set at 100%.

## Advantages

The SMA crossover strategy has the following advantages:

1. The logic is simple and easy to understand, making it suitable for beginners.

2. Utilizes price averaging to filter out noise and avoid being misled by short-term fluctuations.

3. Evaluates trend persistence instead of just blindly following crossover signals, ensuring greater confirmation with overall market conditions.

4. Incorporates a slope momentum factor on the MAs to make signals more reliable.

5. Backtesting and optimization are straightforward, requiring only a few key parameters like MA periods and trend duration.

## Risks

The strategy also has the following risks:

1. Crossover signals are lagging by nature and cannot perfectly predict reversals. Delay risk exists. Should use shorter MAs or combine with predictive indicators.

2. Mechanical systems tend to trigger simultaneous trades, exacerbating momentum and invalidating stop loss/take profit. Should use staged exits or manual override.

3. Does not perform well in choppy sideways markets. Should avoid such instruments and focus on trending pairs.

4. Performance depends greatly on properly calibrated parameters like trend duration. Requires iterative testing to find optimum values.

## Optimization Directions

The strategy can be further optimized by:

1. Adding higher timeframe trend evaluation to avoid counter-trend trades. For example, using weekly or monthly prices.

2. Requiring trading volume confirmation to eliminate false signals. Only trade signals with expanding volume.

3. Optimizing MA parameters to find the best period combination. Consider adaptive moving average parameters.

4. Incorporating popular indicators like MACD, KD to assist in signal confirmation and accuracy.

5. Adopting staged stop loss/take profit to better control risk.

## Conclusion

The SMA crossover strategy is highly intuitive and easy to interpret. It combines the noise-filtering property of moving averages with the simple trend identification capability of crossover signals. The additional signal confirmation provides greater practicality and stability. Beyond the improvements mentioned, there remains ample room for further optimization, making this a worthwhile strategy to research.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Price Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|13|Short SMA Length|
|v_input_3|30|Long SMA Length|
|v_input_4|200|Short SMA Length|
|v_input_5|true|Weeks In Trend|
|v_input_6|0.01|Slope Fact