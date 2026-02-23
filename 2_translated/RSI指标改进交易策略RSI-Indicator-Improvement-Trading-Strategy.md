<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RSI Indicator Improvement Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/110663ce1b21d01ed82.png)
[trans]

## 1. Strategy Overview

This strategy improves upon the classic RSI indicator by setting buy and sell alert levels. When the RSI indicator breaks through these alert levels, corresponding buy or sell actions are taken. Additionally, this strategy provides functionality for switching between long and short positions.

## 2. Strategy Details

### 1. Strategy Name: RSI Histogram Alert Strategy

This strategy triggers buy and sell signals through the Histogram of the RSI indicator.

### 2. Strategy Logic

(1) Calculate the value of the RSI indicator using the formula:

```
RSIMain = (rsi(xPrice, RSIPeriod) - 50) * RSIHistoModify
```

Where xPrice is the price series, RSIPeriod is the parameter for calculating RSI, and RSIHistoModify is a scaling coefficient for the RSI value.

(2) Set the buy alert level BuyAlertLevel and the sell alert level SellAlertLevel. A buy signal is generated when the RSI indicator goes above the buy alert level, and a sell signal is generated when it falls below the sell alert level.

(3) Plot the Histogram of the RSI indicator to visually represent buy and sell signals.

(4) Set position pos, which is set to 1 (long) or -1 (short) when a signal is triggered. The strategy allows choosing between normal or reverse trading.

(5) Determine the entry direction and price based on the value of pos.

### 3. Strategy Advantages

(1) Improves the usage of the RSI indicator, making buy and sell signals clearer.

(2) Customizable parameters allow adjustment of the RSI indicator and alert levels to fit different markets.

(3) Provides an intuitive visualization of buy and sell signals via the Histogram.

(4) Offers options for both normal and reverse trading.

(5) Simple and clear strategy logic that is easy to understand and modify.

### 4. Strategy Risks

(1) Susceptible to false signals; the RSI indicator itself often generates incorrect signals.

(2) Does not consider stop-losses, posing a risk of significant losses.

(3) Inappropriate parameter settings may also lead to strategy failure.

### 5. Strategy Optimization Directions

(1) Combine with other indicators to filter signals and avoid false signals. For example, consider volume breakouts.

(2) Implement stop-loss mechanisms.

(3) Optimize parameters to find the best settings.

(4) Consider integrating with machine learning to automatically find optimal parameters using algorithms.

## 3. Summary

This strategy enhances the use of the RSI indicator by setting buy and sell alert levels, providing a clearer and more intuitive representation of trading signals. Compared to the original RSI indicator, it offers greater practicality. However, it still carries certain risks and requires further optimization and improvements, such as combining with other technical indicators and implementing stop-loss measures to mitigate risks. The strategy concept is straightforward, making it suitable for beginners in quantitative trading to study and practice.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|13|RSIPeriod|
|v_input_2|-10|BuyAlertLevel|
|v_input_3|10|SellAlertLevel|
|v_input_4|1.5|RSIHistoModify|
|v_input_5|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-22 00:00:00
end: 2023-12-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 22/12/2016
// This simple indicator modified RSI
// You can use in the xPrice any series: Open, High, Low, Close, HL2, HLC3, OHLC4 and ect...
// You can change long to short in the Input Settings
// Please, use it only for learning or paper trading. Do not for real trading.
////////////////////////////////////////////////////////////
strategy(title="RSI HistoAlert Strategy")
RSIPeriod = input(13, minval=1)
BuyAlertLevel = input(-10)
SellAlertLevel = input(10)
RSIHistoModify = input(1.5)
reverse = input(false, title="Trade reverse")
hline(0, color=purple, linestyle=line)
hline(BuyAlertLevel, color=green)
hline(SellAlertLevel, color=red)
xPrice = close
RSIMain = (rsi(xPrice, RSIPeriod) - 50) * RSIHistoModify
rsiHcolor =  iff(RSIMain >= 0 , green,
              iff(RSIMain < 0, red, black))
pos = iff(RSIMain > BuyAlertLevel, 1,
	     iff(RSIMain < SellAlertLevel, -1, nz(pos[1], 0))) 
possig = iff(reverse and pos == 1, -1,
          iff(reverse and pos == -1, 1, pos))	   
if (possig == 1) 
    strategy.entry("Long", strategy.long)
if (possig == -1)
    strategy.entry("Short", strategy.short)	   	    
barcolor(possig == -1 ? red: possig == 1 ? green : blue )
plot(RSIMain, color=blue, title="RSI HistoAlert")
plot(RSIMain, color=rsiHcolor, title="Histogram", style = histogram, linewidth  = 1)
```

> Detail

https://www.fmz.com/strategy/437029

> Last Modified

2023-12-29 16:23:48