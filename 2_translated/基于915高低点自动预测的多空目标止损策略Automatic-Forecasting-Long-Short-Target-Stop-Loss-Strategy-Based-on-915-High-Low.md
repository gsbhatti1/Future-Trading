## Overview

This strategy automatically calculates long and short target prices and stop loss levels based on the high and low of the 9:15 minute candle. It uses the RSI indicator to determine the current overbought or oversold state of the market and triggers a long or short entry when the price breaks the 9:15 high/low and the RSI condition is met. The strategy simplifies the trading process by automatically predicting target prices and stop loss levels for long and short directions.

## Strategy Principle

1. Determine the high and low of the 9:15 minute candle as key levels for long and short directions.
2. Long direction: target price is 9:15 high + 200 points, stop loss is 9:15 low.
3. Short direction: target price is 9:15 low - 200 points, stop loss is 9:15 high.
4. Calculate the RSI indicator with default parameters of 14, overbought line at 60, and oversold line at 40.
5. Long entry condition: close price breaks above 9:15 high and RSI is greater than the overbought line.
6. Short entry condition: close price breaks below 9:15 low and RSI is less than the oversold line.
7. Execute the corresponding long or short entry when the entry conditions are met.
8. Plot the 9:15 high/low, long/short target prices, stop loss levels, and entry signals on the chart.

The strategy utilizes the high and low of the 9:15 minute candle as key levels and automatically calculates the target prices and stop losses for long and short directions, simplifying the trader's operation. Additionally, it introduces the RSI indicator as a filter condition, which can help avoid frequent entries and false breakouts to a certain extent.

## Advantage Analysis

1. Automatic calculation of long/short targets and stop losses: The strategy automatically calculates the target prices and stop loss levels for long and short directions based on the 9:15 high/low. Traders do not need to set them manually, simplifying the operation process and improving trading efficiency.

2. RSI indicator filter: The strategy introduces the RSI indicator as a filter condition for entry. When the price breaks a key level, the RSI needs to reach the overbought or oversold state to trigger an entry signal. This can help traders avoid frequent trading and false breakout traps to a certain extent.

3. Intuitive chart display: The strategy plots the 9:15 high/low, long/short target prices, stop loss levels, and entry signals on the chart. Traders can intuitively see the key levels and trading signals, facilitating their decision-making.

4. Suitable for short-term trading: The strategy is based on the high and low of the 9:15 minute candle, and the target prices and stop losses are set relatively close. Therefore, it is more suitable for short-term trading operations, allowing for quick entries and exits to capture short-term price movements.

## Risk Analysis

1. Intraday volatility risk: The strategy uses the 9:15 high/low as key levels, but prices may experience significant fluctuations during the trading day. If the price quickly reverses after triggering an entry, it may cause the trader's loss to exceed expectations.
2. Stop loss level risk: The stop loss levels in the strategy are fixed, with the long stop loss at the 9:15 low and the short stop loss at the 9:15 high. If the price continues to move significantly after breaking the 9:15 high/low, the fixed stop loss levels may result in larger losses.
3. RSI indicator parameter risk: The strategy uses default RSI parameters, with a length of 14, overbought line at 60, and oversold line at 40. However, these parameters may not be suitable for different market environments and instruments. Fixed parameters can affect the effectiveness of the strategy.
4. Profit/Loss ratio risk: The fixed target prices and stop losses in the strategy determine the profit/loss ratio of each trade. If the ratio is set improperly, it may result in poor long-term profitability.

### Solutions:
1. For intraday volatility risk, consider adding more filter conditions such as volume indicators or narrowing the stop loss range.
2. To address fixed stop loss risks, consider using trailing stops or conditional stops to adjust the position based on market conditions.
3. To mitigate RSI indicator parameter risks, optimize parameters for different markets and instruments by testing historical data to find a better combination of parameters.
4. For profit/loss ratio optimization, test various target price and stop loss combinations using historical data to identify settings that provide higher returns.

## Optimization Directions

1. Dynamic Stop Loss: Currently, the strategy uses fixed stop losses; consider implementing dynamic stop loss mechanisms such as trailing or conditional stops to manage risk more effectively during unexpected volatility.
2. Add More Filter Conditions: The current strategy primarily relies on price breaks and RSI indicators; consider incorporating additional filter conditions like volume and volatility indicators to enhance entry signal effectiveness through multiple confirmations.
3. Parameter Optimization: Optimize the RSI indicator parameters for different markets and instruments by testing historical data to find more suitable combinations that improve the stability of the strategy.
4. Profit/Loss Ratio Optimization: The profit/loss ratio is critical for long-term profitability; test various target price and stop loss combinations using backtesting with historical data to find settings that generate higher returns.
5. Incorporate Trend Judgments: This strategy currently relies on breaking 9:15 highs/lows, which is counter-trend trading. Consider incorporating trend analysis to trade in the direction of larger trends, thereby improving win rate and profit/loss ratio.

## Conclusion

This strategy utilizes the high and low of the 9:15 minute candle as key levels to automatically calculate long and short target prices and stop loss levels while using the RSI indicator as a filter condition. It simplifies traders' operations by providing automated predictions for targets and stops, making it suitable for short-term trading. However, this strategy also faces risks such as intraday volatility, fixed stop losses, RSI parameter settings, and profit/loss ratio issues. To address these challenges, improvements can be made through dynamic stop loss mechanisms, incorporating more filter conditions, optimizing parameters, refining the profit/loss ratio, and adding trend analysis.

The continuous optimization and improvement of this strategy will enhance its stability and profitability, better adapting it to various market environments.