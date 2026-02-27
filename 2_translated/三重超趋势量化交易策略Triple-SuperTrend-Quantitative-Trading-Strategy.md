> Name

Triple-SuperTrend-Quantitative-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/db9d0b569071ecf016.png)
[trans]


## Overview

The Triple SuperTrend quantitative trading strategy is a short-term trading strategy that combines the use of three SuperTrend indicators. It is suitable for intraday trading and short-term arbitrage in markets such as cryptocurrencies and forex.

## Trading Logic  

- Use the 200-day moving average to determine the overall market trend direction. Go long when price is above and go short when price is below.
- Use the triple SuperTrend indicators to determine the direction of the minor market trend. The SuperTrend can accurately judge bullish and bearish trends.
- Construct entry signals using the overbought and oversold Stoch RSI indicator with Bollinger Bands. Stoch RSI can identify reversal opportunities.  
- Determine a risk-reward ratio of 1.5 based on SuperTrend stop loss and take profit.

## Advantages

- Multiple trend verifications improve decision accuracy.
- Overbought and oversold indicators identify reversal opportunities.
- Stop loss and take profit control risk and reward proportions.
- Suitable for high-frequency short-term trading with high profit potential.

## Risks

- Larger losses when the major trend is unfavorable for short-term trading. 
- Probability of failed reversals still exists leading to wrong decisions.  
- Requires constant monitoring, not suitable for away-from-market trading.

## Enhancements

- Optimize moving average parameters to adapt to longer periods.
- Optimize Stoch RSI parameters to reduce false signals.
- Optimize SuperTrend ATR period parameters to improve stop effectiveness.
- Add position sizing based on drawdowns to increase position size during pullbacks.

## Summary

The triple SuperTrend strategy enhances decision accuracy through multiple trend verifications and controls risk/reward ratios using stops and limits. It is suitable for high-frequency short-term trading. Optimizing parameters can adapt it to longer periods, reduce false signals, and improve stop effectiveness. Adding position sizing allows increasing the size of positions during pullbacks to maximize profits.

||

## Overview

The Triple SuperTrend quantitative trading strategy combines three SuperTrend indicators for short-term trading such as intraday trading and scalping. It is suitable for high-frequency trading markets such as cryptocurrencies and forex.

## Trading Logic  

- Use the 200-day moving average to determine the overall market trend direction. Go long when price is above and go short when price is below.
- Use the triple SuperTrend indicators to determine the direction of the minor market trend. The SuperTrend can accurately judge bullish and bearish trends.
- Construct entry signals using the overbought and oversold Stoch RSI indicator with Bollinger Bands. Stoch RSI can identify reversal opportunities.  
- Determine a risk-reward ratio of 1.5 based on SuperTrend stop loss and take profit.

## Advantages

- Multiple trend verifications improve decision accuracy.
- Overbought and oversold indicators identify reversal opportunities.
- Stop loss and take profit control risk and reward proportions.
- Suitable for high-frequency short-term trading with high profit potential.

## Risks

- Larger losses when the major trend is unfavorable for short-term trading. 
- Probability of failed reversals still exists leading to wrong decisions.  
- Requires constant monitoring, not suitable for away-from-market trading.

## Enhancements

- Optimize moving average parameters to adapt to longer periods.
- Optimize Stoch RSI parameters to reduce false signals.
- Optimize SuperTrend ATR period parameters to improve stop effectiveness.
- Add position sizing based on drawdowns to increase the size of positions during pullbacks.

## Summary

The triple SuperTrend strategy enhances decision accuracy through multiple trend verifications and controls risk/reward ratios using stops and limits. It is suitable for high-frequency short-term trading. Optimizing parameters can adapt it to longer periods, reduce false signals, and improve stop effectiveness. Adding position sizing allows increasing the size of positions during pullbacks to maximize profits.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2020|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|false|Strategy Direction|
|v_input_5|1.5|P/L Ratio|
|v_input_6|200|EMA Length|
|v_input_7|3|K|
|v_input_8|3|D|
|v_input_9|14|Stoch RSI Length|
|v_input_10|14|Stochastic Length|
|v_input_11_close|0|Stoch RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_12|20|Stoch RSI Entry Thresh|
|v_input_13_hl2|0|SuperTrend Source: hl2|high|low|open|close|hlc3|hlcc4|ohlc4|
|v_input_14|12|Slow SuperTrend Length|
|v_input_15|3|Slow SuperTrend Multiplier|
|v_input_16|11|Med SuperTrend Length|
|v_input_17|2|Med SuperTrend Multiplier|
|v_input_18|10|Fast SuperTrend Length|
|v_input_19|true|Fast SuperTrend Multiplier|
|v_input_20|true|Alternate SuperTrend ATR Calculation?|
|v_input_21|true|Show Open Profit/Loss Targets?|
|v_input_22|true|Show Buy/Sell Indicators?|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-24 00:00:00
end: 2023-11-30 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("3x SuperTrend Strategy (Mel0nTek) V1", calc_on_every_tick=true, overlay=true)

// ***************************************************
// A Mel0nTek Project
// Author: mel0n
// Revision: 1.0 - Initial Release
// ***************************************************

// ***************************************************
//              Strategy & Rules
// ***************************************************
// === Sources ===
// Strategy Idea:
// Trade Pro - HIGHEST PROFIT Triple Supertrend Trading Strategy Proven 100 Trade Results
// https://www.youtube.com/watch?v=HpNZ2VpZzSE

// Combining SuperTrend with StochRSI is not a new idea by any means.
// However the method/criteria used in his video to apply them caught my interest.
// So I decided to code it up for myself to do some backtesting.
// The default values are the ones he uses in his video, however I found some tuning beneficial. YMMV
// Trade Pro makes some great content, the video is a good watch to get a better understanding of this strategy.

// Improved SuperTrend Calculation Method:
// SuperTrend by KivancOzbilgic

// === Indicators ===
// EMA 
// @ 200
// Stoch RSI (default)
// @ 3, 3, 14, 14, close
// Supertrend slow
// @ 12, hl2, 3, change = true
// Supertrend med
// @ 11, hl2, 2, change = true
// Supertrend fast
// @ 10, hl2, 1, change = true

// === Rules ===
// long only 
// - price above EMA200
// short only 
// - price below EMA200
// Stop Loss = 2nd SuperTrend line above (short) or below(long) entry candle
// Profit = 1.5x SL/risk (Profit Ratio x Max Loss)

// === Entries ===
// LONG
// - long entry (Typical): 
// - Stoch RSI below 20, cross up
// - 2nd SuperTrend line below close

// SHORT
// - short entry (Typical): 
// - Stoch RSI above 80, cross down
// - 2nd SuperTrend line above close


// ***************************************************
// Backtest Parameters
// ********************
```