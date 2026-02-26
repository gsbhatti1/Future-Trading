> Name

Multiple-Indicator-Quantitative-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1005f23b21aba2dde79.png)
 [trans]
## Overview

This strategy utilizes multiple technical indicators for quantitative trading. It mainly uses indicators including EMA crossovers, SuperTrend, RSI, MACD etc. to generate trading signals.

## Strategy Logic  

The core logic is based on the following aspects:   

1. EMA Crossover: Compute fast EMA1 and slow EMA2. When EMA1 crosses above EMA2, generate buy signal. When EMA1 crosses below EMA2, generate sell signal.

2. VWMA: Compute VWMA. When close price crosses above VWMA, it is a buy signal. When close price crosses below VWMA, it is a sell signal.  

3. SuperTrend: Compute the upper and lower bands based on ATR and multiplier parameters. Determine trend direction. Generate buy signals in an uptrend and sell signals in a downtrend.  

4. RSI: Compute RSI indicator. When RSI is above the overbought level, it is a sell signal. When RSI is below the oversold level, it is a buy signal.  

5. MACD: Compute MACD, signal line, and histogram. When MACD crosses above the signal line, generate buy signal. When MACD crosses below the signal line, generate sell signal.

The strategy adopts "AND" logic to combine signals. Only when multiple indicators emit buy/sell signals simultaneously, a final trading signal will be generated.   

## Advantages  

This strategy combines multiple indicators to filter the market and avoid false signals. Main advantages:

1. Multiple indicator combination avoids errors from single indicators.  

2. Combination of trend indicators and oscillator capture extra profit during trends.

3. Use of stop loss logic limits maximum loss per trade.  

4. Martingale logic provides chance to break even after losses.  

## Risks   

Main risks:

1. Too conservative indicator combination may miss some trading opportunities. Simplify the indicators combination when necessary.  

2. Martingale logic may lead to significant losses. Set reasonable limitations on additional entries.

3. Improper use of stop loss may lead to unnecessary stopouts. Adopt adaptive stop loss mechanism.

4. Improper parameter tuning may lead to too many false signals. Optimize parameters to find the best combination.  

## Optimization   

The strategy can be further optimized in the following aspects:

1. Evaluate different combinations of indicators and determine their weights.

2. Test different parameters for each indicator.  

3. Add adaptive stop loss logic.  

4. Add dynamic position sizing mechanism.

5. Leverage machine learning to optimize parameters and models.  

## Summary   

In summary, this is a very practical quantitative trading strategy. It combines the strengths of multiple classical technical indicators for market analysis. Further parameter tuning and model optimization can lead to better results.

[/trans]

> Strategy Arguments


| Argument | Default | Description |
| --- | --- | --- |
| v_input_int_1 | true | From Month |
| v_input_int_2 | true | From Day |
| v_input_int_3 | 2021 | From Year |
| v_input_int_4 | true | Thru Month |
| v_input_int_5 | true | Thru Day |
| v_input_int_6 | 2112 | Thru Year |
| v_input_1 | true | Show Date Range |
| v_input_int_7 | 10 | length1 |
| v_input_int_8 | 20 | length2 |
| v_input_int_9 | 20 | VWMA_len |
| v_input_2 | 22 | STR Period |
| v_input_3_hl2 | 0 | Source: hl2, high, low, open, close, hlc3, hlcc4, ohlc4 |
| v_input_float_1 | 5 | STR Multiplier |
| v_input_4 | 14 | Rsi Period |
| v_input_5 | 44 | over_sold |
| v_input_6 | 56 | over_bought |
| v_input_int_10 | 12 | slow_len_macd |
| v_input_int_11 | 26 | fast_len_macd |
| v_input_int_12 | 9 | signal_len_macd |
| v_input_7 | 14 | ADX Smoothing |
| v_input_8 | 14 | DI Length |
| v_input_int_13 | 25 | adx_Greater_than |
| v_input_int_14 | 10 | volume_ema |
| v_input_9 | true | multiple_signals |
| v_input_10 | 0.5 | StopLoss |
| v_input_11 | 1.5 | Profit |
| v_input_12 | 1024 | Reverse Limit |
| v_input_13 | true | Averaging position ? |

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='Pinku Buy', overlay=true)

fromMonth = input.int(defval=1, title='From Month', minval=1, maxval=12)
fromDay = input.int(defval=1, title='From Day', minval=1, maxval=31)
fromYear = input.int(defval=2021, title='From Year', minval=1970)
thruMonth = input.int(defval=1, title='Thru Month', minval=1, maxval=12)
thruDay = input.int(defval=1, title='Thru Day', minval=1, maxval=31)
thruYear = input.int(defval=2112, title='Thru Year', minval=1970)

showDate = input(defval=true, title='Show Date Range')

start = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finish = timestamp(thruYear, thruMonth, thruDay, 23, 59)

window() => true
// ema crossover
length1 = input.int(10)
length2 = input.int(20)
ema1 = ta.ema(close, length1)
ema2 = ta.ema(close, length2)
crossover = ta.crossover(ema1, ema2)
crossunder = ta.crossunder(ema1, ema2)

// VWMA
VWMA_len = input.int(20)
vwap = ta.vwap(open, high, low, close, 13) // Assuming a specific VWMA formula or use another method if needed

// SuperTrend
STR_Period = input.int(22)
STR_Multiplier = input.float(5.0)
[upperband, lowerband] = ta.supertrend(STR_Period, STR_Multiplier)

// RSI
rsiPeriod = input.int(14)
overSoldLevel = input.int(44)
overBoughtLevel = input.int(56)
rsi = ta.rsi(close, rsiPeriod)

// MACD
slow_len_macd = input.int(12)
fast_len_macd = input.int(26)
signal_len_macd = input.int(9)
[macdLine, signalLine, _] = ta.macd(close, slow_len_macd, fast_len_macd, signal_len_macd)

// Add conditions to generate buy and sell signals based on the above indicators
```