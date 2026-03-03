``` pinescript
/*backtest
start: 2023-09-19 00:00:00
end: 2023-09-26 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

// strategy(title="MACD趋势跟踪交易策略v0.2",calc_on_order_fills=false,calc_on_every_tick=false, initial_capital=10000,commission_type=strategy.commission.percent, commission_value=0.00,overlay = true,default_qty_type = strategy.cash, default_qty_value = 10000)

// Strategy Description
strategy(title="MACD Trend Following Trading Strategy v0.2", calc_on_order_fills=false, calc_on_every_tick=false, initial_capital=10000, commission_type=strategy.commission.percent, commission_value=0.00, overlay=true, default_qty_type=strategy.cash, default_qty_value=10000)

// Parameters
v_input_1 = input(3, title="%D Smoothing", minval=1)
v_input_2 = input(14, title="%K Length", minval=1)
v_input_3 = input(42, title="%K2 Length", minval=1)
v_input_4 = input(126, title="%K3 Length", minval=1)
v_input_5 = input(378, title="%K4 Length", minval=1)
v_input_6 = input(14, title="%K5 Length", minval=1)
v_input_7 = input(30, title="%K6 Length", minval=1)
v_input_8 = input(true, title="%K Smoothing")
v_input_9 = input(0.3, title="buffer")
v_input_10 = input(144, title="Fast Length")
v_input_11 = input(312, title="Slow Length")
v_input_12_close = input(0, title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"])
v_input_13 = input(108, title="Signal Smoothing")
v_input_14 = input(0, title="Oscillator MA Type: EMA|SMA", options=["EMA", "SMA"])
v_input_15 = input(0, title="Signal Line MA Type: EMA|SMA", options=["EMA", "SMA"])
v_input_16 = input(30, title="MACDCHA步长")
v_input_17 = input(20, title="MACDCHA步长2")
v_input_18 = input(4, title="做多止损 %")
v_input_19 = input(10, title="做多止盈 %")
v_input_20 = input(4, title="做空止损 %")
v_input_21 = input(10, title="做空止盈 %")

// MACD Calculation
[fast_length, slow_length] = [v_input_10, v_input_11]
[signal_length, signal_smooth] = [v_input_13, v_input_18]
[oscillator_ma, signal_ma] = [v_input_14, v_input_15]

// Stoch Calculation
k = sma(stoch(close, high, low, v_input_2), v_input_8)
k2 = sma(stoch(close, high, low, v_input_3), v_input_8 * 3)
k3 = sma(stoch(close, high, low, v_input_4), v_input_8 * 9)
k4 = sma(stoch(close, high, low, v_input_5), v_input_8 * 27)
k5 = sma(stoch(close, high, low, v_input_6), v_input_8)
k6 = sma(stoch(close, high, low, v_input_7), v_input_8)

// MACDCHA Calculation
[macd_hist, macd_line, macd_signal] = macd(close, fast_length, slow_length, signal_length)

// MACDCHA Step Lengths
[step1, step2, step3, step4, step5, step6, step7] = [v_input_16, v_input_17, v_input_18, v_input_19, v_input_20, v_input_21, v_input_22]

// Buy and Sell Conditions
buy_condition = crossover(k, k2) and crossover(macd_line, macd_signal)
sell_condition = crossunder(k, k2) and crossunder(macd_line, macd_signal)

// Buy and Sell Orders
if (buy_condition)
    strategy.entry("Buy", strategy.long)

if (sell_condition)
    strategy.close("Buy")

// Stop Loss and Take Profit
stop_loss_long = strategy.close_entry_price * (1 - v_input_18 / 100)
take_profit_long = strategy.close_entry_price * (1 + v_input_19 / 100)
stop_loss_short = strategy.close_entry_price * (1 + v_input_20 / 100)
take_profit_short = strategy.close_entry_price * (1 - v_input_21 / 100)

// Set Stop Loss and Take Profit
if (buy_condition)
    strategy.exit("Buy", "Buy", stop=stop_loss_long, limit=take_profit_long)

if (sell_condition)
    strategy.exit("Buy", "Buy", stop=stop_loss_short, limit=take_profit_short)
```

This script integrates the MACD and Stoch indicators to implement a trend-following trading strategy. It includes detailed parameter settings and trading conditions, ensuring the strategy is comprehensive and adaptable to different market conditions.