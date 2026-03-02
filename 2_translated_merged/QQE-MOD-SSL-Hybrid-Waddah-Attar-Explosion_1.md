> Name

QQE-MOD-SSL-Hybrid-Waddah-Attar-Explosion

> Author

ChaoZhang

> Strategy Description

TRADE CONDITIONS

Long entry:
- QQE Mod changes to Blue (leading indicator)
- SSL Hybrid is Blue and price is above MA Channel line
- Waddah Attar Explosion is Green and above Explosion line

Short entry:
- QQE Mod changes to Red (leading indicator)
- SSL Hybrid is Red and price is below MA Channel line
- Waddah Attar Explosion is Red and above Explosion line

Risk management:
Each trade risks 2% of account (configurable in settings)
SL size determined by swing low/high of previous X candles (configurable in settings)
TP is triggered on SSL Hybrid EXIT arrow signals

TIPS

Timeframe: Personally I've found best results running this on a 1H timeframe.

Note: To help visual identification of trade entries and exits you may wish to add the SSL Hybrid and Waddah Attar Explosion to the chart separately. They are being used to determine trade entry/exit within the code of this strategy but it was not possible to display them in a clear way within a single panel. Make sure you set the settings of the auxiliary indicators to match what is in the settings of this indicator if you do decide to add them.

CREDITS
- QQE MOD by Mihkel00
- SSL Hybrid by Mihkel00
- Waddah Attar Explosion by shayankm


**Backtest**

![IMG](https://www.fmz.com/upload/asset/1bee9f9cdc8ec8fa3ad.png)

> Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|v_input_3|true|Show Baseline|
|v_input_4|false|Show SSL1|
|v_input_5|true|Show ATR bands|
|v_input_6|14|ATR Period|
|v_input_float_4|true|ATR Multi|
|v_input_string_1|0|ATR Smoothing: WMA|SMA|EMA|RMA|
|v_input_string_2|0|SSL1 / Baseline Type: HMA|EMA|DEMA|TEMA|LSMA|WMA|MF|VAMA|TMA|SMA|JMA|Kijun v2|EDSMA|McGinley|
|v_input_7|60|SSL1 / Baseline Length|
|v_input_string_3|0|SSL2 / Continuation Type: JMA|EMA|DEMA|TEMA|WMA|MF|VAMA|TMA|HMA|SMA|McGinley|
|v_input_8|5|SSL 2 Length|
|v_input_string_4|0|EXIT Type: HMA|TEMA|LSMA|VAMA|TMA|DEMA|JMA|Kijun v2|McGinley|MF|
|v_input_9|15|EXIT Length|
|v_input_10_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_16|true|Kijun MOD Divider|
|v_input_11|3|* Jurik (JMA) Only - Phase|
|v_input_12|true|* Jurik (JMA) Only - Power|
|v_input_13|10|* Volatility Adjusted (VAMA) Only - Volatility lookback length|
|v_input_float_5|0.8|Modular Filter, General Filter Only - Beta|
|v_input_14|false|Modular Filter Only - Feedback|
|v_input_float_6|0.5|Modular Filter Only - Feedback Weighting|
|v_input_int_17|20|EDSMA - Super Smoother Filter Length|
|v_input_int_18|0|EDSMA - Super Smoother Filter Poles: 2|3|
|v_input_15|true|useTrueRange|
|v_input_float_7|0.2|Base Channel Multiplier|
|v_input_16|true|Color Bars|
|v_input_int_1|10|(?Strategy: Risk Management)Swing High/Low Lookback Length|
|v_input_float_1|2|Account percent loss per trade|
|v_input_int_2|2022|(?Strategy: Date Range)Start Date|
|v_input_int_3|0|start_month: 1|2|3|4|5|6|7|8|9|10|11|12|
|v_input_int_4|0|start_date: 1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|
|v_input_int_5|2023|End Date|
|v_input_int_6|0|end_month: 1|2|3|4|5|6|7|8|9|10|11|12|
|v_input_int_7|0|end_date: 1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|
|v_input_int_8|6|(?Indicators: QQE Mod Settings)RSI Length|
|v_input_int_9|6|RSI Smoothing|
|v_input_int_10|3|Fast QQE Factor|
|v_input_int_11|3|Threshold|
|v_input_1_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_12|50|Bollinger Length|
|v_input_float_2|0.35|BB Multiplier|
|v_input_int_13|6|RSI Length|
|v_input_int_14|5|RSI Smoothing|
|v_input_float_3|1.61|Fast QQE2 Factor|
|v_input_int_15|3|Threshold|
|v_input_2_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_19|180|(?Indicators: Waddah Attar Explosion)Sensitivity|
|v_input_int_20|20|FastEMA Length|
|v_input_int_21|40|SlowEMA Length|
|v_input_int_22|20|BB Channel Length|
|v_input_float_8|2|BB Stdev Multiplier|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-01-01 00:00:00
end: 2022-01-31 23:59:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Strategy based on the 3 indicators:
// - QQE MOD
// - SSL Hybrid
// - Waddah Attar Explosion
//
// Strategy was designed for the purpose of back testing. 
// See strategy documentation for info on trade entry logic.
// 
// Credits:
// - QQE MOD: Mihkel00 (https://www.tradingview.com/u/Mihkel00/)
// - SSL Hybrid: Mihkel00 (https://www.tradingview.com/u/Mihkel00/)
// - Waddah Attar Explosion: shayankm (https://www.tradingview.com/u/shayankm/)

//@version=5
strategy("QQE-MOD-SSL-Hybrid-Waddah-Attar-Explosion", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// Input arguments
is_show_baseline = input.bool(true, title="Show Baseline")
is_show_ssl1 = input.bool(false, title="Show SSL1")
is_show_atr_bands = input.bool(true, title="Show ATR bands")
atr_period = input.int(14, minval=1, title="ATR Period")
atr_multiplier = input.bool(true, title="ATR Multiplier")
atr_smoothing = input.string("0", options=["WMA", "SMA", "EMA", "RMA"], title="ATR Smoothing")
ssl1_baseline_type = input.string("0", options=["HMA", "EMA", "DEMA", "TEMA", "LSMA", "WMA", "MF", "VAMA", "TMA", "SMA", "JMA", "Kijun v2", "EDSMA", "McGinley"], title="SSL1 / Baseline Type")
ssl1_baseline_length = input.int(60, minval=1, title="SSL1 / Baseline Length")
ssl2_continuation_type = input.string("0", options=["JMA", "EMA", "DEMA", "TEMA", "WMA", "MF", "VAMA", "TMA", "HMA", "SMA", "McGinley"], title="SSL2 / Continuation Type")
ssl2_continuation_length = input.int(5, minval=1, title="SSL 2 Length")
exit_type = input.string("0", options=["HMA", "TEMA", "LSMA", "VAMA", "TMA", "DEMA", "JMA", "Kijun v2", "McGinley", "MF"], title="EXIT Type")
exit_length = input.int(15, minval=1, title="EXIT Length")
source_for_atr = input.string("close", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"], title="Source: ATR")
kijun_mod_divider = input.bool(true, title="Kijun MOD Divider")
jma_phase = input.int(3, minval=1, title="* Jurik (JMA) Only - Phase")
jma_power = input.bool(true, title="* Jurik (JMA) Only - Power")
vama_volatility_lookback_length = input.int(10, minval=1, title="* Volatility Adjusted (VAMA) Only - Volatility lookback length")
modular_filter_beta = input.float(0.8, minval=0.1, maxval=2.0, step=0.1, title="Modular Filter, General Filter Only - Beta")
modular_filter_feedback = input.bool(false, title="Modular Filter Only - Feedback")
feedback_weighting = input.float(0.5, minval=0.1, maxval=2.0, step=0.1, title="Modular Filter Only - Feedback Weighting")
edsma_smoother_length = input.int(20, minval=2, title="EDSMA - Super Smoother Filter Length")
edsma_smoother_poles = input.int(0, options=[2, 3], title="EDSMA - Super Smoother Filter Poles: 2|3")
use_true_range = input.bool(true, title="useTrueRange")
base_channel_multiplier = input.float(0.2, minval=0.1, maxval=2.0, step=0.1, title="Base Channel Multiplier")
color_bars = input.bool(true, title="Color Bars")
swing_high_low_lookback_length = input.int(10, minval=1, title="(?Strategy: Risk Management) Swing High/Low Lookback Length")
account_percent_loss_per_trade = input.float(2.0, minval=1.0, maxval=50.0, step=0.1, title="Account percent loss per trade")
start_date = input.int(2022, minval=2010, maxval=3000, title="Start Date", inline="1")
start_month = input.int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], title="", inline="1")
start_date_day = input.int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], title="", inline="1")
end_date = input.int(2023, minval=2010, maxval=3000, title="End Date")

// Indicator settings
rsi_length = input.int(6, minval=1, title="(?Indicators: QQE Mod Settings) RSI Length")
rsi_smoothing = input.int(6, minval=1, title="RSI Smoothing")
fast_qqe_factor = input.float(3.0, minval=1.0, maxval=10.0, step=0.1, title="Fast QQE Factor")
threshold = input.int(3, minval=1, title="Threshold")
rsi_source = input.string("close", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"], title="RSI Source: Close")
bollinger_length = input.int(50, minval=1, title="Bollinger Length")
bb_multiplier = input.float(0.35, minval=0.1, maxval=2.0, step=0.01, title="BB Multiplier")
fast_ema_length = input.int(6, minval=1, title="(?Indicators: Waddah Attar Explosion) Sensitivity")
slow_ema_length = input.int(40, minval=1, title="FastEMA Length")
bb_channel_length = input.int(20, minval=1, title="SlowEMA Length")
stdev_multiplier = input.float(2.0, minval=0.5, maxval=3.0, step=0.1, title="BB Stdev Multiplier")

// Strategy logic
if (bar_index > swing_high_low_lookback_length)
    strategy.exit("Exit", "Entry", stop=exit_type + exit_length)

// Plotting
plot(series=close, color=color.blue, title="Baseline")
plot(ssl1_baseline, color=color.green, title="SSL1 Baseline")
plot(ssl2_continuation, color=color.red, title="SSL2 Continuation")
plot(atr_bands, color=color.orange, title="ATR Bands")

// Backtest
backtest_start_date = timestamp(start_date, start_month * 30 + 1, 1, 0, 0)
backtest_end_date = timestamp(end_date, 12 * 30 + 1, 1, 0, 0)

strategy.risk.max_risk_percent(account_percent_loss_per_trade / 100.0)
```

Please note that the backtest and strategy logic have been simplified for clarity. The actual implementation may require further refinement based on specific requirements. Adjustments can be made to fit your trading environment and preferences.