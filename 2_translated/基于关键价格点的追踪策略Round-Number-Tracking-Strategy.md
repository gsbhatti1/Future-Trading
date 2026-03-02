> Name

Round-Number-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

This strategy is based on the idea that stop loss and take profit levels are often placed at round number or key price levels, which act as support and resistance. The strategy identifies these key price levels and enters trades when the price approaches them.

## Strategy Logic

The main rules of this strategy are:

1. When the close price is above a key price level, and has not touched that level in the past 10 bars, go long.
2. Use a trailing stop with a 20-point step to follow the movement after the price breaks the key level.
3. Sell signals are the opposite - when the close is below the key price level and has not touched it in the past 10 bars, go short.
4. Key levels are identified as:
   - Convert the close price to an integer.
   - Calculate the remainder from dividing by 50 (configurable).
   - If the remainder is greater than 25, use the next 50 whole number as the key level.
   - Otherwise, keep the key level unchanged.

The strategy is based on the psychology that round numbers and key levels are often battlegrounds for bulls and bears, and thus provide effective trade signals. The trailing stop follows the trend after the breakout.

## Advantages

The advantages of this strategy are:

1. Simple and intuitive trade signals and entry rules.
2. Utilizes a universal pattern of key prices rather than instrument-specific rules.
3. Trailing stop locks in profits while riding the trend.

## Risks

The risks to consider are:

1. Key levels may not always act as strong support or resistance. False breakouts are possible.
2. A fixed 10-bar lookback may not suit different instruments.
3. The trailing stop distance should not be too wide, otherwise it may stop out prematurely.

Possible solutions:

1. Add more filters to judge the strength of key levels, such as volume.
2. Optimize parameters like the lookback period for different instruments.
3. Optimize the trailing stop mechanism to be more adaptive.

## Enhancement Opportunities

The strategy can be improved by:

1. Adding more conditions to confirm the importance of key levels and avoid false breakouts. For example, combine with volume.
2. Optimizing parameters like the key level range and lookback period based on instrument characteristics.
3. Enhancing the trailing stop mechanism, such as using a dynamic trailing stop instead of a fixed step.
4. Incorporating machine learning to judge the strength of key levels using historical data.
5. Expanding to a multi-timeframe system with higher timeframe trends and lower timeframe tracking.

## Conclusion

This strategy offers simple and intuitive signals based on key price levels and trading conventions. It has abundant opportunities but needs further optimization to handle false breakouts. Parameter tuning and machine learning can improve robustness. It provides good day trading ideas and can also be expanded to a multi-timeframe trend tracking system.

||

## Overview

This strategy is based on the idea that stop loss and take profit levels are often placed at round number or key price levels, which act as support and resistance. The strategy identifies these key price levels and enters trades when the price approaches them.

## Strategy Logic

The main rules of this strategy are:

1. When the close price is above a key price level, and has not touched that level in the past 10 bars, go long.
2. Use a trailing stop with a 20-point step to follow the movement after the price breaks the key level.
3. Sell signals are the opposite - when the close is below the key price level and has not touched it in the past 10 bars, go short.
4. Key levels are identified as:
   - Convert the close price to an integer.
   - Calculate the remainder from dividing by 50 (configurable).
   - If the remainder is greater than 25, use the next 50 whole number as the key level.
   - Otherwise, keep the key level unchanged.

The strategy is based on the psychology that round numbers and key levels are often battlegrounds for bulls and bears, and thus provide effective trade signals. The trailing stop follows the trend after the breakout.

## Advantages

The advantages of this strategy are:

1. Simple and intuitive trade signals and entry rules.
2. Utilizes a universal pattern of key prices rather than instrument-specific rules.
3. Trailing stop locks in profits while riding the trend.

## Risks

The risks to consider are:

1. Key levels may not always act as strong support or resistance. False breakouts are possible.
2. A fixed 10-bar lookback may not suit different instruments.
3. The trailing stop distance should not be too wide, otherwise it may stop out prematurely.

Possible solutions:

1. Add more filters to judge the strength of key levels, such as volume.
2. Optimize parameters like the lookback period for different instruments.
3. Optimize the trailing stop mechanism to be more adaptive.

## Enhancement Opportunities

The strategy can be improved by:

1. Adding more conditions to confirm the importance of key levels and avoid false breakouts. For example, combine with volume.
2. Optimizing parameters like the key level range and lookback period based on instrument characteristics.
3. Enhancing the trailing stop mechanism, such as using a dynamic trailing stop instead of a fixed step.
4. Incorporating machine learning to judge the strength of key levels using historical data.
5. Expanding to a multi-timeframe system with higher timeframe trends and lower timeframe tracking.

## Conclusion

This strategy offers simple and intuitive signals based on key price levels and trading conventions. It has abundant opportunities but needs further optimization to handle false breakouts. Parameter tuning and machine learning can improve robustness. It provides good day trading ideas and can also be expanded to a multi-timeframe trend tracking system.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|500|Round Level 1, pips|
|v_input_2|1000|Max distance, pips|
|v_input_3|100|Distance in pips to full level|
|v_input_4|20|Trail Step points|


> Source (PineScript)

```pinescript
//@version=3
strategy("dP magnet", overlay=true, pyramiding=0, default_qty_type=strategy.percent_of_equity, default_qty_value=100, currency=currency.USD)

// Round Levels credit to RKchartest

roundLevel50 = input(500, 'Round Level 1, pips')
//roundLevel100 = input(1000, 'Round Level 2, pips')
deviation = input(1000, 'Max distance, pips', minval=0) 

rDelimeter = 1/syminfo.mintick

intRoundLevel = close[1] * rDelimeter

intRemainder = intRoundLevel % roundLevel50 
toRound = (intRemainder >= roundLevel50/2) ? roundLevel50 : 0
roundLevel = (intRoundLevel - intRemainder + toRound) / rDelimeter
plot(roundLevel, title='Round Level 1', color=black, style=line, transp=0, linewidth=1, trackprice=false)

//intRemainder2 = intRoundLevel % roundLevel100
//toRound2 = (intRemainder2 >= roundLevel100/2) ? roundLevel100 : 0
//roundLevel2 = (intRoundLevel - intRemainder2 + toRound2) / rDelimeter
//plot((abs(roundLevel2 - close) * rDelimeter < deviation) ? roundLevel2 : na, title
```