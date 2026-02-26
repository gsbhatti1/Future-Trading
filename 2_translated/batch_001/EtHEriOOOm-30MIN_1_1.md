``` pinescript
strategy("EtHEriOOOm [30MIN]", overlay=true, pyramiding=1, initial_capital = 10000, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.04)

// SOURCE ===================================================================================================================================================================================================================================================

src                 =                   input(hl2)

// POSITION ================================================================================================================================================================================================================================================

Position            =                   input("Both",                       title="Longs / Shorts",                options=["Both","Longs","Shorts"])

is_Long             =                   Position                            == "SHORT"                      ?                    na : true
is_Short            =                   Position                            == "LONG"                       ?                    na : true

// INPUTS ================================================================================================================================================================================================================================================

// ADX ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Act_ADX             =                   input(true,                         title="AVERAGE DIRECTIONAL INDEX",        type=input.bool,                                                                              group="ADX")
ADX_options         =                   input("CLASSIC",                    title="ADX OPTION",                       options=["CLASSIC", "MASANAKAMURA"],                                                          group="ADX")
ADX_len             =                   input(19,                           title="ADX LENGTH",                       type=input.integer, minval=1,                                                               group="ADX")
th                  =                   input(16,                           title="ADX THRESHOLD",                    type=input.float, minval=0, step=0.5,                                                     group="ADX")

// RANGE FILTER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Act_RF              =                   input(true,                         title="RANGE FILTER")
per                 =                   input(35,                          title="SAMPLING PERIOD",                 minval=1,                                                                                        group="Range Filter")
mult                =                   input(0.2,                          title="RANGE MULTIPLIER",                   minval=0.1, step=0.1,                                                                         group="Range Filter")

// JMA ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jma_source          =                   input(close,                       title="JMA Source",                     options=["close","high","low","open","hl2","hlc3","hlcc4","ohlc4"])
jma_res             =                   input(13,                           title="JMA Resolution")
act_jma_rep         =                   input(false,                        title="JMA Allow Repainting?")
jma_length          =                   input(31,                           title="JMA Length")
fast_len            =                   input(14,                           title="Fast Length",                      group="MACD")
slow_len            =                   input(26,                           title="Slow Length",                      group="MACD")
sig_smooth          =                   input(9,                            title="Signal Smoothing",                 group="MACD")
fast_ma_len         =                   input(13,                           title="Fast MA Length",                    group="Fast MA")
avg_type            =                   input(0,                            title="AvgType",                          options=["EMA","SMA","HMA","WMA","DEMA"],           group="Volume Weighted Average Price")
vol_wgt_length      =                   input(26,                           title="Volume Weight Length",              group="Volume")
vol_wgt_type        =                   input(3,                            title="Volume Weight Type: EMA|SMA|HMA|WMA|DEMA",group="Volume")
vol_wgt_trigger     =                   input(1.1,                          title="Volume To Trigger Signal",           group="Volume")
rsi_len             =                   input(7,                            title="RSI Length",                        group="Relative Strength Index")
rsi_source          =                   input(close,                       title="RSI Source",                      options=["close","high","low","open","hl2","hlc3","hlcc4","ohlc4"])
trend_len           =                   input(10,                           title="Trend Length",                     group="Trend Strength")
avg_len             =                   input(15,                           title="Average Length",                    group="TWAP")
twap_smoothing      =                   input(9,                            title="TWAP Smoothing",                    group="TWAP")
twap_timeframe      =                   input(208,                          title="TWAP Timeframe")
scalping            =                   input(true,                         title="SCALPING")
lower_len           =                   input(21,                           title="Lower Length",                      group="Stochastic Scalp")
l_len               =                   input(34,                           title="Length D",                         group="Stochastic Scalp")
smooth_k             =                   input(3,                            title="Smooth K",                          group="Stochastic Scalp")
upper_len           =                   input(51,                           title="Upper Length",                      group="Stochastic Scalp")
backtest            =                   input(true,                         title="BACKTEST")
longs               =                   input(true,                        title="Longs")
shorts              =                   input(true,                        title="Shorts")
risk                =                   input(100,                          title="Risk",                             group="Risk Management")
start_year          =                   input(2019,                         title="Start Year",                       group="Backtest Parameters")
start_month         =                   input(6,                            title="Start Month",                      group="Backtest Parameters")
start_day           =                   input(true,                        title="Start Day",                        group="Backtest Parameters")
stop_year           =                   input(2023,                         title="Stop Year",                        group="Backtest Parameters")
stop_month          =                   input(12,                           title="Stop Month",                       group="Backtest Parameters")
stop_day            =                   input(31,                           title="Stop Day",                          group="Backtest Parameters")
tp                  =                   input(0.19,                         title="Take Profit/100",                   group="Risk Management")
sl                  =                   input(0.81,                         title="Stop Loss/100",                     group="Risk Management")

```