``` pinescript
/*backtest
start: 2023-11-24 00:00:00
end: 2023-12-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Wielkieef


//@version=5
strategy(title='Three SMA-crossover strategy [30min]', overlay=true, pyramiding=1, initial_capital=10000, default_qty_type=strategy.cash, default_qty_value=10000, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.03)

src = close

Length1 = input.int(16, title='  1-SMA Lenght', minval=1, group='SMA')
Length2 = input.int(36, title='  2-SMA Lenght', minval=1, group='SMA')
Length3 = input.int(72, title='  3-SMA Lenght', minval=1, group='SMA')
SMA1 = ta.sma(close, Length1)
SMA2 = ta.sma(close, Length2)
SMA3 = ta.sma(close, Length3)

Long_ma = SMA1 > SMA2 and SMA2 > SMA3
Short_ma = SMA1 < SMA2 and SMA2 < SMA3

LengthMainSMA = input.int(100, title='  Trend SMA ', minval=1)

SMAas = ta.sma(src, LengthMainSMA)

// Powered Kaufman Adaptive Moving Average by alexgrover (modificated by Wielkieef)
lengthas = input.int(50, title='   KAMA Lenght')
sp = input.bool(true, title='  Self Powered')

er = math.abs(ta.change(close, lengthas)) / math.sum(math.abs(ta.change(close)), lengthas)
```