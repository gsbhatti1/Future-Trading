``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Original Idea by: Wunderbit Trading

//@version=5
strategy('Keltner Channel ETH/USDT 1H', overlay=true, initial_capital=1000, pyramiding=0, currency='USD', default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.07)


/// TREND
ribbon_period = input.int(46, 'Period', step=1)

leadLine1 = ta.ema(close, ribbon_period)
leadLine2 = ta.sma(close, ribbon_period)

// p3 = plot(leadLine1, color= #53b987, title="EMA", transp = 50, linewidth = 1)
// p4 = plot(leadLine2, color= #eb4d5c, title="SMA", transp = 50, linewidth = 1)
// fill(p3, p4, transp = 60, color = leadLine1 > leadLine2 ? #53b987 : #eb4d5c)

//Upward Trend
UT = leadLine2 < leadLine1
DT = leadLine2 > leadLine1

///////////////////////////////////////INDICATORS

// KELTNER //
source = close
useTrueRange = input(true)
length = input.int(81, step=1, minval=1)
mult = input.float(2.5, step=0.1)

// Calculate Keltner Channel
ma = ta.sma(source, length)
range_1 = useTrue
```