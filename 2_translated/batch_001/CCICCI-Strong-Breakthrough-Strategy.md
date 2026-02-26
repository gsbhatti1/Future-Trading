``` pinescript
/*backtest
start: 2022-11-08 00:00:00
end: 2023-11-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='CCI High Performance long only', overlay=false )
src = input(close)
length = input.int(20, title='Period', minval=1)
lossp = input.float(8, title='Stop Loss percentage', minval=0.5, step=0.5)
scart = input.float(0.25, title='Close of the signal bar higher than Open %', minval = 0)
upperline = input.int(150, title='Upper Band', minval=0, step=10)
lowline = input.int(-150, title='Low Band', maxval=0, step=10)


// construction of CCI (not on close but in totalprice) and of bands
ma = ta.sma(src, length)
cci = (src - ma) / (0.015 * ta.dev(src, length))
plot(cci, 'CCI', color=color.new(#996A15, 0))
band1 = hline(upperline, 'Upper Band', color=#C0C0C0, linestyle=hline.style_dashed)
band0 = hline(lowline, 'Lower Band', color=#C0C0C0, linestyle=hline.style_dashed)

// Entry and exit logic
long_entry = ta.crossover(cci, lowline) and cci > (ref(cci, 1) * (1 + scart / 100))
long_stop_loss = cci >= upperline

if (long_entry)
    strategy.entry("Long", strategy.long)

if (long_stop_loss or bar_index == input.int(252)) // Exit after a year
    strategy.close("Long")

// Plotting stop loss line
plotshape(series=long_stop_loss, title="Stop Loss", location=location.belowbar, color=color.red, style=shape.triangleup)
```

This script defines the CCI calculation and sets up entry and exit conditions based on the defined parameters. It also plots the CCI values and stop loss levels on the chart. The strategy will only enter long positions when the CCI crosses above the lower band and meets additional criteria, and it exits either upon hitting the stop loss or after a year.