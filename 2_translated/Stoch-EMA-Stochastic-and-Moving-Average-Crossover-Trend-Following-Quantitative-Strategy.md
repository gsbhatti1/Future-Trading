> Name

Stochastic-and-Moving-Average-Crossover-Trend-Following-Quantitative-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/14a6ce95456462b04b6.png)
[trans]
## Overview

This strategy mainly utilizes the crosses of the Stoch indicator in the overbought/oversold area as entry signals, while judging the current trend direction with the EMA indicator. It only goes long in an uptrend determined by EMA and goes short in a downtrend, which is a typical trend following strategy.

## Principles

The strategy consists of three main parts:

1. EMA to determine the trend direction

   Using one fast and one slow EMA, when the fast EMA is above the slow EMA, it is determined as an upward trend. When the fast EMA is below the slow EMA, it is determined as a downward trend.

2. Stoch to generate trading signals 

   The Stoch indicator consists of %K and %D lines. When %K crosses above %D in the overbought area, it generates a buy signal. When %K crosses below %D in the oversold area, it generates a sell signal. This strategy only takes Stoch crossover signals when they happen in the overbought/oversold zones.

3. Risk management mechanism

   The strategy also sets stop loss and take profit levels. When holding a long position, if the price breaks the stop loss level, it will exit the trade. If the price breaks the take profit level, it will close the position for profit. The same logic applies to short positions.

In general, this is a typical quantitative trading strategy that uses a combination of indicators to determine trend direction and trading signals, supplemented by strict risk management rules to reduce trading risk.

## Advantage Analysis

The main advantages of this strategy are:

1. Using EMA to determine the major and minor trends avoids being trapped in a sideways market.
2. The strength of the Stoch indicator lies in its ability to accurately reflect overbought/oversold levels. Combining this with crossover signals allows overbought/oversold zone trading.
3. The strategy specifies the possible long and short scenarios clearly, which further filters the signals and avoids blindly opening positions in a complex market.
4. The strict risk management helps control the loss of individual trades, limits max drawdown while still giving profitable trades room to run.

## Risk Analysis

There are also some risks with this strategy:

1. Indicators like EMA and Stoch have lagging nature, making it hard for this strategy to timely catch market reversals.
2. Purely relying on indicators can establish bias easily, thus missing trading opportunities actually provided by the market.
3. The risk management mechanism itself can also limit the profit potential by setting premature stop loss and take profit.
4. There are risks associated with parameter selection. Extensive backtesting and optimization is needed to find the optimal parameters.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Try different types of EMA for trend determination, like WMA, Hull MA etc and compare results.
2. Combine other indicators to generate trading signals, e.g. MACD, KDJ to build a multi-indicator system.
3. Optimize stop loss and take profit settings to better adapt to market volatility. Can set wider stop loss and tighter take profit.
4. Test performance variance across different products and time frames to find optimal combination.
5. Consider introducing machine learning models to aid trend and signal judgment to make the strategy more intelligent.

## Conclusion

In conclusion, this strategy combines commonly used indicators to form a relatively mature trend following system, taking into account trend determination, trading signals, and risk management. With further optimization, I believe this strategy can achieve better live trading results. At the same time, we should also be aware of limitations of single strategies and continue to learn market intricacies in pursuit of long-term steady profits.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|════════════ INDICATORS ════════════|
|v_input_2|55|Fast MA Period|
|v_input_3|89|Slow MA Period|
|v_input_4|14|Stochastic Length|
|v_input_5|6|%K Smooth|
|v_input_6|3|%D Smooth|
|v_input_7|true|Highlight Stoch Cross?|
|v_input_8|true|Highlight Trend?|
|v_input_9|true|═══════════════ FROM ═══════════════|
|v_input_10|true|From day|
|v_input_11|true|From month|