> Name

DMI and Moving Average Combination Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy integrates the 123 Reversal Strategy, DMI (Directional Movement Index) Strategy, and Moving Average Strategy to form a robust combined approach. It enables reverse operations at trend reversal points while following trends when they continue. Additionally, it uses moving averages for filtering purposes, helping to effectively identify market trend directions and improve the strategy's win rate.

## Strategy Logic

1. **123 Reversal Strategy**: Go long when the close price is higher than the previous day’s close for two consecutive days, and the 9-day slow K line is below 50; go short when the close price is lower than the previous day’s close for two consecutive days, and the 9-day fast K line is above 50.

2. **DMI Strategy**: Go long when the +DI (Positive Directional Indicator) crosses above the -DI (Negative Directional Indicator); go short when the -DI crosses below the +DI.

3. **Moving Average Strategy**: Go long when the close price crosses above the MA (Moving Average); go short when the close price crosses below the MA.

4. Open positions only when all three strategies give consistent signals; otherwise, close positions.

This strategy combines trend and reversal strategies to capture both reversal opportunities and trend-following opportunities promptly. The moving average filter can reduce false signals. Multiple strategies verify each other, enhancing signal reliability.

## Advantage Analysis

1. Combining multiple strategies increases the win rate. 123 Reversal captures turning points, DMI captures trends, and Moving Average filters out signals.

2. Integrating reversal and trend strategies allows for flexible trading by capturing both reversals and trends.

3. The moving average filter reduces false signals due to short-term fluctuations.

4. Combining multiple strategies verifies signals and avoids the failure of a single strategy due to specific market conditions.

5. Multiple parameters allow for optimization to find the best parameter combination, enhancing the strategy's stability.

## Risk Analysis

1. Reversal strategies can get trapped in range-bound trends. Combining with trend strategies helps avoid this risk.

2. DMI might miss early trend opportunities; shorter DMI parameters can be used to improve sensitivity.

3. Moving averages have a lag effect and may delay signal generation; shortening the MA period can speed up reaction times.

4. While combining multiple strategies improves win rates, it also increases complexity. Careful testing of each parameter is necessary.

5. The strategy is sensitive to transaction costs; consider relaxing stop loss ranges to avoid frequent open-close trades.

## Optimization Directions

1. Optimize parameters for each strategy to find the best combination.

2. Add other indicators like MACD and RSI to filter signals and improve stability.

3. Implement stop loss strategies such as trailing stops to control risks.

4. Optimize position sizing, using fixed or dynamic sizing to enhance returns.

5. Adjust parameters for specific products to improve adaptability.

6. Integrate machine learning models to assist decision-making and utilize more historical data to boost performance.

## Conclusion

This strategy forms a flexible combination system by effectively integrating the 123 Reversal Strategy, DMI Strategy, and Moving Average Filter. It can capture both reversal and trend-following opportunities, enhancing signal reliability through multiple strategies. There is still room for improvement in parameter tuning, stop loss settings, position sizing, etc. With proficient application, this practical and expandable strategy can generate considerable profits in live trading.

||

## Overview

This strategy combines the 123 Reversal Strategy, DMI Strategy, and Moving Average Strategy to form an effective combination approach. It enables reverse operations at trend reversal points while following trends when they continue. The moving average filter helps identify market trend directions effectively and improves the win rate of the strategy.

## Strategy Logic

1. **123 Reversal Strategy**: Go long when close price is higher than previous day’s close for two consecutive days, and 9-day slow K line is below 50; go short when close price is lower than previous day's close for two consecutive days, and 9-day fast K line is above 50.

2. **DMI Strategy**: Go long when +DI crosses above -DI; go short when -DI crosses below +DI.

3. **Moving Average Strategy**: Go long when close price crosses above MA; go short when close price crosses below MA.

4. Open positions only if all three strategies give consistent signals, otherwise close positions.

The strategy combines trend and reversal strategies to capture both reversal opportunities and trend-following opportunities promptly. The moving average filter can reduce false signals. Multiple strategies verify each other and improve signal reliability.

## Advantage Analysis

1. Combining multiple strategies increases the win rate. 123 Reversal Strategy for catching turning points, DMI for catching trends, and Moving Average for filtering signals.
   
2. Integrating reversal and trend strategies enables flexible trading by capturing both reversals and trends.

3. The moving average filter reduces false signals due to short-term fluctuations.

4. Combining multiple strategies verifies signals and avoids the failure of a single strategy due to specific market conditions.

5. Multiple parameters allow for optimization to find the best parameter combination, enhancing the stability of the strategy.

## Risk Analysis

1. Reversal strategies can get trapped in range-bound trends; combining with trend strategies helps avoid this risk.

2. DMI might miss early trend opportunities; shorter DMI parameters can be used to improve sensitivity.

3. Moving averages have a lag effect and may delay signal generation; shortening the MA period can speed up reaction times.

4. While combining multiple strategies improves win rates, it also increases complexity. Careful testing of each parameter is necessary.

5. The strategy is sensitive to transaction costs; consider relaxing stop loss ranges to avoid frequent open-close trades.

## Optimization Directions

1. Optimize parameters for each strategy to find the best combination.
2. Add other indicators like MACD and RSI to filter signals and improve stability.
3. Implement stop loss strategies such as trailing stops to control risks.
4. Optimize position sizing, using fixed or dynamic sizing to enhance returns.
5. Adjust parameters for specific products to improve adaptability.
6. Integrate machine learning models to assist decision-making and utilize more historical data to boost performance.

## Conclusion

This strategy forms a flexible combination system by effectively integrating the 123 Reversal Strategy, DMI Strategy, and Moving Average Filter. It can capture both reversal and trend-following opportunities, enhancing signal reliability through multiple strategies. There is still room for improvement in parameter tuning, stop loss settings, position sizing, etc. With proficient application, this practical and expandable strategy can generate considerable profits in live trading.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|30|Length_MA|
|v_input_6|14|Length_DMI|
|v_input_7|false|Trade reverse|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-11 00:00:00
end: 2023-09-18 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

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