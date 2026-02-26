> Name

Order-Block-Finder

> Author

ChaoZhang

> Strategy Description

After finding a huge amount of use from TV user's wugamlo script Order Block Finder (Experimental), I decided to make some much needed upgrades! Added support for plotting the last X number of Order Blocks and am currently working on a multi-timeframe version.

If you'd like to contribute to the MTF analysis portion, that would benefit tons of other scripts and open the possibility to more "MTF Panel" style indicators.

Please visit the original script page (link at top) to review how the indicator is used in trading.


**backtest**

 ![IMG](https://www.fmz.com/upload/asset/bb14ca43e91e986c7f.png) 

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Hover over ( ! ) for documentation|
|v_input_2|0|Color Scheme: LIGHT|DARK|
|v_input_3|7|Relevant Periods to identify OB|
|v_input_4|false|Min. Percent move for valid OB|
|v_input_5|2|Number of Bullish Channels to show|
|v_input_6|2|Number of Bearish Channels to show|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-04-22 00:00:00
end: 2022-05-21 23:59:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
study("Order Block Finder", overlay = true)       
tip1 = "Indicator to help identify institutional Order Blocks (OB). OBs often signal the beginning of a strong move. There is a high probability that OB price levels will be revisited in the future and are interesting levels to place limit orders. A Bullish Order block is the last down candle before a sequence of up candles. A Bearish Order Block is the last up candle before a sequence of down candles."
tip2 = "!Experimental!\nFind Order Blocks from different timeframes. Channel prices are accurate, but arrow positions may not be. Most useful when selecting a timeframe higher than the chart."
tip3 = "Required number of subsequent candles in the same direction to identify an Order Block"
tip4 = "Measured from the potential OB close to the close of the first candle in the sequence"
dummy = input(true,"Hover over ( ! ) for documentation", tooltip = tip1)
colors    = input("LIGHT","Color Scheme", options=["DARK", "LIGHT"])
//res = input("","Order Block Timeframe",input.resolution,tooltip=tip2)
periods   = input(7,     "Relevant Periods to identify OB",tooltip=tip3)    // Required number of subsequent candles in the same direction to identify an Order Block
threshold = input(0.0,   "Min. Percent move for valid OB", step = 0.1, tooltip=tip4)      // Minimum required percentage move (from potential OB close to the close of the first candle in the sequence to identify an Order Block)
bull_channels =  input(2, "Number of Bullish Channels to show")             // Number of channels
bear_channels = input(2, "Number of Bearish Channels to show")              // Number of channels


//Data Curation
res = ""
[copen,chigh,clow,cclose] = security(syminfo.tickerid,res,[open,high,low,close],barmerge.gaps_on, barmerge.lookahead_off)


ob_period = periods + 1                                                     // Identify location of relevant Order Block candle
absmove   = ((abs(cclose[ob_period] - cclose[1]))/cclose[ob_period]) * 100     // Calculate absolute percentage move from potential OB to the last candle in the sequence
relmove   = absmove >= threshold                                            // Identify "Relevant move" by comparing the absolute move to the threshold

// Color Scheme
bullcolor = colors == "DARK"? color.white : color.green
bearcolor = colors == "DARK"? color.blue : color.red

// Bullish Order Block Identification
bullishOB = cclose[ob_period] < copen[ob_period]                              // Determine potential Bullish OB candle (red candle)

int upcandles  = 0
for i = 1 to periods
    upcandles := upcandles + (cclose[i] > copen[i]? 1 : 0)                    // Determine color of subsequent candles (must all be green to identify a valid Bullish OB)

OB_bull      = bullishOB and (upcandles == (periods)) and relmove           // Identification logic (red OB candle & subsequent green candles)
OB_bull_chigh = OB_bull? chigh[ob_period] : na                                // Determine OB upper limit (Open or High depending on input)
OB_bull_clow  = OB_bull? clow[ob_period]  : na                                // Determine OB lower limit (Low)
OB_bull_avg  = (OB_bull_chigh + OB_bull_clow)/2                               // Determine OB middle line


// Bearish Order Block Identification
bearishOB = cclose[ob_period] > copen[ob_period]                              // Determine potential Bearish OB candle (green candle)

int downcandles  = 0
for i = 1 to periods
    downcandles := downcandles + (cclose[i] < copen[i]? 1 : 0)                // Determine color of subsequent candles (must all be red to identify a valid Bearish OB)

OB_bear      = bearishOB and (downcandles == (periods)) and relmove         // Identification logic (green OB candle & subsequent red candles)
OB_bear_chigh = OB_bear? chigh[ob_period] : na                                // Determine OB upper limit (High)
OB_bear_clow  = OB_bear? clow[ob_period] : na                                 // Determine OB lower limit (Open or Low depending on input)
OB_bear_avg  = (OB_bear_clow + OB_bear_chigh)/2                               // Determine OB middle line


// Plotting
plotshape(OB_bull, title="Bullish OB", style = shape.triangleup,   color = bullcolor, textcolor = bullcolor, size = size.tiny, location = location.belowbar, offset = -ob_period, text = "Bull")     // Bullish OB Indicator
bull1 = plot(OB_bull_chigh, title="Bullish OB High", style = plot.style_linebr, color = bullcolor, offset = -ob_period, linewidth = 2)                                               // Bullish OB Upper Limit
bull2 = plot(OB_bull_clow,  title="Bullish OB Low",  style = plot.style_linebr, color = bullcolor, offset = -ob_period, linewidth = 2)                                               // Bullish OB Lower Limit
fill(bull1, bull2, color=bullcolor)                                         // Fill between the upper and lower limits for Bullish OB

```

Please note that the original code has some minor issues with variable names like `colo` at the end of the last line. It should be corrected to `color`.