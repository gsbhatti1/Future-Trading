> Strategy Name

Simple-Holder-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b6b70c9a4e4aecb0d7.png)
[trans]

## Overview

The Simple Holder strategy is a trading approach that involves periodically buying cryptocurrencies and holding them to achieve asset appreciation. The strategy primarily comprises three main components: periodic buy signals, hold signals, and exit signals.

## Strategy Principle 

The basic logic of the strategy is:

1. Send a buy signal at the start to make the first purchase.
2. Send a buy signal every certain number of candles to purchase more base currency using the quote currency.
3. When the candle count reaches a preset value, send an exit order to close the position.
4. Upon reaching the exit time, send an exit signal to stop the strategy and close all positions.

By repeatedly buying and holding cryptocurrencies, this approach aims to achieve cost averaging and continuous accumulation of holdings.

## Advantage Analysis

The advantages of this strategy include:

1. Regular purchases can reduce timing risk associated with cryptocurrency buys.
2. Repetitive buying helps lower the average holding cost of cryptocurrencies.
3. Continuous increase in positions can generate growth profits for the portfolio.
4. Customizable purchase and exit timings enable automated operation.
5. Simple to operate and easy to master.

## Risk Analysis

This strategy also involves certain risks:

1. Systematic risk from the cryptocurrency market, with potential large price fluctuations.
2. Inappropriate exit timing may prevent timely stop losses.
3. Poor capital management could lead to unaffordable losses.

## Optimization Suggestions

To optimize this strategy, consider the following improvements:

1. Dynamically adjust buy intervals and amounts based on market conditions.
2. Add stop loss signals to close positions when prices fall below support levels.
3. Incorporate more factors to determine optimal entry and exit points.

## Summary

The Simple Holder strategy achieves cost averaging and portfolio growth by periodically buying and holding cryptocurrencies. Once understood, it can be a relatively simple quantitative trading approach. Further optimizations can make the strategy more intelligent and adaptable to changing market conditions.

||

## Overview

The Simple Holder strategy is a strategy that periodically buys cryptocurrencies and holds them to achieve asset appreciation. The strategy mainly includes three parts: periodic buying signals, holding signals and exit signals.

## Strategy Principle 

The basic logic of the strategy is:

1. Send a buy signal at start to make the first purchase.
2. Send a buy signal every certain number of candles to purchase more base currency using the quote currency.
3. When candle count reaches preset value, send exit order to close position.
4. When exit time is reached, send exit signal to stop strategy and close all positions.

Through repetitive buying and holding of cryptocurrencies, the effects of cost averaging and continuous increasing of positions can be achieved.

## Advantage Analysis

The advantages of this strategy are:

1. Can periodically buy cryptocurrencies to reduce timing risk of purchases.
2. Can reduce average holding cost of cryptocurrencies through repetitive buying.
3. Can obtain growth profit of portfolio through continuously increasing positions.
4. Customizable purchase and exit timing enables automation.
5. Simple to operate and easy to master.

## Risk Analysis  

Risks of this strategy include:

1. Systematic risk of cryptocurrency market with potentially huge price swings.
2. Inappropriate exit timing may fail to timely stop loss.
3. Inadequate capital management may also lead to failure in bearing losses.

## Optimization Suggestions

The following aspects of the strategy can be optimized:

1. Dynamically adjust buying amount and intervals according to market conditions.
2. Add stop loss signals to close positions when price falls below support level.  
3. Incorporate more factors to determine the optimal entry and exit timing.

## Summary  

The Simple Holder strategy achieves the effect of cost averaging and portfolio growth through periodic buying and holding of cryptocurrencies. It is a relatively simple quantitative strategy once the usage is mastered. Incorporating further optimizations can enhance the strategy's intelligence and adaptability to changing market environments.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|7|(?Trade Range)Close at Candle Count:|
|v_input_1|timestamp(2023-09-21 16:30)|Start Date/Time|
|v_input_2|timestamp(2023-09-21 23:05)|End Date/Time|
|v_input_3|paste your message here|(?3Commas)Message to start bot and deal|
|v_input_4|paste your message here|Message for deal add funds signal in the quote currency|
|v_input_5|paste your message here|Message to cancel the deal|
|v_input_6|paste your message here|Message to cancel all bot deals and stop the bot|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2024-01-07 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Merdoc390

//@version=5

// The idea with this script is to use 3commas DCA bot to keep buying crypto, but not 'close the deal' which sells the crypto.

// Basic idea is to keep adding funds, which increases the buy.
// When you cancel the sale, you keep the crypto, thus HODL.
// I use this to build my positions that I short sale on Coinbase.com, so I need to cancel the deal after several candles so I can
// trade them.

// 3commas HODL DCA Bot article:
// https://3commas.io/blog/3commas-hodl-dca-bot-strategy
// This article includes the bot setup on 3Commas:
// Basicially you start the trade, then add funds to the trade, buying more crypto, then eventually cancel the deal.
// When you create the bot, you set the take profit really high, like 999%. Since it is unlikely to hit the value, it will never sell


// Credit to Irakli Gun as inspriation
// https://3commas.io/blog/3commas-hodl-dca-bot-strategy

strategy(title='HODL Simple v1', shorttitle="HODL'er", 
 calc_on_every_tick=false, calc_on_order_fills=true, process_orders_on_close =true,
 format=format.price, precision=4, overlay=true, pyramiding=365, 
 currency=currency.USD, default_qty_value=10, default_qty_type=strategy.cash , initial_capital=3650, 
 commission_type=strategy.commission.percent, commission_value=0.1)


var startFirstDeal = true
var done = false
var dealCount = 0
var totalDealCount = 0 


i_closeCount = input.int(defval=7,title="Close at Candle Count:",tooltip="How many buy candles to convert to a buy, otherwise it will remain open until end of timeframe.",group="Trade Range")
Start_date   = input(defval=timestamp('2023-09-21 16:30'),title="Start Date/Time",group="Trade Range")
Finish_date  = input(defval=timestamp('2023-09-21 23:05'),title="End Date/Time",group="Trade Range")

i_startBotAndDealMessage     = input(defval="paste your message here",title="Message to start bot and deal", tooltip="Message for 'start bot and deal",                        group="3Commas",displ