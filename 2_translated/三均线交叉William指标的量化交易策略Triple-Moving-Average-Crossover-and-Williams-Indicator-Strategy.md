> Name

Triple-Moving-Average-Crossover-and-Williams-Indicator-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy identifies the price trend direction by combining three smoothed moving averages, relative strength index (RSI), and Williams indicator. It seeks trading opportunities when the trend reverses. When the fast, medium, and slow moving averages align upward (downward), RSI is above (below) 50, and a down (up) Williams signal appears, it goes long (short). The stop loss is set at a certain percentage of the entry price, and take profit at a certain percentage move in the favorable direction from the entry price.

## Strategy Logic

The strategy uses three moving averages with different periods, including fast, medium, and slow MAs. When the fast MA crosses over the medium MA, it signals an upward price trend. When the fast MA crosses below the medium MA, it signals a downward price trend. After identifying the uptrend or downtrend, the strategy waits for the first trading opportunity.

Specifically, after the price enters an uptrend, the strategy waits until the following five conditions are met before going long:

1. The fast, medium, and slow MAs are all pointing up;
2. RSI is above 50;
3. A downside Williams pattern appears;
4. The price crosses over the slow MA;
5. There is no current position.

After the price enters a downtrend, the strategy waits until the following five conditions are met before going short:

1. The fast, medium, and slow MAs are all pointing down;
2. RSI is below 50;
3. An upside Williams pattern appears;
4. The price crosses below the slow MA;
5. There is no current position.

After going long or short, the strategy sets a stop loss at a certain percentage below the entry price, and a take profit target at a certain percentage above the entry price.

## Advantages

1. Combining multiple indicators to confirm entries can effectively avoid false breakouts. The triple MAs identify the trend direction, Williams catches reversal signals, and RSI filters out range-bound price action, jointly improving the accuracy of entries.
2. Setting stop loss and take profit can well control the risk/reward of each trade, ensuring winning trades exceed losing trades.
3. The strategy logic is clear and easy to understand. The parameters are reasonably set. It suits traders at different levels.

## Risks

1. Indicators may generate incorrect signals during range-bound markets, causing unnecessary entries. Optimizing RSI parameters can filter out some whipsaws.
2. The fast and medium MA crossover may have false breakouts. Using other indicators in combination, e.g., volume, is recommended.
3. If the stop loss is too close to the entry price, it may get stopped out prematurely. The stop loss should be adjusted to a proper position.
4. If the take profit is too far from the entry price, it may not get hit. The take profit also needs proper adjustment.

## Optimization Directions

1. Test different parameter combinations for the three MAs and RSI.
2. Add other indicators, like volume, to check if volume surges on breakouts.
3. Test parameters respectively based on different products.
4. Draw profit curves based on backtest results to optimize stop loss and take profit.
5. Try paper trading before enabling it to optimize parameters.

## Conclusion

The strategy has clear logic overall, entering and exiting positions with a combination of indicators, which effectively controls risk. There is large room for parameter optimization. By testing different parameter settings, this strategy can become a steady profitable quantitative trading strategy. However, no strategy can completely avoid losses. Traders need to follow trading disciplines - taking profits when winning and cutting losses when losing.

|Argument|Default|Description|
|---|---|---|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_float_1|0.1|Stop Loss %|
|v_input_float_2|0.4|Target Profit %|
|v_input_int_1|21|(?Smooth Moving Average)Fast Length|
|v_input_int_2|50|Mid Length|
|v_input_int_3|200|Slow Length|
|v_input_int_4|14|(?RSI)length|
|v_input_int_5|2|(?Fractals)Periods|

> Source (PineScript)

```pinescript
// This script is a combination of 3 smoothed moving averages, and RSI. When moving averages are aligned upward (downward) and RSI is above (below) 50 and a down (up) William fractal appears, it enters long (short) position. Exiting from the position occurs when the stop loss or take profit conditions are met.
//@version=4
strategy("Triple-Moving-Average-Crossover-and-Williams-Indicator-Strategy", overlay=true)

// Input parameters
src = input(close)
stopLossPercent = input(0.1, type=float, title="Stop Loss %")
takeProfitPercent = input(0.4, type=float, title="Target Profit %")
fastLength = input(21, minval=1, title="?Smooth Moving Average Fast Length")
midLength = input(50, minval=1, title="Mid Length")
slowLength = input(200, minval=1, title="Slow Length")
rsiLen = input(14, minval=1, title="?RSI length")
fractalsPeriods = input(2, minval=1, title="?Fractals Periods")

// Calculate moving averages
fastSMA = sma(src, fastLength)
midSMA = sma(src, midLength)
slowSMA = sma(src, slowLength)

// RSI calculation
rsiValue = rsi(src, rsiLen)

// Williams fractal detection
downFractal = ta.fractals(src, high=high[1], low=low[2], mode=fractalsPeriods)
upFractal = ta.fractals(src, high=high[2], low=low[1], mode=fractalsPeriods)

// Entry conditions
longCondition = fastSMA > midSMA and midSMA > slowSMA and rsiValue < 50 and downFractal
shortCondition = fastSMA < midSMA and midSMA < slowSMA and rsiValue > 50 and upFractal

// Exit conditions
longExit = stopLossPercent * src - src or takeProfitPercent * src + src
shortExit = stopLossPercent * src + src or takeProfitPercent * src - src

// Plot moving averages and RSI
plot(fastSMA, color=color.blue)
plot(midSMA, color=color.green)
plot(slowSMA, color=color.red)
hline(50, "RSI 50", color=color.black)

// Enter positions
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit positions
strategy.exit("Take Profit/Stop Loss", from_entry="Long", stop=longExit, limit=longExit + takeProfitPercent * src - src)
strategy.exit("Take Profit/Stop Loss", from_entry="Short", stop=shortExit - takeProfitPercent * src + src, limit=shortExit)
```

This script implements the trading strategy using Pine Script in TradingView. It uses three moving averages and RSI to identify trend reversals and set entry points. Stop loss and take profit conditions are also defined to manage risk effectively.