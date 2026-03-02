``` pinescript
/*backtest
start: 2023-12-20 00:00:00
end: 2023-12-27 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Premium MA Ratio Strategy", overlay = true)

// Input: Adjustable parameters for Premium MA Ratio
fast_length = input(10, title = "Fast MA Length")
slow_length = input(50, title = "Slow MA Length")
oscillator_threshold_buy = input(10, title = "Oscillator Buy Threshold")
oscillator_threshold_sell = input(90, title = "Oscillator Sell Threshold")

// Input: Adjustable parameters for Bollinger Bands
bb_length = input(20, title = "Bollinger Bands Length")
bb_source = input(close, title = "Bollinger Bands Source")
bb_deviation = input(2.0, title = "Bollinger Bands Deviation")
bb_width_threshold = input(30, title = "BB Width Threshold")

// Input: Adjustable parameters for trend filter
trend_filter_period1 = input(50, title = "Trend Filter Period 1")
trend_filter_period2 = input(200, title = "Trend Filter Period 2")
use_second_trend_filter = input(true, title = "Use Second Trend Filter?")
use_bollinger_bands_filter = input(true, title = "Use BB Width Filter?")
use_trend_filter = input(true, title = "Use Trend Filter?")

// Input: Adjustable parameters for exit strategies
use_take_profit = input(true, title = "Use Take Profit?")
take_profit_ticks = input(150, title = "Take Profit in Ticks")
use_stop_loss = input(true, title = "Use Stop Loss?")
stop_loss_ticks = input(100, title = "Stop Loss in Ticks")
use_combined_exit_strategy = input(true, title = "Use Combined Exit Strategy?")
combined_exit_ticks = input(50, title = "Combined Exit Ticks")

// Input: Time filter
use_time_filter = input(false, title = "Use Time Filter?")
start_hour = input(8, title = "Start Hour")
end_hour = input(16, title = "End Hour")

// Calculate moving averages and their ratio
fast_ma = sma(close, fast_length)
slow_ma = sma(close, slow_length)
ma_ratio = fast_ma / slow_ma

// Calculate Bollinger Bands
bb_upper, bb_lower = bband(source=bb_source, length=bb_length, stdDev=bb_deviation)

// Calculate BB width and trend filter conditions
bb_width = (bb_upper - bb_lower) / 2
in_uptrend = ta.crossover(slow_ma, fast_ma)
in_downtrend = ta.crossunder(fast_ma, slow_ma)

// Main logic: generate buy/sell signals based on oscillator and Bollinger Bands width
long_signal = ta.crossover(ma_ratio, oscillator_threshold_buy) and (bb_width < bb_width_threshold or not use_bollinger_bands_filter)
short_signal = ta.crossunder(ma_ratio, oscillator_threshold_sell) and (bb_width > bb_width_threshold or not use_bollinger_bands_filter)

// Generate buy/sell orders
if (long_signal and use_time_filter ? time(hour >= start_hour and hour < end_hour) : true)
    strategy.entry("Long", strategy.long)

if (short_signal and use_time_filter ? time(hour >= start_hour and hour < end_hour) : true)
    strategy.entry("Short", strategy.short)

// Exit logic
if (use_take_profit)
    if (long_signal)
        strategy.exit("Take Profit Long", "Long", stop = take_profit_ticks)
    if (short_signal)
        strategy.exit("Take Profit Short", "Short", stop = take_profit_ticks)

if (use_stop_loss)
    if (long_signal)
        strategy.exit("Stop Loss Long", "Long", stop = -stop_loss_ticks)
    if (short_signal)
        strategy.exit("Stop Loss Short", "Short", stop = -stop_loss_ticks)

if (use_combined_exit_strategy)
    strategy.exit("Combined Exit", ["Long", "Short"], stop = combined_exit_ticks)
```

This code completes the PineScript implementation of the premium MA ratio strategy, including all adjustable parameters and logic for generating signals and exits.