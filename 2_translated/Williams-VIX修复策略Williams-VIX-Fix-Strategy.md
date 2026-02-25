> Name

Williams-VIX Fix Strategy Williams-VIX-Fix-Strategy

> Author

ChaoZhang

> Strategy Description


## Overview

This strategy aims to predict VIX market volatility by using the Williams VIX Fix formula in combination with Stochastic RSI and Balance of Power indicators. It captures hidden bullish divergences to identify market bottoms and accurately locate reversal points.

## Strategy Logic

The strategy is mainly based on the combination of the Williams VIX Fix formula, Stochastic RSI, and RSI indicators.

Firstly, the current period's VIX value is calculated using the Williams VIX Fix formula. This formula measures market volatility and panic levels by calculating the ratio of highest price to lowest price. Upper and lower bollinger bands are set here; when VIX values exceed the upper band, it indicates increased market fluctuations and investor panic; when below the lower band, it suggests a stable market.

Secondly, the strategy employs the combination of Stochastic RSI and RSI indicators. RSI is used to determine long/short positions, while Stoch RSI combines K and D lines to identify reversal points of RSI. Sell signals are generated when Stoch RSI falls from an overbought zone.

Finally, the strategy integrates both by using Stoch RSI's overbought signal as a basis for selling and VIX values below the lower bollinger band as a basis for buying, achieving effective capture of market reversal points.

## Advantage Analysis

The primary advantage of this strategy is that it combines the strengths of two different indicators.

The Williams VIX Fix formula effectively reflects market panic emotions. The dynamic adjustment of bollinger bands can adapt to different cycles; Stochastic RSI identifies RSI reversal points through the crossover of K and D lines, avoiding false signals.

Together, these two indicators can more accurately locate market reversal points. Sell signals are generated when the market panic index releases signals while using Stoch RSI to determine specific entry points, thus avoiding erroneous entries.

## Risk Analysis

There are also some risks associated with this strategy:

1. The Williams VIX Fix formula cannot fully reflect market panic emotions; improper parameters for bollinger bands may generate incorrect signals.
2. Reversal signals of Stochastic RSI might also be wrong and need to be verified using other indicators.
3. This is a relatively conservative strategy, which could miss opportunities if unable to track fast-moving markets timely.
4. The strategy may have larger drawdowns, requiring careful position sizing.

To mitigate these risks, we should set parameters reasonably, verify with additional indicators, and control position sizes when implementing this strategy.

## Optimization Directions

Some ways to optimize this strategy:

1. Optimize the parameters of the Williams VIX formula to more accurately reflect market panic levels; consider combining it with moving averages.
2. Optimize Stochastic RSI parameters to find better K and D period combinations for higher reversal accuracy.
3. Add position management mechanisms such as stop loss/take profit or dynamic position adjustment based on drawdown/profit ratio.
4. Integrate other indicators like MACD, KD to achieve multi-indicator verification and reduce false signals.
5. Incorporate machine learning algorithms, utilize big data to train models for automatic parameter optimization, improving strategy stability.

Through these optimizations, the practical effectiveness and stability of the strategy can be significantly enhanced.

## Conclusion

The Williams VIX Fix strategy captures market panic and stability transitions and uses Stochastic RSI to determine specific entry points effectively locating market bottoms. Its advantage lies in combining indicators, but it also involves certain risks. We can strengthen the strategy by parameter optimization and multi-indicator verification, making it an effective tool for identifying market reversals.

---

> Strategy Arguments


|Argument        |Default Value| Description                                                                 |
|----------------|-------------|-----------------------------------------------------------------------------|
|v_input_1       | 14          | Lookback length of Stochastic                                             |
|v_input_2       | 80          | Stochastic overbought condition                                           |
|v_input_3       | 20          | Stochastic oversold condition                                             |
|v_input_4       | 3           | Smoothing of Stochastic %K                                                |
|v_input_5       | 3           | Moving average of Stochastic %K                                           |
|v_input_6       | 14          | Lookback length of RSI                                                    |
|v_input_7       | 70          | RSI overbought condition                                                  |
|v_input_8       | 30          | RSI oversold condition                                                    |
|v_input_9       | 22          | LookBack Period Standard Deviation High                                    |
|v_input_10      | 20          | Bolinger Band Length                                                       |
|v_input_11      | 2           | Bollinger Band Standard Devaition Up                                       |
|v_input_12      | 50          | Look Back Period Percentile High                                          |
|v_input_13      | 0.85        | Highest Percentile - 0.90=90%, 0.95=95%, 0.99=99%                          |
|v_input_14      | false       | ------Te