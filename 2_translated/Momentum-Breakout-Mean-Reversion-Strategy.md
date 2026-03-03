``` pinescript
/*backtest
start: 2023-10-01 00:00:00
end: 2023-10-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("Free Strategy #01 (ES / SPY)", overlay=true)

// Inputs
Quantity = input(1, minval=1, title="Quantity")
EmaPeriod = input(3, minval=1, title="EMA Period")
MaxProfitCloses = input(5, minval=1, title="Max Profit Close")
MaxBars = input(10, minval=1, title="Max Total Bars")

// Misc Variables
src = close
BarsSinceEntry = 0
MaxProfitCount = 0
Ema = ema(close, EmaPeriod)
OHLC = (open + high + low + close) / 4.0

// Conditions
Cond00 = strategy.position_size == 0
Cond01 = close < Ema
Cond02 = open > OHLC
Cond03 = volume <= volume[1]
Cond04 = (close < min(open[1], close[1]) or close > max(open[1], close[1]))

// Update Exit Variables
BarsSinceEntry := Cond00 ? 0 : nz(BarsSinceEntry) + 1

// Entry Logic
if (Cond00 and Cond01 and Cond02 and Cond03 and Cond04)
    strategy.entry("Long", strategy.long)

// Exit Logic
exit_long = BarsSinceEntry >= MaxBars or max(MaxProfitCount, 0) == MaxProfitCloses
if (exit_long)
    strategy.close("Long")

// Plotting
plot(BarsSinceEntry, color=color.blue, title="Bars Since Entry")
plot(Ema, color=color.red, title="3-day EMA")
```

This script implements the logic described in the translated text. It uses Pine Script to define a trading strategy that triggers entries and exits based on the conditions specified. The strategy checks for specific market conditions and opens positions if those conditions are met. It also includes logic to manage position management through maximum bars since entry and maximum profit closes.