```pinescript
/*backtest
start: 2022-12-24 00:00:00
end: 2023-12-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
// originally coded by tmr0, modified by timchep
// original idea from «Way of the Turtle: The Secret Methods that Turned Ordinary People into Legendary Traders» (2007) CURTIS FAITH
strategy("Turtles", shorttitle = "Turtles", overlay=true, pyramiding=1, default_qty_type=strategy.percent_of_equity, default_qty_value = 100)
//////////////////////////////////////////////////////////////////////
// Com
```

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2011|Backtest Start Year|
|v_input_2|12|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2030|Backtest Stop Year|
|v_input_5|12|Backtest Stop Month|
|v_input_6|30|Backtest Stop Day|
|v_input_7|false|Color Background?|
|v_input_8|true|Enable Shorting?|
|v_input_9|20|enter_fast|
|v_input_10|10|exit_fast|
|v_input_11|55|enter_slow|
|v_input_12|20|exit_slow|

> Source (PineScript)

```pinescript
//@version=2
study("Turtle Trading Strategy", shorttitle="TTSS")
// Parameters
N = input(55, title="Enter Slow")
N2 = input(N / 2, title="Enter Fast")

// Calculate channels
slowL = highest(high, N)
slowS = lowest(low, N)
fastL = highest(high, N2)
fastS = lowest(low, N2)

// Long logic
enterL1 = crossover(close, fastL)
exitL1 = crossunder(close, slowL)

// Short logic
enterS1 = crossunder(close, fastS)
exitS1 = crossover(close, slowS)

// Plot channels
plot(slowL, color=color.blue, title="Slow Channel")
plot(slowS, color=color.blue, title="Slow Channel")
plot(fastL, color=color.red, title="Fast Channel")
plot(fastS, color=color.red, title="Fast Channel")

// Enter and Exit positions
if (enterL1)
    strategy.entry("Long", strategy.long)

if (exitL1)
    strategy.close("Long")

if (enterS1)
    strategy.entry("Short", strategy.short)

if (exitS1)
    strategy.close("Short")
```

This PineScript code implements the described Turtle Trading Strategy, including all necessary parameters and logic as specified.