> Name

Dual-Signal-Trend-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/152c854182209303462.png)
[trans]

## Overview

This strategy combines dual EMA and Awesome Oscillator indicators to identify and track trends. EMA quickly judges short-term trend direction while Awesome Oscillator filters out false breakouts and provides entry timing. The strategy name "Dual Signal Trend Tracking Strategy" accurately summarizes its main functionality.

## Strategy Logic 

The strategy mainly utilizes two technical indicators, dual EMA and Awesome Oscillator, to filter signals with the following logic:

1. Calculate 2-period and 20-period EMA. When 2-period EMA breaks 20-period EMA upward, it signals an uptrend. When 2-period EMA breaks 20-period EMA downward, it signals a downtrend.

2. Calculate Awesome Oscillator, which is MACD histogram smoothed by fast EMA minus slow EMA. When AO histogram changes from red to blue, it is a buy signal. When it changes from blue to red, it is a sell signal.

3. Only when EMA shows uptrend and AO shows a buy signal at the same time, a final buy signal is generated. Only when EMA shows downtrend and AO shows a sell signal, a final sell signal is generated. 

4. Through this dual signal filtering mechanism, false breakouts can be reduced and mid-term trends can be tracked.

## Advantage Analysis

The advantages of this strategy are:

1. Dual line filtering reduces noisy trades caused by errors. EMA judges overall trend while AO filters entry timing. Combining the two improves signal reliability.

2. Extremely fast response sensitivity quickly captures short-term reversals. 2-period EMA is very sensitive to breakouts and can quickly determine if recent trends have changed.

3. Awesome Oscillator further filters MACD to effectively identify false breakouts in trends and avoid unnecessary reverse trades.

4. The strategy has a clear direction to track mid-term trends. EMA determines the basic trend while AO filters signals to ensure trading along overall trends.

5. Reasonable parameter selection. 2-period and 20-period EMA capture price changes over different timeframes. AO parameters 5 and 34 are optimized to identify short-term patterns.

## Risk Analysis

Some risks also exist:

1. In ranging markets, EMA and AO may generate more false signals, causing unnecessary short trades. Adjusting EMA period can reduce errors.

2. AO may sometimes lag EMA, causing signal time delays. AO parameters can be optimized for faster response.

3. EMA and AO combining short and mid-term features require quality data and computing power. Parameters should be adjusted for different products.

4. Frequent trading leads to higher commissions and slippage costs. Exit criteria can be relaxed to extend holding periods.

5. The strategy does not consider long-term trends and key support/resistance levels. More factors should be combined to ensure correct trade direction.

## Optimization Directions

The strategy can be optimized through several aspects:

1. Introduce trend indicators like moving average ribbons and ATR to assist EMA in determining overall trend.

2. Add key support/resistance detection like Fibonacci retracements, generating signals only around key levels to avoid bad entry positions.

3. Optimize EMA and AO parameter combinations to improve combo effects. For example, use genetic algorithms to find optimal parameter pairs.

4. Add stop loss exits. Exit when price breaks recent Swing High/Low to control single trade loss. 

5. Backtest on historical data to evaluate strategy performance, check if stable profitability meets expectations.

6. Paper trade to gradually adjust parameters and improve live performance. Test parameter robustness to find better stable parameter sets.

## Conclusion

The overall strategy idea is clear, combining EMA for overall trend and AO for signal filtering. It can effectively identify and track trends but also has some risks and limitations for further optimization and testing to improve stability. The key is choosing suitable products and parameters combined with proper trading principles and styles. Overall this strategy has sound logic and practical value.

||


## Strategy Arguments



|Argument|Default Value|Description|
|---|---|---|
|ema_fast_period|2|The period of the fast EMA used for trend identification.|
|ema_slow_period|20|The period of the slow EMA used for trend identification.|
|ao_short_period|5|The shorter period in the Awesome Oscillator calculation.|
|ao_long_period|34|The longer period in the Awesome Oscillator calculation.|


> Strategy Arguments



|Argument|Default Value|Description|
|---|---|---|
|ema_fast_period|2|The period of the fast EMA used for trend identification.|
|ema_slow_period|20|The period of the slow EMA used for trend identification.|
|ao_short_period|5|The shorter period in the Awesome Oscillator calculation.|
|ao_long_period|34|The longer period in the Awesome Oscillator calculation.|