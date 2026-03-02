> Name

Double-Reversal-RSI-Momentum-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy combines the 123 reversal pattern and RSI momentum strategies to filter signals for high-probability entries at trend reversal points.

## Principle Analysis

### 123 Reversal Pattern

This strategy is derived from Ulf Jensen's book "How I Tripled My Money in the Futures Market" on page 183. It identifies potential trend reversals during consolidation phases.

Specifically, it goes long when the close price is higher than the previous day's close for two consecutive days and the 9-period Slow K line is below 50; it goes short when the close price is lower than the previous day's close for two consecutive days and the 9-period Fast K line is above 50.

So essentially, it uses the stochastic indicator's golden cross and death cross to determine potential reversals.

### RSI Momentum Strategy

This strategy utilizes the ROC function to calculate price rate of change, then constructs an RSI indicator based on this rate of change to identify momentum trends. 

It goes long when RSI is below the buy zone, indicating accelerating upside momentum; it goes short when RSI is above the sell zone, indicating accelerating downside momentum.

### Advantages

- The 123 reversal pattern can identify potential reversal points after consolidation.
- The RSI momentum filter effectively eliminates false breakouts.
- Accumulated signals from both strategies provide strong entry signals.

### Risks

- The 123 pattern is prone to bull traps or false breakouts, requiring additional filtering.
- RSI remains price-based and cannot fully avoid whipsaws.
- Dual signal accumulation may miss optimal entry points.

Possible ways to reduce risks:

1. Adjust Stochastic indicator parameters to use longer periods to define trends.
2. Modify RSI parameters to use wider buy/sell zones.
3. Consider using a single signal for entries only.

## Optimization Directions

- Test ROC period parameters to find more suitable values for specific products.
- Test 123 pattern logic, such as adjusting K line fast and slow parameters.
- Test RSI zone values to determine optimal buy/sell ranges.
- Try other indicators like MACD to replace Stochastic.
- Evaluate the effect of using just one strategy signal.

## Conclusion

This strategy improves entry accuracy at trend reversals by requiring two confirming reversal signals. The 123 pattern identifies reversals, and RSI momentum verifies their validity. It is easy to optimize parameters for different products and preferences but be cautious about missing entries from dual signal accumulation. Overall, it provides an effective framework for identifying reversal trends.

||

## Overview

This strategy combines the 123 reversal pattern and RSI momentum strategies to filter signals for high-probability entries at trend reversal points.

## Principles

### 123 Reversal Pattern 

This strategy is from the book "How I Tripled My Money in the Futures Market" by Ulf Jensen, Page 183. It identifies potential trend reversals during consolidation phases.

Specifically, it goes long when the close price is higher than the previous day's close for two consecutive days and the 9-period Slow K line is below 50; it goes short when the close price is lower than the previous day's close for two consecutive days and the 9-period Fast K line is above 50.

So essentially, it uses the stochastic indicator's golden cross and death cross to determine potential reversals.

### RSI Momentum Pattern

This strategy utilizes the ROC function to calculate price rate of change, then constructs an RSI indicator based on this rate of change to identify momentum trends. 

It goes long when RSI is below the buy zone, indicating accelerating upside momentum; it goes short when RSI is above the sell zone, indicating accelerating downside momentum.

### Advantages

- The 123 reversal pattern can identify potential reversal points after consolidation.
- The RSI momentum filter effectively eliminates false breakouts.
- Accumulated signals from both strategies provide strong entry signals.

### Risks

- The 123 pattern is prone to bull traps or false breakouts, requiring additional filtering.
- RSI remains price-based and cannot fully avoid whipsaws.
- Dual signal accumulation may miss optimal entry points.

Possible ways to reduce risks:

1. Tune Stochastic parameters to use longer periods to define trends.
2. Adjust RSI parameters to use wider buy/sell zones.
3. Consider using just one signal for entries only.

## Optimization Directions

- Test ROC period parameters to find more suitable values for specific products.
- Test 123 pattern logic, such as adjusting K line fast and slow parameters.
- Test RSI zone values to determine optimal buy/sell ranges.
- Try other indicators like MACD to replace Stochastic.
- Evaluate the effect of using just one strategy signal.

## Conclusion

This strategy improves entry accuracy at trend reversals by requiring two confirming reversal signals. The 123 pattern identifies reversals, and RSI momentum verifies their validity. It is easy to optimize parameters for different products and preferences but be cautious about missing entries from dual signal accumulation. Overall, it provides an effective framework for identifying reversal trends.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- RSI based on ROC ----|
|v_input_7|20|RSILength|
|v_input_8|20|ROCLength|
|v_input_9|30|BuyZone|
|v_input_10|70|SellZone|
|v_input_11|false|Trade reverse|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-26 00:00:00
end: 2023-09-25 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 17/06/2021
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
// This is the new-age indicator which is version of RSI calculated upon 
// the Rate-of-change indicator.
// The name "Relative Strength Index" is slightly misleading as the RSI 
// does not compare the relative strength of two securities, but rather 
// the internal strength of a single security. A more appropriate name 
// might be "Internal Strength Index." Relative strength charts that compare 
// two market indices, which are often referred to as Comparative Relative Strength.
// And in its turn, the Rate-of-Change ("ROC") indicator displays the difference 
// between the current price and the price x-time periods ago. The difference can 
// be displayed in either points or as a percentage. The Momentum indicator displays 
// the same information, but expresses it as a ratio.
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] > close[3] and vSlow < 50, 1, pos)
    pos := iff(close[2] < close[3] and vFast > 50, -1, pos)
    
RSIMomentum(RSILength, ROCLength, BuyZone, SellZone) =>
    roc = change(close, ROCLength)
    rsi = rsi(roc, RSILength)
    tradeSignal = iff(rsi < BuyZone, 1, iff(rsi > SellZone, -1, 0))
    
strategy("Double Reversal RSI Momentum Strategy", overlay=true)
    strategy.entry("Long Entry", strategy.long, when=pos == 1 and tradeSignal == 1)
    strategy.close("Long Exit", when=pos == -1 and tradeSignal == -1)

```

Note: The PineScript code has been adjusted to match the logic described in the text.