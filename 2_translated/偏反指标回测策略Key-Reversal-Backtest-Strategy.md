> Name

Key-Reversal-Backtest-Strategy

> Author

ChaoZhang

### Overview

The key reversal backtest strategy detects potential short opportunities in the market by checking if stock prices hit new highs and then close lower. It is a short-term trading strategy. This strategy combines visual pattern recognition to assist in identifying price reversal signals, and then backtests to verify the feasibility of the strategy.

### Strategy Principle  

The core logic of this strategy is based on the "key reversal indicator" theory, by judging whether there are obvious signs of decline after the price hits a new high, to identify potential short opportunities. The specific implementation principles are as follows:

1. Define the parameter `nLength`, which represents the lookback period, to determine whether the price is hitting a new high or not;  
2. Define the variable `xHH` to store the highest price in the past `nLength` cycles;
3. Define the variable `C1` to determine if today's highest price exceeds `xHH`, i.e., hitting a new high, while the closing price is lower than the previous day's closing price, which meets the conditions that may be a key reversal pattern;  
4. Draw triangle to indicate the potential key reversal K-line today;

5. When identifying the key reversal pattern, make short-term short trades and set stop profit and stop loss logic.

Through the above process, potential key reversal patterns can be effectively identified, price reversal signals can be judged, and short-term short trades can be made.

### Advantage Analysis   

The strategy has the following advantages:

1. Identifying reversal signals based on actual price patterns is more reliable;  
2. Visual graphical indicators make trading signals more intuitive;
3. Implementing stop profit and stop loss logic is conducive to risk control;  
4. Backtesting to verify the feasibility of the strategy is more convincing.

Overall, the strategy combines multiple factors to determine trading signals and backtesting to verify the accuracy of price reversals is relatively high, with good practical value.

### Risk Analysis

Although the strategy has obvious advantages, there are still some risks to note:

1. Key reversal patterns do not necessarily lead to trend reversals, there is a certain risk of false signals;  
2. The sample size of a single stock may be small and may not fully represent the overall market;
3. Improper stop loss point settings can lead to greater capital losses.

To avoid the above risks, the following points can be considered:

1. Verify trading signals with more factors, such as abnormal trading volume;  
2. Increase backtest sample size, combination backtest of different varieties;  
3. Optimize and test different stop loss points to find the optimal parameters.

### Optimization Directions   

There are still some directions that can be optimized in this strategy:

1. Increase machine learning algorithms to train models to determine the probability of key reversal patterns to improve accuracy;
2. Optimize stop loss algorithms, such as trailing stop loss, average stop loss, etc., to reduce single stop loss;
3. Incorporate more factors such as sentiment analysis to determine the probability of market reversal and set dynamic trading signals;
4. Enrich strategy types, such as combining momentum indicators, volatility indicators, etc. to determine reversal signals;  
5. Use backtesting and optimization functions of more complex trading systems to improve strategy flexibility.

Through the above aspects of optimization, the accuracy and practical level of this trading strategy can be further improved.

### Summary  

The key reversal backtest strategy identifies short-term reversal signals by judging price patterns, and verifies them through backtesting. It can effectively capture reversal opportunities. This strategy has intuitive graphical indicators and complete stop profit and stop loss logic, with good practical value. Of course, certain false signal risks still need to be noted. By continuously optimizing the judgment model and stop loss algorithm, the effect of the strategy can be better. Overall, this strategy provides new ideas for judging market reversals and is a very promising quantitative trading method.

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Take Profit pip|
|v_input_2|10|Stop Loss pip|
|v_input_3|true|Enter the number of bars over which to look for a new high in prices.|


> Source (PineScript)

``` pinescript
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ChaoZhang

//@version=5
indicator("Key-Reversal-Backtest-Strategy", overlay=true)
nLength = input(20, title="Lookback Period")
xHH = ta.highest(high, nLength)
C1 = high > xHH and close < close[1]
plotshape(series=C1, location=location.abovebar, color=color.red, style=shape.triangleup, title="Potential Key Reversal K-line")

if (C1)
    strategy.entry("Short", strategy.short)

ta.stopprofit(strategy.short, distance=v_input_1)
ta.stoploss(strategy.short, distance=v_input_2)
```