> Name

TrendScalp-FractalBox-3EMA

> Author

ChaoZhang

> Strategy Description

There are many indicators with William’s Fractal and Alligator. As many use EMA's, it may be useful to define a 3-EMA ribbon and combine Fractal Levels/Box (filling the background between top and bottom fractals) for trend scalping. I searched for this kind of indicator in the community – some show fractals, some just levels, some with alligator etc., but couldn't find the one needed. Hence thought of this indicator which may be of interest to other users too.

Key Points:
- An EMA ribbon is created using 3 EMAs: 35/70/105. Users can change these as per their preference. This is used for trend identification – 
  1. Bullish bias if Price > EMA1 > EMA2 > EMA3.
  2. Bearish bias if Price < EMA1 < EMA2 < EMA3.
- The background is marked during the crossing of EMA1 and EMA2 to alert a possible trend change.
- 5-bar fractals are used to mark the Fractal levels, and the background between top and bottom fractals is filled to create a Fractal Box.
- Fractal levels are marked only when the fractal formation is complete. Given an offset, this is lagging.

How to Use:
- The sloping EMA ribbon is used for identifying the trend.
- Trend strength EMA is enabled. An angle of 30 degrees and above is considered strong.
- Fractal box breakouts or breakdowns are used to trigger trades with fractal high/low for entry/stop loss.
  - Waiting for price contraction towards the EMA ribbon, resulting in smaller boxes, is key to initiating a trade.
  - Avoid larger boxes as stop losses will be large and price may move within.
  - To draw the vertical lines of FractalBox, change fractal level0 style to step-line.
- This indicator combined with cycle high/low (overbought/oversold) indicators such as CCI/Stochastic/RSI etc. can make it a good trend scalping setup while trading in the direction of momentum in higher timeframe.
- This setup could be used for any timeframes. Do your back-testing before using it in live market.

This indicator was achieved by combining some fractal ideas from "Fractal and Alligator Alerts by JustUncleL".

**Disclaimer:**
This indicator has been created for educational reference only and does not constitute investment advice. This indicator should not be relied upon as a substitute for extensive independent market research before making your actual trading decisions. Market data or any other content is subject to change at any time without notice. Liability for any loss or damage, including without limitation any loss of profit, which may arise directly or indirectly from use of this indicator, lies with the user using it.

**Backtest**

![IMG](https://www.fmz.com/upload/asset/190db5ecaaed28b368d.png)

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|true|Show EMA Ribbon|
|v_input_int_1|35|Fast EMA|
|v_input_int_2|70|Medium EMA|
|v_input_int_3|105|Slow EMA|
|v_input_int_4|20|Trend Strength EMA|
|v_input_1|true|Show Fractal Levels and Box|
|v_input_int_5|true|Fractal Line Width|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-04-22 00:00:00
end: 2022-05-21 23:59:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5

indicator('[VDB]TrendScalp-FractalBox-3EMA', shorttitle='[VDB]TS-FB-3EMA', overlay=true, max_lines_count=500)

// By: ©vireshdb/vdb/vdb007
//
//Description:
//          There are many indicators with William’s Fractal and Alligator. As many use EMA's it may be useful to define an EMA ribbon 
//          and combining Fractal levels/box (filling the background between top and bottom fractals) for trend scalping. I searched for this kind of indicator in the community – some show fractals, 
//          some just levels, some with alligator etc., but couldn't find the one needed. Hence thought of this indicator which may be of interest to other users too.
//Key Points:
//          An EMA ribbon is created using 3 EMAs: 35/70/105. Users can change these as per their preference. This is used for trend identification – 
//              1. Bullish bias if Price > EMA1 > EMA2 > EMA3.
//              2. Bearish bias if Price < EMA1 < EMA2 < EMA3.
//          The background is marked during the crossing of EMA1 and EMA2 to alert a possible trend change.
//          5-bar fractals are used to mark the Fractal levels, and backgrounds between top and bottom fractals are filled to create the Fractal Box.
//          Fractal levels are marked with offset 2 only when the fractal formation is complete and hence are lagging.
//How to Use:
//          The sloping EMA ribbon is used for identifying the trend.
//          Trend strength EMA is enabled. An angle of 30 degrees and above is considered strong.
//          Fractal box breakouts or breakdowns are used to trigger trades with fractal high/low for entry/stop loss.
//              - Waiting for price contraction towards the EMA ribbon, resulting in smaller boxes, is key to initiating a trade. 
//              - Avoid bigger boxes as stop losses will be big and price may move within.
//              - To draw the vertical lines of FractalBox, change fractal level0 style to stepline.
//          This indicator –
//              - Combined with cycle/ banded indicators such as CCI/Stochastic/RSI etc can make it a good trend scalping setup
//              - While trading in the direction of momentum in higher timeframe.
// Reference: This indicator was achieved by combining some fractal ideas from "Fractal Framer by brobear"
//
// Copyright 2022 vireshdb
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// The GNU General Public License can be found here
// <http://www.gnu.org/licenses/>.
// 
// Start of code **************************************************
```