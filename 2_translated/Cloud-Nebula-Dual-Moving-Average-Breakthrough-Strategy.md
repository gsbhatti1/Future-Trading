```pinescript
/*backtest
start: 2023-12-14 00:00:00
end: 2023-12-19 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// High Low Cloud Strategy Backtesting
// © inno14

//@version=4
strategy(title="High Low Cloud Strategy Backtesting", overlay=true, pyramiding=0)
c1=input(60, title="Fast Cloud Length")
c2=input(240, title="Slow Cloud Length")
c1_high=ema(high,c1)
c1_low=ema(low,c1)
highc1=plot(c1_high, title="Fast Cloud - High", color=color.blue, offset=0, transp=50, linewidth=1)
lowc1=plot(c1_low, title="Fast Cloud - Low", color=color.blue, offset=0, transp=50, linewidth=1)
fill(highc1, lowc1, transp=60, color=color.blue, title="Fast Cloud")
c2_high=ema(high,c2)
c2_low=ema(low,c2)
highc2=plot(c2_high, title="Slow Cloud - High", color=color.green, offset=0, transp=50, linewidth=1)
lowc2=plot(c2_low, title="Slow Cloud - Low", color=color.green, offset=0, transp=50, linewidth=1)
fill(highc2, lowc2, transp=40, color=color.green, title="Slow Cloud")
//Backtesting
//Long condition
ycloud_entry=
       c1_high<c2_low
       and crossover(close,c2_high)

ycloud_stoploss=
       crossunder(close,valuewhen(ycloud_entry,lowest(close[1],c2),0))

ycloud_takeprofit=
      c1_low>c2_high
      and crossunder(close,c1_low)

// Short condition
ycloud_entry_short=
       c1_high>c2_high
       and crossover(close,c2_low)

ycloud_stoploss_short=
       crossunder(close,valuewhen(ycloud_entry_short,highest(close[1],c2),0))

ycloud_takeprofit_short=
      c1_low<c2_low
      and crossunder(close,c1_low)

strategy.entry("Long", strategy.long, when=ycloud_entry)
strategy.exit("Take Profit Long", "Long", stop=ycloud_stoploss, limit=ycloud_takeprofit)
strategy.exit("Stop Loss Long", "Long", stop=ycloud_stoploss)

strategy.entry("Short", strategy.short, when=ycloud_entry_short)
strategy.exit("Take Profit Short", "Short", stop=ycloud_stoploss_short, limit=ycloud_takeprofit_short)
strategy.exit("Stop Loss Short", "Short", stop=ycloud_stoploss_short)
```
```