> Name

CMARSI Trading Strategy CMARSI-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

The CMARSI trading strategy is a trend-following approach that integrates the RSI indicator with moving averages. It employs an improved RSI, known as Connors RSI, to identify trends and uses moving averages as signals for entry and exit. Suitable for medium-to-long term trading, this strategy aims to profit by following established trends.

## Principle Analysis

The CMARSI strategy utilizes a modified RSI indicator called Connors RSI. This combines classic RSI, RSI Up/Down lines, and the Rate of Change (ROC) percentile. The formula is as follows:

Connors RSI = (RSI + RSI Up/Down + ROC Percentile) / 3

Where RSI uses a 3-day period, RSI Up/Down uses a 2-day period, and the ROC percentile uses a 100-day period.

The key advantage of Connors RSI is its ability to incorporate multiple indicators for more accurate trend identification. A cross above 40 indicates a bullish signal, while a cross below 70 signals bearishness.

CMARSI builds upon this by introducing a moving average factor. It calculates a 2-day moving average and uses crossovers of Connors RSI with the MA as trading signals. The specific rules are:

1. Enter long when Connors RSI crosses above 40 and forms a golden cross with the 2-day MA.
2. Exit when Connors RSI falls below 70 and forms a death cross with the 2-day MA.

Using the moving average filter helps reduce false signals from Connors RSI, thereby enhancing strategy stability.

## Advantage Analysis

The primary advantage of the CMARSI strategy lies in its combination of multiple indicators for trend identification. Specifically:

1. Connors RSI is more stable compared to traditional RSI for identifying trend reversal points.
2. The introduction of moving averages helps filter out noise and prevent overbuying or overselling.
3. Combining multiple indicators improves the win rate by following trends.
4. Simple and clear trading rules are easy to implement.
5. As a trend-following strategy, it effectively captures medium-to-long term trends.

## Risk Analysis

The main risks associated with the CMARSI strategy include incorrect trend judgment and inappropriate stop-loss placement:

1. Connors RSI may give false signals leading to unnecessary entries. Parameter adjustments or additional indicator confirmations can mitigate this.
2. Improper stop-loss settings might result in premature exits or overly large stop losses. Stop loss parameters should be optimized for specific products and market environments.
3. Moving averages may perform poorly during range-bound markets, requiring parameter optimization.
4. Long-term use could lead to overfitting. Regular backtesting and adaptive parameter tuning based on market conditions are necessary.

## Optimization Directions

The CMARSI strategy can be enhanced through the following improvements:

1. Optimize Connors RSI parameters for different time frames and asset classes.
2. Experiment with various types of moving averages to further refine signal filtering.
3. Incorporate additional indicators such as MACD or Bollinger Bands for trade confirmation.
4. Improve stop-loss strategies, including trailing stops or stepped stop losses.
5. Select suitable assets through screening to better fit the strategy.
6. Employ Walk Forward Analysis to regularly optimize parameters and avoid overfitting.

## Conclusion

The CMARSI trading strategy combines Connors RSI with moving averages for trend-following in medium-to-long term trades. This approach is stable, straightforward to implement, and effectively tracks trends for profit generation. Continuous optimization based on market conditions, along with risk management, will likely result in favorable returns. Overall, CMARSI represents a recommended trend trading strategy.

||


## Overview

The CMARSI trading strategy is a trend-following approach that integrates the RSI indicator with moving averages. It uses an improved RSI, known as Connors RSI, to identify trends and moving averages as signals for entry and exit. Suitable for medium-to-long term trading, this strategy aims to profit by following established trends.

## Principle Analysis

The CMARSI strategy employs a modified RSI called Connors RSI that combines classic RSI, RSI Up/Down lines, and the Rate of Change (ROC) percentile. The formula is:

Connors RSI = (RSI + RSI Up/Down + ROC Percentile) / 3

Where RSI uses a 3-day period, RSI Up/Down uses a 2-day period, and the ROC percentile uses a 100-day period.

The advantage of Connors RSI is its ability to combine multiple indicators for more accurate trend identification. A crossing above 40 indicates a bullish signal, while below 70 signals bearishness.

CMARSI further introduces a moving average factor by calculating a 2-day moving average and using crossovers between Connors RSI and the MA as trading signals. The specific rules are:

1. Enter long when Connors RSI crosses above 40 and forms a golden cross with the 2-day MA.
2. Exit when Connors RSI falls below 70 and forms a death cross with the 2-day MA.

The moving average filter helps reduce false signals from Connors RSI, improving strategy stability.

## Advantage Analysis

The primary advantage of the CMARSI strategy lies in its combination of multiple indicators for trend identification. Specifically:

1. Connors RSI is more stable than traditional RSI for identifying trend reversal points.
2. The introduction of moving averages helps filter out noise and prevent overbuying or overselling.
3. Combining multiple indicators improves the win rate by following trends.
4. Simple and clear trading rules are easy to implement.
5. As a trend-following strategy, it effectively captures medium-to-long term trends.

## Risk Analysis

The main risks associated with the CMARSI strategy include incorrect trend judgment and inappropriate stop-loss placement:

1. Connors RSI may give false signals leading to unnecessary entries. Parameter adjustments or additional indicator confirmations can mitigate this.
2. Improper stop-loss settings might result in premature exits or overly large stop losses. Stop loss parameters should be optimized for specific products and market environments.
3. Moving averages may perform poorly during range-bound markets, requiring parameter optimization.
4. Long-term use could lead to overfitting. Regular backtesting and adaptive parameter tuning based on market conditions are necessary.

## Optimization Directions

The CMARSI strategy can be enhanced through the following improvements:

1. Optimize Connors RSI parameters for different time frames and asset classes.
2. Experiment with various types of moving averages to further refine signal filtering.
3. Incorporate additional indicators like MACD or Bollinger Bands for trade confirmation.
4. Improve stop-loss strategies, including trailing stops or stepped stop losses.
5. Select suitable assets through screening to better fit the strategy.
6. Employ Walk Forward Analysis to regularly optimize parameters and avoid overfitting.

## Conclusion

The CMARSI trading strategy combines Connors RSI with moving averages for trend-following in medium-to-long term trades. This approach is stable, straightforward to implement, and effectively tracks trends for profit generation. Continuous optimization based on market conditions, along with risk management, will likely result in favorable returns. Overall, CMARSI represents a recommended trend trading strategy.

||


## Source (PineScript)

```pinescript
/*backtest
start: 2022-09-19 00:00:00
end: 2023-09-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
src = close, lenrsi = 3, lenupdown = 2, lenroc = 100, malengt = 2, low = 40, high = 70, a = 1
updown(s) =>
    isEqual = s == s[1]
    isGrowing = s > s[1]
    ud = 0.0
    ud := isEqual ? 0 : isGrowing ? (nz(ud[1]) <= 0 ? 1 : nz(ud[1])+1) : (nz(ud[1]) >= 0 ? -1 : nz(ud[1])-1)
    ud
rsi = rsi(src, lenrsi)
updownrsi = rsi(updown(src), lenupdown)
percentrank = percentrank(roc(src, 1), lenroc)
crsi = avg(rsi, updownrsi, percentrank)
MA = sma(crsi, malengt)

band1 = 70
band0 = 40
```