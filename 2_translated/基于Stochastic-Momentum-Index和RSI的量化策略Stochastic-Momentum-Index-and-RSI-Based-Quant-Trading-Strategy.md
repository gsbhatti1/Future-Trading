``` pinescript
/*backtest
start: 2023-12-04 00:00:00
end: 2023-12-06 19:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Noro
// 2018

//@version=2
strategy(title = "Noro's Stochastic Strategy v1.3", shorttitle = "Stochastic str 1.3", overlay = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 0)

// Settings 
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
usemar = input(false, defval = false, title = "Use Martingale")
capital = input(100, defval = 100, minval = 1, maxval = 10000, title = "Capital, %")
usesmi = input(true, defval = true, title = "Use SMI Strategy")
usersi = input(true, defval = true, title = "Use RSI Strategy")
usecol = input(true, defval = true, title = "Use Color-Filter")
usebod = input(true, defval = true, title = "Use Body-Filter")
a = input(2, defval = 2, minval = 2, maxval = 50, title = "SMI Percent K Length")
b = input(2, defval = 2, minval = 2, maxval = 50, title = "SMI Percent D Length")
limitsmi = input(50, defval = 50, minval = 1, maxval = 100, title = "SMI Limit")
periodrsi = input(2, defval = 2, minval = 2, maxval = 50, title = "RSI Period")
limitrsi = input(10, defval = 10, minval = 1, maxval = 50, title = "RSI Limit")
double = input(false, defval = false, title = "SMI+RSI Mode")
showbg = input(false, defval = false, title = "Show background")
fromyear = input(2018, defval = 2018, minval = 1900, maxval = 2100, title =
```