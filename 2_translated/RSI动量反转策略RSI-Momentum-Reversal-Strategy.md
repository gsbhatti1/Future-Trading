> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long position|
|v_input_2|true|Short position|
|v_input_3|false|Use Martingale strategy|
|v_input_4|100|Capital percentage|
|v_input_5|true|Use CRSI strategy|
|v_input_6|true|Use FRSI strategy|
|v_input_7|true|CRSI+FRSI mode|
|v_input_8|25|RSI limit value|
|v_input_9|true|Use body filter|
|v_input_10|true|Use color filter|
|v_input_11|1900|Start year|
|v_input_12|2100|End year|
|v_input_13|true|Start month|
|v_input_14|12|End month|
|v_input_15|true|Start day|
|v_input_16|31|End day|


> Source (PineScript)

```pinescript
// backtest
start: 2023-10-07 00:00:00
end: 2023-11-06 00:00:00
period: 1h
basePeriod: 15m
exchanges:

// strategy description
strategy("RSI Momentum Reversal Strategy", overlay=false, initial_capital=100)

// input arguments
var bool long_position = v_input_1
var bool short_position = v_input_2
var bool use_martingale = v_input_3
var float capital_percentage = v_input_4 / 100
var bool use_crsi_strategy = v_input_5
var bool use_frsi_strategy = v_input_6
var bool crsi_plus_frsi_mode = v_input_7
var int rsi_limit = v_input_8
var bool use_body_filter = v_input_9
var bool use_color_filter = v_input_10
var int start_year = v_input_11
var int end_year = v_input_12
var bool start_month = v_input_13
var int end_month = v_input_14
var bool start_day = v_input_15
var int end_day = v_input_16

// strategy parameters
rsi_length = 14
crsi_win_ratio_length = 10
crsi_parisian_length = 28
frsi_k_period = 14
frsi_d_smoothing = 3

// RSI calculations
c_rsi = ta.rsi(close, rsi_length)
c_crsi = (ta.ccrsi(c_rsi, crsi_win_ratio_length) + ta.ccrsi(c_rsi, crsi_parisian_length)) / 2
c_frsi = ta.frsi(close, frsi_k_period, frsi_d_smoothing)

// body and color filters
body_filter = na(body_close) ? false : (close > open)
color_filter = close < open ? "red" : "green"

// long condition
long_condition = c_crsi < 20 and c_frsi < rsi_limit and body_filter and use_body_filter

// short condition
short_condition = c_crsi > 80 and c_frsi > (rsi_limit + 5) and not(body_filter) and use_body_filter

// trade execution
if long_condition
    strategy.entry("Long", strategy.long)
    if use_martingale
        // martingale logic here, increase position size based on losses
        pass

if short_condition
    strategy.entry("Short", strategy.short)
    if use_martingale
        // martingale logic here, increase position size based on losses
        pass

// stop loss and exit condition
stop_loss = 10 * close / 100
strategy.exit("Stop Loss", "Long", stop=stop_loss)
strategy.exit("Stop Loss", "Short", stop=stop_loss)

// plot indicators
plot(c_rsi, color=color.blue)
plot(c_crsi, color=color.orange)
plot(c_frsi, color=color.red)
```

```