``` pinescript
/*backtest
start: 2023-06-08 00:00:00
end: 2024-06-13 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Chande-Kroll Stop Dynamic ATR Trend Following Strategy", overlay=true)

atrLength = input(21, title="ATR Period")
multiplier = input(3.0, title="ATR Multiplier")
smaPeriod = input(21, title="SMA Period")

chandekrollStop = ta.atr(atrLength) * multiplier
longCondition = close > chandekrollStop and close > sma(syminfo.tickerid, smaPeriod)
shortCondition = false // Currently only supports long positions

if (longCondition)
    strategy.entry("Long", strategy.long)

if (close < chandekrollStop)
    strategy.close("Long")

plot(chandekrollStop, color=color.red, title="Chande-Kroll Stop")
plot(sma(close, smaPeriod), color=color.blue, title="SMA 21")
```

This Pine Script implements the Chande-Kroll Stop Dynamic ATR Trend Following Strategy. It includes the necessary inputs for the ATR period, multiplier, and SMA period, as well as the logic to determine when to enter and exit trades based on the strategy's principles.