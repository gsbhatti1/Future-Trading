> Name

Quantitative Trading Strategy Based on Stoch and EMA

> Author

ChaoZhang

> Strategy Description


[trans]

This article explains in detail a quantitative trading strategy that combines the Stoch indicator with the EMA moving average. It generates trading signals based on Stoch values, while using EMA to filter out non-mainstream signals.

I. Strategy Logic

The main tools and logic are:

1. Calculate the Stoch indicator with K and D values; K reflects fast price changes, and D is a smoothed signal.
2. Set overbought/oversold zones for the Stoch. Signals are based on relative values of K and D.
3. Compute EMA over a period to gauge the price mainstream trend.
4. Only take trades when Stoch signals agree with EMA direction.
5. Establish long or short positions according to signals, setting stop loss and take profit points.

Together, the Stoch indicator captures opportunities in overbought/oversold areas, while the EMA filters out invalid signals. This combination forms a robust trading strategy.

II. Advantages of the Strategy

The biggest advantage is the complementarity of indicators. The Stoch judges O/S levels, and EMA gauges the mainstream trend, combining to reduce mistakes.

Additionally, adjustable K/D values allow optimization across different products.

Finally, setting stop loss/take profit clearly defines risk/reward for prudent money management.

III. Potential Weaknesses

However, some potential issues are:

Firstly, both Stoch and EMA can lag, causing missed optimal entries.

Secondly, tight stops may trigger many invalidations prematurely.

Lastly, extensive parameter optimization is required to avoid overfitting.

IV. Summary

In summary, this article has explained a quantitative strategy combining Stoch and EMA. It identifies opportunities for overbought/oversold reversals, with the EMA filtering out invalid signals. With proper tuning, this strategy can achieve steady profits but needs to manage the mentioned risks.


[/trans]

> Strategy Arguments


|Argument|Default|Description|
|--------|-------|-----------|
|v_input_int_3|14|RSI Length|
|v_input_int_4|14|Stochastic Length|
|v_input_1_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_string_1|0|Long Signal Type: Stoch Below Value|K&D Cross Below Value|Stoch CrossUp the Value|
|v_input_string_2|0|Short Signal Type: Stoch Above Value|K&D Cross Above Value|Stoch CrossDown the Value|
|v_input_float_1|false|(?TP / SL)Take Profit (%) [0 = Disabled]|
|v_input_float_2|false|Stop Loss (%) [0 = Disabled]|
|v_input_int_1|true|(?Stochastic)K Smoothing|
|v_input_int_2|3|D Smoothing|
|v_input_2_close|0|(?EMA)Source EMA : close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|200|Length EMA |
|v_input_4|20|(?Signal Options)Stoch below/cross this value for Long signals|
|v_input_5|80|Stoch above/cross this value for Short signals|
|v_input_6|timestamp(01 Jan 2014 00:00 +0000)|(?Backtesting)Backtesting Start Time|
|v_input_7|timestamp(01 Jan 2100 23:59 +0000)|Backtesting End Time|
|v_input_string_3|deribit-testnet|(?PV Settings)Exchange|
|v_input_string_4|btc-perpetual|Symbol|
|v_input_string_5||Account|
|v_input_string_6||PV Alert Name Longs|
|v_input_string_7||PV Alert Name Shorts|
|v_input_string_8||PV Alert Name TP/SL|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-15 00:00:00
end: 2023-08-26 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/

//@version=5
strategy(title="EMA Stoch Strategy For ProfitView", overlay=true, calc_on_every_tick=true, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1, initial_capital=1000)

// take profit and stop loss
TakeProfitPercent = input.float(defval=0.0, title="Take Profit (%) [0 = Disabled]", minval=0, step=.25, group='TP / SL')
StopLossPercent = input.float(defval=0.0, title="Stop Loss (%) [0 = Disabled]", minval=0, step=.25, group='TP / SL')

// Stoch
smoothK = input.int(1, title="K Smoothing", minval=1, group='Stochastic')
periodD = input.int(3, title="D Smoothing", minval=1, group='Stochastic')
lenghtRSI = input.int(14, "RSI Length", minval=1)
lenghtStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")

rsi1 = ta.rsi(src, lenghtRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lenghtStoch), smoothK)
d = ta.sma(k, periodD)

plot(k, title="K", color=#2962FF)
plot(d, title="D", color=#FF6D00)
// bgcolor(color=color.from_gradient(k, 0, 100, color.new(#2962FF, 100), color.new(#2962FF, 95)), title="K BG")
// bgcolor(color=color.from_gradient(d, 0, 100, color.new(#FF6D00, 100), color.new(#FF6D00, 95)), title="D BG")

// EMA
src1 = input(close, title='Source EMA ', group='EMA')
len1 = input(200, title='Length EMA ', group='EMA')
ema1 = ta.ema(src1, len1)
plot(ema1, title='EMA', color=color.blue, linewidth=2)

// signals
LongVal = input(20, title='Stoch below/cross this value for Long signals', group='Signal Options')
scegliLong = input.string('Stoch Below Value', options=['Stoch Below Value' , 'K&D Cross Below Value' , 'Stoch CrossUp the Value'] , title='Long Signal Type')

long1 = scegliLong == 'Stoch Below Value' ? k < LongVal and d < LongVal and close > k : na
```