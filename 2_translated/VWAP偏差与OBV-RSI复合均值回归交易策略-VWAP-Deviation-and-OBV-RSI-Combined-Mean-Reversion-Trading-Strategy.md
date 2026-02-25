``` pinescript
/*backtest
start: 2024-02-19 00:00:00
end: 2025-02-16 08:00:00
period: 4h
basePeriod: 4h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=6
strategy('[Hoss] Combined Strategy', overlay=true)

// Indicator 1: [Hoss] VWAP Deviation
indicator_vwap = input.bool(true, title="Show VWAP Deviation Indicator", group="Visibility")
length = input.int(60, title="VWAP Length", group="VWAP Settings")
src = input(close, title="Source", group="VWAP Settings")

// Calculations for VWAP
vwmean = ta.wma(src, length)
dev = ta.stdev(src, length)
basis = vwmean
upper_dev2 = vwmean + dev * 2
lower_dev2 = vwmean - dev * 2

// Plotting VWAP Deviation
plot(indicator_vwap ? basis : na, color=color.gray, title='Basis', linewidth=2)
plot1 = plot(indicator_vwap ? upper_dev2 : na, color=color.red, title='Upper Dev 2', linewidth=2)
plot2 = plot(indicator_vwap ? lower_dev2 : na, color=color.green, title='Lower Dev 2', linewidth=2)
fill(plot1, plot2, color=color.new(color.green, 80), title='Deviation Band')

// Indicator 2: [Hoss] OBV RSI
indicator_obv_rsi = input.bool(true, title="Show OBV RSI Indicator", group="Visibility")
len = input.int(14, title="RSI Length", group="OBV RSI Settings")
obv = ta.cum(ta.change(src) > 0 ? volume : ta.change(src) < 0 ? -volume : 0)
rsi = ta.rsi(obv, len)

// Plotting OBV RSI
plot(indicator_obv_rsi ? rsi : na, color=color.blue, title='OBV RSI', linewidth=2)
```

This Pine Script code snippet sets up a trading strategy that combines VWAP deviation and OBV RSI indicators. The script defines the input parameters for both indicators, calculates their values, and plots them on the chart.