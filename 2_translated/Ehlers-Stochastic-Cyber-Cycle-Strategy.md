> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_hl2|0|Source: hl2|high|low|open|close|hlc3|hlcc4|ohlc4|
|v_input_2|0.07|Alpha|
|v_input_3|9|Lag|
|v_input_4|8|Stochastic len|
|v_input_5|true|oppositeTrade|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-09 00:00:00
end: 2024-01-16 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("Ehlers Stochastic Cyber Cycle Strategy", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100.0, pyramiding=1, commission_type=strategy.commission.percent, commission_value=0.1)
src = input(hl2, title="Source") 
alpha = input(0.07, title="Alpha")
lag = input(9, title="Lag")
smooth = (src + 2 * src[1] + 2 * src[2] + src[3]) / 6
len = input(8, title="Stochastic len")
cycle = (1 - alpha) * (1 - alpha) * 
         (smooth - 2 * smooth[1] + smooth[2]) + 
         2 * (1 - alpha) * cycle[1] - 
         (1 - alpha) * (1 - alpha) * cycle[2]

value1 = ta.rsi(cycle, len)
signal = sma(value1, lag)

plot(signal, title="Signal", color=color.blue)
if (signal > signal[1])
    strategy.entry("Long", strategy.long)
if (signal < signal[1])
    strategy.exit("Exit Long", from_entry="Long")

```

This PineScript code implements the described Ehlers Stochastic Cyber Cycle Strategy. It calculates a smoothed cycle indicator, generates a stochastic value based on this cycle, and uses moving averages to create trading signals for entering long positions.