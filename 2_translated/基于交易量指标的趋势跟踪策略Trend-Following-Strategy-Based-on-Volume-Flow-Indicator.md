> Name

Trend-Following-Strategy-Based-on-Volume-Flow-Indicator

> Author

ChaoZhang

> Strategy Description

### Overview

This strategy implements trend-following trading based on the Volume Flow Indicator (VFI). It judges the market trend direction by calculating price fluctuations and volume changes, aiming to achieve low buying and high selling.

### Strategy Principle 

1. **Calculate VFI Indicator**: Compute VFI value based on logarithmic price change and volume, and smooth out oscillations through smoothing techniques.
2. **Determine Trend Direction**: VFI crossing above 0 is a bullish signal; VFI crossing below 0 is a bearish signal.
3. **Trading Signals**: Go long when the fast EMA crosses above the slow EMA and VFI crosses above the buy line; close position when VFI crosses below the sell line.
4. **Stop Loss**: Set fixed stop loss percentage.

This strategy mainly relies on VFI to determine the trend direction, combined with moving averages for signal generation. VFI reflects market sentiment through price volatility and volume changes, making it a trend-following indicator. Compared with single price indicators, VFI provides more comprehensive judgments, better identifying trend reversal points while filtering out consolidations.

### Advantages

1. **Superior Trend Detection**: VFI determines trends better than single price indicators, effectively filtering out consolidations and false breakouts.
2. **Moving Averages for Supplementary Judgements**: Moving averages provide additional signals to avoid incorrect signals from VFI in ranging markets.
3. **Fixed Stop Loss for Risk Management**: Fixed stop loss controls risk and facilitates effective risk management.
4. **Trend Following Mode for Excess Returns**: Trend following mode generates excess returns without the need to predict reversals.
5. **Flexible Parameter Tuning for Adaptability**: Flexible parameter tuning allows adaptation to different timeframes and market conditions.

### Risks

1. **Incorrect Signals During Significant Fluctuations**: VFI may generate incorrect signals during significant price fluctuations.
2. **Fixed Stop Loss May Be Too Wide or Narrow**: Fixed stop loss settings could be too wide, causing premature exits, or too narrow, resulting in inadequate protection.
3. **Poorly Configured Entry and Exit Settings**: Improper entry and exit parameters can lead to over-trading or missing trades.
4. **Trend Following Fails to Capture Reversals**: Trend following strategies may fail to capture market reversals and require timely stop losses.
5. **Improper Parameters Cause Premature or Delayed Entries/Exits**: Incorrect parameter settings can result in entering the trade too early or too late.

### Enhancements

1. **Optimize VFI Calculation by Adjusting Parameters**: Fine-tune VFI calculation parameters for better performance.
2. **Fine-Tune Moving Average Periods for Better Signal Timing**: Adjust moving average periods to improve signal timing.
3. **Use Dynamic Stop Loss Instead of Fixed One**: Implement a dynamic stop loss strategy instead of a fixed one.
4. **Add Other Indicators to Filter Signals**: Incorporate additional indicators to filter out weaker signals and improve overall trading performance.
5. **Optimize Parameters Separately Based on Timeframe**: Optimize parameters for different timeframes (e.g., daily, intraday).
6. **Test Robustness Across Different Products**: Test the strategy across different financial instruments to ensure parameter adaptability.

### Conclusion

This strategy determines market trend direction using VFI and uses moving averages to filter out wrong signals. It achieves low buying and high selling through trend following without predicting specific reversals. The main advantage is its superior trend detection over single price indicators and ability to filter out consolidations. The primary risk is generating incorrect signals during significant fluctuations. Optimizing parameters, adding supplementary indicators, and implementing stop loss techniques can enhance the strategy's stability. Overall, with parameter tuning and stop loss optimizations, this VFI-based strategy can become a reliable trend-following system.

---

### Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 8 | Length |
| v_input_2 | 0.2 | Coef |
| v_input_3 | 2.5 | Volume Cutoff |
| v_input_4 | 3 | Smoothing Period |
| v_input_5 | 0 | Smoothing Type: EMA | ALMA | SMA | WMA |
| v_input_6 | -4 | Buy Line |
| v_input_7 | 5 | Sell Line |
| v_input_8 | 5 | Stop Loss% |
| v_input_9 | 200 | Long EMA |
| v_input_10 | 50 | short EMA1 |
| v_input_11 | 9 | short EMA2 |
| v_input_12 | false | Visualize Trend |
| v_input_13 | true | Apply Filling |
| v_input_14 | true | Show Moving Average |
| v_input_15 | 0 | Moving Average Type: SMA | EMA | ALMA | WMA |
| v_input_16 | 30 | Moving Average Length |
| v_input_17 | 0.85 | • ALMA - Offset (global setting) |
| v_input_18 | 6 | • ALMA - Sigma (global setting) |

---

### Source (PineScript)

```pinescript
//@version=4
strategy(title="VFI Strategy [based on VFI indicator published by UTS]", overlay=false, pyramiding=2, default_qty_type=strategy.fixed,
         initial_capital=10000, currency=currency.USD)

// Constants
kMaColor = color.aqua
kNeutralColor = color.gray
kBearColor = color.red
 kBullColor = color.green

kAlma = "ALMA"
kEma = "EMA"
kSma = "SMA"
kWma = "WMA"

// Inputs
vfi_length = input(8, title="Length", minval=1)  // default 130
vfi_coef = input(0.2, title="Coef", minval=0.1)
vfi_volCutoff = input(2.5, title="Volume Cutoff", minval=0.1)
vfi_smoothLen = input(3, title="Smoothing