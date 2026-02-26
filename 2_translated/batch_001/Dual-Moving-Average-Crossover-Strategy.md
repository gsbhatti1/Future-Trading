> Name

Dual-Moving-Average-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1148a4aa63b71da3062.png)

[trans]

## Overview

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two different-period EMA lines, going long when the short-term EMA crosses above the long-term EMA and going short when the opposite crossover happens to capture price trend reversals.

## Principles  

The core indicators of this strategy are two EMA lines, one with a 30-period length and another with a 60-period length. The two EMAs are calculated by custom functions in the code:   

```
emaLen1 = emaFuncOne(close, lenMA1)
emaLen2 = emaFuncTwo(close, lenMA2)  
```

The trading signals are generated from the crossovers of these EMA lines:  

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
  
When the short-term EMA crosses above the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you go long. 
When the short-term EMA crosses below the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you go short.

## Advantage Analysis  

The advantages of this strategy are:  

1. The logic is simple and intuitive, making it easy to understand and implement  
2. Utilizes the smoothing property of EMAs to filter out market noise  
3. Automatically follows trends, reducing the risk of missing trades

## Risk Analysis   

There are also some risks with this strategy:  

1. Crossover signals may lag and fail to capture reversals in a timely manner
2. Whipsaw signals may occur frequently during ranging markets  
3. Poor parameter tuning may cause oversensitivity or delays

Optimization can be done by adjusting EMA periods or adding filters.

## Optimization Directions

This strategy can be optimized from the following aspects:  

1. Test different combinations of EMA periods  
2. Add volume or volatility filters to reduce false signals
3. Incorporate other indicators like MACD to confirm trends
4. Optimize money management with stop loss and take profit

## Conclusion  

The Dual Moving Average Crossover strategy is overall a simple and practical trend-following system. It is straightforward, easy to implement, and can automatically track trends. However, some risks such as lagging and false signals exist. With parameter tuning and adding filters, it can be further improved to become one of the fundamental algorithmic trading strategies.

||

## Overview   

The Dual Moving Average Crossover strategy is a typical trend-following strategy. It uses two different-period EMA lines and goes long when the short-term EMA crosses above the long-term EMA and goes short when the opposite crossover happens to capture price trend reversals.

## Principles  

The core indicators of this strategy are two EMA lines, one with a 30-period length and another with a 60-period length. The two EMAs are calculated by custom functions in the code:   

```
emaLen1 = emaFuncOne(close, lenMA1)
emaLen2 = emaFuncTwo(close, lenMA2)  
```

The trading signals are generated from the crossovers of these EMA lines:  

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
  
When the short-term EMA crosses above the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you go long. 
When the short-term EMA crosses below the long-term EMA, `currentState` is not equal to `previousState`, a crossover signal is triggered, and you go short.

## Advantage Analysis  

The advantages of this strategy are:  

1. The logic is simple and intuitive, making it easy to understand and implement  
2. Utilizes the smoothing property of EMAs to filter out market noise  
3. Automatically follows trends, reducing the risk of missing trades

## Risk Analysis   

There are also some risks with this strategy:  

1. Crossover signals may lag and fail to capture reversals in a timely manner
2. Whipsaw signals may occur frequently during ranging markets  
3. Poor parameter tuning may cause oversensitivity or delays

Optimization can be done by adjusting EMA periods or adding filters.

## Optimization Directions

This strategy can be optimized from the following aspects:  

1. Test different combinations of EMA periods  
2. Add volume or volatility filters to reduce false signals
3. Incorporate other indicators like MACD to confirm trends
4. Optimize money management with stop loss and take profit

## Conclusion  

The Dual Moving Average Crossover strategy is overall a simple and practical trend-following system. It is straightforward, easy to implement, and can automatically track trends. However, some risks such as lagging and false signals exist. With parameter tuning and adding filters, it can be further improved to become one of the fundamental algorithmic trading strategies.

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
    
//plot ema based on len1
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

emaLen1 = emaFuncOne(close, lenMA1)

plot(emaLen1, color=green, transp=0, linewidth=2)
// now we plot the _30_period_ema

//plot ema based on len2
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

//plot ema based on len2
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

emaLen2 = emaFuncOneLast(close, lenMA2)
plot(emaLen2, color=red, transp=0, linewidth=2)
// now we plot the _60_period_ema
```