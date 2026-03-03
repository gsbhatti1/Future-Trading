> Name

Momentum-Reversal-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/784d7d70c8e6c93103.png)
[trans]
# 

## Overview

This strategy combines the 123 reversal pattern and Ease of Movement (EOM) to trade at turning points. The 123 reversal pattern generates signals when the price forms specific patterns over three consecutive days. The EOM strategy utilizes changes in price and volume to gauge market momentum. The combination of both strategies considers technical patterns as well as momentum, improving the accuracy of trading signals.

## Strategy Logic

The strategy consists of two components:

1. 123 Reversal Pattern

  - Use Stoch to identify overbought and oversold levels
  - Go short when price falls for two consecutive days and Stoch fast line is above slow line
  - Go long when price rises for two consecutive days and Stoch fast line is below slow line

2. Ease of Movement

  - Calculate the midpoint of the previous day’s range
  - Calculate the change in the midpoint relative to the previous day
  - Calculate the ratio of midpoint move and volume
  - Ratio above threshold indicates bullish, below threshold bearish

The strategy goes long when EOM and 123 signals align on the long side, and goes short when signals align on the short side.

## Advantage Analysis

The advantages of this strategy:

1. Combines price patterns and momentum for better signal accuracy

2. 123 pattern catches turning points, EOM gauges trend momentum, two complement each other

3. Stoch avoids whipsaws during consolidation

4. Simple and easy to implement

5. Customizable parameters for different market environments

## Risk Analysis

The risks to consider:

1. Overly reliant on parameter settings, improper settings may lead to overtrading or missing trades

2. Many filters may generate too few signals

3. EOM sensitive to volatility, may generate false signals

4. Live performance weaker than backtest, need to control position sizing

5. Only suitable for trending stocks, not ranging markets

## Optimization Directions

The strategy can be improved by:

1. Optimizing parameters to balance frequency and quality of signals

2. Adding stop loss to control single trade loss

3. Adding trend filter to avoid counter-trend trades

4. Incorporating position sizing based on volatility

5. Using machine learning to dynamically optimize parameters

## Conclusion

This strategy integrates price patterns and momentum for high practical value. But trading frequency, loss control, and counter-trend risks need to be managed. Further improvements in parameters, stop loss, trend filtering can enhance stability and profitability. The logic is clear and easy to implement for quant traders.

||


## Overview

This strategy combines the 123 reversal pattern and Ease of Movement (EOM) to trade at turning points. The 123 reversal pattern generates signals when the price forms specific patterns over three consecutive days. The EOM strategy utilizes changes in price and volume to gauge market momentum. The combination of both strategies considers technical patterns as well as momentum, improving the accuracy of trading signals.

## Strategy Logic

The strategy consists of two components:

1. 123 Reversal Pattern

  - Use Stoch to identify overbought and oversold levels
  - Go short when price falls for two consecutive days and Stoch fast line is above slow line
  - Go long when price rises for two consecutive days and Stoch fast line is below slow line

2. Ease of Movement

  - Calculate the midpoint of the previous day’s range
  - Calculate the change in the midpoint relative to the previous day
  - Calculate the ratio of midpoint move and volume
  - Ratio above threshold indicates bullish, below threshold bearish

The strategy goes long when EOM and 123 signals align on the long side, and goes short when signals align on the short side.

## Advantage Analysis

The advantages of this strategy:

1. Combines price patterns and momentum for better signal accuracy

2. 123 pattern catches turning points, EOM gauges trend momentum, two complement each other

3. Stoch avoids whipsaws during consolidation

4. Simple and easy to implement

5. Customizable parameters for different market environments

## Risk Analysis

The risks to consider:

1. Overly reliant on parameter settings, improper settings may lead to overtrading or missing trades

2. Many filters may generate too few signals

3. EOM sensitive to volatility, may generate false signals

4. Live performance weaker than backtest, need to control position sizing

5. Only suitable for trending stocks, not ranging markets

## Optimization Directions

The strategy can be improved by:

1. Optimizing parameters to balance frequency and quality of signals

2. Adding stop loss to control single trade loss

3. Adding trend filter to avoid counter-trend trades

4. Incorporating position sizing based on volatility

5. Using machine learning to dynamically optimize parameters

## Conclusion

This strategy integrates price patterns and momentum for high practical value. But trading frequency, loss control, and counter-trend risks need to be managed. Further improvements in parameters, stop loss, trend filtering can enhance stability and profitability. The logic is clear and easy to implement for quant traders.

||


> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|4000|BuyZone|
|v_input_6|-4000|SellZone|
|v_input_7|false|Trade reverse|


> Source (PineScript)

```pinescript
//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 14/04/2020
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
// This indicator gauges the magnitude of price and volume movement. 
// The indicator returns both positive and negative values where a 
// positive value means the market has moved up from yesterday's value 
// and a negative value means the market has moved down. A large positive 
// or large negative value indicates a large move in price and/or lighter 
// volume. A small positive or small negative value indicates a small move 
// in price and/or heavier volume.
// A positive or negative numeric value. A positive value means the market 
// has moved up from yesterday's value, whereas, a negative value means the 
// market has moved down. 
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff
```