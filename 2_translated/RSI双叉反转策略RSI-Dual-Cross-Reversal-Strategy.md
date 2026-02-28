> Name

RSI Double Fork Reversal Strategy RSI-Dual-Cross-Reversal-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10b768e77f595f1576d.png)

[trans]

### Overview

This strategy is a trend-following approach based on the dual cross reversal principle of the RSI indicator. It uses crossovers between RSI lines of different periods as buy and sell signals, while also incorporating RSI judgments to determine whether the current situation is overbought or oversold, thereby further confirming the validity of trading signals.

### Strategy Logic

The strategy primarily relies on two RSI lines with 5-day and 11-day periods. A buy signal is generated when the faster RSI (5-day line) breaks through the slower RSI (11-day line) upward while the 6-day RSI is below 30 at the same time; a sell signal is generated when the faster RSI breaks through the slower RSI downward while the 6-day RSI is above 70.

The strategy also draws horizontal lines at 30 and 70, with 30 representing the oversold area and 70 representing the overbought area. The basic idea behind the RSI indicator is that when in the overbought/oversold areas, it indicates that the asset may be over/under valued and suggests taking profits or waiting for a rebound opportunity. Therefore, this strategy includes judgments on the 6-day RSI to determine if it is in an oversold area, which helps filter out some false signals and improve signal reliability.

When buy and sell signals are generated, the strategy places long and short orders accordingly. Thus, it is a dual-directional trading strategy that can track both uptrends and downtrends.

### Advantages

1. High reliability due to the dual cross principle
2. Avoids false signals by incorporating multi-period RSI judgments
3. Suitable for dual directional trading, fitting trend following strategies
4. The RSI indicator is stable with significant optimization potential

### Risks and Solutions

1. Dual cross signals may be delayed and miss some price movements
   Solution: Shorten the faster RSI period parameter to make signals more sensitive

2. More false signals in trending markets
   Solution: Adjust overbought/oversold judgment parameters to avoid false signals in trends

3. Probability of RSI indicator divergence or failure
   Solution: Combine with other indicators to reduce the risk of sole RSI failure

### Optimization Directions

1. Period parameter optimization: Adjust faster and slower RSI periods, find optimal combinations
2. Overbought/Oversold parameter optimization: Adjust overbought/oversold parameters to improve signal accuracy
3. Combining with other indicators: Incorporate moving averages or volatility indicators for a comprehensive system

### Conclusion

This strategy is based on the dual cross reversal logic of RSI, making it a reliable trend-following approach. Its multi-period RSI design can help avoid certain false signals and thus has good practical outcomes. Through parameter optimization and indicator combinations, this strategy has potential for even better performance. Overall, the strategy has clear logic and strong practicality, making it worth key attention and further refinement.

|||

### Overview

This strategy is a trend-following approach based on the dual cross reversal principle of the RSI indicator. It uses crossovers between RSI lines of different periods as buy and sell signals, while also incorporating RSI judgments to determine whether the current situation is overbought or oversold, thereby further confirming the validity of trading signals.

### Strategy Logic

The strategy mainly relies on two RSI lines with 5-day and 11-day periods. A buy signal is generated when the faster RSI (5-day line) breaks through the slower RSI (11-day line) upward while the 6-day RSI is below 30; a sell signal is generated when the faster RSI breaks through the slower RSI downward while the 6-day RSI is above 70.

The strategy also draws horizontal lines at 30 and 70, with 30 representing the oversold area and 70 representing the overbought area. The basic idea behind the RSI indicator is that when in the overbought/oversold areas, it means the asset may be over/under valued and suggests taking profits or waiting for a rebound opportunity. Therefore, this strategy includes judgments on the 6-day RSI to determine if it is in an oversold area, which helps filter out some false signals and improve signal reliability.

When buy and sell signals are generated, the strategy places long and short orders accordingly. So, it is a dual-directional trading strategy that can track both uptrends and downtrends.

### Advantages

1. High reliability due to the dual cross principle
2. Avoids false signals by incorporating multi-period RSI judgments
3. Suitable for dual directional trading, fitting trend following strategies
4. The RSI indicator is stable with significant optimization potential

### Risks and Solutions

1. Dual cross signals may be delayed and miss some price movements
   Solution: Shorten the faster RSI period parameter to make signals more sensitive

2. More false signals in trending markets
   Solution: Adjust overbought/oversold judgment parameters to avoid false signals in trends

3. Probability of RSI indicator divergence or failure
   Solution: Combine with other indicators to reduce the risk of sole RSI failure

### Optimization Directions

1. Period parameter optimization: Adjust faster and slower RSI periods, find optimal combinations
2. Overbought/Oversold parameter optimization: Adjust overbought/oversold parameters to improve signal accuracy
3. Combining with other indicators: Incorporate moving averages or volatility indicators for a comprehensive system

### Conclusion

This strategy is based on the dual cross reversal logic of RSI, making it a reliable trend-following approach. Its multi-period RSI design can help avoid certain false signals and thus has good practical outcomes. Through parameter optimization and indicator combinations, this strategy has potential for even better performance. Overall, the strategy has clear logic and strong practicality, making it worth key attention and further refinement.

|||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|5|MA 1|
|v_input_2|11|MA 1|
|v_input_3|6|MA 1|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-15 00:00:00
end: 2023-11-21 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © email_analysts
// This code gives indication on the chart to go long or short based on RSI crossover strategy.
// Default values have been taken as 5 and 11, with 6 being used to identify highs & lows.
//@version=4
strategy("RSITrendStrategy", overlay=false)
len1 = input(title="MA 1", defval = 5)
len2 = input(title="MA 1", defval = 11)
len3 = input(title="MA 1", defval = 6)

h1 = hline(30.)
h2 = hline(70.)
///fill(h1, h2, color = color.new(color.blue, 80))
sh = rsi(close, len1)
ln = rsi(close, len2)
rs = rsi(close, len3)
p1 = plot(sh, color = color.red)
p2 = plot(ln, color = color.green)
p3 = plot(rs, color = color.white)

mycol = sh > ln ? color.lime : color.red
fill(p1, p2, color = mycol)

buy = (sh[1] < ln[1] and sh > ln and rs[1] < 30) 
if (buy)
    strategy.entry("long", strategy.long)

sell = (sh[1] > ln[1] and sh < ln and rs[1] > 70)
if (sell)
    strategy.entry("short", strategy.short)
```

> Detail

https://www.fmz.com/strategy/432885

> Last Modified

2023-11-22 14:59:07