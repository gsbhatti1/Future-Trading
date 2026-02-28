> Name

Vitalik-Scalpe

> Author

a624587332



> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1_open|0|  Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_32|false|  Filter|
|v_input_33|7|  Pullback Lookback|
|v_input_34|true|  Use H.A Calculations|
|v_input_2|0|(?Average Directional Index)  Adx Type: CLASSIC|MASANAKAMURA|
|v_input_3|22|  Adx Lenght|
|v_input_4|13|  Adx Treshold|
|v_input_5|false|(?Support and Resistance)Show Support and Resistance levels|
|v_input_6|7|  Left|
|v_input_7|8|  Right|
|v_input_8|1.8|(?Volume)  Volume mult.|
|v_input_9|33|  Volume lenght|
|v_input_10|true|(?SAR)Show Parabolic SAR|
|v_input_11|0.7|  Sar Start|
|v_input_12|0.2|  Sar Int|
|v_input_13|0.38|  Sar Max|
|v_input_14|15|(?Range Filter)  Period|
|v_input_15|1.6|  mult.|
|v_input_16|15|(?MACD)  Fast Length|
|v_input_17|16|  Slow Length|
|v_input_18|21|  Signal Smoothing|
|v_input_19|50|(?Relative Strenght Indeks)  RSI Lenght|
|v_input_20_hlc3|0|  RSI Source: hlc3|high|low|open|hl2|close|hlcc4|ohlc4|
|v_input_21|false|(?Bolinger Bands)Show Bollinger Bands|
|v_input_22||  Timeframe 2|
|v_input_23_high|0|  Source 2: high|close|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_24|15|(?Relative Momentum Index)  Rmi Lenght|
|v_input_25|24|  Rmi Momentum|
|v_input_26|31|  Rmi overbought|
|v_input_27|63|  Rmi overbought|
|v_input_28|6|(?Scalping)  Scalping Lenght|
|v_input_29|10|  Fast EMA lenght|
|v_input_30|120|  Medium EMA lenght|
|v_input_31|500|  Slow EMA lenght|
|v_input_35|2|(?Average True Range)  PP period|
|v_input_36|4|  ATR Factor|
|v_input_37|true|  ATR Period|
|v_input_38|0.9|(?Target Point)  % TP Long|
|v_input_39|0.9|  % TP Short|
|v_input_40|3.5|(?Stop Loss)  % Stop loss|
|v_input_41|true|(?BACKTEST)Backtest|
|v_input_42|1997|start year|
|v_input_43|6|start month|
|v_input_44|true|start day|
|v_input_45|3333|stop year|
|v_input_46|12|stop month|
|v_input_47|31|stop day|


> Source (PineScript)


```pinescript
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © wielkieef

//@version=4

strategy("Vitalik Scalper", overlay=true, pyramiding=1, initial_capital = 10000, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.03)


//SOURCE =============================================================================================================================================================================================================================================================================================================

src                 = input(open, title="  Source")

// Indicators Inputs ========================================================================================================================================================================================================================================================================================================

//ADX-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ADX_options         = input("CLASSIC", title="  Adx Type", options=["CLASSIC", "MASANAKAMURA"], group="Average Directional Index")
ADX_len             = input(22, title="  Adx Lenght", type=input.integer, minval=1, group="Average Directional Index")
th                  = input(13, title="  Adx Treshold", type=input.integer, minval=0, group="Average Directional Index")

// Support and Resistance ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SHOW_S_R            = input(false, title="Show Support and Resistance levels", group="Support and Resistance")
left                = input(7, title="  Left", group="Support and Resistance")
right               = input(8, title="  Right", group="Support and Resistance")

// Volume ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

volume_f            = input(1.8, title="  Volume mult.", minval=0, step=0.1, group="Volume")
sma_length          = input(33, title="  Volume lenght", minval=1, group="Volume")

// SAR ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SAR_show            = input(true, title="Show Parabolic SAR")
sar_start           = input(0.7, title="  Sar Start")
sar_int             = input(0.2, title="  Sar Int")
sar_max             = input(0.38, title="  Sar Max")

// Range Filter ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

range_filter_period = input(15, title="(?Range Filter)  Period")
range_filter_mult   = input(1.6, title="  mult.")

// MACD --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

macd_fast_len       = input(15, title="(?MACD)  Fast Length")
macd_slow_len       = input(16, title="  Slow Length")
macd_signal_smooth  = input(21, title="  Signal Smoothing")

// RSI --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

rsi_lenght          = input(50, title="(?Relative Strenght Indeks)  RSI Lenght")
rsi_source_hlc3     = input(0, title="  RSI Source: hlc3", options=["hlc3", "high", "low", "open", "hl2", "close", "hlcc4", "ohlc4"])

// Bollinger Bands ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

show_bbands         = input(false, title="(?Bolinger Bands)Show Bollinger Bands")

// RMI --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

rmi_len             = input(15, title="(?Relative Momentum Index)  Rmi Lenght")
rmi_momentum        = input(24, title="  Rmi Momentum")
rmi_overbought      = input(31, title="  Rmi overbought")
rmi_overbought_val  = input(63, title="  Rmi overbought")

// Scalping ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

scalping_len        = input(6, title="(?Scalping)  Scalping Lenght")
fast_ema_len        = input(10, title="  Fast EMA lenght")
medium_ema_len      = input(120, title="  Medium EMA lenght")
slow_ema_len        = input(500, title="  Slow EMA lenght")

// ATR ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

atr_period          = input(true, title="  ATR Period")
atr_factor          = input(4, title="  ATR Factor")
pp_period           = input(2, title="(?Average True Range)  PP period")

// Target Point -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tp_long             = input(0.9, title="(?Target Point)  % TP Long")
tp_short            = input(0.9, title="  % TP Short")

// Stop Loss ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

stop_loss           = input(3.5, title="(?Stop Loss)  % Stop loss")

// Backtest ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

backtest            = input(true, title="(?BACKTEST)Backtest")
start_year          = input(1997, title="start year", type=input.integer)
start_month         = input(6, title="start month", type=input.integer)
start_day           = input(true, title="start day", type=input.bool)
stop_year           = input(3333, title="stop year", type=input.integer)
stop_month          = input(12, title="stop month", type=input.integer)
stop_day            = input(31, title="stop day", type=input.integer)
```