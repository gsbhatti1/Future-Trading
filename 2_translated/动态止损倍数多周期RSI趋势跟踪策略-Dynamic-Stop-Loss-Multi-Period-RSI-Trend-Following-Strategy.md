``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-04 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Aggressive Scalper Strategy", overlay=true)

// Parameters
account_balance = input.float(28.37, title="Account Balance", tooltip="Update this with your balance")
risk_per_trade = input.float(0.015, title="Risk per Trade", tooltip="1.5% risk")
leverage = input.int(2, title="Leverage", minval=1)
stop_loss_percentage = input.float(0.015, title="Stop Loss Percentage", tooltip="1.5% stop loss")
take_profit_multiplier = input.float(4, title="Take Profit Multiplier", tooltip="Take Profit is 4x Stop Loss")
stop_loss_multiplier = input.float(2, title="Stop Loss Multiplier", tooltip="Dynamic Stop Loss Multiplier")

// Trade Size Calculation
position_size = account_balance * risk_per_trade / (stop_loss_percentage / leverage)
trade_qty = position_size / close // This gives you the qty in terms of contracts

// Indicators
rsiLength = input.int(14, title="RSI Length")
emaShort = input.int(9, title="Short-term EMA Length")
emaLong = input.int(21, title="Long-term EMA Length")
rsi = ta.rsi(close, rsiLength)
emaShortLine = ta.ema(close, emaShort)
emaLongLine = ta.ema(close, emaLong)

// Entry Conditions
longCondition = ta.crossover(emaShortLine, emaLongLine) and rsi < 70
shortCondition = ta.crossunder(emaShortLine, emaLongLine) and rsi > 30

// ATR for dynamic stop loss and take profit levels
atrLength = input.int(14, title="ATR Length")
atrMultiplier = input.float(1.5, title="ATR Multiplier")
atr = ta.atr(atrLength)

// Dynamic Take Profit and Stop Loss Levels
longTakeProfitLevel = close + (atr * take_profit_multiplier)
shortTakeProfitLevel = close - (atr * stop_loss_multiplier)
longStopLossLevel = close - (atr * stop_loss_multiplier)
shortStopLossLevel = close + (atr * stop_loss_multiplier)

// Orders
if (longCondition)
    strategy.entry("Long", strategy.long, qty=trade_qty)
    strategy.exit("Take Profit Long", "Long", limit=longTakeProfitLevel, stop=longStopLossLevel)
    
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=trade_qty)
    strategy.exit("Take Profit Short", "Short", limit=shortTakeProfitLevel, stop=shortStopLossLevel)
```
```