``` pinescript
/*backtest
start: 2023-09-10 00:00:00
end: 2023-10-10 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

//strategy("Strategy RSI | Fadior", shorttitle="Strategy RSI", pyramiding=10, calc_on_order_fills=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, currency="USD", default_qty_value=100, overlay=false)
 
len = input(3, minval=1, title="RSI Length") 
threshLow = input(title="Treshold Low", defval=35)
threshHigh = input(title="Treshold High", defval=80)
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

// Strategy Logic
longCondition = rsi < threshLow and crossover(sma(rsi, rsiLength1), sma(rsi, rsiLength2)) 
shortCondition = rsi > threshHigh and crossunder(sma(rsi, rsiLength1), sma(rsi, rsiLength2))

// Entry and Exit Conditions
if (longCondition)
    strategy.entry("Long", strategy.long)
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Stop Loss and Take Profit
if (strategy.position_size > 0)
    strategy.exit("SL/TP - Long", "Long", stop=SL, limit=TP)
if (strategy.position_size < 0)
    strategy.exit("SL/TP - Short", "Short", stop=-SL, limit=-TP)

// Optimization Parameters
//@input len = input(3, title="RSI Length")
//@input threshLow = input(35, title="Treshold Low")
//@input threshHigh = input(80, title="Treshold High")
//@input rsiLength1 = input(3, title="RSI Smoothing 1")
//@input rsiLength2 = input(5, title="RSI Smoothing 2")
//@input SL = input(.026, title="Stop loss %", type=float, step=.001)
//@input TP = input(300, title="Take Profit")

// Output
//@output len
//@output threshLow
//@output threshHigh
//@output rsiLength1
//@output rsiLength2
//@output SL
//@output TP

```

## Summary
The RSI range breakout strategy is a typical trend-following strategy. It uses the Relative Strength Index (RSI) to identify entry and exit points based on overbought or oversold conditions. The strategy employs two Simple Moving Averages (SMA) for filtering signals and sets stop loss and take profit levels to manage risks. While this strategy offers a straightforward approach, it can benefit from further optimization through additional indicators and parameters adjustments.
```