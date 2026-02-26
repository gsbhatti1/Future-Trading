> Name

Eleven-Moving-Averages-Crossover-Strategy Ten Moving Averages Crossover Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1f7f2cebbb13c6663dd.png)

[trans]

## Overview

This strategy combines crossovers of 11 different types of moving averages for long and short entries. The 11 moving averages used are: Simple (SMA), Exponential (EMA), Weighted (WMA), Volume-weighted (VWMA), Smoothed (SMMA), Double Exponential (DEMA), Triple Exponential (TEMA), Hull (HMA), Zero Lag Exponential (ZEMA), Triangular (TMA), and SuperSmoother (SSMA) filter.

The strategy allows configuring two moving averages - a faster one and a slower one, both selected from the 11 options. Long signals are generated when the faster MA crosses above the slower MA. Short signals occur when the faster MA crosses below the slower MA.

Additional features include pyramiding settings, take profit and stop loss levels.

## Strategy Logic

The core strategy logic relies on crossovers between two moving averages to determine entries and exits.

The entry conditions are:

Long entry: Fast MA > Slow MA  
Short entry: Fast MA < Slow MA  

Exits are determined by one of three criteria:

1. Take profit level reached
2. Stop loss level reached 
3. Opposite signal generated (MA crossover in opposite direction)

The strategy allows configuring key parameters like the MA type and length, pyramiding settings, take profit and stop loss percentages. This provides flexibility to optimize the strategy for different market conditions and risk preferences.

## Advantages

- Combines 11 different MA types for robust signals  
- Flexible configuration of key parameters
- Take profit and stop loss features protect profits and limit losses
- Pyramiding allows increased position size for strong trends

## Risks

- As with any technical indicator, MA crossovers can generate false signals
- Overoptimization for current market conditions may degrade future performance
- Hard stop loss exits can lead to exiting good trades early in volatile markets

Risk management can be enhanced by using price action confirmation for entry signals, using trailing stops instead of hard stops, and avoiding overoptimization.

## Enhancement Opportunities

There are several ways in which this strategy can be improved:

1. Incorporate additional filters before entry, such as volume and price action checks
2. Test performance of different MA types systematically and select optimal 1 or 2
3. Optimize MA lengths specifically for trading instrument and time frame
4. Employ trailing stops instead of hard stops
5. Add profit taking at incremental levels as trend extends

## Conclusion

The eleven moving averages crossover strategy provides a systematic approach to trading crossovers. By combining signals across multiple MA indicators and allowing configuration of key parameters, it provides a robust yet flexible trading framework. Fine-tuning and risk management will play key roles in optimizing performance. The strategy has strong potential for momentum-based trading but should be adapted for different market environments.

||

## Overview

This strategy combines 11 different types of moving averages (SMA, EMA, WMA, VWMA, SMMA, DEMA, TEMA, HMA, ZEMA, TMA, SSMA) to generate both long and short trading signals. The core logic revolves around crossovers between two selected MA lines.

The strategy allows the user to configure:

- Two moving averages: a fast one and a slow one
- Take profit and stop loss levels
- Pyramiding settings

### Entry Conditions

- Long entry: Fast MA crosses above Slow MA  
- Short entry: Fast MA crosses below Slow MA  

### Exit Criteria

- Reaching the take profit level
- Reaching the stop loss level 
- Generating an opposite signal (crossover in the opposite direction)

Key parameters like MA type, length, and settings can be fine-tuned for different market conditions.

## Advantages

- Combines 11 different MA types to generate robust signals  
- Flexible configuration options
- Protection through take profit and stop loss features
- Ability to increase position size with pyramiding during strong trends

## Risks

- Like any technical indicator, there's a risk of generating false signals
- Overfitting the strategy may reduce its effectiveness in future markets
- Hard stop losses might force exiting profitable trades prematurely in volatile periods

To mitigate these risks, using price action confirmation for entries, employing trailing stops, and avoiding overfitting are recommended.

## Enhancement Opportunities

Improvements can be made by:

1. Incorporating additional filters before entry (e.g., volume and price action checks)
2. Systematically testing different MA types to select the most optimal 1-2
3. Optimizing MA lengths specifically for the trading instrument and timeframe
4. Replacing hard stops with trailing stops 
5. Adding incremental profit-taking levels as the trend extends

## Conclusion

The eleven moving averages crossover strategy provides a structured approach to detecting crossovers. By combining signals from multiple MA indicators and allowing flexible parameter configurations, it offers a robust yet adaptable trading framework. Fine-tuning and effective risk management are crucial for optimal performance. The strategy has significant potential in momentum-based trading but should be tailored to varying market conditions.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|0|MA Type: : ZEMA|EMA|WMA|VWMA|SMMA|DEMA|TEMA|HullMA|SMA|TMA|SSMA|
|v_input_2|8|Fast MA Length|
|v_input_3_close|0|Fast MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|21|Slow MA Length|
|v_input_5_close|0|Slow MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|true|Pyramiding|
|v_input_7|false|Take Profit Long|
|v_input_8|false|Take Profit Short|
|v_input_9|3|Take Profit Long %|
|v_input_10|30|Take Profit Short %|
|v_input_11|false|Stop Loss Long|
|v_input_12|false|Stop Loss Short|
|v_input_13|3|Stop Loss %|

> Source (PineScript)

``` pinescript
//@version=3
strategy(title="[STRATEGY] MA Cross Eleven", overlay=true)

// MA - type, source, length

type = input("ZEMA", title="MA Type: ", options=["SMA", "EMA", "WMA", "VWMA", "SMMA", "DEMA", "TEMA", "HullMA", "ZEMA", "TMA", "SSMA"])
len1 = input(8, title="Fast MA Length", minval=1)
srcclose1 = input(close, "Fast MA Source")
len2 = input(21, title="Slow MA Length", minval=1)
srcclose2 = input(close, "Slow MA Source")

// Returns MA input selection variant, default to SMA if blank or typo.
variant(type, src, len) =>
    v1 = sma(src, len)

```