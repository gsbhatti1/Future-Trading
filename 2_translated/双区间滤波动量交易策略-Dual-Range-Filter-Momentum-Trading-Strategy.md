> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_string_1|0|İşlem Yönü: Alis|Satis|Tum|
|v_input_int_1|true|İlk ay|
|v_input_int_2|true|İlk Gün|
|v_input_int_3|2023|İlk Yil|
|v_input_int_4|true|Son Ay|
|v_input_int_5|true|Son Gün|
|v_input_int_6|9999|Son Yıl|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|true|Show Buy/Sell Signals ?|
|v_input_int_7|27|Fast period|
|v_input_float_1|1.6|Fast range|
|v_input_int_8|55|Slow period|
|v_input_float_2|2|Slow range|
|v_input_3|true|Mum Renk Ayarları?|
|v_input_4|true|Trend Bazlı Mum Rengi Değişimi?|
|v_input_float_3|100|Zarar Kes Yüzdesi|
|v_input_int_9|5|Satış Lot Sayısı 1.Kısım %|
|v_input_int_10|8|Satış Lot Sayısı 2.Kısım %|
|v_input_int_11|13|Satış Lot Sayısı 3.Kısım %|
|v_input_int_12|21|Satış Lot Sayısı 4.Kısım %|
|v_input_float_4|13|Kar Yüzdesi 1.Kısım|
|v_input_float_5|21|Kar Yüzdesi 2.Kısım|
|v_input_float_6|29|Kar Yüzdesi 3.Kısım|
|v_input_float_7|34|Kar Yüzdesi 4.Kısım|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License (MPL) v2.0.
// The source code is provided "as is" and without any warranty.
// You can obtain a copy of the MPL at http://www.mozilla.org/MPL/2.0/.

//@version=5
indicator("Dual-Range-Filter-Momentum-Trading-Strategy", shorttitle="DRF MT", overlay=true)

// Input Arguments
var input_string_1 = input.string("Alis", title="Operation Direction: Buy|Sell|All", options=["Alis", "Satis", "Tum"])
var input_int_1 = input(true, title="First Month")
var input_int_2 = input(true, title="First Day")
var input_int_3 = input(2023, title="First Year")
var input_int_4 = input(true, title="Last Month")
var input_int_5 = input(true, title="Last Day")
var input_int_6 = input(9999, title="Last Year")
var input_1_close = input(close, title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4")
var input_2 = input(true, title="Show Buy/Sell Signals?")
var input_int_7 = input(27, title="Fast period")
var input_float_1 = input(1.6, title="Fast range")
var input_int_8 = input(55, title="Slow period")
var input_float_2 = input(2, title="Slow range")
var input_3 = input(true, title="Bar Color Settings?")
var input_4 = input(true, title="Trend-Based Bar Color Change?")
var input_float_3 = input(100, title="Loss Cut Percentage")
var input_int_9 = input(5, title="Sell Lot Quantity 1st Segment %")
var input_int_10 = input(8, title="Sell Lot Quantity 2nd Segment %")
var input_int_11 = input(13, title="Sell Lot Quantity 3rd Segment %")
var input_int_12 = input(21, title="Sell Lot Quantity 4th Segment %")
var input_float_4 = input(13, title="Profit Percentage 1st Segment")
var input_float_5 = input(21, title="Profit Percentage 2nd Segment")
var input_float_6 = input(29, title="Profit Percentage 3rd Segment")
var input_float_7 = input(34, title="Profit Percentage 4th Segment")

// Strategy Logic
var fast_period = input_int_7
var fast_range = input_float_1
var slow_period = input_int_8
var slow_range = input_float_2

// Calculate TRF
trf = ta.ema(input_1_close, fast_period) + (ta.ema(input_1_close, fast_period) * fast_range) - (ta.ema(input_1_close, slow_period) + (ta.ema(input_1_close, slow_period) * slow_range))

// Buy/Sell Signal
if (input_2)
    if (close > trf)
        strategy.entry("Buy", strategy.long)
    if (close < trf)
        strategy.entry("Sell", strategy.short)

// Plot TRF
plot(trf, color=color.blue, title="TRF")

// Plot Buy/Sell Signals
if (input_2)
    plotshape(series=strategy.position.entry_price("Buy"), location=location.belowbar, color=color.green, style=shape.labelup, title="Buy Signal")
    plotshape(series=strategy.position.exit_price("Sell"), location=location.abovebar, color=color.red, style=shape.labeldown, title="Sell Signal")

// Stop Loss and Take Profit
if (strategy.position_size > 0)
    strategy.exit("Take Profit 1", from_entry="Buy", limit=trf * (1 + input_float_4 / 100))
    strategy.exit("Take Profit 2", from_entry="Buy", limit=trf * (1 + input_float_5 / 100))
    strategy.exit("Take Profit 3", from_entry="Buy", limit=trf * (1 + input_float_6 / 100))
    strategy.exit("Take Profit 4", from_entry="Buy", limit=trf * (1 + input_float_7 / 100))
    strategy.exit("Stop Loss", from_entry="Buy", stop=trf * (1 - input_float_3 / 100))
```