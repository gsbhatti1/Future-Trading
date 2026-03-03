> Name

Double-K-Crossbow-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/144fa1e1f200cad1f22.png)

[trans]


Overview: The Double K Crossbow strategy combines the 123 Reversal strategy and Martin Pring's Special K strategy to leverage their respective advantages. This strategy aims to generate more accurate buy and sell signals by utilizing the strengths of both strategies.

Strategy Logic:

The Double K Crossbow consists of two parts:

1. 123 Reversal Strategy: It identifies buy and sell signals based on the reversal of closing prices over two consecutive days, combined with stochastic oscillator readings. A buy signal is generated when the close is higher than the previous close for two days and the stochastic indicator is below 50, indicating consolidation. Conversely, a sell signal is generated when the close is lower than the previous close for two days and the stochastic indicator is above 50, indicating distribution.

2. Martin Pring's Special K Strategy: It uses a composite cyclical indicator formed by stacking rate-of-change values from different timeframes. Buy signals are generated when the indicator crosses above its moving average, while sell signals are generated when it crosses below.

The Double K Crossbow consolidates the signals from both strategies, requiring agreement to trigger actual trades. This leverages the timing strengths of each strategy and avoids false signals.

Advantage Analysis:

- Combines signals from two strategies for more reliable trade entry and exit. Avoids false trades.
- The 123 Reversal Strategy can catch short-term reversals while Martin Pring's Special K Strategy judges long-term trends, combining both short and long-term considerations.
- Multi-timeframe rate-of-change values provide insight into market cycles.
- Optimizable stochastic parameters adapt to different market conditions.

Risk Analysis:

- Consolidating signals may miss some buy/sell points and lag short-term moves.
- Strategies can disagree during outlier events, requiring judgment on direction.
- Requires monitoring and optimizing parameters for both strategies, increasing complexity.
- Incorrect optimization of short and long-term parameters may miss cycle turning points.

Enhancement Opportunities:

- Test different parameter combinations to find optimal settings.
- Add stop loss module to limit losses.
- Add position sizing module to adjust with market conditions.
- Incorporate machine learning for more robust signal modeling.
- Add adaptive optimization to dynamically track market rhythms.

Conclusion:

The Double K Crossbow successfully combines the strengths of reversal and cyclical strategies for quality signals and multi-timeframe profit opportunities. The novel approach is worth further testing and optimization as a stable strategy. But risk management and parameter tuning remain essential for consistent gains in ever-changing markets.


||


Overview: The Double K Crossbow strategy combines the 123 Reversal strategy and Martin Pring's Special K strategy to take advantage of reversal signals and cyclical indicators. It aims to generate more accurate buy and sell signals by leveraging the strengths of both strategies.

Strategy Logic:

The Double K Crossbow consists of two parts:

1. 123 Reversal Strategy: It identifies buy and sell signals based on the reversal of closing prices over two consecutive days, combined with stochastic oscillator readings. A buy signal is generated when the close is higher than the previous close for two days and the stochastic indicator is below 50, indicating consolidation. Conversely, a sell signal is generated when the close is lower than the previous close for two days and the stochastic indicator is above 50, indicating distribution.

2. Martin Pring's Special K Strategy: It uses a composite cyclical indicator formed by stacking rate-of-change values from different timeframes. Buy signals are generated when the indicator crosses above its moving average, while sell signals are generated when it crosses below.

The Double K Crossbow consolidates the signals from both strategies, requiring agreement to trigger actual trades. This leverages the timing strengths of each strategy and avoids false signals.

Advantage Analysis:

- Combines signals from two strategies for more reliable trade entry and exit. Avoids false trades.
- The 123 Reversal Strategy can catch short-term reversals while Martin Pring's Special K Strategy judges long-term trends, combining both short and long-term considerations.
- Multi-timeframe rate-of-change values provide insight into market cycles.
- Optimizable stochastic parameters adapt to different market conditions.

Risk Analysis:

- Consolidating signals may miss some buy/sell points and lag short-term moves.
- Strategies can disagree during outlier events, requiring judgment on direction.
- Requires monitoring and optimizing parameters for both strategies, increasing complexity.
- Incorrect optimization of short and long-term parameters may miss cycle turning points.

Enhancement Opportunities:

- Test different parameter combinations to find optimal settings.
- Add stop loss module to limit losses.
- Add position sizing module to adjust with market conditions.
- Incorporate machine learning for more robust signal modeling.
- Add adaptive optimization to dynamically track market rhythms.

Conclusion:

The Double K Crossbow successfully combines the strengths of reversal and cyclical strategies for quality signals and multi-timeframe profit opportunities. The novel approach is worth further testing and optimization as a stable strategy. But risk management and parameter tuning remain essential for consistent gains in ever-changing markets.


> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|--- 123 Reversal ---|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|--- Martin Pring's ---|
|v_input_7|10|Smooth|
|v_input_8_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_9|false|Trade reverse|


> Source (PineScript)

```pinescript
//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 17/02/2021
// This is a combo strategy to get a cumulative signal.
//
// First Strategy:
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market if close price is higher than the previous close 
// during two days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market if close price is lower than the previous close price 
// during two days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Second Strategy:
// Martin Pring's Special K is a cyclical indicator created by Martin Pring. 
// His method combines short-term, intermediate, and long-term velocity 
// into one complete series. Useful tool for Long Term Investors
// Modified for any source.
//
// WARNING:
// - For purpose of education only
// - This script changes bar colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing)
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > Level, 1,
	         iff(close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < Level, -1, nz(pos[1], 0)))
    pos

MPSK(a, sources) =>
    pos = 0.0
    roc1 = (sma(roc(sources