> Name

KDJ阳线突破买入策略KDJ-Golden-Cross-Long-Entry-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/112e7b7a7509279d403.png)
[trans]
### Overview

The KDJ Golden Cross Long Entry Strategy is a quantitative trading strategy based on the KDJ indicator. This strategy mainly uses the golden cross of the J line and D line of the KDJ indicator to generate buy signals, going long when the J line crosses above the D line. The strategy is relatively simple and easy to implement, suitable for beginners of quantitative trading.

### Strategy Logic

The main technical indicator used in this strategy is the KDJ indicator. KDJ consists of the K line, D line, and J line where:

- **K** = (Current Close - Lowest Low over the past N days) ÷ (Highest High over the past N days - Lowest Low over the past N days) x 100;
- **D** = M-day moving average of K;  
- **J** = 3K - 2D.

According to the KDJ rules, when J crosses above D, it signals a buy opportunity as prices are reversing upward. Conversely, if J falls below D, it suggests a sell signal due to a price reversal downward. 

This strategy uses these rules and generates buy signals when the J line crosses above the D line, i.e., a golden cross forms, triggering long positions. The exit condition is when J goes above 100, closing out long positions.

### Advantages

1. Using KDJ to determine entry timing incorporates price fluctuations reliably.
2. The strategy has clear and simple rules that are easy to understand and implement, suitable for beginners.
3. Stop profit and stop loss mechanisms effectively control risks.
4. Large flexibility in parameter optimization offers room for customization.

### Risks  

1. KDJ can generate false signals leading to potential losses.
2. Market short-term adjustments after buying may trigger stop losses, missing larger trends.
3. Improper parameters could result in excessive trading or unclear signals.
4. Transaction costs might affect overall profitability.

Main risk management methods: Proper parameter optimization, tracking index enhancements, and appropriately expanding the stop loss range.

### Optimization Directions 

1. Optimize KDJ parameters to find the best combination.
2. Add filtering conditions to avoid false signals by combining with other indicators or formations.
3. Adjust parameters based on market conditions (bull/bear markets).
4. Appropriately expand stop losses to reduce exit frequency.
5. Integrate trading volume analysis to prevent being trapped.

### Summary

The KDJ Golden Cross Long Entry Strategy is simple and practical, easy for beginners to implement, particularly suitable for quantitative traders. While it offers certain advantages, risks must be managed through targeted optimization to fully leverage the strategy’s potential. Overall, this strategy warrants in-depth study and application.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|period|
|v_input_2|3|signal|
|v_input_float_1|1.2|Profit Margin|
|v_input_float_2|0.98|Stop Loss Margin|
|v_input_int_1|true|Start Date|
|v_input_int_2|true|Start Month|
|v_input_int_3|2023|Start Year|
|v_input_int_4|true|End Date|
|v_input_int_5|true|End Month|
|v_input_int_6|2024|End Year|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-01-25 00:00:00
end: 2024-01-31 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// ## !<------------------ Script --------------------------> 
//@version=5
strategy('KDJ NVDA', shorttitle='KDJ')

ilong = input(9, title='period')
isig = input(3, title='signal')

bcwsma(s, l, m) =>
    _bcwsma = float(na)
    _s = s
    _l = l
    _m = m
    _bcwsma := (_m * _s + (_l - _m) * nz(_bcwsma[1])) / _l
    _bcwsma

// profit strategy add
profit_m = input.float(1.20, "Profit Margin", minval=1.0, maxval=1.99, step=0.05)
stop_m = input.float(0.98, "Stop Loss Margin", minval=0.0, maxval=1.0, step=0.05)

// Make input options that configure backtest date range
startDate = input.int(title="Start Date", defval=1, minval=1, maxval=31)
startMonth = input.int(title="Start Month", defval=1, minval=1, maxval=12)
startYear = input.int(title="Start Year", defval=2023, minval=2018, maxval=2024)
endDate = input.int(title="End Date", defval=1, minval=1, maxval=31)
endMonth = input.int(title="End Month", defval=1, minval=1, maxval=12)
endYear = input.int(title="End Year", defval=2024, minval=2018, maxval=2099)

// intialization of variables
// Look if the close time of the current bar
// falls inside the date range
inDateRange = (time >= timestamp(syminfo.timezone, startYear, startMonth, startDate, 0, 0)) and (time < timestamp(syminfo.timezone, endYear, endMonth, endDate, 0, 0))

c = close
h = ta.highest(high, ilong)
l = ta.lowest(low, ilong)
j = (3 * c - 2 * d) / 1.0
d = bcwsma(c, l, isig)

// Conditions for entering long positions based on the golden cross condition
longCondition = j > d and inDateRange

if (longCondition)
    strategy.entry("Golden Cross Long", strategy.long)

stopLossPrice = c * stop_m
takeProfitPrice = c * profit_m

trailStop = max(stopLossPrice, strategy.position_avg_price)
strategy.exit("Trail Stop Loss", from_entry="Golden Cross Long", limit=takeProfitPrice, trail_offset=trailStop - strategy.position_avg_price)

// Plot the KDJ lines
plot(j, color=color.red, title='J Line')
plot(d, color=color.blue, title='D Line')

```
```