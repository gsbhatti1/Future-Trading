> Name

SR-突破策略-SR-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11747ab4f0b0f935ba8.png)

[trans]
#### Overview
The SR Breakout Strategy is a support and resistance breakout strategy developed based on LonesomeTheBlue's breakout finder indicator. The main idea of this strategy is to generate long or short signals by judging whether the closing price breaks through the support or resistance level. The default settings are based on 8-hour candlesticks, but there are better parameter settings for 4-hour candlesticks. This strategy uses the `pivothigh` and `pivotlow` functions to determine support and resistance levels, and uses the highest and lowest prices to determine breakouts. At the same time, this strategy also sets stop loss and take profit.

#### Strategy Principle
1. Use the `pivothigh` and `pivotlow` functions to calculate the highs and lows over a certain period of time and store them in arrays.
2. Determine whether the current closing price is higher than the resistance level. If so, it is judged as a bullish breakout, generating a long signal.
3. Determine whether the current closing price is lower than the support level. If so, it is judged as a bearish breakout, generating a short signal.
4. After generating a trading signal, calculate the stop loss and take profit prices based on the set stop loss and take profit ratios, and set the corresponding stop loss and take profit orders.
5. Draw the corresponding breakout range according to the breakout direction.

#### Strategy Advantages
1. Support and resistance breakout is a classic trading strategy with a certain practical basis.
2. By using the `pivothigh` and `pivotlow` functions to calculate support and resistance levels, breakouts can be captured relatively accurately.
3. The code structure of this strategy is clear, making it easy to backtest and optimize by storing highs and lows in arrays.
4. Stop loss and take profit are set, which can control risks effectively.

#### Strategy Risks
1. The support and resistance breakout strategy performs poorly in choppy markets and is prone to frequent false breakouts.
2. Fixed stop loss and take profit ratios may not adapt well to different market conditions, leading to an imbalance of risk and return.
3. This strategy only considers price factors and does not account for other important indicators such as trading volume, which might miss some crucial signals.

#### Strategy Optimization Direction
1. Consider incorporating more technical indicators like trading volume or MACD to improve signal accuracy and reliability.
2. For stop loss and take profit, consider using trailing stops or dynamic stop loss and take profit ratios to better adapt to different market conditions.
3. Introduce filtering conditions such as trend filters or volatility filters to reduce false breakouts in choppy markets.
4. Optimize support and resistance levels by using adaptive periods or incorporating Fibonacci levels.

#### Summary
The SR Breakout Strategy is a trading strategy based on the classic idea of support and resistance breakout, where highs and lows are calculated using `pivothigh` and `pivotlow` functions to generate trading signals when closing prices break through these levels. The advantage of this strategy lies in its clear logic and ease of implementation and optimization; however, it also faces risks such as poor performance in choppy markets and the potential for fixed stop loss and take profit ratios to cause imbalances in risk and return. Future improvements could focus on optimizing from technical indicators, stop loss and take profit mechanisms, filtering conditions, support and resistance levels, etc., to enhance its stability and profitability.

||

#### Overview
The SR Breakout Strategy is a support and resistance breakout strategy developed based on LonesomeTheBlue's breakout finder indicator. The main idea of this strategy is to generate long or short signals by judging whether the closing price breaks through the support or resistance level. The default settings are based on 8-hour candlesticks, but there are better parameter settings for 4-hour candlesticks. This strategy uses the `pivothigh` and `pivotlow` functions to determine support and resistance levels, and uses the highest and lowest prices to determine breakouts. At the same time, this strategy also sets stop loss and take profit.

#### Strategy Principle
1. Use the `pivothigh` and `pivotlow` functions to calculate the highs and lows over a certain period of time and store them in arrays.
2. Determine whether the current closing price is higher than the resistance level. If so, it is judged as a bullish breakout, generating a long signal.
3. Determine whether the current closing price is lower than the support level. If so, it is judged as a bearish breakout, generating a short signal.
4. After generating a trading signal, calculate the stop loss and take profit prices based on the set stop loss and take profit ratios, and set the corresponding stop loss and take profit orders.
5. Draw the corresponding breakout range according to the breakout direction.

#### Strategy Advantages
1. Support and resistance breakout is a classic trading strategy with a certain practical basis.
2. By using the `pivothigh` and `pivotlow` functions to calculate support and resistance levels, breakouts can be captured relatively accurately.
3. The code structure of this strategy is clear, making it easy to backtest and optimize by storing highs and lows in arrays.
4. Stop loss and take profit are set, which can control risks effectively.

#### Strategy Risks
1. The support and resistance breakout strategy performs poorly in choppy markets and is prone to frequent false breakouts.
2. Fixed stop loss and take profit ratios may not adapt well to different market conditions, leading to an imbalance of risk and return.
3. This strategy only considers price factors and does not account for other important indicators such as trading volume, which might miss some crucial signals.

#### Strategy Optimization Direction
1. Consider incorporating more technical indicators like trading volume or MACD to improve signal accuracy and reliability.
2. For stop loss and take profit, consider using trailing stops or dynamic stop loss and take profit ratios to better adapt to different market conditions.
3. Introduce filtering conditions such as trend filters or volatility filters to reduce false breakouts in choppy markets.
4. Optimize support and resistance levels by using adaptive periods or incorporating Fibonacci levels.

#### Summary
The SR Breakout Strategy is a trading strategy based on the classic idea of support and resistance breakout, where highs and lows are calculated using `pivothigh` and `pivotlow` functions to generate trading signals when closing prices break through these levels. The advantage of this strategy lies in its clear logic and ease of implementation and optimization; however, it also faces risks such as poor performance in choppy markets and the potential for fixed stop loss and take profit ratios to cause imbalances in risk and return. Future improvements could focus on optimizing from technical indicators, stop loss and take profit mechanisms, filtering conditions, support and resistance levels, etc., to enhance its stability and profitability.

||

```pinescript
//@version=5
strategy("SR Breakout Strategy", overlay=true, max_bars_back=500, max_lines_count=400)
prd = input.int(5, title="Period", minval=2)
bo_len = input.int(71, title="Max Breakout Length", minval=30, maxval=300)
cwidthu = input.float(3.0, title="Threshold Rate %") / 100
mintest = input.int(2, title="Minimum Number of Tests", minval=1)
bocolorup = input.color(color.blue, title="Breakout Colors")
```