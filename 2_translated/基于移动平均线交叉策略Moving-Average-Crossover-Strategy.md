> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_2|13|Len|
|v_input_float_3|7|Take Profit %|
|v_input_float_4|7|Stop Loss %|
|v_input_1||(?entry)Signal Token|
|v_input_string_1|0|Order Type: market|limit|
|v_input_float_1|false|Order Price Offset|
|v_input_string_2|0|Investment Type: percentage_balance|contract|margin|percentage_investment|
|v_input_float_2|100|Amount|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-23 00:00:00
end: 2023-10-23 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
//@strategy_alert_message {{strategy.order.alert_message}} 
////////////////////////////////////////////////////////////
//  Copyright by HPotter v2.0 19/09/2023
// MA Crossover Bot for OKX Exchange
////////////////////////////////////////////////////////////
var ALERTGRP_CRED = "entry"
signalToken = input("", "Signal Token", inline = "11", group = ALERTGRP_CRED)
OrderType = input.string("market", "Order Type", options = ["market", "limit"], inline = "21", group = ALERTGRP_CRED)
OrderPriceOffset = input.float(0, "Order Price Offset", minval = 0, maxval = 100, step = 0.01, inline = "21", group = ALERTGRP_CRED)
InvestmentType = input.string("percentage_balance", "Investment Type", options = ["margin", "contract", "percentage_balance", "percentage_investment"], inline = "31", group = ALERTGRP_CRED)
Amount = input.float(100, "Amount", minval = 0.01, inline = "31", group = ALERTGRP_CRED)

getAlertMsg(action, instrument, signalToken, orderType, orderPriceOffset, investmentType, amount) =>
    str = '{'
    str := str + '"action": "' + action + '", '
    str := str + '"instrument": "' + instrument + '", '
    str := str + '"signalToken": "' + signalToken + '", '
    //str := s
```