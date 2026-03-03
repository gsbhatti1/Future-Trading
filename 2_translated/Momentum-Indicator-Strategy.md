> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|12|fastLength|
|v_input_2|26|slowLength|
|v_input_3|9|signalLength|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-09 00:00:00
end: 2023-11-15 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy(title="Moving Average Convergence/Divergence MaCD Backesting", shorttitle="MACD Backtesting", precision = 6, pyramiding = 3, default_qty_type = strategy.percent_of_equity, currency = currency.USD, commission_type = strategy.commission.percent, commission_value = 0.10, initial_capital = 1000, default_qty_value = 100)
source = close
fastLength = input(12, minval=1), slowLength=input(26,minval=1)
signalLength=input(9,minval=1)

fastMA = ema(source, fastLength)
slowMA = ema(source, slowLength)

macd = fastMA - slowMA
signal = ema(macd, signalLength)
hist = macd - signal

plot(hist, color=red, style=histogram)
plot(macd, color=blue)
plot(signal, color=orange)

buy = crossover(macd,signal)
sell = crossunder(macd,signal)

plotshape(buy, "buy", shape.triangleup, color = olive , size = size.tiny, location  = location.bottom)
plotshape(sell, "sell", shape.triangledown, color = orange , size = size.tiny, location  = location.bottom)

if (buy)
    strategy.entry("Buy", strategy.long)
```

The remaining part of the PineScript code is automatically completed to handle the buy entry based on the MACD crossover signal.