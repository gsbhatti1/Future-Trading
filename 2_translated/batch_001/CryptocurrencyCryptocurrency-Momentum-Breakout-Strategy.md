> Name

Cryptocurrency Momentum Breakout Strategy Cryptocurrency-Momentum-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/eaab537c14cced3117.png)

[trans]

### Overview

This strategy utilizes momentum indicators to identify the main trend direction in the Cryptocurrency market and establishes long positions at breakout points, realizing the trading idea of trend following.

### Strategy Logic

The strategy uses a custom "Pump&Dump Oscillator" as the only indicator. The oscillator uses the size of candlestick bodies to identify the main trend direction of the market. Specifically, it calculates the moving average of candlestick bodies and multiplies it by a user-set multiplier. When the body is greater than the moving average, it signals an uptrend. When the body is less than the moving average, it signals a downtrend.

Based on the oscillator indicator, this strategy only establishes long positions. When the indicator shows that the market is currently in an uptrend, a long position is established on the close of that candlestick. Afterwards, if a downtrend signal appears, or the stop loss is triggered, all positions will be closed.

The strategy provides two stop loss methods, either one or both can be used:

1. Percentage stop loss: Users can set the maximum percentage loss allowed for each position. If the price drops below this percentage stop loss level, the position will be closed.
2. Breakout stop loss: Record the lowest point of the candlestick when opening the position. If the price then drops below this point later, close the position.

### Advantage Analysis

This strategy has the following advantages:

1. Uses a custom indicator to identify market trends, which is more sensitive and accurate.
2. Only goes long, avoiding the unlimited loss risk of short selling.
3. Adopts the idea of trend trading, which is a classic trend following approach.
4. Provides dual stop loss methods, allowing free choice of the more suitable stop loss mode.
5. Simple and clear code, easy to understand and modify.
6. No need to set dynamic take profit, avoiding premature profit taking leading to lost profits.

### Risk Analysis

This strategy also has some risks:

1. Custom indicators may not be stable and reliable, with the risk of misjudgement.
2. Only establishing long positions may miss short-term pullback shorting opportunities.
3. Stop loss settings may be too conservative, unable to hold longer trending positions.
4. Lack of dynamic take profit requires timely manual profit taking, with operational risks.
5. Although both stop loss methods can be freely combined, the optimal stop loss point may still not be found.
6. Trend chasing strategies are prone to be misguided by ranging markets, producing excessive invalid trades.

### Optimization Directions

This strategy can be optimized from the following aspects:

1. Try other indicators, such as KDJ, MACD etc., to find more stable and reliable trend identification methods.
2. Increase shorting opportunities by allowing short positions when trends reverse, improving strategy profitability.
3. Optimize stop loss strategies by testing different parameters to find better stop loss points, or use ATR, MA etc. to set dynamic stops.
4. Add dynamic take profit, such as setting profit taking after breaking previous highs, reducing manual operation risks.
5. Conduct parameter optimization by adjusting MA periods, entry conditions etc. to find optimal parameter combinations.
6. Add filtering conditions like Only Long or bottom indicators to avoid invalid trades.
7. Test on different products to evaluate strategy effectiveness across major coin pairs and optimize applicability.
8. Utilize backtesting and demo trading to optimize parameters and stop loss/take profit points.

### Summary

Overall, this is a relatively simple trend chasing strategy. It uses a custom momentum indicator to judge market trends, establishes long positions at the start of trends, and provides dual stop loss methods. The main advantages are a clear strategy logic, limited risks, and ease of operation. But there is also room for optimization in areas like stop loss strategies and parameter selection. In general, this strategy provides a fundamental trend trading idea for the Cryptocurrency market, and is very suitable for beginners to learn and practice. But sufficient backtesting should still be conducted to validate its effectiveness and optimize further before applying it in live trading.

[/trans]

> Strategy Arguments

|Argument|Default|Descrip