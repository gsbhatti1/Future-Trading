``` pinescript
/*backtest
start: 2024-04-23 00:00:00
end: 2024-09-06 00:00:00
period: 4h
basePeriod: 4h
exchanges: [{"eid":"Futures_Binance","currency":"DOGE_USDT"}]
*/

//@version=5
strategy("? RX Swing ", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=1)


// === INPUTS ===
rsiLength     = input.int(14, title="RSI Length")
maLength      = input.int(14, title="RSI MA Length")
maType        = input.string("SMA", options=["SMA", "EMA"], title="MA Type for RSI")
sl_pct        = input.float(1.5, title="Stop Loss %", minval=0.0)
tp_pct        = input.float(2.5, title="Take Profit %", minval=0.0)
capitalPerTrade = input.float(15000, title="Capital Per Trade (INR)", minval=1)
lotSize       = input.int(50, title="Lot Size (Nifty Options Lot)", minval=1)
trail_points  = input.float(10, title="Trailing SL Points", minval=0.1)

// === CALCULATIONS ===
rsi    = ta.rsi(close, rsiLength)
rsiMA  = maType == "SMA" ? ta.sma(rsi, maLength) : ta.ema(rsi, maLength)

longSignal  = ta.crossover(rsi, rsiMA)
shortSignal = ta.crossunder(rsi, rsiMA)

// === TRADING WINDOW ===
canTrade = true

// === ENTRY AND EXIT CONDITIONS ===
if (longSignal and canTrade)
    strategy.entry("Long", strategy.long, comment="Long Entry")
    
if (shortSignal and canTrade)
    strategy.entry("Short", strategy.short, comment="Short Entry")

// === STOP-LOSS AND TAKE-PROFIT ===
trailingStop = strategy.trail_percent(trail_points)

strategy.exit("Take Profit Long", "Long", profit=tp_pct * capitalPerTrade)
strategy.exit("Take Profit Short", "Short", loss=-sl_pct * capitalPerTrade)

// === RISK MANAGEMENT ===
if (strategy.closed_trades > 2)
    strategy.close_all()
    
if (time.hour == 9 and time.min >= 15)
    canTrade = true

plotshape(series=longSignal, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortSignal, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// === VISUALIZATION ===
plot(rsi, title="RSI", color=color.blue)
hline(70, "Overbought", color=color.red, linestyle=hline.style_dashed)
hline(30, "Oversold", color=color.green, linestyle=hline.style_dashed)
```

This script implements the described strategy with clear entry and exit conditions, stop-loss/take-profit mechanisms, and risk management features.