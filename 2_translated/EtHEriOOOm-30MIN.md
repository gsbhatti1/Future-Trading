``` pinescript
strategy("EtHEriOOOm [30MIN]", overlay=true, pyramiding=1, initial_capital = 10000, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.04)

//SOURCE =============================================================================================================================================================================================================================================================================================================

src                 =                   input(hl2)

// POSITION ==========================================================================================================================================================================================================================================================================================================

Position            =                   input("Both",                       title="Longs / Shorts",                options=["Both","Longs","Shorts"])

is_Long             =                   Position                            == "SHORT"                      ?                    na : true
is_Short            =                   Position                            == "LONG"                       ?                    na : true

// INPUTS ============================================================================================================================================================================================================================================================================================================

//ADX --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Act_ADX             =                   input(true,                         title="AVERAGE DIRECTIONAL INDEX",        type=input.bool,                                                                              group="ADX")
ADX_options         =                   input("CLASSIC",                     title="ADX OPTION",                       options=["CLASSIC", "MASANAKAMURA"],                                                          group="ADX")
ADX_len             =                   input(19,                           title="ADX LENGTH",                       type=input.integer, minval=1,                                                               group="ADX")
th                  =                   input(16,                           title="ADX THRESHOLD",                    type=input.float, minval=0, step=0.5,                                                     group="ADX")

// Range Filter ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Act_RF              =                   input(true,                         title="RANGE FILTER")
per                 =                   input(35,                          title="SAMPLING PERIOD",                 minval=1,                                                                                        group="Range Filter")
mult                =                   input(0.2,                          title="RANGE MULTIPLIER",                   minval=0.1, step=0.1,                                                                         group="Range Filter")

//JMA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jma_source          =                   input(close,                       title="JMA Source",                      options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"],                     group="JMA")
jma_res             =                   input("15",                         title="JMA Resolution")
jma_repaint         =                   input(false,                       title="JMA Allow Repainting?")
jma_len             =                   input(31,                           title="JMA Length",                       type=input.integer, minval=1,                                                               group="JMA")
fast_length         =                   input(13,                          title="Fast Length",                      type=input.integer, minval=1,                                                               group="MACD")
slow_length         =                   input(19,                          title="Slow Length",                      type=input.integer, minval=1,                                                               group="MACD")
signal_smooth       =                   input(19,                          title="Signal Smoothing",                 type=input.integer, minval=1,                                                               group="MACD")
fast_ma_len         =                   input(61,                          title="Fast MA Length",                    type=input.integer, minval=1,                                                               group="Fast MA")
avg_type            =                   input(5,                           title="Avg Type",                          type=input.integer, minval=1,                                                               group="Volume Weight")
vol_weight_len     =                   input(61,                          title="Volume Weight Length",              type=input.integer, minval=1,                                                               group="Volume Weight")
vol_weight_type    =                   input("SMA",                        title="Volume Weight Type",                options=["EMA", "SMA", "HMA", "WMA", "DEMA"],                                                group="Volume Weight")
vol_to_trigger      =                   input(1.1,                         title="Volume To Trigger Signal",          type=input.float, minval=0.1, step=0.1,                                                      group="Volume Weight")
rsi_length          =                   input(50,                          title="RSI Length",                        type=input.integer, minval=1,                                                               group="RSI")
rsi_source          =                   input(close,                       title="RSI Source",                       options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"],                     group="RSI")
channel_length     =                   input(10,                          title="Channel Length",                    type=input.integer, minval=1,                                                               group="Trend Strength")
avg_length         =                   input(21,                          title="Average Length",                    type=input.integer, minval=1,                                                               group="TWAP")
twap_smoothing      =                   input(20,                          title="TWAP Smoothing",                    type=input.integer, minval=1,                                                               group="TWAP")
twap_timeframe     =                   input(0,                           title="TWAP Timeframe")
scalping           =                   input(true,                         title="Scalping",                          options=["true", "false"],                                                                     group="Stoch Scalps")
lower_length       =                   input(42,                          title="Lower Length",                      type=input.integer, minval=1,                                                               group="Stoch Scalps")
length_D           =                   input(12,                          title="Length D",                          type=input.integer, minval=1,                                                               group="Stoch Scalps")
smooth_K           =                   input(72,                          title="Smooth K",                          type=input.integer, minval=1,                                                               group="Stoch Scalps")
upper_length       =                   input(67,                          title="Upper Length",                      type=input.integer, minval=1,                                                               group="Stoch Scalps")
backtest           =                   input(true,                         title="Backtest",                          options=["true", "false"],                                                                     group="BACKTEST")
longs              =                   input(true,                         title="Longs",                             options=["true", "false"])
shorts             =                   input(true,                         title="Shorts",                            options=["true", "false"])
risk               =                   input(100,                          title="Risk",                              type=input.integer, minval=1,                                                               group="BACKTEST")
start_year         =                   input(2019,                         title="Start Year",                        type=input.integer, minval=1970, maxval=3000)
start_month        =                   input(6,                           title="Start Month",                       type=input.integer, minval=1, maxval=12)
start_day          =                   input(true,                         title="Start Day",                          options=["true", "false"])
stop_year          =                   input(3000,                         title="Stop Year",                         type=input.integer, minval=1970, maxval=3000)
stop_month         =                   input(12,                          title="Stop Month",                        type=input.integer, minval=1, maxval=12)
stop_day           =                   input(31,                          title="Stop Day",                          type=input.integer, minval=1, maxval=31)
tp_percentage      =                   input(0.019,                        title="TP/100")
sl_percentage      =                   input(0.081,                        title="SL/100")

// END OF INPUTS ==============================================================================================================================================================================================================================================
```

This translation keeps the original code blocks and formatting intact while translating the human-readable text into English.