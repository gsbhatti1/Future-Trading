> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2019|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2022|Backtest Stop Year|
|v_input_5|true|Backtest Stop Month|
|v_input_6|true|Backtest Stop Day|
|v_input_7|true|Color Background?|
|v_input_8|27|Length|
|v_input_9|10|RSI MA Window|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-31 00:00:00
end: 2023-11-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RSI w MA Strategy", shorttitle="RSI w MA Strategy", overlay=false, initial_capital=10000, currency='USD', process_orders_on_close=true)

// TIME FRAME AND BACKGROUND CONTROL ///////////////////////////////////////////
testStartYear = input(2019, "Backtest Start Year")
testStartMonth = input(true, "Backtest Start Month")
testStartDay = input(true, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear, testStartMonth ? 1 : testStartMonth, testStartDay ? 1 : testStartDay, 0, 0)
testStopYear = input(2022, "Backtest Stop Year")
testStopMonth = input(true, "Backtest Stop Month")
testStopDay = input(true, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear, testStopMonth ? 1 : testStopMonth, testStopDay ? 1 : testStopDay, 0, 0)
testPeriodBackground = input(title="Color Background?", defval=true)

// CALCULATIONS ///////////////////////////////////////////////////////////////
length = input(27, "Length")
rsi_ma_window = input(10, "RSI MA Window")

rsi = rsi(close, length)
rsi_ma = sma(rsi, rsi_ma_window)

// STRATEGY SIGNALS ///////////////////////////////////////////////////////////
buyCondition = crossover(rsi, rsi_ma)
sellCondition = crossunder(rsi, rsi_ma)

if (buyCondition)
    strategy.entry("Buy", strategy.long)

if (sellCondition)
    strategy.exit("Sell", "Buy")

// PLOTTING //////////////////////////////////////////////////////////////////////
plot(rsi, title="RSI", color=color.blue, linewidth=2)
plot(rsi_ma, title="RSI MA", color=color.orange, linewidth=2)
hline(70, "Overbought Level", color=color.red)
hline(30, "Oversold Level", color=color.green)

// INDICATOR STATUS AND SIGNALS MARKER ///////////////////////////////////////////
bgcolor(testPeriodBackground ? color.new(color.blue, 90) : na, title="Background Color")

// END OF SCRIPT //////////////////////////////////////////////////////////////
```

This script implements the RSI moving average crossover strategy with clear parameters and logic. It includes all the necessary elements from the original code, such as backtesting start/end dates, background control, calculations, trading signals, and plotting.