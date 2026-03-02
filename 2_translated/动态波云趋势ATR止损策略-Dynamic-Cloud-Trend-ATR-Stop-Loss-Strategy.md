``` pinescript
/*backtest
start: 2024-09-01 00:00:00
end: 2025-02-18 00:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Binance","currency":"TRB_USDT"}]
*/

//@version=5
strategy("Ichimoku Cloud + ATR Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// === Inputs ===
conversionPeriods = input.int(9, title="Tenkan-sen Period", minval=1)
basePeriods = input.int(26, title="Kijun-sen Period", minval=1)
laggingSpan2Periods = input.int(52, title="Senkou Span B Period", minval=1)
displacement = input.int(26, title="Displacement", minval=1)
atrLength = input.int(14, title="ATR Period", minval=1)
atrMultiplier = input.float(1.5, title="ATR Multiplier for Stop-Loss", minval=0.1, step=0.1)

// === Indicator Calculations ===
// Ichimoku Cloud
tenkan = (ta.highest(high, conversionPeriods) + ta.lowest(low, conversionPeriods)) / 2
kijun = (ta.highest(high, basePeriods) + ta.lowest(low, basePeriods)) / 2
senkouSpanA = ta.sma(high, basePeriods - displacement)
senkouSpanB = ta.sma(low, laggingSpan2Periods - displacement)

// === Signal Generation ===
bullishSignal = ta.crossover(tenkan, kijun) and close > senkouSpanA and chikou >= close
bearishSignal = ta.crossunder(tenkan, kijun) and close < senkouSpanA and chikou <= close

// === Stop-Loss Setup ===
stopLossPrice = na
if (bullishSignal)
    stopLossPrice := low[1] - atr(high, low, close, atrLength) * atrMultiplier
else if (bearishSignal)
    stopLossPrice := high[1] + atr(high, low, close, atrLength) * atrMultiplier

// === Entry and Exit Conditions ===
if (bullishSignal or bearishSignal)
    strategy.entry("Long", strategy.long, when=bullishSignal)
    strategy.exit("Exit Long", "Long", stop=stopLossPrice)

if (bullishSignal or bearishSignal)
    strategy.close("Short", when=bearishSignal)
```

This Pine Script code implements the described dynamic wave cloud trend ATR stop-loss strategy. The script calculates the Ichimoku Cloud and uses ATR to dynamically set stop-loss levels, following the detailed description provided.