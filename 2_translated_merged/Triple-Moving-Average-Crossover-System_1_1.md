<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Triple Moving Average Crossover System

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

The Triple Moving Average Crossover System is a typical trend-following stock trading strategy. It uses the crossover of three moving averages with different time lengths as buy and sell signals. A buy signal is generated when the short-term moving average crosses above the medium-term moving average, and the medium-term moving average crosses above the long-term moving average. A sell signal is generated when the short-term moving average crosses below the medium-term moving average, and the medium-term moving average crosses below the long-term moving average.

## Strategy Principle

This strategy is based on three moving averages: the long-term moving average ma1, the medium-term moving average ma2, and the short-term moving average ma3. First, these three lines are calculated:

```pine
length1 = input(18,'长线') 
length2 = input(9,'中线')
length3 = input(4,'短线')

ma1 := sma(close,length1) 
ma2 := sma(close,length2)
ma3 := sma(close,length3)
```

Here, length1, length2, and length3 respectively define the time lengths of the three moving averages. The sma function calculates the simple moving average of the closing price over the corresponding length.

Then, the crossovers of the three moving averages are used to determine buying and selling opportunities:

```pine
if ma2 > ma1 and ma3 > ma3[1] 
    strategy.entry("Long", strategy.long)

if ma2 < ma1 and ma3 < ma3[1]
    strategy.entry("Short", strategy.short) 
```

A long signal is issued when the medium-term line ma2 crosses above the long-term line ma1, and the short-term line ma3 crosses above the previous cycle's ma3. A short signal is issued when the medium-term line ma2 crosses below the long-term line ma1, and the short-term line ma3 crosses below the previous cycle's ma3.

## Strategy Advantages

- Using three moving averages allows for a clearer judgment of trend changes.
- The combination of long and short periods can filter out some short-term market noise and lock onto longer-term trends.
- The rules are simple and easy to operate.
- The parameters of the three moving averages can be adjusted to adapt to different market conditions.

## Strategy Risks

- Buy and sell points are confirmed after the fact and cannot completely avoid losses.
- Multiple false signals may occur when the stock price oscillates near the moving averages.
- If the long-term line is too long, it will miss turning points in the trend. If the short-term line is too short, frequent trades will occur due to noise.
- It does not handle sideways markets well.

These risks can be reduced by appropriately optimizing parameters and combining other indicators as filtering conditions.

## Strategy Optimization Directions 

- Different combinations of length parameters can be tested to find the best parameters.
- Stop-losses can be added to control losses.
- Other indicators can be added to judge strength and divergence to avoid misjudgments, such as MACD, KD, etc.
- Appropriate take-profit strategies can be chosen based on actual conditions.

## Summary

The Triple Moving Average Crossover strategy belongs to a simple and practical trend-following strategy. It determines changes in market trends based on the crossovers of three moving averages to generate trading signals. The advantages of this strategy are its simple rules and effective trend tracking, making it suitable for medium to long-term operations. However, there are certain risks of false signals and drawdowns. These can be improved by parameter optimization and adding auxiliary indicators to adapt to different market environments. Overall, the Triple Moving Average Crossover strategy is a basic introductory strategy for quantitative trading and is an excellent starting point for learning algorithmic trading.


||


## Overview

The Triple Moving Average Crossover System is a typical trend-following stock trading strategy. It uses the crossover of three moving averages of different time lengths as buy and sell signals. When the short period moving average crosses above the medium period moving average, and the medium period moving average crosses above the long period moving average, a buy signal is generated. When the short period moving average crosses below the medium period moving average, and the medium period moving average crosses below the long period moving average, a sell signal is generated.

## Strategy Logic

The strategy is based on three moving averages: the long period moving average ma1, the medium period moving average ma2 and the short period moving average ma3. First it calculates these three lines:

```pine
length1 = input(18,'长线')  
length2 = input(9,'中线')
length3 = input(4,'短线')

ma1 := sma(close,length1)
ma2 := sma(close,length2) 
ma3 := sma(close,length3)
```

Where length1, length2 and length3 define the time lengths of the three moving averages. The sma function calculates the simple moving average of the close price over the corresponding length.

It then uses the crossover of the three moving averages to determine entries and exits:

```pine 
if ma2 > ma1 and ma3 > ma3[1]
    strategy.entry("Long", strategy.long)

if ma2 < ma1 and ma3 < ma3[1] 
    strategy.entry("Short", strategy.short)
```

When the medium term ma2 crosses above the long term ma1, and the short term ma3 crosses above the previous period's ma3, a long signal is triggered. When the medium term ma2 crosses below the long term ma1, and the short term ma3 crosses below the previous period's ma3, a short signal is triggered.

## Advantages of the Strategy

- Using three moving averages can clearly identify trend changes.
- The combination of long and short periods filters out some short term market noise and locks in longer term trends. 
- Simple rules make it easy to implement.
- Parameters can be adjusted to adapt to different market environments.

## Risks of the Strategy

- Entries and exits are identified in hindsight and cannot completely avoid losses.
- Whipsaws occur when the price oscillates around moving averages.
- Long period line that is too long may miss trend turning points. Short period line that is too short may trigger frequent trades due to noise.
- Does not handle ranging markets very well.

These risks can be reduced through appropriate parameter optimization, adding filters with other indicators etc.

## Improvement Directions

- Backtest different parameter combinations to find optimal values.
- Add stop loss to control losses.
- Add other indicators to judge momentum and divergence to avoid false signals. E.g. MACD, KD etc.
- Choose suitable profit taking strategy according to actual situation.

## Summary 

The Triple Moving Average Crossover strategy is a simple and practical trend following strategy. It identifies changes in trend direction based on the crossover of three moving averages to generate trading signals. The advantages of this strategy are its simple rules and effective tracking of trends, making it suitable for medium to long term trading. However, there are also risks of false signals and drawdowns. The strategy can be improved by optimizing parameters, adding supporting indicators etc. to adapt to different market environments. Overall, the Triple Moving Average Crossover is a foundational algorithmic trading strategy that provides a good starting point for learning quantitative trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|18|Long Period|
|v_input_2|9|Medium Period|  
|v_input_3|4|Short Period|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-08-28 00:00:00
end: 2023-09-27 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © dongyun

//@version=4
strategy("Triple Crossover Revised Mode System", overlay=true)
//strategy.risk.allow_entry_in(strategy.direction.long)
length1 = input(18,'Long Period')
length2 = input(9,'Medium Period')
length3 = input(4,'Short Period')

ma1 =0.0
ma2 = 0.0
ma3 = 0.0

ma1 := sma(close,length1)
ma2 := sma(close,length2)
ma3 := sma(close,length3)

plot(ma1)
plot(ma2)
plot(ma3)

if ma2 > ma1 and ma3 > ma3[1]
	strategy.entry("Long", strategy.long, when=strategy.position_size <= 0)

if ma2 < ma1 and ma3 < ma3[1]
	strategy.entry("Short", strategy.short, when=strategy.position_size > 0)
```

> Detail

https://www.fmz.com/strategy/428089

> Last Modified

2023-09-28 15:33:14