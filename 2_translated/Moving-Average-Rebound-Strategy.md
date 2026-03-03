> Name

Moving-Average-Rebound-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1c8ccdc05512fb628d4.png)
[trans]

## Overview

The Moving-Average-Rebound-Strategy is a strategy that combines technical indicators and price patterns to trade long and short around support and resistance levels. The strategy uses moving averages to identify market trend direction, pattern indicators to assist in determining turning points, and previous swing highs/lows to spot key support and resistance levels for counter-trend trading.

## Strategy Principles

The key steps for determining trade entries are:

1. Use the Alligator triple moving average indicator to judge trend direction. Crossing the Lip Lines signals strong momentum.
2. Identify potential reversal zones with Peak-Trough pattern indicator when in overbought/oversold areas. Breaking specific highs/lows indicates possible reversal.
3. Combine with support and resistance to pinpoint counter-trend trade entry points around key levels.
4. Use EMAS to assist in determining overall long-term trend direction. Use mean reversion in range-bound and trend following in trending markets.
5. Employ trailing stop loss to control single trade loss amount.

## Advantages

Advantages of the strategy:

1. Combining signals from multiple indicators improves accuracy.
2. Trading counter-trend from key support/resistance areas has high probability.
3. Trailing stop loss containing losses on single trades.

## Risks

Risks involved:

1. More indicators can lead to higher trade frequency & needs transaction cost control.
2. Failed support/resistance levels are the biggest risk. Price may not reverse as expected leading to large losses.
3. Stop loss can be taken out during huge volatile moves.

## Enhancement Areas

Areas for improvement:

1. Optimize weights between indicators to find best performance combination.
2. Employ machine learning for improving key support/resistance level accuracy.
3. Add volume indicators to avoid trades when volatile but low volume environments.
4. Refine adaptive stop loss models to balance effectiveness and unnecessary stops.

## Summary

In summary, the Moving-Average-Rebound-Strategy utilizes a confluence of indicators including moving averages, price patterns, and support/resistance for entries. It is a typical technical strategy with higher accuracy from multiple signals. Monitor risks around failure of key levels and stop loss slippage. Further optimization on indicator weights, machine learning, and volume can enhance performance.

||

## Overview
The Moving-Average-Rebound-Strategy is a strategy that combines technical indicators and price patterns to trade long and short around support and resistance levels. The strategy uses moving averages to identify market trend direction, pattern indicators to assist in determining turning points, and previous swing highs/lows to spot key support and resistance levels for counter-trend trading.

## Strategy Principles
The key steps for determining trade entries are:

1. Use the Alligator triple moving average indicator to judge trend direction. Crossing the Lip Lines signals strong momentum.
2. Identify potential reversal zones with Peak-Trough pattern indicator when in overbought/oversold areas. Breaking specific highs/lows indicates possible reversal.
3. Combine with support and resistance to pinpoint counter-trend trade entry points around key levels.
4. Use EMAS to assist in determining overall long-term trend direction. Use mean reversion in range-bound and trend following in trending markets.
5. Employ trailing stop loss to control single trade loss amount.

## Advantages

Advantages of the strategy:

1. Combining signals from multiple indicators improves accuracy.
2. Trading counter-trend from key support/resistance areas has high probability.
3. Trailing stop loss containing losses on single trades.

## Risks

Risks involved:

1. More indicators can lead to higher trade frequency & needs transaction cost control.
2. Failed support/resistance levels are the biggest risk. Price may not reverse as expected leading to large losses.
3. Stop loss can be taken out during huge volatile moves.

## Enhancement Areas

Areas for improvement:

1. Optimize weights between indicators to find best performance combination.
2. Employ machine learning for improving key support/resistance level accuracy.
3. Add volume indicators to avoid trades when volatile but low volume environments.
4. Refine adaptive stop loss models to balance effectiveness and unnecessary stops.

## Summary
In summary, the Moving-Average-Rebound-Strategy utilizes a confluence of indicators including moving averages, price patterns, and support/resistance for entries. It is a typical technical strategy with higher accuracy from multiple signals. Monitor risks around failure of key levels and stop loss slippage. Further optimization on indicator weights, machine learning, and volume can enhance performance.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|5|? Lips Length|
|v_input_2|8|? Teeth Length|
|v_input_3|13|? Jaw Length|
|v_input_4|3|? Lips Offset|
|v_input_5|5|? Teeth Offset|
|v_input_6|8|? Jaw Offset|
|v_input_int_1|2|? Period|
|v_input_7|true|⤒⤓ Show Res-Sup|
|v_input_8|13|⤒⤓ Res-Sup Length|

## Source (PineScript)

```pinescript
/*backtest
start: 2022-12-21 00:00:00
end: 2023-12-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © vhurtadocos

//@version=5
strategy('Estrategia EMA Resistencia Soporte', shorttitle='Estrategia EMA RESISTENCIA Y SOPORTE', overlay=true, margin_long=100, margin_short=100, pyramiding = 10 )

//INICIO DE CONDICIONES BASICAS
/// Alligator
smma(src, length) =>
    smma = 0.0
    sma_1 = ta.sma(src, length)
    smma := na(smma[1]) ? sma_1 : (smma[1] * (length - 1) + src) / length
    smma
lipsLength = input.int(title='? Lips Length', defval=5)
teethLength = input.int(title='? Teeth Length', defval=8)
jawLength = input.int(title='? Jaw Length', defval=13)
lipsOffset = input.int(title='? Lips Offset', defval=3)
teethOffset = input.int(title='? Teeth Offset', defval=5)
jawOffset = input.int(title='? Jaw Offset', defval=8)
lips = smma(hl2, lipsLength)
teeth = smma(hl2, teethLength)
jaw = smma(hl2, jawLength)

// Fractals
n = input.int(title='? Period', defval=2, minval=2)
upFractal = high[n + 2] < high[n] and high[n + 1] < high[n] and high[n - 1] < high[n] and high[n - 2] < high[n] or high[n + 3] < high[n] and high[n + 2] < high[n] and high[n + 1] == high[n] and high[n - 1] < high[n] and high[n - 2] < high[n] or high[n + 4] < high[n] and high[n + 3] < high[n] and high[n + 2] == high[n] and high[n + 1] <= high[n] and high[n - 1] < high[n] and high[n - 2] < high[n] or high[n + 5] < high[n] and high[n + 4] < high[n] and high[n + 3] == high[n] and high[n + 2] == high[n] and high[n + 1] <= high[n] and high[n - 1] < high[n] and high[n - 2] < high[n] or high[n + 6] < high[n] and high[n + 5] < high[n] and high[n + 4] == high[n] and high[n + 3] <= high[n] and high[n + 2] == high[n] and high[n + 1] <= high[n] and high[n - 1] < high[n] and high[n - 2] < high[n]
dnFractal = low[n + 2] > low[n] and low[n + 1] > low[n] and low[n - 1] > low[n] and low[n - 2] > low[n]

// Additional Code Here
```

This PineScript code defines the strategy as described, with input parameters for Alligator indicator lengths and offsets, and fractal detection logic.