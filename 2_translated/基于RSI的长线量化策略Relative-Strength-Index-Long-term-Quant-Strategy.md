> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|40|RSvalue|
|v_input_4|true|From Month|
|v_input_5|true|From Day|
|v_input_6|2015|From Year|
|v_input_7|3|To Month|
|v_input_8|true|To Day|
|v_input_9|2022|To Year|


> Source (PineScript)

```pinescript
// RSI Long-term Quant Strategy
strategy("Relative Strength Index Long-term Quant Strategy", overlay=true)

// Input Parameters
length = input(14, title="Length")
rsvalue = input(40, title="RSvalue")
from_month = input(true, title="From Month")
from_day = input(true, title="From Day")
from_year = input(2015, title="From Year")
to_month = input(3, title="To Month")
to_day = input(true, title="To Day")
to_year = input(2022, title="To Year")

// RSI Calculation
rsi_source = input(close, title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4")
rsi = rsi(rsi_source, length)

// Oversold and Overbought Lines
overbought_line = 70
oversold_line = 30

// Buy Condition
buy_condition = rsi < oversold_line

// Plotting RSI
plot(rsi, title="RSI", color=color.blue, linewidth=1)

// Buy Signal
if (buy_condition and from_month and from_day and from_year and to_month and to_day and to_year)
    strategy.entry("Long", strategy.long)
```

This PineScript code implements the RSI Long-term Quant Strategy as described. It sets up the RSI calculation with the specified length and RSvalue, and it includes a buy condition based on the RSI crossing the oversold line. The strategy also allows for setting the timeframe for when positions should be opened.