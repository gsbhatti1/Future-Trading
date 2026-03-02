``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
//for coinbase, 3min logic
//This strategy trades against the short term trend. The first position can be either long or short.
//In the short term, prices fluctuate up and down on wide spread exchanges.
//And if the price moves to one side, the price tends to return to its original position momentarily.
//This strategy set stop order. Stop price is calculated with upper and lower shadows.

strategy("ndb_mm_for_coinbase_btcusd", overlay=true, initial_capital=100000, slippage=50)

fromyear = input(2019, minval = 2017, maxval = 2100, title = "From Year")
frommonth = input(12, minval = 1, maxval = 12, title = "From Month")
fromday = input(1, minval = 1, maxval = 31, title = "From day")
toyear = input(2100, minval = 2017, maxval = 2100, title = "To Year")
tomonth = input(12, minval = 1, maxval = 12, title = "To Month")
today = input(31, minval = 1, maxval = 31, title = "To day")
period = input(3, title = "period")
sigma = input(1.2, title = "sigma")

plotshape(series=na, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangledown, text="Long")
plotshape(series=na, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, text="Short")

var float upper_shadow = na
var float lower_shadow = na

if (bar_index % period == 0)
    open_time = time("1", "D")
    close_time = time("1", "D")
    upper_shadow := high - max(high, close)
    lower_shadow := min(low, close) - low

long_stop = close - (upper_shadow * sigma)
short_stop = close + (lower_shadow * sigma)

if (close > upper_shadow)
    strategy.entry("Long", strategy.long, stop=long_stop)
    strategy.exit("Short Exit", from_entry="Long", stop=short_stop)

if (close < lower_shadow)
    strategy.entry("Short", strategy.short, stop=short_stop)
    strategy.exit("Long Exit", from_entry="Short", stop=long_stop)
```

This Pine Script translates the provided Chinese trading strategy document into English, maintaining the original formatting and code blocks.