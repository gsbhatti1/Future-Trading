> Name

Triple-Moving-Average-Combined-with-MACD-Quantitative-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1d2c8e4caaaf440cce2.png)
 [trans]
## Overview

This strategy develops a relatively stable and reliable quantitative trading strategy by combining the use of triple moving average indicator and MACD indicator. It aims to capture possible future trends and is particularly suitable for medium and long term holdings.

## Strategy Principle  

The strategy is mainly based on the combination of triple moving average and MACD indicator.

Firstly, the strategy uses triple exponential moving averages with lengths of 3, 7 and 2 respectively. These three moving averages construct a fast to slow moving average system to determine the direction of future trends. When the short-term moving average crosses over the longer-term moving average, it is a long signal; when the short-term moving average crosses below the longer-term moving average, it is a short signal.

Secondly, the strategy also uses MACD indicator with parameters of 3 and 7 simultaneously. When MACD main line crosses over signal line, it is a long signal, and when it crosses below, it is a short signal.

By combining the use of dual indicators, it can avoid multiple false signals caused by a single indicator, thereby improving the stability of the strategy.

## Advantages of the Strategy  

1. Improved signal quality by using dual indicator filtering  
2. Parameters have been tested and optimized many times, stable and reliable
3. The triple moving average system can effectively filter market noise and determine future trends  
4. MACD indicator parameters are set faster to quickly capture short term opportunities

## Risks of the Strategy

1. There are certain risks of drawdown and consecutive losses
2. When the market has no obvious trend, there will be more false trades in this strategy
3. MACD indicator is prone to generating false signals and needs to be combined with moving average indicators

Solutions:

1. Adopt appropriate stop loss strategy to control maximum drawdown  
2. Reduce trading frequency when market state is clearly trendless
3. Optimize MACD parameters and use in combination with other indicators

## Directions for Strategy Optimization  

1. Test and optimize parameters of moving averages and MACD to find the best combination  
2. Increase auxiliary indicators like KDJ and VRSI to avoid false signals
3. Introduce machine learning models to judge market state and achieve dynamic adjustment  
4. Combine with stop loss strategies and set optimal stop loss points  

## Summary

This strategy achieves stable trend capturing through the combination of moving averages and MACD. Its advantage lies in the combination use of indicators, which can effectively reduce false signals and obtain better strategy performance. Next steps to further improve the strategy include introducing parameters optimization, stop loss strategies, dynamic adjustment etc, making it an effective tool to find medium and long term opportunities.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|50|Trailing Stop in cents|
|v_input_2|6|From Month|
|v_input_3|true|From Day|
|v_input_4|2017|From Year|
|v_input_5|true|To Month|
|v_input_6|true|To Day|
|v_input_7|9999|To Year|
|v_input_8|false|Enable Bar Color?|
|v_input_9|true|Enable Moving Averages?|
|v_input_10|false|Enable Background Color?|
|v_input_11|false|Enable Bolinger Bands?|
|v_input_12|false|Enable Keltner Channel?|
|v_input_13|14|R_length|
|v_input_14|80|%R Overbought|
|v_input_15|20|%R Oversold|
|v_input_16|3|RSI Length|
|v_input_17|80|RSI Overbought|
|v_input_18|20|RSI Oversold|
|v_input_19|20|cci_length|
|v_input_20_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_21|3|MFI Length|
|v_input_22|80|MFI Overbought|
|v_input_23|20|MFI Oversold|
|v_input_24|50|Very slow SMA|
|v_input_25_close|0|MACD source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_26|12|MACD Fast Length|
|v_input_27|3|MACD Fast Length #2|
|v_input_28|26|MACD Slow Length|
|v_input_29|7|MACD Slow Length #2|
|v_input_30|7|Signal Smoothing|
|v_input_31|12|Signal Smoothing|
|v_input_32|5|Signal Smoothing #2|
|v_input_33|9|Signal Smoothing #2|
|v_input_34|-0.003|MACD % Threshold|
|v_input_35|20|bb_length|
|v_input_36|1.86|bb_mult|
|v_input_37|true|KC_useTrueRange|
|v_input_38|20|KC_length|
|v_input_39|3|KC_mult|
|v_input_40_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_41|5|Resolution|
|v_input_42|15|Resolution|
|v_input_43|30|Resolution|
|v_input_44|60|Resolution|
|v_input_45|0.02|start|
|v_input_46|0.02|increment|
|v_input_47|0.2|maximum|
|v_input_48|3|v_input_48|
|v_input_49|3|v_input_49|
|v_input_50|7|v_input_50|
|v_input_51|2|v_input_51|
|v_input_52|true|v_input_52|
|v_input_53|9|Conversion Line Periods|
|v_input_54|26|Base Line Periods|
|v_input_55|50|Lagging Span 2 Periods|
|v_input_56|25|Displacement|
|v_input_57|9|Length