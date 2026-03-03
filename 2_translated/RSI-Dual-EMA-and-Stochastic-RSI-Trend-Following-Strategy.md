``` pinescript
/*backtest
start: 2025-01-10 00:00:00
end: 2025-02-09 00:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA 9/21 + Stoch RSI Strategy", shorttitle="EMA+StochRSI", overlay=true)

// ===== User Inputs ===== //
emaFastLen     = input.int(9,   "Fast EMA (9)")
emaSlowLen     = input.int(21,  "Slow EMA (21)")
rsiLen         = input.int(14,  "RSI Length")
stochRsiLen    = input.int(14,  "Stoch RSI Length")     // range from which we take min/max RSI
stochSignalLen = input.int(3,   "Stoch RSI K/D Smoothing")
overSold       = input.int(20,  "Stoch RSI Oversold (%)")
overBought     = input.int(80,  "Stoch RSI Overbought (%)")

// ===== Calculation of EMA(9) and EMA(21) ===== //
emaFast = ta.ema(close, emaFastLen)
emaSlow = ta.ema(close, emaSlowLen)

// ===== Calculation of RSI and Stoch RSI ===== //
// 1) Classic RSI
rsiValue = ta.rsi(close, rsiLen)

// 2) Convert RSI -> Stoch RSI: 
//    (rsiValue - ta.lowest(rsiValue, stochRsiLen)) / (ta.highest(rsiValue, stochRsiLen) - ta.lowest(rsiValue, stochRsiLen)) * 100
//    Then smooth K and D (similar to regular Stochastic)
rsiLowest  = ta.lowest(rsiValue, stochRsiLen)
rsiHighest = ta.highest(rsiValue, stochRsiLen)
stochRSIK  = (rsiValue - rsiLowest) / (rsiHighest - rsiLowest) * 100
stochRSID  = ta.sma(stochRSIK, stochSignalLen)

// ===== Trading Conditions ===== //
// Long Condition
longCondition = ta.crossover(emaFast, emaSlow) and stochRSID < overSold
if (longCondition)
    strategy.entry("Long", strategy.long)

// Short Condition
shortCondition = ta.crossunder(emaFast, emaSlow) and stochRSID > overBought
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Conditions
// Exit on opposite signal
exitCondition = ta.crossover(emaSlow, emaFast) or ta.crossunder(emaSlow, emaFast)
if (exitCondition)
    strategy.close("Long")
    strategy.close("Short")
```

This Pine Script translates the provided strategy into a clear and functional format. It includes the necessary calculations for EMAs, RSI, and Stochastic RSI, as well as the conditions for entering and exiting trades based on the specified parameters.