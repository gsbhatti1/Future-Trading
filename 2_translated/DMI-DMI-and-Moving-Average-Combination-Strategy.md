> Name

DMI and Moving Average Combination Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy combines the 123 Reversal Strategy, DMI (Directional Movement Index) Strategy, and Moving Average Strategy to form a powerful integrated strategy. It can perform reverse operations at trend reversal points and follow trends when they continue. Additionally, it uses moving averages to filter signals, effectively identifying market trends and improving the strategy's win rate.

## Strategy Logic

1. **123 Reversal Strategy**: Buy if the close price is higher than the previous day’s close for 2 consecutive days and the 9-day slow K line is below 50; Sell if the close price is lower than the previous day’s close for 2 consecutive days and the 9-day fast K line is above 50.

2. **DMI Strategy**: Buy when +DI (Positive Directional Indicator) crosses above -DI (Negative Directional Indicator); Sell when -DI crosses below +DI.

3. **Moving Average Strategy**: Buy when the close price crosses above the moving average; Sell when the close price crosses below the moving average.

4. Open positions only if all three strategies give consistent signals, otherwise close positions.

The strategy combines trend and reversal strategies to capture both turning points and trends flexibly. The moving average filter reduces false signals, and multiple strategies verify each other to improve signal reliability.

## Advantage Analysis

1. Combining various strategies enhances the win rate by utilizing different methods for capturing market movements.
2. Integrating reversal and trend strategies allows for flexible trading that can capture both reversals and trends.
3. The moving average filter helps reduce false signals caused by short-term fluctuations.
4. Multiple strategies provide cross-verification, avoiding reliance on a single strategy which may fail under specific market conditions.
5. With numerous parameters, the strategy can be optimized to find the best combination, increasing its stability.

## Risk Analysis

1. Reversal strategies are prone to being trapped in range-bound trends and may need additional trend-following signals for better performance.
2. The DMI strategy might miss early trend opportunities; adjusting DMI parameters could increase sensitivity.
3. Moving averages have a lag effect that can delay signal generation, shortening the period may help speed up response times.
4. While combining strategies improves win rate, it also increases complexity and may require careful parameter tuning.
5. The strategy is sensitive to transaction costs; setting wider stop losses might reduce frequent trading.

## Optimization Directions

1. Optimize parameters for each strategy to find the best combination.
2. Add other indicators like MACD or RSI to further enhance signal stability.
3. Incorporate stop loss strategies such as trailing stops to manage risks.
4. Improve position sizing through fixed or dynamic approaches to boost returns.
5. Tailor parameters for specific products to improve adaptiveness.
6. Integrate machine learning models to assist in decision-making and leverage more historical data.

## Conclusion

This strategy forms a flexible combination by integrating reversal, trend-following, and moving average filtering strategies. It captures both turning points and trend continuations effectively through multiple strategies, enhancing signal reliability. Further optimization of parameters, stop loss mechanisms, and position sizing can improve its practicality and expandability. With proficient application, this robust and versatile strategy has the potential to generate significant profits in live trading.

||

## Overview

This strategy combines the 123 Reversal Strategy, DMI (Directional Movement Index) Strategy, and Moving Average Strategy to form an effective integrated system. It can perform reverse operations at trend reversal points and follow trends when they continue. Meanwhile, it uses moving averages to filter signals and identify market trends to improve its win rate.

## Strategy Logic

1. **123 Reversal Strategy**: Buy if the close price is higher than the previous day’s close for 2 consecutive days and the 9-day slow K line is below 50; Sell if the close price is lower than the previous day’s close for 2 consecutive days and the 9-day fast K line is above 50.

2. **DMI Strategy**: Buy when +DI (Positive Directional Indicator) crosses above -DI (Negative Directional Indicator); Sell when -DI crosses below +DI.

3. **Moving Average Strategy**: Buy when the close price crosses above the moving average; Sell when the close price crosses below the moving average.

4. Open positions only if all three strategies give consistent signals, otherwise close positions.

The strategy combines trend and reversal strategies to capture both turning points and trends flexibly. The moving average filter reduces false signals, and multiple strategies verify each other to improve signal reliability.

## Advantage Analysis

1. Combining various strategies enhances the win rate by utilizing different methods for capturing market movements.
2. Integrating reversal and trend strategies allows for flexible trading that can capture both reversals and trends.
3. The moving average filter helps reduce false signals caused by short-term fluctuations.
4. Multiple strategies provide cross-verification, avoiding reliance on a single strategy which may fail under specific market conditions.
5. With numerous parameters, the strategy can be optimized to find the best combination, increasing its stability.

## Risk Analysis

1. Reversal strategies are prone to being trapped in range-bound trends and may need additional trend-following signals for better performance.
2. The DMI strategy might miss early trend opportunities; adjusting DMI parameters could increase sensitivity.
3. Moving averages have a lag effect that can delay signal generation, shortening the period may help speed up response times.
4. While combining strategies improves win rate, it also increases complexity and may require careful parameter tuning.
5. The strategy is sensitive to transaction costs; setting wider stop losses might reduce frequent trading.

## Optimization Directions

1. Optimize parameters for each strategy to find the best combination.
2. Add other indicators like MACD or RSI to further enhance signal stability.
3. Incorporate stop loss strategies such as trailing stops to manage risks.
4. Improve position sizing through fixed or dynamic approaches to boost returns.
5. Tailor parameters for specific products to improve adaptiveness.
6. Integrate machine learning models to assist in decision-making and leverage more historical data.

## Conclusion

This strategy forms a flexible combination by integrating reversal, trend-following, and moving average filtering strategies. It captures both turning points and trend continuations effectively through multiple strategies, enhancing signal reliability. Further optimization of parameters, stop loss mechanisms, and position sizing can improve its practicality and expandability. With proficient application, this robust and versatile strategy has the potential to generate significant profits in live trading.

---

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 14 | Length |
| v_input_2 | true | KSmoothing |
| v_input_3 | 3 | DLength |
| v_input_4 | 50 | Level |
| v_input_5 | 30 | Length_MA |
| v_input_6 | 14 | Length_DMI |
| v_input_7 | false | Trade reverse |

> Source (PineScript)

```pinescript
//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 15/10/2019
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market, if close price is lower than the previous close price 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Second strategy
// The related article is copyrighted material from Stocks & Commodities Aug 2009 
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
/////////////////////////
```