```pinescript
/*backtest
start: 2024-08-01 00:00:00
end: 2025-02-18 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © FIWB

//@version=6
strategy("Refined Ichimoku with MACD and RSI Strategy", overlay=true)

// Inputs for Ichimoku Cloud
conversionLength = input.int(9, title="Conversion Line Length", group="Ichimoku Settings")
baseLength = input.int(26, title="Base Line Length", group="Ichimoku Settings")
laggingSpanLength = input.int(52, title="Lagging Span Length", group="Ichimoku Settings")
displacement = input.int(26, title="Displacement", group="Ichimoku Settings")

// Inputs for MACD
macdFastLength = input.int(12, title="MACD Fast Length", group="MACD Settings")
macdSlowLength = input.int(26, title="MACD Slow Length", group="MACD Settings")
macdSignalLength = input.int(9, title="MACD Signal Length", group="MACD Settings")

// Inputs for RSI/Stochastic RSI
rsiLength = input.int(14, title="RSI Length", group="Momentum Indicators")
stochKLength = input.int(14, title="Stochastic K Length", group="Momentum Indicators")
stochDSpanLength = input.int(3, title="Stochastic D Span Length", group="Momentum Indicators")

// Ichimoku Cloud
conversionLine = ta.sma(close, conversionLength)
baseLine = ta.sma(close, baseLength)
laggingSpan = close[displacement]
tenkanSen = (conversionLine + baseLine) / 2
kijunSen = ta.sma(close, baseLength)
senKouA = tenkanSen - kijunSen
senKouB = laggingSpan - kijunSen

// MACD
macdLine = ta.macd(close, macdFastLength, macdSlowLength, macdSignalLength)[0]
macdHist = macdLine - macdSignalLength[0]

// Stochastic RSI
rsiValue = ta.rsi(close, rsiLength)
stochK = ta.stoch(rsiValue, rsiValue, 14)
stochD = ta.sma(stochK, stochDSpanLength)

plot(tenkanSen, color=color.blue, title="Tenkan Sen")
plot(kijunSen, color=color.red, title="Kijun Sen")
fill(tenkanSen, kijunSen, color=color.new(color.gray, 90), title="Ichimoku Cloud")

// Entry Conditions
longCondition = (close > tenkanSen and rsiValue > 55 and macdHist > 0)
shortCondition = (close < tenkanSen and rsiValue < 45 and macdHist < 0)

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Conditions
exitLongCondition = close < senKouA or rsiValue > 70
exitShortCondition = close > senKouB or rsiValue < 30

if (exitLongCondition)
    strategy.close("Long")

if (exitShortCondition)
    strategy.close("Short")

// ATR for stop-loss management
atrLength = input.int(14, title="ATR Length", group="Stop-Loss Settings")
atrValue = ta.atr(atrLength)

longStopLoss = close - 2 * atrValue
shortStopLoss = close + 2 * atrValue

// Visualization of market state with background colors
bgcolor(tenkanSen > kijunSen ? color.green : tenkanSen < kijunSen ? color.red : na, title="Market State Background")
```