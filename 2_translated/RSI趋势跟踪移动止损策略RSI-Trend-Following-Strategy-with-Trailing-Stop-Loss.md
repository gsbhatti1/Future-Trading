> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_3|true|Start Date|
|v_input_int_4|6|Start Month|
|v_input_int_5|2022|Start Year|
|v_input_1|2|Return Precision|
|v_input_int_1|4|(?RSI Settings)RSI Length|
|v_input_source_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_string_1|0|(?MA Settings)MA Type: SMA|Bollinger Bands|EMA|SMMA (RMA)|WMA|VWMA|
|v_input_int_2|23|MA Length|
|v_input_float_1|2|BB StdDev|


> Source (PineScript)

``` pinescript
// © CRabbit
//@version=5

// Starting with $100 and using 10% of the account per trade
strategy("RSI Template", shorttitle="RSI", overlay=false, initial_capital=100, default_qty_value=10, default_qty_type=strategy.percent_of_equity)

// RSI Indicator
ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "Bollinger Bands" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

rsiLengthInput = input.int(4, minval=1, title="RSI Length", group="RSI Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
maLengthInput = input.int(23, minval=1, title="MA Length", group="MA Settings")
bbStdDevInput = input.float(2.0, title="BB StdDev", group="Bollinger Bands")

// Strategy Logic
longCondition = rsi(rsiSourceInput, rsiLengthInput) > 68 and ta.crossover(sma(close, maLengthInput), sma(close, maLengthInput - 1))
shortCondition = rsi(rsiSourceInput, rsiLengthInput) < 28 and ta.crossunder(sma(close, maLengthInput), sma(close, maLengthInput - 1))

// Place Orders
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Stop Loss and Take Profit Settings
strategy.exit("Long Exit", "Long", stop=ta.valuewhen(longCondition, close * (1 - bbStdDevInput / 100), 1))
strategy.exit("Short Exit", "Short", stop=ta.valuewhen(shortCondition, close * (1 + bbStdDevInput / 100), 1))

// Take Profit Settings
takeProfitLong = ta.valuewhen(longCondition, close * (1.4 / 100), 1)
strategy.exit("Take Profit Long", "Long", limit=takeProfitLong)

takeProfitShort = ta.valuewhen(shortCondition, close * (0.8 / 100), 1)
strategy.exit("Take Profit Short", "Short", limit=takeProfitShort)

// Stop Loss Settings
stopLossLong = ta.valuewhen(longCondition, close * (2 / 100), 1)
strategy.exit("Stop Loss Long", "Long", stop=stopLossLong)

stopLossShort = ta.valuewhen(shortCondition, close * (2 / 100), 1)
strategy.exit("Stop Loss Short", "Short", stop=stopLossShort)
```