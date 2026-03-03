> Name

Historical Volatility Range Breakout Trading Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy generates trading signals based on the historical volatility range of the price. It calculates the difference between the highest and lowest prices over a certain period, and forms a volatility range using moving averages. Trading signals are triggered when the price breaks through the upper or lower bands of the range. This belongs to trend-following breakout strategies.

## Strategy Logic

The core indicator is the historical volatility of the price. The specific calculation is:

1. Calculate the difference between the highest and lowest prices over the past N bars, called HL
2. Calculate the average of the highest and lowest prices over N bars, avg(H, L)
3. Volatility = HL / avg(H, L)

Where N is the "Volatility Length" parameter.

After getting the volatility, the bands are calculated as:

Upper Band = Current close + Current close * Volatility

Lower Band = Current close - Current close * Volatility

The bands are then smoothed by WMA with period set as "Average Length".

When price breaks above the upper band, go long. When price breaks below the lower band, go short.

Exit signals are defined by "Exit Type":

1. If Exit Type is Volatility MA, exit when price crosses back below WMA.
2. If Exit Type is Range Crossover, exit when price crosses back below the bands.

## Advantages

- Volatility catches trending moves well
- WMA makes the bands more stable and reliable
- Breakout signals catch trend turns timely
- Exits based on WMA/bands cut losses fast
- Much room for parameter tuning for different markets

## Risks

- Breakouts may whipsaw with price reversing 
- Large risks at trend reversals
- WMA sometimes lags in detecting trend turns
- Parameter optimization not easy, needs much trial and error
- Larger drawdowns, need good risk management

Risks can be reduced by:

- Optimizing parameters for more reliable bands
- Adding other indicators to avoid whipsaws
- Smaller sizes and better risk management 
- Considering re-entries

## Optimization Directions

The strategy can be improved by:

1. Parameter tuning  
   Test different Length values to find optimal combinations.
2. Adding other indicators
   For example, when price breaks above upper band, check if MACD also golden crosses.
3. Better stop loss
   Optimizing to trailing stops instead of simple range break stops.
4. Re-entries
   Set re-entry rules to catch trends again after stops.
5. Position sizing
   Dynamically adjust sizes based on market volatility.

## Summary

This strategy works well for trending markets in general by using volatility-based bands to gauge trend strength and WMA to form reliable trading ranges for breakout signals. But some issues exist like lagging trend detection, improvable stops, etc. Extensive backtesting and optimization is needed using real data to adjust parameters and rules, reducing false signals and making it robust across different market conditions. Also strict risk management is key for long-term profitability.

||

## Overview

This strategy generates trading signals based on the historical volatility range of the price. It calculates the difference between the highest and lowest prices over a certain period, and forms a volatility range using moving averages. Trading signals are triggered when the price breaks through the upper or lower bands of the range. This belongs to trend-following breakout strategies.

## Strategy Logic

The core indicator is the historical volatility of the price. The specific calculation is:

1. Calculate the difference between the highest and lowest prices over the past N bars, called HL
2. Calculate the average of the highest and lowest prices over N bars, avg(H, L)
3. Volatility = HL / avg(H, L)

Where N is the "Volatility Length" parameter.

After getting the volatility, the bands are calculated as:

Upper Band = Current close + Current close * Volatility

Lower Band = Current close - Current close * Volatility

The bands are then smoothed by WMA with period set as "Average Length".

When price breaks above the upper band, go long. When price breaks below the lower band, go short.

Exit signals are defined by "Exit Type":

1. If Exit Type is Volatility MA, exit when price crosses back below WMA.
2. If Exit Type is Range Crossover, exit when price crosses back below the bands.

## Advantages

- Volatility catches trending moves well
- WMA makes the bands more stable and reliable
- Breakout signals catch trend turns timely
- Exits based on WMA/bands cut losses fast
- Much room for parameter tuning for different markets

## Risks

- Breakouts may whipsaw with price reversing 
- Large risks at trend reversals
- WMA sometimes lags in detecting trend turns
- Parameter optimization not easy, needs much trial and error
- Larger drawdowns, need good risk management

Risks can be reduced by:

- Optimizing parameters for more reliable bands
- Adding other indicators to avoid whipsaws
- Smaller sizes and better risk management 
- Considering re-entries

## Optimization Directions

The strategy can be improved by:

1. Parameter tuning  
   Test different Length values to find optimal combinations.
2. Adding other indicators
   For example, when price breaks above upper band, check if MACD also golden crosses.
3. Better stop loss
   Optimizing to trailing stops instead of simple range break stops.
4. Re-entries
   Set re-entry rules to catch trends again after stops.
5. Position sizing
   Dynamically adjust sizes based on market volatility.

## Summary

This strategy works well for trending markets in general by using volatility-based bands to gauge trend strength and WMA to form reliable trading ranges for breakout signals. But some issues exist like lagging trend detection, improvable stops, etc. Extensive backtesting and optimization is needed using real data to adjust parameters and rules, reducing false signals and making it robust across different market conditions. Also strict risk management is key for long-term profitability.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|100|Average Length|
|v_input_int_2|100|Volatility Length|
|v_input_source_1_close|0|Volatility Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_source_2_close|0|Exit Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_string_1|0|Exit Type: Volatility MA|Range Crossover|


> Source (PineScript)

```pinescript
//@version=5
strategy("Historical Volatility Range Breakout Trading Strategy", shorttitle = "VRB Strategy", overlay=true,
    pyramiding=20, max_bars_back=2000, initial_capital=10000)

wma(float priceType, int length, float weight) =>
    norm = 0.0
    sum = 0.0
    for i = 0 to length - 1
        norm := norm + weight
        sum := sum + priceType[i] * weight
    sum / norm

// This definition of volatility uses the high-low range divided by the average of that range.
volatility(source, length) =>
    h = ta.highest(source, length)
    l = ta.lowest(source, length)
    vx = 2 * (h - l) / (h + l)
    vx

vm1 = input.int(100, "Average Length")
volLen = input.int(100, "Volatility Length")
vsrc = input.source(close, "Volatility Source")
cross_type = input.source(close, "Exit Source")
exit_type = input.string("Volatility MA", "Exit Type")

// Calculate volatility and bands
hl = ta.highest(vsrc, volLen)
ll = ta.lowest(vsrc, volLen)
vx = volatility(vsrc, volLen)

upper_band = close + close * vx
lower_band = close - close * vx

smooth_upper_band = wma(upper_band, vm1)
smooth_lower_band = wma(lower_band, vm1)

// Trading logic
if exit_type == "Volatility MA"
    if ta.crossover(close, smooth_upper_band)
        strategy.entry("Long", strategy.long)
    if ta.crossunder(close, smooth_lower_band)
        strategy.close("Long")

elif exit_type == "Range Crossover"
    if close > upper_band
        strategy.entry("Long", strategy.long)
    if close < lower_band
        strategy.close("Long")
```

This PineScript code implements the described historical volatility range breakout trading strategy. It uses a WMA to smooth the calculated bands and provides options for different exit types based on the WMA or range crossover.