<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Bollinger Band RSI Dual Line Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1718937808d5911aac0.png)
[trans]

## Overview

This strategy combines Bollinger Bands with the Relative Strength Index (RSI). It generates trading signals only when RSI indicates overbought/oversold conditions simultaneously with price breaking through the upper/lower bands of Bollinger Bands. This makes the trading signals stricter and more reliable.

## Strategy Principle

1. Use Bollinger Bands to calculate the middle line, upper line, and lower line based on closing prices over the past n days.
2. Calculate the RSI indicator to judge whether the market is excessively bullish or bearish.
3. Initiate a short trade only when RSI indicates overbought (above the rsi_overbought parameter) and price breaks above the upper Bollinger Band.
4. Initiate a long trade only when RSI indicates oversold (below the rsi_oversold parameter) and price breaks below the lower Bollinger Band.

Thus, this strategy leverages both the channel characteristics of Bollinger Bands and the overbought/oversold signals of the RSI indicator, avoiding errors from single-indicator judgments and enhancing reliability.

## Strategy Advantages

1. Combines the advantages of Bollinger Bands and RSI indicator for stricter judgment and fewer mistakes.
2. Bollinger Bands set dynamic channels that can capture market volatility patterns.
3. RSI judges overbought/oversold conditions to avoid buying high and selling low.

## Strategy Risks

1. If Bollinger Bands parameters are improperly set, the upper and lower bands may fail to effectively envelope prices.
2. If RSI parameters are improperly set, it may fail to accurately judge true overbought/oversold conditions.
3. The strategy itself cannot determine trend direction and needs to be used with other indicators.

To address these risks, parameters should be optimized, models strictly tested, and supplemented with other indicators to judge major trends.

## Strategy Optimization Directions

1. Test Bollinger Bands with different cycle parameters to find the optimal cycle parameters.
2. Test RSI indicators with different parameters to determine better parameters.
3. Can add other indicators such as moving averages to judge overall trends.

## Summary

This strategy successfully combines the advantages of Bollinger Bands and the RSI indicator, issuing trading instructions only when signals appear simultaneously from both. This effectively avoids misjudgments from single indicators, making trading more reliable. At the same time, parameters should be optimized, models strictly tested, and supplemented with other indicators to judge major trends, thereby further improving the strategy's stability and profitability.

||


## Overview

This strategy combines Bollinger Bands with the Relative Strength Index (RSI) indicator. It issues trading signals only when both RSI overbought/oversold conditions and breakthroughs of Bollinger Bands' upper/lower rails occur simultaneously, making this strategy's trading signals more stringent and reliable.

## Strategy Logic

1. Use Bollinger Bands to calculate the midline, upper rail, and lower rail based on closing prices over the previous n days.
2. Calculate the RSI indicator to determine if the market is excessively bullish or bearish.
3. Only initiate a short trade when the RSI indicator shows overbought (above the rsi_overbought parameter) and the price breaks through the upper Bollinger Band.
4. Only initiate a long trade when the RSI indicator shows oversold (below the rsi_oversold parameter) and the price breaks through the lower Bollinger Band.

In this way, the strategy utilizes both the channel characteristics of Bollinger Bands and the overbought/oversold signals of the RSI indicator, avoiding incorrect judgments from a single indicator and making it more reliable.

## Strategy Advantages

1. Integrates the advantages of Bollinger Bands and RSI indicator for stricter judgment and avoidance of mistakes.
2. Bollinger Bands set dynamic channels that can grasp market volatility patterns.
3. RSI judges overbought/oversold situations to avoid chasing highs and selling lows.

## Strategy Risks

1. If Bollinger Bands parameters are improperly set, the upper and lower rails may fail to effectively envelop prices.
2. If RSI parameters are improperly set, it may fail to effectively judge true overbought/oversold conditions.
3. The strategy itself cannot determine trend direction and needs to be used with other indicators.

For the above risks, parameters should be optimized, models strictly tested, and supplemented with other indicators to judge major trends.

## Strategy Optimization Directions

1. Test Bollinger Bands with different period parameters to find the best period parameters.
2. Test RSI indicators with different parameters to determine relatively better parameters.
3. Can incorporate other indicators like moving averages to judge overall trends.

## Conclusion

This strategy successfully combines the advantages of Bollinger Bands and the RSI indicator, issuing trading instructions only when signals appear simultaneously from both. This effectively avoids misjudgments from single indicators, making trading more reliable. Meanwhile, parameters should be optimized, models strictly tested, and supplemented with other indicators to judge major trends, thereby further enhancing the strategy's stability and return rate.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|6|RSI Period Length|
|v_input_2|200|Bollinger Period Length|
|v_input_3|true|Enable Bar Color?|
|v_input_4|true|Enable Background Color?|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-25 00:00:00
end: 2023-12-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Bollinger + RSI, Double Strategy (by ChartArt) v1.1", shorttitle="CA_-_RSI_Bol_Strat_1.1", overlay=true)

// ChartArt's RSI + Bollinger Bands, Double Strategy - Update
//
// Version 1.1
// Idea by ChartArt on January 18, 2015.
//
// This strategy uses the RSI indicator 
// together with the Bollinger Bands 
// to sell when the price is above the
// upper Bollinger Band (and to buy when
// this value is below the lower band).
//
// This simple strategy only triggers when
// both the RSI and the Bollinger Bands
// indicators are at the same time in
// a overbought or oversold condition.
//
// In this version 1.1 the strategy was
// both simplified for the user and
// made more successful in backtesting. 
//
// List of my work: 
// https://www.tradingview.com/u/ChartArt/
// 
//  __             __  ___       __  ___ 
// /  ` |__|  /\  |__)  |   /\  |__)  |  
// \__, |  | /~~\ |  \  |  /~~\ |  \  |  
// 
// 


///////////// RSI
RSIlength = input(6,title="RSI Period Length") 
RSIoverSold = 50
RSIoverBought = 50
price = close
vrsi = rsi(price, RSIlength)


///////////// Bollinger Bands
BBlength = input(200, minval=1,title="Bollinger Period Length")
BBmult = 2 // input(2.0, minval=0.001, maxval=50,title="Bollinger Bands Standard Deviation")
BBbasis = sma(price, BBlength)
BBdev = BBmult * stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev
source = close
buyEntry = crossover(source, BBlower)
sellEntry = crossunder(source, BBupper)
plot(BBbasis, color=aqua,title="Bollinger Bands SMA Basis Line")
p1 = plot(BBupper, color=silver,title="Bollinger Bands Upper Line")
p2 = plot(BBlower, color=silver,title="Bollinger Bands Lower Line")
fill(p1, p2)


///////////// Colors
switch1=input(true, title="Enable Bar Color?")
switch2=input(true, title="Enable Background Color?")
TrendColor = RSIoverBought and (price[1] > BBupper and price < BBupper) and BBbasis < BBbasis[1] ? red : RSIoverSold and (price[1] < BBlower and price > BBlower) and BBbasis > BBbasis[1] ? green : na
barcolor(switch1?TrendColor:na)
bgcolor(switch2?TrendColor:na,transp=50)


///////////// RSI + Bollinger Bands Strategy
if (not na(vrsi))

    if (crossover(vrsi, RSIoverSold) and crossover(source, BBlower))
        strategy.entry("RSI_BB_L", strategy.long, stop=BBlower,  comment="RSI_BB_L")
    else
        strategy.cancel(id="RSI_BB_L")
        
    if (crossunder(vrsi, RSIoverBought) and crossunder(source, BBupper))
        strategy.entry("RSI_BB_S", strategy.short, stop=BBupper,  comment="RSI_BB_S")
    else
        strategy.cancel(id="RSI_BB_S")

//plot(strategy.equity, title="equity", color=red, linewidth=2, style=areabr)
```

> Detail

https://www.fmz.com/strategy/436643

> Last Modified

2023-12-26 15:30:26