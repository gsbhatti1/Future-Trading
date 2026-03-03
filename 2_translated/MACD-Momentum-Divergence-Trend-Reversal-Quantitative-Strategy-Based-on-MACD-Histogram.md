``` pinescript
/*backtest
start: 2024-11-10 00:00:00
end: 2025-02-19 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

//@version=5
strategy("MACD Momentum Reversal Strategy", overlay=true, initial_capital=100000, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// === MACD Calculation ===
fastLength   = input.int(12, "MACD Fast Length")
slowLength   = input.int(26, "MACD Slow Length")
signalLength = input.int(9, "MACD Signal Length")
[macdLine, signalLine, histLine] = ta.macd(close, fastLength, slowLength, signalLength)

// === Candle Properties ===
bodySize      = math.abs(close - open)
prevBodySize  = math.abs(close[1] - open[1])
candleBigger  = bodySize > prevBodySize

bullishCandle = close > open
bearishCandle = close < open

// === MACD Momentum Conditions ===
// For bullish candles: if the MACD histogram (normally positive) is decreasing over the last 3 bars,
// then the bullish momentum is fading – a potential short signal.
macdLossBullish = (histLine[2] > histLine[1]) and (histLine[1] > histLine[0])

// For bearish candles: if the MACD histogram (normally negative) is increasing (moving closer to zero)
// over the last 3 bars, then the bearish momentum is fading – a potential long signal.
macdGainBearish = (histLine[2] < histLine[1]) and (histLine[1] < histLine[0])

// === Trading Logic ===
if (bullishCandle and candleBigger) and macdLossBullish
    strategy.entry("Short", strategy.short)

if (bearishCandle and candleBigger) and macdGainBearish
    strategy.entry("Long", strategy.long)

// === Position Management ===
// Close positions when opposite signals appear.
if (strategy.position_size < 0 and not bullishCandle) or (strategy.position_size > 0 and not bearishCandle)
    strategy.close("Short")
    strategy.close("Long")

// === Summary ===
// This strategy combines candlestick patterns with MACD histogram momentum changes to capture market reversals.
// It offers clear signals, simple operation, and high adaptability across different markets and timeframes.
```