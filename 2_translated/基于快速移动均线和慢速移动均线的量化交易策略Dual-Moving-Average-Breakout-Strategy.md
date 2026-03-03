> Name

Dual Moving Average Breakout Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b5cb668aa015a95ac2.png)
 [trans]
## Overview

The Dual Moving Average Breakout Strategy is a quantitative trading strategy based on a fast moving average and a slow moving average. It uses two exponential moving averages (EMA) with different periods as trading signals. When the fast EMA crosses above the slow EMA, a buy signal is generated. When the fast EMA crosses below the slow EMA, a sell signal is generated.

## Strategy Logic

The core logic of this strategy is to use a fast moving average and a slow moving average to form trading signals. The strategy defines the fast EMA period as 12 days and the slow EMA period as 26 days. The calculation method is as follows:

1. Calculate the exponential moving average AP of the price array with a period of 2 days
2. Calculate the fast moving average Fast based on AP, with a period of 12 days
3. Calculate the slow moving average Slow based on AP, with a period of 26 days
4. Compare the fast and slow moving averages:
   1. When Fast crosses above Slow, it is a bullish signal
   2. When Fast crosses below Slow, it is a bearish signal
5. Determine specific trading signals combining price and moving average relationship:
   1. Bullish signal: Fast>Slow && AP>Fast
   2. Bearish signal: Fast<Slow && AP<Fast

Using the crossover of the fast and slow moving average to determine market trends and generate trading signals is a typical dual moving average strategy.

## Advantage Analysis

The Dual Moving Average Breakout Strategy has the following advantages:

1. The strategy logic is simple and clear, easy to understand and implement
2. The moving average period can be adjusted to adapt to different market environments
3. Allow both long and short positions to achieve higher returns
4. More precise trading signals can be generated combining price and moving averages
5. The lagging feature of moving averages can effectively filter out market noise

## Risk Analysis

The Dual Moving Average Breakout Strategy also has some risks:

1. More false signals may occur when the market is range-bound
2. The dual moving average strategy may cause curve fitting, ignoring structural market changes
3. Relying solely on technical indicators is vulnerable to fake breakouts, with the risk of losses

Solutions:

1. Optimize the moving average period to better adapt to current market conditions
2. Confirm signals with other indicators like volume to avoid fake breakouts
3. Adopt trend following strategies to control profit/loss ratio and reduce risk

## Optimization Directions

The Dual Moving Average Breakout Strategy can be optimized in the following aspects:

1. Find more suitable moving average period combinations to adapt to market changes
2. Add indicators like volume for signal filtering to ensure validity
3. Incorporate market structure indicators to identify trends and adjust parameters
4. Adopt dynamic moving averages which can automatically adjust periods based on market changes
5. Incorporate stop loss strategies to effectively control risk and protect capital

## Conclusion

The Dual Moving Average Breakout Strategy is a simple and practical quantitative trading strategy. It has advantages like easy logic and implementation, and also has some market adaptability issues. We can make it a stable profitable trading system through parameter optimization, signal filtering, risk control, etc. Overall, the dual moving average strategy is a great strategy prototype worth in-depth research and application for quantitative traders.

||

## Overview

The Dual Moving Average Breakout Strategy is a quantitative trading strategy based on a fast moving average and a slow moving average. It uses two exponential moving averages (EMA) with different periods as trading signals. When the fast EMA crosses above the slow EMA, a buy signal is generated. When the fast EMA crosses below the slow EMA, a sell signal is generated.

## Strategy Logic

The core logic of this strategy is to use a fast moving average and a slow moving average to form trading signals. The strategy defines the fast EMA period as 12 days and the slow EMA period as 26 days. The calculation method is as follows:

1. Calculate the exponential moving average AP of the price array with a period of 2 days
2. Calculate the fast moving average Fast based on AP, with a period of 12 days
3. Calculate the slow moving average Slow based on AP, with a period of 26 days
4. Compare the fast and slow moving averages:
   1. When Fast crosses above Slow, it is a bullish signal
   2. When Fast crosses below Slow, it is a bearish signal
5. Determine specific trading signals combining price and moving average relationship:
   1. Bullish signal: Fast>Slow && AP>Fast
   2. Bearish signal: Fast<Slow && AP<Fast

Using the crossover of the fast and slow moving average to determine market trends and generate trading signals is a typical dual moving average strategy.

## Advantage Analysis

The Dual Moving Average Breakout Strategy has the following advantages:

1. The strategy logic is simple and clear, easy to understand and implement
2. The moving average period can be adjusted to adapt to different market environments
3. Allow both long and short positions to achieve higher returns
4. More precise trading signals can be generated combining price and moving averages
5. The lagging feature of moving averages can effectively filter out market noise

## Risk Analysis

The Dual Moving Average Breakout Strategy also has some risks:

1. More false signals may occur when the market is range-bound
2. The dual moving average strategy may cause curve fitting, ignoring structural market changes
3. Relying solely on technical indicators is vulnerable to fake breakouts, with the risk of losses

Solutions:

1. Optimize the moving average period to better adapt to current market conditions
2. Confirm signals with other indicators like volume to avoid fake breakouts
3. Adopt trend following strategies to control profit/loss ratio and reduce risk

## Optimization Directions

The Dual Moving Average Breakout Strategy can be optimized in the following aspects:

1. Find more suitable moving average period combinations to adapt to market changes
2. Add indicators like volume for signal filtering to ensure validity
3. Incorporate market structure indicators to identify trends and adjust parameters
4. Adopt dynamic moving averages which can automatically adjust periods based on market changes
5. Incorporate stop loss strategies to effectively control risk and protect capital

## Conclusion

The Dual Moving Average Breakout Strategy is a simple and practical quantitative trading strategy. It has advantages like easy logic and implementation, and also has some market adaptability issues. We can make it a stable profitable trading system through parameter optimization, signal filtering, risk control, etc. Overall, the dual moving average strategy is a great strategy prototype worth in-depth research and application for quantitative traders.

[/trans]

> Strategy Arguments

| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_1 | 0 | Long/Short: Long only | Short only | Both |
| v_input_2_ohlc4 | 0 | Data Array: ohlc4 | high | low | open | hl2 | hlc3 | hlcc4 | close |
| v_input_3 | 12 | Short MA period |
| v_input_4 | 26 | Long MA period |
| v_input_5 | 2000 | From Year |
| v_input_6 | true | From Month |
| v_input_7 | true | From Day |
| v_input_8 | 9999 | To Year |
| v_input_9 | 12 | To Month |
| v_input_10 | 31 | To Day |

> Source (PineScript)

```pinescript
//@version=4
strategy("Dual Moving Average Breakout Strategy", overlay=true)

// CDC ActionZone V2 29 Sep 2016
// CDC ActionZone is based on a simple 2MA and is most suitable for use with medium volatility market
// 11 Nov 2016 : Ported to Trading View with minor UI enhancement
LSB = input(title="Long/Short", defval="Long only", options=["Long only", "Short only", "Both"])
src = input(title="Data Array", type=input.source, defval=close)
short_ma_period = input(12, title="Short MA period")
long_ma_period = input(26, title="Long MA period")
start_year = input(2000, title="From Year")
start_month = input(true, title="From Month")
start_day = input(true, title="From Day")
end_year = input(9999, title="To Year")
end_month = input(12, title="To Month")
end_day = input(31, title="To Day")

// Calculate EMA
short_ma = ema(src, short_ma_period)
long_ma = ema(src, long_ma_period)

// Generate signals
long_signal = crossover(short_ma, long_ma)
short_signal = crossunder(short_ma, long_ma)

// Plot signals
plotshape(series=long_signal, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(series=short_signal, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")

// Strategy logic
if (LSB == "Both")
    strategy.entry("Long", strategy.long, when=long_signal)
    strategy.exit("Short", from_entry="Long", when=short_signal)
else if (LSB == "Long only")
    strategy.entry("Long", strategy.long, when=long_signal)
else if (LSB == "Short only")
    strategy.entry("Short", strategy.short, when=short_signal)
```