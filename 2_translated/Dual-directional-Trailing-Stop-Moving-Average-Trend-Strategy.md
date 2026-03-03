> Name

Dual-directional-Trailing-Stop-Moving-Average-Trend-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/123a7de0b9d63cc5b54.png)
[trans]

### Overview

This strategy combines the Super Trend, SSL Hybrid Baseline Channel and QQE indicators to implement dual-directional position tracking stop loss and capture mid-to-long term trends.

### Strategy Logic

The strategy is mainly based on the following key points:

1. Use the Super Trend indicator to determine the overall trend direction and assist in judging entry timing.
2. Use the SSL Hybrid Baseline Channel to determine specific entry points. Channel breakouts serve as the basic entry signal.
3. Use QQE indicator crosses to provide confirmation for entry signals.
4. Use the ATR indicator to aid in stop loss and take profit calculations.
5. Employ percentage-based risk management and dynamic stop adjustment to control per-trade risk.

The entry logic requires a Super Trend reversal along with a price breakout of the baseline channel and a cross of the QQE indicator before entering a position.

This combined indicator system can effectively control entry timing and avoid unnecessary entries during market churns.

The exit logic is simple - a Super Trend reversal serves as the signal to close positions, in addition to triggered stop losses and take profits.

### Advantage Analysis 

The biggest advantage of this strategy is using a combination of indicators to filter out false breakouts and reduce invalid trades.

Another major highlight is the use of percentage-based stops to control per-trade risk.  

By using ATR to calculate stop distance and combining that with a configurable multiplier, we can clearly see the risk taken per trade. This is critical for proper risk management.

We can even set a max tolerable loss percentage to limit total losses.  

The use of a trailing stop to lock in profits is also a key part of enhancing returns.

### Risk Analysis

The biggest risk of this strategy is the probability of combined signal errors. Despite our use of multi-indicator filtering, no indicator is perfect.

When Super Trend shows a false breakout, or QQE gives incorrect crosses, it becomes easy for this strategy to mistakenly enter positions and face increased likelihood of stopped out trades.

There is also some risk of over-optimization with this strategy. Care should be taken to avoid excessive reliance on historical patterns when setting parameters.  

We need to pay attention to key settings like ATR period, stop multiplier, risk percentage etc. These require individual tuning for different instruments.

### Optimization Opportunities

There remains room for further enhancements:

1. Test combinations with more indicators like adding in the KD oscillator.
2. Examine parameter stability under different configurations.
3. Try auto-optimization techniques like machine learning.
4. Introduce adaptive stop logic to adjust stop distance based on market volatility.
5. Build re-entry logic to reduce missed opportunities after stops are triggered.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_3_low|0|RSI Source: low|high|close|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_1|timestamp(20 Jan 2009 00:00 +0900)|(?Time)Start Date|
|v_input_2|timestamp(20 Dec 2030 00:00 +0900)|End Date|
|v_input_bool_1|true|(?Long / Short)Long?|
|v_input_bool_2|true|Short?|
|v_input_bool_3|false|(?Filters)ATR Filter On?|
|v_input_int_1|9|Length for ATR Filter|
|v_input_int_2|27|SMA Length for ATR SMA|
|v_input_bool_4|false|EMA Filter On?|
|v_input_int_3|122|EMA Length|
|v_input_bool_5|false|ADX Filter On?|
|v_input_bool_6|false|DMI Filter On?|
|v_input_int_4|18|ADX Length|
|v_input_int_5|36|ADX Threshold|
|v_input_int_6|21|(?1: SuperTrend)ATR Length|
|v_input_float_1|8|Factor|
|v_input_bool_7|true|(?2: SSL Hybrid)use true range for Keltner Channel?|
|v_input_string_1|0|Baseline Type: EMA|SMA|DEMA|TEMA|LSMA|WMA|VAMA|TMA|HMA|McGinley|
|v_input_int_7|30|Baseline Length|
|v_input_float_2|0.2|Base Channel Multiplier|
|v_input_int_8|42|Volatility lookback length(for VAMA)|
|v_input_int_9|11|(?3: QQE MOD)RSI Length|
|v_input_int_10|9|RSI Smoothing|
|v_input_float_3|4|Fast QQE Factor|
|v_input_int_11|4|Thresh-hold|
|v_input_int_12|42|Bollinger Length|
|v_input_float_4|0.27|BB Multiplier|
|v_input_int_13|6|RSI 2  Length|
|v_input_int_14|5|RSI Smoothing|
|v_input_float_5|1.61|Fast QQE2 Factor|
|v_input_int_15|3|Thresh-hold|
|v_input_4_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_bool_8|true|(?Stop Loss)Enable SL & TP?|
|v_input_bool_9|false|Enable Trailing SL?|
|v_input_string_2|0|Stop Loss Type: ATR|Percent|Previous LL / HH|
|v_input_int_16|14|ATR Length|
|v_input_float_6|3|ATR Multiplier|
|v_input_float_7|3|Percent|
|v_input_int_17|30|Lowest Price Before Entry|
|v_input_bool_10|true|(?Take Profit)Use Take Profi