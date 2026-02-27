> Name

RSI Trend Following Strategy with Trailing Stop Loss  
RSI-Trend-Following-Strategy-with-Trailing-Stop-Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/deb2c8f31adb212a04.png)
 [trans]
## Overview

This is a quantitative trading strategy that utilizes the RSI indicator to determine market trends and sets stop loss and take profit levels to lock in profits and minimize risks.

## Strategy Logic

The strategy primarily uses the RSI indicator to determine the direction of the market trend for long or short positions. When the RSI line crosses above the lower threshold, it is considered an upward trend, triggering a buy signal. Conversely, when the RSI line crosses below the upper threshold, it indicates a downward trend, triggering a sell signal.

Simultaneously, the strategy tracks the entry price of each trade and sets dynamic stop loss and take profit levels. For long trades, the entry price is set as the basis for calculating the stop loss level, while short trades use the entry price to determine the take profit level. When the price hits either line, the position will be automatically closed.

## Advantages

- Utilizes the RSI indicator to identify market trends and avoid trading in range-bound markets;
- Sets dynamic stop loss and take profit levels, providing flexible risk management and effective profit locking;
- RSI parameters and stop loss/take profit ratios can be adjusted externally for optimization.

## Risks 

- The RSI indicator may have some lag, potentially missing short-term trend reversals;  
- Stop loss and take profit lines that are set too close may be easily breached.

## Optimization

- Test the effectiveness of different periods with the RSI indicator;
- Explore different parameter combinations to find the optimal stop loss/take profit ratios;
- Incorporate additional indicators for filtering signals.

## Conclusion

Overall, this is a quantitative trading strategy that leverages the RSI indicator to track trends and incorporates dynamic stop loss and take profit levels. Compared to single-indicator strategies, it excels in managing risks by flexibly locking in profits. Further improvements can be achieved through parameter optimization and the addition of auxiliary indicators.

||

## Overview

This is a quantitative trading strategy that utilizes the RSI indicator to determine market trends and sets stop loss and take profit levels to lock in profits and minimize risks.

## Strategy Logic

The strategy primarily uses the RSI indicator to determine the direction of the market trend for long or short positions. When the RSI line crosses above the lower threshold, it is considered an upward trend, triggering a buy signal. Conversely, when the RSI line crosses below the upper threshold, it indicates a downward trend, triggering a sell signal.

Simultaneously, the strategy tracks the entry price of each trade and sets dynamic stop loss and take profit levels. For long trades, the entry price is set as the basis for calculating the stop loss level, while short trades use the entry price to determine the take profit level. When the price hits either line, the position will be automatically closed.

## Advantages

- Utilizes the RSI indicator to identify market trends and avoid trading in range-bound markets;
- Sets dynamic stop loss and take profit levels, providing flexible risk management and effective profit locking;
- RSI parameters and stop loss/take profit ratios can be adjusted externally for optimization.

## Risks 

- The RSI indicator may have some lag, potentially missing short-term trend reversals;  
- Stop loss and take profit lines that are set too close may be easily breached.

## Optimization

- Test the effectiveness of different periods with the RSI indicator;
- Explore different parameter combinations to find the optimal stop loss/take profit ratios;
- Incorporate additional indicators for filtering signals.

## Conclusion

Overall, this is a quantitative trading strategy that leverages the RSI indicator to track trends and incorporates dynamic stop loss and take profit levels. Compared to single-indicator strategies, it excels in managing risks by flexibly locking in profits. Further improvements can be achieved through parameter optimization and the addition of auxiliary indicators.

[/trans]

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_int_1|8|(?Signals)5 day input or RSI1|
|v_input_int_2|28|RSI Lower|
|v_input_int_3|72|RSI Upper |
|v_input_int_4|200|EMA Period|
|v_input_int_5|true|Look back days for close/open|
|v_input_int_6|5|(?Order Controls)max open orders|
|v_input_int_7|40|Buy breakout range|
|v_input_float_1|1.15|(?TPSL)Buy TP: 1+TP %, .05 seems to work well.|
|v_input_float_2|0.975|Sell TP: 1-TP%. .025 seems to work well. |
|v_input_bool_1|false|(?Alerts)Turns on Buy/Sell Alerts|
|v_input_bool_2|false|Use default Buy/Sell or the messages below|
|v_input_1|Buy|Buy signal API/TXT message template|
|v_input_2|Sell|Sell signal API/TXT message template|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// ©chewyScripts.

//@version=5
strategy("96er RSI+200EMA Strategy + Alerts", overlay=true, shorttitle = "The old 96er - RSI5 + 200 EMA")
//,use_bar_magnifier=false 
// This works best on a small account $100, with 50% of equity and up to 10 max open trades. 
// 96% Profitable, turns $100 into $350 in 1 month. very few losses. super happy with it.
// So far it triples the account on a 1m chart in 1 month back testing on the SEI-USD pair.
// I did not test on FX pairs or other instruments.
// had some issues with the inputs not working so had to hard code some, also the lastClose var sometimes breaks and starts following every candle, not sure why.

in_r1 = input.int(8,"5 day input or RSI1", group = "Signals")
in_lowerRSI = input.int(28,"RSI Lower", group = "Signals")
in_upperRSI = input.int(72,"RSI Upper ", group = "Signals")
in_emaperiod = input.int(200,"EMA Period", group = "Signals")
in_daysback = input.int(1,"Look back days for close/open", group = "Signals")

in_openOrders = input.int(5,"max open orders",tooltip = "Be careful, to high and you will get margin called!! 5 is probably the highest you should go", group = "Order Controls")
in_buybreakout = input.int(40,"Buy breakout range", group = "Order Controls")

in_buyTP = input.float(1.1500,"Buy TP: 1+TP %, .05 seems to work well.", group = "TPSL")
in_sellTP = input.float(0.9750, "Sell TP: 1-TP%. .025 seems to work well. ", group = "TPSL")

in_useAlerts = input.bool(false,"Turns on Buy/Sell Alerts",group = "Alerts")
in_useCustomAlertMSG = input.bool(false,"Use default Buy/Sell or the messages below",group = "Alerts")
in_alertBuySignalTxt = input("Buy","Buy signal API/TXT message template", tooltip = "Review the UserGuid on JSON varibles in alerts", group = "Alerts")
in_alertSellSignalTxt = input("Sell","Sell signal API/TXT message template", tooltip = "Review the UserGuid on JSON varibles in alerts", group = "Alerts")

simple int rsi5 = in_r1

// 3 rsi strategy , when all of them are overbought we sell, and vice versa
rsi7 = ta.rsi(close,rsi5)
[lastOpen, lastClose] = request.security(syminfo.tickerid, "D", [open,close],
```