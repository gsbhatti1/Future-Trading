> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|true|(?Date Range)Start Date & Time|
|v_input_1|timestamp(16 Apr 2021)|startPeriodTime|
|v_input_bool_2|false|End Date & Time|
|v_input_2|timestamp(31 Dec 2222)|endPeriodTime|
|v_input_bool_3|false|Highlight|
|v_input_string_1|0|highlightType: Anchors|Background|
|v_input_color_1|white|highlightColor|
|v_input_3_close|0|(?Support)Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|true|Show EMA|
|v_input_int_1|6|(?Stochastic RSI)K period|
|v_input_int_2|3|(?Stochastic RSI)D period|
|v_input_int_3|50|(?EMA)Short EMA period|
|v_input_int_4|100|(?EMA)Long EMA period|
|v_input_int_5|200|(?EMA)Very Long EMA period|
|v_input_bool_5|false|Show Stochastic|
|v_input_int_6|6|(?Stochastic RSI)Smooth K|
|v_input_int_7|3|(?Stochastic RSI)Smooth D|
|v_input_bool_6|true|Show Buy Signal|
|v_input_bool_7|true|Show Sell Signal|
|v_input_int_8|0|(?Other)Trade Signal Color|
|v_input_int_9|0|(?Other)Stochastic Signal Color|
|v_input_int_10|0|(?Other)EMA Signal Color|
|v_input_int_11|0|(?Other)Overbought Level|
|v_input_int_12|0|(?Other)Oversold Level|


> Strategy Description

## Overview

This strategy uses dual moving average indicators and triple exponential moving average indicators, combined with stochastic indicators, to form a relatively stable and reliable trend tracking trading strategy. Its main idea is to issue trading signals when the moving average indicator detects golden crosses or death crosses; while the stochastic indicator is used to assist in judging overbought and oversold situations to avoid generating wrong signals during drastic market fluctuations.

## Principles

This strategy consists mainly of four parts:

1. Dual Moving Average Indicator: Calculates the 50-period and 100-period exponential moving averages (EMA) respectively. It generates a buy signal when the short-term EMA crosses above the long-term EMA, and a sell signal when crossing below.
  
2. Triple Exponential Indicator: Calculates the 50-period, 100-period, and 200-period exponential moving averages to determine the market trend direction. When 50EMA > 100EMA > 200EMA, it is a bullish market. When 50EMA < 100EMA < 200EMA, it is a bearish market.

3. Stochastic Indicator: Calculates the 6-day K and D values of RSI to determine overbought and oversold conditions. When the K value crosses above the D value, it is oversold. When crossing below, it is overbought. 

4. Trading Signals: Only when the dual moving average indicator generates a signal at the same time when the market conforms to the bullish or bearish state of the triple exponential moving average, and the stochastic indicator does not show overbought or oversold, will true trading orders be issued.

## Advantages

This strategy combines the advantages of moving average indicators and stochastic indicators. It takes into account both the judgment of trend direction and the overbought/oversold state of the market when issuing trading signals, thereby filtering out noise more effectively to track clearer trends. In addition, it uses the triple exponential moving average to determine the overall trend, making the signals more reliable. This strategy is simple, easy to implement, and easy to optimize.

## Risks and Countermeasures

The biggest risk of this strategy is that it relies on indicator judgments. When the indicator gives out wrong signals, it can easily lead to failed trades. In addition, when using longer cycle moving averages to determine the overall trend, some short-term opportunities may also be missed out. The main risk countermeasures are as follows:

1. Optimize indicator parameters and adjust the cycle combinations of dual moving averages and triple exponential moving averages to match them better to market characteristics.

2. Incorporate more indicators for CANCEL operations, terminating current trades when the market shows drastic fluctuations.

3. Employ auxiliary short-term bullish strategies to capitalize on short-term opportunities in long-term bull markets.

## Optimization Directions

The main aspects where this strategy can be optimized include:

1. Adjust the cycle parameters of the dual moving average and triple exponential moving average to optimize the indicators’ adaptation to market characteristics.

2. Increase VOLUME, MACD and other judgments to avoid abnormal price movements causing wrong signals.

3. Better confirm trends using candlestick patterns to avoid wrong signals after short-term pullbacks.

4. Expand it to more varieties like stocks, forex and test adaptability of the strategy.

5. Incorporate VIX indicators to determine overall market volatility and control position sizing.

## Conclusion

This strategy uses dual moving average indicators to issue trading signals, with triple exponential moving averages and stochastic indicators as complements, thereby constructing a relatively stable trend tracking strategy. It is simple, easy to implement, highly matched with market characteristics, delivering stable returns. It is a worthwhile quantitative strategy to recommend. Through targeted optimizations, it has the potential to achieve even better results.