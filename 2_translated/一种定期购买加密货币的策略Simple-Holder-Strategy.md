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
// Basically you start the trade, then add funds to the trade, buying more crypto, then eventually cancel the deal.
// When you create the bot, you set the take profit really high, like 999%. Since it is unlikely to hit the value, it will never sell

// Credit to Irakli Gun as inspiration
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

i_startBotAndDealMessage     = input(defval="paste your message here",title="Message to start bot and deal", tooltip="Message for 'start bot and deal'",                        group="3Commas")
i_addFundsMessage            = input(defval="paste your message here",title="Message for deal add funds signal in the quote currency",tooltip="Message for deal add funds signal in the quote currency",group="3Commas")
i_cancelDealMessage          = input(defval="paste your message here",title="Message to cancel the deal", tooltip="Message to cancel the deal", group="3Commas")
i_cancelAllBotDealsMessage   = input(defval="paste your message here",title="Message to cancel all bot deals and stop the bot",tooltip="Message to cancel all bot deals and stop the bot",group="3Commas")

// Your Pine Script code continues here
```