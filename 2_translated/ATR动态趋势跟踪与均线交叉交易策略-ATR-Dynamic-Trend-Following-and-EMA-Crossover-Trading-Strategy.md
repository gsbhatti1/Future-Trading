``` pinescript
/*backtest
start: 2024-05-15 00:00:00
end: 2024-08-08 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

//@version=6
strategy(title="UT Bot Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Inputs
a = input.float(1, title="Key Value. 'This changes the sensitivity'")
c = input.int(10, title="ATR Period")
h = input.bool(false, title="Signals from Heikin Ashi Candles")

// Calculate ATR
xATR = ta.atr(c)
nLoss = a * xATR

// Source for calculations
src = h ? request.security(syminfo.tickerid, timeframe.period, hlc3) : close

// ATR Trailing Stop logic
var float xATRTrailingStop = na
if (not na(xATRTrailingStop[1]) and src > xATRTrailingStop[1] and src[1] > xATRTrailingStop[1])
    xATRTrailingStop := math.max(xATRTrailingStop[1], src - nLoss)
else if (not na(xATRTrailingStop[1]) and src < xATRTrailingStop[1] and src[1] < xATRTrailingStop[1])
    xATRTrailingStop := math.min(xATRTrailingStop[1], src + nLoss)
else
    xATRTrailingStop := src > xATRTrailingStop[1] ? src - nLoss : src + nLoss

// Position logic
var int pos = 0
if (not na(xATRTrailingStop[1]) and src[1] < xATRTrailingStop[1] and src > xATRTrailingStop[1])
    if (pos == 0)
        strategy.entry("Buy", strategy.long)
    pos := 1

if (not na(xATRTrailingStop[1]) and src[1] > xATRTrailingStop[1] and src < xATRTrailingStop[1])
    if (pos == 1)
        strategy.close("Buy")
    pos := -1
```

This Pine Script translates the provided code block from Chinese to English, maintaining all original elements such as inputs, calculations, and logic.