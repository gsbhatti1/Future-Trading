> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2017|From Year|
|v_input_4|34|Length Slow|
|v_input_5|5|Length Fast|
|v_input_6|false|Include Short Trades|
|v_input_7|false|Trade reverse|
|v_input_8|14|length|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-15 00:00:00
end: 2023-11-21 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
// This strategy is a modification to the "Bill Williams, Awesome Oscillator
// (AO) Backtest" strategy (Copyright by HPotter v1.0 29/12/2016)
//
// This version of the strategy by Midnight Mouse. 10/4/2018
//
// DESCRIPTION
//
// This indicator plots the oscillator as a column where periods fit for buying
// are marked as green, and periods fit for selling as orange/brown. If the
// current value of AO (Awesome Oscillator) crosses above its signal line,
// it generates a buy signal; if below, it generates a sell signal.
//
// The strategy uses two moving averages to identify crossover points:
// - A short-term fast MA with a length specified by 'v_input_5'
// - A long-term slow MA with a length specified by 'v_input_4'
//
// When the fast MA crosses above the slow MA, it triggers a buy signal.
// Conversely, when the fast MA crosses below the slow MA, it triggers a sell signal.
//
// The strategy also includes an optional stop loss feature. If enabled, the
// strategy will exit positions when the MAs cross in the opposite direction,
// effectively acting as a stop loss mechanism.
//
// Additional parameters:
// - v_input_1: Start month (boolean)
// - v_input_2: Start day (boolean)
// - v_input_3: Start year (integer, default 2017)
// - v_input_8: Length of the stop loss period (integer, default 14 days)
//
// The strategy is designed for beginners in quantitative trading and aims to
// filter out noise while following the main trend. It can be optimized by
// adjusting the lengths of the fast and slow MAs based on market conditions.
```

This Pine Script code implements a dual-moving-average crossover strategy similar to the described concept, but with some additional details for clarity.