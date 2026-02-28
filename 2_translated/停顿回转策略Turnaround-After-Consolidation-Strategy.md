> Name

Turnaround-After-Consolidation-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/bb10819e9afe328d83.png)
[trans]


## Overview

The main idea of this strategy is to detect obvious short-term consolidation in stock price movements, and then judge the likely next direction based on the consolidation pattern formed during the "consolidation" phase, so as to take corresponding long or short positions.

## Strategy Logic

1. The strategy uses the Stochastic oscillator indicator to determine if the stock price has entered consolidation. Oscillation of Stochastic oscillator in overbought or oversold zones indicates price consolidation.
2. When Stochastic oscillator oscillates, candlestick directional changes are used to detect trend reversal points. A candle change from black to white signals consolidation end and go long. A change from white to black signals consolidation end and go short.
3. Profit targets and stop loss after entry are set dynamically based on entry price using trailing stops. Fixed profit/loss used for full position, trailing stops used for partial position.
4. The strategy supports both full and partial position trading. Fixed points used for full position, trailing stops used for partial position.
5. Trading hours are also configured in the strategy. Trades only allowed during set hours.

## Advantage Analysis

1. Stochastic oscillator accurately identifies short-term price consolidation.
2. Trading at reversal points after consolidation improves accuracy.
3. Trailing stops lock in profits as price moves favorably.
4. Supports full and partial position trading based on risk preference.
5. Trading hours avoid wrong trades during volatile periods.

## Risk Analysis

1. Stochastic oscillator prone to false signals, missing entries or giving premature entries.
2. Candlestick reversals may not be accurate for detecting trend changes.
3. Trailing stops subject to being hit by price whipsaws.
4. Higher risk with partial position trading, losses could magnify on reversals.
5. Stop loss and trailing stop parameters need tuning for different instruments.
6. Major events can affect strategy performance.

## Optimization Directions

1. Optimize Stochastic oscillator parameters for better consolidation detection.
2. Add filters to confirm candlestick signals, improving accuracy.
3. Enhance trailing stop algorithms for better tracking.
4. Add position sizing rules to limit losses in single stocks.
5. Avoid major event driven volatility by incorporating event schedule.
6. Improve partial position model to better capture trends.

## Conclusion

The turnaround after consolidation strategy identifies short-term consolidation using Stochastic oscillator and trades at trend reversal points after the consolidation phase. It has a decent winning rate and allows locking in segment profits in trends. However, Stochastic is prone to false signals. Accuracy can be improved by optimizing parameters, adding filters etc. In addition, optimizing the trailing stops, controlling position sizing, and avoiding event risks are areas that require focus. Overall, this strategy provides a reference model but needs tuning and risk control for live trading based on individual trading style.

||

## Overview

The main idea of this strategy is to detect obvious short-term consolidation in stock price movements, and then judge the likely next direction based on the consolidation pattern formed during the "consolidation" phase, so as to take corresponding long or short positions.

## Strategy Logic

1. The strategy uses the Stochastic oscillator indicator to determine if the stock price has entered consolidation. Oscillation of Stochastic oscillator in overbought or oversold zones indicates price consolidation.
2. When Stochastic oscillator oscillates, candlestick directional changes are used to detect trend reversal points. A candle change from black to white signals consolidation end and go long. A change from white to black signals consolidation end and go short.
3. Profit targets and stop loss after entry are set dynamically based on entry price using trailing stops. Fixed profit/loss used for full position, trailing stops used for partial position.
4. The strategy supports both full and partial position trading. Fixed points used for full position, trailing stops used for partial position.
5. Trading hours are also configured in the strategy. Trades only allowed during set hours.

## Advantage Analysis

1. Stochastic oscillator accurately identifies short-term price consolidation.
2. Trading at reversal points after consolidation improves accuracy.
3. Trailing stops lock in profits as price moves favorably.
4. Supports full and partial position trading based on risk preference.
5. Trading hours avoid wrong trades during volatile periods.

## Risk Analysis

1. Stochastic oscillator prone to false signals, missing entries or giving premature entries.
2. Candlestick reversals may not be accurate for detecting trend changes.
3. Trailing stops subject to being hit by price whipsaws.
4. Higher risk with partial position trading, losses could magnify on reversals.
5. Stop loss and trailing stop parameters need tuning for different instruments.
6. Major events can affect strategy performance.

## Optimization Directions

1. Optimize Stochastic oscillator parameters for better consolidation detection.
2. Add filters to confirm candlestick signals, improving accuracy.
3. Enhance trailing stop algorithms for better tracking.
4. Add position sizing rules to limit losses in single stocks.
5. Avoid major event driven volatility by incorporating event schedule.
6. Improve partial position model to better capture trends.

## Conclusion

The turnaround after consolidation strategy identifies short-term consolidation using Stochastic oscillator and trades at trend reversal points after the consolidation phase. It has a decent winning rate and allows locking in segment profits in trends. However, Stochastic is prone to false signals. Accuracy can be improved by optimizing parameters, adding filters etc. In addition, optimizing the trailing stops, controlling position sizing, and avoiding event risks are areas that require focus. Overall, this strategy provides a reference model but needs tuning and risk control for live trading based on individual trading style.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|2022|Year|
|v_input_int_2|true|Month|
|v_input_int_3|true|Day|
|v_input_int_4|true|Hour|
|v_input_int_5|false|Minute|
|v_input_int_6|10|Start Trading Hour Robo|
|v_input_int_7|40|End Everything Minuto|
|v_input_int_8|17|Close Market Hour|
|v_input_int_9|50|End New Operations Minuto|
|v_input_int_10|50|End Everything Minuto|
|v_input_int_11|90|Stochastic Target - For Short|
|v_input_int_12|10|Stochastic Target - For Buy |
|v_input_1|true|Partial? |
|v_input_int_13|150|Points for Gain |
|v_input_int_14|150|Points for Loss|
|v_input_int_15|50|Points for Partial |


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-27 00:00:00
end: 2023-11-02 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy('Turnaround-After-Consolidation', overlay=true, initial_capital=1000 )

// Creditos : Cleber.martinelli
////////////////////////////////////////////////////////
//                                                    //
//                                                    //
//                    CALENDARIO                      //
//                                                    //
//                                                    //
////////////////////////////////////////////////////////

//052)
// trading view 
```