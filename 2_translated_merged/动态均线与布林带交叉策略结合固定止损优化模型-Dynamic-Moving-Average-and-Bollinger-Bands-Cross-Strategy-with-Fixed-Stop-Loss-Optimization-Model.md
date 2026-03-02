``` pinescript
/*backtest
start: 2024-11-26 00:00:00
end: 2024-12-25 08:00:00
period: 3h
basePeriod: 3h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/


//@version=5
strategy("MA 200 and Bollinger Bands Strategy", overlay=true) // 2.86% for 35x leverage

// inputs
ma_length = input(200, title="MA Length")
bb_length = input(20, title="Bollinger Bands Length")
bb_mult = input(2.0, title="Bollinger Bands Multiplier")

// calculations
ma_200 = ta.sma(close, ma_length)
bb_basis = ta.sma(close, bb_length)
bb_upper = bb_basis + (ta.stdev(close, bb_length) * bb_mult)
bb_lower = bb_basis - (ta.stdev(close, bb_length) * bb_mult)

// plot indicators
plot(ma_200, color=color.blue, title="200 MA")
plot(bb_upper, color=color.red, title="Bollinger Upper Band")
plot(bb_basis, color=color.gray, title="Bollinger Basis")
plot(bb_lower, color=color.green, title="Bollinger Lower Band")

// strategy logic
long_condition = close > ma_200 and bb_basis > ma_200 and ta.crossover(close, bb_lower)
short_condition =  price < ma_200 and bb_basis < ma_200 and ta.crossunder(price, bb_upper)

// position management
risk_percentage = 0.03
max_leverage = 35

if (long_condition)
    strategy.entry("Long", strategy.long)
    strategy.exit("Stop Loss Long", "Long", stop=bb_upper[1])
    
if (short_condition)
    strategy.entry("Short", strategy.short)
    strategy.exit("Stop Loss Short", "Short", stop=bb_lower[1])

// plot signals
plotshape(series=long_condition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Long Entry")
plotshape(series=short_condition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Short Entry")

```