``` pinescript
/*backtest
start: 2022-10-01 00:00:00
end: 2023-10-07 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 04/01/2018
//    Trend continuation factor, by M.H. Pee 
//    The related article is copyrighted material from Stocks & Commodities.
//
//You can change long to short in the Input Settings
//WARNING:
//- For purpose educate only
//- This script to change bars colors.
////////////////////////////////////////////////////////////
strategy(title="Momentum-Trend-Continuation-Factor-Strategy")
Length = input(35, minval=1)
reverse = input(false, title="Reverse trade direction")
hline(0, color=
```

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|35|Length|
|v_input_2|false|Trade reverse|


> Source (PineScript)

``` pinescript
//@version=2
strategy(title="Momentum-Trend-Continuation-Factor-Strategy")
Length = input(35, minval=1)
reverse = input(false, title="Reverse trade direction")
hline(0, color=
```