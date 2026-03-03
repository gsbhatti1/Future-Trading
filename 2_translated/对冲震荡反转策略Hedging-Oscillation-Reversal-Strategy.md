> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|Length BB|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_float_1|2|StdDev BB|
|v_input_int_2|20|Length Envelope|
|v_input_2|true|percent|
|v_input_3|false|exponential|
|v_input_4|14|ADX Smoothing|
|v_input_5|14|DI Length|
|v_input_int_3|50|%K Length|
|v_input_int_4|20|%K Smoothing|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-12 00:00:00
end: 2023-12-19 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License Version 2.0.
// You can obtain a copy of the License at https://mozilla.org/MPL/2.0/.

//@version=5
strategy("Hedging-Oscillation-Reversal-Strategy", overlay=true)

// Input parameters
length_bb = input.int(20, title="Length BB")
source = input.source(close, title="Source")
std_dev = input.float(2, title="StdDev BB")
length_env = input.int(20, title="Length Envelope")
percent = input.bool(true, title="Percent")
exponential = input.bool(false, title="Exponential")
src_adx = input.int(14, title="ADX Smoothing")
src_di = input.int(14, title="DI Length")
src_k = input.int(50, title="%K Length")
src_d = input.int(20, title="%K Smoothing")

// Bollinger Bands
bb = ta.bbands(source, length_bb, std_dev, 0, percent, exponential)
bb_upper = bb[1].top
bb_lower = bb[1].bottom

// Envelope Lines
env = ta.envelop(bb[1].close, length_env, percent, exponential)
env_upper = env[1].top
env_lower = env[1].bottom

// ADX and DI
adx = ta.adx(bb[1].close, src_di, src_di)
di_plus = ta.adx(bb[1].close, src_di, src_di, true)
di_minus = ta.adx(bb[1].close, src_di, src_di, false)

// Stochastic
k = ta.stoch(bb[1].close, bb[1].high, bb[1].low, src_k)
d = ta.sma(k, src_d)

// Conditions for short positions
short_exit_condition = ta.crossover(bb[1].close, bb_lower) or ta.crossover(env[1].close, env_lower) or d < 50
short_exit = na(short_exit_condition) ? na : short_exit_condition

// Conditions for long positions
long_exit_condition = ta.crossunder(bb[1].close, bb_upper) or ta.crossunder(env[1].close, env_upper) or d > 50
long_exit = na(long_exit_condition) ? na : long_exit_condition

// Plot indicators
plot(bb_upper, color=color.blue, title="Bollinger Bands Upper")
plot(bb_lower, color=color.red, title="Bollinger Bands Lower")
plot(env_upper, color=color.green, title="Envelope Upper")
plot(env_lower, color=color.orange, title="Envelope Lower")
plot(k, color=color.purple, title="%K")
plot(d, color=color.orange, title="%D")

// Trading logic
if (ta.crossover(bb[1].close, bb_upper) and ta.crossover(env[1].close, env_upper) and d < 50)
    strategy.entry("Short", strategy.short)

if (ta.crossunder(bb[1].close, bb_lower) and ta.crossunder(env[1].close, env_lower) and d > 50)
    strategy.entry("Long", strategy.long)

// Stop loss for short positions
if (bb[1].close < bb_lower or env[1].close < env_lower or d < 50)
    strategy.exit("Short Exit", "Short", stop=bb_lower)

// Stop loss for long positions
if (bb[1].close > bb_upper or env[1].close > env_upper or d > 50)
    strategy.exit("Long Exit", "Long", stop=bb_upper)
```

This PineScript code defines the Hedging-Oscillation-Reversal-Strategy using multiple technical indicators to identify market reversals and generate trade signals.