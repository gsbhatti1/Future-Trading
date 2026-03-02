> Name

Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c824c0d077d8c43c7c.png)
[trans]


## Overview

The trend-following strategy is a trading strategy based on the crossover of moving averages. This strategy uses the intersection of an Exponential Moving Average (EMA) and a Hull Moving Average (HMA) to determine market trend direction and generate buy/sell signals accordingly. The strategy is suitable for medium-to-short-term trend trading, aimed at tracking longer-term price trends rather than short-term oscillations.

## Strategy Logic  

The strategy employs two moving averages with different parameters: a faster EMA and a slower HMA. The EMA reacts quickly to price changes and is used to identify short-term trends, while the HMA responds more slowly, helping to determine long-term trend direction.

When the shorter EMA crosses above the longer HMA, it signals an upward trend, and the strategy will place a market buy order at the next bar open. Conversely, when the shorter EMA crosses below the longer HMA, it indicates a downward trend, and the strategy will place a market sell order at the next bar open.

To optimize entry timing, the strategy includes an option to use Heikin-Ashi bars. When enabled, buy/sell signals are based on Heikin-Ashi bars rather than regular candlesticks. This helps filter out short-term price fluctuations and reduce false signals.

The strategy also incorporates a stop-loss mechanism. If the position loss reaches the preset percentage, it will be closed at market price to limit maximum per-trade losses.

## Advantage Analysis

This strategy offers several advantages:

1. Using EMA and HMA crossovers leverages different periods of moving averages to enhance accuracy.
2. Trend-based trading reduces unnecessary trades during minor oscillations.
3. The Heikin-Ashi option optimizes entry timing by filtering out false signals.
4. A dynamic stop-loss strategy limits maximum loss per trade.
5. Customizable parameters allow for adjustments based on various assets and timeframes.

## Risk Analysis

This strategy also has some risks:

1. As a trend-following system, it performs poorly in range-bound markets.
2. Large losses may occur during trend reversals.
3. Improper stop-loss settings can lead to unnecessary stops or increased losses.
4. Incorrect parameter tuning might cause overtrading or no action at all.
5. EMA and HMA periods need optimization for different assets and timeframes.
6. Heikin-Ashi cannot fully prevent false breakouts.

## Optimization Directions

The strategy can be improved by:

1. Utilizing more indicators such as MACD, KDJ to improve trend accuracy.
2. Adding more filters like volume and ATR to reduce false signals.
3. Optimizing moving average parameters based on specific assets and timeframes.
4. Fine-tuning stop-loss percentages for better risk management.
5. Considering profit-taking features like dynamic profit stops or partial profits.
6. Testing alternative methods for calculating position costs.

## Summary

The trend-following strategy identifies trends using EMA and HMA crossovers, enhances performance with Heikin-Ashi bars and a moving stop loss mechanism. It is suitable for medium-to-short-term trading and can be further improved through parameter tuning and feature expansion. Users should be aware of the risks associated with reversals and improper stop-loss settings. Overall, it provides a flexible framework for trend trading across various assets and timeframes.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Heikin Ashi Source|
|v_input_2|true|Stop Loss|
|v_input_int_1|9|EMA Length|
|v_input_int_2|69|HMA Length|
|v_input_float_1|-6.5|Stop Loss (%)|


> Source (PineScript)

```pinescript
//@version=5
strategy("Trend-Following-Strategy", overlay=true, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=15)

//Heikin Ashi Option
ha = input(true, title="Heikin Ashi Source")
src = ha ? request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, close, barmerge.gaps_off, barmerge.lookahead_off) : close
usestoploss = input(true, title="Stop Loss")

//EMA
len1 = input.int(9, minval=1, title="EMA Length")
ema = ta.ema(src, len1)
emaline = plot(ema, color=color.blue, linewidth=2)

//HMA
len2 = input.int(69, minval=1, title="HMA Length")
hma = ta.hma(src, len2)
hmpline = plot(hma, color=color.red, linewidth=2)

//Long Entry Condition
long_condition = ema > hma

//Short Entry Condition
short_condition = ema < hma

//Heikin Ashi Bar Filtering (Optional)
if usestoploss
    long_entry_price = src[1]
    short_entry_price = src[1]

//Place Orders
if long_condition and not na(long_entry_price) and not na(emaline)
    strategy.entry("Long", strategy.long, price=long_entry_price)

if short_condition and not na(short_entry_price) and not na(hmpline)
    strategy.exit("Short Exit", "Long", price=short_entry_price)

//Stop Loss
stop_loss_percent = input.float(-6.5, minval=-100, maxval=0, title="Stop Loss (%)")
if usestoploss
    stop_loss_level = ema * (1 + stop_loss_percent / 100)
    strategy.exit("Stop Loss", "Long", stop=stop_loss_level)

//Plot Strategy Lines
plotshape(series=long_condition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=short_condition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

```

Please note that the Pine Script provided here is a simplified version based on the strategy description. Adjustments may be needed for specific use cases and further optimization.