> Name

Ichimoku-Kinko-Hyo Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/eb0c0c3e4e79b939b7.png)
[trans]

### Overview

The Ichimoku Kinko Hyo trading strategy is a trend-following strategy based on the Ichimoku technical indicator. It uses the conversion line, base line, leading span 1, and leading span 2 indicators to determine the direction of the trend and the timing of entry and exit.

### Strategy Logic

The strategy mainly judges the following four conditions to decide the trading direction:

1. Go long when the closing price crosses above the 26-period average of the top of the cloud.
2. Go short when the closing price crosses below the 26-period average of the bottom of the cloud.
3. Take profit condition: 3.5%.
4. Stop loss condition: 1.5%.

Specifically, the strategy first calculates the conversion line, base line, leading span 1, and leading span 2. It then determines whether to go long or short based on if the closing price breaks through the top or bottom of the cloud.

If the closing price crosses above the top of the cloud, i.e., above the 26-period average of the greater value between leading span 1 and leading span 2, it indicates an upward trend and goes long.

If the closing price crosses below the bottom of the cloud, i.e., below the 26-period average of the lower value between leading span 1 and leading span 2, it indicates a downward trend and goes short.

After entry, take profit and stop loss conditions are set. Take profit is set at 3.5% of the entry price, and stop loss is 1.5% of the entry price.

### Advantage Analysis

The Ichimoku Kinko Hyo trading strategy has the following advantages:

1. It can identify trend changes early and enter trends in a timely manner.
2. Using the cloud to determine support and resistance areas makes entries more accurate.
3. It considers both price and volume, avoiding false breakouts.
4. Clear profit-taking and stop-loss conditions help control trading risk.

### Risk Analysis

The Ichimoku Kinko Hyo trading strategy also has some risks:

1. In range-bound markets, it can produce multiple small losses.
2. A large stop loss may be triggered if the major trend reverses.
3. Multiple conditions need to be met for entry, reducing opportunities.
4. Incorrect parameter settings may misinterpret indicator signals.

Solutions:

1. Relax entry conditions to increase opportunities.
2. Optimize parameters to better fit market characteristics.
3. Add filters with other indicators to avoid false signals.

### Optimization Directions

The Ichimoku Kinko Hyo trading strategy can be optimized in the following aspects:

1. Optimize conversion line, base line, and other parameters to fit different period market conditions.
2. Optimize entry conditions to capitalize on more opportunities.
3. Optimize take-profit and stop-loss strategies for higher risk-adjusted returns.
4. Add filters with other indicators to reduce whipsaws.
5. Dynamically adjust position sizing based on market volatility.

### Summary

The Ichimoku Kinko Hyo trading strategy is an overall relatively good strategy that can capture potential trends in a timely manner. However, it still needs further optimization and combination with other indicators to form a robust trading system. By adjusting parameters, improving entry and exit techniques, and controlling risks, the Ichimoku strategy can achieve higher risk-adjusted returns in trending markets.

||

### Overview

The Ichimoku Kinko Hyo trading strategy is a trend-following strategy based on the Ichimoku technical indicator. It uses the conversion line, base line, leading span 1, and leading span 2 indicators to determine the direction of the trend and the timing of entry and exit.

### Strategy Logic

The strategy mainly judges the following four conditions to decide the trading direction:

1. Go long when the closing price crosses above the 26-period average of the top of the cloud.
2. Go short when the closing price crosses below the 26-period average of the bottom of the cloud.
3. Take profit condition: 3.5%.
4. Stop loss condition: 1.5%.

Specifically, the strategy first calculates the conversion line, base line, leading span 1 and leading span 2. It then determines whether to go long or short based on if the closing price breaks through the top or bottom of the cloud.

If the closing price crosses above the top of the cloud, i.e., above the 26-period average of the greater value between leading span 1 and leading span 2, it indicates an upward trend and goes long.

If the closing price crosses below the bottom of the cloud, i.e., below the 26-period average of the lower value between leading span 1 and leading span 2, it indicates a downward trend and goes short.

After entry, take profit and stop loss conditions are set. Take profit is set at 3.5% of the entry price, and stop loss is 1.5% of the entry price.

### Advantage Analysis

The Ichimoku Kinko Hyo trading strategy has the following advantages:

1. It can identify trend changes early and enter trends in a timely manner.
2. Using the cloud to determine support and resistance areas makes entries more accurate.
3. It considers both price and volume, avoiding false breakouts.
4. Clear profit-taking and stop-loss conditions help control trading risk.

### Risk Analysis

The Ichimoku Kinko Hyo trading strategy also has some risks:

1. In range-bound markets, it can produce multiple small losses.
2. A large stop loss may be triggered if the major trend reverses.
3. Multiple conditions need to be met for entry, reducing opportunities.
4. Incorrect parameter settings may misinterpret indicator signals.

Solutions:

1. Relax entry conditions to increase opportunities.
2. Optimize parameters to better fit market characteristics.
3. Add filters with other indicators to avoid false signals.

### Optimization Directions

The Ichimoku Kinko Hyo trading strategy can be optimized in the following aspects:

1. Optimize conversion line, base line and other parameters to fit different period market conditions.
2. Optimize entry conditions to capitalize on more opportunities.
3. Optimize take-profit and stop-loss strategies for higher risk-adjusted returns.
4. Add filters with other indicators to reduce whipsaws.
5. Dynamically adjust position sizing based on market volatility.

### Summary

The Ichimoku Kinko Hyo trading strategy is an overall relatively good strategy that can capture potential trends in a timely manner. However, it still needs further optimization and combination with other indicators to form a robust trading system. By adjusting parameters, improving entry and exit techniques, and controlling risks, the Ichimoku strategy can achieve higher risk-adjusted returns in trending markets.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|false|only shows buying Trade|
|v_input_2|9|Conversion Line Periods|
|v_input_3|26|Base Line Periods|
|v_input_4|52|Lagging Span 2 Periods|
|v_input_5|26|Displacement|
|v_input_6|3.5|enter target in % after entry|
|v_input_7|1.5|enter Stoploss in % after entry|


> Source (PineScript)

```pinescript
//@version=4
strategy("Ichimoku system", overlay=true, initial_capital = 100000, default_qty_type = strategy.percent_of_equity, default_qty_value=100)

buyOnly = input(false, "only shows buying Trade", type=input.bool)


conversionPeriods = input(9, minval=1, title="Conversion Line Periods"),
basePeriods = input(26, minval=1, title="Base Line Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span 2 Periods"),
displacement = input(26, minval=1, title="Displacement")

donchian(len) => avg(lowest(len), highest(len))

conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadingSpan1 = donchian(laggingSpan2Periods + displacement)
leadingSpan2 = donchian(laggingSpan2Periods - displacement)

cloudTop = max(leadinSpan1, leadingSpan2)
cloudBottom = min(leadingSpan1, leadingSpan2)

plot(conversionLine, color=color.blue, title="Conversion Line")
plot(baseLine, color=color.orange, title="Base Line")
plot(cloudTop, color=color.green, title="Cloud Top")
plot(cloudBottom, color=color.red, title="Cloud Bottom")

if (not buyOnly)
    longCondition = close > cloudTop
    shortCondition = close < cloudBottom

    if (longCondition)
        strategy.entry("Long", strategy.long)

    if (shortCondition)
        strategy.entry("Short", strategy.short)

takeProfitPercent = input(3.5, title="enter target in % after entry")
stopLossPercent = input(1.5, title="enter Stoploss in % after entry")

longTakeProfitPrice = strategy.position_avg_price * (1 + takeProfitPercent / 100)
shortTakeProfitPrice = strategy.position_avg_price * (1 - stopLossPercent / 100)

longStopLossPrice = strategy.position_avg_price * (1 - stopLossPercent / 100)
shortStopLossPrice = strategy.position_avg_price * (1 + takeProfitPercent / 100)

if (strategy.is_long)
    strategy.exit("Long Take Profit", "Long", limit=longTakeProfitPrice, stop=longStopLossPrice)

if (strategy.is_short)
    strategy.exit("Short Take Profit", "Short", limit=shortTakeProfitPrice, stop=shortStopLossPrice)
```

Note: The code block was provided in the original text and has been kept as is.