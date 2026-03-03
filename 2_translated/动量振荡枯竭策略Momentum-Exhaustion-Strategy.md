> Name

Momentum Exhaustion Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/17c5d7f10e1296264f7.png)
[trans]


## Overview

The Momentum Exhaustion Strategy is a trend following strategy that utilizes moving averages and price percentage oscillators to minimize downside exposure. It belongs to index fund trading models and can effectively control risks.

## Strategy Logic

The core indicators of this strategy are Exhaustion and Exhaustion Moving Average. Exhaustion is a measure of price oscillation, calculated from close, high, and low prices. The specific calculation is: \((\text{close} + \text{high} + \text{low} - \text{Exhaustion's moving average}) / \text{Exhaustion's moving average}\). The Exhaustion Moving Average is the moving average of Exhaustion. When Exhaustion crosses above Exhaustion Moving Average, it indicates consolidation in the market and a possible new trend forming. When Exhaustion crosses below Exhaustion Moving Average, it signals a trend reversal, and we should consider taking profit.

In addition, the strategy also uses long and short-term moving averages to assist in determining the trend, including 300-day, 150-day, and 50-day lines. When the short-term moving average crosses below the long-term moving average, it signals a trend reversal, and we should consider stopping loss.

MACD is also used for short-term buy and sell signals. When MACD line crosses above the signal line, it indicates a bullish signal, and when MACD crosses below the signal line, it indicates a bearish signal. RSI bottoms are also used as buy signals.

The specific entry and exit logic is:

Buy signal: Exhaustion crossing above Exhaustion Moving Average, and 50-day MA above 150-day MA; or RSI below 30.

Short-term stop loss: Exhaustion crossing below Exhaustion Moving Average; or MACD crossing below signal line.

Mid-long term stop loss: 50-day MA crossing below 150-day MA; or 150-day MA crossing below 300-day MA.

## Advantages of the Strategy

This strategy combines multiple indicators to determine the trend exhaustion and control risks. The advantages are:

1. The Exhaustion indicator can effectively identify consolidation and reversal. Timely detecting trend reversal is key to controlling risks.
2. Using moving averages of multiple timeframes to determine the trend avoids being misled by short-term market noise.
3. MACD helps confirm buy and sell signals, improving the strategy's performance.
4. RSI plays its role of buying low and selling high, buying at extremely oversold situations.
5. The clear profit taking and stop loss strategy can effectively control the risk of each trade.

## Risks of the Strategy

There are also some risks with this strategy:

1. Relying on multiple indicators, improper parameter settings may lead to wrong trading signals. Parameters need to be repeatedly tested and optimized.
2. The Exhaustion indicator is not completely reliable, it may fail when there is price divergence.
3. Improper stop loss placement may result in being stopped out by short-term fluctuations. Stop loss should balance long and short term effects.
4. When the overall market is ranging, the indicators may fail. Position sizing needs to be controlled.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Test different parameter combinations to find the optimal parameters and reduce false signals. Key adjustable parameters include moving average periods, Exhaustion periods, etc.
2. Incorporate volatility indicators like ATR to dynamically adjust stop loss range according to market volatility.
3. Optimize position sizing, with different position sizing rules for different market conditions.
4. Incorporate chart patterns like trendlines, support lines to improve strategy performance.
5. Add machine learning algorithms to assist in gauging the effectiveness of key indicators, realizing dynamic optimization.

## Conclusion

The Momentum Exhaustion Strategy combines multiple indicators to identify trend reversal and control risks. It has trend following capability and can effectively determine entry and exit points. Further improvements can be made through parameter optimization, stop loss rules, incorporating chart patterns, and more. Overall, it has adaptability to market fluctuations and can be considered as a risk control strategy option.

||
 

## Overview

The Momentum Exhaustion Strategy is a trend following strategy that utilizes moving averages and price percentage oscillators to minimize downside exposure. It belongs to index fund trading models and can effectively control risks.

## Strategy Logic

The core indicators of this strategy are Exhaustion and Exhaustion Moving Average. Exhaustion is a measure of price oscillation, calculated from close, high, and low prices. The specific calculation is: \((\text{close} + \text{high} + \text{low} - \text{Exhaustion's moving average}) / \text{Exhaustion's moving average}\). The Exhaustion Moving Average is the moving average of Exhaustion. When Exhaustion crosses above Exhaustion Moving Average, it indicates consolidation in the market and a possible new trend forming. When Exhaustion crosses below Exhaustion Moving Average, it signals a trend reversal, and we should consider taking profit.

In addition, the strategy also uses long and short-term moving averages to assist in determining the trend, including 300-day, 150-day, and 50-day lines. When the short-term moving average crosses below the long-term moving average, it signals a trend reversal, and we should consider stopping loss.

MACD is also used for short-term buy and sell signals. When MACD line crosses above the signal line, it indicates a bullish signal, and when MACD crosses below the signal line, it indicates a bearish signal. RSI bottoms are also used as buy signals.

The specific entry and exit logic is:

Buy signal: Exhaustion crossing above Exhaustion Moving Average, and 50-day MA above 150-day MA; or RSI below 30.

Short-term stop loss: Exhaustion crossing below Exhaustion Moving Average; or MACD crossing below signal line.

Mid-long term stop loss: 50-day MA crossing below 150-day MA; or 150-day MA crossing below 300-day MA.

## Advantages of the Strategy

This strategy combines multiple indicators to determine the trend exhaustion and control risks. The advantages are:

1. The Exhaustion indicator can effectively identify consolidation and reversal. Timely detecting trend reversal is key to controlling risks.
2. Using moving averages of multiple timeframes to determine the trend avoids being misled by short-term market noise.
3. MACD helps confirm buy and sell signals, improving the strategy's performance.
4. RSI plays its role of buying low and selling high, buying at extremely oversold situations.
5. The clear profit taking and stop loss strategy can effectively control the risk of each trade.

## Risks of the Strategy

There are also some risks with this strategy:

1. Relying on multiple indicators, improper parameter settings may lead to wrong trading signals. Parameters need to be repeatedly tested and optimized.
2. The Exhaustion indicator is not completely reliable, it may fail when there is price divergence.
3. Improper stop loss placement may result in being stopped out by short-term fluctuations. Stop loss should balance long and short term effects.
4. When the overall market is ranging, the indicators may fail. Position sizing needs to be controlled.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Test different parameter combinations to find the optimal parameters and reduce false signals. Key adjustable parameters include moving average periods, Exhaustion periods, etc.
2. Incorporate volatility indicators like ATR to dynamically adjust stop loss range according to market volatility.
3. Optimize position sizing, with different position sizing rules for different market conditions.
4. Incorporate chart patterns like trendlines, support lines to improve strategy performance.
5. Add machine learning algorithms to assist in gauging the effectiveness of key indicators, realizing dynamic optimization.

## Conclusion

The Momentum Exhaustion Strategy combines multiple indicators to identify trend reversal and control risks. It has trend following capability and can effectively determine entry and exit points. Further improvements can be made through parameter optimization, stop loss rules, incorporating chart patterns, and more. Overall, it has adaptability to market fluctuations and can be considered as a risk control strategy option.

||
 

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|12|Fast Length|
|v_input_2|26|Slow Length|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|9|Signal Smoothing|
|v_input_5|false|Simple MA (Oscillator)|
|v_input_6|false|Simple