<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Buy-Sell-on-Candle-Close-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/185a3e5722294581cba.png)
[trans]

## Overview

This strategy triggers buy/sell signals by comparing the closing prices of the current candle and previous candle. 

Specifically, if the current candle closes above the highest price of the previous candle, a buy signal is triggered. If the current candle closes below the lowest price of the previous candle, a sell signal is triggered.

## Strategy Logic

1. Get historical highest and lowest prices of the specified timeframe (e.g., daily, hourly).
2. Calculate stop loss and take profit distances:
   - Stop loss distance = Previous candle highest - Previous candle lowest
   - Take profit distance = Stop loss distance * 3 (set to a 1:3 risk-reward ratio)
3. Determine the relationship between current close and previous high/low:
   - If current close > previous candle highest, trigger buy signal
   - If current close < previous candle lowest, trigger sell signal
4. Set stop loss and take profit after entry:
   - After buying, set stop loss at previous candle lowest - stop loss distance, take profit at previous candle highest + take profit distance
   - After selling, set stop loss at previous candle highest + stop loss distance, take profit at previous candle lowest - take profit distance

The above is the basic trading logic of this strategy.

## Advantage Analysis

- The strategy idea is simple and clear, easy to understand and implement.
- Use candlestick information to determine trend direction.
- Have a stop loss and take profit mechanism to control risk.

## Risk Analysis

- Judgment based solely on one timeframe may generate more false signals.
- Does not consider more factors such as volume change, volatility, etc.
- Stop loss and take profit settings could be inappropriate; distances that are too wide or too narrow both pose risks.

## Optimization Directions

- Combine more factors to confirm entry signal, like volume, moving average, etc.
- Optimize stop loss and take profit algorithms for more reasonable stop loss and sufficient take profit.
- Parameter tuning may be needed for different products.
- Longer timeframe can be tested.

## Summary

The strategy idea is simple and clear overall. Using candlestick closing price to determine trend direction and also has a stop loss/take profit mechanism to control risk, it can serve as a basic strategy for stocks and crypto trading. But with judgment solely based on one timeframe, it tends to generate false signals more easily. There is still much room for improvement by incorporating more factors and tuning parameters to enhance the performance of the strategy.

||

## Overview

This strategy triggers buy/sell signals by comparing the closing prices of the current candle and previous candle. 

Specifically, if the current candle closes above the highest price of the previous candle, a buy signal is triggered. If the current candle closes below the lowest price of the previous candle, a sell signal is triggered.

## Strategy Logic

1. Get historical highest and lowest prices of the specified timeframe (e.g., daily, hourly).
2. Calculate stop loss and take profit distances:
   - Stop loss distance = Previous candle highest - Previous candle lowest
   - Take profit distance = Stop loss distance * 3 (set to a 1:3 risk-reward ratio)
3. Determine the relationship between current close and previous high/low:
   - If current close > previous candle highest, trigger buy signal
   - If current close < previous candle lowest, trigger sell signal
4. Set stop loss and take profit after entry:
   - After buying, set stop loss at previous candle lowest - stop loss distance, take profit at previous candle highest + take profit distance
   - After selling, set stop loss at previous candle highest + stop loss distance, take profit at previous candle lowest - take profit distance

The above is the basic trading logic of this strategy.

## Advantage Analysis

- The strategy idea is simple and clear, easy to understand and implement.
- Use candlestick information to determine trend direction.
- Have a stop loss and take profit mechanism to control risk.

## Risk Analysis

- Judgment based solely on one timeframe may generate more false signals.
- Does not consider more factors such as volume change, volatility, etc.
- Stop loss and take profit settings could be inappropriate; distances that are too wide or too narrow both pose risks.

## Optimization Directions

- Combine more factors to confirm entry signal, like volume, moving average, etc.
- Optimize stop loss and take profit algorithms for more reasonable stop loss and sufficient take profit.
- Parameter tuning may be needed for different products.
- Longer timeframe can be tested.

## Summary

The strategy idea is simple and clear overall. Using candlestick closing price to determine trend direction and also has a stop loss/take profit mechanism to control risk, it can serve as a basic strategy for stocks and crypto trading. But with judgment solely based on one timeframe, it tends to generate false signals more easily. There is still much room for improvement by incorporating more factors and tuning parameters to enhance the performance of the strategy.

||

> Source (PineScript)

```pinescript
//@version=5
strategy("Buy/Sell on Candle Close", overlay=true)

var float prevLowest = na
var float prevHighest = na
var float slDistance = na
var float tpDistance = na

// Specify the desired timeframe here (e.g., "D" for daily, "H" for hourly, etc.)
timeframe = "D"

// Fetching historical data for the specified timeframe
pastLow = request.security(syminfo.tickerid, timeframe, low, lookahead=barmerge.lookahead_on)
pastHigh = request.security(syminfo.tickerid, timeframe, high, lookahead=barmerge.lookahead_on)

if bar_index > 0
    prevLowest := pastLow[1]
    prevHighest := pastHigh[1]

currentClose = close

if not na(prevLowest) and not na(prevHighest)
    slDistance := prevHighest - prevLowest
    tpDistance := 3 * slDistance // Adjusted for a 1:3 risk-reward ratio

// Buy trigger when current close is higher than previous highest
if not na(prevLowest) and not na(prevHighest) and currentClose > prevHighest
    strategy.entry("Buy", strategy.long)
    strategy.exit("Buy TP/SL", "Buy", stop=prevLowest - slDistance, limit=prevHighest + tpDistance)

// Sell trigger when current close is lower than previous lowest
if not na(prevLowest) and not na(prevHighest) and currentClose < prevLowest
    strategy.entry("Sell", strategy.short)
    strategy.exit("Sell TP/SL", "Sell", stop=prevHighest + slDistance, limit=prevLowest - tpDistance)

plot(prevLowest, color=color.blue, title="Previous Lowest")
plot(prevHighest, color=color.red, title="Previous Highest")

```

> Detail

https://www.fmz.com/strategy/438017

> Last Modified

2024-01-08 11:11:18