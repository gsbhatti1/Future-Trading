``` pinescript
/*backtest
start: 2023-10-16 00:00:00
end: 2023-11-15 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Ichimoku system", overlay=true, initial_capital = 100000, default_qty_type = strategy.percent_of_equity, default_qty_value=100)

buyOnly = input(false, "only shows buying Trade", type=input.bool)


conversionPeriods = input(9, minval=1, title="Conversion Line Periods")
basePeriods = input(26, minval=1, title="Base Line Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span 2 Periods")
displacement = input(26, minval=1, title="Displacement")

donchian(len) => avg(lowest(len), highest(len))

conversionLine = donchian(conversionPeriods)
baseLine = (highest(basePeriods) + lowest(basePeriods)) / 2
leadingSpan1 = conversionLine - displacement
leadingSpan2 = leadingSpan1 - displacement

plotshape(series=crossover(close, baseLine), title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=crossunder(close, baseLine), title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

if (not buyOnly) or (buyOnly and crossover(close, baseLine))
    strategy.entry("Buy", strategy.long)
    
stopLossPercent = close * (v_input_7 / 100)
takeProfitPercent = close * (v_input_6 / 100)

strategy.exit("Close Long Position", from_entry="Buy", stop=close + stopLossPercent, limit=close - takeProfitPercent)
```

This Pine Script code defines the Ichimoku trading strategy based on the provided description. It includes the necessary input arguments and implements logic to identify buy/sell signals and set up appropriate orders with predefined take profit and stop loss levels.