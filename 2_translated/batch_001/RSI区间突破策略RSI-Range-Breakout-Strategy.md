> Name

RSI Range Breakout Strategy RSI-Range-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

The RSI range breakout strategy is a typical trend-following strategy. It uses the Relative Strength Index (RSI) as the primary technical indicator to identify breakouts when RSI is in overbought or oversold levels, aiming to follow the trend.

## Strategy Logic

This strategy mainly relies on the RSI indicator to determine overbought and oversold conditions. The RSI calculation formula is: `RSI = (Average Up Value / (Average Up Value + Average Down Value)) * 100`. Here, the Average Up Value represents the simple moving average of close-up amplitudes over the past N days, while the Average Down Value represents the simple moving average of close-down amplitudes over the same period.

When RSI is greater than the predefined overbought line (default 80), it indicates an overbought market. Conversely, when RSI is lower than the defined oversold zone (default 35), it suggests an oversold market. The strategy seeks short opportunities when RSI breaks below the overbought line and long opportunities when RSI breaks above the oversold level.

Specifically, the strategy employs two Simple Moving Average (SMA) lines to gauge the trend of the RSI indicator. When the fast SMA crosses above the slow SMA while RSI breaches the oversold zone, it signals a buy opportunity. Conversely, when the fast SMA crosses below the slow SMA and RSI breaches the overbought line, it indicates a sell opportunity. The strategy also sets stop loss and take profit levels to control risk.

## Advantages

- Utilizes the RSI indicator to determine overbought and oversold conditions, providing certain trend judgment capabilities
- Combines with dual SMA lines to avoid false breakouts caused by RSI oscillations  
- Sets stop loss and take profit limits to control single trades
- Break-in entry avoids frequent opening and closing

## Risks and Solutions

- The RSI indicator has a lagging effect, potentially missing trend reversal points.
  - Adjust the RSI parameters appropriately to optimize the sensitivity of the indicator.
- Incorrect overbought and oversold zone settings can make it difficult to achieve profit targets.
  - Adjust parameters according to different markets to ensure reasonable settings.
- Stop loss levels too close may be triggered by overnight fluctuations.
  - Widen stop loss distances appropriately to avoid being trapped.
- Take profit levels set too low fail to fully capture trend runs.
  - Adjust take profit lines flexibly based on market volatility.

## Optimization Directions

- Integrate with other indicators, such as KDJ and MACD, to mitigate the RSI indicator lag issue.
- Incorporate major trend judgments to avoid trading against the prevailing trend.
- Optimize stop loss and take profit strategies, including trailing stops and moving take profits.
- Customize parameters for different products based on market characteristics to determine appropriate settings.
- Add position management strategies by adjusting positions through adding orders.

## Summary

The RSI range breakout strategy is a typical trend-following approach overall. It identifies buy/sell points using the RSI indicator, filters signals with dual SMA lines, and sets stop loss and take profit levels to control risk. However, the lag in the RSI indicator and improper parameter settings can affect performance. Further optimization can fully leverage its trend-following capabilities.

||

## Overview

The RSI range breakout strategy is a typical trend following strategy. It uses the Relative Strength Index (RSI) as the main technical indicator to look for breakout opportunities when RSI is in overbought or oversold levels, with the goal of following the trend.

## Strategy Logic

The strategy mainly relies on the RSI indicator to determine overbought and oversold conditions. The RSI calculation formula is: `RSI = (Average Up Value / (Average Up Value + Average Down Value)) * 100`. Here, the Average Up Value represents the simple moving average of close-up amplitudes over the past N days. The Average Down Value represents the simple moving average of close-down amplitudes over the same period.

When RSI is higher than the predefined overbought line (default 80), it indicates an overbought market; when RSI is lower than the defined oversold zone (default 35), it suggests an oversold market. The strategy looks for short opportunities when RSI breaks down the overbought line and long opportunities when RSI breaks up the oversold level.

Specifically, the strategy uses two Simple Moving Average (SMA) lines to determine the trend of the RSI indicator. When the fast SMA crosses above the slow SMA, while RSI breaches the oversold zone, it signals a buy opportunity; conversely, when the fast SMA crosses below the slow SMA and RSI breaches the overbought line, it indicates a sell opportunity. The strategy also sets stop loss and take profit levels to control risk.

## Advantages

- Utilizes the RSI indicator to determine overbought and oversold conditions, providing certain trend judgment capabilities.
- Combines with dual SMA lines to avoid false breakouts caused by RSI oscillations.
- Sets stop loss and take profit limits to control single trades.
- Break-in entry avoids frequent opening and closing.

## Risks and Solutions

- The RSI indicator has a lagging effect, potentially missing trend reversal points.
  - Adjust the RSI parameters appropriately to optimize the sensitivity of the indicator.
- Incorrect overbought and oversold zone settings can make it difficult to achieve profit targets.
  - Adjust parameters according to different markets to ensure reasonable settings.
- Stop loss levels too close may be triggered by overnight fluctuations.
  - Widen stop loss distances appropriately to avoid being trapped.
- Take profit levels set too low fail to fully capture trend runs.
  - Adjust take profit lines flexibly based on market volatility.

## Optimization Directions

- Integrate with other indicators, such as KDJ and MACD, to mitigate the RSI indicator lag issue.
- Incorporate major trend judgments to avoid trading against the prevailing trend.
- Optimize stop loss and take profit strategies, including trailing stops and moving take profits.
- Customize parameters for different products based on market characteristics to determine appropriate settings.
- Add position management strategies by adjusting positions through adding orders.

## Summary

The RSI range breakout strategy is a typical trend following approach overall. It identifies buy/sell points using the RSI indicator, filters signals with dual SMA lines, and sets stop loss and take profit levels to control risk. However, the lag in the RSI indicator and improper parameter settings can affect performance. Further optimization can fully leverage its trend-following capabilities.

---

## Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|3|RSI Length|
|v_input_2|35|Treshold Low|
|v_input_3|80|Treshold High|
|v_input_4|3|RSI Smoothing 1|
|v_input_5|5|RSI Smoothing 2|
|v_input_6|0.026|Stop loss %|
|v_input_7|300|TP|
|v_input_8|true|Long only ?|

---

## Source (PineScript)

```pinescript
/*backtest
start: 2023-09-10 00:00:00
end: 2023-10-10 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

//strategy("Strategy RSI | Fadior", shorttitle="Strategy RSI", pyramiding=10, calc_on_order_fills=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, currency="USD", default_qty_value=100, overlay=false)
 
len = input(3, minval=1, title="RSI Length") 
threshLow = input(title="Treshold Low", defval=35)
threshHigh = input(title="Treshold High", defval=80)
rsiLength1 = input(title="RSI Smoothing 1", defval=3)
rsiLength2 = input(title="RSI Smoothing 2", defval=5)
SL = input(title="Stop loss %", type=float, defval=.026, step=.001)
TP = input( defval=300)

// 3 40 70 2
// 14 40 70 2 16 0.05 50

src = close
  
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))

plot(sma(rsi, rsiLength2), color=orange)
plot(sma(rsi, rsiLength1), color=green)

band1 = hline(threshHigh)
band0 = hline(threshLow)
fill(band1, band0, color=purple, transp=90)

```