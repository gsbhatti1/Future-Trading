> Name

Momentum-Breakout-Identifies-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/165c87312bbfd12f475.png)
[trans]

## Overview

This strategy identifies rapidly rising stocks and takes long positions when price breaks out new highs. It uses a fixed percentage take profit to lock in profits. The strategy belongs to trend following strategies.

## Principle 

The strategy is mainly based on two indicators:

1. Fast RSI: It calculates the rise and fall of recent 3 bars to judge price momentum. When fast RSI is below 10, it is considered oversold status.

2. Body filter: It calculates the average body size of recent 20 bars. When the body size is larger than 2.5 times of average body, it is considered a valid breakout.

When fast RSI is below 10 and body filter is valid, a long position will be opened. After that, a fixed take profit of 20% is set. When price exceeds the open price * (1 + take profit percentage), the position will be closed.

The advantage of this strategy is it can capture breakout opportunities at the beginning of trends. The fast RSI judges oversold levels and body filter avoids false breakouts. The fixed percentage take profit locks in profits of each trade and keeps catching the trend.

## Advantage Analysis

The advantages of this strategy:

1. Fast RSI identifies oversold levels and increases entry accuracy.
2. Body filter avoids false breakouts caused by fluctuations.
3. Fixed percentage take profit realizes stable profits and catches trends.
4. The logic is simple and clear, easy to understand and implement.
5. Elegant code structure with great extensibility, easy to optimize.
6. Stable positive returns and high win rate in backtest.

## Risk Analysis

Some risks to note:

1. No stop loss mechanism, risks of expanding losses.
2. Improper take profit levels may lead to premature or too deep exit.
3. Consecutive small losses may occur in choppy markets.
4. Financing costs are not considered, actual returns may be lower.
5. Insufficient parameter optimization across different products.

## Optimization Directions

Some aspects can be optimized:

1. Add stop loss to control single trade loss.
2. Optimize dynamic take profit to follow trends.
3. Enhance breakout logic to improve entry accuracy.
4. Add position sizing module to optimize capital usage.
5. Add parameter optimization module for different products.
6. Add filters to avoid losses in choppy markets.
7. Consider adding average cost management.

## Conclusion

In summary, this is an elegant and simple trend following strategy. It uses fast RSI to identify oversold levels, body filter to confirm valid breakout, and fixed percentage take profit to generate steady returns. Although there are rooms for optimization, the strategy is responsive and suitable for fast changing markets, making it a very practical trading strategy. With continuous optimizations, it can become a robust long term strategy.

||

## Overview

This strategy identifies rapidly rising stocks and takes long positions when price breaks out new highs. It uses fixed percentage take profit to lock in profits. The strategy belongs to trend following strategies.

## Principle 

The strategy is mainly based on two indicators:

1. Fast RSI: It calculates the rise and fall of recent 3 bars to judge price momentum. When fast RSI is below 10, it is considered oversold status.
2. Body filter: It calculates the average body size of recent 20 bars. When the body size is larger than 2.5 times of average body, it is considered a valid breakout.

When fast RSI is below 10 and body filter is valid, a long position will be opened. After that, a fixed take profit of 20% is set. When price exceeds the open price * (1 + take profit percentage), the position will be closed.

The advantage of this strategy is it can capture breakout opportunities at the beginning of trends. The fast RSI judges oversold levels and body filter avoids false breakouts. The fixed percentage take profit locks in profits of each trade and keeps catching the trend.

## Advantage Analysis

The advantages of this strategy:

1. Fast RSI identifies oversold levels and increases entry accuracy.
2. Body filter avoids false breakouts caused by fluctuations.
3. Fixed percentage take profit realizes stable profits and catches trends.
4. The logic is simple and clear, easy to understand and implement.
5. Elegant code structure with great extensibility, easy to optimize.
6. Stable positive returns and high win rate in backtest.

## Risk Analysis

Some risks to note:

1. No stop loss mechanism, risks of expanding losses.
2. Improper take profit levels may lead to premature or too deep exit.
3. Consecutive small losses may occur in choppy markets.
4. Financing costs are not considered, actual returns may be lower.
5. Insufficient parameter optimization across different products.

## Optimization Directions

Some aspects can be optimized:

1. Add stop loss to control single trade loss.
2. Optimize dynamic take profit to follow trends.
3. Enhance breakout logic to improve entry accuracy.
4. Add position sizing module to optimize capital usage.
5. Add parameter optimization module for different products.
6. Add filters to avoid losses in choppy markets.
7. Consider adding average cost management.

## Conclusion

In summary, this is an elegant and simple trend following strategy. It uses fast RSI to identify oversold levels, body filter to confirm valid breakout, and fixed percentage take profit to generate steady returns. Although there are rooms for optimization, the strategy is responsive and suitable for fast changing markets, making it a very practical trading strategy. With continuous optimizations, it can become a robust long term strategy.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|TAKE PROFIT %|
|v_input_2|2019|BACKTEST START YEAR|
|v_input_3|true|BACKTEST START MONTH|
|v_input_4|true|BACKTEST START DAY|


> Source (PineScript)

```pinescript
//@version=4
// this is based on https://www.tradingview.com/v/PbQW4mRn/
strategy(title = "ONLY LONG V4 v1", overlay = true, initial_capital = 1000, pyramiding = 1000,
   calc_on_order_fills = false, calc_on_every_tick = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 50, commission_value = 0.075)

// study(title = "ONLY LONG V4 v1", overlay = true)

// Fast RSI
src = close
fastup = rma(max(change(src), 0), 3)
fastdown = rma(-min(change(src), 0), 3)
fastrsi = fastdown == 0 ? 100 : fastup == 0 ? 0 : 100 - (100 / (1 + fastup / fastdown))

// Body Filter
body = abs(close - open)
abody = sma(body, 20)

mac = sma(close, 20)
len = abs(close - mac)
sma = sma(len, 100)
max = max(open, close)
min = min(open, close)
up = close < open and len > sma * 2 and min < min[1] and fastrsi < 10 and body > abody * 2.5

// Strategy
// ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░