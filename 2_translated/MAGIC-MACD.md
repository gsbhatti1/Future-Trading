``` pinescript
/*backtest
start: 2022-04-07 00:00:00
end: 2022-05-06 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
indicator(title="MAGIC MACD", shorttitle="MAGIC MACD", timeframe="", timeframe_gaps=true)
//By ChaoZhang 
//How to use?
//1. Signal RED Arrow on green Histogram for down
//2. Signal GREEN Arrow on Red Histogram for Up
//
//3. Confirmation by Crossover
//4. Place when Histogram is not Gray
//
//5. RED on RED Histogram IGNORE
//6. GREEN on GREEN Histogram IGNORE
//Buy SELL SIGNALS on EMA CROSSOVER

// Getting inputs
enableema=input.bool(true,title='Enable Signal EMA=ON/MACD=OFF', inline="MACD")
fast_length = input.int(5, title="Fast Length")
slow_length = input.int(50, title="Slow Length")
src = input(title="Source", defval=ohlc4)
signal_length = input.int(30, title="Signal Smoothing")
sma_source = input.string("EMA", title="Oscillator MA Type")
sma_signal = input.string("EMA", title="Signal Line MA Type")

// Plot colors
col_macd = input(#2962FF, "MACD Line  ", group="Color Settings", inline="MACD")
col_signal = input(#FF6D00, "Signal Line  ", group="Color Settings", inline="Signal")
col_grow_above = input(#26A69A, "Above   Grow", group="Histogram", inline="A
```