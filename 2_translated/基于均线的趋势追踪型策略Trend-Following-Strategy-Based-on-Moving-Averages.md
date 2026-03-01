``` pinescript
/*backtest
start: 2023-10-27 00:00:00
end: 2023-11-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy(title="Trend-Following Strategy Based on Moving Averages", overlay=true)

ema200 = ema(close, 200)
conversionPeriods = input(9, minval=1, title="Conversion Line Periods")
basePeriods = input(26, minval=1, title="Base Line Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span 2 Periods")
displacement = input(26, minval=1, title="Displacement")

donchian(len) => avg(lowest(len), highest(len))

conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadLine1 = avg(conversionLine, baseLine)
leadLine2 = donchian(laggingSpan2Periods)

plot(conversionLine, color=#0496ff, title="Conversion Line", linewidth=3)
plot(baseLine, color=#991515, title="Base Line", linewidth=3)
plot(close, offset=-displacement, color=#459915, title="Lagging Span")

p1 = plot(leadLine1, offset=displacement, color=green,
          title="Lead 1")
p2 = plot(leadLine2, offset=displacement, color=red, 
          title="Lead 2")
fill(p1, p2, color=leadLine1 > leadLine2 ? green : red)

plot(ema200, color=purple, linewidth=4, title='EMA200')
strategy.initial_capital = 50000

strategy.entry('trendEntry', strategy.long, strategy.initial_capital / close, when=conversionLine > baseLine and close > ema200)
strategy.close('trendExit', when=conversionLine < baseLine)
```

This code block correctly reflects the translated text while keeping all original elements intact.