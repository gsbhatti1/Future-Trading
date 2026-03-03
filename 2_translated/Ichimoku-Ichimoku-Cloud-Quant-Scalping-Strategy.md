> Name

Ichimoku Cloud Quantitative Short-term Strategy Ichimoku-Cloud-Quant-Scalping-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1735a46dc0abe867cf1.png)
[trans]

## Overview

The Ichimoku Cloud Quantitative Short-term Strategy (Ichimoku-Cloud-Quant-Scalping-Strategy) is a short-term quantitative strategy that integrates the Ichimoku Cloud and Average Directional Index (ADX). It uses the Ichimoku Cloud to determine trend direction, combined with the ADX to filter non-trending markets for scalping during trending conditions.

## Strategy Logic

The strategy consists of two main components:

1. **Ichimoku Cloud to Judge Trend Direction**

    - Conversion Line: Middle price of the last 7 periods
    - Base Line: Middle price of the last 26 periods
    - Leading Span A: Midpoint between the Conversion Line and Base Line
    - Leading Span B: Middle price of the last 52 periods

    Prices above the cloud indicate an uptrend, while prices below it indicate a downtrend. The strategy uses the breakout of the Conversion Line to determine trend reversals.

2. **ADX to Filter Non-trending Markets**

    Only taking signals when ADX is greater than 20, indicating a trending market. No trades are placed when ADX < 20 during range-bound markets.
    
Trade Rules:

- Long Entry: Price breaks above Conversion Line and ADX > 20
- Short Entry: Price breaks below Conversion Line and ADX > 20  
- Stop Loss: 150 ticks  
- Take Profit: 200 ticks

## Advantage Analysis

The advantages of this strategy include:

1. **Following the Trend, Avoiding Ranges**: The Ichimoku Cloud can accurately determine trend directions and turning points, while ADX filters range-bound markets to prevent false breakouts.

2. **Drawdown Control**: A stop loss set at 150 ticks effectively limits per trade losses.

3. **High Profit Factor**: With a take profit of 200 ticks compared to a stop loss of 150 ticks, the profit factor is 1.33, making it easier to gain profits.

4. **Appropriate Trading Frequency**: The strategy only trades during trending conditions, preventing over-trading.

## Risk Analysis

The risks associated with this strategy include:

1. **Trend Determination Failure Risk**: Incorrect signals can occur if the Ichimoku Cloud fails to detect trend reversals. Optimizing parameters may help improve accuracy.

2. **Stop Loss Being Hit Risk**: In fast markets, stop losses can be penetrated. Using trailing stop loss or widening the stop loss range could mitigate this risk.

3. **Night and Pre-market Trading Risks**: The default setting only allows day trading; extended hours trading may fail to yield accurate signals. Enabling 24-hour trading or customizing strategies for night and pre-market sessions could address these risks.

## Optimization Directions

The potential optimization directions include:

1. **Ichimoku Cloud Parameter Tuning** to find the optimal settings.
  
2. **ADX Parameter and Threshold Optimization** to determine the best values.
  
3. **Profit Target and Stop Loss Optimization** based on historical data.

4. **Trailing Stop Loss** to better follow trend profits.  

5. **Additional Indicators Like MACD and KD** to assist in trend determination.

6. **Adaptive Optimization for Different Products** to tailor strategies to different markets.

## Conclusion

The Ichimoku Cloud Quantitative Short-term Strategy integrates the advantages of both the Ichimoku Cloud and ADX, allowing for accurate identification of trend reversal points while effectively filtering out range-bound markets. With high profit factors and controllable drawdowns, it is suitable for short-term trading along trends. Further improvements through parameter optimization, stop loss adjustments, and auxiliary indicators can enhance strategy stability and profitability.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|7|Conversion Periods:|
|v_input_2|14|Length|
|v_input_3|20|Threshold|
|v_input_4|true|Use Trading Session?|
|v_input_5|0400-1500|Trading Session:|
|v_input_6|true|Trade Size:|
|v_input_7|150|Stop Loss in Ticks:|
|v_input_8|200|Take Profit in Ticks:|


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