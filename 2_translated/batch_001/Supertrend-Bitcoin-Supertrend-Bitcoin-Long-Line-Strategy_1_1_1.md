> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|10|ATR Length|
|v_input_float_1|3|Factor|
|v_input_2|7|ADX Smoothing|
|v_input_3|7|DI Length|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-01-26 00:00:00
end: 2024-02-01 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Supertrend Bitcoin Long Line Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000, margin_long=0.1)

atrPeriod = input(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 0.01)

[superTrendValue, direction] = ta.supertrend(atrPeriod, factor)
longCondition = direction < 0 and ta.rsi(close, 21) < 66 and ta.rsi(close, 3) > 80 and ta.rsi(close, 28) > 49 and ta.adx(close) > 20

plotshape(series=longCondition ? direction : na, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")

if (direction >= 1)
    strategy.close("Long Position")
```

This PineScript code implements the Supertrend Bitcoin Long Line Strategy as described. The strategy uses the `ta.supertrend` function to determine entry and exit conditions based on SuperTrend, RSI, and ADX indicators. The script also includes a buy signal plot for visualization purposes.