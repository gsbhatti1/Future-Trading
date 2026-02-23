> Name

Bullish-Engulfing Buy-and-Sell Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fe0eb407587a51dbc8.png)
[trans]

## Overview

The Bullish Engulfing buy and sell strategy is a quantitative trading strategy based on candlestick patterns. It captures opportunities to profit from price reversals by identifying the "Bullish Engulfing" candlestick pattern. The main advantages of this strategy are:

1. Based on mature technical analysis theories, it identifies high probability price reversal opportunities.
2. Simple and intuitive trading signals.
3. Controllable risks.

### Strategy Logic

This strategy identifies price reversals based on the "Bullish Engulfing" candlestick pattern.

When a stock is in a downtrend, if a candlestick with a small real body is followed by a candlestick whose real body completely engulfs the previous real body, and the closing price is higher than the previous high price, this forms a Bullish Engulfing pattern, signaling an imminent trend reversal where the price will start rising.

This strategy will open a long position when a Bullish Engulfing pattern is identified, with a profit target of 1% and a stop loss of 1%, to lock in profits.

### Advantage Analysis

The advantages of this strategy are:

1. Based on mature technical analysis theories, the Bullish Engulfing pattern signals a high probability price reversal.
2. Trading signals are simple and intuitive, easy to understand and automate for quantitative trading.
3. Trading high liquidity products like index futures allows efficient entries and exits.
4. The profit target and stop loss exits effectively control the risk/reward ratio of each trade, ensuring profitability and avoiding huge losses.
5. Flexible parameter adjustments suit different products and market environments.

### Risk Analysis

There are some risks to this strategy:

1. False signals exist as it is based on technical analysis theories.
2. Market regime changes may invalidate parameters which need adjustment.
3. Stop loss values that are too tight may result in premature exiting, while values too wide may produce large losses.

To address these risks, we can:

1. Optimize parameters and verify performance across market conditions.
2. Widen stop loss levels to control single trade loss at acceptable levels.
3. Trade high liquidity products with suitable volatility like index and futures ETFs.

### Optimization Directions

This strategy can also be enhanced by:

1. Adding filters like moving averages to avoid trading against trends.
2. Increasing profit target to expand profit potential.
3. Optimizing stop loss mechanisms, like trailing stops to reduce the probability of stopping out.
4. Using combinations of other candlestick patterns similar to "Bullish Engulfing" to create a trading system.

## Conclusion

The Bullish Engulfing buy and sell strategy is a mature quantitative trading strategy based on technical analysis, with the advantages of simple and clear trading signals that are easy to implement. With optimized parameters and good risk control measures, it can produce steady profits and is highly recommendable.

||

## Overview

The Bullish Engulfing buy and sell strategy is a quantitative trading strategy based on candlestick patterns. It captures opportunities to profit from price reversals by identifying the "Bullish Engulfing" candlestick pattern. The main advantages of this strategy are:

1. Based on mature technical analysis theories, it identifies high probability price reversal opportunities.
2. Simple and intuitive trading signals.
3. Controllable risks.

### Strategy Logic

This strategy identifies price reversals based on the "Bullish Engulfing" candlestick pattern.

When a stock is in a downtrend, if a candlestick with a small real body is followed by a candlestick whose real body completely engulfs the previous real body, and the closing price is higher than the previous high price, this forms a Bullish Engulfing pattern, signaling an imminent trend reversal where the price will start rising.

This strategy will open a long position when a Bullish Engulfing pattern is identified, with a profit target of 1% and a stop loss of 1%, to lock in profits.

### Advantage Analysis

The advantages of this strategy are:

1. Based on mature technical analysis theories, the Bullish Engulfing pattern signals a high probability price reversal.
2. Trading signals are simple and intuitive, easy to understand and automate for quantitative trading.
3. Trading high liquidity products like index futures allows efficient entries and exits.
4. The profit target and stop loss exits effectively control the risk/reward ratio of each trade, ensuring profitability and avoiding huge losses.
5. Flexible parameter adjustments suit different products and market environments.

### Risk Analysis

There are some risks to this strategy:

1. False signals exist as it is based on technical analysis theories.
2. Market regime changes may invalidate parameters which need adjustment.
3. Stop loss values that are too tight may result in premature exiting, while values too wide may produce large losses.

To address these risks, we can:

1. Optimize parameters and verify performance across market conditions.
2. Widen stop loss levels to control single trade loss at acceptable levels.
3. Trade high liquidity products with suitable volatility like index and futures ETFs.

### Optimization Directions

This strategy can also be enhanced by:

1. Adding filters like moving averages to avoid trading against trends.
2. Increasing profit target to expand profit potential.
3. Optimizing stop loss mechanisms, like trailing stops to reduce the probability of stopping out.
4. Using combinations of other candlestick patterns similar to "Bullish Engulfing" to create a trading system.

## Conclusion

The Bullish Engulfing buy and sell strategy is a mature quantitative trading strategy based on technical analysis, with the advantages of simple and clear trading signals that are easy to implement. With optimized parameters and good risk control measures, it can produce steady profits and is highly recommendable.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|true|(?START DATE BACKTESTING)D: |
|v_input_int_2|true|M: |
|v_input_int_3|2022|Y: |
|v_input_int_4|31|(?END DATE BACKTESTING)D: |
|v_input_int_5|12|M: |
|v_input_int_6|2023|Y: |
|v_input_float_1|true|(?TAKE PROFIT-STOP LOSS)Target profit (%): |
|v_input_float_2|true|Stop Loss (%): |
|v_input_float_3|2|(?RISK MANAGEMENT)Orders size (%): |
|v_input_string_1|0|(?BULLISH ENGULFING)Detect Trend Based On: SMA50|SMA50, SMA200|No detection|
|v_input_color_1|#2bff00|Label Color Bullish|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-12-20 00:00:00
end: 2023-12-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © thequantscience

// ██████╗ ██╗   ██╗██╗     ██╗     ██╗███████╗██╗  ██╗    ███████╗███╗   ██╗ ██████╗ ██╗   ██╗██╗     ███████╗██╗███╗   ██╗ ██████╗ 
// ██╔══██╗██║   ██║██║     ██║     ██║██╔════╝██║  ██║    ██╔════╝████╗  ██║██╔═══██╗██║   ██║██║     ██╔════╝██║████╗  ██║██╔══██╗ 
// ██████╔╝██║   ██║██║     ██║     ██║███████╗███████║    █████╗  ██╔██╗ ██║██║   ██║██║   ██║██║     █████╗  ██║██╔██╗ ██║██║  ██║ 
// ██╔══██╗██║   ██║██║     ██║     ██║╚════██║██╔══██║    ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██║     ██╔══╝  ██║██║╚██╗██║██║  ██║ 
// ██████╔╝╚██████╔╝███████╗███████╗██║███████║██║  ██║    ███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║     ██║██║ ╚████║██████╔╝ 
// ╚