``` pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-02-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © samuelarbos

//@version=4
strategy("Bollinger Bands and RSI Combination Strategy", overlay=true)

// Define the Bollinger Bands parameters
source = input(close, title="Price base")
length = input(20, minval=1, title="Length")
mult = input(2.0, minval=0.001, maxval=50, title="Standard Deviation")

// Calculate the Bollinger Bands
basis = sma(source, length)
dev = mult * stdev(source, length)
upper = basis + dev
lower = basis - dev

// Define the RSI and its parameters
rsi_source = input(close, title="RSI Source")
rsi_length = input(14, minval=1, title="RSI Length")
rsi_overbought = input(70, minval=0, maxval=100, title="RSI Overbought")
rsi_oversold = input(30, minval=0, maxval=100, title="RSI Oversold")

// Calculate the RSI
rsi = rsi(rsi_source, rsi_length)

// Trading signals
buy_signal = crossover(close, lower) and rsi < rsi_oversold
sell_signal = crossunder(close, upper) and rsi > rsi_overbought

// Plotting bands and RSI on the chart
plot(upper, color=color.red)
plot(lower, color=color.green)
hline(rsi_overbought, "Overbought Level", color=color.red)
hline(rsi_oversold, "Oversold Level", color=color.green)

// Strategy conditions to enter and exit trades
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.exit("Sell", "Buy")

```

This Pine Script defines the Bollinger Bands and RSI combination strategy as described. It calculates the bands, sets up the trading signals based on crossover/crossunder conditions for both indicators, and enters/exit trades accordingly.