<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Trix Simple Trend Following Strategy

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

The Trix simple trend following strategy is a straightforward trend-following approach based on the Trix indicator. It leverages the Trix indicator to identify price trends and incorporates moving averages to execute buy and sell decisions. This strategy is well-suited for medium to long-term trading, allowing traders to capitalize on significant market trends.

## Strategy Principle

This strategy primarily relies on the Trix indicator. The Trix indicator is a technical analysis tool designed to detect changes in price momentum. It computes the rate of change of a triple-smoothed exponential moving average of the price. A buy signal is generated when the Trix crosses above its moving average, while a sell signal occurs when it crosses below.

More specifically, the strategy calculates two distinct Trix indicators, labeled as Trix and Trix1, using different parameter sets: (7,4,4) for Trix and (4,4,4) for Trix1. Additionally, a 20-day simple moving average of the Trix is computed to form the "middle band."

A buy signal is triggered when the faster EMA13 crosses above the slower SMA68, and simultaneously, the Trix value falls below the middle band. The actual purchase is executed when Trix1 crosses above Trix. Positions are closed when the Trix line crosses back above the middle band.

Conversely, a sell signal arises when EMA13 crosses below SMA68, with the Trix positioned above the middle band. The sale is initiated upon a crossunder event between Trix1 and Trix. Closing the short position happens when Trix crosses back below the middle band.

## Strategy Advantages

This is a relatively simple yet effective trend-following strategy offering several benefits:

1. Utilizing the Trix indicator helps accurately identify price trends, thereby minimizing false signals.
2. Integrating both fast and slow moving averages enhances the determination of trend direction.
3. Employing two Trix indicators with varying parameters improves the reliability of generated signals.
4. The inclusion of a middle band acts as a filter, preventing excessive trades during range-bound market conditions.
5. Ideal for medium-to-long-term trend trading without being influenced by minor price fluctuations.
6. Straightforward to comprehend and apply, making it accessible even for novice traders.

## Strategy Risks

Despite its merits, the strategy presents certain risks that warrant attention:

1. During strong trending phases, the strategy might lag behind, potentially causing missed opportunities for profit capture.
2. In highly volatile markets, the Trix indicator could produce misleading signals leading to erroneous trades.
3. Poor management of positions based on fast/slow moving averages may exacerbate losses.
4. Absence of a defined stop-loss mechanism limits risk control per individual trade.
5. Incorrect parameter configurations might either increase transaction costs due to frequent trading or degrade signal accuracy.
6. Trading commissions and fees could erode part of the gains over time.

## Strategy Optimization Opportunities

Several enhancements can further refine this strategy:

1. Introduce robust stop-loss mechanisms such as trailing stops or Average True Range (ATR)-based stops to manage downside risks effectively.
2. Fine-tune the Trix parameters through optimization processes to discover superior combinations enhancing signal precision.
3. Incorporate supplementary indicators like MACD or Stochastic Oscillator (KDJ) to corroborate signals and mitigate false readings.
4. Adaptively modify the parameters of the fast and slow moving averages according to prevailing market dynamics for increased responsiveness.
5. Include trend strength metrics such as the Directional Movement Index (ADX) to avoid entering trades against dominant trends.
6. Implement regime-switching models distinguishing bullish from bearish environments, applying tailored parameter sets accordingly.
7. Improve entry timing by confirming trend initiation before initiating new positions.

## Summary

Overall, the Trix Simple Trend Following Strategy represents an easily implementable method for capturing medium-to-long-term market movements. By utilizing the Trix indicator alongside moving averages, it offers clear entry and exit points aligned with underlying price trends. While simple and user-friendly—particularly beneficial for newcomers—it does carry inherent risks requiring careful consideration. Through appropriate modifications and refinements, however, its performance can be significantly enhanced. Ultimately, this strategy serves as a foundational concept for those beginning their journey into systematic trend-based trading approaches.

||

## Overview

The Trix simple trend following strategy is a simple trend following strategy based on the Trix indicator. It uses the Trix indicator to judge price trends and combines moving averages to generate buy and sell signals. This strategy is suitable for medium-to-long term trading and can profit from larger trends.

## Strategy Logic 

This strategy is mainly based on the Trix indicator. The Trix indicator is a technical analysis tool that can identify price trend changes. It calculates the rate of change of prices through triple smoothed moving averages. When the Trix crosses above its moving average, it is a buy signal. When the Trix crosses below its moving average, it is a sell signal.

Specifically, this strategy first calculates two groups of Trix indicators with different parameters, named Trix and Trix1. The parameters for Trix are (7,4,4) and for Trix1 are (4,4,4). Then it calculates the 20-day simple moving average of Trix to get the middle band.

When the faster EMA13 crosses above the slower SMA68, and Trix is below the middle band, it is a buy signal. When Trix1 crosses above Trix, it triggers the buy. When Trix crosses back above the middle band, it closes the position. 

When EMA13 crosses below SMA68, and Trix is above the middle band, it is a sell signal. When Trix1 crosses below Trix, it triggers the sell. When Trix crosses back below the middle band, it closes the position.

## Advantages

This is a very simple trend following strategy with these advantages:

1. Using the Trix indicator can effectively identify price trends and reduce false signals.

2. Combining fast and slow moving averages helps determine trend direction. 

3. Using two Trix indicators with different parameters improves signal quality.

4. The middle band filter increases the filtering effect and avoids frequent opening during market oscillation.

5. It is suitable for medium-to-long term trend trading and is not disturbed by short-term fluctuations.

6. It is easy to understand and implement, suitable for beginners to learn.

## Risks

There are also some risks to note for this strategy:

1. It cannot catch trends in time during stable trends, missing some profits.

2. The Trix indicator may generate incorrect signals during huge market swings.

3. Improper fast and slow moving average position management can lead to greater losses. 

4. It lacks a stop loss strategy and cannot effectively control single losses.

5. Improper parameter settings may lead to too high trading frequency or poor signal quality.

6. Transaction fees may take up some profits.

## Optimization

This strategy can be optimized in the following aspects:

1. Add stop loss strategies like trailing stop loss or ATR stop loss to control single losses.

2. Optimize Trix parameters to find more suitable combinations and improve signal quality.

3. Add other indicator filters like MACD, KDJ etc. to avoid false signals. 

4. Dynamically adjust fast and slow moving average parameters based on market conditions to improve flexibility.

5. Add trend judging indicators like ADX to avoid trading against the trend.

6. Use different parameter sets to distinguish bull and bear markets.

7. Optimize entry timing and enter after trend confirmation.

## Conclusion

In summary, this is an easy to implement trend following strategy. It uses the Trix indicator to determine trend direction and generates trading signals in combination with moving averages. The advantages are its simplicity and ability to effectively track medium-to-long term trends, making it suitable for beginners to learn. But risks exist and need to be prevented. With proper optimizations, the strategy's effectiveness can be improved. Overall, it provides beginners with a simple and practical trend trading idea.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|7|lengtha|
|v_input_2|4|lengtha1|
|v_input_3|20|bb|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-07 00:00:00
end: 2023-10-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

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
Middle_Band = sma(Trix, bb)
sma68 = sma(close,68)
ema13 = sma(close,13)



longCondition = ema13>sma68 and Middle_Band>0 and Trix<Middle_Band
if (longCondition)
    strategy.entry("Buy", strategy.long, when = crossover(Trix1,Trix))
    strategy.exit("Buy", when = cross(Trix,Middle_Band))
    
    
shortCondition = ema13<sma68 and Middle_Band<0 and Trix>Middle_Band
if (shortCondition)
    strategy.entry("Sell", strategy.short, when = crossunder(Trix1,Trix))
    strategy.exit("Sell",when = cross(Trix,Middle_Band))
```

> Detail

https://www.fmz.com/strategy/428683

> Last Modified

2023-10-08 12:17:21