> Name

HMA Daily Crossover Trading Strategy

> Author

ChaoZhang

> Strategy Description


## Overview

This strategy uses the cross signal of HMA moving average and daily line to enter the market, and sets stop loss and take profit logic to manage positions. This strategy combines different time period indicators and is suitable for medium and long-term trend trading.

## Strategy Principle

This strategy mainly judges trading signals through the following indicators and rules:

- **HMA Moving Average:** Calculate the Hull moving average of the price and determine the medium and long-term trend direction.
- **Daily Closing Price:** Determine the short-period price trend.
- **Entry Signal:** HMA crosses yesterday's closing price, and the short-term price is higher than the previous day's price, which is considered a long signal; otherwise, it is short.
- **Stop Loss/Profit:** Set fixed stop loss and take profit points, and close positions when the price hits these levels.

## Strategic Advantages

- The HMA indicator smoothing parameter is adjustable and has strong adaptability.
- Consider different time period indicators to improve signal quality.
- Set stop loss and take profit logic to facilitate risk control.
- Clear entry rules and position management strategies.
- Backtest parameters can be optimized to adapt to different market environments.

## Risk Analysis

- HMA lag may miss the best entry point.
- Fixed Stop Loss and Take Profit parameters may be too aggressive or conservative.
- Lack of judgment on the strength of the trend, and possible opening of a position in the opposite direction.
- Simple trading rules can easily produce false signals.

Consider the following measures to reduce risk:

1. Optimize HMA parameters to balance hysteresis.
2. Set a trailing stop loss and adjust the stop loss position in real time.
3. Add volume and price indicators to judge the strength of the trend.
4. Add indicators such as MACD to verify trading signals.

## Strategy Optimization Direction

Directions in which this strategy can be optimized:

1. Optimize HMA parameters and find the best parameter combination.
2. Add trend strength indicators to avoid counter-trend trading.
3. Use dynamic stop loss and take profit instead of fixed points.
4. Introduce machine learning algorithms and use big data to automatically optimize parameters.
5. Add a simulated delivery function to test actual performance.

## Summary

The overall idea of this strategy is clear, but there is still room for optimization. Adding trend judgment indicators, dynamic stop loss, etc., can improve the stability of the strategy. Overall, the strategic framework is reasonable and helps to grasp medium and long-term trends.

---

## Overview

This strategy enters trades based on HMA line and daily candlestick crosses and manages positions using stop loss and take profit logic. It combines different timeframe indicators for trend trading.

## Strategy Logic

The main signals and rules:

- **HMA Line:** Calculates Hull Moving Average to determine medium-long term trend.
- **Daily Close Price:** Judges short-term price action.
- **Entry Signal:** HMA crossing above previous daily close, with price higher than previous day's price for long. Reverse for short.
- **Stop Loss/Take Profit:** Fixed levels to close positions when hit.

## Advantages

- Adjustable HMA parameters for adaptability.
- Considers multi-timeframe indicators for higher quality signals.
- Stop loss/take profit facilitates risk management.
- Clear entry rules and position management.
- Backtest parameters can be optimized for different markets.

## Risks

- HMA lag may miss the best entry timing.
- Fixed stop loss/take profit may be too aggressive or conservative.
- Lacks trend strength filter, risks countertrend trades.
- Simple rules prone to false signals.

Improvements:

1. Optimize HMA parameters for lag.
2. Use trailing stop loss instead of fixed.
3. Add volume or momentum indicators to judge trend strength.
4. Incorporate other indicators like MACD for signal confirmation.

## Optimization

Potential ways to optimize the strategy:

1. Optimize HMA parameters for ideal combo.
2. Add trend strength filter to avoid countertrends.
3. Use dynamic stops instead of fixed levels.
4. Incorporate machine learning for auto parameter optimization.
5. Add simulated trading to test real-world performance.

## Summary

The strategy logic is clear but has room for improvement. Adding trend filters, dynamic stops can improve stability. Overall provides a reasonable framework for catching medium-long term trends.

---

|Argument|Default|Description|
|----|----|----|
|v_input_1|-0.05|StopLoss $|
|v_input_2|0.05|TargetPoint $|
|v_input_3_open|0|Source: open, high, low, close, hl2, hlc3, hlcc4, ohlc4|
|v_input_4|14|Period|

> Source (PineScript)

```pinescript
//@version=4
// created by SeaSide420 Enters on crossovers, exits Basket when profit $ = TP
strategy(title="HMA & D1 crossover", overlay=true, currency="BTC", initial_capital=1, default_qty_type=strategy.percent_of_equity, default_qty_value=1, commission_type=strategy.commission.percent,commission_value=0.25,slippage=1)
SL = input(defval=-0.05, title="StopLoss $", type=input.float, step=0.01, maxval=-0.01)
TP = input(defval=0.05, title="TargetPoint $", type=input.float, step=0.01, minval=0.01)
price = input(title="Source", type=input.source, defval=open)
Period = input(14, minval=1)
hma = wma(2*wma(price, Period/2) - wma(price, Period), round(sqrt(Period)))
s1 = security(syminfo.tickerid, timeframe.period, price, barmerge.gaps_off, barmerge.lookahead_off)
s2 = security(syminfo.tickerid, "D", price, barmerge.gaps_off, barmerge.lookahead_off)
cp = s2 < price ? color.lime : color.red
plot(cp)
```