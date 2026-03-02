> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|9|ADX Smoothing|
|v_input_2|14|DI Length|
|v_input_3|25|ADX Entry|
|v_input_4|20|CCI Length|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-02 00:00:00
end: 2023-11-01 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("ADX Strategy", currency = "USD", initial_capital = 1000, overlay=true)
adxlen = input(9, title="ADX Smoothing")
dilen = input(14, title="DI Length")
ADX_Entry = input(25, title="ADX Entry")
dirmov(len) =>
	up = change(high)
	down = -change(low)
	truerange = rma(tr, len)
	plus = fixnan(100 * rma(up > down and up > 0 ? up : 0, len) / truerange)
	minus = fixnan(100 * rma(down > up and down > 0 ? down : 0, len) / truerange)
	[plus, minus]

adx(dilen, adxlen) => 
	[plus, minus] = dirmov(dilen)
	sum = plus + minus
	adx = 100 * rma(abs(plus - minus) / (sum == 0 ? 1 : sum), adxlen)
	[adx, plus, minus]

[sig, up, down] = adx(dilen, adxlen)
cci_length = input(20, minval=1, title="CCI Length")
cci_ma = sma(close, cci_length)
cci = (close - cci_ma) / (0.015 * dev(close, cci_length))

stop_loss = syminfo.mintick * 100

open_longs = strategy.position_size > 0
open_shorts = strategy.position_size < 0

possible_bull = false
possible_bull := not open_longs ? (possible_bull[1] and not crossunder(up,down) ? true : false) : false
possible_bear = false
possible_bear := not open_shorts ? (possible_bear[1] and not crossunder(down,up) ? true : false) : false

bool bull_entry = crossover(up, down)

if(bull_entry and up < ADX_Entry and cci < 0)
	possible_bull := true
	bull_entry := false

if(possible_bull and up > ADX_Entry and cci > -100)
	bull_entry := true

bool bear_entry = crossover(down, up)

if(bear_entry and down < ADX_Entry and cci > 0)
	possible_bear := true
	bear_entry := false

if(possible_bear and down >= ADX_Entry and cci < 100)
	bear_entry := true

strategy.entry("Long", strategy.long, when = bull_entry)
strategy.exit("Close Long", "Long", stop = -stop_loss * close)

strategy.entry("Short", strategy.short, when = bear_entry)
strategy.exit("Close Short", "Short", stop = -stop_loss * close)
```

This code completes the PineScript for the described trading strategy.