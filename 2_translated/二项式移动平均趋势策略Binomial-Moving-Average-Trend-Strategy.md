> Strategy Name

Binomial Moving Average Trend Strategy

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|10|Fast MA|
|v_input_2|30|Slow MA|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-07 00:00:00
end: 2023-12-07 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © HosseinDaftary

//@version=4
strategy("Binomial Moving Average", "BMA", overlay=true, margin_long=100, margin_short=100, max_bars_back=96)
// Binomial Moving Average: This type of moving average that is made by myself and I did not see anywhere before uses the half of binomial coefficients for
// averaging the prices. For example, if the period be 5, then we use the 9-degree binomial coefficients (that yields 10 coefficients) and use half of them.
// We use 126/256
```