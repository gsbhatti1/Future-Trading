> Name

Hull Moving Average Swing Trading Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy is a short-term trading strategy based on the Hull Moving Average indicator. The strategy uses the golden cross and dead cross of the Hull Moving Average lines to generate trading signals, belonging to a trend-following strategy.

## Strategy Logic

This strategy is mainly based on the Hull Moving Average indicator. The Hull Moving Average line consists of two moving averages. First it calculates the median moving average line `nma` with a period of `hullperiod`. Then it calculates the fast moving average line `n2ma`, with a period of half of the `nma`. When `n2ma` crosses above `nma`, a buy signal is generated. When `n2ma` crosses below `nma`, a sell signal is generated.

To filter out some false signals, the strategy also introduces the Hull Line (`Hull_Line`). The Hull Line is a linear regression result of the difference between `nma` and `n2ma`. When there is divergence between the price and the Hull Line, the strategy will skip the trading signal. 

Specifically, the strategy rules are as follows:

1. Calculate the `nma`, with period `hullperiod`
2. Calculate the `n2ma`, with period half of the `nma` period 
3. Calculate the difference `diff` between `n2ma` and `nma`
4. Moving average the `diff` with period `sqrt(hullperiod)`, to get the Hull Line `Hull_Line`
5. When price crosses above `Hull Line`, a buy signal is generated
6. When price crosses below `Hull Line`, a sell signal is generated
7. If there is divergence between price and `Hull Line`, skip the signal
8. Enter with a certain percentage of the position, adopt exit stop loss

## Advantage Analysis

The advantages of this strategy include:

1. Based on Hull Moving Average, it can quickly capture the trend and follow the trend
2. Use Hull Line to filter false signals and improve signal quality
3. Good risk-reward ratio and drawdown, suitable for short-term trading
4. Flexible parameter tuning, adaptable to different market environments
5. Adopt reversal stop loss, can stop loss in time and control risks
6. Combine seasonality to avoid systemic risks in specific time periods

## Risk Analysis

This strategy also has some risks:

1. Trend following strategy, cannot trade all day long
2. Larger losses when trend reverses 
3. Lagging of moving averages, cannot timely capture turning points
4. High trading frequency leads to higher trading costs
5. Inappropriate parameter settings may lead to lower profitability in range-bound markets

To control these risks, we can take the following measures:

1. Adopt martingale stop loss strategy to control single loss
2. Optimize parameters and test robustness in different market environments 
3. Combine trend judging indicators to avoid chasing trends during reversals
4. Increase holding time to lower trading frequency

## Optimization Directions

This strategy can also be optimized in the following aspects:

1. Combine momentum indicators to locate the starting point of trends for better entry
2. Add machine learning models to assist in judging trend direction and strength
3. Adopt adaptive parameter setting to adjust parameters based on real-time market dynamics
4. Configure multi-timeframe Hull systems, with different position sizes for different timeframes
5. Combine volume indicators to avoid false breakouts with insufficient momentum
6. Add volatility-based position sizing model to dynamically adjust position sizes based on volatility

## Summary

The Hull Moving Average Swing Trading Strategy is an efficient short-term trend following strategy overall. It uses the Hull Moving Average system to determine the trend direction for the purpose of following the trend. Compared with single moving average systems, it has higher signal quality and parameters flexibility. The advantage of this strategy lies in quickly capturing trend changes with relatively small drawdowns. The weakness is the inability to cope with trend reversals. We can use parameter optimization, stop loss strategies, adding auxiliary models etc. to control risks and make the strategy robust in more market environments.

||

## Overview

This strategy is a short-term trading strategy based on the Hull Moving Average indicator. The strategy uses the golden cross and dead cross of the Hull Moving Average lines to generate trading signals, belonging to a trend-following strategy.

## Strategy Logic

This strategy is mainly based on the Hull Moving Average indicator. The Hull Moving Average line consists of two moving averages. First it calculates the median moving average line `nma` with a period of `hullperiod`. Then it calculates the fast moving average line `n2ma`, with a period of half of the `nma`. When `n2ma` crosses above `nma`, a buy signal is generated. When `n2ma` crosses below `nma`, a sell signal is generated.

To filter out some false signals, the strategy also introduces the Hull Line (`Hull_Line`). The Hull Line is a linear regression result of the difference between `nma` and `n2ma`. When there is divergence between the price and the Hull Line, the strategy will skip the trading signal. 

Specifically, the strategy rules are as follows:

1. Calculate the `nma`, with period `hullperiod`
2. Calculate the `n2ma`, with period half of the `nma` period 
3. Calculate the difference `diff` between `n2ma` and `nma`
4. Moving average the `diff` with period `sqrt(hullperiod)`, to get the Hull Line `Hull_Line`
5. When price crosses above `Hull Line`, a buy signal is generated
6. When price crosses below `Hull Line`, a sell signal is generated
7. If there is divergence between price and `Hull Line`, skip the signal
8. Enter with a certain percentage of the position, adopt exit stop loss

## Advantage Analysis

The advantages of this strategy include:

1. Based on Hull Moving Average, it can quickly capture the trend and follow the trend
2. Use Hull Line to filter false signals and improve signal quality
3. Good risk-reward ratio and drawdown, suitable for short-term trading
4. Flexible parameter tuning, adaptable to different market environments
5. Adopt reversal stop loss, can stop loss in time and control risks
6. Combine seasonality to avoid systemic risks in specific time periods

## Risk Analysis

This strategy also has some risks:

1. Trend following strategy, cannot trade all day long
2. Larger losses when trend reverses 
3. Lagging of moving averages, cannot timely capture turning points
4. High trading frequency leads to higher trading costs
5. Inappropriate parameter settings may lead to lower profitability in range-bound markets

To control these risks, we can take the following measures:

1. Adopt martingale stop loss strategy to control single loss
2. Optimize parameters and test robustness in different market environments 
3. Combine trend judging indicators to avoid chasing trends during reversals
4. Increase holding time to lower trading frequency

## Optimization Directions

This strategy can also be optimized in the following aspects:

1. Combine momentum indicators to locate the starting point of trends for better entry
2. Add machine learning models to assist in judging trend direction and strength
3. Adopt adaptive parameter setting to adjust parameters based on real-time market dynamics
4. Configure multi-timeframe Hull systems, with different position sizes for different timeframes
5. Combine volume indicators to avoid false breakouts with insufficient momentum
6. Add volatility-based position sizing model to dynamically adjust position sizes based on volatility

## Summary

The Hull Moving Average Swing Trading Strategy is an efficient short-term trend following strategy overall. It uses the Hull Moving Average system to determine the trend direction for the purpose of following the trend. Compared with single moving average systems, it has higher signal quality and parameters flexibility. The advantage of this strategy lies in quickly capturing trend changes with relatively small drawdowns. The weakness is the inability to cope with trend reversals. We can use parameter optimization, stop loss strategies, adding auxiliary models etc. to control risks and make the strategy robust in more market environments.

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|210|HullMA Period|
|v_input_2_open|0|Price data: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|true|From Month|
|v_input_4|true|From Day|
|v_input_5|2020|From Year|
|v_input_6|true|To Month|
|v_input_7|true|To Day|
|v_input_8|9999|To Year|

> Source (PineScript)

```pinescript
//@version=5
strategy("Hull Moving Average Swing Trading Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

hull_period = input.int(210, "HullMA Period")
price_data = input.source(close, "Price data: open|high|low|close|hl2|hlc3|hlcc4|ohlc4", type=input.source)
from_month = input.bool(true, "From Month")
from_day = input.bool(true, "From Day")
from_year = input.int(2020, "From Year")
to_month = input.bool(true, "To Month")
to_day = input.bool(true, "To Day")
to_year = input.int(9999, "To Year")

var float nma = na
var float n2ma = na
var float hull_line = na

nma := ta.sma(price_data, hull_period)
n2ma := ta.sma(price_data, hull_period / 2)

hull_line := ta.ema(ta.linear_reg_slope(ta.linear_reg(diff(n2ma - nma), length=sqrt(hull_period)), horizon=1), length=hull_period)

if (close > hull_line)
    strategy.entry("Buy", strategy.long)
    
if (close < hull_line)
    strategy.exit("Sell", "Buy")

if (not na(hull_line) and ta.crossover(n2ma, nma))
    strategy.entry("Buy", strategy.long)
    
if (not na(hull_line) and ta.crossunder(n2ma, nma))
    strategy.close("Buy")
```