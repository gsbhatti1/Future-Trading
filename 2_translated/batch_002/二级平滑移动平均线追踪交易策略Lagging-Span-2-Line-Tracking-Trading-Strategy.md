> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|52|Lead Look Back|
|v_input_int_2|26|Displacement|
|v_input_bool_1|false|Sadece Long Yönlü Poz Aç|
|v_input_int_3|10000|Long Kar Al Puanı|
|v_input_int_4|7500|Long Zarar Durdur Puanı|
|v_input_int_5|20000|Short Kar Al Puanı|
|v_input_int_6|7500|Short Zarar Durdur Puanı|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-25 00:00:00
end: 2024-01-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © MGULHANN

//@version=5
strategy("TPS - FX Trade", overlay=true)

laggingSpan2Periods = input.int(52, minval=1, title="Lead Look Back")
displacement = input.int(26, minval=1, title="Displacement")

pozyonu = input.bool(false,title="Sadece Long Yönlü Poz Aç")

// Stop Loss ve Kar Al Seviye Girişleri
TPLong = input.int(10000, minval = 30, title ="Long Kar Al Puanı", step=10)
SLLong = input.int(7500, minval = 30, title ="Long Zarar Durdur Puanı", step=10)
TPShort = input.int(20000, minval = 30, title ="Short Kar Al Puanı", step=10)
SLShort = input.int(7500, minval = 30, title ="Short Zarar Durdur Puanı", step=10)

donchianHigh = ta.highest(high, laggingSpan2Periods + displacement)
donchianLow = ta.lowest(low, laggingSpan2Periods + displacement)

longCondition = close > donchianLow
shortCondition = close < donchianHigh

if (pozyonu == false)
    if (longCondition and not strategy.opentrades)
        strategy.entry("Long", strategy.long)
        
        // Stop Loss and Take Profit for Long Position
        if (close >= TPLong)
            strategy.exit("Exit Long TP", "Long")
            
        if (close <= SLLong)
            strategy.exit("Exit Long SL", "Long")

    if (shortCondition and not strategy.opentrades)
        strategy.entry("Short", strategy.short)

        // Stop Loss and Take Profit for Short Position
        if (close <= -TPShort)
            strategy.exit("Exit Short TP", "Short")
            
        if (close >= -SLShort)
            strategy.exit("Exit Short SL", "Short")

// Plotting the Donchian Channels
plot(donchianHigh, color=color.blue, linewidth=2)
plot(donchianLow, color=color.red, linewidth=2)

```

Note: The Pine Script was translated to maintain the structure and meaning of the original code. Adjustments were made for clarity in English, but the core logic remains intact.