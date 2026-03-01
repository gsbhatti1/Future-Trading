``` pinescript
/*backtest
start: 2023-09-06 00:00:00
end: 2023-09-08 09:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Rolan_Kruger

//@version=5
strategy("PSAR BBPT ZLSMA", "PBZ", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

///////////////////////////////////////////////////////////////////////////////////////////////////////
// PSAR BUY/SELL

start = input.float(title='Start', step=0.00005, defval=0.05, group="PSAR")
increment = input.float(title='Increment', step=0.00005, defval=0.05, group="PSAR")
maximum = input.float(title='Maximum', step=0.01, defval=0.13, group="PSAR")
width = input.int(title='Point Width', minval=1, defval=20, group="PSAR")
highlightStartPoints = input(title='Highlight Start Points ?', defval=false, group="PSAR")

psar = ta.sar(start, increment, maximum)
dir = psar < close ? 1 : -1

psarColor = psar < close ? #3388bb : #fdcc02


plotshape(dir == 1 and dir[1] == -1 and highlightStartPoints ? psar : na, title='Buy', style=shape.labelup, location=location.absolute, size=size.normal, text='Buy', textcolor=color.new(color.white, 0), color=color.new(color.green, 0))
plotshape(dir == -1 and dir[1] == 1 and highlightStartPoints ? psar : na, title='Sell', style=shape.labeldown, location=location.absolute, size=size.normal, text='Sell', textcolor=color.new(color.white, 0), color=color.new(color.red, 0))

barcolor(dir == 1 ? color.green : color.red, display=display.none)
PSAR_Buy = dir == 1 and dir[1] == -1
```

The translated document ends here. The code blocks are kept exactly as they were originally.