``` pinescript
/*backtest
start: 2022-04-24 00:00:00
end: 2022-05-23 23:59:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
//

study(title = "Scalping Swing Trading Tool R1-4 by ChaoZhang", shorttitle = "SCALPSWING R1-4", overlay = true)

//
// Revision:        1
// Original Author: ChaoZhang
//
// Description:
//    This study project is a Scalping Swing trading Tool designed for a two pane TradingView chart layout: 
//    - the first pane set to 15min Time Frame; 
//    - the second pane set to 1min Time Frame (TF).
//    The tools incorporates the majority of the indicators needed to analyse and scalp Trends for Swings,
//    PullBacks, and reversals on 15min charts and 1min charts. The setup optionally utilizes Heikin Ashi
//    candle charts.
//
//    NOTE: A Pullback is synonymous to Retracement, generally a Pullback refers to a large Retracement of 100 pips
//    or more. In the context of this Tool and any comments related to it, a Pullback will be the same as a Retracement.
//
//    Incorporated within this tool are the following indicators:
//    1. The following EMAs: 
//       - Green = EMA89 (15min TF) = EMA75 (1min TF)
//       - Blue  = EMA200 (15min TF) = EMA180 (1min TF)
//       - Black = EMA633 (15min TF) = EMA540 (1min TF)
//    2. The 10EMA (default) High/Low+Close Price Action Channel (PAC), the PAC channel display is disabled by default.
//    3. Optionally display Fractals and optional Fractal levels
//    4. Optional HH, LH, LL, HL finder.
//    5. Coloured coded Bar high lighting based on the PAC:
//       - blue = bar closed above PAC
//       - red = bar closed below PAC
//       - gray = bar closed inside PAC
//       - lime line = EMA10 of bar close
//    6. Pivot points (disables Fractals automatically when selected) with optional labels.
//    7. EMA5-12 Channel is displayed by default.
//    8. EMA12-36 Ribbon is displayed by default
//    9. Optionally display EMA36 and PAC instead of EMA12-36 Ribbon.

Set up and hints:
I am unable to provide a full description here, as Pullback Trading incorporates a full trading methodology, there are numerous articles and books written on the subject.

Set to two pane TradingView chart, set first pane to 15Min and second to 1min.
Set the chart to Heikin Ashi Candles (optional).
I also add a "Sweetspot Gold2" indicator to the chart as well to help with support and resistance finding and shows where the important "00" lines are.
Use the EMA200 on the 15min pane as the anchor. So when prices above EMA200 we only trade long (buy) and when prices below the EMA200 we only trade short (sell).
On the 15min chart draw any obvious Vertical Trend Lines (VTL), use Pivots point as a guide.
On the 15min chart, what we’re looking for price to Pullback into the EMA5-12 Channel or EMA12-36 ribbon, we draw Trendlines utilizing the Pivot points or Fractals to guide your TL drawing.
On the 15min chart look for the trend to resume and break through the drawn TL. The bar color needs to change back to the trend direction color to confirm as a break.
Now this break can be traded as a 15min trade or now look to the 1min chart.
On the 1min chart draw any Pullback into any of the EMAs.
On the 1min chart, look for the trend to resume and break through the drawn TL. The bar color needs to change back to the trend direction color to confirm as a break.
Now this break can be traded as a 1min trade.
There is also an option to select Pristine (ie Ideal) filtered Fractals, which look like tents or V shape 5-candle patterns. These are actually used to calculate the Pivot points as well.
Other than the "SweetSpot Gold2" indicator, you should not need any other indicator to successfully trade trends for Pullbacks and reversals. If you really want another indicator use the AO (Awesome Oscillator) as it is momentum based.

**backtest**

![IMG](https://www.fmz.com/upload/asset/11a7ebca21140501d74.png)

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | true | Show Price Action Channel (PAC) |
| v_input_2 | true | Show colored Bars close relative on PAC |
| v_input_3 | 10 | High Low PAC Length |
| v_input_4 | false | Show PAC Swing Alerts |
| v_input_5 | false | Use Big Arrows for Swing Alerts |
| v_input_6 | true | Filter PAC Alerts with 200ema |
| v_input_7 | true | Show EMA12 Channel |
| v_input_8 | true | Show EMA36 Ribbon |
| v_input_9 | true | Show Pivots |
| v_input_10 | true | Show Pivot Labels |
| v_input_11 | false | Show HH, LH, LL, HL finder |
| v_input_12 | true | Show Fractals |
| v_input_13 | false | Show Fractal Levels |
| v_input_14 | false | Filter for Pristine (Ideal) Fractals |

> Source (PineScript)

``` pinescript
//@version=3
//

study(title = "Scalping Swing Trading Tool R1-4 by ChaoZhang", shorttitle = "SCALPSWING R1-4", overlay = true)

//
// Revision:        1
// Original Author: ChaoZhang
//
// Description:
//    This study project is a Scalping Swing trading Tool designed for a two pane TradingView chart layout: 
//    - the first pane set to 15min Time Frame; 
//    - the second pane set to 1min Time Frame (TF).
//    The tools incorporates the majority of the indicators needed to analyse and scalp Trends for Swings,
//    PullBacks, and reversals on 15min charts and 1min charts. The setup optionally utilizes Heikin Ashi
//    candle charts.
//
//    NOTE: A Pullback is synonymous to Retracement, generally a Pullback refers to a large Retracement of 100 pips
//    or more. In the context of this Tool and any comments related to it, a Pullback will be the same as a Retracement.
//
//    Incorporated within this tool are the following indicators:
//    1. The following EMAs: 
//       - Green = EMA89 (15min TF) = EMA75 (1min TF)
//       - Blue  = EMA200 (15min TF) = EMA180 (1min TF)
//       - Black = EMA633 (15min TF) = EMA540 (1min TF)
//    2. The 10EMA (default) High/Low+Close Price Action Channel (PAC), the PAC channel display is disabled by default.
//    3. Fractals
//    4. HH, LH, LL, HL finder to help with drawing Trend lines and mini Trend Lines.
//    5. Coloured coded Bar high lighting based on the PAC: 
//       - blue = bar closed above PAC
//       - red = bar closed below PAC
//       - gray = bar closed inside PAC
//       - lime line = EMA10 of bar close
//    6. Optionally display Pivot points (disables Fractals automatically when selected).
//    7. Display EMA5-12 Channel
//    8. Display EMA12-36 Ribbon
//    9. Optionally display EMA36 and PAC instead of EMA12-36 Ribbon.

Set up and hints:
I am unable to provide a full description here, as Pullback Trading incorporates a full trading methodology, there are numerous articles and books written on the subject.

Set to two pane TradingView chart, set first pane to 15Min and second to 1min.
Set the chart to Heikin Ashi Candles (optional).
I also add a "Sweetspot Gold2" indicator to the chart as well to help with support and resistance finding and shows where the important "00" lines are.
Use the EMA200 on the 15min pane as the anchor. So when prices above EMA200 we only trade long (buy) and when prices below the EMA200 we only trade short (sell).
On the 15min chart draw any obvious Vertical Trend Lines (VTL), use Pivots point as a guide.
On the 15min chart, what we’re looking for price to Pullback into the EMA5-12 Channel or EMA12-36 ribbon, we draw Trendlines utilizing the Pivot points or Fractals to guide your TL drawing.
On the 15min chart look for the trend to resume and break through the drawn TL. The bar color needs to change back to the trend direction color to confirm as a break.
Now this break can be traded as a 15min trade or now look to the 1min chart.
On the 1min chart draw any Pullback into any of the EMAs.
On the 1min chart, look for the trend to resume and break through the drawn TL. The bar color needs to change back to the trend direction color to confirm as a break.
Now this break can be traded as a 1min trade.
There is also an option to select Pristine (ie Ideal) filtered Fractals, which look like tents or V shape 5-candle patterns. These are actually used to calculate the Pivot points as well.
Other than the "SweetSpot Gold2" indicator, you should not need any other indicator to successfully trade trends for Pullbacks and reversals. If you really want another indicator use the AO (Awesome Oscillator) as it is momentum based.

**backtest**

![IMG](https://www.fmz.com/upload/asset/11a7ebca21140501d74.png)
``` ```markdown
# Scalping Swing Trading Tool R1-4

## Overview
This Pine Script tool, named "Scalping Swing Trading Tool R1-4," is designed for swing trading and scalping strategies. It utilizes a dual-timeframe approach with 15-minute and 1-minute charts to identify entry and exit points based on various technical indicators.

### Key Features:
- **Timeframes:** 
  - First pane: 15-minute chart
  - Second pane: 1-minute chart

- **Indicators:**
  - EMAs (Exponential Moving Averages):
    - Green EMA89 (15min) = EMA75 (1min)
    - Blue EMA200 (15min) = EMA180 (1min)
    - Black EMA633 (15min) = EMA540 (1min)

  - **Price Action Channel:** 
    - Default is disabled, but can be enabled.
  
  - Fractals and their levels.

  - HH, LH, LL, HL finder for drawing trend lines.

  - Colored bar high lighting based on the Price Action Channel:
    - Blue: Bar closed above channel
    - Red: Bar closed below channel
    - Gray: Bar closed inside channel
    - Lime Line: EMA10 of the bar

- **Pivots and Labels:** 
  - Can be displayed or disabled.
  
- **EMA Channels:**
  - Default is enabled for EMA5-12 Channel.
  - Default is enabled for EMA12-36 Ribbon.

  - Option to display EMA36 and Price Action Channel instead of the EMA12-36 Ribbon.

### Setup Instructions:
1. **Timeframe Configuration:**
   - Set first pane to 15-minute chart.
   - Set second pane to 1-minute chart.
  
2. **Candlestick Type:**
   - Optionally use Heikin Ashi Candles for more reliable price action insights.

3. **Additional Indicators:**
   - Add the "Sweetspot Gold2" indicator for support and resistance levels and important "00" lines.

4. **Trading Strategy:**
   - Use EMA200 as an anchor:
     - Long (Buy) when prices are above the 15-minute EMA200.
     - Short (Sell) when prices are below the 15-minute EMA200.
  
5. **Trend Identification:**
   - On the 15-minute chart, draw obvious vertical trend lines using pivot points as guides.
   - Look for price to pull back into the EMA5-12 Channel or EMA12-36 Ribbon.
   - Draw trendlines utilizing pivot points or fractals to identify breakouts.

### Backtesting:
The provided backtest results can be viewed by clicking on the link: ![Backtest](https://www.fmz.com/upload/asset/11a7ebca21140501d74.png).

### Strategy Arguments (Pine Script):

```pinescript
//@version=3
study("Scalping Swing Trading Tool R1-4", shorttitle="SCALPSWING R1-4", overlay=true)

// Default values
v_input_1 = input(true, title="Show Price Action Channel (PAC)")
v_input_2 = input(true, title="Show colored Bars close relative on PAC")
v_input_3 = input(10, title="High Low PAC Length")
v_input_4 = input(false, title="Show PAC Swing Alerts")
v_input_5 = input(false, title="Use Big Arrows for Swing Alerts")
v_input_6 = input(true, title="Filter PAC Alerts with 200ema")
v_input_7 = input(true, title="Show EMA12 Channel")
v_input_8 = input(true, title="Show EMA36 Ribbon")
v_input_9 = input(true, title="Show Pivots")
v_input_10 = input(true, title="Show Pivot Labels")
v_input_11 = input(false, title="Show HH, LH, LL, HL finder")
v_input_12 = input(true, title="Show Fractals")
v_input_13 = input(false, title="Show Fractal Levels")
v_input_14 = input(false, title="Filter for Pristine (Ideal) Fractals")

// Description
description = "This study is a Scalping Swing Trading Tool R1-4 designed with dual-timeframe analysis. Key features include EMAs, Price Action Channel, Fractals, and Pivot points."
title = description

```

### Conclusion:
The provided tool offers robust technical indicators to help traders identify potential entry and exit points in the market. The setup involves configuring multiple timeframes and indicators to enhance your trading strategy.
``` 

This markdown provides a detailed explanation of the tool, its features, setup instructions, and backtesting information. It also includes a sample Pine Script for reference. Feel free to use this as a template or modify it according to your needs!