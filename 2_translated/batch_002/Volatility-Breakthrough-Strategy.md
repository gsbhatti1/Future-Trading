> Name

Volatility Breakthrough Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/ee9d0469967007f329.png)
[trans]

## Overview

The Volatility Breakthrough Strategy is a trading approach that identifies buy and sell opportunities when prices break through key support or resistance levels during volatile periods. This strategy integrates multiple technical indicators to recognize critical trading points.

## Strategy Principle

This strategy primarily relies on Bollinger Bands Middle Line, 48-day Simple Moving Average (SMA), MACD, and ADX four technical indicators. The specific logic is:

1. Consider trading opportunities when closing price crosses above or below the 48-day SMA;
2. When closing price breaks through the Bollinger Bands Middle Line, it serves as an entry signal;
3. MACD greater than or less than zero serves as an auxiliary indicator to determine trend direction;  
4. ADX greater than 25 to filter out non-trending markets.

When all four conditions are met, a long or short position is taken.

## Advantages of the Strategy

This strategy integrates both trend and volatility indicators, offering several advantages:

1. The 48-day SMA filters out excessive trading frequency, locking in medium-to-long-term trends;
2. Bollinger Bands Middle Line breakout captures key support/resistance breakouts with strong stop-loss functionality;
3. MACD helps identify the direction of major trends to avoid counter-trend trades;
4. ADX filters non-trending markets and increases the strategy’s win rate.

Overall, this strategy optimizes trading frequency, identifies critical points, determines trend direction, and filters out irrelevant moves, resulting in a relatively high win rate.

## Risks of the Strategy

The main risks associated with this strategy include:

1. In volatile markets, Bollinger Bands Middle Line may trigger too many trading opportunities, leading to excessive trading;
2. ADX indicators can have errors when determining trends and non-trending periods; 
3. Significant drawdown risk exists, suitable for investors who can bear a certain level of risk.

## Optimization Directions

This strategy can be further optimized in the following aspects:

1. Add ATR indicator to set stop loss points, reducing per trade stop loss;
2. Optimize Bollinger Bands parameters to lower middle line triggering frequency; 
3. Introduce trading volume or trend strength indicators to assess trend strength and avoid weak reversals.

## Summary

In summary, the Volatility Breakthrough Strategy is relatively mature as a whole, effectively capturing key trading points in volatile markets. It combines trend and volatility indicators to balance risk and return. Further optimization could yield more stable excess returns.

||

## Overview

The Volatility Breakthrough Strategy is a strategy that makes buy and sell operations when prices break through key support or resistance levels during volatile periods. This strategy integrates multiple technical indicators to identify critical trading opportunities.

## Strategy Principle

This strategy primarily relies on Bollinger Bands Middle Line, 48-day Simple Moving Average (SMA), MACD, and ADX four technical indicators. The specific logic is:

1. Consider trading opportunities when closing price crosses above or below the 48-day SMA;
2. When closing price breaks through the Bollinger Bands Middle Line, it serves as an entry signal;
3. MACD greater than or less than zero serves as an auxiliary indicator to determine trend direction;  
4. ADX greater than 25 to filter out non-trending markets.

When all four conditions are met, a long or short position is taken.

## Advantages of the Strategy

This strategy integrates both trend and volatility indicators, offering several advantages:

1. The 48-day SMA filters out excessive trading frequency, locking in medium-to-long-term trends;
2. Bollinger Bands Middle Line breakout captures key support/resistance breakouts with strong stop-loss functionality;
3. MACD helps identify the direction of major trends to avoid counter-trend trades;
4. ADX filters non-trending markets and increases the strategy’s win rate.

Overall, this strategy optimizes trading frequency, identifies critical points, determines trend direction, and filters out irrelevant moves, resulting in a relatively high win rate.

## Risks of the Strategy

The main risks associated with this strategy include:

1. In volatile markets, Bollinger Bands Middle Line may trigger too many trading opportunities, leading to excessive trading;
2. ADX indicators can have errors when determining trends and non-trending periods; 
3. Significant drawdown risk exists, suitable for investors who can bear a certain level of risk.

## Optimization Directions

This strategy can be further optimized in the following aspects:

1. Add ATR indicator to set stop loss points, reducing per trade stop loss;
2. Optimize Bollinger Bands parameters to lower middle line triggering frequency; 
3. Introduce trading volume or trend strength indicators to assess trend strength and avoid weak reversals.

## Summary

In summary, the Volatility Breakthrough Strategy is relatively mature as a whole, effectively capturing key trading points in volatile markets. It combines trend and volatility indicators to balance risk and return. Further optimization could yield more stable excess returns.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|12|fastLength|
|v_input_3|26|slowlength|
|v_input_4|9|MACDLength|
|v_input_5|20|length|
|v_input_6|2|mult|
|v_input_7|25|ADX Threshold|
|v_input_8|14|ADX Smoothing|
|v_input_9|14|DI Length|
|v_input_10|false|Take Profit Points|
|v_input_11|false|Stop Loss Points|
|v_input_12|false|Trailing Stop Loss Points|
|v_input_13|false|Trailing Stop Loss Offset Points|
|v_input_14|false|Custom Backtesting Dates|
|v_input_15|2020|Backtest Start Year|
|v_input_16|true|Backtest Start Month|
|v_input_17|true|Backtest Start Day|
|v_input_18|false|Backtest Start Hour|
|v_input_19|2020|Backtest Stop Year|
|v_input_20|12|Backtest Stop Month|
|v_input_21|31|Backtest Stop Day|
|v_input_22|23|Backtest Stop Hour|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-11 00:00:00
end: 2023-12-12 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © 03.freeman
// Volatility Traders Minds Strategy (VTM Strategy)
// I found this startegy on internet, with a video explaingin how it works.
// Conditions for entry:
// 1 - Candles must to be above or bellow the 48 MA (Yellow line)
// 2 - Candles must to break the middle of bollinger bands
// 3 - Macd must to be above or bellow zero level;
// 4 - ADX must to be above 25 level
//@version=4
strategy("Volatility Traders Minds Strategy (VTM Strategy)", shorttitle="VTM", overlay=true)
source = input(close)
// MA
ma48 = sma(source, 48)
// MACD
fastLength = input(12)
slowlength = input(26)
MACDLength = input(9)

MACD = ema(source, fastLength) - ema(source, slowlength)
aMACD = ema(MACD, MACDLength)
delta = MACD - aMACD

// BB
length = input(20, minval=1)
mult = input(2.0, minval=0.001, maxval=50)

basis = sma(source, length)
dev = mult * stdev(source, length)

upper = basis + dev
lower = basis - dev

// ADX
adxThreshold = input(title="ADX Threshold", type=input.integer, defval=25, minval=1)
adxlen = input(14, title="ADX Smoothing")
dilen = input(14, title="DI Length")
dirmov(len) =>
    up = change(high)
    down = -change(low)
    plusDM = na(up) ? na : (up > down and up > 0 ? up : 0)
    minusDM = na(down) ? na :
```