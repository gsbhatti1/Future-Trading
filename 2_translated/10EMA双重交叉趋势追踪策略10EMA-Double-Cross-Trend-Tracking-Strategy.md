> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|10|short ema|
|v_input_int_2|50|long ema|
|v_input_int_3|200|hourly 10 ema|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_4|false|Offset|


> Source (PineScript)

```pinescript
//@version=5
strategy("10EMA-Double-Cross-Trend-Tracking-Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

short_ema = input.int(10, title="short ema")
long_ema = input.int(50, title="long ema")
hourly_10ema = input.int(200, title="hourly 10 ema")
source = input(close, title="Source")
offset = input(false, title="Offset")

// Calculate EMAs
short_emac = ta.ema(source, short_ema)
long_emac = ta.ema(source, long_ema)
hourly_emac = ta.ema(source, hourly_10ema)

// Golden Cross and Death Cross logic
golden_cross = ta.crossover(short_emac, long_emac) and not offset
death_cross = ta.crossunder(short_emac, long_emac) and not offset

var float entry_price = na
var int entry_bar_index = na

if (golden_cross)
    if (not na(entry_price))
        strategy.close("Long", when=bar_index > entry_bar_index + 4)
    
    entry_price := close
    entry_bar_index := bar_index
    strategy.entry("Long", strategy.long)

if (death_cross)
    if (not na(entry_price))
        strategy.close("Short", when=bar_index > entry_bar_index + 4)
    
    entry_price := close
    entry_bar_index := bar_index
    strategy.entry("Short", strategy.short)

// Tracking Stop Loss and Limit Profit Logic
long_stop_loss = ta.valuewhen(strategy.opentrades.entry_bar_index(0) == entry_bar_index, entry_price - (entry_price * 0.01), 0)
short_stop_loss = ta.valuewhen(strategy.opentrades.entry_bar_index(0) == entry_bar_index, entry_price + (entry_price * 0.01), 0)

strategy.exit("Long Exit", "Long", stop=long_stop_loss)
strategy.exit("Short Exit", "Short", stop=short_stop_loss)

// Plot EMAs
plot(short_emac, color=color.blue, title="short ema")
plot(long_emac, color=color.red, title="long ema")
plot(hourly_emac, color=color.orange, title="hourly 10ema")
```
```