> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|8|fastLength|
|v_input_2|16|slowLength|
|v_input_3|11|signalLength|
|v_input_4|false|Trade reverse|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-14 00:00:00
end: 2023-11-20 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 06/09/2017
// MACD – Moving Average Convergence Divergence. The MACD is calculated 
// by subtracting a 26-day moving average of a security's price from a 
// 12-day moving average of its price. The result is an indicator that 
// oscillates above and below zero. When the MACD is above zero, it means 
// the 12-day moving average is higher than the 26-day moving average. 
// This is bullish as it shows that current expectations (i.e., the 12-day 
// moving average) are more bullish than previous expectations (i.e., the 
// 26-day average). This implies a bullish, or upward, shift in the supply/demand 
// lines. When the MACD falls below zero, it means that the 12-day moving average 
// is less than the 26-day moving average, implying a bearish shift in the 
// supply/demand lines.
// A 9-day moving average of the MACD (not of the security's price) is usually 
// plotted on top of the MACD indicator. This line is referred to as the "signal" 
// line. The signal line anticipates the convergence of the two mov
```