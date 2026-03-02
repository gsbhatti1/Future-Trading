> Name

TAM Intraday RSI Trading Strategy TAM-Intraday-RSI-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1afaea96d4e98dfbfd9.png)

[trans]

## Overview

The TAM Intraday RSI trading strategy utilizes the crossover of RSI indicators across different periods to generate intraday entry and exit signals. The strategy performs well in both bull and bear environments by effectively capitalizing on overbought and oversold conditions revealed by the RSI indicator and making counter-trend trades when the market shows signs of reversal.

## Strategy Logic

The strategy employs two RSI indicators to generate buy and sell signals. The buy signal uses a short period 2-day RSI and a medium period 14-day RSI, triggering a buy when either the short or medium RSI crosses above 50. The sell signal uses a short period 7-day RSI and a medium period 50-day RSI, triggering a sell when either the short or medium RSI crosses below 50.

The strategy also requires the RSI to actually move past the 50 threshold, not just cross it, which helps filter out many false signals. Specifically, a buy requires meeting the following conditions:
- 2-day RSI crosses above 50
- 2-day RSI is greater than 50
- 14-day RSI crosses above 50
- 14-day RSI is greater than 50

The sell conditions are similar:
- 7-day RSI crosses below 50
- 7-day RSI is less than 50
- 50-day RSI crosses below 50 
- 50-day RSI is less than 50

Such multi-layer filtering ensures signals are only triggered when RSI shows clear overbought/oversold indications, and will not be misled by minor oscillations.

## Advantage Analysis 

The TAM Intraday RSI strategy has the following advantages:

1. Utilizing dual RSI provides multi-timeframe analysis, effectively filtering market noise and entering at significant trend reversal points.
2. Requiring actual RSI value to breach key threshold avoids false breakout signals.
3. Adopting RSI of differing parameters for entry and exit can pinpoint reversal timing more precisely.
4. RSI exhibits relatively stable performance within intraday trading windows, suitable for intraday strategies.
5. Customizable parameters allow adjusting RSI inputs for different markets and better results.
6. Simple and clear logic makes it easy to understand and implement for algo trading.

## Risk Analysis

Some risks also exist with the strategy:

1. Intraday trading has overnight gap risk that can skip stop loss settings.
2. RSI divergence occurs frequently and must be validated with other indicators.
3. High volatility in intraday periods means stop loss must be wide yet not too wide.
4. Parameter optimization risks overfitting, requiring testing across varying markets.
5. Backtesting limitations cannot fully reflect real trading, requiring tuning for live performance.

## Optimization Directions

The strategy can be improved in the following aspects:

1. Add confirmation with other indicators like KDJ, MACD etc.
2. Implement volume filter to only consider signals on increasing volume.
3. Optimize parameters for even shorter intraday cycles.
4. Assist decision with machine learning models to find optimal parameters algorithmically.
5. Artistic touch combining key S/R levels, chart patterns from technical analysis.
6. Improve stop loss with dynamic ATR, volatility based methods.

## Conclusion

Overall, the TAM Intraday RSI strategy is a very practical quant strategy. It effectively assesses overbought and oversold conditions using the multi-timeframe RSI evaluation and generates solid signals when combined with strict entry/exit rules to filter out false signals. With proper optimization and risk management, the strategy can produce stable trade signals and achieve good results. Its clear and straightforward logic makes it easy to implement and test for algo traders.

|||

## Overview

The TAM intraday RSI trading strategy utilizes the crossover of RSI indicators across different periods to generate intraday entry and exit signals. The strategy performs well in both bull and bear environments by effectively capitalizing on overbought and oversold conditions revealed by the RSI indicator and making counter-trend trades when the market shows signs of reversal.

## Strategy Logic

The strategy employs two RSI indicators to generate buy and sell signals. The buy signal uses a short period 2-day RSI and a medium period 14-day RSI, triggering a buy when either the short or medium RSI crosses above 50. The sell signal uses a short period 7-day RSI and a medium period 50-day RSI, triggering a sell when either the short or medium RSI crosses below 50.

The strategy also requires the RSI to actually move past the 50 threshold, not just cross it, which helps filter out many false signals. Specifically, a buy requires meeting the following conditions:
- 2-day RSI crosses above 50
- 2-day RSI is greater than 50
- 14-day RSI crosses above 50
- 14-day RSI is greater than 50

The sell conditions are similar:
- 7-day RSI crosses below 50
- 7-day RSI is less than 50
- 50-day RSI crosses below 50 
- 50-day RSI is less than 50

Such multi-layer filtering ensures signals are only triggered when RSI shows clear overbought/oversold indications, and will not be misled by minor oscillations.

## Advantage Analysis 

The TAM intraday RSI strategy has the following advantages:

1. Utilizing dual RSI provides multi-timeframe analysis, effectively filtering market noise and entering at significant trend reversal points.
2. Requiring actual RSI value to breach key threshold avoids false breakout signals.
3. Adopting RSI of differing parameters for entry and exit can pinpoint reversal timing more precisely.
4. RSI exhibits relatively stable performance within intraday trading windows, suitable for intraday strategies.
5. Customizable parameters allow adjusting RSI inputs for different markets and better results.
6. Simple and clear logic makes it easy to understand and implement for algo trading.

## Risk Analysis

Some risks also exist with the strategy:

1. Intraday trading has overnight gap risk that can skip stop loss settings.
2. RSI divergence occurs frequently and must be validated with other indicators.
3. High volatility in intraday periods means stop loss must be wide yet not too wide.
4. Parameter optimization risks overfitting, requiring testing across varying markets.
5. Backtesting limitations cannot fully reflect real trading, requiring tuning for live performance.

## Optimization Directions

The strategy can be improved in the following aspects:

1. Add confirmation with other indicators like KDJ, MACD etc.
2. Implement volume filter to only consider signals on increasing volume.
3. Optimize parameters for even shorter intraday cycles.
4. Assist decision with machine learning models to find optimal parameters algorithmically.
5. Artistic touch combining key S/R levels, chart patterns from technical analysis.
6. Improve stop loss with dynamic ATR, volatility based methods.

## Conclusion

Overall, the TAM intraday RSI strategy is a very practical quant strategy. It effectively assesses overbought and oversold conditions using the multi-timeframe RSI evaluation and generates solid signals when combined with strict entry/exit rules to filter out false signals. With proper optimization and risk management, the strategy can produce stable trade signals and achieve good results. Its clear and straightforward logic makes it easy to implement and test for algo traders.

|||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|true|(?Backtest Time Period)Filter Date Range of Backtest|
|v_input_1|timestamp(2020-01-01)|Start date|
|v_input_2|2|(?Buy configuration)RSI Buy Length 1 (default 2)|
|v_input_3|14|RSI Buy Length 2 (default 14)|
|v_input_4|50|RSI Buy Value Signal (default 50)|
|v_input_5|7|(?Close configuration)RSI Close Length 1 (default 7)|
|v_input_6|50|RSI Close Length 2 (default 50)|
|v_input_7|50|RSI Close Value Signal (default 50)|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-16 00:00:00
end: 2023-10-16 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2