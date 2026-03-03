> Name

RSI Tracking ADX Strategy RSI-Tracking-ADX-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]


## Overview

The RSI Tracking ADX Strategy is a long-term trend-following strategy that combines the RSI and ADX indicators. This strategy uses the RSI indicator to determine whether the market is overbought or oversold, and the ADX indicator to assess the strength of the current trend. It allows for long positions when the trend is upward and not overbought, and exits when the trend weakens or becomes overbought.

## Strategy Principle

The strategy mainly uses a combination of RSI and ADX indicators to determine entry and exit conditions.

### Entry Conditions:
1. 20-day Simple Moving Average (SMA) is rising;
2. ADX has increased by more than 0.2 compared to the previous day, indicating strengthening trend;
3. RSI is below 85 to avoid overbought state;

Or:

1. 20-day SMA is rising;  
2. ADX is increasing but less than 0.2, indicating a mild trend;
3. RSI is below 50, with potential for rebound.

### Exit Conditions:
1. RSI exceeds 75, indicating overbought state;
2. ADX shows a minor increase, suggesting weak trend;

Or:

1. RSI exceeds 75, indicating overbought state;
2. ADX shows a sharp increase, indicating strong trend;

Or:

20-day SMA turns downward.

The strategy uses the RSI to determine overbought/oversold conditions and the ADX to assess trends. It aims to enter long positions during upward trends that are not overbought and exit when the trend weakens or becomes overbought, thereby following medium-to-long term uptrends.

## Strategy Advantages

The main advantages of this strategy include:

1. Combining RSI and ADX allows for more accurate determination of trends and overbought/oversold conditions, leading to precise entries and exits.
2. Using ADX to gauge trend strength can reduce false exits during consolidation periods.
3. Loose parameters in the RSI allow it to track medium-to-long term trends while reducing excessive trading.
4. The strategy is simple to operate and easy to implement, suitable for long-term holdings.
5. Flexible parameter configurations offer ample room for optimization.

## Strategy Risks

The main risks associated with this strategy are:

1. ADX lag can cause missing trend turning points, leading to larger losses.
2. Stop loss may be triggered late during cliff-like price drops, expanding losses.
3. RSI parameters set too loosely might result in prolonged overbought positions.
4. ADX parameters set too sensitively could lead to erroneous exits during weak trends.
5. Individual stocks may behave abnormally during market regime shifts.

### Risk Management

1. Use shorter ADX periods for sensitivity.
2. Set stricter stop losses to limit potential losses.
3. Shorten RSI periods to avoid prolonged overbought conditions.
4. Avoid overly sensitive ADX parameters.
5. Manually override the strategy during significant market shifts.

## Strategy Optimization

This strategy can be optimized by:

1. Testing different RSI period settings for better performance.
2. Optimizing ADX period combinations to enhance trend capturing ability.
3. Adding additional indicators like MACD for confirmation purposes.
4. Experimenting with moving average combinations to improve entry points.
5. Incorporating profit taking and stop loss strategies to boost the risk-reward ratio.
6. Judging market regimes to manually override during turning points.

## Conclusion

The RSI Tracking ADX Strategy is a relatively simple yet effective long-term trend-following strategy that combines the strengths of both RSI and ADX for accurate overbought/oversold analysis and trend determination. The logic is straightforward, easy to implement, and offers optimization flexibility. However, caution should be exercised regarding ADX lag and stop loss settings. Overall, this strategy is well-suited for tracking medium-to-long term trends and can provide stable returns.

||


## Summary 

The RSI Tracking ADX strategy is a trend following strategy that combines the RSI indicator and the ADX indicator. It uses the RSI indicator to determine overbought and oversold conditions, and the ADX indicator to gauge trend strength, allowing entries during uptrends when not overbought and exits when trends weaken or become overbought.

## Strategy Logic

The strategy mainly utilizes a combination of the RSI indicator and the ADX indicator to determine entries and exits.

### Entry Conditions:

1. 20-day SMA is rising;

2. ADX has increased by more than 0.2 from previous day, indicating strengthening trend; 

3. RSI is below 85 to avoid overbought state;

Or:

1. 20-day SMA is rising;

2. ADX is increasing but less than 0.2, indicating a mild trend;

3. RSI is below 50, with potential for rebound.

### Exit Conditions:

1. RSI exceeds 75, indicating overbought state;

2. ADX shows a minor increase, suggesting weak trend;

Or: 

1. RSI exceeds 75, indicating overbought state;

2. ADX shows a sharp increase, indicating strong trend;

3. 20-day SMA turns downward.

The strategy uses RSI for overbought/oversold and ADX for trend to enter during uptrends when not overbought and exit when overbought or trend weakens. This allows following medium-to-long term uptrends.

## Advantages

The main advantages of this strategy are:

1. Combining RSI and ADX provides more accurate trend and overbought/oversold readings for better entries and exits.
2. Using ADX to gauge trend strength can avoid premature exits during consolidation periods.
3. Loose parameters in the RSI allow it to follow medium-to-long term trends while reducing excessive trading.
4. The strategy is simple and easy to implement, suitable for long-term holdings.
5. Configurable parameters offer flexibility.

## Risks

The main risks are:

1. ADX lag may cause missing trend turning points leading to larger losses.
2. Stop loss may trigger late during cliff-like price drops, expanding losses.
3. RSI parameters set too loosely might result in overbought positions for too long.
4. ADX parameters set too sensitively could lead to false exits during weak trends.
5. Stocks may behave abnormally during market regime shifts.

### Risk Management

1. Use shorter ADX periods for sensitivity.
2. Set stricter stop loss levels to limit potential losses.
3. Shorten RSI periods to avoid prolonged overbought positions.
4. Avoid overly sensitive ADX parameters.
5. Manually override the strategy during significant market shifts.

## Enhancements

The strategy can be optimized by:

1. Testing different RSI period settings for better performance.
2. Optimizing ADX period combinations to enhance trend capturing ability.
3. Adding other indicators like MACD for confirmation purposes.
4. Experimenting with moving average combinations to improve entry points.
5. Incorporating profit taking and stop loss strategies to boost the risk-reward ratio.
6. Judging market regimes to manually override during turning points.

## Conclusion

The RSI Tracking ADX strategy is an effective yet simple long-term trend-following strategy that synergizes the strengths of both RSI and ADX for accurate overbought/oversold analysis and trend determination. The logic is straightforward, easy to implement with optimization flexibility. Caution should be exercised regarding ADX lag and stop loss settings. Overall, it is suitable for tracking medium-to-long term trends and can provide steady profits.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|ADX Smoothing|
|v_input_2|14|DI Length|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-10-03 00:00:00
end: 2023-10-09 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Copyright by Reed Asset Management registered in Shanghai, China
// This strategy is developed by Shanghai Reed Asset Management Co., Ltd.
//@version=2
strategy("[Reed Strategy] ADX+RSI", overlay=true)

//ADX
adxlen = input(14, title="ADX Smoothing")
dilen = input(14, title="DI Length")
dirmov(len) =>
    up = change(high)
    down = -change(low)
    truerange = rma(tr, len)
    plus = fixnan(100 * rma(up > down and up > 0 ? up : 0, len) / truerange)
    minus = fixnan(100 * rma(down > up and down > 0 ? down : 0, len) / truerange)
    [plus, minus]

longCondition1 = (sma(close, 20) > sma(close, 20)[-1]) and
                ((adx(14, 14) - adx(14, 14)[-1]) > 0.2) or
                rsi(close, 14) < 85 or
                ((adx(14, 14) - adx(14, 14)[-1]) > 0 and 
                 (adx(14, 14) - adx(14, 14)[-1] ) < 0.2) and
                rsi(close, 14) < 50

longCondition2 = sma(close, 20) > sma(close, 20)[-1]

// Additional logic for entry conditions can be added here

// Exit Conditions
exitCondition1 = rsi(close, 14) > 75 and 
                 (adx(14, 14) - adx(14, 14)[-1]) < 0.2
exitCondition2 = rsi(close, 14) > 75 and 
                 (adx(14, 14) - adx(14, 14)[-1]) > 0.2 or 
                 sma(close, 20) < sma(close, 20)[-1]

// Strategy logic
if longCondition1
    strategy.entry("Long", strategy.long)

if exitCondition1 or exitCondition2
    strategy.close("Long")

plot(adx(14, 14), color=color.blue)
plot(rsi(close, 14), color=color.red)
```

Note: The provided Pine Script has been slightly adjusted to ensure clarity and completeness. Adjustments may be necessary based on specific requirements or additional logic needed for the strategy.