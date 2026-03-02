``` pinescript
/*backtest
start: 2024-11-01 00:00:00
end: 2025-02-19 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © FIWB
//@version=6
strategy("Momentum Edge Strategy - 1D BTC Optimized", overlay=true)

// --- Input Parameters ---
atrLength     = input.int(14, title="ATR Length")
atrMultiplier = input.float(1.5, title="ATR Multiplier")
bbWidthThreshold = input.float(0.02, title="Bollinger Band Width Threshold")

// --- Ichimoku Cloud ---
conversionLine = (ta.highest(high, 9) + ta.lowest(low, 9)) / 2
baseLine = (ta.highest(high, 26) + ta.lowest(low, 26)) / 2
leadingSpanA = (conversionLine + baseLine) / 2
leadingSpanB = (ta.highest(high, 52) + ta.lowest(low, 52)) / 2
priceAboveCloud = close > leadingSpanA and close > leadingSpanB
priceBelowCloud = close < leadingSpanA and close < leadingSpanB

// --- MACD Histogram ---
[_, _, macdHistogram] = ta.macd(close, 12, 26, 9)

// --- Multi-Timeframe Trend Confirmation ---
higherTFTrend = request.security(syminfo.tickerid, "W", close > ta.sma(close, 50))

// --- Bollinger Band Width ---
bbBasis = ta.sma(close, 20)
bbUpper = bbBasis + 2 * ta.stdev(close, 20)
bbLower = bbBasis - 2 * ta.stdev(close, 20)
bbWidth = (bbUpper - bbLower) / bbBasis

// --- ATR-based Stop Loss ---
atrValue     = ta.atr(atrLength)
highestHigh = ta.highest(high, atrLength)
lowestLow = ta.lowest(low, atrLength)
longStopLoss = bbWidth < bbWidthThreshold ? lowestLow : close - atrValue * atrMultiplier
shortStopLoss= bbWidth < bbWidthThreshold ? highestHigh : close +
```