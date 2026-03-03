> Name

RSI True Level Breakout Strategy RSI-True-Level-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1264238b32a4cea9bbc.png)
[trans]


### Overview

The RSI True Level Breakout strategy is a quantitative trading strategy that combines the RSI indicator with true range bands to implement breakout trades. It calculates upper and lower bounds of the true range based on closing prices, standard deviations, and linear regression, using the RSI overbought/oversold signals for trade entry. In strong trending markets, it can capture trend directions early; in range-bound markets, it effectively filters noise and locks in significant directional opportunities.

### Strategy Logic

First, manually set 14 different parameter true range bands. True ranges are calculated based on closing prices, standard deviation, and linear regression over a certain period. The upper band is the linear regression line plus n times the standard deviation, while the lower band is the linear regression line minus n times the standard deviation. Parameter n can be adjusted through the interface. This plots 14 true range bands with different parameters.

Next, in each period, the highest of the 14 bands serves as the true range upper bound and the lowest as the lower bound. Combined with RSI values, it determines if RSI enters overbought or oversold zones. When RSI is overbought or price breaks below the upper band, a short position is taken; when RSI is oversold or price rises above the lower band, a long position is initiated.

Finally, entry and exit bands are set. The entry line represents the true range lower bound, while the exit line represents the upper bound of the true range. After opening positions, prices touching the exit line again will trigger stop-loss exits.

Overall, this strategy leverages both the trend strength of RSI and the adaptive ability of true range channels to effectively determine market trends, capture significant directional opportunities in range-bound markets, and manage risk with the exit bands.

### Advantages

1. Uses adaptive true range zones. The upper and lower bands change dynamically to adapt to market fluctuations.
2. Customizable true range parameters. Users can optimize parameters for different market conditions.
3. Combines RSI overbought/oversold signals to avoid whipsaws in sideways markets.
4. Reasonable entry and exit lines help control risk.

### Risks

1. Careful optimization of RSI parameters is required. Incorrect values may generate misleading signals.
2. True range parameters need testing and optimization. Unsuitable settings can undermine performance.
3. High whipsaw risk in choppy markets when prices frequently hit the exit bands, leading to significant losses.
4. True range bands require a sufficient period to form. The strategy may fail with insufficient data.

These risks can be mitigated by optimizing RSI parameters, adjusting true range settings, adding filters, and using prudent exits. Parameters should be tuned for different market environments.

### Optimization Directions

1. Optimize RSI parameters to find the best settings. Test different RSI periods.
2. Optimize true range parameters for current markets.
3. Add other indicators like MACD or KD to avoid incorrect trades in sideways markets.
4. Test different trading times or products to identify optimal environments.
5. Optimize exits, such as trailing stops or ATR-based stop losses.
6. Combine parameter testing and seek maximum stability.
7. Utilize machine learning and big data for automatic optimization.

### Conclusion

The RSI True Level Breakout strategy integrates the strengths of a trend indicator and adaptive channel technology. It can effectively determine market trends and capture significant directional opportunities in range-bound markets while controlling risk with exit bands. The high degree of parameter customization allows it to be tuned for different market conditions, making it a very flexible breakout strategy. Overall, by integrating multiple indicators, it has advantages in trend determination and risk control, making it a recommended quantitative trading strategy.

||

### Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|RSI Period|
|v_input_2|65|RSI Overbought Level|
|v_input_3|40|RSI Oversold Level|
|v_input_4|12|Entry TrueLevel Band|
|v_input_5|12|Exit TrueLevel Band|
|v_input_6|false|Enable Long and Short|
|v_input_7|126|Length 1|
|v_input_8|189|Length 2|
|v_input_9|252|Length 3|
|v_input_10|378|Length 4|
|v_input_11|504|Length 5|
|v_input_12|630|Length 6|
|v_input_13|756|Length 7|
|v_input_14|1008|Length 8|
|v_input_15|1260|Length 9|
|v_input_16|1638|Length 10|
|v_input_17|2016|Length 11|
|v_input_18|2646|Length 12|
|v_input_19|3276|Length 13|
|v_input_20|4284|Length 14|