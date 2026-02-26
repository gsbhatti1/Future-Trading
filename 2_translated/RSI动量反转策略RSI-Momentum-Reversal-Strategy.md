> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|false|Use Martingale|
|v_input_4|100|Capital, %|
|v_input_5|true|Use CRSI Strategy|
|v_input_6|true|Use FRSI Strategy|
|v_input_7|true|CRSI+FRSI Mode|
|v_input_8|25|RSI limit|
|v_input_9|true|Use Body-filter|
|v_input_10|true|Use Color-filter|
|v_input_11|1900|From Year|
|v_input_12|2100|To Year|
|v_input_13|true|From Month|
|v_input_14|12|To Month|
|v_input_15|true|From day|
|v_input_16|31|To day|


> Source (PineScript)

```pinescript
// Strategy Arguments
strategy("RSI Momentum Reversal Strategy", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=10000, pyramiding=0)

v_input_1 = input(true, title="Long")
v_input_2 = input(true, title="Short")
v_input_3 = input(false, title="Use Martingale")
v_input_4 = input(100, title="Capital, %")
v_input_5 = input(true, title="Use CRSI Strategy")
v_input_6 = input(true, title="Use FRSI Strategy")
v_input_7 = input(true, title="CRSI+FRSI Mode")
v_input_8 = input(25, title="RSI limit")
v_input_9 = input(true, title="Use Body-filter")
v_input_10 = input(true, title="Use Color-filter")
v_input_11 = input(1900, title="From Year")
v_input_12 = input(2100, title="To Year")
v_input_13 = input(true, title="From Month")
v_input_14 = input(12, title="To Month")
v_input_15 = input(true, title="From day")
v_input_16 = input(31, title="To day")

// Connors RSI
connors_rsi = rsi(close, 14)
rsi_win_ratio = (high - low) / volume
rsi_parisian = ((close[2] - open[2]) + (close[1] - open[1])) > 0 ? 1 : 0
crsi = (connors_rsi + rsi_win_ratio + rsi_parisian) / 3

// Fast RSI
frsi = rsi(close, v_input_8)

// Candlestick body filter
body_filter = close > open and v_input_9 == true

// Color filter
color_filter = color.red if close < open else color.green

// Strategy conditions
if (crsi < 20 and frsi < v_input_8 and body_filter)
    strategy.entry("Long", strategy.long)

if (crsi > 80 and frsi > v_input_8 and not(body_filter))
    strategy.exit("Short", "Long")

// Stop loss exit
stop_loss = close * 0.95
strategy.exit("Stop Loss", "Long", stop=stop_loss)
```
```