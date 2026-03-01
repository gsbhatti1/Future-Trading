> Name

RSI Indicator-Based Reversal Strategy

> Author

ChaoZhang

> Strategy Description


|||

## Overview

This strategy identifies reversal opportunities based on RSI indicators in overbought or oversold conditions. It monitors price divergence from RSI after it enters an overbought or oversold zone to determine potential future reversals.

## Strategy Logic  

This strategy uses the RSI indicator to identify market overbought and oversold situations. Once RSI enters a preset overbought or oversold zone, it starts monitoring for divergence between price and RSI.   

Specifically, if RSI enters the overbought zone, it monitors whether the price continues to rise (forming higher lows) while RSI forms lower lows - this is a regular bullish divergence; or the price forms lower lows and RSI forms higher lows – which is a hidden bullish divergence. Both situations signal potential downside reversals ahead.  

Similarly, if RSI enters the oversold zone, it monitors whether the price continues to fall (forming lower highs) while RSI forms higher highs - this is a regular bearish divergence; or the price forms higher highs and RSI forms lower lows – which is a hidden bearish divergence. Both situations also signal potential upside reversals ahead.

Once these reversal signals are detected, long or short positions will be taken according to the configured parameters.   

## Advantages  

The biggest advantage of this strategy is its ability to identify extreme market conditions where reversals are more likely, and thus provide a larger profit margin for such operations. Compared to simple trend-following strategies, counter-trend strategies like this one have higher win rates and profitability.

In addition, the strategy incorporates monitoring for both regular and hidden divergences, allowing for the identification of more reversal opportunities and preventing missed chances due to one-off situations.

## Risks

The biggest risk associated with this strategy is the potential for even more extreme overbought or oversold conditions – so-called "straight up, 90 degrees down." In such cases, continuing long or short positions are more likely, making it easy to suffer stop losses if a reversal operation is taken.

Additionally, improper parameter settings and errors in judging overbought and oversold situations can lead to mistakes. 

The solution is to reasonably set the upper and lower limits for overbought and oversold zones to avoid overly extreme conditions. Furthermore, scale down the position size during live trading to control the single stop loss amount.

## Optimization Directions   

The strategy can be optimized in several ways:

1. Incorporate other indicators to determine overbought and oversold conditions, avoiding reliance solely on RSI.
2. Add logic to identify consolidation before breakouts when reversal probabilities are higher.
3. Optimize profit target settings after reversals for more scientific position sizing.
4. Utilize machine learning methods with recent years of historical data to automatically optimize parameters.
5. Improve stop loss logic optimization, such as timely profit taking, staggered stop losses, and trailing stops.

## Conclusion  

In conclusion, this is a typical statistical arbitrage strategy that aims to capture opportunities when the market rebounds from extreme conditions back to equilibrium. Compared to trend-following strategies, it has higher win rates and profitability but also faces greater risks. With proper parameter optimization and risk management, such strategies can achieve steady profits.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|14|(?regular RSI settings)RSI Period|
|v_input_source_1_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_2|5|Pivot Lookback Right|
|v_input_int_3|5|Pivot Lookback Left|
|v_input_int_4|60|Max of Lookback Range|
|v_input_int_5|5|Min of Lookback Range|
|v_input_bool_1|true|Plot Bullish|
|v_input_bool_2|true|Plot Hidden Bullish|
|v_input_bool_3|true|Plot Bearish|
|v_input_bool_4|true|Plot Hidden Bearish|
|v_input_int_6|70|(?look for RSI divergence after OverBought/OverSold)OB RSI Value|
|v_input_int_7|30|OB lookback period|
|v_input_int_8|35|OS RSI Value|
|v_input_int_9|30|OS lookback period|
|v_input_int_10|60|min RSI for bear Alerts|
|v_input_int_11|50|max RSI for Bull Alerts|
|v_input_1|true|(?enable Backtester)to enable the Backtester, uncomment/comment the ? lines in the source code|
|v_input_2|true|(?Long Backtester)enable Long Backtester (to disable uncheck 'plot Bullish' and 'plot hidden Bullish as well')|
|v_input_float_1|0.5|Stop Loss %|
|v_input_float_2|2|Take Profit %|
|v_input_3|true|(?Short Backtester)enable Short Backtester (to disable uncheck