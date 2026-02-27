> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|src: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|34|length|
|v_input_float_1|2|mult|
|v_input_int_2|34|Length|
|v_input_float_2|2|Multiplier|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-05-03 00:00:00
end: 2024-05-08 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Unique Bollinger Bands Strategy", overlay=true)
src = v_input_1_close >= 0 ? close : high == low ? open : (high + low) / 2

// Calculate Bollinger Bands
length = v_input_int_1
mult = v_input_float_1
basis = sma(src, length)
dev = mult * stdev(src, length)
upperBB = basis + dev
lowerBB = basis - dev

// Calculate Stochastic Oscillator
kLength = v_input_int_2
dLength = v_input_int_2
srcStoch = highest(high, kLength) == low ? close : (high + low) / 2
highK = sma(srcStoch, dLength)
lowK = sma(srcStoch, dLength)
k = (close - lowest(lowK)) / (highest(highK) - lowest(lowK))
d = sma(k, dLength)

// Buy Condition: Price breaks above upper Bollinger Band and Stochastic %K crosses above %D
longCondition = close > upperBB and k > d

// Sell Condition: Price falls below lower Bollinger Band and Stochastic %K crosses below %D
shortCondition = close < lowerBB and k < d

// Place orders
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)
```

This script implements the described trading strategy, using Bollinger Bands and the Stochastic Oscillator to generate buy and sell signals.