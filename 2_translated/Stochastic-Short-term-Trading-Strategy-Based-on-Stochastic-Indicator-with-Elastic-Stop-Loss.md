> Name

Short-term-Trading-Strategy-Based-on-Stochastic-Indicator-with-Elastic-Stop-Loss

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy uses the Stochastic oscillator indicator to determine overbought and oversold market conditions for short-term trading. It goes long when there is a golden cross on the Stochastic indicator, and goes short on a death cross, with elastic stop loss based on previous pivot points to secure profits while controlling risks.

## Strategy Logic

### Entry Logic

The Stochastic oscillator indicator consists of the %K line and %D line. When the %K line crosses above the %D line, a golden cross buy signal is generated. When the %K line crosses below the %D line, a death cross sell signal is triggered. This strategy simply follows the crossovers on the Stochastic indicator to determine entries.

Specifically, when there is a golden cross on the Stochastic indicator, if the %K value is less than 80 (not overbought), a long position will be taken. On a Stochastic death cross, if the %K value is greater than 20 (not oversold), a short position will be initiated.

```pine
GoLong=crossover(k,d) and k<80 
GoShort=crossunder(k,d) and k>20
```

### Stop Loss Logic

This strategy uses an elastic stop loss approach, setting the stop price based on previous pivot points, as shown below:

```pine
piv_high = pivothigh(high,1,1)
piv_low = pivotlow(low,1,1)

stoploss_long=valuewhen(piv_low,piv_low,0) 
stoploss_short=valuewhen(piv_high,piv_high,0)
```

Pivots represent important support and resistance levels. If price breaks through the pivot level, the position will be closed and the stop loss price will "elasticly" follow the changing pivot points.

In addition, the stop price also considers the highest and lowest prices of the current period for further optimization:

```pine
if GoLong
    stoploss_long := low<pl ? low : pl
if GoShort  
    stoploss_short := high>ph ? high : ph   
```

### Advantages

1. Using Stochastic to avoid chasing tops and bottoms;
2. Elastic stop loss follows market changes and optimizes stop price;
3. Stop loss based on pivot point breakout is more effective;
4. Stop price optimization using current highest and lowest prices makes stop more precise.

## Risks and Solutions

1. Risk of false signals from Stochastic
    - Solution: Confirm signals with other indicators to avoid false signals
2. Risk of stop loss being hit and loss increased
    - Solution: Reduce stop distance, or use methods like Chandelier Exit
3. Risk of high trading frequency and commissions
    - Solution: Loosen entry rules to reduce number of trades

## Optimization Directions

1. Optimize stop loss, using methods like Chandelier Exit, trailing stop, oscillating stop loss etc
2. Optimize entry rules with other indicators to avoid Stochastic false signals
3. Optimize profit taking, using trailing profit target, oscillating profit target etc to increase profitability
4. Add position sizing, like fixed quantity per trade, fixed risk percentage etc to control per trade risk
5. Optimize parameters like K, D periods, smoothing etc based on different markets

## Summary

This strategy enters based on Stochastic overbought/oversold and manages risk with elastic stop loss. It has the advantage of avoiding chasing momentum, effective stops, but also has some false signal risks. Future improvements can be made on entries, stops, exits, risk management etc.

|||

## Overview

This strategy uses the Stochastic oscillator indicator to determine overbought and oversold market conditions for short-term trading. It goes long when there is a golden cross on the Stochastic indicator, and goes short on a death cross, with elastic stop loss based on previous pivot points to secure profits while controlling risks.

## Strategy Logic

### Entry Logic

The Stochastic oscillator indicator consists of the %K line and %D line. When the %K line crosses above the %D line, a golden cross buy signal is generated. When the %K line crosses below the %D line, a death cross sell signal is triggered. This strategy simply follows the crossovers on the Stochastic indicator to determine entries.

Specifically, when there is a golden cross on the Stochastic indicator, if the %K value is less than 80 (not overbought), a long position will be taken. On a Stochastic death cross, if the %K value is greater than 20 (not oversold), a short position will be initiated.

```pine
GoLong=crossover(k,d) and k<80 
GoShort=crossunder(k,d) and k>20
```

### Stop Loss Logic

This strategy uses an elastic stop loss approach, setting the stop price based on previous pivot points, as shown below:

```pine
piv_high = pivothigh(high,1,1)
piv_low = pivotlow(low,1,1)

stoploss_long=valuewhen(piv_low,piv_low,0) 
stoploss_short=valuewhen(piv_high,piv_high,0)
```

Pivots represent important support and resistance levels. If price breaks through the pivot level, the position will be closed and the stop loss price will "elasticly" follow the changing pivot points.

In addition, the stop price also considers the highest and lowest prices of the current period for further optimization:

```pine
if GoLong 
    stoploss_long := low<pl ? low : pl
if GoShort  
    stoploss_short := high>ph ? high : ph   
```

### Advantages

1. Using Stochastic to avoid chasing tops and bottoms;
2. Elastic stop loss follows market changes and optimizes stop price;
3. Stop loss based on pivot point breakout is more effective;
4. Stop price optimization using current highest and lowest prices makes stop more precise.

## Risks and Solutions

1. Risk of false signals from Stochastic
    - Solution: Confirm signals with other indicators to avoid false signals
2. Risk of stop loss being hit and loss increased
    - Solution: Reduce stop distance, or use methods like Chandelier Exit
3. Risk of high trading frequency and commissions
    - Solution: Loosen entry rules to reduce number of trades

## Optimization Directions 

1. Optimize stop loss, using methods like Chandelier Exit, trailing stop, oscillating stop loss etc
2. Optimize entry rules with other indicators to avoid Stochastic false signals
3. Optimize profit taking, using trailing profit target, oscillating profit target etc to increase profitability
4. Add position sizing, like fixed quantity per trade, fixed risk percentage etc to control per trade risk
5. Optimize parameters like K, D periods, smoothing etc based on different markets

## Summary

This strategy enters based on Stochastic overbought/oversold and manages risk with elastic stop loss. It has the advantage of avoiding chasing momentum, effective stops, but also has some false signal risks. Future improvements can be made on entries, stops, exits, risk management etc.

|||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|400|TakeProfitLevel|
|v_input_2|10|Entry distance for stop orders|


> Source (PineScript)

```pinescript
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Peter_O

//@version=4
strategy(title="Short-term Trading Strategy Based on Stochastic Indicator with Elastic Stop Loss", overlay=true, default_qty_value=100000)

// This script was created for educational purposes only.
// It is showing how to create pending orders and cancel them
// Together with syntax to send these events through TradingView alerts system
// All the way to brokers for execution

// Inputs
take_profit_level = input(400, title="TakeProfitLevel")
entry_distance = input(10, title="Entry distance for stop orders")

piv_high = pivothigh(high, 1, 1)
piv_low = pivotlow(low, 1, 1)

stoploss_long = valuewhen(piv_low, piv_low[0], 0) 
stoploss_short = valuewhen(piv_high, piv_high[0], 0)

GoLong = crossover(k, d) and k < take_profit_level
GoShort = crossunder(k, d) and k > (100 - take_profit_level)

if GoLong
    strategy.entry("Buy", strategy.long)
    strategy.exit("Take Profit", "Buy", profit = take_profit_level * entry_distance)

if GoShort 
    strategy.entry("Sell", strategy.short)
    strategy.exit("Take Profit", "Sell", profit = (100 - take_profit_level) * entry_distance)

// Placeholder for stop loss logic
```