> Name

Dual-Moving-Average-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1148a4aa63b71da3062.png)

[trans]

## Overview

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two different-period EMA lines, going long when the short-term EMA crosses above the long-term EMA and going short when the opposite happens to capture price trend reversals.

## Principles  

The core indicators of this strategy are two EMAs, one with 30 periods and the other with 60 periods. The code calculates these two EMAs using custom functions:

```
emaLen1 = emaFuncOne(close, lenMA1)  
emaLen2 = emaFuncTwo(close, lenMA2)
```

The trading signals are generated from the crossing of the two EMA lines:

```  
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

When the short-term EMA crosses above the long-term EMA, `currentState` is not equal to `previousState`, triggering a crossover signal. At that point, go long.
When the short-term EMA crosses below the long-term EMA, `currentState` is not equal to `previousState`, triggering a crossover signal. At that point, go short.

## Advantage Analysis  

The advantages of this strategy include:

1. The logic is simple and intuitive, making it easy to understand and implement.
2. Utilizing the smoothing properties of EMAs helps filter out market noise.
3. Automatically follows trends without missing trades.

## Risk Analysis   

This strategy also has some risks:

1. Crossover signals may be delayed, failing to capture reversals in a timely manner.
2. Frequent whipsaw signals can occur during ranging markets.
3. Poor parameter settings can cause the system to become too sensitive or too slow.

Optimization can be achieved by adjusting EMA periods or adding additional filters.

## Optimization Directions  

This strategy can be optimized in several ways:

1. Test different combinations of EMA periods.
2. Add volume or volatility conditions to reduce false signals.
3. Incorporate other indicators like MACD to confirm trends.
4. Optimize money management with stop loss and take profit levels.

## Conclusion  

The Dual Moving Average Crossover strategy is a straightforward, practical trend-following system overall. It is simple to implement and can automatically track trends. However, it comes with some risks such as lagging and false signals. By tuning parameters and adding filters, it can be further improved to become one of the foundational strategies in algorithmic trading.

||

## Overview   

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two different-period EMA lines, going long when the short-term EMA crosses above the long-term EMA and going short when the opposite happens to capture price trend reversals.  

## Principles  

The core indicators of this strategy are two EMAs, one with 30 periods and the other with 60 periods. The code calculates these two EMAs using custom functions:   

```
emaLen1 = emaFuncOne(close, lenMA1)  
emaLen2 = emaFuncTwo(close, lenMA2)  
```

The trading signals are generated from the crossing of the two EMA lines:  

```  
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
  
When the short-term EMA crosses above the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, go long. 
When the short-term EMA crosses below the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, go short.

## Advantage Analysis  

The advantages of this strategy are:  

1. The logic is simple and intuitive, making it easy to understand and implement  
2. Utilizing the smoothing properties of EMAs helps filter out market noise  
3. Automatically follows trends without missing trades   

## Risk Analysis   

There are also some risks with this strategy:  

1. Crossover signals may lag and fail to capture reversals in a timely manner
2. Frequent whipsaw signals can occur during ranging markets  
3. Poor parameter tuning may cause oversensitivity or delays

Optimization can be done by adjusting EMA periods or adding filters.

## Optimization Directions

This strategy can be optimized from the following aspects:  

1. Test different EMA period combinations  
2. Add volume or volatility filters to reduce false signals
3. Incorporate other indicators like MACD to confirm trends  
4. Optimize money management with stop loss and take profit

## Conclusion  

The Dual Moving Average Crossover strategy is a simple and practical trend-following system overall. It is straightforward, easy to implement, and can automatically track trends. However, some risks such as lagging and false signals exist. With parameter tuning and adding filters, it can be further improved to become one of the fundamental algorithmic trading strategies.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|30|Length 1|
|v_input_2|60|Length 2|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-10 00:00:00
end: 2024-01-11 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Dual Moving Average Crossover Strategy", overlay=true)

lenMA1 = input(title="Length 1", defval=30)
lenMA2 = input(title="Length 2", defval=60)

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
// now we plot the _30_period_ema

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
```