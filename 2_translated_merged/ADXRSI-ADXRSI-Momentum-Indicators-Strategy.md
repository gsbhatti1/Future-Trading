> Name

ADXRSI Momentum Indicators Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13ea780e8d31b825e6f.png)
[trans]
### Overview

This strategy utilizes momentum indicators ADX, RSI, and Bollinger Bands to determine market trends and overbought/oversold conditions, in order to implement automated trading for buying low and selling high.

### Strategy Principles

1. ADX indicator determines trend. When ADX is greater than 32, it indicates a trending market.
2. RSI indicator determines overbought/oversold levels. When RSI crosses above 30, it signals an oversold market; when RSI crosses below 70, it signals an overbought market.
3. Bollinger Bands determine consolidation and breakout. When close price breaks above the upper band, it signals the end of consolidation and an upside breakout. When close price breaks below the lower band, it signals the end of consolidation and a downside breakout.

Based on the indicators above, the trading strategy is defined as follows:

Buy condition:
1. ADX > 32, trend status
2. RSI crosses above 30, oversold state
3. Close price below lower Bollinger band, end of downtrend consolidation

Sell condition:
1. ADX > 32, trend status
2. RSI crosses below 70, overbought state
3. Close price above upper Bollinger band, end of uptrend consolidation

### Advantage Analysis

This strategy utilizes multiple indicators to determine market conditions, avoiding the probability of error when relying on a single indicator. By determining trend and overbought/oversold status, it can effectively capture market turning points and achieve buy low sell high.

Compared to using trend indicators alone, this strategy can capture short-term opportunities in a timelier manner. Compared to using solely oscillators, this strategy can better grasp the trend direction. Therefore, it retains the advantage of tracking trends while also having the flexibility of mean-reversion trading. It is a potentially efficient quantitative strategy.

### Risk Analysis

The main risks of this strategy include:

1. The risk of false signals from indicators. Indicators may fail when markets experience extreme events.
2. The risk of stop losses being too tight. Short-term market fluctuations may take out the position if stops are too close.
3. The risk of overfitting. If indicator parameters are merely fitted to historical data, the stability would be questionable and may fail to adapt to changing market dynamics.

Risk management measures:

1. Manually intervene under abnormal market conditions to pause the strategy and avoid losses from false signals.
2. Set reasonable stop distance, combining with moving averages to determine stop levels, avoiding being stopped out prematurely.
3. Introduce Parameter Tuning module, dynamically optimize parameters using Walk Forward Analysis to ensure robustness.

### Optimization Directions

The main aspects to improve this strategy include:

1. Optimize indicator parameters, using machine learning algorithms tailored to each market.
2. Feature engineering, introducing more technical indicators and training models like SVM to improve signal accuracy.
3. Incorporate breakout strategies based on characteristics of each market using price channels, supports/resistances etc., to enhance stability.
4. Optimize profit taking and stop loss mechanisms by introducing trailing stops, moving stops etc., to maximize profit and effectively control risks.

### Conclusion

This medium-term quantitative trading strategy utilizes multiple technical indicators like ADX, RSI, and Bollinger Bands to determine market conditions and places trades when significant structural changes are identified. The logic is clear and interpretable, drastically reducing reliance on a single indicator. Meanwhile, risks such as false signals, overly tight stops, and parameter overfitting need to be addressed through risk management and model optimization to enhance stability and efficiency.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|ADX Smoothing|
|v_input_2|14|DI Length|
|v_input_3|20|threshold|
|v_input_4|7|Periodo RSI|
|v_input_5|30|Livello Ipervenduto|
|v_input_6|70|Livello Ipercomprato|
|v_input_7|50|Periodo BB|
|v_input_8|2|Dev BB|

> Source (PineScript)

```pinescript
//@version=4
strategy("ADXRSI Momentum Indicators Strategy", overlay=true)

// Create ADX
adxlen = input(14, title="ADX Smoothing")
dilen = // Continue the code block as it was in the original script
```