> Name

Combining DMI and Moving Average Trading Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy identifies trend direction by combining the Directional Movement Index (DMI) and moving average to generate buy and sell signals. When DMI indicates that the price is in a trending state and the moving average confirms the trend direction, trading signals are produced.

## Strategy Logic

The strategy is based on two main indicators:

1. **DMI** includes DMI+ and DMI-, used to identify the existence and direction of a trend. When DMI+ is above DMI-, an uptrend is present; when DMI- is above DMI+, a downtrend is present.

2. The **moving average**, usually set between 15 to 50 days, determines the price trend direction. When the price is above (below) the moving average, it indicates an uptrend (downtrend).

The strategy first calculates the DMI+ and DMI- values along with the moving average. A trading signal is generated when both DMI shows a trending state (DMI+ above DMI- or vice versa) and the moving average confirms the direction:

- When DMI+ crosses above DMI- and price crosses above the MA, go long.
- When DMI- crosses above DMI+ and price crosses below the MA, go short.

A reverse input option is also included. Enabling this reverses the buy and sell signals.

## Advantage Analysis

Combining a trend-following indicator like DMI with a trend indicator like the moving average can improve signal reliability by leveraging the strengths of both indicators.

The advantage of DMI lies in its ability to quickly identify emerging trends. The moving average helps filter out noise, confirming the trend direction. By using both together, this strategy allows for early entry into trends while avoiding false signals in non-trending markets.

Additionally, the reverse option adds flexibility to trade with or against the trend.

## Risk Analysis

The main risks of this strategy are:

1. Incorrect signals may occur during trend transitions, potentially leading to losses. Adjusting parameters or setting stops can control this risk.
2. Trend formation takes time. During this period, price fluctuations might generate false signals. Lengthening DMI and MA periods can help filter out noise.
3. Reversal trading has the potential for larger loss magnification during adverse moves. With the reverse option enabled, losses should be limited, and trailing stops used to protect profits.
4. Parameters need optimization for different products and timeframes. Directly copying parameters may not yield good results in other contexts.

## Optimization Directions

Possible optimizations for this strategy include:

1. Testing different moving average period lengths to find the best fit for trend transitions.
2. Experimenting with DMI smoothing periods to filter out short-term reversals within trends.
3. Evaluating the impact of the reverse option versus default trend-following in historical backtests to determine which is more effective.
4. Incorporating stop strategies like trailing stops, time-based stops, or breakout stops to limit loss size.
5. Assessing parameter performance across different products and timeframes to optimize parameter combinations.
6. Adding filters like RSI to avoid false signals at localized extremes.

## Summary

This strategy combines the strengths of trend-following DMI and moving average indicators to enter trends early while avoiding whipsaws in choppy markets. The reverse option also adds flexibility. Further enhancements can be made through parameter optimization, stop strategies, and combining with additional filters. However, parameters will need to be re-tested for applicability across different products and timeframes.

|Argument|Default|Description|
|---|---|---|
|v_input_1|30|Length_MA|
|v_input_2|14|Length_DMI|
|v_input_3|false|Trade reverse|

> Source (PineScript)

``` pinescript
//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 03/03/2017
// The related article is copyrighted material from Stocks & Commodities Aug 2009 
//
// You can change long to short in the Input Settings
// Please, use it only for learning or paper trading. Do not for real trading.
////////////////////////////////////////////////////////////
strategy(title="Combining DMI And Moving Average For A EUR/USD Trading System")
Length_MA = input(30, minval=1)
Length_DMI = input(14, minval=1)
reverse = input(false, title="Trade reverse")
xMA = sma(close, Length_MA)
up = change(high)
down = -change(low)
trur = rma(tr, Length_DMI)
xPDI = fixnan(100 * rma(up > down and up > 0 ? up : 0, Length_DMI))
```