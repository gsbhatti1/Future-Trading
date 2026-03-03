```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-18 23:59:59
Period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Smart Money Concept Strategy", overlay=true)

// On-Balance Volume (OBV)
obv = ta.cum(ta.change(close) * volume)
plot(obv, title="On-Balance Volume")

// Smart Money Conditions
longCondition = ta.slope(obv, 10) > 0
shortCondition = ta.slope(obv, 10) < 0

// Plot Signals
plotshape(series=longCondition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

// Entry Logic
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Logic
if (is_long := strategy.opentrades.get_order("Long").state == order.state.open)
    if (shortCondition or bar_index > 100) // Exit after 100 bars or when short condition met
        strategy.close("Long")

if (is_short := strategy.opentrades.get_order("Short").state == order.state.open)
    if (longCondition or bar_index > 100) // Exit after 100 bars or when long condition met
        strategy.close("Short")

// Risk Management
strategy.exit("Exit Long", "Long", stop=ta.slope(obv, 5) < -20)
strategy.exit("Exit Short", "Short", stop=ta.slope(obv, 5) > 20)

```

```