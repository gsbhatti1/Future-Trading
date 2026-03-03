``` pinescript
/*backtest
start: 2024-02-20 00:00:00
end: 2025-02-18 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"DOGE_USDT"}]
*/

//@version=5
strategy("DOGE Enhanced Trend Following Strategy", 
         overlay=true, 
         default_qty_type=strategy.percent_of_equity, 
         default_qty_value=5, 
         commission_value=0.1, 
         slippage=2)

// === INPUT PARAMETERS ===
emaFastLength = input(50, title="Fast EMA Length")
emaSlowLength = input(200, title="Slow EMA Length")
adxLength = input.int(14, title="ADX Length")
adxSmoothing = input.int(14, title="ADX Smoothing Factor")
adxThreshold = input.float(25, title="ADX Trend Strength Threshold")
rsiLength = input.int(14, title="RSI Length")
rsiOverbought = input.float(70, title="RSI Overbought Level")
rsiOversold = input.float(30, title="RSI Oversold Level")
takeProfitMultiplier = input.float(1.03, title="Take Profit Multiplier", tooltip="Set a dynamic take profit level, e.g., 1.03 = 3% profit")
stopLossMultiplier = input.float(0.97, title="Stop Loss Multiplier", tooltip="Set stop loss level, e.g., 0.97 = 3% below entry price")

// === INDICATOR CALCULATIONS ===
emaFast = ta.ema(close, emaFastLength)
emaSlow = ta.ema(close, emaSlowLength)
[dip, dim, adxValue] = ta.dmi(adxLength, adxSmoothing)
rsiValue = ta.rsi(close, rsiLength)

// === MULTI-TIMEFRAME CONFIRMATION ===
emaFastHTF = request.security(syminfo.tickerid, "240", ta.ema(close, emaFastLength))
emaSlowHTF = request.security(syminfo.tickerid, "240", ta.ema(close, emaSlowLength))

// === CONDITIONS FOR TRADE ENTRY ===
bullishTrend = ta.crossover(emaFast, emaSlow) and adxValue > adxThreshold and rsiValue > rsiOversold
bearishTrend = ta.crossunder(emaFast, emaSlow) and adxValue > adxThreshold and rsiValue < rsiOverbought

// === TRADE EXECUTION ===
if (bullishTrend)
    strategy.entry("Long", strategy.long)
    strategy.exit("TakeProfit_Long", from_entry="Long", limit=close * takeProfitMultiplier, stop=close * stopLossMultiplier)

if (bearishTrend)
    strategy.entry("Short", strategy.short)
    strategy.exit("TakeProfit_Short", from_entry="Short", limit=close * takeProfitMultiplier, stop=close * stopLossMultiplier)
```

This Pine Script code implements the described strategy, ensuring that all code blocks, numbers, and formatting remain unchanged. The comments and variable names have been translated to English to match the provided text.