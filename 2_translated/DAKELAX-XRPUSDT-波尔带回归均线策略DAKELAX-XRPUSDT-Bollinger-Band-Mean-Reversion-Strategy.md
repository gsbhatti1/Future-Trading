<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

## Overview

DAKELAX-XRPUSDT is a trading bot strategy for XRPUSDT on Binance. It is a simple reverse to mean strategy using Bollinger Bands, and performs well in backtest on H1 timeframe from May to Aug 2019, as well as running live.

## Strategy Logic

The strategy first calculates the 20-period SMA (Simple Moving Average) and upper/lower Bollinger Bands. The upper band is calculated as SMA + 1.5 times the standard deviation, and the lower band as SMA - 2.2 times the standard deviation. It then calculates the contraction rate of the bands. Bands are filled black if the contraction ratio is greater than 1.3, yellow if it is less than 0.1, otherwise red.

When the closing price is below the lower band, a long position is opened with 20 coins. When the closing price exceeds the upper band, all positions are closed.

The strategy also calculates the 7-period EMA (Exponential Moving Average) fast line and the 18-period EMA slow line. A crossover of the fast line above the slow line generates a buy signal, while a crossover below the slow line generates a sell signal.

## Advantage Analysis

- The use of Bollinger Bands and their contraction rate intuitively identifies trends and volatility.
- Combining with EMA crossovers strengthens signals.
- Backtest results are good, and it performs relatively stably in live trading.

## Risk Analysis

- There is a high probability of failure when the bands expand after contraction.
- Fixed amount buying without position sizing risks overtrading.
- Too many crossovers in ranging markets can lead to losses.
- Only considers daily factors; misses larger timeframe trends.

Consider dynamic position sizing or setting stop losses to control risk. Optimize crossover strategies to avoid being trapped in ranging markets. Integrate higher timeframe trend indicators to identify broader market movements.

## Optimization Directions

- Adjust the buy amount based on the band width, buying less when contracted and more when expanded.
- Consider accumulating positions during contraction if no signals are triggered yet.
- Add longer timeframe trend INDICATORs to determine overall direction; pause strategy when unclear trends exist.
- Incorporate stop losses to control risk, setting them near recent low points of the bands.
- Optimize crossover parameters such as EMA periods to avoid getting trapped.

## Summary

DAKELAX-XRPUSDT is a trading bot strategy using Bollinger Band contraction with EMA crossovers. It is intuitive and has good backtest results but contains some risks. These can be reduced through position sizing, pausing the strategy, adding stop losses, and optimizing crossover logic. Overall, it provides a clear example of a Bollinger Band strategy, but requires specific optimization for stable live profits.

||


## Overview

DAKELAX-XRPUSDT is a trading bot strategy for XRPUSDT on Binance. It uses the Bollinger Bands combined with EMA crossovers and performs well in backtests during the H1 timeframe from May to August 2019, as well as during live operations.

## Strategy Logic

First, calculate the 20-period SMA (Simple Moving Average) and upper/lower Bollinger Bands. The upper band is calculated as SMA + 1.5 times the standard deviation, while the lower band is SMA - 2.2 times the standard deviation. Then, determine the contraction rate of the bands: if the contraction ratio exceeds 1.3, fill with black; if it is less than 0.1, fill with yellow; otherwise, fill with red.

When the closing price falls below the lower band, a long position is opened using 20 coins. When the closing price exceeds the upper band, all positions are closed.

The strategy also calculates the 7-period EMA (Exponential Moving Average) fast line and the 18-period EMA slow line. A crossover of the fast line above the slow line generates a buy signal, while a crossover below the slow line generates a sell signal.

## Advantage Analysis

- The use of Bollinger Bands and their contraction rate provides an intuitive way to identify trends and volatility.
- Combining with EMA crossovers strengthens signals.
- Backtest results are good, and it performs relatively stably in live trading.

## Risk Analysis

- There is a high probability of failure when the bands expand after contraction.
- Fixed amount buying without position sizing risks overtrading.
- Too many crossovers in ranging markets can lead to losses.
- Only considers daily factors; misses larger timeframe trends.

Consider dynamic position sizing or setting stop losses to control risk. Optimize crossover strategies to avoid being trapped in ranging markets. Integrate higher timeframe trend indicators to identify broader market movements.

## Optimization Directions

- Adjust the buy amount based on band width, buying less when contracted and more when expanded.
- Consider accumulating positions during contraction if no signals are triggered yet.
- Add longer timeframe trend INDICATORs to determine overall direction; pause strategy when unclear trends exist.
- Incorporate stop losses to control risk, setting them near recent low points of the bands.
- Optimize crossover parameters such as EMA periods to avoid getting trapped.

## Summary

DAKELAX-XRPUSDT is a trading bot strategy using Bollinger Bands and EMAs. It is intuitive with good backtest results but contains some risks. These can be reduced through position sizing, pausing the strategy, adding stop losses, and optimizing crossover logic. Overall, it provides a clear example of a Bollinger Band strategy, but requires specific optimization for stable live profits.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|buyAmount|
|v_input_2|20|len2|
|v_input_3_close|0|src2: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|


## Source (PineScript)

```pinescript
/*backtest
start: 2022-10-26 00:00:00
end: 2023-11-01 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
// study(title="Tradebotler DAKELAX Binance:XRPUSDT Study-strategy", overlay=true)
strategy(title="Tradebotler DAKELAX Binance:XRPUSDT Strategy", overlay=true)

buyAmount = input(20, minval=1)

// SMA20
len2 = input(20, minval=1)
src2 = input(close)
out2 = sma(src2, len2)

// BB contraction value (medium tight)
contraction_value = 1.3
// BB contraction value (very tight)
contraction_value2 = 0.1

// 2xSTDEV BB calculation
dev = stdev(src2, len2)
upper_BB = out2 + 1.5*dev
lower_BB = out2 - 2.2*dev
x1 = plot(upper_BB, color=blue, linewidth = 2)
x2 = plot(lower_BB, color=blue, linewidth = 2)

contraction = (upper_BB-lower_BB)/out2

// fills the BBands according to the contraction value (threshold)

// Calculate values
fastMA  = ema(close, 7)
slowMA  = ema(close, 18)

// Determine alert setups
crossUp   = crossover(fastMA, slowMA)
crossDown = crossunder(fastMA, slowMA)

buySignal   = (crossUp or crossUp[1]) and (low > slowMA)
shortSignal = (crossDown or crossDown[1]) and (high < slowMA)

// Highlight alerts on the chart
bgColour =
     (buySignal and barstate.isrealtime) ? green :
     (shortSignal and barstate.isrealtime) ? red :
     na

signalBuy = (buySignal ) ? true : false
signalSell = (shortSignal ) ? true : false

test = true

test := not test[1]

closesBelowLowerBB = close < lower_BB
closesAboveUpperBB = close > upper_BB

tmptext = "blah"

// Plot values
plot(series=fastMA, color=teal)
plot(series=slowMA, color=orange)

plot(out2, color=black, linewidth = 1)
fill(x1, x2, color = contraction > contraction_value ? black : contraction < contraction_value2 ? yellow: red)

isInRed = contraction < contraction_value and contraction >= contraction_value2
isInYellow = contraction < contraction_value and contraction < contraction_value2

if ( closesBelowLowerBB )
    strategy.order('Buy', strategy.long, buyAmount)

if ( closesAboveUpperBB )
    strategy.close_all()
```

## Detail

https://www.fmz.com/strategy/4308