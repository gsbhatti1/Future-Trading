```pinescript
/*backtest
start: 2023-04-24 00:00:00
end: 2024-04-29 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @ Julien_Eche

//@version=5
strategy("MACD RSI Ichimoku Strategy", overlay=true)

string t1 = ("If checked, this strategy is suitable for those who buy and sell. If unchecked, it is suitable for those who only want to take long positions—buying and closing buys.")

start_date = input(timestamp("1975-01-01T00:00:00"), title="Start Date")
end_date = input(timestamp("2099-01-01T00:00:00"), title="End Date")

tenkan_sen_length = input.int(9, minval=1, title="Tenkan-sen Length")
kijun_sen_length = input.int(26, minval=1, title="Kijun-sen Length")
senkou_span_a_length = input.int(52, minval=1, title="Senkou Span A Length")
macd_fast_length = input.int(12, minval=1, title="MACD Fast Length")
macd_slow_length = input.int(26, minval=1, title="MACD Slow Length")
macd_signal_length = input.int(9, minval=1, title="MACD Signal Length")
rsi_length = input.int(14, minval=1, title="RSI Length")

buy_sell = input.bool(false, title="Buy/Sell")

// Ichimoku Cloud
src = close
conversion_line = na
base_line = na
leading_span_a = na
leading_span_b = na

if barstate.isfirst
    conversion_line := ta.sma(src, tenkan_sen_length)
    base_line := ta.sma(conversion_line, kijun_sen_length)
    leading_span_a := ta.ema(base_line, (senkou_span_a_length - 26) / 2 + 26)
    leading_span_b := ta.ema(close, (tenkan_sen_length - 9) / 2 + 9)

plot(leading_span_a, color=color.blue, title="Leading Span A")
plot(leading_span_b, color=color.red, title="Leading Span B")

// MACD
fast_k = ta.sma(close, macd_fast_length)
slow_d = ta.sma(close, macd_slow_length)
macd_line = fast_k - slow_d
signal_line = ta.sma(macd_line, macd_signal_length)

plot(macd_line, color=color.orange, title="MACD Line")
plot(signal_line, color=color.green, title="Signal Line")

// RSI
rsi = ta.rsi(close, rsi_length)
plot(rsi, color=color.purple, title="RSI")

// Strategy Logic
if (barstate.islast and not na(macd_line) and not na(signal_line) and not na(rsi))
    if macd_line > signal_line and rsi < 70 and close > leading_span_b and time >= start_date and time <= end_date
        strategy.entry("Long", strategy.long)

    if macd_line < signal_line or close <= leading_span_a
        strategy.close("Long")
```