> Name

VWMA-and-ATR-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/155d0eace762da9195d.png)
[trans]


## Overview

This strategy uses the VWMA indicator to determine trend direction and sets stop loss with ATR to follow trends. It is suitable for markets with obvious trends.

## Strategy Logic

1. Use the VWMA indicator to determine the trend direction. Go long when price is above VWMA, go short when price is below VWMA.
2. Add an RSI oscillator filter to avoid false breakouts. Only take long signals when RSI is above 30.
3. Use ATR to calculate the stop loss line. The ATR length is set to be the same as the VWMA length with a multiplier of 3.5. Stop loss lines update in real time.
4. The ATR multiplier controls how tight or loose the stop loss line is. Larger multipliers result in less frequent updates, which are better for following trends.
5. Position size is calculated based on account equity and stop loss percentage.
6. Exit long positions when price breaks below the stop loss line.

## Advantages

1. Using VWMA to determine trend direction can persistently catch trend opportunities.
2. The RSI filter helps avoid false breakout signals.
3. ATR trailing stop follows trends, avoiding being stopped out by reversals.
4. Position sizing based on account equity and stop loss percentage supports risk management.

## Risks

1. Potential losses at trend turning points. Reduce position size to limit single trade losses.
2. Improper ATR parameter settings can lead to overly sensitive or insensitive stop loss lines. Test parameters to find the best setting.
3. Fast trend reversals may cause stop loss updates to be too late, increasing potential losses.
4. In low-volatility environments, reduce position size and increase stop loss update frequency.

## Optimization

1. Test different VWMA parameter combinations to identify the optimal signal-generating parameters.
2. Test other RSI settings like overbought/oversold levels.
3. Test ATR multipliers to find a balance between drawdown and tracking ability.
4. Add filters from other indicators such as MACD or KD to improve signal quality.
5. Optimize position sizing and stop loss percentages based on market volatility.

## Summary

This strategy has a trend-following bias and is effective at capturing obvious price trends. It offers advantages in trend determination, signal filtering, and trailing stop management but also faces risks during trend reversals. Fine-tuning parameters and position sizing can lead to better performance.

|||

## Overview

This strategy uses VWMA to determine the trend direction and sets a stop loss with ATR to follow trends. It is suitable for markets with clear trends.

## Strategy Logic

1. Use VWMA to determine the trend direction. Go long when price is above VWMA, go short when price is below VWMA.
2. Add an RSI oscillator filter to avoid false breakouts. Only take long signals when RSI is above 30.
3. Use ATR to calculate the stop loss line. The ATR length is set to be the same as the VWMA length with a multiplier of 3.5. Stop loss lines update in real time.
4. The ATR multiplier controls how tight or loose the stop loss line is. Larger multipliers result in less frequent updates, which are better for following trends.
5. Position size is calculated based on account equity and stop loss percentage.
6. Exit long positions when price breaks below the stop loss line.

## Advantages

1. Using VWMA to determine trend direction can persistently catch trend opportunities.
2. The RSI filter helps avoid false breakout signals.
3. ATR trailing stop follows trends, avoiding being stopped out by reversals.
4. Position sizing based on account equity and stop loss percentage supports risk management.

## Risks

1. Potential losses at trend turning points. Reduce position size to limit single trade losses.
2. Improper ATR parameter settings can lead to overly sensitive or insensitive stop loss lines. Test parameters to find the best setting.
3. Fast trend reversals may cause stop loss updates to be too late, increasing potential losses.
4. In low-volatility environments, reduce position size and increase stop loss update frequency.

## Optimization

1. Test different VWMA parameter combinations to identify the optimal signal-generating parameters.
2. Test other RSI settings like overbought/oversold levels.
3. Test ATR multipliers to find a balance between drawdown and tracking ability.
4. Add filters from other indicators such as MACD or KD to improve signal quality.
5. Optimize position sizing and stop loss percentages based on market volatility.

## Summary

This strategy has a trend-following bias and is effective at capturing obvious price trends. It offers advantages in trend determination, signal filtering, and trailing stop management but also faces risks during trend reversals. Fine-tuning parameters and position sizing can lead to better performance.

|||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|33|VWMA Length|
|v_input_2|33|ATR length|
|v_input_3|3.5|ATR Multiplier|
|v_input_4|14|RSI of VWMA Length|
|v_input_5|10|Risk % of capital|
|v_input_6|5|Stop Loss|


## Source (PineScript)

```pinescript
/*backtest
start: 2023-10-07 00:00:00
end: 2023-10-13 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © mohanee

//@version=4
strategy(title="VWMA_withATRstops_strategy V2", overlay=true, pyramiding=1, default_qty_type=strategy.percent_of_equity, default_qty_value=20, initial_capital=10000, currency=currency.USD)  //default_qty_value=10, default_qty_type=strategy.fixed,

float xATRTrailingStop = na
int pos = na

vwmalength = input(33, title="VWMA Length", minval=1, maxval=365)
nATRPeriod = input(33, title="ATR length", minval=1, maxval=365)
nATRMultip = input(3.5, title="ATR Multiplier")

rsiofVwmaLength = input(14, title="RSI of VWMA Length")

riskCapital = input(title="Risk % of capital", defval=10, minval=1)
stopLoss = input(5, title="Stop Loss", minval=1)

vwmaVal = vwma(close, vwmalength)

plot(vwmaVal, color=color.orange, linewidth=2,  title="VWMA")

rsiofVwmaVal = rsi(vwmaVal, rsiofVwmaLength)

xATR = atr(nATRPeriod)
nLoss = nATRMultip * xATR

xATRTrailingStop := iff(close > nz(xATRTrailingStop[1], 0) and close[1] > nz(xATRTrailingStop[1], 0), max(nz(xATRTrailingStop[1]), close - nLoss),
                      iff(close < nz(xATRTrailingStop[1], 0) and close[1] < nz(xATRTrailingStop[1], 0), min(nz(xATRTrailingStop[1]), close + nLoss),
                      iff(close > nz(xATRTrailingStop[1], 0), close - nLoss, close + nLoss)))

pos := iff(close[1] < nz(xATRTrailingStop[1], 0) and close > nz(xATRTrailingStop[1], 0), 1,
           iff(close[1] > nz(xATRTrailingStop[1], 0) and close < nz(xATRTrailingStop[1], 0), -1, nz(pos[1], 0)))

color1 = pos == -1 ? color.red : pos == 1 ? color.green : color.blue

// plot(xATRTrailingStop, color=color1, title="ATR Trailing Stop")

// Entry
// Determine how many units can be purchased based on risk management and stop loss
qty1 = (strategy.equity * riskCapital / 100) / (close * stopLoss)
```