``` pinescript
/*backtest
start: 2024-02-25 00:00:00
end: 2025-02-22 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]
*/

//@version=5
strategy("PSAR & RSI Strategy with Risk Management", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// User Inputs
psar_start = input.float(0.02, title="PSAR Start")
psar_increment = input.float(0.02, title="PSAR Increment")
psar_max = input.float(0.2, title="PSAR Max")
rsi_length = input.int(14, title="RSI Length")
rsi_overbought = input.int(70, title="RSI Overbought Level")
rsi_oversold = input.int(30, title="RSI Oversold Level")

tp_percent = input.float(5, title="Take Profit %") / 100  // Take Profit Level
sl_percent = input.float(3, title="Stop Loss %") / 100    // Stop Loss Level

// PSAR Calculation
psar = ta.sar(psar_start, psar_increment, psar_max)

// RSI Calculation
rsi = ta.rsi(close, rsi_length)

// Buy & Sell Conditions
buy_signal = ta.crossover(close, psar) and rsi < rsi_oversold
sell_signal = ta.crossunder(close, psar) and rsi > rsi_overbought

// Plot PSAR on Chart
plot(psar, style=plot.style_cross, color=color.blue, title="PSAR")

// Buy & Sell Signals on Chart
plotshape(series=buy_signal, location=location.belowbar, color=color.green, style=shape.labelup, title="BUY Signal")
plotshape(series=sell_signal, location=location.abovebar, color=color.red, style=shape.labeldown, title="SELL Signal")

// RSI Visualization (Dynamic Colors)
rsi_color = rsi > rsi_overbought ? color.red : rsi < rsi_oversold ? color.green : color.blue
plot(rsi, title="RSI", color=rsi_color, linewidth=2)
hline(rsi_overbought, "Overbought", color=color.red)
hline(rsi_oversold, "Oversold", color=color.green)

// Alerts for Buy & Sell
alertcondition(buy_signal, title="Buy Signal Alert", message="BUY Signal Generated")
alertcondition(sell_signal, title="Sell Signal Alert", message="SELL Signal Generated")

// Trade Execution and Risk Management
long_condition = ta.crossover(close, psar) and rsi < rsi_oversold
short_condition = ta.crossunder(close, psar) and rsi > rsi_overbought

if (long_condition)
    strategy.entry("Long", strategy.long)
    strategy.exit("Take Profit/Stop Loss", "Long", profit=tp_percent * close, loss=sl_percent * close)

if (short_condition)
    strategy.entry("Short", strategy.short)
    strategy.exit("Take Profit/Stop Loss", "Short", profit=tp_percent * close, loss=sl_percent * close)
```

This Pine Script code implements the dynamic RSI and PSAR crossover trading strategy with a risk management system. It includes user inputs for setting parameters, conditions for entering trades based on signals from the PSAR and RSI indicators, and alerts for both buy and sell signals. Additionally, it handles trade execution and incorporates stop-loss and take-profit levels to manage risk effectively.