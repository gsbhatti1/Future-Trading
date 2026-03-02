> Name

Dual-Moving-Average-RSI-Indicator-Combination-Reversal-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a1891ae0ee82932bf0.png)
[trans]


## Overview

This strategy combines the use of dual moving averages, relative strength index (RSI), and parabolic SAR to identify price reversal points. It then makes buy and sell decisions based on these signals, belonging to a reversal trading strategy.

## Principles 

The strategy mainly uses the following technical indicators to determine price reversal points:

1. Dual Moving Average: Calculate fast moving average (MA fast line) and slow moving average (MA slow line). When the fast line crosses above the slow line, it indicates a bull market and goes long; when the fast line crosses below the slow line, it indicates a bear market and goes short.

2. RSI Indicator: RSI judges overbought and oversold conditions by calculating the average closing gain and average closing loss over a period of time. RSI above 70 indicates an overbought zone, while below 30 indicates an oversold zone.

3. PSAR Indicator: Parabolic SAR (SAR) helps in determining trend direction. SAR points below price indicate a bull market; above price indicate a bear market.

4. ADX Indicator: ADX measures the strength of trends by calculating directional movement. ADX above 20 signals a trending market, while below 20 indicates consolidation.

The logic for buy and sell signals is as follows:

- Buy Signal: Fast MA crosses above slow MA, RSI below 30 (oversold), SAR points above price, ADX above 20.
- Sell Signal: Fast MA crosses below slow MA, RSI above 70 (overbought), SAR points below price, ADX above 20.

When buy or sell signals occur, take a position with 10% of equity respectively. Close positions promptly when the reversal signal fails.

## Advantages

- Dual moving averages help determine major trend directions while RSI and PSAR filter out false signals to accurately identify reversal points.
- Combining multiple indicators reduces the risk of incorrect signals from a single indicator.
- Setting stop-loss conditions helps manage risks effectively.
- The strategy is simple and straightforward, making it easy to implement.
- It works for both uptrends and downtrends, providing strategies for different market scenarios.

## Risks and Solutions

- Dual moving averages may generate false breakouts. Consider using longer MA periods or adding Bollinger Bands to confirm true breakouts.
- RSI can produce wrong signals if improperly configured. Adjust RSI parameters and add other indicators to verify RSI signals.
- Suspend trading when ADX is below 20 to avoid reversal trading in directionless markets. Alternatively, shorten the ADX period.
- A poorly set stop loss may lead to unnecessary losses. Set a reasonable stop loss based on market volatility.
- High trading frequency can be mitigated by adjusting MA periods and lowering trade frequency.

## Optimization Directions

- Test different lengths of moving averages to find the best combination.
- Experiment with various RSI parameters for better overbought/oversold judgments.
- Integrate other indicators such as Bollinger Bands, KDJ to enhance signal determination logic.
- Set dynamic stop-loss mechanisms based on different products and markets.
- Implement position sizing strategies to better follow trends.
- Test different ADX parameters to find the optimal value that best determines trend strength.
- Add an auto-stop loss feature.

## Conclusion

This strategy identifies major trend directions using dual moving averages, while incorporating RSI and PSAR for additional signal filtering. After optimizing the parameters, it can effectively identify reversal points and capture trends around these reversals. In practice, managing risks through proper stop-loss settings and continuously optimizing parameters are crucial. Overall, this strategy uses a combination of indicators with clear logic and easy operation, making it a reliable reversal trading strategy.

||

## Overview

This strategy combines the use of dual moving averages, relative strength index (RSI), and parabolic SAR to identify price reversal points and make buy and sell decisions accordingly. It belongs to a reversal trading strategy.

## Principles 

The strategy mainly uses the following technical indicators to determine price reversal points:

1. Dual Moving Average: Calculate fast moving average (MA fast line) and slow moving average (MA slow line). When the fast line crosses above the slow line, it indicates a bull market and goes long; when the fast line crosses below the slow line, it indicates a bear market and goes short.

2. RSI Indicator: RSI judges overbought and oversold conditions by calculating the average closing gain and average closing loss over a period of time. RSI above 70 indicates an overbought zone, while below 30 indicates an oversold zone.

3. PSAR Indicator: Parabolic SAR (SAR) helps in determining trend direction. SAR points below price indicate a bull market; above price indicate a bear market.

4. ADX Indicator: ADX measures the strength of trends by calculating directional movement. ADX above 20 signals a trending market, while below 20 indicates consolidation.

The logic for buy and sell signals is as follows:

- Buy Signal: Fast MA crosses above slow MA, RSI below 30 (oversold), SAR points above price, ADX above 20.
- Sell Signal: Fast MA crosses below slow MA, RSI above 70 (overbought), SAR points below price, ADX above 20.

When buy or sell signals occur, take a position with 10% of equity respectively. Close positions promptly when the reversal signal fails.

## Advantages

- Dual moving averages help determine major trend directions while RSI and PSAR filter out false signals to accurately identify reversal points.
- Combining multiple indicators reduces the risk of incorrect signals from a single indicator.
- Setting stop-loss conditions helps manage risks effectively.
- The strategy is simple and straightforward, making it easy to implement.
- It works for both uptrends and downtrends, providing strategies for different market scenarios.

## Risks and Solutions

- Dual moving averages may generate false breakouts. Consider using longer MA periods or adding Bollinger Bands to confirm true breakouts.
- RSI can produce wrong signals if improperly configured. Adjust RSI parameters and add other indicators to verify RSI signals.
- Suspend trading when ADX is below 20 to avoid reversal trading in directionless markets. Alternatively, shorten the ADX period.
- A poorly set stop loss may lead to unnecessary losses. Set a reasonable stop loss based on market volatility.
- High trading frequency can be mitigated by adjusting MA periods and lowering trade frequency.

## Optimization Directions

- Test different lengths of moving averages to find the best combination.
- Experiment with various RSI parameters for better overbought/oversold judgments.
- Integrate other indicators such as Bollinger Bands, KDJ to enhance signal determination logic.
- Set dynamic stop-loss mechanisms based on different products and markets.
- Implement position sizing strategies to better follow trends.
- Test different ADX parameters to find the optimal value that best determines trend strength.
- Add an auto-stop loss feature.

## Conclusion

This strategy identifies major trend directions using dual moving averages, while incorporating RSI and PSAR for additional signal filtering. After optimizing the parameters, it can effectively identify reversal points and capture trends around these reversals. In practice, managing risks through proper stop-loss settings and continuously optimizing parameters are crucial. Overall, this strategy uses a combination of indicators with clear logic and easy operation, making it a reliable reversal trading strategy.

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|0.02|start|
|v_input_2|0.02|increment|
|v_input_3|0.2|max|
|v_input_4|30|ADX Smoothing|
|v_input_5|30|DI Length|
|v_input_6|50|length|
|v_input_7|0.5|Mult Factor|
|v_input_8|0.1|alertLevel|
|v_input_9|0.75|impulseLevel|
|v_input_10|false|showRange|

> Source (PineScript)

```pinescript
//@version=2
// Based on Senpai BO 3
strategy(title="Senpai_Strat_3", shorttitle="Senpai_Strat_3", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100)
src = close

// PSAR
start = input(0.02)
increment = input(0.02)
maximum = input(0.2)
psar = sar(start, increment, maximum)

// ADX Init
adxlen = input(30, title="ADX Smoothing")	
dilen = input(30, title="DI Length")	
dirmov(...