> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_timeframe_1|0|Resolution: 15|5|1H|D|W|M|
|v_input_1|1600|Reward|
|v_input_2|1600|Risk|
|v_input_3|5|length|
|v_input_4|30|overSold|
|v_input_5|70|overBought|
|v_input_6|200|EMA|


> Source (PineScript)

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
higherTF1 = input.timeframe('15', "Resolution", options=['5', '15', '1H', 'D', 'W', 'M'])
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
cu = ta.crossover(vrsi, overBought)

plot(ta.ema(close, EMA))
plot(ta.ema(close, 50), color=color.orange)

UponEMA = close > ta.ema(close, EMA) ? true : false
belowEMA = close < ta.ema(close, EMA) ? true : false

//transfer 'float' to 'int' to 'string'
r = int(vrsi)
value = str.tostring(r)

m = int(strategy.openprofit)
money = str.tostring(m)

if (not na(vrsi))
    // When price stands above 200EMA and RSI is in oversold area, open long position
    if (co and UponEMA)
        strategy.order("Rsi long", strategy.long, 1, comment="")
```