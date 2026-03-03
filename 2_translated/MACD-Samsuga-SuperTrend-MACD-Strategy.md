> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|7|ATR Length|
|v_input_float_1|true|Factor|


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
strategy("Samsuga supertrend", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)


atrPeriod = input.int(7,    "ATR Length", minval = 1)
factor =    input.float(1.0, "Factor",     minval = 0.01, step = 0.01)

[supertrend, direction] = ta.supertrend(factor, atrPeriod)

supertrend := barstate.isfirst ? na : supertrend
upTrend =    plot(direction <= 0 ? supertrend : na, "Up Trend",   color = color.green, style = plot.style_linebr)
downTrend =  plot(direction <= 0 ? na : supertrend, "Down Trend", color = color.red,   style = plot.style_linebr)
bodyMiddle = plot(barstate.isfirst ? na : (open + close) / 2, "Body Middle", display = display.none)
longcondition = direction[1] > 0 and not na(direction[1]) ? true : false
shortCondition = direction[1] < 0 and not na(direction[1]) ? true : false

// MACD part
macdData = request.security(syminfo.tickerid, "30", ta.macd(close)[1])
macdLine = macdData[0]
signalLine = macdData[1]
histogram = macdData[2]

// Long entry condition
if (upTrend and histogram > 0)
    strategy.entry("Long", strategy.long)

// Short entry condition
if (downTrend and histogram < 0)
    strategy.entry("Short", strategy.short)

// Exit conditions
strategy.exit("Close Long", "Long", stop=supertrend <= close, limit=supertrend >= close)
strategy.exit("Close Short", "Short", stop=supertrend >= close, limit=supertrend <= close)
```

This PineScript code implements the `Samsuga supertrend` strategy as described. It uses both SuperTrend and MACD indicators to manage entries and exits based on market trends and price action.