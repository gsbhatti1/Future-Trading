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

// Plot indicators on chart
plotcci = plot(cci_value, title="CCI", color=ccibar_color)
plothorzline1 = hline(overbought_level, "Overbought Level", color=color.red, linestyle=hline.style_dashed)
plothorzline2 = hline(oversold_level, "Oversold Level", color=color.green, linestyle=hline.style_dashed)

// Place orders
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.exit("Sell", from_entry="Buy")
```

This PineScript code defines a trading strategy that combines CCI, DMI, and MACD indicators. It sets up conditions for generating buy and sell signals based on these indicators and includes the necessary plotting to visualize them on the chart.