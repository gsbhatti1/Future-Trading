> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|14|Length|
|v_input_2|27|Buy Level 1|
|v_input_3|18|Buy Level 2|
|v_input_4|68|Sell Level 1|
|v_input_5|80|Sell Level 2|
|v_input_6|2500|Target Pips|
|v_input_7|5000|Stop Pips|
|v_input_8|true|Lot Size|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-16 00:00:00
end: 2023-10-16 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Rawadabdo

// Ramy's Algorithm

//@version=5
strategy("BTC/USD - RSI", overlay=false, initial_capital = 5000)

// User input
length = input(title = "Length", defval=14, tooltip="RSI period")

first_buy_level = input(title = "Buy Level 1", defval=27, tooltip="Level where 1st buy triggers")
second_buy_level = input(title = "Buy Level 2", defval=18, tooltip="Level where 2nd buy triggers")

first_sell_level = input(title = "Sell Level 1", defval=68, tooltip="Level where 1st sell triggers")
second_sell_level = input(title = "Sell Level 2", defval=80, tooltip="Level where 2nd sell triggers")

takeProfit = input(title="Target Pips", defval=2500, tooltip="Fixed pip take profit distance")
stopLoss = input(title="Stop Pips", defval=5000, tooltip="Fixed pip stop loss distance")

lot = input(title = "Lot Size", defval = 1, tooltip="Trading Lot size")

// Get RSI
vrsi = ta.rsi(close, length)

// Entry Conditions
long1 = (vrsi <= first_buy_level and vrsi > second_buy_level)
long2 = (vrsi <= second_buy_level)

short1 = (vrsi >= first_sell_level and vrsi < second_sell_level)
short2 = (vrsi >= second_sell_level)


// Entry Orders
// Buy Orders
if (long1 and strategy.position_size == 0)
    strategy.entry("Long", strategy.long, qty=lot, comment="Buy")
    if (long2 and strategy.position_size > 0)
        strategy.exit("Long Exit", "Long", profit=takeProfit, loss=stopLoss)

// Sell Orders
if (short1 and strategy.position_size == 0)
    strategy.entry("Short", strategy.short, qty=lot, comment="Sell")
    if (short2 and strategy.position_size > 0)
        strategy.exit("Short Exit", "Short", profit=takeProfit, loss=stopLoss)

// Close Positions When RSI Leaves Signal Range
if not long1 and not long2 and strategy.long_position_size != 0
    strategy.close("Long")
if not short1 and not short2 and strategy.short_position_size != 0
    strategy.close("Short")
```

This PineScript code defines the trading strategy as described in the document, with proper corrections for syntax issues.