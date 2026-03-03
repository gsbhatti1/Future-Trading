``` pinescript
/*backtest
start: 2023-11-05 00:00:00
end: 2023-11-12 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Noro
//2018

//@version=2
strategy(title = "Fast RSI Risk Control Compound Futures Trading Strategy v1.0", shorttitle = "Fast RSI Risk Control", overlay = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 10)

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
usemar = input(true, defval = true, title = "Use Martingale")
capital = input(100, defval = 100, minval = 1, maxval = 10000, title = "Capital, %")
rsiperiod = input(7, defval = 7, minval = 2, maxval = 100, title = "RSI Period")
rsilimit = input(25, defval = 25, minval = 1, maxval = 30, title = "RSI limit")
rsibars = input(1, defval = 1, minval = 1, maxval = 20, title = "RSI Bars")
useocf = input(true, defval = true, title = "Use Open Color Filter")
useccf = input(true, defval = true, title = "Use Close Color Filter")
openbars = input(4, defval = 4, minval = 1, maxval = 20, title = "Open Color Bars")
closebars = input(1, defval = 1, minval = 1, maxval = 20, title = "Close Color Bars")
useobf = input(true, defval = true, title = "Use Open Body Filter")
usecbf = input(true, defval = true, title = "Use Close Body Filter")
openbody = input(20, defval = 20, minval = 0, maxval = 1000, title = "Open Body Minimum, %")
closebody = input(50, defval = 50, minval = 0, maxval = 1000, title = "Close Body Minimum, %")
usecnf = input(true, defval = true, title = "Use Close Norma Filter")
fromyear = input(1900, defval = 1900, minval = 1900, maxval = 2100, title = "From Year")
toyear = input(2100, defval = 2100, minval = 1900, maxval = 2100, title = "To Year")
frommonth = input(01, defval = 01, minval = 01, maxval = 12, title = "From Month")
fromday = input(01, defval = 01, minval = 01, maxval = 31, title = "From Day")
toyear = input(2100, defval = 2100, minval = 1900, maxval = 2100, title = "To Year")
today = input(31, defval = 31, minval = 01, maxval = 31, title = "To Day")
```

This translation preserves the original code blocks, numbers, and formatting while translating the human-readable text.