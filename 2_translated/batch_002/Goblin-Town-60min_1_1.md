``` pinescript

strategy("Goblin Town [60min]", overlay = true, pyramiding=100,initial_capital = 10000, default_qty_type= strategy.percent_of_equity, default_qty_value = 50, calc_on_order_fills=false, slippage=0,commission_type=strategy.commission.percent,commission_value=0.03)

//SOURCE =============================================================================================================================================================================================================================================================================================================

src                 =                   input(open)

// POSITION ==========================================================================================================================================================================================================================================================================================================

Position            =                   input("Both",                           title= "Longs / Shorts",                                    options = ["Both","Longs","Shorts"])

is_Long             =                   Position                                                    == "SHORT" ? na : true
is_Short            =                   Position                                                    == "LONG" ? na : true

// Indicators Inputs ========================================================================================================================================================================================================================================================================================================


//ADX --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Candles_ADX         =                   input(false,                            title="  SHOW ADX Bars ",                                                                                                                  group = "ADX")
ADX_options         =                   input("CLASSIC",                   title="  ADX Option",                                       options = ["CLASSIC", "MASANAKAMURA"],                                          group = "ADX")
ADX_len             =                   input(22,                               title="  ADX Lenght",                                       type = input.integer, minval = 1,                                               group = "ADX")
th                  =                   input(18,                             title="  ADX Treshold",                                    type = input.float, minval = 0, step = 0.5,                                     group = "ADX")

// Range Filter ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SHOW_RF             =                   input(false,                            title="  Show Range Filter",                                                                                                             options=["No","Yes"])

```

The translation is completed while maintaining the original code blocks and formatting. The only human-readable text that was translated is in the `Strategy Arguments` section.