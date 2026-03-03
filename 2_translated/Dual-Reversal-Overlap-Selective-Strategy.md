> Name

Dual-Reversal-Overlap-Selective-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fb1c725ca92b7921b7.png)

[trans]

## Overview

The Dual Reversal Overlap Selective Strategy (Dual Reversal Overlap Selective Strategy) combines reversal trading strategies and overbought/oversold filters to achieve asset allocation and timing trading. This strategy aims to take long and short positions at trend reversal points while avoiding unnecessary trades in irrational expansion areas using overbought/oversold indicators.

## Strategy Logic

The strategy consists of two overlapping sub-strategies:

1. 123 Reversal Strategy

This strategy uses reversal signals based on two consecutive days of closing price reversal. Specifically, it goes long if the closing prices rise over the last two days and the 9-day slow stochastic is below 50, and it goes short if the closing prices fall over the last two days and the 9-day fast stochastic is above 50. This reversal strategy aims to capture short-term trend reversals.

2. DSS Oscillator Strategy

This strategy uses the DSS oscillator for overbought/oversold analysis. It goes long if the 5-day moving average (MA) is below the 10-day MA and the 20 oversold level, and it goes short if the 5-day MA is above the 10-day MA and the 80 overbought level. This overbought/oversold strategy helps avoid unnecessary trades in irrational zones.

The final signal is generated only when both strategies agree. This improves profitability by combining the strengths of the two strategy types.

## Advantage Analysis

1. Combines the advantages of reversal and overbought/oversold strategies — catching short-term reversals while avoiding irrational zone trades.

2. Simple logic and few parameters make 123 reversal easy to implement. DSS uses double smoothing for robust overbought/oversold analysis, effectively filtering out bearish signals in bull markets and bullish signals in bear markets.

3. Combination improves signal reliability by reducing false signals.

4. Flexible parameter tuning adapts the strategy to different markets.

## Risk Analysis

1. Reversal strategies have "picking up pennies" risk and whipsaw in ranging markets.

2. DSS optimization is difficult and sensitive to parameters.

3. Divergent signals may miss trading opportunities.

4. Simple price indicators limit profitability.

Solutions:

1. Shorten holding periods to reduce whipsaw risk.

2. Careful parameter tuning based on successful examples.

3. Add filters to improve strategy performance.

4. Optimize entry timing or position sizing.

## Enhancement Directions

1. Test other reversal indicators to improve signal accuracy.

2. Explore alternative overbought/oversold indicators like RSI.

3. Add stop loss mechanisms to lock in profits and limit losses.

4. Optimize parameters for different markets.

5. Consider dynamic parameter adjustment based on market conditions.

6. Build machine learning models to generate signals.

## Conclusion

The Dual Reversal Overlap Selective Strategy provides both asset allocation and timing trading functionality through combining reversal and overbought/oversold strategies. It has advantages like flexible parameters, simple logic, and easy implementation, effectively filtering out noise trades in irrational zones. But limitations exist like reversal risks and parameter optimization difficulties. Future enhancements can come from adding stop loss mechanisms, parameter optimization, machine learning incorporation, etc. Overall, it provides a robust quantitative trading solution.

||


## Overview

The Dual Reversal Overlap Selective Strategy combines reversal trading strategies with overbought/oversold filters to achieve asset allocation and timing trading. It aims to take long and short positions at trend reversal points while avoiding unnecessary trades in irrational expansion areas using overbought/oversold indicators.

## Strategy Logic

The strategy consists of two overlapping sub-strategies:

1. 123 Reversal Strategy  

This strategy uses reversal signals based on two consecutive days of closing price reversal. Specifically, it goes long if the closing prices rise over the last two days and the 9-day slow stochastic is below 50, and it goes short if the closing prices fall over the last two days and the 9-day fast stochastic is above 50. This reversal strategy aims to capture short-term trend reversals.

2. DSS Oscillator Strategy

This strategy uses the DSS oscillator for overbought/oversold analysis. It goes long if the 5-day moving average (MA) is below the 10-day MA and the 20 oversold level, and it goes short if the 5-day MA is above the 10-day MA and the 80 overbought level. This overbought/oversold strategy helps avoid unnecessary trades in irrational zones.

The final signal is generated only when both strategies agree. This improves profitability by combining the strengths of the two strategy types.

## Advantage Analysis

1. Combines the advantages of reversal and overbought/oversold strategies - catching short-term trend reversals while avoiding non-rational zone trades.

2. 123 Reversal Strategy has fewer parameters, simple logic, and is easy to implement. The DSS Oscillator uses double exponential smoothing for robust overbought/oversold analysis, effectively filtering out bearish signals in bull markets and bullish signals in bear markets.

3. Combining two different types of strategies improves signal reliability while reducing false signals from the original strategy.

4. Flexible parameter settings allow adjustments based on different market conditions, enhancing adaptability.

## Risk Analysis

1. Reversal strategies are prone to "picking up pennies" risk and whipsaw in ranging markets.

2. DSS Oscillator Strategy optimization is challenging due to its sensitivity to parameters.

3. Inconsistent signals may lead to missed trading opportunities.

4. The strategy relies solely on simple price indicators, limiting potential profitability.

Solutions:

1. Shorten holding periods to reduce the risk of whipsaw.

2. Carefully test parameter combinations based on successful examples and optimize for specific markets.

3. Introduce additional filters to enhance the effectiveness of the strategy.

4. Optimize entry timing or adjust position sizing accordingly.

## Enhancement Directions

1. Test other reversal indicators to improve signal accuracy.

2. Explore alternative overbought/oversold indicators like RSI.

3. Add stop loss mechanisms to lock in profits and limit losses.

4. Optimize parameters for different market conditions.

5. Consider dynamic parameter adjustment based on changing market conditions.

6. Incorporate machine learning models to generate trading signals.

## Conclusion

The Dual Reversal Overlap Selective Strategy provides both asset allocation and timing trading functionalities through the combination of reversal and overbought/oversold strategies. It offers advantages such as flexible parameters, simple logic, and easy implementation, effectively filtering out noise trades in non-rational zones. However, it also faces challenges like reversal risks and parameter optimization difficulties. Future improvements can be achieved by incorporating stop loss mechanisms, optimizing parameters, and integrating machine learning models to enhance the strategy's performance.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|10|PDS|
|v_input_6|9|EMAlen|
|v_input_7|5|TriggerLen|
|v_input_8|80|Overbought|
|v_input_9|20|Oversold|
|v_input_10|false|Trade reverse|


> Source (PineScript)

```pinescript
//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 12/03/2020
// This is a combo strategy for getting a cumulative signal.
// 
// First strategy
// This system was created from the book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, page 183. This is a reversal type of strategies.
// The strategy buys at market if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50.
// The strategy sells at market if close price is lower than the previous close 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.

```