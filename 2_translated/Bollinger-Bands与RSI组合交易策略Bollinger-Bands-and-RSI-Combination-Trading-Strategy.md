> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Precio base: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|20|Longitud|
|v_input_3|2|Desviación estándar|
|v_input_4_close|0|RSI Fuente: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5|14|RSI Longitud|
|v_input_6|70|RSI Sobrecompra|
|v_input_7|30|RSI Sobrevendido|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-28 00:00:00
end: 2024-02-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © samuelarbos


//@version=4
strategy("Bollinger Bands and RSI Combination Trading Strategy", overlay=true)

// Define Bollinger Bands parameters
source = input(close, title="Price source")
length = input(20, minval=1, title="Length")
mult = input(2.0, minval=0.001, maxval=50, title="Standard deviation")

// Calculate Bollinger Bands
basis = sma(source, length)
dev = mult * stdev(source, length)
upper = basis + dev
lower = basis - dev

// Define RSI and its parameters
rsi_source = input(close, title="RSI source")
rsi_length = input(14, minval=1, title="RSI Length")
overbought_level = input(70, minval=1, maxval=100, title="Overbought Level")
oversold_level = input(30, minval=1, maxval=100, title="Oversold Level")

// Calculate RSI
rsi = rsi(rsi_source, rsi_length)

// Generate buy and sell signals based on Bollinger Bands and RSI
if (rsi < oversold_level and close < lower)
    strategy.entry("BB-RSI Buy", strategy.long)
if (rsi > overbought_level and close > upper)
    strategy.exit("BB-RSI Sell", "BB-RSI Buy")
```

This PineScript code defines a trading strategy that combines Bollinger Bands and RSI to generate buy and sell signals. It sets up the necessary parameters for both indicators, calculates them, and uses conditions based on these calculations to execute trades.