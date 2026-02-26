<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Eight-Days-Reversal-Momentum-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/dc004000dc448841b4.png)

[trans]
## Overview

This strategy primarily utilizes the reversal feature of prices after continuously closing above or below the 5-day simple moving average for 8 days to capture momentum effects in medium and short-term trading. It goes long when the closing price crosses above the 5-day line again after continuously closing below it for 8 days; it goes short when the closing price crosses below the 5-day line again after continuously closing above it for 8 days.

## Strategy Logic

1. Calculate the 5-day simple moving average (SMA).
2. Define an uptrend as the close being greater than or equal to the SMA, and a downtrend as the close being less than or equal to the SMA.
3. Confirm trend reversal conditions: trigger a buy signal when the closing price closes below the SMA for 8 consecutive days, then crosses above the SMA on the next day; trigger a sell signal when the closing price closes above the SMA for 8 consecutive days, then crosses below the SMA on the next day.
4. Entry: go long when the previous day's buy condition is triggered and the current trend is downtrend; go short when the previous day's sell condition is triggered and the current trend is uptrend.
5. Exit: close long position when the closing price crosses below the SMA; close short position when the closing price crosses above the SMA.

## Advantage Analysis

1. Utilizes the reversal feature of prices to capture momentum effects in medium and short-term trading.
2. High trading opportunities as continuous SMA breakout for 8 days happens frequently, increasing trade opportunities.
3. The 5-day SMA parameter performs well, avoiding too many false breakouts.
4. Risk is controllable with a clear stop loss point.

## Risk Analysis

1. Stop loss may be triggered frequently during market consolidation.
2. May miss the best entry point if the breakout days are set too long.
3. Hard to profit if there is a prolonged trend.

Can optimize SMA parameters, improve entry criteria to prevent false breakouts, and combine with trend indicators to strengthen the strategy.

## Optimization Directions

1. Parameter optimization: test different periods of the SMA to find better parameters.
2. Entry optimization: add volume indicators to avoid false breakouts; or judge bull/bear candles to avoid whipsaws.
3. Exit optimization: test fixed percentage trailing stop loss to give more room.
4. Risk control: set maximum daily stop loss times to limit losses.
5. Combine indicators: add RSI, MACD to determine trend to identify market conditions.

## Conclusion

The strategy captures the price movement from breakout to pullback by judging momentum and implements a trading logic of avoiding whipsaws and following trends. The keys are strict parameter settings and robust entry criteria to prevent noise; reasonable stop loss to limit losses. Combining with trend indicators can achieve better results. The strategy logic is simple and clean, making it worthwhile for further exploration and optimization.

||

## Overview

This strategy mainly utilizes the reversal feature of prices after continuously closing above or below the 5-day simple moving average (SMA) for 8 days to capture momentum effects in medium and short-term trading. It goes long when the closing price crosses above the 5-day line again after continuously closing below it for 8 days; it goes short when the closing price crosses below the 5-day line again after continuously closing above it for 8 days.

## Strategy Logic

1. Calculate the 5-day simple moving average (SMA).
2. Define an uptrend as the close being greater than or equal to the SMA, and a downtrend as the close being less than or equal to the SMA.
3. Confirm trend reversal conditions: trigger a buy signal when the closing price closes below the SMA for 8 consecutive days, then crosses above the SMA on the next day; trigger a sell signal when the closing price closes above the SMA for 8 consecutive days, then crosses below the SMA on the next day.
4. Entry: go long when the previous day's buy condition is triggered and the current trend is downtrend; go short when the previous day's sell condition is triggered and the current trend is uptrend.
5. Exit: close long position when the closing price crosses below the SMA; close short position when the closing price crosses above the SMA.

## Advantage Analysis

1. Captures momentum by utilizing the reversal features of prices, suitable for medium and short-term trading.
2. High trading opportunities as continuous SMA breakout for 8 days happens frequently, increasing trade opportunities.
3. The 5-day SMA parameter performs well, avoiding too many false breakouts.
4. Risk is controllable with a clear stop loss point.

## Risk Analysis

1. Stop loss may be triggered frequently during market consolidation.
2. May miss the best entry point if the breakout days are set too long.
3. Hard to profit if there is a prolonged trend.

Can optimize SMA parameters, improve entry criteria to prevent false breakouts, and combine with trend indicators to strengthen the strategy.

## Optimization Directions

1. Parameter optimization: test different periods of the SMA to find better parameters.
2. Entry optimization: add volume indicators to avoid false breakouts; or judge bull/bear candles to avoid whipsaws.
3. Exit optimization: test fixed percentage trailing stop loss to give more room.
4. Risk control: set maximum daily stop loss times to limit losses.
5. Combine indicators: add RSI, MACD to determine trend to identify market conditions.

## Conclusion

The strategy captures the price movement from breakout to pullback by judging momentum and implements a trading logic of avoiding whipsaws and following trends. The keys are strict parameter settings and robust entry criteria to prevent noise; reasonable stop loss to limit losses. Combining with trend indicators can achieve better results. The strategy logic is simple and clean, making it worthwhile for further exploration and optimization.

## Source Code (PineScript)

```pinescript
/*backtest
start: 2023-11-04 00:00:00
end: 2023-12-04 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Marcuscor

//@version=5

// Inspired by Linda Bradford Raschke: a strategy for trading momentum in futures markets

strategy("8D Run", initial_capital = 50000, commission_value = 0.0004) 

SMA = ta.sma(close, 5)

TrendUp = close >= SMA
TrendDown = close <= SMA


// logic to go long
TriggerBuy = ta.barssince(close < SMA) >= 8

Buy = TriggerBuy[1] and TrendDown 

strategy.entry("EL", strategy.long, when = Buy)
strategy.close(id = "EL", when = close > SMA)

// 1) color background when "run" begins and 2) change color when buy signal occurs
bgcolor(TriggerBuy ? color.green : na, transp = 90)
bgcolor(Buy ? color.green : na, transp = 70)


// logic to go short 
TriggerSell = ta.barssince(close > SMA) >= 8

Sell = TriggerSell[1] and TrendUp

strategy.entry("ES", strategy.short, when = Sell)
strategy.close(id = "ES", when = close < SMA)

// 1) color background when "run" begins and 2) change color when sell signal occurs
bgcolor(TriggerSell ? color.red : na, transp = 90)
bgcolor(Sell ? color.red : na, transp = 70) 
```

> Detail

https://www.fmz.com/strategy/434294

> Last Modified

2023-12-05 10:56:37