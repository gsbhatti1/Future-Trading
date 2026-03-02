> Name

RSI-VWAP Price-Volume Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

The RSI-VWAP price-volume strategy is a trend-following strategy. It combines the Relative Strength Index (RSI) and Volume Weighted Average Price (VWAP) to implement multiple additions of positions with stop losses in trends. This strategy is suitable for medium-to-long term trend trading.

## Principle  

When the RSI line falls from the overbought zone into the oversold zone, it is considered a trend reversal signal to go long. When the RSI line rises from the oversold zone into the overbought zone, it is considered a trend reversal signal to go short.

The stop loss for long positions is set at (1-stop loss percentage) of the latest entry price. The take profit is set at (1+take profit percentage) of the average holding price. The settings for short positions are similar.

After each new entry, the strategy allows up to 5 additional additions if the signal triggers again. The position size increases with each new addition to follow the trend.

## Advantages

1. Combining the RSI indicator and VWAP indicator helps better identify trend reversal points.
2. Multiple additions allow taking full advantage of trending moves. As the number of entries increases, the position size gradually expands to follow the trend.
3. The stop loss effectively controls risks. Exits are triggered when a loss occurs to avoid further losses.
4. The trailing take profit locks in profits and avoids giving back gains.

## Risks  

1. The RSI indicator has repainting. Actual signal timing may deviate.
2. VWAP may also repaint. The actual optimal entry can only be determined in hindsight.
3. Improper stop loss placement may cause unnecessary losses.
4. Improper take profit placement may prevent gains from being realized.
5. Wrong trend judgment can increase losses from persistently holding long or short positions.

## Enhancements

1. Optimize RSI parameters to find the optimal lookback period.
2. Optimize the overbought/oversold zones for better trend reversal signals.
3. Test different addition strategies to find the optimal approach.
4. Optimize the stops and takes to find the best parameters.
5. Try combining other indicators to increase the probability of accurately detecting trend reversals.

## Conclusion

The RSI-VWAP strategy identifies trend reversal points using RSI and VWAP, adds positions to follow the trend, takes profit when predefined targets are met, and stops out with a loss. It balances risk management and profit protection. Further optimizations can improve strategy performance. This strategy suits experienced traders for medium-to-long term trend trading.

||

## Overview

The RSI-VWAP price-volume strategy is a trend following strategy that combines the Relative Strength Index (RSI) and Volume Weighted Average Price (VWAP) to implement pyramiding and stop loss in trends. It is suitable for medium-to-long term trend trading.

## Principle  

When the RSI line falls from the overbought zone into the oversold zone, it is considered a trend reversal signal to go long. When the RSI line rises from the oversold zone into the overbought zone, it is considered a trend reversal signal to go short.

The stop loss for long positions is set at (1-stop loss percentage) of the latest entry price. The take profit is set at (1+take profit percentage) of the average holding price. The settings for short positions are similar.

After each new entry, the strategy allows up to 5 additional pyramiding entries if the signal triggers again. The position size increases with each new entry to follow the trend.

## Advantages

1. Combining the RSI indicator and VWAP indicator helps better identify trend reversal points.
2. Pyramiding entries allow taking full advantage of trending moves. As the number of entries increases, the position size gradually expands to follow the trend.
3. The stop loss effectively controls risks. Exits are triggered when a loss occurs to avoid further losses.
4. The trailing take profit locks in profits and avoids giving back gains.

## Risks  

1. The RSI indicator has repainting. Actual signal timing may deviate.
2. VWAP may also repaint. The actual optimal entry can only be determined in hindsight.
3. Improper stop loss placement may cause unnecessary losses.
4. Improper take profit placement may prevent gains from being realized.
5. Wrong trend judgment can increase losses from persistently holding long or short positions.

## Enhancements

1. Optimize RSI parameters to find the optimal lookback period.
2. Optimize the overbought/oversold zones for better trend reversal signals.
3. Test different pyramiding strategies to find the optimal approach.
4. Optimize the stops and takes to find the best parameters.
5. Try combining other indicators to increase the probability of accurately detecting trend reversals.

## Conclusion

The RSI-VWAP strategy identifies trend reversal points using RSI and VWAP, adds positions to follow the trend, takes profit when predefined targets are met, and stops out with a loss. It balances risk management and profit protection. Further optimizations can improve strategy performance. This strategy suits experienced traders for medium-to-long term trend trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|0|LONG / SHORT: LONG ONLY|LONG & SHORT|
|v_input_2|true|RSI VOLUME WEIGHTED AVERAGE PRICE|
|v_input_3|17|RSI-VWAP LENGTH|
|v_input_4|19|RSI-VWAP OVERSOLD|
|v_input_5|80|RSI-VWAP OVERBOUGHT|
|v_input_6|5|PYRAMIDING ?|
|v_input_7|true|ACTIVATE SL / DEACTIVATE RE-ENTRY|
|v_input_8|7.5|STOP LOSS / RE-ENTRY %|
|v_input_9|false|ACTIVATE TAKE PROFIT|
|v_input_10|10|TAKE PROFIT %|
|v_input_11|true|BACKTEST ?|
|v_input_12|1000|$ QUANTITY 1ST ENTRY|
|v_input_13|500|$ INCREASE NEXT ENTRY|
|v_input_14|2019|BACKTEST START YEAR ⏲️|
|v_input_15|true|BACKTEST START MONTH|
|v_input_16|true|BACKTEST START DAY|
|v_input_17|2222|BACKTEST STOP YEAR|
|v_input_18|12|BACKTEST STOP MONTH|
|v_input_19|31|BACKTEST STOP DAY|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-07 00:00:00
end: 2023-10-07 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Xaviz

//#####©ÉÉÉÉ¶N###############################################
//####*..´´´´´´,,,»ëN########################################
//###ë..´´´´´´,,,,,,''%©#####################################
//###'´´´´´´,,,,,,,'''''?¶###################################
//##o´´´´´´,,,,,,,''''''''*©#################################
//##'´´´´´,,,,,,,'''''''^^^~±################################
//#±´´´´´,,,,,,,''''''''^í/;~*©####æ%;í»~~~~;==I±N###########
//#»´´´´,,,,,,'''''''''^;////;»¶X/í~~/~~~;=~~~~~~~~*¶########
//#'´´´,,,,,,''''''''^^;////;%I^~/~~/~~~=~~~;=?;~~~~;?ë######
//©´´,,,,,,,''''''''^^~/////X~/~~/~~/~~»í~~=~~~~~~~~~~^;É####
//¶´,,,,,,,''''''''^^^;///;%;~/~~;í~~»~í?~?~~~?I/~~~~?*=íÑ###
//N,,,,,,,'''''''^^^^^///;;;;o/~~;;~~;£=»í»;IX/=~~~~~~^^^^'*æ##
//#í,,,,,''''''''^^^^^^í;;;;£;~~~//»I»/£X/X/»í*&~~~^^^^'^*~'É#
//##N^''''''^^^^^^^^^^~~~;;;;/£;~~/»~~»~~///o~~^^^^''''?^',æ#
//###Ñ''''^^^^^^^^^^^~~~~~;;;;;í*X*í»;~~IX?~~^^^^/?'''''=,=##
//####X'''^^^^^^^^^^~~~~~~~~;;íííííí~~í*=~~~~Ií^'''=''''^»©##
//#####£^^^^^^^^^^^~~~~~~~~~~~íííííí~~~~~*~^^^;/''''='',,N###
//####