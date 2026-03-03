> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|(?Bollinger Bands)length|
|v_input_string_1|0|Basis MA Type: SMA|EMA|SMMA (RMA)|WMA|VWMA|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_float_1|2|StdDev|
|v_input_int_2|false|Offset|
|v_input_bool_1|true|(?Strategy)Long|
|v_input_bool_2|true|Short|
|v_input_float_2|3|Target Multiplier (X)|
|v_input_string_2||(?AUTOMATION)Token|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-24 00:00:00
end: 2024-01-31 00:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(shorttitle="BB Strategy", title="Bollinger Bands Strategy", overlay=true)
length = input.int(20, minval=1, group = "Bollinger Bands")
maType = input.string("SMA", "Basis MA Type", options = ["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group = "Bollinger Bands")
src = input(close, title="Source", group = "Bollinger Bands")
mult = input.float(2.0, minval=0.001, maxval=50, title="StdDev", group = "Bollinger Bands")

ma(source, length, _type) =>
    switch _type
        "SMA" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

basis = ma(src, length, maType)
dev = mult * ta.stdev(src, length)
upper = basis + dev
lower = basis - dev
offset = input.int(0, "Offset", minval = -500, maxval = 500, group = "Bollinger Bands")
plot(basis, "Basis", color=#FF6D00, offset = offset)
p1 = plot(upper, "Upper", color=#2962FF, offset = offset)
p2 = plot(lower, "Lower", color=#2962FF, offset = offset)
fill(p1, p2, title = "Background", color=color.rgb(33, 150, 243, 95))

lo = input.bool(true, "Long", group = "Strategy")
sh = input.bool(true, "Short", group = "Strategy")
x = input.float(3.0, "Target Multiplier (X)", group = "Strategy", minval = 1.0, step = 0.1)
token = input.string(defval = "", title = "Token", group = "AUTOMATION")

Buy_CE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(1) + '"}'
Buy_PE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(2) + '"}'
Exit_CE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(-1) + '"}'
Exit_PE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(-2) + '"}'
Exit_PE_CE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(2.5) + '"}'
Exit_CE_PE = '{"auth-token":"' + token + '","key":"Value1","value":"' + str.tostring(1.5) + '"}'

long = high < lower
short = low > upper

var sl_b = 0.0
var tar_b = 0.0
var sl_s = 0.0
var tar_s = 0.0
var static_sl = 0.0
entry = strategy.opentrades.entry_price(strategy.opentrades - 1)

if long and lo and strategy.position_size == 0
    strategy.entry("Long", strategy.long, alert_message = Buy_CE, stop = high)
    sl_b := high - x * dev
    tar_b := low + x * dev

if short and sh and strategy.position_size == 0
    strategy.entry("Short", strategy.short, alert_message = Buy_PE, stop = low)
    sl_s := low + x * dev
    tar_s := high - x * dev

static_sl := if na(static_sl) or (strategy.opentrades > 1 and static_sl < lower)
    lower
else
    static_sl

if strategy.position_size != 0
    strategy.exit("LX", "Long", stop = static_sl, profit = (math.abs(...))
```

This translation maintains the original code format and arguments while translating the human-readable text.