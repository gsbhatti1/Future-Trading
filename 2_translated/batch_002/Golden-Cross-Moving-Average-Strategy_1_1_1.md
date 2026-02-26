<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

A Trend Following Strategy Based on Moving Average Golden Cross - Golden-Cross-Moving-Average-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/7a2d874bcdcf935225.png)
 [trans]
## Overview

The Golden Cross Moving Average strategy is a trend-following strategy based on moving averages. It determines market trend direction by calculating moving averages over different periods, and generates trading signals accordingly. Specifically, this strategy calculates three moving averages: the 50-day, 100-day, and 200-day lines. A buy signal is generated when the short-term moving average breaks upward through the long-term moving average; a sell signal is generated when the short-term moving average breaks downward through the long-term moving average.

## Strategy Principle  

The core signal of this strategy originates from the golden cross of moving averages. The so-called golden cross occurs when the short-term moving average breaks upward through the long-term moving average, signaling that the market has entered a bullish trend. This strategy uses the 50-day line as the short-term moving average and the 200-day line as the long-term moving average, buying when the two averages form a golden cross; it uses the 50-day line as the short-term average and the 100-day line as the long-term average, selling when the short-term average crosses below the long-term average, completing one trading cycle.

By setting moving averages with different parameters, the strategy can better capture turning points in market trends. Short-term moving averages respond more quickly to price changes, reflecting recent price movements; long-term moving averages are less sensitive to short-term fluctuations and can identify the main trend direction. A golden cross between these two averages can effectively confirm a trend reversal and generate a trading signal.

## Advantages of the Strategy

This strategy offers the following advantages:

1. Strong trend-following ability. The dual moving average strategy can align with major market trends, avoiding interference from short-term market noise, thus demonstrating strong trend-following capabilities.

2. Clear trading signals. The strategy relies entirely on the relationship between moving averages to generate signals, making signal generation and interpretation straightforward and direct, minimizing subjective judgment errors.

3. Easy to backtest. As a typical trend-following strategy, it can be quickly backtested to assess performance.

4. High scalability potential. Parameters such as moving average settings, trading instruments, and timeframes can all be optimized and expanded to find better parameter combinations.

## Risk Analysis

This strategy also carries certain risks:

1. Missing turning points. Moving averages inherently have a lag, which prevents accurate identification of key turning points and may result in missing optimal buying opportunities.

2. False bullish signals. Multiple short-term golden crosses might produce false signals, leading investors to misjudge the market.

3. Sudden event risk. Major unexpected events can cause severe market fluctuations that moving average strategies struggle to handle.

4. Market consolidation risk. During prolonged periods of sideways market movement, the strategy may generate numerous ineffective signals, leading to frequent trades with minimal overall returns.

These risks can be mitigated by adjusting moving average parameters, implementing stop-loss strategies, or combining the strategy with other indicators.

## Optimization Directions  

The strategy can be optimized in the following ways:

1. Optimize moving average parameters to find the best parameter combinations. Testing additional cycle parameters or introducing adaptive moving averages such as Triple Exponential Moving Average (TEMA) can help.

2. Incorporate stop-loss mechanisms to control individual trade losses. Trailing stops or percentage-based stops can prevent losses from escalating.

3. Combine with other indicators to filter signals. Signals from dual moving averages can be used alongside indicators such as volume or volatility to ensure trades are executed only under strong trending conditions.

4. Utilize machine learning techniques for strategy optimization. Algorithms can automatically search for better parameter combinations and trading rules, iteratively improving the strategy’s return potential.

## Summary

The Golden Cross Moving Average strategy identifies the primary market trend direction by analyzing the relationship between dual moving averages, aiming to capture mid-to-long-term trend opportunities. Its strengths lie in its clear and straightforward signal rules, ease of implementation and optimization, making it suitable for mid-to-long-term investors. However, it is essential to recognize the strategy’s inherent lag and potential for generating false signals, and adopt combined strategies and optimizations to mitigate associated risks.

||

## Overview

The Golden Cross Moving Average strategy is a trend-following strategy based on moving averages. It determines the market trend direction by calculating moving averages of different periods and generates trading signals accordingly. Specifically, it calculates the 50-day, 100-day, and 200-day moving averages. When the short-term moving average crosses above the long-term moving average, a buy signal is generated. When the short-term moving average crosses below the long-term moving average, a sell signal is generated.

## Strategy Logic

The core signal of this strategy comes from the golden cross of moving averages. The so-called golden cross refers to the short-term moving average crossing above the long-term moving average, indicating the market is entering a bullish trend. This strategy uses the 50-day moving average as the short-term MA and the 200-day moving average as the long-term MA. It buys when the two MAs form a golden cross and sells when the 50-day MA crosses below the 100-day MA to complete a trading cycle. 

By setting moving averages of different periods, we can better capture the inflection points of market trends. The short-term MA responds faster to price changes and reflects recent price movements. The long-term MA is insensitive to short-term fluctuations and can determine the primary trend direction. The golden cross formed between the two MAs can effectively confirm the trend reversal and generate trading signals.

## Advantage Analysis  

The advantages of this strategy are:

1. Strong trend following capability. The dual moving average strategy can follow the primary market trend, avoid being disturbed by short-term market noise, and has strong trend-following capability.

2. Clear trading signals. The strategy relies entirely on the relationship between moving averages to generate trading signals, making signal generation and interpretation very direct and unambiguous, avoiding subjective judgment errors.

3. Easy backtesting implementation. As a typical trend-following strategy, it can be quickly implemented for backtesting to evaluate the strategy's effectiveness. 

4. Great scalability. Parameters like moving average periods, trading products, and time frames can all be optimized and expanded to find better parameter combinations.

## Risk Analysis

The strategy also has some risks:

1. Missing inflection points. The inherent lagging of moving averages cannot accurately locate important inflection points and may miss the best buying opportunities.

2. Generating false bullish signals. There may be multiple golden crosses forming false signals in the short term, causing investors to make wrong judgements. 

3. Risks of sudden events. Major sudden events can cause drastic market fluctuations that moving average strategies may fail to cope with. 

4. Risks of range-bound markets. When the market is range-bound for an extended period, the strategy may generate excessive invalid signals, resulting in frequent trading but overall meager profitability.

These risks can be mitigated by adjusting moving average parameters, setting stop losses, or combining with other indicators. 

## Optimization Directions   

The strategy can be optimized in the following aspects:

1. Optimize moving average parameters to find the best combinations. More cycle parameters can be tested. Adaptive moving averages like triple exponential moving averages can also be introduced.

2. Add stop loss strategies to control single loss. Both trailing stop loss and proportional stop loss can avoid further loss expansion.

3. Combine other indicators to filter signals. Dual moving average signals can be combined with indicators like volume and volatility to ensure signals are only generated when the trend is strong.

4. Utilize machine learning techniques to optimize the strategy. The algorithms can automatically search for more optimal parameter sets and trading rules to continuously improve the strategy's profitability.

## Conclusion

The Golden Cross Moving Average strategy determines the primary market trend direction by calculating the relationship between dual moving averages, trying to capture mid-to-long term trend opportunities. The advantages are clear signal rules that are easy to implement and optimize. It is suitable for mid-to-long term investors. We should also note the lagging limitation and possible false signals of this strategy and take combination and optimization measures to mitigate potential risks.

[/trans]



> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy(title="MA Cross", overlay=true)
short = sma(close, 50)
short1 = sma(close[5], 50)
medium = sma(close, 100)
long = sma(close, 200)
long1 = sma(close[5], 200)

plot(short, color = color.red)
plot(long, color = color.green)
trendUp = (cross(short, long) and (long1 > short1) ? true : false)
x = if (trendUp)
    (long1 - short1)*5
else
    0
    
//start     = timestamp(2000, 01, 01, 00, 00)        // backtest start window
//finish    = timestamp(2020, 02, 09, 23, 59)        // backtest finish window
//window()  => time >= start and time <= finish ? true : false  

//strategy.entry("long", true, 1000, limit = high, when = window() and trendUp)
//strategy.close("long", when = window() and close < medium)

strategy.entry("long", true, 1, limit = high, when = trendUp)
strategy.close("long", when = close < medium)


```

> Detail

https://www.fmz.com/strategy/440074

> Last Modified

2024-01-26 14:23:55