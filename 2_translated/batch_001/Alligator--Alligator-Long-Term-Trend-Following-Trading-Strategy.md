> Source (PineScript)

``` pinescript
/*backtest
start: 2023-05-11 00:00:00
end: 2024-05-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//_______ <licence>
// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://www.mozilla.org/en-US/MPL/2.0/
// For more information about Pine Script™, visit https://tradingview.com/pine-script-docs/en/latest/index.html
// Created by: ChaoZhang

//@version=5
indicator("Alligator-Long-Term-Trend-Following-Trading-Strategy", shorttitle="Alligator LTTFS", overlay=false)

lenJaw = 13, smmaPeriodJaw = 8
lenTeeth = 8, smmaPeriodTeeth = 5
lenLips = 5, smmaPeriodLips = 3

// Calculate Alligator Indicator Lines
jaw_line = smma(close, lenJaw - smmaPeriodJaw)
teeth_line = smma(close, lenTeeth - smmaPeriodTeeth)
lips_line = smma(close, lenLips - smmaPeriodLips)

plot(jaw_line, color=color.blue, title="Jaw Line")
plot(teeth_line, color=color.green, title="Teeth Line")
plot(lips_line, color=color.red, title="Lips Line")

// Determine Trend Direction
isBullish = jaw_line > teeth_line and teeth_line > lips_line
isBearish = jaw_line < teeth_line and teeth_line < lips_line

bullishSignal = isBullish and close > max(jaw_line, teeth_line, lips_line)
bearishSignal = isBearish and close < min(jaw_line, teeth_line, lips_line)

// Trading Logic
var float entryPrice = na
if bullishSignal
    strategy.entry("Long", strategy.long)
    entryPrice := close

if bearishSignal
    strategy.close("Long")

plotshape(series=bullishSignal, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=bearishSignal, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

// Risk Management
slippage = 50 // in pips
strategy.exit("SL", from_entry="Long", limit=entryPrice + slippage * syminfo.mintick)
```

This Pine Script™ code defines the Alligator Long-Term Trend Following Trading Strategy, which uses moving averages to identify and follow market trends. The strategy is implemented on the Binance Futures platform for trading BTC/USDT pairs over a one-hour base period with daily backtesting.