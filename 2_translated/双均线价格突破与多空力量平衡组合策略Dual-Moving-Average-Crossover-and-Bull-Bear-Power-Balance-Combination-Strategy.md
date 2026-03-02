```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2024-01-07 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 23/05/2022
// This is a combination strategy to get a cumulative signal.
//
// First, using the dual moving average lines of 2-period and 20-period EMA to determine if price breaks through the moving averages as a basic criterion for entering the market.
// At the same time, the auxiliary indicator "Bull Bear Power Balance Indicator" further identifies the relative power between bulls and bears to avoid mis-operations.
// The two types of indicators jointly generate the final trading signal.

strategy("Dual-Moving-Average-Crossover-and-Bull-Bear-Power-Balance-Combination-Strategy", overlay=false)

// Strategy Arguments
v_input_int_1 = input.int(14, title="?●═════ 2/20 EMA ═════● Length")
v_input_float_1 = input.float(-15, title="?●═════ Bull And Bear Balance ═════● SellLevel")
v_input_float_2 = input.float(15, title="BuyLevel")
v_input_bool_1 = input.bool(false, title="?●═════ MISC ═════● Trade reverse")
v_input_int_2 = input.int(1, title="?●═════ Time Start ═════● From Day")
v_input_int_3 = input.int(1, title="From Month")
v_input_int_4 = input.int(2005, title="From Year")

// Calculate 2/20 EMA
ema_2 = ta.ema(close, v_input_int_1)
ema_20 = ta.ema(close, v_input_int_1 * 10)

// Determine if price breaks through the moving averages
long_condition = ta.crossover(ema_2, ema_20)
short_condition = ta.crossunder(ema_2, ema_20)

// Bull Bear Power Balance Indicator
bull_power = ta.ema(close - close[1], v_input_int_1) * 100
bear_power = ta.ema(open - open[1], v_input_int_1) * 100

// Buy and Sell Conditions
buy_condition = long_condition and bull_power > v_input_float_1
sell_condition = short_condition and bear_power < v_input_float_2

if (v_input_bool_1)
    if (buy_condition)
        strategy.entry("Long", strategy.long)
    elif (sell_condition)
        strategy.exit("Short", "Long")
else
    if (buy_condition)
        strategy.entry("Long", strategy.long, when=ta.time(v_input_int_2, v_input_int_3, v_input_int_4))
    elif (sell_condition)
        strategy.close("Long")

// Plot EMA lines and signals
plot(ema_2, color=color.blue, title="2-EMA")
plot(ema_20, color=color.red, title="20-EMA")
hline(v_input_float_1, "SellLevel", color=color.orange)
hline(v_input_float_2, "BuyLevel", color=color.green)

// Additional notes
```

This Pine Script translates the provided Chinese strategy into English and keeps all code blocks intact.