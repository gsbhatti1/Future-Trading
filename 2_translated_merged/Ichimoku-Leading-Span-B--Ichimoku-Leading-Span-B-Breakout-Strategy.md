> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|Conversion Period|
|v_input_2|26|Base Period|
|v_input_3|52|Lagging Span 2 Period|
|v_input_4|26|Displacement|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-04-23 00:00:00
end: 2024-04-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Ichimoku Leading Span B Buy/Sell Strategy", overlay=true)

// Ichimoku indicator parameters
conversionPeriods = input(9, title="Conversion Period")
basePeriods = input(26, title="Base Period")
laggingSpan2Periods = input(52, title="Lagging Span 2 Period")
displacement = input(26, title="Displacement")

// Ichimoku calculation
tenkanSen = (high[conversionPeriods] + low[conversionPeriods]) / 2
kijunSen = (ta.highest(high, basePeriods) + ta.lowest(low, basePeriods)) / 2
senkouSpanA = (tenkanSen + kijunSen) / 2
senkouSpanB = (ta.highest(high, laggingSpan2Periods) + ta.lowest(low, laggingSpan2Periods)) / 2

// Plot Leading Span B on the chart
plot(senkouSpanB, color=color.red, title="Leading Span B", offset=displacement)

// Buy signal: Price crosses above Leading Span B
buy_signal = ta.crossover(close, senkouSpanB[displacement])
if (buy_signal)
    strategy.entry("Buy", strategy.long)

// Sell signal: Price crosses below Leading Span B
sell_signal = ta.crossunder(close, senkouSpanB[displacement])
if (sell_signal)
    strategy.close("Buy")
```

This code completes the Ichimoku Leading Span B Buy/Sell Strategy in PineScript. It calculates and plots the Ichimoku Cloud indicator, and generates buy and sell signals based on price crossing above or below the Leading Span B line.