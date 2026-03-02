``` pinescript
/*backtest
start: 2023-12-25 00:00:00
end: 2024-01-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Trend Confirmation Strategy", overlay=true)

// Supertrend Indicator
atrPeriod = input(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 0.5)
vwapLength = input(12, "Fast Length")
vwapSmooth = input(26, "Slow Length")
priceSource = input(close, "Source: close/high/low/open/hl2/hlc3/hlcc4/ohlc4")
signalSmoothing = input.int(9, "Signal Smoothing")
osciMAType = input.string("EMA", "Oscillator MA Type: EMA/SMA")
signalMAType = input.string("EMA", "Signal Line MA Type: EMA/SMA")
hideVWAP1D = input(false, "Hide VWAP on 1D or Above")
vwapSource = input.hlc3(0, "VWAP Source: hlc3/high/low/open/hl2/close hlcc4/ohlc4")
stopLossRange = input.float(2.0, "Stop Loss Range", step=0.5)
trailingOffset = input.float(0.5, "Trailing Stop Offset", step=0.1)

// Supertrend Calculation
[supertrend, direction] = supertrend(priceSource, atrPeriod, factor)

// VWAP Calculation
vwap = ta.vwma(vwapSource, vwapLength)
plotshape(series=crossover(supertrend, 0) and close<vwap, title="Entry Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=crossunder(supertrend, 0) or (close>vwap and direction==1), title="Exit Signal Long", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// MACD Calculation
[macdLine, signalLine] = macd(priceSource, vwapLength, vwapSmooth)
plot(macdLine, title="MACD Line", color=color.blue)
plot(signalLine, title="Signal Line", color=color.orange)

// Exit Condition Based on MACD Crossovers
strategy.close("Long Position", when=crossunder(macdLine, signalLine))
strategy.close("Short Position", when=crossover(macdLine, signalLine))

// Stop Loss and Take Profit
stopLossLevel = vwap * (1 - stopLossRange / 100)
takeProfitLevel = vwap * (1 + trailingOffset)

longCondition = crossover(supertrend, 0) and close < vwap
shortCondition = crossunder(supertrend, 0)
if (longCondition or shortCondition)
    strategy.entry("Long Position", strategy.long, stop=stopLossLevel, comment="Stop Loss Entry")
else if (strategy.position_size > 0)
    strategy.exit("Take Profit Long", "Long Position", limit=takeProfitLevel, comment="Trailing Stop")

// Plot Indicators
plot(vwap, title="VWAP", color=color.blue)
```