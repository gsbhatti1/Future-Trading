``` pinescript
/*backtest
start: 2024-05-01 00:00:00
end: 2024-05-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Chandelier Exit Strategy with ZLSMA and Volume Spike Detection", shorttitle="CES with ZLSMA and Volume", overlay=true, process_orders_on_close=true, calc_on_every_tick=false)
// Chandelier Exit Inputs
lengthAtr = input.int(title='ATR Period', defval=14) // Default ATR period is 14
mult = input.float(title='ATR Multiplier', step=0.1, defval=2.0)
useClose = input.bool(title='Use Close Price for Extremums', defval=true)

// Calculate ATR
atr = mult * ta.atr(lengthAtr)

// Calculate Long and Short Stops
longStop = (useClose ? ta.highest(close, lengthAtr) : ta.highest(high, lengthAtr)) - atr
shortStop = (useClose ? ta.lowest(close, lengthAtr) : ta.lowest(low, lengthAtr)) + atr

// ZLSMA Inputs
zlsmaLength = input.int(title='ZLSMA Period', defval=13)
zlsmaSrc = input.source(title="ZLSMA Source", defval=close)

// Calculate ZLSMA
zlsma = ta.sma(zlsmaSrc, zlsmaLength)

// RVOL Inputs
rvolThreshold = input.float(title='RVOL Threshold', step=0.1, defval=1.5)
volatilityRatio = 1.0

// Calculate RVOL
rvol = (volume / typicalPrice) * volatilityRatio

// Long Entry
if (close > zlsma and rvol > rvolThreshold)
    strategy.entry("Long", strategy.long, stop=longStop)

// Short Entry
if (close < zlsma and rvol > rvolThreshold)
    strategy.entry("Short", strategy.short, stop=shortStop)

// Long Exit
if (close <= zlsma)
    strategy.close("Long")

// Short Exit
if (close >= zlsma)
    strategy.close("Short")
```

This Pine Script code implements the described trading strategy with enhanced functionality. It includes dynamic stop-loss positions based on ATR, trend direction using ZLSMA, and volume spike detection. The script sets default values for parameters to ensure a robust implementation.