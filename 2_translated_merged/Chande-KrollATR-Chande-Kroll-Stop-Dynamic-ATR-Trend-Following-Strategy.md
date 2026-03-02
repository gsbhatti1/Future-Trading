``` pinescript
/*backtest
start: 2023-06-08 00:00:00
end: 2024-06-13 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Chande-Kroll Stop Dynamic ATR Trend Following Strategy", shorttitle="CK-Stop-Dynamic-ATR-Trend-Following", overlay=true)

// Parameters
atrPeriod = input(21, title="ATR Period")
atrMultiplier = input(3.0, title="ATR Multiplier")
smaPeriod = input(21, title="SMA Period")

// ATR and SMA Calculation
atrValue = ta.atr(atrPeriod)
chandeStopLower = close - (atrValue * atrMultiplier)
chandeStopUpper = close + (atrValue * atrMultiplier)
sma = ta.sma(close, smaPeriod)

// Trading Logic
longCondition = ta.crossover(close, chandeStopLower) and close > sma
strategy.entry("Long", strategy.long, when=longCondition)

exitCondition = ta.crossunder(close, chandeStopUpper)
strategy.close("Long", when=exitCondition)

// Plotting
plot(chandeStopLower, color=color.red, title="Chande Stop Lower")
plot(chandeStopUpper, color=color.green, title="Chande Stop Upper")
hline(sma, "SMA", color=color.orange)
```

This Pine Script code implements the Chande-Kroll Stop Dynamic ATR Trend Following Strategy as described. The script uses the specified parameters to calculate dynamic stop-loss levels and a 21-period SMA for trend filtering, and it triggers long positions based on these conditions.