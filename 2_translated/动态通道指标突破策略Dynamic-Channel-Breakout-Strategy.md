``` pinescript
/*backtest
start: 2023-10-13 00:00:00
end: 2023-11-12 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © pratyush_trades

//@version=4
strategy("Dynamic-Channel-Breakout-Strategy", overlay=true)

length = input(20, title="Length")
longRule = input("Higher High", "Long Entry", options=["Higher High", "Basis"])
shortRule = input("Lower Low", "Short Entry", options=["Lower Low", "Basis"])
longSL=input("Lower Low", "LONG SL", options=["Lower Low", "Basis"])
shortSL=input("Higher High", "SHORT SL", options=["Higher High", "Basis"])

hh = highest(high, length)
ll = lowest(low, length)

up = plot(hh, 'Upper Band', color=color.green)
dw = plot(ll, 'Lower Band', color=color.red)
mid = (hh + ll) / 2
midPlot = plot(mid, 'Basis', color=color.orange)
fill(up, midPlot, color=color.green, transp=95)
fill(dw, midPlot, color=color.red, transp=95)
plot(ema(close, 200), "ema", color=color.orange)

if (close > ema(close, 200))
    if not na(close[length])
        strategy.entry("Long", strategy.long, stop=(longRule == "Basis" ? mid : hh))

if (close < ema(close, 200))
    if not na(close[length])
        strategy.entry("Short", strategy.short, stop=(shortRule == "Basis" ? mid : ll))
```

The translation maintains the original formatting and code blocks while translating the human-readable text.