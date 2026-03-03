``` pinescript
/*backtest
start: 2022-11-06 00:00:00
end: 2023-11-12 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy('Dual Reversal Entry Strategy', overlay=true)
//Developer: Andrew Palladino
//Owner: Rob Booker
//Date Modified: 11/25/2018
//Updated to Pinescript V5 and transformed into a Strategy by: Powerscooter	11/25/2022

StrategyMode = input.bool(true, title='Strategy Mode')
fastLength = input.int(12, title='MACD Fast Period')
slowLength = input.int(26, title='MACD Slow Period')
signalLength = input.int(9, title='MACD Signal Period')
rsiKPeriod = input.int(70, title='%K Period', minval=1)
rsiDSmoothed = input.int(30, title='%D Smoothing Period', minval=1)
stochOverboughtLevel = input.int(70, title='Stochastic Overbought Level', minval=1)
stochOversoldLevel = input.int(30, title='Stochastic Oversold Level', minval=1)

[trans]


## Overview

The Dual Reversal Entry strategy generates entries by combining reversal signals from the MACD and Stochastic RSI indicators to accurately go long and short at trend reversal points. It belongs to the class of reversal trading strategies.

## Strategy Logic

The strategy consists of the following components:

1. Using the MACD indicator's crossover of the zero line to determine trend reversal.
2. Using the Stochastic RSI indicator to identify overbought and oversold conditions. Stochastic RSI combines RSI overbought/oversold principles, above 70 is overbought and below 30 is oversold.
3. When the MACD line crosses above zero (bullish reversal signal) and Stochastic RSI shows oversold, a buy signal is generated. When the MACD line crosses below zero (bearish reversal signal) and Stochastic RSI shows overbought, a sell signal is generated.
4. The strategy has both indicator plotting mode and execution mode. In indicator mode, reversal signals are marked with triangles. In strategy mode, long/short positions are opened on reversal signals.

Combining the MACD reversal signal with Stochastic RSI overbought/oversold levels improves the accuracy of entries. It provides good timing for entries at trend reversal points.

## Advantages

- Dual indicator filtering improves entry accuracy
The dual reversal filters ensure entries are taken only after trend reversal, reducing false signals and improving entry accuracy.
- Reversal trading works for choppy/ranging markets
As a reversal strategy, it excels in choppy bear market conditions with frequent ups and downs and allows winning trades at each minor swing reversal.
- Beginner friendly without trend bias
It directly trades all reversals without the need to determine the major trend, simple to use for beginners.
- Flexible indicator or strategy modes
The modes allow flexible usage for analysis or automated executions.

## Risks

- Higher risk of reversal trading 
Without considering major trend, reversal trading has higher risk in strong trending markets, with likely consecutive losses opening countertrend. Need to combine with trend strategies.
- Difficult multi-parameter optimization
The multiple parameters of dual indicators make optimization challenging. Inappropriate parameters may cause over-trading or insufficient signals. Requires extensive testing.
- Requires high-frequency trading account
The high-frequency strategy needs low-cost trading accounts to support, otherwise fees may offset profits.

## Enhancement Opportunities

- Optimize indicator parameters
Testing different parameter combinations to find the optimal settings for reliable signals. E.g., MACD periods, Stochastic lookback.
- Add trend filter 
Adding a trend indicator and taking reversal signals only in trend direction avoids counter-trend trades. E.g., using MA to determine long-term trend.
- Implement stop loss 
Adding stop loss by price or percentage to control risk on trades. Consider partial profit taking and adding to loser.
- Tighten entry conditions 
Additional entry filters like volume spike or crossing moving average to reduce false entries.

## Conclusion

The dual reversal entry strategy provides a novel and reliable approach to trade local reversals. It excels in choppy bear market conditions but has higher risks. Extensive optimization, trend filters, and risk controls are needed to profit consistently when live trading.
[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|StrategyMode|true|Strategy Mode|
|fastLength|12|MACD Fast Period|
|slowLength|26|MACD Slow Period|
|signalLength|9|MACD Signal Period|
|rsiKPeriod|70|%K Period|
|rsiDSmoothed|30|%D Smoothing Period|
|stochOverboughtLevel|70|Stochastic Overbought Level|
|stochOversoldLevel|30|Stochastic Oversold Level|

> Source (PineScript)

``` pinescript
//@version=5
strategy('Dual Reversal Entry Strategy', overlay=true)
StrategyMode = input.bool(true, title='Strategy Mode')
fastLength = input.int(12, title='MACD Fast Period')
slowLength = input.int(26, title='MACD Slow Period')
signalLength = input.int(9, title='MACD Signal Period')
rsiKPeriod = input.int(70, title='%K Period', minval=1)
rsiDSmoothed = input.int(30, title='%D Smoothing Period', minval=1)
stochOverboughtLevel = input.int(70, title='Stochastic Overbought Level', minval=1)
stochOversoldLevel = input.int(30, title='Stochastic Oversold Level', minval=1)

// Calculate MACD
[macdLine, signalLine, _] = macd(close, fastLength, slowLength, signalLength)

// Calculate Stochastic RSI
rsiVal = rsi(close, 14)
stochRSI = stoch(rsiVal, rsiVal, rsiVal, 5, 3, 0)

buySignal = (macdLine > 0) and (stochRSI < stochOversoldLevel)
sellSignal = (macdLine < 0) and (stochRSI > stochOverboughtLevel)

if (StrategyMode)
    strategy.entry('Long', strategy.long, when=buySignal)
    strategy.close('Long', when=sellSignal)
else
    plotshape(series=buySignal, title='Buy Signal', location=location.below, color=color.green, style=shape.triangleup, size=size.small)
    plotshape(series=sellSignal, title='Sell Signal', location=location.above, color=color.red, style=shape.triangledown, size=size.small)

// Additional logic can be added here
```