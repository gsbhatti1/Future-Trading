``` pinescript
// © Milleman
//@version=4
strategy("MilleMachine", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=10000, commission_type=strategy.commission.percent, commission_value=0.06)


// Additional settings
Mode = input(title="Mode", defval="LongShort", options=["LongShort", "OnlyLong", "OnlyShort","Indicator Mode"])
QuickSwitch = true                          //input(true, title="Quickswitch")
UseTC = true                                //input(true, title="Use Trendchange?")

// Risk management settings
Risk = input(1.0, title="% Risk", minval=0)/100
RRR = 2                                     //input(2,title="Risk Reward Ratio", step=0.1, minval=0, maxval=20)
SL_Mode = false                             //input(false, title="ON = Fixed SL / OFF = Dynamic SL (ATR)")
SL_Fix = 3                                  //input(3,title="StopLoss %", step=0.25, minval=0)/100
ATR = atr(14)                               //input(14,title="Period ATR")
Mul = input(2, title="ATR Multiplier", step=0.1)
xATR = ATR * Mul
SL = SL_Mode ? SL_Fix : (1 - close / (close + xATR))

// INDICATORS  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Ind(type, src, len) =>
    float result = na
    if type == "McGinley"
        result := na(result[1]) ? ema(src, len) : result[1] + (src - result[1]) / (len * pow(src / result[1], 4))
    if type == "HMA"
        result := wma(2*wma(src, len/2)-wma(src, len), round(sqrt(len)))
    if type == "EHMA"
        result := ema(2*ema(src, len/2)-ema(src, len), round(sqrt(len)))
    if type == "THMA"
        lend = len/2
        result := wma(wma(src, lend/3)*3-wma(src, lend/2)-wma(src,lend), lend)
    if type == "SMA" // Simple
        result := sma(src, len)
    if type == "EMA" // Exponential
        result := ema(src, len)
    if type == "DEMA" // Double Exponential
        e = ema(src, len)
        result := 2 * e - ema(e, len)
    if type == "TEMA" // Triple Exponential
        e = ema(src, len)
        result := 3 * (e - ema(e, len)) + ema(ema(e, len), len)
    if type == "WMA" // Weighted
        result := wma(src, len)
    if type == "VWMA" // Volume Weighted
        result := vwma(src, len) 
    if type == "SMMA" // Smoothed
        w = wma(src, len)
        result := (w[1] * (len - 1) + src) / len
    if type == "RMA"
        result := rma(src, len)
    if type == "LSMA" // Least Squares
        result := linreg(src, len, 0)
    if type == "ALMA" // Arnaud Legoux
        result := alma(src, len, 0.85, 6)
    if type == "Kijun" // Kijun-sen
        kijun = avg(lowest(len), highest(len))
        result := kijun
    if type == "WWSA" // Welles Wilder Smoothed Moving Average
        result := nz(rma(src, len))

// Trading Logic
if (Mode == "LongShort")
    longCondition = Ind(v_input_9, v_input_10, v_input_11) > 0 and close > ref(Ind(v_input_9, v_input_10, v_input_11), -1)
    shortCondition = Ind(v_input_9, v_input_10, v_input_11) < 0 and close < ref(Ind(v_input_9, v_input_10, v_input_11), -1)

if (Mode == "OnlyLong")
    longCondition = Ind(v_input_9, v_input_10, v_input_11) > 0 and close > ref(Ind(v_input_9, v_input_10, v_input_11), -1)
    shortCondition := na

if (Mode == "OnlyShort")
    longCondition := na
    shortCondition = Ind(v_input_9, v_input_10, v_input_11) < 0 and close < ref(Ind(v_input_9, v_input_10, v_input_11), -1)

if (Mode == "Indicator Mode")
    longCondition := na
    shortCondition := na

if QuickSwitch
    baselineType = input("Baseline Type", title="Baseline Type", options=["McGinley", "HMA", "EHMA", "THMA", "SMA", "EMA", "DEMA", "TEMA", "WMA", "VWMA", "SMMA", "RMA", "LSMA", "ALMA", "Kijun", "WWSA"])
    blSource = input("Baseline Source", title="BL source", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"])
    baselineLength = input(50, title="BL length")
    
    // Calculate Baseline
    baselineresult = Ind(baselineType, blSource, baselineLength)
    confirmIndicator = input("Confirmation Indicator", title="C1 Entry indicator", options=["SMA", "HMA", "EHMA", "THMA", "McGinley", "EMA", "DEMA", "TEMA", "WMA", "VWMA", "SMMA", "RMA", "LSMA", "ALMA", "Kijun", "WWSA"])
    confirmSource = input("Confirmation Source", title="Source", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"])
    confirmLength = input(5, title="Length")
    
    // Calculate Confirmation Indicator
    confirmresult = Ind(confirmIndicator, confirmSource, confirmLength)
    
    if (baselineType != "")
        longCondition = baselineresult > 0 and close > ref(baselineresult, -1) and confirmresult > 0
        shortCondition = baselineresult < 0 and close < ref(baselineresult, -1) and confirmresult < 0

if (QuickSwitch)
    if v_input_12
        entryIndicatorType = input("ENTRY indicator", title="EI Entry indicator", options=["HMA", "McGinley", "EHMA", "THMA", "SMA", "EMA", "DEMA", "TEMA", "WMA", "VWMA", "SMMA", "RMA", "LSMA", "ALMA", "Kijun", "WWSA"])
        entrySource = input("Entry Source", title="Source", options=["close", "high", "low", "open", "hl2", "hlc3", "hlcc4", "ohlc4"])
        entryLength = input(46, title="Length")
        
        // Calculate ENTRY Indicator
        entryresult = Ind(entryIndicatorType, entrySource, entryLength)
    
    if (entryIndicatorType != "")
        longCondition = entryresult > 0 and close > ref(entryresult, -1)
        shortCondition = entryresult < 0 and close < ref(entryresult, -1)

if QuickSwitch
    if v_input_16
        trailingStopType = input("Trailing Stop Type", title="TS Trailing Stop Type", options=["EMA", "HMA", "EHMA", "THMA", "SMA", "McGinley", "DEMA", "TEMA", "WMA", "VWMA", "SMMA", "RMA", "LSMA", "ALMA", "Kijun", "WWSA"])
        smoothTrailLongEma = input(5, title="Smoothing Trail Long EMA")
        smoothTrailShortEma = input(2, title="Smoothing Trail Short EMA")
        
    if (trailingStopType != "")
        strategy.entry("long", strategy.long, when=longCondition)
        trail_price = low
        strategy.exit("exit_long", from_entry="long", limit=high + ATR * smoothTrailLongEma, stop=low - ATR * smoothTrailShortEma)

    if (QuickSwitch and v_input_16) or (v_input_4)
        // Handle Quickswitch logic here
```

Note: The original script has been translated to English while maintaining the structure and code blocks. However, some parts of the Pine Script might need further optimization or correction depending on the specific requirements and context in which it is intended to be used.