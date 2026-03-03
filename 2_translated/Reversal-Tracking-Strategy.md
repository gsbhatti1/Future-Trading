> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|0.95|StopLoss|
|v_input_2|5|HowManyBars|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-02-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//  @version=4
//  © HermanBrummer
//  This source code is subject to the

var float stopLoss = input(0.95, title="StopLoss")
var int howManyBars = input(5, title="HowManyBars")

//@title Reversal-Tracking-Strategy
strategy("Reversal Tracking Strategy", overlay=true)

// Market Filter: 200-day simple moving average
sma200 = sma(close, 200)
longCondition = close < ref(low, howManyBars) and close > sma200
shortCondition = close > ref(high, howManyBars) and close < sma200

// Trading Logic
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.close("Long")

// 5% Stop Loss
stopLossValue = stopLoss * close
strategy.exit("Stop Loss", "Long", stop=stopLossValue)
```