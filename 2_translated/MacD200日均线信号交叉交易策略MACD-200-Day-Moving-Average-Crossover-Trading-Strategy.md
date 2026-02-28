> Name

MacD 200-Day Moving Average Signal Crossover Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/16eecb1e1a3b09aa25a.png)
[trans] 

## Overview

This trading strategy is based on the crossover operation of the MACD indicator's 200-day moving average. It combines the dual functions of the MACD indicator to judge market buy and sell signals and the 200-day moving average to judge market trends, aiming to identify more precise entry and exit timing.

## Strategy Principle 

There are two key points to this strategy:

1. The fast and slow lines of the MACD indicator generate buy and sell signals. A buy signal is generated when the fast line breaks through the slow line from below. A sell signal is generated when the fast line breaks through the slow line from above.

2. The 200-day moving average determines the overall market trend. Prices above the 200-day moving average indicate a bull market, and prices below it indicate a bear market. Buy signals are only acted upon in a bull market, and sell signals are only acted upon in a bear market.

According to these two points, the specific trading rules of this strategy are:

When the MACD fast line breaks through the MACD slow line from below with a negative histogram and prices above the 200-day moving average, a buy operation is made. When the MACD fast line breaks through the slow line from above with a positive histogram and prices below the 200-day moving average, a sell operation is made.

## Advantage Analysis 

1. The dual confirmation improves the stability and success rate of the strategy. The MACD indicator judges buy and sell signals, while the 200-day moving average judges market trends. Dual confirmation can filter out some uncertain trading signals.

2. In a strongly trending market, this strategy can bring relatively high profits. Especially in a bull market, it can quickly capture price upside opportunities.

3. The MACD indicator is also sensitive to getting out of consolidation phases. When the price ends a long period of consolidation and enters a trending phase, this strategy can quickly capture new trend directions.

## Risk Analysis 

1. This strategy is quite sensitive to parameter settings. Improper MACD indicator parameter settings may result in false signals.

2. Near trend turning points, MACD buy and sell signals tend to produce more errors. At this time, there may be a larger drawdown in the profitability of the strategy.

3. When prices are in a long period of consolidation, this strategy cannot determine a clear trend direction, which can lead to increased profit/loss fluctuation and longer drawdown periods.

## Optimization 

1. Different parameter combinations can be tested to find MACD parameters that produce more accurate signals.

2. Consider adding confirmation from other technical indicators like RSI and KD to form a consensus of multiple indicators, thereby increasing the reliability of the strategy.

3. Set stop loss points to control maximum drawdown. Immediately stop loss when prices make a significant reversal, which can effectively avoid enlarging losses.

## Conclusion 

The MACD 200-day moving average crossover strategy combines trend judgment and trading signal judgment functions, which can effectively improve profitability probability. It is a relatively robust and reliable quantitative trading strategy. However, this strategy also relies somewhat on parameters and market conditions. Continued optimization and testing can further enhance the stable profit-generating ability of the strategy.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|12|Fast Length|
|v_input_2|26|Slow Length|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|9|Signal Smoothing|
|v_input_5|false|Simple MA (Oscillator)|
|v_input_6|false|Simple MA (Signal Line)|
|v_input_7|200|Moving Average Length|


> Source (PineScript)

```pinescript
//@version=4
strategy(title="MacD 200-Day Moving Average Signal Crossover Strategy", overlay=false, precision=2, commission_value=0.26, initial_capital=10000, currency=currency.USD, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Getting inputs
fast_length = input(title="Fast Length", type=input.integer, defval=12)
slow_length = input(title="Slow Length", type=input.integer, defval=26)
src = input(title="Source", type=input.source, defval=close)
signal_length = 9
```