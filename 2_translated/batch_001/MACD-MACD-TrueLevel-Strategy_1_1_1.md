``` pinescript
/*backtest
start: 2023-09-06 00:00:00
end: 2023-10-06 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Julien_Eche

//@version=4
strategy("MACD TrueLevel Strategy", shorttitle="MACD TL", overlay=true)

// Input parameters for MACD
fastLength = input(12, title="Fast Length", type=input.integer)
slowLength = input(26, title="Slow Length", type=input.integer)
signalLength = input(9, title="Signal Length", type=input.integer)

// Inputs for selecting bands
entry_band = input(12, title="Entry TrueLevel Band", type=input.integer, minval=1, maxval=14)
exit_band = input(12, title="Exit TrueLevel Band", type=input.integer, minval=1, maxval=14)

// Input for long and short mode
long_and_short = input(false, title="Enable Long and Short", type=input.bool)

// Calculate the MACD
[macdLine, signalLine, _] = macd(close, fastLength, slowLength, signalLength)

// User inputs
len1 = input(title="Length 1", type=input.integer, defval=126)
len2 = input(title="Length 2", 
```