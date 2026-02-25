``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI-and-Dual-EMA-Crossover-Signal-Quantitative-Strategy", overlay=true)

// Strategy Arguments
v_input_int_1 = input.int(14, title="RSI Length")
v_input_int_2 = input.int(100, title="EMA Length (Closing Price)")
v_input_int_3 = input.int(20, title="EMA Length (Low Price)")
v_input_int_4 = input.int(30, title="Oversold Level")
v_input_int_5 = input.int(70, title="Overbought Level")

// RSI Calculation
rsi_value = rsi(close, v_input_int_1)

// EMA Calculations
ema_close = ta.ema(close, v_input_int_2)
ema_low = ta.ema(lowest(low, v_input_int_3), v_input_int_3)

// Buy Signal Condition
buy_condition = close < ema_close and close < ema_low and rsi_value < v_input_int_4

// Sell Signal Condition
sell_condition = close > ema_close and close > ema_low and rsi_value > v_input_int_5

// Plot EMA lines
plot(ema_close, color=color.blue, title="EMA100")
plot(ema_low, color=color.red, title="EMA20")

// Signal Generation
if (buy_condition)
    strategy.entry("Buy", strategy.long)

if (sell_condition)
    strategy.close("Buy")
```

This Pine Script implements the RSI and Dual EMA Crossover Signal Quantitative Strategy as described in the provided text. It includes the necessary arguments for customizing the RSI length, EMA lengths, oversold level, and overbought level. The script also plots the EMA lines on the chart and generates buy/sell signals based on the defined conditions.