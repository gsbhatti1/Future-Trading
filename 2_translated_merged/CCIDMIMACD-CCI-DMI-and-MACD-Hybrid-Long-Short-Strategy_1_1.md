> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|CCI Length|
|v_input_2|100|Overbought Level|
|v_input_3|-100|Oversold Level|


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
strategy("CCI, DMI, and MACD Strategy", overlay=true)

// Define inputs
cci_length = input(14, title="CCI Length")
overbought_level = input(100, title="Overbought Level")
oversold_level = input(-100, title="Oversold Level")

// Calculate CCI
cci_value = ta.cci(close, cci_length)

// Calculate DMI
[di_plus, di_minus, _] = ta.dmi(14, 14)

// Calculate MACD
[macd_line, signal_line, _] = ta.macd(close, 24, 52, 9)

// Define buy and sell conditions
buy_signal = ta.crossover(cci_value, oversold_level) and di_plus > di_minus and macd_line > signal_line // CCI crosses above -100, Di+ > Di-, and MACD > Signal
sell_signal = ta.crossunder(cci_value, overbought_level) and di_minus > di_plus and macd_line < signal_line // CCI crosses below 100, Di- > Di+, and MACD < Signal

// Plot indicators on the chart
plotcci = plot(cci_value, title="CCI", color=color.blue)
plotdi = plot(di_plus, title="Di+", color=color.red)
plotsignal = plot(macd_line - signal_line, title="MACD Difference", color=color.green)

// Buy and sell orders
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.close("Buy")
```

This PineScript code defines a trading strategy that combines the Commodity Channel Index (CCI), Directional Movement Index (DMI), and Moving Average Convergence Divergence (MACD) indicators to generate buy and sell signals. The script sets up the necessary inputs, calculates the technical indicators, and implements the conditions for entering and exiting trades based on these indicators.