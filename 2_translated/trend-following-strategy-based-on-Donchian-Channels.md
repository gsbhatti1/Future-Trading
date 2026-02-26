> Name

Trend-Following Strategy Based on Donchian Channels

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/18888140f2939f6e2d8.png)

[trans]
# Puling Strategy

## Overview

The Puling strategy is a trend-following strategy based on Donchian Channels. It uses fast and slow Donchian channels to identify the trend direction and enter during pullbacks by buying low and selling high. The advantages of this strategy are that it can automatically track trends, cut losses quickly when the trend changes, and reverse positions accordingly. However, there is a risk of significant drawdowns and stop-loss points being too close.

## Strategy Logic

The strategy first defines the fast channel period as 20 bars and the slow channel period as 50 bars. The fast channel is used to set the stop loss price, while the slow channel determines the trend direction and entry timing.

First, the highest high and lowest low of the fast channel are calculated, and the midpoint is taken as the stop loss line. At the same time, the highest high and lowest low of the slow channel are calculated, with the channel top and bottom serving as the entry lines.

When the price breaks through the top of the slow channel, go long; when it breaks through the bottom of the slow channel, go short. After entering the position, set the stop loss at the midpoint of the fast channel.

So, the slow channel determines the major trend direction, while the fast channel tracks minor breakouts within a small range to determine the stop loss point. When the major trend reverses, the price will first break through the stop loss line of the fast channel to realize the stop loss.

## Advantages

- Automatically track trends and cut losses in time. The double channel structure can automatically track trends and quickly cut losses when trends reverse.
  
- Enter during pullbacks with some trend filtering effect. Only taking entries when price breaks through channel boundaries can filter out false breakouts without real trends.
  
- Controllable risk. The close stop loss distance can control single loss.

## Risks

- Larger drawdowns. Trend following strategies can have relatively large drawdowns, requiring psychological preparation.
  
- Stop loss too close. The fast channel period is short, so the stop loss is close and prone to being stopped out. We can appropriately relax the fast channel period.
  
- Too many trades. The double channel structure can generate excessive entries, requiring reasonable position sizing.

## Optimization Directions

- Add entry filters. We can add volatility etc. in entry conditions to filter breakouts without enough trend strength.
  
- Optimize channel period parameters. We can find the optimal channel parameter combinations systematically.
  
- Combining multiple timeframes. Determine the major trend on higher timeframes and trade on lower timeframes.
  
- Dynamic stop loss distance. Adjust stop distance dynamically based on market volatility.

## Summary

The Puling strategy is a standard trend-following strategy overall. It uses price channels to determine trend direction and sets stop losses to control risks. The strategy has some advantages but also the problems of drawdowns and stop-loss points being too close. We can optimize it through adjusting channel parameters, adding filters, etc. However, we should note that trend following strategies require strong psychology to endure drawdowns.

||

## Overview

The Puling strategy is a trend-following strategy based on Donchian Channels. It uses fast and slow Donchian channels to identify the trend direction and enter during pullbacks. The advantages of this strategy are that it can automatically track trends, cut losses quickly when the trend changes, and reverse positions accordingly. But it also has the risks of significant drawdowns and stop-loss points being too close.

## Strategy Logic

The strategy first defines the fast channel period as 20 bars and the slow channel period as 50 bars. The fast channel is used to set the stop loss price, while the slow channel determines the trend direction and entry timing.

First, the highest high and lowest low of the fast channel are calculated, and the midpoint is taken as the stop loss line. At the same time, the highest high and lowest low of the slow channel are calculated, with the channel top and bottom serving as the entry lines.

When the price breaks through the top of the slow channel, go long; when it breaks through the bottom of the slow channel, go short. After entering the position, set the stop loss at the midpoint of the fast channel.

So, the slow channel determines the major trend direction, while the fast channel tracks minor breakouts within a small range to determine the stop loss point. When the major trend reverses, the price will first break through the stop loss line of the fast channel to realize the stop loss.

## Advantages

- Automatically track trends and cut losses in time. The double channel structure can automatically track trends and quickly cut losses when trends reverse.
  
- Enter during pullbacks with some trend filtering effect. Only taking entries when price breaks through channel boundaries can filter out false breakouts without real trends.
  
- Controllable risk. The close stop loss distance can control single loss.

## Risks

- Larger drawdowns. Trend following strategies can have relatively large drawdowns, requiring psychological preparation.
  
- Stop loss too close. The fast channel period is short, so the stop loss is close and prone to being stopped out. We can appropriately relax the fast channel period.
  
- Too many trades. The double channel structure can generate excessive entries, requiring reasonable position sizing.

## Optimization Directions

- Add entry filters. We can add volatility etc. in entry conditions to filter breakouts without enough trend strength.
  
- Optimize channel period parameters. We can find the optimal channel parameter combinations systematically.
  
- Combining multiple timeframes. Determine the major trend on higher timeframes and trade on lower timeframes.
  
- Dynamic stop loss distance. Adjust stop distance dynamically based on market volatility.

## Summary

The Puling strategy is a standard trend-following strategy overall. It uses price channels to determine trend direction and sets stop losses to control risks. The strategy has some advantages but also the problems of drawdowns and stop-loss points being too close. We can optimize it through adjusting channel parameters, adding filters etc. But we should note that trend following strategies require strong psychology to endure drawdowns.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|2|Risk size, %|
|v_input_4|20|Fast channel (for stop-loss)|
|v_input_5|50|Slow channel (for entries)|
|v_input_6|true|Show offset|
|v_input_7|true|Show lines|
|v_input_8|true|Show label (drawdown)|
|v_input_9|true|Show background|
|v_input_10|1900|From Year|
|v_input_11|2100|To Year|
|v_input_12|true|From Month|
|v_input_13|12|To Month|
|v_input_14|true|From day|
|v_input_15|31|To day|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-30 00:00:00
end: 2023-10-30 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Noro
//2020

//@version=4
strategy("Puling's RiskTurtle Strategy", shorttitle = "RiskTurtle str", overlay = true, default_qty_type = strategy.percent_of_equity, initial_capital = 100, default_qty_value = 100, commission_value = 0.1)

//Settings
needlong  = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
risk      = input(2, minval = 0.1, maxval = 99, title = "Risk size, %")
fast      = input(20, minval = 1, title = "Fast channel (for stop-loss)")
slow      = input(50, minval = 1, title = "Slow channel (for entries)")
showof    = input(true, defval = true, title = "Show offset")
showll    = input(true, defval = true, title = "Show lines")
showdd    = input(true, defval = true, title = "Show label (drawdown)")
showbg    = input(true, defval = true, title = "Show background")
fromyear  = input(1900, defval = 1900, minval=