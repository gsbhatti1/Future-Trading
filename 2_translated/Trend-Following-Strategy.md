```pinescript
/*backtest
start: 2022-10-30 00:00:00
end: 2023-11-05 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Trend-Following Strategy", overlay=true, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=15)

//Heikin Ashi Option
ha = input(true, title="Heikin-Ashi Source")
src = ha ? request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, close, barmerge.gaps_off, barmerge.lookahead_off) : close
usestoploss = input(true, title="Stop Loss")

//EMA
len1 = input.int(9, minval=1, title="EMA Length")
ema = ta.ema(src, len1)
emaline = plot(ema, color=color.blue, linewidth=2, title="EMA Line")

//HMA
len2 = input.int(69, minval=1, title="HMA Length")
hma = ta.hma(src, len2)

//Strategy Logic
longCondition = ema > hma and not na(prevClose) and prevClose < hma[1] and close > emaline[1]
shortCondition = ema < hma and not na(prevClose) and prevClose > hma[1] and close < emaline[1]

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

//Exit Conditions
exitLongCondition = ema < hma and not na(prevClose) and prevClose > hma[1] and close < emaline[1]
exitShortCondition = ema > hma and not na(prevClose) and prevClose < hma[1] and close > emaline[1]

if (exitLongCondition)
    strategy.close("Long")

if (exitShortCondition)
    strategy.close("Short")

//Stop Loss
stoplossPercent = input.float(-6.5, minval=0, title="Stop Loss (%)")
stopLossPrice = na(strategy.position_avg_price) ? na : strategy.position_avg_price * (1 - stoplossPercent / 100)

if (usestoploss)
    if (strategy.position_size > 0 and close < stopLossPrice)
        strategy.exit("Long Stop Loss", "Long")
    if (strategy.position_size < 0 and close > stopLossPrice)
        strategy.exit("Short Stop Loss", "Short")

// Plotting
plotshape(series=longCondition, location=location.belowbar, color=color.green, style=shape.triangleup, title="Buy Signal")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.triangledown, title="Sell Signal")

// Optional Plotting of EMA and HMA Lines
line.new(x1=bar_index - 1, y1=ema[-1], x2=bar_index, y2=ema, color=color.blue, width=2)
line.new(x1=bar_index - 1, y1=hma[-1], x2=bar_index, y2=hma, color=color.red, width=2)

// Alert Conditions
alertcondition(longCondition, title="Long Entry Alert", message="Long entry signal generated at bar open.")
alertcondition(shortCondition, title="Short Entry Alert", message="Short entry signal generated at bar open.")
```

This script implements the trend-following strategy with Heikin-Ashi and stop-loss features. The key components include setting up EMA and HMA lines, generating buy/sell signals based on their crossovers, and implementing a stop loss mechanism to manage risk.