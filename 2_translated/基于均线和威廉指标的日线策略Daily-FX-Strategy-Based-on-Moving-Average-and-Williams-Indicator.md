> Name

Daily-FX-Strategy-Based-on-Moving-Average-and-Williams-Indicator

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/a72434a65ae0f75d5b.png)
 [trans]
## Overview

This strategy combines the use of moving averages, ATR indicators, and Williams indicators for daily foreign exchange (FX) trading. It first judges the overall trend and potential reversal points through the moving average, then uses the Williams indicator to further confirm trading signals. The ATR indicator is utilized to calculate stop loss and position sizing.

## Strategy Logic

1. Use a 20-day moving average (baseline) to determine the overall trend. A price crossing from below to above is a buy signal, while a crossing from above to below is a sell signal.
2. The Williams indicator is used to confirm price reversals. An indicator crossing above -35 is a buy confirmation, while crossing below -70 is a sell confirmation.
3. The ATR indicator calculates the average price range over the last 2 days. The value multiplied by a factor is set as the stop loss distance.
4. Position sizing is based on 50% of account equity. Trade size is calculated based on the stop loss distance and risk percentage.
5. After entering a long position, the stop loss is set at the price low minus the stop loss distance. The take profit is set at the entry price plus 100 points. Exiting logic further confirms exit signals.
6. Similarly, for a short position, the stop loss and take profit are set the same way. Exiting logic is also used to confirm exits.

## Advantage Analysis

1. Combining trend judgment by moving averages and confirmation by indicators can effectively avoid losses from false breakouts.
2. Dynamic stop loss by ATR can set a reasonable stop distance based on market volatility.
3. Risk control and dynamic position sizing can maximize control over single trade loss.
4. Exiting logic combined with moving averages can help further confirm good exit timing and avoid premature profit taking.

## Risk Analysis

1. Moving average signals may have a higher probability of being wrong, needing further confirmation from indicators.
2. Indicators themselves can also generate wrong signals, unable to completely avoid losses.
3. This strategy fits trending pairs better, may have poorer results for range-bound pairs.
4. Improper risk control ratio settings can also impact strategy profitability.

Methods like adjusting the moving average period, combining more indicators, manual intervention, etc., can help further optimize and improve the strategy.

## Conclusion

This strategy combines trend judgment and indicator filtering for daily trading. It also leverages dynamic stop loss, risk control, and other means to control trading risk. There is much room for optimization by parameter tuning and method combination to further improve strategy performance.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Use Heikin Ashi Candles in Algo Calculations|
|v_input_2|true|Is this a 2 digit pair? (JPY, XAU, XPD...|
|v_input_3|50|Risk %|
|v_input_4|30|Equity Protection %|
|v_input_5|true|Average True Range multiplier|
|v_input_6|100|Target TP in Points|
|v_input_7|true|From Day|
|v_input_8|true|From Month|
|v_input_9|2000|From Year|
|v_input_10|31|To Day|
|v_input_11|12|To Month|
|v_input_12|2021|To Year|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-29 00:00:00
end: 2024-01-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("GBPJPY DAILY FX", initial_capital = 1000, currency="USD", overlay=true)

UseHAcandles    = input(false, title="Use Heikin Ashi Candles in Algo Calculations")
//
// === /INPUTS ===

// === BASE FUNCTIONS ===

haClose = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, close) : close
haOpen  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, open) : open
haHigh  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, high) : high
haLow   = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, low) : low

//INDICATOR---------------------------------------------------------------------    
    //Average True Range (1. RISK)
atr_period = 2
atr = atr(atr_period)

    //Ichimoku Cloud - Kijun Sen (2. BASELINE)
ks_period = 20
kijun_sen = (highest(haHigh,ks_period) + lowest(haLow,ks_period))/2
base_long = haOpen < kijun_sen and haClose > kijun_sen
base_short = haOpen > kijun_sen and haClose < kijun_sen

    //Williams Percent Range (3. Confirmation#1)
use_wpr = true
wpr_len = 4
wpr = -100*(highest(haHigh,wpr_len) - haClose)/(highest(haHigh,wpr_len) - lowest(haLow,wpr_len))
wpr_up = -35
wpr_low = -70
conf1_long = wpr >= wpr_up
conf1_short = wpr <= wpr_low
if(use_wpr == false)
    conf1_long := true
    conf1_short := true
//TRADE LOGIC-------------------------------------------------------------------
    //Long Entry
    //if -> WPR crosses below -39 AND MACD line is less than signal line
l_en = base_long and conf1_long
    //Long Exit
    //if -> WPR crosses above -14
l_ex = haClose < kijun_sen
    //Short Entry
    //