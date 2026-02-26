```pinescript
/*backtest
start: 2022-12-08 00:00:00
end: 2023-12-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © RingsCherrY

//@version=5

strategy("Heiken Ashi & Super Trend", overlay=true, pyramiding=1, initial_capital = 10000, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.02)

///////////////////////////////////////////////////
////////////////////Function///////////////////////
///////////////////////////////////////////////////


heikinashi_open = request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, open)
heikinashi_high = request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, high)
heikinashi_low  = request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, low)
heikinashi_close= request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, close)
heikinashi_color = heikinashi_open < heikinashi_close ? #53b987 : #eb4d5c
// plotbar(heikinashi_open, heikinashi_high, heikinashi_low, heikinashi_close, color=heikinashi_color)

x_sma(x, y) =>
    sumx = 0.0
    for i = 0 to y - 1
        sumx := sumx + x[i] / y
    sumx

x_rma(src, length) =>
	alpha = 1/length
	sum = 0.0
	sum := na(sum[1]) ? x_sma(src, length) : alpha * src + (1 - alpha) * nz(sum[1])

x_atr(length) =>
    trueRange = na(heikinashi_high[1])? heikinashi_high-heikinashi_low : math.max(math.max(heikinashi_high - heikinashi_low, math.abs(heikinashi_high - heikinashi_close[1])), math.abs(heikinashi_low - heikinashi_close[1]))
    //true range can be also calculated with ta.tr(true)
    x_rma(trueRange, length)

x_supertrend(factor, atrPeriod) =>
	src = (heikinashi_high+heikinashi_low)/2
	atr = x_atr(atrPeriod)
	multiplier = factor * atr
	highFactor = src + multiplier
	lowFactor = src - multiplier

	var int supertrendUp = na
	var int supertrendDown = na
	if (na(supertrendUp) or heikinashi_high < lowFactor[supertrendUp])
		supertrendUp := 1
	else if (supertrendUp and not(heikinashi_low > highFactor[supertrendUp]))
		supertrendUp := na

	if (na(supertrendDown) or heikinashi_low > highFactor[supertrendDown])
		supertrendDown := 1
	else if (supertrendDown and not(heikinashi_high < lowFactor[supertrendDown]))
		supertrendDown := na

	hline(0, "Zero Line", color=color.black)
	line.new(x1=bar_index-20, y1=0, x2=bar_index+20, y2=0, width=1, color=color.gray)

plot(supertrendUp ? heikinashi_close : na, style=plot.style_histogram, title="SuperTrend Up", color=color.green)
plot(supertrendDown ? heikinashi_close : na, style=plot.style_histogram, title="SuperTrend Down", color=color.red)
```

This updated Pine Script completes the `x_supertrend` function and adds the necessary plotting logic to visualize the Super Trend signals.