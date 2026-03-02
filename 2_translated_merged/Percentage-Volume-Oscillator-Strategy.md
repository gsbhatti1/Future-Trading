> Overview

The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume. PVO measures the difference between two volume-based moving averages as a percentage of the larger moving average to gauge shifts in volume trends. This strategy uses PVO to identify volume trends to confirm or refute price action. Typically, a breakout or support break is validated when PVO is rising or positive.

Strategy Logic:

1. Calculate short period volume EMA (default 12 days)
2. Calculate long period volume EMA (default 26 days)
3. Calculate PVO as the percentage difference between short and long EMA
4. Calculate signal line EMA on PVO (default 9 days)
5. Calculate histogram as difference between PVO and signal line
6. Go short when signal line crosses above PVO, go long when crosses below
7. Option to reverse trade direction
8. Color bars based on signal

The strategy forms PVO indicator through double EMA composition and uses a signal line to identify volume trend changes to anticipate potential price direction. Unlike regular double EMA, PVO focuses more on the percentage difference in volume for clearer judgement of volume increase/decrease.

Advantages:

1. Utilize volume changes to determine future price trends as an early warning
2. Simple and practical double EMA structure with flexible parameter tuning
3. Visualized color bars for intuitive trend judgment and easy operation
4. Signal line reduces false signals and improves stability
5. Optional reverse trading enriches strategy usage
6. Applicable for mid-to-long term trends and short-term trading

This strategy fully leverages the indicative effect of volume changes on price action. Compared to a single indicator, the PVO structure is more stable with customizable parameters to judge volume trend changes and detect potential price direction in advance. The intuitive color differentiation strengthens trend decision-making, and the reverse trading option makes it a versatile volume-based strategy.

Risks:

1. Volume indicator lags price signal and may diverge
2. Improper EMA parameter setting may misjudge market state
3. Reverse trading needs caution, can increase loss
4. Volume change alone cannot determine specific entry point 
5. Volume does not fully predict price, needs combining with other indicators

Volume changes often lag behind price action, and PVO may give a wrong signal when prices approach the end of a trend. Incorrect parameter settings can also affect judgment accuracy. Caution is needed during reverse trading as trends may continue. Volume alone cannot determine precise entry points and requires auxiliary indicators for timing. Volume does not fully predict price movements and should be followed with caution.

Optimization:

1. Optimize EMA periods for different products and timeframes
2. Add filter conditions to avoid invalid signals
3. Combine other indicators to confirm entry timing  
4. Add stop loss

Testing and optimizing EMA combinations to find the best periods for trend detection. Adding volume fluctuation thresholds to filter out ineffective signals. Incorporating MACD, KD, etc., for further confirmation of entry points. Setting up stop losses to control single trade losses. These will greatly improve strategy applicability.

Conclusion:

The Percentage Volume Oscillator strategy judges volume trend changes by calculating the percentage difference between volume EMAs to anticipate potential price direction. It adopts a simple and effective double EMA structure to measure volume fluctuations, and uses intuitive color coding to enhance visual effects. The flexible reverse trading option and parameter settings make it suitable for both mid-to-long term and short-term trading. However, as the volume indicator lags behind price signals and cannot determine precise entry points, parameters and integration with other indicators need optimization to improve strategy performance.

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|12|LengthShortEMA|
|v_input_2|26|LengthLongEMA|
|v_input_3|9|LengthSignalEMA|
|v_input_4|false|Trade reverse|


> Source (PineScript)

```pinescript
//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 27/09/2017
// The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume. 
// PVO measures the difference between two volume-based moving averages as a percentage of the larger moving average to gauge shifts in volume trends.
study("Percentage-Volume-Oscillator-Strategy", shorttitle="PVO")

// Input parameters
short_ema_len = input(12, title="LengthShortEMA")
long_ema_len = input(26, title="LengthLongEMA")
signal_ema_len = input(9, title="LengthSignalEMA")
trade_reverse = input(false, title="Trade reverse", type=bool)

// Calculating PVO
short_ema = ema(volume, short_ema_len)
long_ema = ema(volume, long_ema_len)
pvo = (short_ema - long_ema) / long_ema * 100

// Calculating signal line EMA
signal_ema = ema(pvo, signal_ema_len)

// Plotting histogram
histogram(pvo - signal_ema, color=if pvo > signal_ema then green else red)

// Trading logic
long_condition = crossover(signal_ema, pvo)
short_condition = crossunder(signal_ema, pvo)

plotshape(series=long_condition, title="Long Signal", location=location.belowbar, color=limegreen, style=shape.triangleup, text="BUY")
plotshape(series=short_condition, title="Short Signal", location=location.abovebar, color=crimson, style=shape.triangledown, text="SELL")

if (long_condition and not trade_reverse)
    strategy.entry("Long", strategy.long)

if (short_condition and not trade_reverse)
    strategy.entry("Short", strategy.short)

// Optional reverse trading
if (trade_reverse and long_condition)
    strategy.close("Long")
    
if (trade_reverse and short_condition) 
    strategy.close("Short")
```

This PineScript code implements the Percentage Volume Oscillator (PVO) strategy with customizable parameters for EMA lengths and an option to trade in reverse. The script calculates PVO, signals its trend direction using a histogram, and triggers entry orders based on crossovers of the signal line and PVO.