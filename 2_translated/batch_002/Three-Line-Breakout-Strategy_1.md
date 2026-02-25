<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Three-Line-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

This strategy is based on an improved three-line-break charting method. It consists of two lines formed by closing prices that create a "cloud" pattern. When in a bullish trend, if the price breaks below the bottom of the cloud, a new bearish trend begins. Conversely, when in a bearish trend, if the price breaks above the top of the cloud, a new bullish trend starts. This strategy falls under pure price action strategies and can be used in combination with indicators like SuperTrend.

## Strategy Logic

1. Define the current price as `xu`, along with `xu1`, `xu2`, and `xu3` used for plotting the three-line pattern.

2. Determine the upper and lower bounds for drawing the three-line pattern based on price movements, updating `xu1`, `xu2`, and `xu3`.

3. A break of `xu` below `xu3` initiates a short trend; a break above `xu1` initiates a long trend.

4. Plot the cloud pattern using `xu` and `xu3` as boundaries.

5. Option to trade in the forward or reverse direction.

6. Go long or short upon breaking through the cloud, and close positions when price returns within the cloud.

## Advantages

Main advantages of this strategy include:

1. Pure price action-based approach, unaffected by external indicators.

2. Clear and intuitive three-line pattern, making operations easy to judge.

3. Configurable for reverse trading, suitable for bearish opportunities.

4. Easily combinable with trends and other indicators.

5. Convenient for backtesting and visualization, facilitating mastery and optimization.

## Risk Analysis

Key risks associated with this strategy include:

1. Pure price action is susceptible to false breakouts caused by sudden events.

2. Lack of stop-loss settings exposes the strategy to significant loss risk.

3. Trading costs are not taken into account.

4. Fixed parameters may yield varying effectiveness across different instruments.

5. Consecutive breakouts are not considered.

6. Reverse trading should be approached cautiously as it might go against the major trend.

## Optimization Directions

This strategy can be optimized in several ways:

1. Implement stop-loss strategies and optimize stop levels.

2. Factor in trading costs.

3. Test parameter effectiveness across different instruments and establish parameter optimization.

4. Improve breakout detection logic to handle consecutive breakouts.

5. Add combinations with trend indicators to avoid counter-trend moves.

6. Incorporate position sizing controls.

7. Extend backtesting periods to verify robustness.

## Conclusion

The Three-Line Breakout Strategy is intuitive and straightforward, generating trading signals based on price behavior. Combining it with trends and other indicators can enhance its performance. By incorporating stop-loss mechanisms, optimizing parameters and logic, and implementing position control, it can be refined into a relatively stable short-term trading strategy.

||

## Overview

This strategy is based on a modified three line break chart. Two lines made of closing prices form a "cloud" shape. Breakout below the cloud signals a new bearish trend. Breakout above the cloud signals a new bullish trend. It is a price action strategy that can be combined with trend filters like SuperTrend.

## Strategy Logic  

1. Define current price xu, xu1, xu2, xu3 for plotting three lines.

2. Update xu1, xu2, xu3 based on price as upper/lower band.

3. xu breaking xu3 starts a short trend, breaking xu1 starts a long trend.

4. Plot cloud band using xu and xu3. 

5. Option to trade in reverse direction.

6. Enter on cloud breakouts, exit on returning inside cloud.

## Advantage Analysis

The advantages of this strategy are:

1. Based purely on price action, unaffected by indicators.

2. Clear and intuitive three line pattern. 

3. Flexibility to trade reversals.

4. Easy to combine with trends and other indicators.

5. Easy backtesting and visualization for refinement.

## Risk Analysis

The main risks of this strategy are:

1. Price patterns prone to false breakouts from events.

2. No stop loss exposes to large losses.

3. Ignores trading costs. 

4. Fixed parameters may not suit different products.

5. Doesn't account for consecutive breakouts.

6. Reversal trading risky against major trends. 

## Optimization Directions 

The strategy can be improved by:

1. Adding stop loss and optimizing stops.

2. Accounting for trading costs.

3. Testing parameters for different products. 

4. Improving breakout logic for consecutive breaks.

5. Adding trend filter to avoid counter-trend trades.

6. Controlling position sizing.

7. Expanding backtest period for robustness.

## Summary

The three line breakout strategy provides intuitive signals based on price patterns. It can be strengthened by adding trends, indicators, stops, optimized logic and parameters, and position sizing. This can transform it into a robust short-term trading system.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-09-22 00:00:00
end: 2023-09-22 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 31/05/2019
// This is a modified version of the three line break price representation. 
// It is composed with 2 lines made of Close price values forming a “cloud”.
//    If the trend is bullish and the price breach the lower level of the green 
//       cloud, a new bearish trend is taking place.
//    If the current trend is bearish and the price breakout the upper band of 
//       the cloud, a new bullish trend is forming.
// This is a “price action” indicator, signals may be filtered by long term trend 
// analysis with other indicators such as Supertrend for instance.
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
strategy(title="Three Line Break", overlay = true)
reverse = input(false, title="Trade reverse")
xtrend = 1
xu = close
xu1 = close
xu2 = close
xu3 = close
if xtrend[1] == 1
    if close > xu[1]
        xu3 := xu2[1]
        xu2 := xu1[1]
        xu1 := xu[1]
        xu := close
        xtrend := 1
    else 
        if close < xu3[1]
            xu3 := xu1[1]
            xu2 := xu1[1]
            xu1 := xu1[1]
            xu := close
            xtrend := -1        
        else
            xtrend := 1
else
    if close > xu3[1]
        xu3 := xu1[1]
        xu2 := xu1[1]
        xu1 := xu1[1]
        xu := close
        xtrend := 1
    else
        if close < xu[1] 
            xu3 := xu2[1]
            xu2 := xu1[1]
            xu1 := xu[1]
            xu := close
            xtrend := -1
        else
            xtrend := -1
colorm = xtrend == -1 ? red: xtrend == 1 ? green : blue 
possig = iff(reverse and xtrend == 1, -1,
          iff(reverse and xtrend == -1, 1, xtrend))	   
if (possig == 1) 
    strategy.entry("Long", strategy.long)
if (possig == -1)
    strategy.entry("Short", strategy.short)	 
if (possig == 0) 
    strategy.close_all()
barcolor(possig == -1 ? red: possig == 1 ? green : blue ) 		
p1 = plot(xu, color=colorm)
p2 = plot(xu3, color=colorm)
fill(p1, p2, color=colorm)
```

> Detail

https://www.fmz.com/strategy/427684

> Last Modified

2023-09-23 16:02:20