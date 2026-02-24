> Name

MACD Trend Following Intraday Strategy MACD-Trend-Following-Intraday-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fca9fc5800d445f52b.png)
[trans]

## Overview

The MACD Trend Following Intraday Strategy is a short-term trading strategy that combines moving averages, the MACD indicator, and the Williams Indicator. It uses different combinations of these three indicators to form entry and exit conditions for long and short positions, aiming to capture the trending characteristics of short-term price movements.

## Strategy Logic

The key trading logic of this strategy is based on several aspects:

1. Go long when price breaks above the Exponential Moving Average (EMA) line, and go short when it breaks below;
2. Go long when the MACD fast line is above the slow line, and go short when below;
3. Go long when William Indicator’s fast MA line is above the slow MA line, and vice versa;
4. Use the combinations of these 3 scenarios as entry conditions;
5. Exit on reversal signals.

By combining EMA for overall trend direction and MACD for short-term momentum, this strategy can capture price trend moves at decent entry points for profits. Williams Indicator further helps avoid false breakouts by gauging overbought/oversold levels.

## Advantages

This multi-indicator combo structure makes a typical short-term trend following strategy with main edges like:

1. Triple cross verification to reduce false signals;
2. EMA for main trend, MACD for short-term momentum;
3. Williams Indicator avoids chasing tops or bottom fishing during volatile moves;
4. Reversal combo ensures risk control aligns with exits.

## Risks

There are also major risks to note for this strategy:

1. The complex structure makes parameter tuning challenging;
2. Frequent short-term trades may lead to higher transaction costs;
3. Failure to detect true trend reversal points may result in losses.

The main mitigations are parameter optimization and stop loss to maximize profit combos and control max single trade loss.

## Enhancement Opportunities

Main aspects to enhance the strategy:

1. Test more parameter combinations for optimum set;
2. Add more data feeds like volume for entry validation;
3. Employ dynamic or trailing stop loss to strengthen risk control;
4. Incorporate machine learning for detecting true reversals.

## Conclusion

This MACD trend following intraday strategy effectively combines indicators for identifying short-term trends and managing risks. Further improvements on tuning parameters, setting stop loss levels, and incorporating more data feeds can lift strategy win rate and profitability. The concepts are worth researching for strategy advancement.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|50|Volume MA Period|
|v_input_5|12|Fast Length|
|v_input_6|26|Slow Length|
|v_input_int_7|9|Signal Smoothing|
|v_input_string_1|0|Oscillator MA Type: EMA|SMA|
|v_input_string_2|0|Signal Line MA Type: EMA|SMA|
|v_input_int_8|34|w_length|
|v_input_13|5|Smoothed %R Length|
|v_input_14|13|Slow EMA Length|
|v_input_1|2011|(?Trading window)Start Year|
|v_input_int_1|true|Start Month|
|v_input_int_2|true|Start Day|
|v_input_2|2050|Finish Year|
|v_input_int_3|12|Finish Month|
|v_input_int_4|31|Finish Day|
|v_input_float_1|true|(?Trading Options)Leverage (if applicable)|
|v_input_bool_1|false|Reinvest profit|
|v_input_float_2|20|Reinvest percentage|
|v_input_int_5|14|(?Daily ATR)ATR period|
|v_input_float_3|5|% ATR to use for SL / PT|
|v_input_float_4|20|(?VIX Volatility Index)VIX Threshold for entry|
|v_input_int_6|200|(?Moving Averages)EMA|
|v_input_7|#2962FF|(?Color Settings)MACD Line  |
|v_input_8|#FF6D00|Signal Line  |
|v_input_9|#26A69A|(?Histogram)Above   Grow|
|v_input_10|#B2DFDB|Fall|
|v_input_11|#FFCDD2|Below Grow|
|v_input_12|#FF5252|Fall|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-18 00:00:00
end: 2023-12-18 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © platsn

//@version=5
strategy("MACD Willy Strategy", overlay=true, pyramiding=1, initial_capital=10000) 

// ******************** Trade Period **************************************
startY = input(title='Start Year', defval=2011, group = "Trading window")
startM = input.int(title='Start Month', defval=1, minval=1, maxval=12, group = "Trading window")
startD = input.int(title='Start Day', defval=1, minval=1, maxval=31, group = "Trading window")
finishY = input(title='Finish Year', defval=2050, group = "Trading window")
finishM = input.int(title='Finish Month', defval=12, minval=1, maxval=12, group = "Trading window")
finishD = input.int(title='Finish Day', defval=31, minval=1, maxval=31, group = "Trading window")
timestart = timestamp(year=startY, month=startM, day=startD) // Start time for backtest

// Strategy main logic
// Add your strategy code here
```