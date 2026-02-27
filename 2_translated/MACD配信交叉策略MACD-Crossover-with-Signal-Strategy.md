> Name

MACD Crossover with Signal Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/18ef70b95608e5f3d6f.png)
[trans]

## Overview

The MACD Crossover with Signal strategy generates trading signals when the MACD crosses above or below the signal line. The strategy combines the idea of double moving averages to capture the turning points of medium-term trends in stock prices, belonging to a typical trailing stop loss strategy.

## Strategy Principle

The strategy first calculates the fast moving average line `fastMA` and the slow moving average line `slowMA`. The fast moving average parameter is 12 days, and the slow moving average parameter is 26 days. Then it calculates the difference between the two moving average lines to form the MACD. Then a 9-day moving average of the MACD is calculated to get the signal line. Trading signals are generated when the MACD crosses above or below the signal line.

The advantage of the strategy is to capture the turning point of the medium-term trend of stock prices. The combination of fast and slow moving averages filters out short-term price fluctuations and noise, and can capture medium-term price trends. When the stock price undergoes a medium-term reversal, the MACD will break through the signal line and generate relatively clear trading signals.

## Advantage Analysis

The MACD Crossover with Signal strategy combines the idea of double moving averages to filter out short-term noise and only capture the turning points of long and medium-term trends. Compared with a single price indicator, it can generate fewer false signals.

MACD itself is more sensitive and can respond sensitively to price trend changes. The addition of the signal line can filter out more short-term false signals. Only when the medium-term trend changes significantly, the MACD breaks through the signal line up and down, will a signal be generated.

In a sustainable uptrend, the MACD maintains above the signal line most of the time, which can capture multiple opportunities along the way. Similarly, in a sustained downtrend, the MACD can also maintain a long/short pattern and give short signals in a timely manner.

## Risk Analysis

Since the strategy buy and sell signals rely entirely on the crossover of the moving averages, if the market fluctuates greatly, more false signals will be generated, resulting in frequent stop loss. The actual profit and loss of the strategy may not meet expectations.

Breaking through the signal line does not necessarily ensure that the medium-term trend has changed. Relying solely on a single technical indicator as a buy signal has a certain blindness, and the timing may not be accurate enough.

In the ever-changing market, using the crossover of double moving averages alone as the threshold may miss more trading opportunities. In more complex strong trends, this strategy will also lag significantly.

## Optimization Directions

1. Add liquidity and volatility filtering indicators to reduce opening frequency and avoid ineffective trading. Such as adding trading volume, dynamically adjusting moving average parameters, etc.
2. Combine multiple other technical indicators to form an indicator portfolio to improve signal quality. The combination of short-term and medium and long-term indicators can more comprehensively judge the market structure.
3. Add machine learning algorithms to train parameters and attention thresholds that are more suitable for the current market environment, reducing human intervention.
4. Combine VIX and other fear indices to predict market trends and volatility, and dynamically adjust parameters to better take advantage of MACD opportunities.

## Conclusion

The MACD Crossover with Signal strategy uses the principle of double moving average crossover to generate trading signals. Drawing the price graph by the difference between fast and slow moving averages, medium-term price trend changes will have obvious characteristics. The addition of the signal line also effectively filters out some noisy signals. The strategy has some advantages in capturing relatively clear medium-term trend reversals. However, the crossover of MACD and signal line cannot fully determine the fundamental change in market structure, and trading signals need to be treated with caution. It is recommended to use in combination with other technical indicators, and machine learning optimization can also be considered.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Use Current Chart Resolution?|
|v_input_2|60|Use Different Timeframe? Uncheck Box Above|
|v_input_3|true|Show MacD & Signal Line? Also Turn Off Dots Be