``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-24 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © laptevmaxim92

//@version=4
strategy("Variable Moving Average Strategy", overlay=true)

v_input_1 = input(5, title="VMA Length")
v_input_2 = input(true, title="Show Trend Direction Colors")
v_input_3 = input(false, title="Use take profit?")
v_input_4 = input(100, title="Take profit pips")
v_input_5 = input(false, title="Use stop loss?")
v_input_6 = input(100, title="Stop loss pips")
v_input_7 = input(true, title="From Day")
v_input_8 = input(true, title="From Month")
v_input_9 = input(2000, title="From Year")
v_input_10 = input(31, title="To Day")
v_input_11 = input(12, title="To Month")
v_input_12 = input(2019, title="To Year")

// Your strategy logic goes here
```