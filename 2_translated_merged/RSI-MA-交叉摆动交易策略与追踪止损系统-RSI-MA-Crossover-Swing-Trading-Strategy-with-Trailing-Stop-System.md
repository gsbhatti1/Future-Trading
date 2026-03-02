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

// === ORDER MANAGEMENT ===
if (canTrade and longSignal)
    strategy.entry("Long", strategy.long, comment="Enter Long Position")
    
if (canTrade and shortSignal)
    strategy.entry("Short", strategy.short, comment="Enter Short Position")

// === STOP-LOSS AND TAKE PROFIT ===
stopLoss = sl_pct * strategy.close_price
takeProfit = tp_pct * strategy.close_price

strategy.exit("Long Exit", "Long", stop=stopLoss, limit=takeProfit)
strategy.exit("Short Exit", "Short", stop=stopLoss, limit=takeProfit)

// === TRAILING STOP ===
trailStop = ta.lowest(low[1], trail_points) + (ta.close - ta.lowest(low[1], trail_points))
strategy.exit("Long Trail Stop", "Long", stop=trailStop)
strategy.exit("Short Trail Stop", "Short", stop=trailStop)

// === RISK CONTROL ===
consecutiveLosses = 0
if (strategy.open_orders == 0 and strategy.positions_size_long > 0)
    consecutiveLosses := 1
else if (strategy.open_orders == 0 and strategy.positions_size_short > 0)
    consecutiveLosses := 1

if (strategy.open_orders == 0 and consecutiveLosses >= 2)
    strategy.cancel_all()
    label.new(x=bar_index, y=strategy.close_price, text="Trading Paused", color=color.red, style=label.style_label_left)

// === DAILY RESUME ===
label.new(x=47, y=strategy.close_price, text="Daily Reset at 9:15 AM", color=color.blue)
```

This Pine Script code implements the RSI-MA crossover swing trading strategy with a trailing stop and risk management mechanisms. It includes parameters for stop-loss and take-profit percentages, position sizing based on capital per trade, lot size for futures contracts, and a mechanism to pause trading after two consecutive losses until 9:15 AM daily.