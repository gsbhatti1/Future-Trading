> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Position Size (%)|
|v_input_int_1|25|EMA 1|
|v_input_2_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_2|100|EMA 2|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_3|200|EMA 3|
|v_input_4_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5|14|RSI length|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-20 00:00:00
end: 2023-12-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy('EMA Crossover Strategy', shorttitle='EMA Crossover', overlay=true)


// Define input for position size as a percentage of equity
position_size_pct = input(1, title='Position Size (%)') / 100

// Input EMA
len1 = input.int(25, minval=1, title='EMA 1')
src1 = input(close, title='Source')
ema1 = ta.ema(src1, len1)
len2 = input.int(100, minval=1, title='EMA 2')
src2 = input(close, title='Source')
ema2 = ta.ema(src2, len2)
len3 = input.int(200, minval=1, title='EMA 3')
src3 = input(close, title='Source')
ema3 = ta.ema(src3, len3)
// End of EMA format

// RSI Format
lenrsi = input(14, title='RSI length')
outrsi = ta.rsi(close, lenrsi)

bodybar1 = math.abs(close - open)
bodybar2 = math.abs(close[1] - open[1])

// Plot the EMAs
plot(ema1, color=color.blue, linewidth=2, title='EMA 1')
plot(ema2, color=color.red, linewidth=2, title='EMA 2')
plot(ema3, color=color.green, linewidth=2, title='EMA 3')

// Buy signal logic
buy_signal = ta.crossover(ema1, ema2) and bodybar1 > bodybar2 and close > open
plotshape(series=buy_signal, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")

// Sell signal logic
sell_signal = ta.crossunder(ema1, ema2) and bodybar1 < bodybar2 and close < open
plotshape(series=sell_signal, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")
```

Note: The provided code has been completed to include buy and sell signal logic based on the EMA crossovers and additional conditions.