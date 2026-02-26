> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Take Profit pip|
|v_input_2|20|Stop Loss pip|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-29 00:00:00
end: 2023-10-29 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 12/02/2019
//    This is a three candlestick bullish reversal pattern consisting of a 
//    bullish harami pattern formed by the first 2 candlesticks then followed 
//    by up candlestick with a higher close than the prior candlestick.
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
/////////////////////////////////////////
study("Three Inside Up Reversal Strategy", shorttitle="3INSUPR", overlay=true)

// Inputs
takeProfitPips = input(20, title="Take Profit (pip)")
stopLossPips = input(20, title="Stop Loss (pip)")

// Functions
bullishHaramiCandle1 = close[1] < open[1]
bullishHaramiCandle2 = close[2] > open[2] and close[2] < open[1]
upCandle3 = close[3] > open[3] and close[3] > highest(high[0], 2)

// Pattern Detection
if (bullishHaramiCandle1 and bullishHaramiCandle2 and upCandle3)
    strategy.entry("Short", strategy.short, when=barssince(bullishHaramiCandle2) == 1)
    
    // Stop Loss and Take Profit Levels
    stopLossLevel = close[3] - stopLossPips * pointSize
    takeProfitLevel = close[3] + takeProfitPips * pointSize
    
    strategy.exit("Take Profit", "Short", limit=takeProfitLevel, stop=stopLossLevel)
```

This Pine Script implements the Three Inside Up Reversal Strategy as described. It detects the specific pattern and triggers a short position with predefined entry, stop loss, and take profit levels based on user inputs.