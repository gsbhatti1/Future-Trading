> Name

Scalping-PullBack-Tool-R1

> Author

ChaoZhang

> Strategy Description

This study project is a Scalping Pullback trading Tool that incorporates the majority of the indicators needed to analyze and scalp trends for pullbacks and reversals on 1min, 5min or 15min charts. The setup uses Heikin Ashi candle charts. Incorporated within this tool are the following indicators:
1. Major industry (Banks) recognized important EMAs in an EMA Ribbon:
   - Green = EMA89
   - Blue = EMA200
   - Black = EMA633
2. The 36EMA (default) High/Low+Close Price Action Channel (PAC).
3. Fractals
4. HH, LH, LL, HL finder to help with drawing trend lines and mini trend lines.
5. Colored-coded bar highlighting based on the PAC:
   - Blue = bar closed above PAC
   - Red = bar closed below PAC
   - Gray = bar closed inside PAC
6. Red line = EMA36 of bar close

Setup and hints:
Set the chart to Heikin Ashi Candles.
Add "Sweetspot Gold10" indicator to the chart as well to help with support and resistance finding and shows where the important "00" and "0" lines are.
When price is above the PAC (blue bars), we are only looking to buy as price comes back to the PAC.
When price is below the PAC (red bars), we are only looking to sell when price comes back to the PAC.
What we’re looking for when price comes back into the PAC, we draw mini trend lines using the Fractals and HH/LL points to guide your TL drawing.
Now look for the trend to pull back and break the drawn TL. That's when we place the scalp trade.
So we are looking for continuation signals in terms of a strong, momentum-driven pullbacks (normally short term 10-20 pips) of the EMA36.
The other EMAs are there to check for other pullbacks when EMA36 is broken.
Other than the SweetSpot Gold10 indicator, you should not need any other indicator to scalp the pullbacks.

**Backtest**
![IMG](https://www.fmz.com/upload/asset/108b0415e329fb1a830.png)

> Strategy Arguments

| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_1 | 34 | High/Low PAC channel Length |
| v_input_2 | 89 | Fast EMA length |
| v_input_3 | 200 | Medium EMA length |
| v_input_4 | 600 | Slow EMA length |
| v_input_5 | true | Show Fast EMA |
| v_input_6 | true | Show Medium EMA |
| v_input_7 | false | Show Slow EMA |
| v_input_8 | false | Show HH/LL |
| v_input_9 | true | Show Fractals |
| v_input_10 | false | Show Ideal Fractals Only |
| v_input_11 | true | Show colored bars around PAC |
| v_input_12 | true | Show TrendDirection/TrendDirection Alert Arrows |
| v_input_13 | 3 | Pullback Lookback for PAC Cross Check |
| v_input_14 | false | Show Alert Arrows Only on Closed Candles |
| v_input_15 | true | Show TrendBGcolor |
| v_input_16 | true | Use Heikin Ashi Candles in Algo Calculations |

> Source (PineScript)

```pinescript
//@version=4
study(title="Scalping PullBack Tool R1.1 by ChaoZhang", shorttitle="SCALPTOOL R1.1", overlay=true)

// Revision:        1.1
// Original Author: ChaoZhang

// Description:
//    This study project is a Scalping Pullback trading Tool that incorporates the majority of the indicators needed to analyze and scalp trends for pullbacks and reversals intended for lower time frame charts up to 15min, but it should work just as well on higher time frame charts for longer term trades.
//
//    This Tool can be used with Heikin Ashi (HA) candle charts or normal candle charts. HA candles will show a cleaner/smoother looking candle trend but not show true prices.
//
//    Incorporated within this tool are the following indicators:
//    1. Trader selectable important EMAs in an EMA style Ribbon: 
//       - Green = fast EMA (default=89)
//       - Blue  = medium EMA (default=200) 
//       - Black = slow EMA (default=600)
//    2. The PAC EMA (default=34) High/Low+Close creates the Price Action Channel (PAC).
//    3. Fractals
//    4. HH, LH, LL, HL finder may help with drawing trend lines and mini trend lines.
//    5. Colored coded Bar high lighting based on the PAC: 
//       - blue = bar closed above PAC
//       - red  = bar closed below PAC
//       - gray = bar closed inside PAC
//       - red line = PAC EMA (34) of bar close
//    6. Colored chart Background to indicate trend direction 
//       (NOTE: slow EMA(600) is not used in this Algo):
//       - green  = Trend direction is up when PAC and fast EMA(89) are above medium EMA(200).
//       - red    = Trend direction is down when PAC and fast EMA(89) are below medium EMA(200).
//       - yellow = Trend direction is in transition.
//    7. Pullback is defined as Price starts outside the PAC and then pulls back into the PAC closing the opposite side of the PAC center line, then a recovery arrow can occur.
//    8. Colored Alert Arrows:
//       - maroon down arrow  = Pullback recovery Sell alert
//       - green up arrow     = Pullback recovery Buy alert
//    9. Option to force Heikin Ashi candles in Algo calculations.

// Setup and hints:

//  - I also add "Sweetspot Gold10" indicator to the chart as well to help with support and resistance finding and shows where the important "00" and "0" lines are.
//  - When price is above the PAC (blue bars) we are only looking to buy as price comes back to the PAC
//    When price is below the PAC (red bars), we are only looking to sell when price comes back to the PAC
//  - What we’re looking for when price comes back into the PAC, we draw mini trend lines using the Fractals and HH/LL points to guide your TL drawing.
//  - Now look for the trend to pull back and break the drawn mini TL. That's where we can place the scalp trade.
//  - So we are looking for continuation signals in terms of a strong, momentum-driven pullbacks (normally short term 10-20 pips) of the EMA36.
//  - The other EMAs are there to check for other pullbacks when PAC EMA(34) is broken.
//  - Other than the "SweetSpot Gold10" indicator, you should not need any other indicator to scalp for pullbacks.

```