> Name

Trix Simple Trend Following Strategy Trix-Simple-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description


## Overview

The Trix simple trend following strategy is a straightforward trend-following strategy based on the Trix indicator. It utilizes the Trix indicator to assess price trends and employs moving averages for buy and sell signals. This strategy is suitable for medium-to-long-term trading, enabling gains during larger trends.

## Strategy Logic 

This strategy primarily relies on the Trix indicator. The Trix indicator is a technical analysis tool designed to identify price trend changes by calculating the rate of change through triple smoothed moving averages. When the Trix crosses above its moving average, it generates a buy signal; when it crosses below its moving average, it signals a sell.

Specifically, this strategy first calculates two sets of Trix indicators with different parameters: named Trix and Trix1. The parameters for Trix are (7,4,4), while those for Trix1 are (4,4,4). Then the 20-day simple moving average is calculated for Trix to form a middle band.

When EMA13 crosses above SMA68, and Trix remains below the middle band, it triggers a buy signal. When Trix1 crosses above Trix, this further confirms the buy decision. Closing occurs when Trix recrosses above the middle band.

Conversely, if EMA13 crosses below SMA68, and Trix is above the middle band, it generates a sell signal. Trix1 crossing below Trix triggers the sell. Positions are closed when Trix re-crosses below the middle band.

## Advantages

This simple trend-following strategy has several advantages:

1. Using the Trix indicator effectively identifies price trends and reduces false signals.
2. Combining fast and slow moving averages aids in determining trend direction.
3. Utilizing two sets of Trix indicators with different parameters enhances signal quality.
4. The middle band filter increases filtering effectiveness, avoiding frequent openings during market oscillation.
5. It is suitable for medium-to-long-term trading, minimizing interference from short-term fluctuations.
6. Easy to understand and implement, making it ideal for beginners.

## Risks

Some risks associated with this strategy should be noted:

1. In stable trends, the strategy may fail to catch full trend gains.
2. During significant market swings, Trix signals might be incorrect.
3. Improper management of fast and slow moving averages can exacerbate losses.
4. Lack of a stop-loss mechanism limits control over single trades' losses.
5. Incorrect parameter settings could result in overly frequent trading or low-quality signals.
6. Transaction fees may reduce overall profits.

## Optimization

The strategy can be optimized through the following aspects:

1. Incorporating trailing stop loss or ATR-based stop loss to manage single trade risks.
2. Refining Trix parameters to find more effective combinations and improve signal quality.
3. Adding additional indicator filters, such as MACD or KDJ, to reduce false signals.
4. Dynamically adjusting fast and slow moving average settings based on market conditions for greater flexibility.
5. Introducing trend confirmation indicators like ADX to avoid trading against the trend.
6. Using different parameter sets to differentiate between bull and bear markets.
7. Optimizing entry timing by confirming trends before initiating trades.

## Conclusion

Overall, this Trix simple trend following strategy is a straightforward approach that leverages the Trix indicator in conjunction with moving averages for generating buy and sell signals. Its simplicity and effectiveness make it suitable for medium-to-long-term trading, particularly appealing to beginners. However, there are inherent risks that must be managed. With appropriate optimization, the strategy's performance can be significantly enhanced. This provides a practical trend trading idea for new traders.

---

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|7|lengtha|
|v_input_2|4|lengtha1|
|v_input_3|20|bb|

> Source (PineScript)

```pinescript
//@version=3
strategy("Trix simple", overlay=true)

///_____________Made by Zan______//
// All thanks to Nmike's Chat, go visit there lol, you'll learn a lot.//

//Length setting
lengtha = input(7, minval=1)
lengtha1 = input(4, minval=1)
Trix = 10000 * change(ema(ema(ema(log(close), lengtha), lengtha), lengtha)) // TRIX 5
Trix1= 10000 * change(ema(ema(ema(log(close), lengtha1), lengtha1), lengtha1)) // TRIX 3
bb = input(20)
MiddleBand = sma(Trix, bb)
```