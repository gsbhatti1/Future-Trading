> Name

MACD Oscillator with EMA Crossover Strategy

> Author

ChaoZhang

> Strategy Description

### Overview

This is a simple yet efficient trading strategy combining the MACD oscillator and EMA crossover. Currently set up for 4h candles but adaptable to other timeframes. It has performed well on BTC and ETH over the past 3 years, beating buy and hold. With optimizations it can be adapted for futures, indexes, forex, stocks etc.

### Strategy Logic 

The key components are:

1. MACD: Judging price momentum changes.
2. EMA: Determining price trend direction.
3. Time condition: Defining valid strategy period.
4. Long/short option: Choosing long or short direction.

The trading rules are:

1. Long/exit short: When close above EMA, MACD histogram positive, and current candle higher than previous candle.
2. Short/exit long: When close below EMA, MACD histogram negative, and current candle lower than previous candle.

The strategy combines trend following and momentum in a simple and efficient system.

### Advantages

Compared to single indicators, the main advantages are:

1. MACD judges short-term momentum, EMA determines trend direction.
2. Simple and clear rules, easy to understand and implement.
3. Flexible parameter tuning for different products and timeframes.
4. Option for long/short only or bidirectional trading.
5. Can define valid strategy period to avoid unnecessary trades.
6. Stable outperformance over years.
7. Controllable risk per trade.
8. Potential to optimize further with machine learning.

### Risks

Despite the merits, risks to consider:

1. Broad parameter tuning risks overfitting.
2. No stops in place, risks unlimited losses.
3. No volume filter, risk of false breakouts.
4. Lag in catching trend turns, cannot avoid all losses.
5. Performance degradation from changing market regimes.
6. Based only on historical data, model robustness is key.
7. High trade frequency increases transaction costs.
8. Need to monitor reward/risk ratios and equity curves.

### Enhancements

The strategy can be enhanced by:

1. Adding volume filter to avoid false breakouts.
2. Implementing stops to control loss per trade.
3. Evaluating parameter efficacy across time periods.
4. Incorporating machine learning for dynamic optimizations.
5. Robustness testing across markets.
6. Adjusting position sizing to reduce frequency.
7. Optimizing risk management strategies.
8. Testing spread instruments to increase frequency.
9. Continual backtesting to prevent overfitting.

### Conclusion

In summary, the strategy forms a simple yet powerful system from the MACD and EMA combo. But continual optimizations and robustness testing are critical for any strategy to adapt to changing market conditions. Trading strategies need to keep evolving.

|||

### Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Use Heikin Ashi Candles in Algo Calculations|
|v_input_2|true|From Day|
|v_input_3|true|From Month|
|v_input_4|2020|From Year|
|v_input_5|31|To Day|
|v_input_6|12|To Month|
|v_input_7|2021|To Year|
|v_input_8|9|Length|
|v_input_9_hl2|0|Source: hl2|high|low|open|close|hlc3|hlcc4|ohlc4|
|v_input_10|12|Fast Length|
|v_input_11|26|Slow Length|
|v_input_12|9|Signal Smoothing|
|v_input_13|false|Simple MA (Oscillator)|
|v_input_14|false|Simple MA (Signal Line)|
|v_input_15|true|longEntry|
|v_input_16|false|shortEntry|


> Source (PineScript)

```pinescript
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © SoftKill21

//@version=4
strategy("My Script", overlay=true)

//Heikin Ashi calculation
UseHAcandles    = input(false, title="Use Heikin Ashi Candles in Algo Calculations")
//
// === /INPUTS ===

// === BASE FUNCTIONS ===

haClose = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, close) : close
haOpen  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, open) : open
haHigh  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, high) : high
haLow   = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, low) : low

//timecondition
fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2020, title = "From Year", minval = 1970)

//monday and session 
 
// To Date Inputs
toDay = input(defval = 31, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 12, title = "From Month", minval = 1, maxval = 12)
toYear = input(defval = 2021, title = "To Year", minval = 1970)

startDate = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finishDate = timestamp(toYear,