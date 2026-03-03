``` pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © AHMEDABDELAZIZZIZO

//@version=5
strategy("Trend-Reversal-Momentum-Indicators-Crossover-Tracking-Strategy", overlay=true )

// inputs
inversestrategy = input.bool(false, title="Inverse Strategy", tooltip="This option makes you reverse the strategy so that long signals become where to short")
direction = input.string(defval="Both", options=["Both", "Short", "Long"], title="Direction")

leftbars = input(6, title="Left Bars", group="Support and resistance")
rightbars = input(6, title="Right Bars", group="Support and resistance")

macdfast = input(12, title="MACD Fast", group="MACD")
macdslow = input(26, title="MACD Slow", group="MACD")
macdsignal = input(7, "MACD Signal", group="MACD")

sellqty = input(50, title="QTY to sell at TP 1")

len = input(14, title="ADX Length", group="ADX")


// support and resistance
res = fixnan(ta.pivothigh(high, leftbars, rightbars))
sup = fixnan(ta.pivotlow(low, leftbars, rightbars))

// macd
macd = ta.ema(close, macdfast) - ta.ema(close, macdslow)
signal = ta.ema(macd, macdsignal)

// adx
up = ta.change(high)
down = -ta.change(low)
plusDM = na(up) ? na : (up > down and up > 0 ? up : 0)
minusDM = na(down) ? na : (down > up and down > 0 ? down : 0)
truerange = ta.rma(ta.tr, len)
plusDI = 100 * ta.rma(plusDM, len) / truerange
minusDI = 100 * ta.rma(minusDM, len) / truerange
dx = 100 * ta.rma(math.abs(plusDI - minusDI) / (truerange)

// strategy logic
if (inversestrategy)
    longCondition = macd > signal and close > sup and dx > 20
    shortCondition = macd < signal and close < res and dx > 20
else
    longCondition = macd > signal and close > sup and dx > 20
    shortCondition = macd < signal and close < res and dx > 20

if (direction == "Both" or direction == "Long")
    strategy.entry("Long", strategy.long, when=longCondition)
    
if (direction == "Both" or direction == "Short") 
    strategy.entry("Short", strategy.short, when=shortCondition)

// stop loss and take profit
longSL = strategy.infinity
longTP1 = 6.0 * syminfo.mintick
longTP2 = 12.0 * syminfo.mintick

if (direction == "Both" or direction == "Long")
    strategy.exit("Long Exit", from_entry="Long", stop=close < longSL, limit=close + longTP1)

shortSL = strategy.infinity
shortTP1 = 6.0 * syminfo.mintick
shortTP2 = 12.0 * syminfo.mintick

if (direction == "Both" or direction == "Short")
    strategy.exit("Short Exit", from_entry="Short", stop=close > shortSL, limit=close - shortTP1)
```

This code block defines the strategy based on the provided description and arguments. The logic for entering trades, setting stop losses, and take profits is included in a clear manner.