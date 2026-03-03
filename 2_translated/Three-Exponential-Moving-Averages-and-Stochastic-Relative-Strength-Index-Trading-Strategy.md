> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_10_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_1|true|(?Backtesting range)Start Date|
|v_input_2|true|Start Month|
|v_input_3|1900|Start Year|
|v_input_4|true|End Date|
|v_input_5|true|End Month|
|v_input_6|2040|End Year|
|v_input_7|8|(?EMAs)Fast EMA|
|v_input_8|14|Medium EMA|
|v_input_9|50|Slow EMA|
|v_input_11|3|(?Stoch-RSI)K|
|v_input_12|3|D|
|v_input_13|14|RSI Length|
|v_input_14|14|Stochastic Length|
|v_input_15_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_16|14|(?ATR)Length|
|v_input_17|0|Smoothing: RMA|SMA|EMA|WMA|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//              3ESRA
//              v0.2a

// Coded by Vaida Bogdan

// 3ESRA consists of a 3 EMA cross + a close above (for longs) the quickest EMA
// or below (for shorts). Note that I've deactivated the RSI Cross Over/Under
// (you can modify the code and activate it). The strategy also uses a stop loss
// that's at 1 ATR distance from the entry price and a take profit that's at
// 4 times the ATR distance from the entry.

//@version=5
strategy("3-Exponential-Moving-Averages-and-Stochastic-Relative-Strength-Index-Trading-Strategy", overlay=true)

// Input parameters
fast_ema = input(8, title="(?EMAs)Fast EMA")
medium_ema = input(14, title="Medium EMA")
slow_ema = input(50, title="Slow EMA")
k_length = input(3, title="(?Stoch-RSI)K")
d_length = input(3, title="D")
rsi_length = input(14, title="RSI Length")
stochastic_length = input(14, title="Stochastic Length")
atr_length = input(14, title="(?ATR)Length")

// Calculate EMAs
ema_fast = ta.ema(close, fast_ema)
ema_medium = ta.ema(close, medium_ema)
ema_slow = ta.ema(close, slow_ema)

// Calculate RSI and Stochastic RSI
rsi = ta.rsi(close, rsi_length)
stoch_rsi_k = ta.sma(rsi, k_length)
stoch_rsi_d = ta.sma(stoch_rsi_k, d_length)

// Entry conditions
long_condition = ema_fast > ema_medium and ema_medium > ema_slow and close > ema_fast
short_condition = ema_fast < ema_medium and ema_medium < ema_slow and close < ema_fast

// Stop loss and take profit
stop_loss = atr_length == 0 ? na : ta.atr(1)
take_profit_factor = atr_length == 0 ? 4.0 : 1.0

long_entry_price = na
short_entry_price = na
if (long_condition)
    long_entry_price := close
else if (short_condition)
    short_entry_price := close

strategy.entry("Long", strategy.long, when=long_entry_price > na and stop_loss == na or not is_nan(long_entry_price))
strategy.close("Long", when=strategy.position_size == 1 and strategy.position_avg_price + take_profit_factor * stop_loss > close)

if (short_condition)
    short_entry_price := close
else if (long_condition)
    long_entry_price := close

strategy.entry("Short", strategy.short, when=short_entry_price > na and stop_loss == na or not is_nan(short_entry_price))
strategy.close("Short", when=strategy.position_size == -1 and strategy.position_avg_price - take_profit_factor * stop_loss < close)

// Plot EMAs
plot(ema_fast, color=color.blue)
plot(ema_medium, color=color.green)
plot(ema_slow, color=color.red)

// Plot RSI and Stochastic RSI
hline(70, "Overbought", color=color.orange)
hline(30, "Oversold", color=color.purple)
plot(stoch_rsi_k, title="Stoch K", color=color.blue, linewidth=2)
plot(stoch_rsi_d, title="Stoch D", color=color.green, linewidth=2)
```