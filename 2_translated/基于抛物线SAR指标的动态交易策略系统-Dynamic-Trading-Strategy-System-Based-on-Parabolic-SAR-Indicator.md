> Source (PineScript)

``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-25 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("LTJ Strategy", overlay=true)

// Parámetros del Parabolic SAR
start = input(0.02, title="Start")
increment = input(0.02, title="Increment")
maximum = input(0.2, title="Maximum")

// Calculando el Parabolic SAR
sar = ta.sar(start, increment, maximum)

// Condiciones para entrar y salir de la posición
longCondition = ta.crossunder(sar, close) // Compra cuando el Parabolic SAR cruza por debajo del precio de cierre
exitLongCondition = ta.crossover(sar, close) // Venta cuando el Parabolic SAR cruza por encima del precio de cierre

// Condiciones para entrar y salir de la posición
shortCondition = ta.crossover(sar, close) // Compra cuando el Parabolic SAR cruza por debajo del precio de cierre
exitShortCondition = ta.crossunder(sar, close) // Venta cuando el Parabolic SAR cruza por encima del precio de cierre

// Mostrando los puntos del Parabolic SAR en la gráfica
plotshape(series=sar > close ? na : sar, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=sar < close ? na : sar, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Implementando las condiciones de entrada y salida
if (longCondition)
    strategy.entry("Long", strategy.long)
if (exitLongCondition)
    strategy.close("Long")
if (shortCondition)
    strategy.entry("Short", strategy.short)
if (exitShortCondition)
    strategy.close("Short")
```
```