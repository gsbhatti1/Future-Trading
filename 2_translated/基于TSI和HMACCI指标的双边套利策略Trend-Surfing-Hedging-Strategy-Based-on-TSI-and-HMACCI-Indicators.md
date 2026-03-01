> Name

Trend-Surfing-Hedging-Strategy-Based-on-TSI-and-HMACCI-Indicators

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/120bfc6da0109ab1c39.png)
[trans]
## Overview

This strategy combines the bilateral trading signals of the TSI and improved CCI indicators, adopting a hedging approach to frequently open and close positions, aiming to pursue more stable continuous profits. The key logic is the golden cross and dead cross of the fast and slow moving averages of the TSI indicator, combined with the buy and sell signals of the HMACCI indicator to determine market direction. Risks are controlled by limiting opening conditions, while stop loss and take profit logics are set.

## Strategy Principle

The strategy is mainly based on the combination of the TSI and HMACCI indicators.

The TSI indicator contains a fast moving average and a slow one to determine trading signals. When the fast line breaks through the slow line upwards, it is a buy signal; vice versa for sell signals. This can capture changes in market trends more sensitively.

The HMACCI indicator is based on the traditional CCI indicator using Hull Moving Average instead of price itself, which can filter out some noise and judge overbought and oversold zones. The overbought and oversold zones can further confirm the signal direction of the TSI indicator.

The key logic of the strategy is to combine the judgments of these two indicators and set certain additional conditions to filter out false signals, such as examining the previous bar's closing price and maximum and minimum prices over multiple periods to control the quality of reversal signals.

For opening positions, if conditions are met, market orders are placed each time the bar closes, going both long and short. This can obtain more stable returns but undertakes the risks of a hedging strategy.

For take profit and stop loss, floating stop loss and close all orders when reaching target profit are set. This can effectively control the risks of one-way trades.

## Advantages of the Strategy

This is a relatively stable and reliable high-frequency hedging strategy. The main advantages include:

1. Combination of dual indicators can effectively avoid false signals
2. Frequent hedging operations every bar lead to more stable fluctuations in profit and loss 
3. Strict opening logic and stop loss conditions can control risks
4. Combining trend and reversal judgments leads to higher fault tolerance  
5. No directional bias, suitable for various market conditions
6. Large adjustable parameter space, can be optimized for different products

## Risk Analysis

The main risks to note are:

1. More fee loss caused by high-frequency trading 
2. Impossibility to perfectly avoid being locked in a hedge
3. Overly aggressive entry if parameters not set properly  
4. Difficulty to withstand one-way huge losses in the short term  

Risks can be reduced through:

1. Adjusting opening frequency appropriately to lower fee impact  
2. Optimizing indicator parameters to ensure signal quality  
3. Increasing stop loss amplitude but suffering more hedging losses
4. Testing on different products

## Optimization Directions

There is still a large room for optimizing this strategy, mainly:

1. Optimizing parameters like period, length etc., through testing 
2. Trying different indicator combinations e.g. MACD, BOLL etc.
3. Modifying opening logic, setting stricter filters   
4. Optimizing take profit and stop loss strategies e.g. dynamic, breakout stops
5. Using machine learning methods to find more stable parameter ranges
6. Testing on different trading products and timeframes  
7. Combining trend detection to avoid overly aggressive trades in range-bound markets

## Conclusion

Overall, this strategy is a stable, reliable hedging strategy with high fault tolerance. It combines trend and reversal indicators, obtaining steady returns through frequent dual-directional trading. Also, the strategy itself has strong potential for optimization and represents a worthwhile high-frequency trading idea to research further.

||

## Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|25|TSI Long Length|
|v_input_2|25|TSI Short Length|
|v_input_3|13|TSI Signal Length|
|v_input_4|33|HMACCI Length|
|v_input_5_open|0|Price Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|50|Line Distance|
|v_input_7|8|Candles Look Back|
|v_input_8|3000|Stop Loss|
|v_input_9|3000|Target Profit Close All|
|v_input_10|true|FromMonth|
|v_input_11|true|FromDay|
|v_input_12|2020|FromYear|
|v_input_13|true|ToMonth|
|v_input_14|true|ToDay|
|v_inpu