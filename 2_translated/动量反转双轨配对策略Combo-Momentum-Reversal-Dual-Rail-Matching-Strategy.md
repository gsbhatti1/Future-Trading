> Name

Combo-Momentum-Reversal-Dual-Rail-Matching-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c673feb61bc6c01e2b.png)
[trans]

## Overview

This strategy integrates multiple technical indicators to implement momentum reversal and dual-rail matching, generating trading signals. The strategy uses the 123 pattern to determine reversal points and matches these with the ergodic CSI indicator to achieve trend tracking. This approach aims to capture medium-short term trends and generate higher profits.

## Principles

The strategy comprises two parts:

1. **123 Pattern for Determining Reversal Points**
2. **Ergodic CSI Indicator for Generating Matching Signals**

### 123 Pattern Logic
- The pattern is based on the close prices of recent three bars.
- **Buy Signal**: If the close price of the third bar rises compared to the previous two, and both fast and slow stochastics are below 50.
- **Sell Signal**: If the close price of the third bar falls compared to the previous two, and both fast and slow stochastics are above 50.

### Ergodic CSI Indicator
- This indicator considers multiple factors such as price, true range, trend indicators, etc., to comprehensively determine market conditions and generate buy/sell zones.
- A buy signal is generated when the indicator rises above the buy zone. A sell signal is generated when it falls below the sell zone.

Finally, the reversal signals from the 123 pattern and the zone signals from the ergodic CSI are "ANDed" to produce the final strategy signal.

## Advantages

- Captures medium-short term trends with high profit potential.
- Effective in catching turning points using reversal patterns.
- Dual-rail matching helps reduce false signals.

## Risks

- Individual stock may diverge, leading to stop loss.
- Reversal patterns susceptible to impact from range-bound markets.
- Limited parameter optimization space; performance fluctuates significantly.

## Optimization Directions

- Optimize parameters to improve strategy profitability.
- Add stop-loss logic to minimize single trade losses.
- Incorporate multi-factor models for better stock selection.

## Conclusion

This strategy effectively tracks medium-short term trends by combining reversal patterns and dual-rail matching. Compared to using a single technical indicator, it offers higher stability and profit levels. Future improvements will focus on further parameter optimization and adding stop-loss and stock-selection modules to reduce drawdowns and enhance overall performance.


||

## Overview

This strategy integrates multiple technical indicators to implement momentum reversal and dual-rail matching, generating trading signals. The strategy uses the 123 pattern to determine reversal points and matches these with the ergodic CSI indicator to achieve trend tracking. This approach aims to capture medium-short term trends and generate higher profits.

## Principles

The strategy comprises two parts:

1. **123 Pattern for Determining Reversal Points**
2. **Ergodic CSI Indicator for Generating Matching Signals**

### 123 Pattern Logic
- The pattern is based on the close prices of recent three bars.
- **Buy Signal**: If the close price of the third bar rises compared to the previous two, and both fast and slow stochastics are below 50.
- **Sell Signal**: If the close price of the third bar falls compared to the previous two, and both fast and slow stochastics are above 50.

### Ergodic CSI Indicator
- This indicator considers multiple factors such as price, true range, trend indicators, etc., to comprehensively determine market conditions and generate buy/sell zones.
- A buy signal is generated when the indicator rises above the buy zone. A sell signal is generated when it falls below the sell zone.

Finally, the reversal signals from the 123 pattern and the zone signals from the ergodic CSI are "ANDed" to produce the final strategy signal.

## Advantages

- Captures medium-short term trends with high profit potential.
- Effective in catching turning points using reversal patterns.
- Dual-rail matching helps reduce false signals.

## Risks

- Individual stock may diverge, leading to stop loss.
- Reversal patterns susceptible to impact from range-bound markets.
- Limited parameter optimization space; performance fluctuates significantly.

## Optimization Directions

- Optimize parameters to improve strategy profitability.
- Add stop-loss logic to minimize single trade losses.
- Incorporate multi-factor models for better stock selection.

## Conclusion

This strategy effectively tracks medium-short term trends by combining reversal patterns and dual-rail matching. Compared to using a single technical indicator, it offers higher stability and profit levels. Future improvements will focus on further parameter optimization and adding stop-loss and stock-selection modules to reduce drawdowns and enhance overall performance.


||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|32|r|
|v_input_6|true|LengthECSI|
|v_input_7|true|BigPointValue|
|v_input_8|5|SmthLen|
|v_input_9|0.06|SellZone|
|v_input_10|0.02|BuyZone|
|v_input_11|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-24 00:00:00
end: 2023-11-23 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 22/07/2020
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market, if close price is lower than the previous close price 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Second strategy
// This is one of the techniques described by William Blau in his book 
// "Momentum, Direction and Divergence" (1995). If you like to learn more, 
// we advise you to read this book. His book focuses on three key aspects 
// of trading: momentum, direction and divergence. Blau, who was an electrical 
// engineer before becoming a trader, thoroughly examines the relationship between 
// price and momentum in step-by-step examples. From this grounding, he then looks 
// at the deficiencies in other oscillators and introduces some innovative techniques, 
// including a fresh twist on Stochastics. On directional issues, he analyzes the 
// intricacies of ADX and offers a unique approach to help define trending and 
// non-trending periods.
// This indicator plots Ergotic CSI and smoothed Ergotic CSI to filter out noise. 
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > Level, 1,
             iff(close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < Level, -1, nz(pos[1], 0))) 
	pos

fADX(Len) =>
    up = change(high)
    down = -change(low)
    trur = rma(tr, Len)
    plus = fixnan(100 * rma(up > down and
```