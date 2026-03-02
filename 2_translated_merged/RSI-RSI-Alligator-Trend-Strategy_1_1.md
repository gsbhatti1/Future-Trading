<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

RSI Alligator Trend Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/b879246e0062392917.png)
[trans]
## Overview

The RSI Alligator Trend Strategy combines the RSI indicator with the Alligator indicator to determine trend entries and exits. It uses three moving average lines— the Alligator’s jaw line, teeth line, and lip line—constructed using RSI with different periods. It goes long when the teeth line crosses above the lip line and the RSI jaw line is higher than the teeth line; it goes short when the teeth line crosses below the lip line and the RSI jaw line is lower than the teeth line. This strategy also includes stop-loss and take-profit conditions.

## Strategy Logic

The RSI Alligator Trend Strategy constructs the three moving average lines of the Alligator indicator using the RSI indicator. Specific settings are as follows:

- Jaw Line: RSI line with a period of 5
- Teeth Line: RSI line with a period of 13
- Lip Line: RSI line with a period of 34

Entry signal logic is:

Long Signal: When the teeth line crosses above the lip line, and the jaw line is higher than the teeth line, go long.

Short Signal: When the teeth line crosses below the lip line, and the jaw line is lower than the teeth line, go short.

This strategy also sets stop-loss and take-profit conditions:

- Stop-loss set at 10% of the entry price
- Take-profit set at 90% of the entry price

## Advantages Analysis

The RSI Alligator Trend Strategy has the following advantages:

1. Using the Alligator lines to determine trends effectively filters out market noise and locks onto the main trend.
2. Combining multi-period RSI avoids false breakouts and improves signal reliability.
3. Setting reasonable stop-loss and take-profit conditions helps ensure stable strategy performance.
4. The strategy concept is clear and easy to understand, with simple parameter settings, making it suitable for real trading.
5. It can go both long and short, covering both trend directions, offering strong flexibility.

## Risk Analysis

The RSI Alligator Trend Strategy also presents the following risks:

1. Crossovers between the teeth line and lip line may produce false breakouts, leading to unnecessary losses. Adjusting period parameters can help reduce the probability of false breakouts.

2. Stop-loss settings might be too aggressive, resulting in frequent unnecessary stops. Consider widening the stop-loss range or adding additional conditions to activate the stop loss.

3. During volatile markets, stop-losses may not adequately protect margin. Manual intervention might be needed to timely cut losses.

4. Frequent switching between long and short positions increases transaction costs. Relaxing entry conditions can reduce unnecessary trades.

## Optimization Directions

The RSI Alligator Trend Strategy can be optimized in several ways:

1. Optimize Alligator line parameter settings by adjusting period values to find the optimal combination.

2. Enhance entry logic, e.g., add trading volume indicators to filter signals.

3. Improve stop-loss and take-profit strategies to better align with market movements and margin levels.

4. Add mechanisms to handle sudden events and avoid exposure during abnormal market conditions.

5. Introduce position sizing algorithms to control the percentage of capital risked per trade and mitigate risk.

## Summary

Overall, the RSI Alligator Trend Strategy is a reliable and easy-to-implement trend-following strategy. It uses the Alligator indicator to determine trend direction and RSI to set reference thresholds, effectively capturing trends and setting reasonable exit points. Additionally, the strategy offers strong flexibility and scalability, making it valuable for practical application and future enhancements.

[/trans]

> Strategy Arguments

| Argument       | Default | Description              |
|----------------|---------|--------------------------|
| v_input_1      | 70      | Overbought               |
| v_input_2      | 30      | Oversold                 |
| v_input_3      | 5       | Jaw Periods              |
| v_input_4      | false   | Jaw Offset               |
| v_input_5      | 13      | Teeth Periods            |
| v_input_6      | false   | Teeth Offset             |
| v_input_7      | 34      | Lips Periods             |
| v_input_8      | false   | Lips Offset              |
| v_input_9      | 0       | Strategy Type: Long Only | Long & Short | Short Only |
| v_input_10     | 7       | From Month               |
| v_input_11     | true    | From Day                 |
| v_input_12     | 2018    | From Year                |
| v_input_13     | 12      | To Month                 |
| v_input_14     | true    | To Day                   |
| v_input_15     | 2020    | To Year                  |
| v_input_16     | 10      | Stop Loss %              |
| v_input_17     | 90      | Take Profit %            |

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=3
// RSI Alligator
// Forked from Author: Reza Akhavan
// Updated by Khalid Salomão

strategy("RSI Alligator Strategy", overlay=false, pyramiding=0, default_qty_type=strategy.cash, default_qty_value=25000, initial_capital=25000, commission_type=strategy.commission.percent, commission_value=0.15, slippage=3)

// === TA LOGIC ===
overBought = input(70, minval=0, maxval=100, title="Over bought")
overSold = input(30, minval=0, maxval=100, title="Over sold")
jawPeriods = input(5, minval=1, title="Jaw Periods")
jawOffset = input(0, minval=0, title="Jaw Offset")
teethPeriods = input(13, minval=1, title="Teeth Periods")
teethOffset = input(0, minval=0, title="Teeth Offset")
lipsPeriods = input(34, minval=1, title="Lips Periods")
lipsOffset = input(0, minval=0, title="Lips Offset")

jaws = rsi(close, jawPeriods)
teeth = rsi(close, teethPeriods)
lips = rsi(close, lipsPeriods)
plot(jaws, color=green, offset=jawOffset, title="Jaw")
plot(teeth, color=red, offset=teethOffset, title="Teeth")
plot(lips, color=blue, offset=lipsOffset, title="Lips")

//
// === Signal logic ===
// 
LONG_SIGNAL_BOOLEAN  = crossover(teeth, lips) and jaws > teeth
SHORT_SIGNAL_BOOLEAN = crossunder(teeth, lips) and jaws < teeth

// === INPUT BACKTEST DATE RANGE ===
strategyType = input(defval="Long Only", options=["Long & Short", "Long Only", "Short Only"])

FromMonth = input(defval = 7, title = "From Month", minval = 1, maxval = 12)
FromDay   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
FromYear  = input(defval = 2018, title = "From Year", minval = 2017)
ToMonth   = input(defval = 12, title = "To Month", minval = 1, maxval = 12)
ToDay     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
ToYear    = input(defval = 2020, title = "To Year", minval = 2017)

start     = timestamp(FromYear, FromMonth, FromDay, 00, 00)  
finish    = timestamp(ToYear, ToMonth, ToDay, 23, 59)        
window()  => true

// === STRATEGY BUY / SELL ENTRIES ===

// TODO: update the placeholder LONG_SIGNAL_BOOLEAN and SHORT_SIGNAL_BOOLEAN to signal
// long and short entries
buy()  => window() and LONG_SIGNAL_BOOLEAN
sell() => window() and SHORT_SIGNAL_BOOLEAN

if buy()
    if (strategyType == "Short Only")
        strategy.close("Short")
    else
        strategy.entry("Long", strategy.long, comment="Long")

if sell()
    if (strategyType == "Long Only")
        strategy.close("Long")
    else
        strategy.entry("Short", strategy.short, comment="Short")
        

// === BACKTESTING: EXIT strategy ===
sl_inp = input(10, title='Stop Loss %', type=float)/100
tp_inp = input(90, title='Take Profit %', type=float)/100

stop_level = strategy.position_avg_price * (1 - sl_inp)
take_level = strategy.position_avg_price * (1 + tp_inp)

strategy.exit("Stop Loss/Profit", "Long", stop=stop_level, limit=take_level)
```

> Detail

https://www.fmz.com/strategy/440337

> Last Modified

2024-01-29 14:40:07