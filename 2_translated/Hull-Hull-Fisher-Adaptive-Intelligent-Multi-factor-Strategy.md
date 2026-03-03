> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|HullMA Length|
|v_input_2|9|Signal Length|
|v_input_3|5|Top Line|
|v_input_4|-5|Bottom Line|
|v_input_5_open|0|Price data: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|true|Open when HullFisher crossover outside Lines|
|v_input_7|true|Open when HullFisher past zero|
|v_input_8|true|Include Hull_moving_average|
|v_input_9|true|Include Commodity_channel_index|
|v_input_10|true|Close order when Fisher crossover|
|v_input_11|true|Close order when Hull crossover|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-09 00:00:00
end: 2024-01-15 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is free to copy/paste/use. No permission required. Just do it!
// © @SeaSide420 
//@version=4
strategy(title="Hull Fisher", currency="USD", default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.25)

//=================================== Inputs =========================================================
period = input(title="HullMA Length", type=input.integer, defval=14, minval=2)
length = input(9, minval=1, title="Signal Length")
line1 = input(5, minval=2, title="Top Line")
line5 = input(-5, maxval=-2, title="Bottom Line")
price = input(open, type=input.source, title="")
```

Please note that the `title` attribute in the last line is incomplete. It should be completed with the appropriate text to represent "Price data" as mentioned in the default value description for `v_input_5_open`.