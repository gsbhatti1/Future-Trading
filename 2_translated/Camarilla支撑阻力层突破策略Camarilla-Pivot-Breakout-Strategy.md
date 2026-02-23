> Name

Camarilla Support Resistance Level Breakout Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11a805f97ef831a5d72.png)
[trans]

## Overview

The Camarilla Support Resistance Level Breakout Strategy (Camarilla Pivot Breakout Strategy) is a quantitative trading strategy that utilizes Camarilla support resistance levels for entries and exits. This strategy draws upon the support resistance theory from traditional technical analysis, combining Camarilla mathematical formulas to calculate key support resistance pivot points at different time levels, setting breakthroughs of these key points as conditions for establishing positions and closing positions, aiming to achieve excess returns.

## Strategy Principle

The core logic of this strategy is: calculating the H4 and L4, two key support resistance points obtained from the Camarilla formula at the daily level, and generating trading signals when the price breaks through these two points.

Specifically, the strategy first calculates the midpoint of the intraday highest price, lowest price, and closing price of the current K-line as the pivot point of the day's support resistance center. Then it calculates the range of these three prices as Range. Based on Range, the key support resistance levels in the Camarilla formula can be calculated, including H4, H3, H2, H1 and L1, L2, L3, L4, etc. Among them, H4 is the first resistance level of the day, and L4 is the first support level of the day.

In terms of trading signal generation, if the closing price of the day breaks through the H4 level above, a long signal is generated; if the closing price breaks through the L4 level below, a short signal is generated. In this way, by capturing the breakthrough of key support resistance levels, the direction and strength of market movement are judged to generate trading signals.

Therefore, the main logic of this strategy is: using Camarilla key point breakthroughs to judge market structure and obtain trading signals.

## Advantage Analysis

There are several main advantages to using this Camarilla support resistance level breakthrough strategy:

1. Utilizing traditional technical analysis theory indicators with stable backtesting

Camarilla analysis is based on the support resistance theory in traditional technical analysis. This theory has withstood the test of time, ensuring the stability of the strategy across different varieties and time periods.

2. Simple parameter settings, easy for live trading operations

Compared to customized strategies such as machine learning, the Camarilla strategy has simple rules and fewer parameters, making it easy to understand and operate in live trading. This is very important for beginners.

3. Clear breakthrough signals, simple implementation

Monitoring the breakthrough of H4 and L4 can establish positions. The strategy signals are concise and clear, and the code implementation is also simple. This enables us to quickly test strategy ideas and go live.

4. Suitable for both high-frequency and low-frequency trading

The Camarilla strategy is suitable for both high-frequency (second-level, fractional K-lines) and low-frequency (daily, weekly level) trading, which is a great advantage.

## Risk Analysis

Of course, this simple breakthrough strategy also has certain risks, mainly concentrated in:

1. Risk of false breakthroughs

After the market breaks through the Camarilla points, it may not continue to move in the same direction, resulting in the risk of reversal or false breakthroughs. Without timely stop-loss, significant losses will be faced.

2. Risk of missing partial breakthroughs

If only monitoring closing price breakthroughs, some breakthrough opportunities may be missed, thus affecting profitability. This needs to be resolved by optimizing entry conditions.

3. Risk of limited profits

Compared to more complex strategies, relying solely on Camarilla point breakthroughs may have limited profit space and amplitude. This can be alleviated by appropriately adjusting position size and other methods.

Therefore, this simple breakthrough strategy still needs further risk control through stop-loss strategies, optimizing entry conditions, appropriately adjusting positions, and other methods to ensure its stable operation.

## Optimization Directions

To further optimize and improve this Camarilla breakthrough strategy, the following aspects can be approached:

1. Combine more indicators to judge true/false breakthroughs

For example, combine volume indicators, moving averages, etc., to judge the reliability of breakthroughs and avoid the risk of false breakthroughs.

2. Optimize breakthrough determination logic

Such as relaxing breakthrough amplitude, determining better parameters through backtesting. Or combine seasonality and more rules.

3. Optimize stop-loss strategy

Appropriately reduce stop-loss amplitude while preventing being trapped. Or set profit-taking stop-loss, trailing stop-loss, and other strategies.

4. Dynamically adjust positions and leverage

Timely adjust position size and leverage parameters according to market changes to make the strategy better adapt to different market conditions.

5. Combine more complex machine learning algorithms

Use deep learning models such as LSTM and RNN to predict key point breakthrough probability and make the strategy more intelligent.

## Summary

The Camarilla Support Resistance Level Breakout Strategy is a simple, straightforward, and easily implementable quantitative trading strategy. It employs mature technical analysis tools, generating trading signals by capturing breakthroughs of key support resistance points. The advantages of this strategy are stability and reliability, with relatively simple live trading operations. Of course, to achieve higher trading efficiency, further optimization through stop-loss, parameter adjustment, risk control, and other methods is still needed.

|| 

[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-27 00:00:00
end: 2024-01-03 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
//Created by CristianD
strategy(title="CamarillaStrategy", shorttitle="CD_Camarilla_Strategy", overlay=true) 
//sd = input(true, title="Show Daily Pivots?")
EMA = ema(close,3)

//Camarilla
pivot = (high + low + close ) / 3.0 
range = high - low
h5 = (high/low) * close 
h4 = close + (high - low) * 1.1 / 2.0
h3 = close + (high - low) * 1.1 / 4.0
h2 = close + (high - low) * 1.1 / 6.0
h1 = close + (high - low) * 1.1 / 12.0
l1 = close - (high - low) * 1.1 / 12.0
l2 = close - (high - low) * 1.1 / 6.0
l3 = close - (high - low) * 1.1 / 4.0
l4 = close - (high - low) * 1.1 / 2.0
h6 = h5 + 1.168 * (h5 - h4) 
l5 = close - (h5 - close)
l6 = close - (h6 - close)

// Daily line breaks
//sopen = request.security(syminfo.tickerid, "D", open [1])
//shigh = request.security(syminfo.tickerid, "D", high [1])
//slow = request.security(syminfo.tickerid, "D", low [1])
//sclose = request.security(syminfo.tickerid, "D", close [1])
//
// Color
//dcolor=sopen != sopen[1] ? na : black
//dcolor1=sopen != sopen[1] ? na : red
//dcolor2=sopen != sopen[1] ? na : green

//Daily Pivots 
dtime_pivot = request.security(syminfo.tickerid, 'D', pivot[1]) 
dtime_h6 = request.security(syminfo.tickerid, 'D', h6[1]) 
dtime_h5 = request.security(syminfo.tickerid, 'D', h5[1]) 
dtime_h4 = request.security(syminfo.tickerid, 'D', h4[1]) 
dtime_h3 = request.security(syminfo.tickerid, 'D', h3[1]) 
dtime_h2 = request.security(syminfo.tickerid, 'D', h2[1]) 
dtime_h1 = request.security(syminfo.tickerid, 'D', h1[1]) 
dtime_l1 = request.security(syminfo.tickerid, 'D', l1[1]) 
dtime_l2 = request.security(syminfo.tickerid, 'D', l2[1]) 
dtime_l3 = request.security(syminfo.tickerid, 'D', l3[1]) 
dtime_l4 = request.security(syminfo.tickerid, 'D', l4[1]) 
dtime_l5 = request.security(syminfo.tickerid, 'D', l5[1]) 
dtime_l6 = request.security(syminfo.tickerid, 'D', l6[1]) 

//offs_daily = 0
//plot(sd and dtime_pivot ? dtime_pivot : na, title="Daily Pivot",color=dcolor, linewidth=2)
//plot(sd and dtime_h6 ? dtime_h6 : na, title="Daily H6", color=dcolor2, linewidth=2)
//plot(sd and dtime_h5 ? dtime_h5 : na, title="Daily H5",color=dcolor2, linewidth=2)
//plot(sd and dtime_h4 ? dtime_h4 : na, title="Daily H4",color=dcolor2, linewidth=2)
//plot(sd and dtime_h3 ? dtime_h3 : na, title="Daily H3",color=dcolor1, linewidth=3)
//plot(sd and dtime_h2 ? dtime_h2 : na, title="Daily H2",color=dcolor2, linewidth=2)
//plot(sd and dtime_h1 ? dtime_h1 : na, title="Daily H1",color=dcolor2, linewidth=2)
//plot(sd and dtime_l1 ? dtime_l1 : na, title="Daily L1",color=dcolor2, linewidth=2)
//plot(sd and dtime_l2 ? dtime_l2 : na, title="Daily L2",color=dcolor2, linewidth=2)
//plot(sd and dtime_l3 ? dtime_l3 : na, title="Daily L3",color=dcolor1, linewidth=3)
//plot(sd and dtime_l4 ? dtime_l4 : na, title="Daily L4",color=dcolor2, linewidth=2)
//plot(sd and dtime_l5 ? dtime_l5 : na, title="Daily L5",color=dcolor2, linewidth=2)
//plot(sd and dtime_l6 ? dtime_l6 : na, title="Daily L6",color=dcolor2, linewidth=2)

longCondition = close >dtime_h4
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long)
    


shortCondition = close <dtime_l4
if (shortCondition)
    strategy.entry("My Short Entry Id", strategy.short)
    

```

> Detail

https://www.fmz.com/strategy/437664

> Last Modified

2024-01-04 16:17:06