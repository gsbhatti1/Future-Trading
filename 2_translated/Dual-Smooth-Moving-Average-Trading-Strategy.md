> Name

Dual-Smooth-Moving-Average-Trading-Strategy

> Author

ChaoZhang

> Strategy Description


## Overview

This strategy utilizes a dual smooth moving average system as the primary trading signal, combined with the TDFI volume validation indicator for trade signal filtering. It leverages the advantages of smooth moving averages to reduce incorrect trades in non-trending markets.

## Strategy Logic

The strategy employs two sets of smooth moving averages with different parameter configurations as the primary trading signals. First, an 8-period fast smooth moving average is used as the initial confirmation, and then a slightly slower 16-period smooth moving average acts as the second confirmation. When the fast moving average gives a buy signal, if the slower moving average also signals in the same direction within the last 1-2 bars, a long position is opened; when the fast moving average gives a sell signal, if the slower moving average also signals in the same direction within the last 1-2 bars, a short position is opened. Exits are triggered when the second confirmation moving average reverses direction. Additionally, the TDFI volume indicator is used to detect trading volume energy behind price bars for filtering misleading signals. Trades are only taken when volume aligns with expectations.

## Advantages

- Smooth MAs effectively track trends and avoid market noise, catching mid- to long-term trends.
- The dual smooth MA setup enhances signal reliability, avoiding incorrect trades in non-trending markets.
- Volume indicator introduction filters misleading low-volume signals, avoiding unnecessary losses.
- High parameter optimization space allows adjustment for different products and timeframes, making it highly adaptable.

## Risks

- Smooth MAs can be slow to identify trend reversals, potentially leading to some losses.
- Dual smooth MAs may still generate concurrent wrong signals in non-trending markets.
- Volume indicator has limited effect, cannot filter all misleading signals.

To reduce risks, the following optimization directions could be considered:

- Add a trend strength indicator to aid trend reversal identification.
- Optimize smooth MA parameters for a more effective fast/slow configuration.
- Test different volume indicators to better filter misleading low-volume signals.

## Optimization Directions

- Add MACD or other auxiliary indicators to help identify trend reversals.
- Adjust ATR stop and limit settings to suit different product characteristics.
- Try increasing position sizing to improve strategy return.
- Optimize parameters based on backtest results to enhance stability.

## Summary

Overall, this is a typical trend-following strategy. The dual smooth MA system combined with the TDFI volume filter can effectively leverage trend-tracking capabilities while reducing incorrect signal rates in non-trending markets. Through parameter optimization, it can be adapted to different timeframes and products. However, it relies more on parameter tweaking than mechanical application. Lack of trend reversal identification and parameter tuning impacts should be noted. Overall, a clear and straightforward approach that is worthy of further optimization and practice.

||


## Overview

This strategy utilizes a dual smooth moving average system as the primary trading signal, combined with the TDFI volume validation indicator for trade signal filtering, in order to leverage the advantages of smooth moving averages while reducing incorrect trades in non-trending markets.

## Strategy Logic

The strategy employs two sets of smooth moving averages with different parameter configurations as the primary trading signals. First an 8-period fast smooth moving average is used as the initial confirmation, then a slightly slower 16-period smooth moving average acts as the second confirmation. When the fast MA gives a buy signal, if the slower MA also signals in the same direction within the last 1-2 bars, a long position is opened; when the fast MA gives a sell signal, if the slower MA also signals in the same direction within the last 1-2 bars, a short position is opened. Exits are triggered when the second confirmation MA reverses direction. In addition, the TDFI volume indicator is used to detect trading volume energy behind price bars to filter misleading signals. Trades are only taken when volume aligns with expectations.

## Advantages

- Smooth MAs effectively track trends and avoid market noise, catching mid- to long-term trends.
- The dual smooth MA setup enhances signal reliability, avoiding incorrect trades in non-trending markets.
- Volume indicator introduction filters misleading low-volume signals, avoiding unnecessary losses.
- High parameter optimization space allows adjustment for different products and timeframes, making it highly adaptable.

## Risks

- Smooth MAs can be slow to identify trend reversals, potentially leading to some losses.
- Dual smooth MAs may still generate concurrent wrong signals in non-trending markets.
- Volume indicator has limited effect, cannot filter all misleading signals.

To reduce risks, the following optimization directions could be considered:

- Add a trend strength indicator to aid trend reversal identification.
- Optimize smooth MA parameters for a more effective fast/slow configuration.
- Test different volume indicators to better filter misleading low-volume signals.

## Optimization Directions

- Add MACD or other auxiliary indicators to help identify trend reversals.
- Adjust ATR stop and limit settings to suit different product characteristics.
- Try increasing position sizing to improve strategy return.
- Optimize parameters based on backtest results to enhance stability.

## Summary

Overall, this is a typical trend-following strategy. The dual smooth MA system combined with the TDFI volume filter can effectively leverage trend-tracking capabilities while reducing incorrect signal rates in non-trending markets. Through parameter optimization, it can be adapted to different timeframes and products. However, it relies more on parameter tweaking than mechanical application. Lack of trend reversal identification and parameter tuning impacts should be noted. Overall, a clear and straightforward approach that is worthy of further optimization and practice.

||


## Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|1.5|SL|
|v_input_2|true|TP|
|v_input_3|14|ATR Length|
|v_input_4|0|Smoothing: SMA|RMA|EMA|WMA|
|v_input_5|8|SSL 1 Length Period|
|v_input_6|16|SSL 2 Length Period|
|v_input_7|6|TDFI Lookback|
|v_input_8|0.05|Filter High|
|v_input_9|-0.05|Filter Low|

> Source (PineScript)

```pinescript
//@version=3
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Designed per No Nonsense Forex VP rules
// Made to be as modular as possible, so we can swap the indicators in and out.
// Originated from causecelebre
// Tried to put in as much VP rules as possible

///////////////////////////////////////////////////
// Rules Implemented:
///////////////////////////////////////////////////
// - SL 1.5 x ATR
// - TP 1 x ATR
//
// - Entry conditions
//// - Entry within first confirmation cross over and 1 candle of second confirmation + volume
// - Exit conditions
//// - Exit on exit indicator or when baseline or confirmation flip 

///////////////////////////////////////////////////
// Trades entries
///////////////////////////////////////////////////
// - First entry L1 or S1 with standard SL and TP

///////////////////////////////////////////////////
// Included Indicators and settings
///////////////////////////////////////////////////
// - Confirmtion = SSL 8, 16
// - Volume = TDFI 6

//////////////////
```