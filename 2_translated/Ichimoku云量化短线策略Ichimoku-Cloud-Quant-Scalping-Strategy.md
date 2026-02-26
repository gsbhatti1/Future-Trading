> Name

Ichimoku Cloud Quant Scalping Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1735a46dc0abe867cf1.png)
[trans]

## Overview

The Ichimoku Cloud Quant Scalping Strategy (Ichimoku-Cloud-Quant-Scalping-Strategy) is a short-term quantitative strategy that integrates the Ichimoku Cloud and Average Directional Index (ADX). It uses the Ichimoku Cloud to determine trend direction and ADX to filter non-trending markets for scalping during trending conditions.

## Strategy Logic

The strategy consists of two main components:

1. **Ichimoku Cloud to Judge Trend Direction**
    - Conversion Line: middle price of last 7 periods
    - Base Line: middle price of last 26 periods
    - Leading Span A: midpoint of Conversion Line and Base Line
    - Leading Span B: middle price of last 52 periods
    
    Price above the cloud indicates an uptrend, while below means a downtrend. The strategy uses the breakout of the Conversion Line to determine trend reversals.

2. **ADX to Filter Non-Trending Markets**
    Only generating trade signals when ADX is greater than 20, indicating a trending market. No trades are generated during range-bound markets.

Trade Rules:

- Long Entry: Price breaks above Conversion Line and ADX > 20
- Short Entry: Price breaks below Conversion Line and ADX > 20
- Stop Loss: 150 ticks
- Take Profit: 200 ticks

## Advantage Analysis

The advantages of this strategy include:

1. **Following the Trend, Avoiding Ranges**: Ichimoku Cloud can accurately determine trend direction and turning points. ADX filters range-bound markets to prevent false breakouts.
   
2. **Drawdown Control**: A 150-tick stop loss effectively limits per-trade losses.

3. **High Profit Factor**: With a take profit of 200 ticks versus a stop loss of 150 ticks, the profit factor is 1.33, making it easier to generate profits.

4. **Appropriate Trading Frequency**: Only trades during trending conditions prevent over-trading.

## Risk Analysis

This strategy also involves risks:

1. **Trend Determination Failure Risk**: Incorrect signals can occur if Ichimoku Cloud fails to detect trend reversals. Optimizing parameters may help improve accuracy.
   
2. **Stop Loss Being Hit Risk**: Stop losses may be penetrated during fast-moving markets. Trailing stop losses or wider stop loss ranges could mitigate this risk.

3. **Night and Pre-Market Trading Risks**: The default setting allows only day trading. Judgments may fail during extended hours. Enabling 24-hour trading or customizing strategies for extended sessions might address these risks.

## Optimization Directions

Potential optimization directions include:

1. Parameter Tuning of Ichimoku Cloud to find the optimal settings.
   
2. ADX parameter and threshold optimization to determine the best values.
  
3. Profit target and stop loss optimization based on historical data.

4. Implementing trailing stop losses to better follow trends.
  
5. Using additional indicators like MACD and KD to assist trend determination.

6. Adaptive optimization for different products.

## Conclusion

The Ichimoku Cloud Quant Scalping Strategy integrates the strengths of Ichimoku Cloud and ADX to accurately determine trend reversal points and filter out range-bound markets, offering a high profit factor and controllable drawdown. It is suitable for scalping along trends. Further improvements through parameter optimization, stop loss adjustments, and auxiliary indicators can enhance stability and profitability.

[/trans]

> Strategy Arguments


| Argument | Default | Description |
|----------|---------|-------------|
| v_input_1 | 7       | Conversion Periods: |
| v_input_2 | 14      | Length       |
| v_input_3 | 20      | threshold    |
| v_input_4 | true    | Use Trading Session? |
| v_input_5 | 0400-1500 | Trade Session: |
| v_input_6 | true    | Trade Size: |
| v_input_7 | 150     | Stop Loss in ticks: |
| v_input_8 | 200     | Take Profit in ticks: |

> Source (PineScript)

```pinescript
//@version=2
strategy(title='[STRATEGY][RS]Spot/Binary Scalper V0', shorttitle='IC', overlay=true, initial_capital=100000, currency=currency.USD)
//  ||  Adapted from:
//  ||      http://www.binaryoptionsedge.com/topic/1414-ta-spot-scalping-it-works-damn-good/?hl=singh

//  ||  Ichimoku cloud:
conversionPeriods = input(title='Conversion Periods:', defval=7, minval=1),
basePeriods = 26 // input(title='Base Periods', defval=26, minval=1)
laggingSpan2Periods = 52 // input(title='Lagging Span:', defval=52, minval=1),
displacement = 26 // input(title='Displacement:', defval=26, minval=1)

f_donchian(_len) => avg(lowest(_len), highest(_len))

f_ichimoku_cloud(_conversion_periods, _base_periods, _lagging_span)=>
    _conversion_line 