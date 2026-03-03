> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|timestamp(01 Jan 2021 00:00 UTC)|From Date|
|v_input_2|timestamp(31 Dec 2121 23:59 UTC)|To Date|
|v_input_int_1|23|Fast SMA Length|
|v_input_int_2|50|Slow SMA Length|
|v_input_float_1|0.5|Long Take Profit %|
|v_input_float_2|0.5|Short Take Profit %|
|v_input_bool_1|true|Enable Trailing|
|v_input_float_3|0.01|Trailing Take Profit %|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-08-23 00:00:00
end: 2023-09-22 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='Joker Trailing TP Bot', shorttitle='Joker TTP Bot', overlay=true, pyramiding=0, process_orders_on_close=false, close_entries_rule='ANY', calc_on_every_tick=false, calc_on_order_fills=false, commission_type=strategy.commission.percent, commission_value=0.07, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000, currency=currency.USD) //, max_labels_count=500)

fromDate = input(timestamp('01 Jan 2021 00:00 UTC'), 'From Date')
toDate = input(timestamp('31 Dec 2121 23:59 UTC'), 'To Date')
fastMALen = input.int(23, 'Fast SMA Length')
slowMALen = input.int(50, 'Slow SMA Length')
longTakeProfitPerc = input.float(0.5, 'Long Take Profit %')
shortTakeProfitPerc = input.float(0.5, 'Short Take Profit %')
enableTrailing = input.bool(true, 'Enable Trailing')
trailingTakeProfitPerc = input.float(0.01, 'Trailing Take Profit %')

// Define the strategy logic
if (time >= fromDate and time <= toDate)
    // Calculate signals based on moving averages
    fastSMA = sma(close, fastMALen)
    slowSMA = sma(close, slowMALen)

    longSignal = ta.crossover(fastSMA, slowSMA)
    shortSignal = ta.crossunder(fastSMA, slowSMA)

    // Place orders based on signals
    if (longSignal and not enableTrailing)
        strategy.entry('Long', strategy.long)
        takeProfitPrice = na
    else if (longSignal and enableTrailing)
        strategy.entry('Long', strategy.long)
        takeProfitPrice = close * (1 + longTakeProfitPerc)

    if (shortSignal and not enableTrailing)
        strategy.entry('Short', strategy.short)
        takeProfitPrice = na
    else if (shortSignal and enableTrailing)
        strategy.entry('Short', strategy.short)
        takeProfitPrice = close * (1 - shortTakeProfitPerc)

    // Trailing stop for long positions
    if (strategy.position_size > 0 and enableTrailing)
        strategy.exit(id='Long TP', from_entry='Long', limit=takeProfitPrice + trailingTakeProfitPerc * close, trail_offset=trailingTakeProfitPerc * close)
    
    // Trailing stop for short positions
    if (strategy.position_size < 0 and enableTrailing)
        strategy.exit(id='Short TP', from_entry='Short', limit=takeProfitPrice - trailingTakeProfitPerc * close, trail_offset=trailingTakeProfitPerc * close)

```