> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|120|Timeframe|
|v_input_2|25|Long Length|
|v_input_3|13|Short Length|
|v_input_4|13|Signal Length|
|v_input_5|300|Period|
|v_input_6|true|From Month|
|v_input_7|true|From Day|
|v_input_8|2017|From Year|
|v_input_9|true|To Month|
|v_input_10|true|To Day|
|v_input_11|9999|To Year|


> Source (PineScript)

```pinescript
//backtest
//start: 2023-01-01 00:00:00
//end: 2024-01-07

//@version=5
strategy("Momentum Dual Moving Window TSI Indicator Strategy", overlay=true)

timeframe = input.int(120, title="Timeframe")
longLength = input.int(25, title="Long Length")
shortLength = input.int(13, title="Short Length")
signalLength = input.int(13, title="Signal Length")
period = input.int(300, title="Period")

// Helper functions
smooth = ta.sma
double_smooth = lambda pc, l, s: smooth(smooth(pc, l), s)

// Calculate price changes
pc = change(close)

// Double smoothed price changes and absolute values
double_smoothed_pc = double_smooth(pc, longLength, shortLength)
double_smoothed_abs_pc = double_smooth(abs(pc), longLength, shortLength)

// TSI value
tsi_value = 100 * (double_smoothed_pc / double_smoothed_abs_pc)

plot(tsi_value, title="TSI Value", color=color.blue)

// Buy and sell signals
buy_signal = ta.crossover(tsi_value, sma(tsi_value, signalLength))
sell_signal = ta.crossunder(tsi_value, sma(tsi_value, signalLength))

strategy.entry("Buy", when=buy_signal)
strategy.close("Buy", when=sell_signal)
```
```