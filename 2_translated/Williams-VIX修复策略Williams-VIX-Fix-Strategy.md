> Name

Williams-VIX修复策略Williams-VIX-Fix-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

This strategy aims to predict the volatility of the VIX market by using the Williams Vix Fix formula combined with Stochastic RSI and balance indicators. It captures hidden bullish divergences to identify market bottoms, achieving an accurate positioning of the market reversal point.

## Strategy Logic

The strategy is mainly based on the combination of the Williams Vix Fix formula and Stochastic RSI & RSI indicators.

Firstly, the current period's VIX value is calculated using the Williams Vix Fix formula by measuring the ratio of the highest price to the lowest price, which represents market volatility and panic levels. Upper and lower Bollinger bands are set here; when the VIX value is higher than the upper band, it indicates increased market fluctuation and investor panic; when lower than the lower band, it signifies a stable market.

Secondly, the strategy adopts the combination of Stochastic RSI and RSI indicators. RSI is used to determine long/short positions, while Stoch RSI combines K & D lines to identify reversal points of RSI. Sell signals are generated when Stoch RSI falls from overbought territory.

Finally, the strategy integrates both by taking Stoch RSI's overbought signal as the basis for selling and VIX value below the lower Bollinger band as the basis for buying, achieving effective market reversal point capture.

## Advantage Analysis

The biggest advantage of this strategy is that it can utilize the strengths of two different indicators in combination. 

The Williams Vix Fix formula effectively reflects market panic emotions; the dynamic adjustment of Bollinger bands can adapt to different cycles. The Stochastic RSI identifies RSI reversal points through the crossover of K & D lines, avoiding false signals.

Combined use can more accurately locate market reversal points. It generates sell signals when market panic index releases signals while utilizing Stoch RSI to determine specific entry points, thus avoiding erroneous entries.

## Risk Analysis

This strategy also has certain risks:

1. The Williams Vix Fix formula may not fully reflect market panic emotions; improper Bollinger band parameters can generate false signals.
2. Reversal signals of Stochastic RSI may also be wrong and need to be verified with other indicators.
3. The strategy is relatively conservative, which may miss opportunities if unable to track fast-moving markets in a timely manner.
4. The strategy may have larger drawdowns, requiring careful position sizing.

When using this strategy, we need to set parameters reasonably, verify with other indicators, and control position sizes to mitigate risks.

## Optimization Directions

Some ways to optimize this strategy:

1. Optimize the parameters of the Williams Vix formula to more accurately reflect market panic levels. Consider combining with moving averages.
2. Optimize Stochastic RSI parameters to find better combinations of K & D periods for higher reversal accuracy.
3. Add position sizing mechanisms like stop loss/take profit, or dynamic position adjustment based on drawdown/profit ratio.
4. Incorporate other indicators like MACD and KD to achieve multi-indicator verification and reduce false signals.
5. Add machine learning algorithms, use big data to train models and auto-optimize parameters, improving strategy stability.

Through these optimizations, the strategy's performance and stability can be significantly enhanced.

## Conclusion

The Williams Vix Fix strategy captures market panic and stability transitions, using Stoch RSI to determine specific entry points effectively locating market bottoms. Its advantage lies in indicator combination use, but there are also certain risks. We can strengthen the strategy by parameter optimization and multi-indicator verification, making it an effective tool for identifying market reversals.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|lookback length of Stochastic|
|v_input_2|80|Stochastic overbought condition|
|v_input_3|20|Stochastic oversold condition|
|v_input_4|3|smoothing of Stochastic %K |
|v_input_5|3|moving average of Stochastic %K|
|v_input_6|14|lookback length of RSI|
|v_input_7|70|RSI overbought condition|
|v_input_8|30|RSI oversold condition|
|v_input_9|22|LookBack Period Standard Deviation High|
|v_input_10|20|Bolinger Band Length|
|v_input_11|2|Bollinger Band Standard Devaition Up|
|v_input_12|50|Look Back Period Percentile High|
|v_input_13|0.85|Highest Percentile - 0.90=90%, 0.95=95%, 0.99=99%|
|v_input_14|false|-------Te