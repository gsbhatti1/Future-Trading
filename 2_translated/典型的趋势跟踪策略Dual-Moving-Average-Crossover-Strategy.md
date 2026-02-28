> Name

Dual-Moving-Average-Crossover-Strategy


> Author

ChaoZhang


> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1148a4aa63b71da3062.png)

[trans]

## Overview

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two different period EMAs, going long when the short-term EMA crosses above the long-term EMA and going short when the opposite happens to capture price trend reversals.

## Principles  

The core indicators of this strategy are two EMAs: one with 30 periods and another with 60 periods. The two EMAs are calculated by custom functions in the code:

```
emaLen1 = emaFuncOne(close, lenMA1)  
emaLen2 = emaFuncTwo(close, lenMA2)
```

The trading signals arise from the crossing of the two EMAs:

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

A crossover signal is triggered when the short-term EMA crosses above the long-term EMA, making the `currentState` different from the `previousState`. This triggers a buy order.  
A crossover signal is also triggered when the short-term EMA crosses below the long-term EMA, again making the `currentState` different from the `previousState`, which triggers a sell order.

## Advantage Analysis  

The advantages of this strategy include:

1. The logic is straightforward and easy to understand and implement.
2. EMAs smooth price fluctuations and filter out market noise.
3. It automatically tracks trends and avoids missing trades.

## Risk Analysis  

This strategy also has some risks:

1. Crossover signals may be delayed, failing to capture reversals in a timely manner.
2. Frequent false signals can occur during ranging markets.
3. Poorly tuned parameters might cause the strategy to be overly sensitive or too slow.

These risks can be mitigated by adjusting EMA periods or adding filters.

## Optimization Directions  

This strategy can be optimized from several aspects:

1. Test different combinations of EMA periods.
2. Add volume or volatility conditions to filter false signals.
3. Incorporate other indicators like MACD for trend confirmation.
4. Optimize money management with stop-loss and take-profit levels.

## Conclusion  

Overall, the Dual Moving Average Crossover strategy is a simple and practical trend-following system that is straightforward to implement and automatically tracks trends. However, it may suffer from lagging and false signals. With proper parameter tuning and additional filters, it can be further refined into one of the foundational algorithmic trading strategies.

||

## Overview  

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two EMA lines with different periods and goes long when the short-term EMA crosses above the long-term EMA and goes short when the opposite crossing happens to capture price trend reversals.  

## Principles  

The core indicators of this strategy are two EMAs, one 30-period and the other 60-period. The two EMAs are calculated by custom functions in the code:   

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

1. The logic is simple and intuitive, easy to understand and implement  
2. EMAs smooth price fluctuations with their smoothing properties, effectively filtering out market noise  
3. It automatically follows trends, reducing the risk of missing trades

## Risk Analysis   

There are also some risks associated with this strategy:  

1. Crossover signals may lag and fail to capture reversals in a timely manner
2. Frequent false signals can occur during ranging markets  
3. Poor parameter tuning might cause the system to be overly sensitive or too slow

These risks can be addressed by adjusting EMA periods or adding additional filters.

## Optimization Directions  

This strategy can be optimized from several aspects:  

1. Test different combinations of EMA periods
2. Add volume or volatility conditions to reduce false signals 
3. Incorporate other indicators like MACD for trend confirmation  
4. Optimize money management with stop loss and take profit levels

## Conclusion  

Overall, the Dual Moving Average Crossover strategy is a simple and practical trend-following system that is straightforward to implement and automatically tracks trends. However, it may suffer from lagging and false signals. With proper parameter tuning and additional filters, it can be further refined into one of the foundational algorithmic trading strategies.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
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
    // we have defined the alpha function above
    ema = 0.0
    // this is the initial declaration of ema, since we dont know the first ema we will declare it to 0.0 [as a decimal]
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    // this returns the computed ema at the current time
    // notice the use of : (colon) symbol before =, it symbolises that we are changing the value of ema,
    // since the ema was previously declared to 0
    // this is called mutable variable declaration in pine script
    ema
    // return ema from the function

emaLen1 = emaFuncOne(close, lenMA1)

plot(emaLen1, color=green, transp=0, linewidth=2)
// now we plot the 30_period_ema

// plot ema based on len2
emaFuncTwo(src, time_period) =>
    alpha = 2 / (time_period + 1)
    // we have defined the alpha function above
    ema = 0.0
    // this is the initial declaration of ema, since we dont know the first ema we will declare it to 0.0 [as a decimal]
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    // this returns the computed ema at the current time
    // notice the use of : (colon) symbol before =, it symbolises that we are changing the value of ema,
    // since the ema was previously declared to 0
    // this is called mutable variable declaration in pine script
    ema
    // return ema from the function

// plot ema based on len2
emaFuncOneLast(src, time_period) =>
    alpha = 2 / (time_period + 1)
    // we have defined the alpha function above
    ema = 0.0
    // this is the initial declaration of ema, since we dont know the first ema we will declare it to 0.0 [as a decimal]
    ema := alpha * src + (1 - alpha) * nz(ema[1])
    // this returns the computed ema at the current time
    // notice the use of : (colon) symbol before =, it symbolises that we are changing the value of ema,
    // since the ema was previously declared to 0
    // this is called mutable variable declaration in pine script
    ema
    // return ema from the function

emaLen2 = emaFuncTwo(close, lenMA2)

plot(emaLen2, color=red, transp=0, linewidth=2)
// now we plot the 60_period_ema

```

This PineScript code implements a simple dual moving average crossover strategy. It plots two EMAs: one with a 30-period length and another with a 60-period length. The trading signals are generated based on the crossovers of these two EMAs, providing buy or sell signals accordingly.