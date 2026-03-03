> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2024|Backtest Start Year|
|v_input_2|1|Backtest Start Month|
|v_input_3|2|Backtest Start Day|
|v_input_4|2024|Backtest Stop Year|
|v_input_5|9|Backtest Stop Month|
|v_input_6|26|Backtest Stop Day|
|v_input_7|9|length|
|v_input_8_close|close|Price: close, high, low, open, hl2, hlc3, hlcc4, ohlc4|
|v_input_9|-80|buyline|
|v_input_10|80|sellline|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-02 00:00:00
end: 2024-02-01 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

//* Backtesting Period Selector | Component *//
//* https://www.tradingview.com/script/eCC1cvxQ-Backtesting-Period-Selector-Component *//
//* https://www.tradingview.com/u/pbergden/ *//
//* Modifications made *//
testStartYear = input(2024, "Backtest Start Year")
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(2, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0)

testStopYear = input(2024, "Backtest Stop Year")
testStopMonth = input(9, "Backtest Stop Month")
testStopDay = input(26, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay,0,0)

testPeriod() => true
/////////////// END - Backtesting Period Selector | Component ///////////////
strategy(title="Chande Momentum Strat", shorttitle="ChandeMO Strat", format=format.price, precision=2)
length = input(9, minval=1)
src = input(close, "Price", type=input.source)
momm = change(src)
f1(m) => m >= 0.0 ? m : 0.0
f2(m) => m >= 0.0 ? 0.0 : -m
m1 = f1(momm)
m2 = f2(momm)
sm1 = sum(m1, length)
sm2 = sum(m2, length)
percent(nom, div) => 100 * nom / div
chandeMO = percent(sm1 - sm2, sm1 + sm2)
plot(chandeMO, "Chande MO", color=color.blue)
hline(0, color=#C0C0C0, linestyle=hline.style_dashed, title="Zero Line")
buyline = input(-80)
sellline = input(80)
hline(buyline, color=color.gray)
hline(sellline, color=color.gray)

if testPeriod()
    if crossover(chandeMO, buyline)
        strategy.entry("Long", strategy.long, alert_message="a=ABCD b=buy e=binanceus q=1.2 s=uniusd")
    //    strategy.exit(id="Long Stop Loss", stop=strategy.position_avg_price*0.8) //20% stop loss 
        
```