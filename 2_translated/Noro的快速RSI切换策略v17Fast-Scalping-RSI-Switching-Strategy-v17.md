> Name

Noro's Fast RSI Switching Strategy v17  
> Author

ChaoZhang  

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/15f8d998a0bb60965aa.png)
[trans]

## Overview

Noro’s Fast RSI Switching Strategy is a quantitative trading strategy that identifies overbought and oversold opportunities using the RSI indicator. The strategy also incorporates candlestick patterns, moving average filters, and stop loss methods to control risk.

The key components of this strategy include:

1. **Fast RSI Indicator:** Identify overbought and oversold levels  
2. **Candlestick Patterns:** Assist in determining trend directionality
3. **Moving Average Filter:** Use SMA to avoid false signals
4. **Stop Loss Mechanism:** Implement stop loss based on RSI limits

## Strategy Logic

Noro’s Fast RSI Switching Strategy mainly identifies the following trading signals:

1. **Fast RSI Overbought/Oversold Signals:** Trade signals are generated when fast RSI crosses above its upper limit or below its lower limit.

2. **Candlestick Signals:** Candlestick parameters like body size and direction are used to determine trend and supplement fast RSI signals.

3. **SMA Filter Signals:** SMA direction filters out false breakout signals.

4. **Stop Loss Signals:** Positions are closed when fast RSI crosses back above its upper limit or below its lower limit.

Specifically, this strategy identifies trading opportunities based on the overbought and oversold zones of the fast RSI. The fast RSI crossing below its lower limit signals an oversold condition; while crossing above its upper limit signals an overbought condition.

To avoid noise, the following supplementary conditions are added:

1. **Candle Body Size:** Larger candle bodies represent a stronger trend
2. **Candle Direction:** Determines bullish or bearish trend  
3. **SMA Filter:** Filters out false breakout signals
4. **Stop Loss:** Exits trades when fast RSI crosses back past its limits

Therefore, this strategy combines fast RSI, candlesticks, moving average, and stop loss together to generate trading signals.

## Advantages

The advantages of this strategy include:

1. **Fast RSI is Sensitive:** Quickly captures overbought/oversold opportunities  
2. **Candlestick & MA Filter:** Avoids false signals
3. **Automatic Stop Loss:** Effectively controls risks
4. **Suitable for Scalping:** Works well with shorter timeframes e.g., 1H, 30M
5. **Easy to Optimize:** Parameters can be tuned for different markets

## Risks

There are also some risks to consider:

1. **Consecutive Stop Loss:** More stop loss signals may occur in ranging markets
2. **Parameter Optimization Needed:** Parameters need tuning for different pairs and timeframes
3. **Unable to Avoid All Losses:** Timely stop loss still results in some losses

The following optimization methods can help mitigate risks:

1. **Optimize Fast RSI Parameters:** Reduce false signals
2. **Optimize Stop Loss Placement:** Control single trade loss size
3. **Add Position Sizing:** Distribute risks across multiple trades

## Optimization Directions

Some ways to further optimize this strategy include:

1. **Add Profit Taking Exits:** Take partial profits when hitting profit targets
2. **Enhance Risk Management:** Incorporate position sizing rules to diversify risks
3. **Parameter Tuning:** Test effect of parameter adjustments across timeframes  
4. **Machine Learning:** Use algorithms to automatically optimize parameters over time
5. **Robustness Testing:** Evaluate strategy performance across more symbol pairs

By incorporating profit taking, risk management, parameter optimization, machine learning, and robustness testing, the strategy can be significantly enhanced in stability.

## Conclusion

In summary, Noro’s Fast RSI Switching Strategy combines the fast RSI indicator with supplementary candlestick analysis to identify overbought and oversold trading opportunities. With quick signal response times, ease of optimization, and incorporated stop loss modules, this short-term trading strategy has strong potential to generate positive results after further machine learning and parameter tuning.

[/trans]

> Strategy Arguments


| Argument  | Default | Description |
|-----------|---------|-------------|
| v_input_1 | true    | Long        |
| v_input_2 | true    | Short       |
| v_input_3 | false   | Use Martingale |
| v_input_4 | 100     | Capital, %  |
| v_input_5 | true    | Use Fast RSI Strategy |
| v_input_6 | true    | Use Min/Max Strategy |
| v_input_7 | true    | Use BarColor Strategy |
| v_input_8 | false   | Use SMA Filter |
| v_input_9 | 20      | SMA Filter Period |
| v_input_10 | 7       | Fast RSI Period |
| v_input_11 | 30      | RSI limit    |
| v_input_12_close | 0 | RSI Price: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
| v_input_13 | true    | RSI Bars     |
| v_input_14 | true    | Min/Max Bars |
| v_input_15 | false   | Use Custom Indicator |