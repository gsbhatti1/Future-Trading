``` pinescript
/*backtest
start: 2023-09-10 00:00:00
end: 2023-10-10 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

//strategy("RSI Range Breakout Strategy | ChaoZhang", shorttitle="RSIBreakoutStrategy", pyramiding=10, calc_on_order_fills=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, currency="USD", default_qty_value=100, overlay=false)
 
len = input(3, minval=1, title="RSI Length") 
threshLow = input(title="Oversold Zone", defval=35)
threshHigh = input(title="Overbought Line", defval=80)
rsiLength1 = input(title="RSI Smoothing 1", defval=3)
rsiLength2 = input(title="RSI Smoothing 2", defval=5)
SL = input(title="Stop loss %", type=float, defval=.026, step=.001)
TP = input( defval=300)

// 3 40 70 2
// 14 40 70 2 16 0.05 50

src = close
  
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))

plot(sma(rsi,rsiLength2), color=orange)
plot(sma(rsi,rsiLength1), color=green)

band1 = hline(threshHigh)
band0 = hline(threshLow)
fill(band1, band0, color=purple, transp=90)

// Define strategy conditions
longCondition = crossover(sma(rsi, rsiLength1), sma(rsi, rsiLength2)) and rsi < threshLow
shortCondition = crossunder(sma(rsi, rsiLength1), sma(rsi, rsiLength2)) and rsi > threshHigh

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Set stop loss and take profit
strategy.exit("Take Profit", "Long", profit=TP)
strategy.exit("Stop Loss", "Long", stop=SL)

```