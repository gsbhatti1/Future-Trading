> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_float_1|true|Take Profit %|
|v_input_float_2|true|Stop Loss %|
|v_input_int_1|10|BB Periods|
|v_input_float_3|true|Deviations|
|v_input_int_2|12|fastLength|
|v_input_int_3|26|slowLength|
|v_input_int_4|9|signalLength|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// AK MACD BB 
strategy("AK MACD BB strategy", overlay = true)

// Inputs for TP and SL
tp_percent = input.float(1.0, title="Take Profit %") / 100
sl_percent = input.float(1.0, title="Stop Loss %") / 100

length = input.int(10, minval=1, title="BB Periods")
dev = input.float(1, minval=0.0001, title="Deviations")

// MACD
fastLength = input.int(12, minval=1, title="Fast Length") 
slowLength = input.int(26, minval=1)
signalLength = input.int(9, minval=1)
fastMA = ta.ema(close, fastLength)
slowMA = ta.ema(close, slowLength)
macd = fastMA - slowMA

// Bollinger Bands
Std = ta.stdev(macd, length)
Upper = (Std * dev + ta.sma(macd, length))
Lower = (ta.sma(macd, length) - Std * dev)

Band1 = plot(Upper, color=color.gray, style=plot.style_line, linewidth=2, title="Upper Band")
Band2 = plot(Lower, color=color.gray, style=plot.style_line, linewidth=2, title="Lower Band")

// Trading logic
if (macd > Upper)
    strategy.entry("Long", strategy.long)

if (macd < Lower)
    strategy.entry("Short", strategy.short)

stopLossLevel = sl_percent * close
takeProfitLevel = tp_percent * close

strategy.exit("Long Exit", from_entry="Long", stop=stopLossLevel, limit=takeProfitLevel)
strategy.exit("Short Exit", from_entry="Short", stop=stopLossLevel, limit=takeProfitLevel)
```

This PineScript code implements the MACD BB Breakout Strategy as described. It calculates the MACD and Bollinger Bands indicators and uses them to generate trade signals based on crossing the upper or lower Bollinger Bands. The strategy also sets up take profit and stop loss levels for each entry.