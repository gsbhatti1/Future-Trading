> Name

Dual-Moving-Average-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1148a4aa63b71da3062.png)

[trans]

## Overview

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two EMA lines with different periods and goes long when the shorter period EMA crosses over the longer period EMA, and goes short when the opposite crossing happens to capture trend reversals.

## Principles  

The core indicators of this strategy are two EMA lines, one is 30-period and the other is 60-period. The two EMA lines are calculated by custom functions in the code:

```pinescript
emaLen1 = emaFuncOne(close, lenMA1)  
emaLen2 = emaFuncTwo(close, lenMA2)
```

The trading signals are generated from the crossing of the two EMA lines:

```pinescript
currentState = if emaLen2 > emaLen1
    0
else 
    1

previousState = if emaLastLen2 > emaLastLen1 
    0  
else
    1

convergence = if currentState != previousState
    1
else 
    0
```

When the shorter period EMA crosses over the longer period EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you should go long. When the shorter period EMA crosses below the longer period EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you should go short.

## Advantage Analysis

The advantages of this strategy are:

1. The logic is simple and intuitive, easy to understand and implement.
2. Smoothes price fluctuations with EMA and filters out market noise.
3. Automatically follows trends, avoiding missing trades.

## Risk Analysis  

There are also some risks with this strategy:

1. Crossover signals may lag and fail to capture reversals in a timely manner.
2. Whipsaw signals may occur frequently during ranging markets.
3. Poor parameter tuning may cause oversensitivity or delays.

Optimization can be done by adjusting EMA periods or adding filters.

## Optimization Directions

This strategy can be optimized from the following aspects:

1. Test different EMA period combinations.
2. Add volume or volatility conditions to reduce false signals.
3. Incorporate other indicators like MACD to confirm trends.
4. Optimize money management with stop loss and take profit.

## Conclusion  

The Dual Moving Average Crossover strategy is a simple and practical trend-following system overall. It is straightforward, easy to implement, and can automatically track trends. However, some risks such as lagging and false signals exist. With parameter tuning and adding filters, it can be further improved to become one of the fundamental algorithmic trading strategies.

||

## Overview  

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two EMA lines with different periods and goes long when the shorter period EMA crosses over the longer period EMA and goes short when the opposite crossing happens to capture trend reversals.

## Principles  

The core indicators of this strategy are two EMA lines, one is 30-period and the other is 60-period. The two EMA lines are calculated by custom functions in the code:

```pinescript
emaLen1 = emaFuncOne(close, lenMA1)  
emaLen2 = emaFuncTwo(close, lenMA2)
```

The trading signals are generated from the crossing of the two EMA lines:

```pinescript
currentState = if emaLen2 > emaLen1
    0
else 
    1

previousState = if emaLastLen2 > emaLastLen1 
    0  
else
    1

convergence = if currentState != previousState
    1
else 
    0
```

When the shorter period EMA crosses over the longer period EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you should go long. When the shorter period EMA crosses below the longer period EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you should go short.

## Advantage Analysis  

The advantages of this strategy are:

1. The logic is simple and intuitive, easy to understand and implement.
2. Smoothes price fluctuations with EMA and filters out market noise.
3. Automatically follows trends, avoiding missing trades.

## Risk Analysis  

There are also some risks with this strategy:

1. Crossover signals may lag and fail to capture reversals in a timely manner.
2. Whipsaw signals may occur frequently during ranging markets.
3. Poor parameter tuning may cause oversensitivity or delays.

Optimization can be done by adjusting EMA periods or adding filters.

## Optimization Directions  

This strategy can be optimized from the following aspects:

1. Test different EMA period combinations.
2. Add volume or volatility conditions to reduce false signals.
3. Incorporate other indicators like MACD to confirm trends.
4. Optimize money management with stop loss and take profit.

## Conclusion  

The Dual Moving Average Crossover strategy is a simple and practical trend-following system overall. It is straightforward, easy to implement, and can automatically track trends. However, some risks such as lagging and false signals exist. With parameter tuning and adding filters, it can be further improved to become one of the fundamental algorithmic trading strategies.

||

> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|30|Length 1|
|v_input_2|60|Length 2|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-10 00:00:00
end: 2024-01-11 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("ParkerMAStrat", overlay=true)

lenMA1=input(title="Length 1", defval=30)
lenMA2=input(title="Length 2",  defval=60)

x = 0

checkLines(current, last) =>
    if current > last
        x := 1
    else
        x := 0
    x
    
// plot ema based on len1
emaFuncOne(src, time_period) =>
    alpha = 2 / (time_period + 1)
    ema = 0.0
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    ema

emaLen1 = emaFuncOne(close, lenMA1)

plot(emaLen1, color=green, transp=0, linewidth=2)
// now we plot the _10_period_ema

// plot ema based on len2
emaFuncTwo(src, time_period) =>
    alpha = 2 / (time_period + 1)
    ema = 0.0
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    ema

// plot ema based on len2
emaFuncOneLast(src, time_period) =>
    alpha = 2 / (time_period + 1)
    ema = 0.0
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    ema

// add your strategy logic here
```