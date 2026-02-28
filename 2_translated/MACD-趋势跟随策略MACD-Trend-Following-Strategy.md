> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|false|Short|
|v_input_3|false|Use EMA filter|
|v_input_4|5|EMA filter period|
|v_input_5|12|fastLength|
|v_input_6|26|slowlength|
|v_input_7|9|MACDLength|


> Source (PineScript)

```pinescript
// backtest
// start: 2022-11-14 00:00:00
// end: 2023-10-27 05:00:00

//@version=5
strategy("MACD Trend Following Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

long = input(true, title="Long")
short = input(false, title="Short")
use_ema_filter = input(false, title="Use EMA filter")
ema_filter_period = input(5, minval=1, title="EMA filter period")
fastLength = input(12, minval=1, title="Fast EMA Length")
slowlength = input(26, minval=1, title="Slow EMA Length")
macdLength = input(9, minval=1, title="MACD Length")

[macdLine, signalLine, _] = ta.macd(close, fastLength, slowlength, macdLength)

delta = macdLine - signalLine

longCondition = delta > 0 and close > ta.ema(close, ema_filter_period)
shortCondition = delta < 0 and close < ta.ema(close, ema_filter_period)

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.close("Long")

plot(macdLine, title="MACD Line", color=color.blue)
plot(signalLine, title="Signal Line", color=color.red)
plot(delta, title="Delta", color=color.green)

```
```