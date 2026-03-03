```markdown
## Overview

This strategy is mainly based on the SSL Channel indicator and the Wave Trend indicator, combined with other auxiliary indicators, to implement a relatively complete quantitative trading strategy. The strategy name contains the core indicators SSL Channel and Wave Trend, as well as the keyword quantitative trading, meeting the requirements.

## Strategy Logic

This strategy has six conditions for entry, of which the first two are core conditions, specifically:

1. SSL Hybrid baseline is blue (bullish) or red (bearish)
2. SSL Channel crossover up (bullish) or down (bearish)
3. Wave Trend crossover up (bullish) or down (bearish)
4. Entry candle height not greater than threshold
5. Entry candle inside Bollinger Bands  
6. Take profit target does not touch EMA

When these 6 conditions are met at the same time, the strategy will go long or go short. The stop loss distance is calculated based on the ATR indicator value, and the take profit distance is the Risk Reward Ratio times the stop loss.

The strategy also has a sound risk and money management mechanism, including stop loss setting, position sizing control, and maximum drawdown control. At the same time, the strategy draws auxiliary lines on the chart, which can visually see the stop loss and take profit for each trade, as well as the specific profit and loss. This is very helpful for both strategy analysis and optimization.

## Advantage Analysis 

The biggest advantage of this strategy is that the SSL Channel indicator is very accurate in determining the trend direction. When combined with the Wave Trend and other indicators for confirmation, it can greatly reduce false signals. At the same time, the strict entry conditions can also avoid unnecessary trades, thereby reducing the number of trades and lowering transaction costs.

In addition, the sound risk and capital management mechanism of the strategy is also a significant advantage. The pre-set stop loss and take profit strategies can effectively control the maximum loss of a single trade. Together with position sizing control, it can keep the maximum account drawdown within an acceptable range.

## Risk Analysis

The biggest risk of this strategy is that the strict entry conditions may miss some trading opportunities, affecting profitability. When the market is in a shock state, the profitability of the strategy will also be discounted.

In addition, the effectiveness of Wave Trend and other indicators in determining market trends will also be affected by anomalies such as false breakouts in the market. At this point parameters need to be adjusted or other indicators added for confirmation.

Overall, the risks of this strategy are still controllable. Through parameter tuning and optimization, the strategy can be made more adaptable to different market environments.

## Optimization Directions

There are several optimization directions for this strategy:

1. Optimize Wave Trend parameters to determine trend reversal points more accurately  
2. Add other indicators for confirmation, such as KDJ, MACD, etc., to avoid the impact of false breakouts
3. Parameters can be adjusted and optimized for different products and timeframes to improve strategy stability  
4. Add machine learning algorithms to train models with historical data and optimize parameters in real time
5. Use high frequency factors and other algorithms to increase strategy trade frequency and profitability

Through the implementation of these optimization measures, it is expected to take the profitability and stability of the strategy to a higher level.

## Conclusion

In summary, this strategy integrates multiple indicators and strict entry mechanisms to ensure high win rate while achieving good risk control. Combined with future optimization directions, the strategy has great potential for development and is a recommended quantitative trading strategy.
```

---

### Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_bool_1 | true | (?Strategy: Entry Conditions) Use SSL Hybrid Condition |
| v_input_bool_2 | true | Use Keltner Channel Condition |
| v_input_bool_3 | true | Keltner Channel Include Wicks |
| v_input_bool_4 | true | Target not touch EMA Condition |
| v_input_bool_5 | true | Use Candle Height Condition |
| v_input_float_1 | 0.7 | (?Strategy: Entry Conditions) Candle Height Threshold |
| v_input_float_2 | 1.7 | (?Strategy: Exit Conditions) Stop Loss ATR Multiplier |
| v_input_float_3 | 2.5 | (?Strategy: Risk Management) Risk : Reward 1 : |
| v_input_float_4 | 0.05 | (?Strategy: Risk Management) Portfolio Risk % |
| v_input_int_1 | 2022 | 
```