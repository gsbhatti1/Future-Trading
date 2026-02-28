``` pinescript
/*backtest
start: 2023-10-22 00:00:00
end: 2023-10-29 00:00:00
period: 15m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI Improved strategy", overlay=true)
higherTF1 = input.timeframe('15', "Resolution", options = ['5', '15', '1H', 'D', 'W', 'M'])
dailyopen = request.security(syminfo.tickerid, higherTF1, close)

Reward = input(1600)
Risk = input(1600)

length = input(5)
overSold = input(30)
overBought = input(70)
EMA = input(200)
price = close

vrsi = ta.rsi(price, length)

RSIlowest = vrsi[1] > vrsi ? true : false
RSIhighest = vrsi[1] < vrsi ? true : false

//ro = ta.crossunder(vrsi, 20)
//ru = ta.crossover(vrsi, 80)

co = ta.crossunder(vrsi, overSold)
cu = ta.crossabove(vrsi, overBought)

plot(ta.ema(close, EMA))
plot(ta.ema(close, 50), color=color.orange)

UponEMA = close > ta.ema(close, EMA) ? true : false
belowEMA = close < ta.ema(close, EMA) ? true : false

// Transfer 'float' to 'int' to 'string'
r = int(vrsi)
value = str.tostring(r)

m = int(strategy.openprofit)
money = str.tostring(m)

if (not na(vrsi))
    // When price stands above 200EMA and RSI is in oversold area, open long position
    if (co and UponEMA)
        strategy.order("Rsi long", strategy.long, 1, comment="RSI Long Entry")
    
    // When price crosses below EMA and RSI is in overbought area, open short position
    if (cu and belowEMA) 
        strategy.order("Rsi short", strategy.short, 1, comment="RSI Short Entry")
        
// Add stop loss and take profit levels
if (strategy.position_size > 0)
    strategy.exit("RSI Long Exit", "Rsi long", stop=ta.stop_loss(strategy.close_price * (1 - Risk / 100)), limit=ta.take_profit(strategy.close_price * (1 + Reward / 100)))
    
if (strategy.position_size < 0)
    strategy.exit("RSI Short Exit", "Rsi short", stop=ta.stop_loss(strategy.close_price * (1 + Risk / 100)), limit=ta.take_profit(strategy.close_price * (1 - Reward / 100)))
```

This Pine Script code defines the RSI improved trading strategy as described in the document. It includes setting up conditions for entering long and short positions based on RSI levels, crossing price EMA lines, and managing stop losses and take profits.