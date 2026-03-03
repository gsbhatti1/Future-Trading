``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=2
strategy("Renko Stock Daily")


Rango1 = input(false, title="Rango 1")
Rango2 = input(false, title="Rango 2")

Situacion = ((highest(close, 22)-low)/(highest(close, 22)))*100

DesviaccionTipica = 2 * stdev(Situacion, 20)
Media = sma(Situacion, 20)

Rango11 = Media + DesviaccionTipica

Rango22 = (highest(Situacion, 50)) * 0.85


advertir = Situacion > Rango11 ? "GO LONG" : Situacion < Rango22 ? "CLOSE POSITION" : ""

if (close < open)
    strategy.close("Close Position")

plot(Rango11, title="Upper Rail", color=color.blue)
plot(Rango22, title="Lower Rail", color=color.red)

```

### Summary

The provided Pine Script implements a simple intraday trading strategy for stocks based on renko low point retracement. The script calculates the upper and lower rails using statistical measures and uses them to generate buy (`GO LONG`) or sell (`CLOSE POSITION`) signals. When the close price is below the open price, it closes the position.

The strategy aims to leverage the filtering capabilities of renko charts to avoid false signals in range-bound markets while providing clear entry and exit rules based on retracement levels.