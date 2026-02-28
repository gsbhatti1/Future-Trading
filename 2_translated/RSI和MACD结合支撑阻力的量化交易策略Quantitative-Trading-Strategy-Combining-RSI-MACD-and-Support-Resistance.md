> Name

RSI and MACD Combined with Support and Resistance Quantitative Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/12931d843ccc4cfa6d0.png)

[trans]

## Overview

This strategy is based on the RSI and MACD indicators, combined with support/resistance levels for trade signal judgment. Its name is "Panda Sticking Out Tongue" strategy. The strategy uses the RSI indicator to determine overbought/oversold levels, the MACD indicator to determine bullish/bearish trends, and draws support/resistance levels based on the highest and lowest prices over the past 100 periods, generating buy signals near support and sell signals near resistance. It belongs to a common trend-following strategy.

## Strategy Logic

The strategy mainly relies on two indicators - RSI and MACD. The RSI indicator judges overbought/oversold statuses, while the MACD indicator determines bullish/bearish trend statuses. It first calculates the 14-period RSI value, and sets the overbought threshold as 70 and oversold threshold as 30. Then it calculates the MACD value based on 12-day fast line, 26-day slow line, and 9-day signal line. RSI below 30 is considered oversold; RSI above 70 is considered overbought. MACD golden cross is the buy signal while death cross is the sell signal.

In addition, the strategy also calculates the highest and lowest prices over the past 100 periods as the support/resistance levels. When a buy signal is triggered, the price needs to be close to the support level, i.e., within 1% of the support level, to actually issue a buy order. Similarly when a sell signal is triggered, the price needs to be within 1% below the resistance level to actually issue a sell order.

## Advantages of the Strategy

The strategy combines trend analysis and overbought/oversold level detection to avoid false signals relying on single indicator only. By introducing support/resistance filter, it can reduce wrong trades due to rebounds near key S/R levels. The combination of MACD and RSI can accurately identify price movements and overbought/oversold statuses. Compared to simple Moving Average strategies, this strategy can capture long-term price trends more flexibly.

## Risks of the Strategy

The main risks of this strategy include:

1) It may miss most profits in strong trends, as it tends to enter after reversal finishes.
2) Inappropriate RSI and MACD parameter settings may cause wrong signals.
3) Simple S/R detection logic may overestimate or underestimate actual S/R zones.
4) Lack of stop loss mechanism. Unable to effectively control losses in extreme market conditions.

To address these risks, methods like adaptive MACD, optimized RSI parameters tuning, improved S/R identification, and market regime modeling can be used to improve the strategy.

## Directions for Enhancement

The strategy can be enhanced from the following dimensions:

1) Introduce stop loss mechanisms e.g. CANVAS stop loss
2) Use adaptive MACD for dynamic parameter tuning
3) Introduce price pattern recognition for more scientific S/R identification
4) Incorporate more data to establish market state detection logic for using different parameters adaptively
5) Use machine learning algorithms to optimize the strategy end-to-end

Through these improvements, we can further reduce drawdown and improve stability of the strategy.

## Conclusion

The strategy integrates RSI and MACD indicators to determine overbought/oversold statuses and trade around support/resistance levels. It represents a trend-following approach that incorporates support/resistance filter to reduce risk. The advantage lies in stable signals and controllable risk suitable for long-term holding. Still, some components such as indicator parameters, S/R range can be further tuned to improve profitability. Overall, it shows good performance in following market trends with easy implementation and risk control.

||

## Overview

This strategy is based on the RSI and MACD indicators, combined with support/resistance levels for trade signal judgment. Its name is "Panda Sticking Out Tongue" strategy. The strategy uses the RSI indicator to determine overbought/oversold levels, the MACD indicator to determine bullish/bearish trends, and draws support/resistance levels based on the highest and lowest prices over the past 100 periods, generating buy signals near support and sell signals near resistance. It belongs to a common trend-following strategy.

## Strategy Logic

The strategy mainly relies on two indicators - RSI and MACD. The RSI indicator judges overbought/oversold statuses, while the MACD indicator determines bullish/bearish trend statuses. It first calculates the 14-period RSI value, and sets the overbought threshold as 70 and oversold threshold as 30. Then it calculates the MACD value based on 12-day fast line, 26-day slow line, and 9-day signal line. RSI below 30 is considered oversold; RSI above 70 is considered overbought. MACD golden cross is the buy signal while death cross is the sell signal.

In addition, the strategy also calculates the highest and lowest prices over the past 100 periods as the support/resistance levels. When a buy signal is triggered, the price needs to be close to the support level, i.e., within 1% of the support level, to actually issue a buy order. Similarly when a sell signal is triggered, the price needs to be within 1% below the resistance level to actually issue a sell order.

## Advantages of the Strategy

The strategy combines trend analysis and overbought/oversold level detection to avoid false signals relying on single indicator only. By introducing support/resistance filter, it can reduce wrong trades due to rebounds near key S/R levels. The combination of MACD and RSI can accurately identify price movements and overbought/oversold statuses. Compared to simple Moving Average strategies, this strategy can capture long-term price trends more flexibly.

## Risks of the Strategy

The main risks of this strategy include:

1) It may miss most profits in strong trends, as it tends to enter after reversal finishes.
2) Inappropriate RSI and MACD parameter settings may cause wrong signals.
3) Simple S/R detection logic may overestimate or underestimate actual S/R zones.
4) Lack of stop loss mechanism. Unable to effectively control losses in extreme market conditions.

To address these risks, methods like adaptive MACD, optimized RSI parameters tuning, improved S/R identification, and market regime modeling can be used to improve the strategy.

## Directions for Enhancement

The strategy can be enhanced from the following dimensions:

1) Introduce stop loss mechanisms e.g. CANVAS stop loss
2) Use adaptive MACD for dynamic parameter tuning
3) Introduce price pattern recognition for more scientific S/R identification
4) Incorporate more data to establish market state detection logic for using different parameters adaptively
5) Use machine learning algorithms to optimize the strategy end-to-end

Through these improvements, we can further reduce drawdown and improve stability of the strategy.

## Conclusion

The strategy integrates RSI and MACD indicators to determine overbought/oversold statuses, and trade around support/resistance levels. It represents a trend-following approach that incorporates support/resistance filter to reduce risk. The advantage lies in stable signals and controllable risk suitable for long-term holding. Still, some components such as indicator parameters, S/R range can be further tuned to improve profitability. Overall, it shows good performance in following market trends with easy implementation and risk control.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|70|RSI Overbought Threshold|
|v_input_2|30|RSI Oversold Threshold|
|v_input_3|12|MACD Fast Length|
|v_input_4|26|MACD Slow Length|
|v_input_5|9|MACD Signal Smoothing|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-28 00:00:00
end: 2024-01-04 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI + MACD with Support and Resistance", shorttitle="RSI_MACD_SR", overlay=true)

// Input for RSI and MACD values
rsiOverbought = input(70, title="RSI Overbought Threshold")
rsiOversold = input(30, title="RSI Oversold Threshold")
macdFastLength = input(12, title="MACD Fast Length")
macdSlowLe