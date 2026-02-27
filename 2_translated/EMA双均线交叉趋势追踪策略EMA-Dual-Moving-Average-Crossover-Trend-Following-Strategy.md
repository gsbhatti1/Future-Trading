> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|Longitud Media Rápida|
|v_input_2|21|Longitud Media Lenta|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-02-01 00:00:00
end: 2024-02-29 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA-Dual-Moving-Average-Crossover-Trend-Following-Strategy by ChaoZhang", overlay=true)

// Parameters for the moving averages
fastMA = input(9, "Longitud Media Rápida")
slowMA = input(21, "Longitud Media Lenta")

// Calculating the moving averages
emaFast = ta.ema(close, fastMA)
emaSlow = ta.ema(close, slowMA)

// Buy condition (crossover upwards)
buySignal = ta.crossover(emaFast, emaSlow)

// Sell condition (crossover downwards)
sellSignal = ta.crossunder(emaFast, emaSlow)

// Drawing arrows for the signals
plotshape(buySignal, title="Compra", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(sellSignal, title="Venta", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)
```

This PineScript code implements the EMA-Dual-Moving-Average-Crossover-Trend-Following-Strategy with inputs for the fast and slow moving average periods. It uses exponential moving averages (EMAs) to generate buy and sell signals based on crossovers between the two EMAs, and plots arrows to visually indicate these signals.