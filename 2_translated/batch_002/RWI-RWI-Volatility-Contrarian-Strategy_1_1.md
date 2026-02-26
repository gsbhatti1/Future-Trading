<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RWI Volatility Contrarian Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/172c13c696da25da589.png)
[trans]
### Overview

The RWI Volatility Contrarian Strategy determines whether the market is in a reversal state by calculating the RWI highs and RWI lows over a certain period, to identify reversal opportunities. It employs a contrarian strategy—going short at highs and long at lows—in hopes of profiting from such moves.

### Strategy Principle  

This strategy first calculates the RWI highs and lows over a specified length period (e.g., 14 candles). The calculation formulas for RWI highs and lows are as follows:

RWI High = (High - Lowest Low N periods ago) / (ATR of N periods * sqrt(N))

RWI Low = (Highest High N periods ago - Low) / (ATR of N periods * sqrt(N))

Next, it calculates the difference between the RWI highs/lows and a threshold to determine if they fall below the threshold (e.g., 1). If both RWI highs and lows are below the threshold, the market is judged to be in a ranging condition, and no action is taken.

If the RWI high exceeds the RWI low by more than the threshold, it suggests an upcoming reversal, prompting consideration for short positions. Conversely, if the RWI low exceeds the RWI high by more than the threshold, it indicates a potential reversal, suggesting consideration for long positions. Thus, a contrarian trading strategy based on the RWI indicator for determining market reversal states is formed.

### Advantages Analysis

The RWI Volatility Contrarian Strategy offers several advantages:

1. Accurate identification of reversal points using the RWI indicator results in higher win rates.
2. Utilizing a contrarian approach suits ranging market conditions.
3. Clear and understandable strategy logic allows for flexible parameter adjustments.
4. Configurable short and long cycle judgments improve signal quality.

### Risk Analysis 

However, the RWI Volatility Contrarian Strategy also presents certain risks:

1. Reversal signals might result in false breakouts, causing losses.
2. During trending markets, numerous reversal signals may lead to losses.
3. Inappropriate RWI parameter settings could degrade signal quality.
4. Expanding volatility may render the RWI indicator ineffective.

To mitigate these risks, one can appropriately adjust RWI parameters, configure filter conditions, and limit the scope of reversals.

### Optimization Directions  

The RWI Volatility Contrarian Strategy can be further optimized in the following aspects:

1. Incorporate dual timeframe analysis with configurable short and long-period RWI indicators to enhance signal quality.
2. Combine with other indicators like KD and MACD to prevent false breakouts.
3. Implement stop-loss strategies to strictly control individual losses.
4. Dynamically optimize RWI parameters to adapt to changing market conditions.
5. Optimize position management by adjusting positions based on market status.

### Conclusion  

Overall, the RWI Volatility Contrarian Strategy has clear logic, utilizing the RWI indicator to judge reversal timing. Its trading logic performs well, especially in range-bound markets. Through parameter optimization and risk control measures, this strategy can be applied more stably and efficiently.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|Threshold|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// Copyright (c) 2020-present, JMOZ (1337.ltd)
strategy("RWI Strategy", overlay=false)


length = input(title="Length", type=input.integer, defval=14, minval=1)
threshold = input(title="Threshold", type=input.float, defval=1.0, step=0.1)


rwi(length, threshold) =>
    rwi_high = (high - nz(low[length])) / (atr(length) * sqrt(length))
    rwi_low = (nz(high[length]) - low) / (atr(length) * sqrt(length))
    is_rw = rwi_high < threshold and rwi_low < threshold
    [is_rw, rwi_high, rwi_low]


[is_rw, rwi_high, rwi_low] = rwi(length, threshold)


long = not is_rw and rwi_high > rwi_low
short = not is_rw and rwi_low > rwi_high


strategy.entry("Long", strategy.long, when=long)
strategy.entry("Short", strategy.short, when=short)


plot(rwi_high, title="RWI High", linewidth=1, color=is_rw?color.gray:color.blue, transp=0)
plot(rwi_low, title="RWI Low", linewidth=1, color=is_rw?color.gray:color.red, transp=0)

```

> Detail

https://www.fmz.com/strategy/440724

> Last Modified

2024-02-01 14:56:58