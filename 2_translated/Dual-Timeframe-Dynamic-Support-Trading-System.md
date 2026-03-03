``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-04 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Demo GPT - Bull Market Support Band", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_value=0.1, slippage=3)

start_date = input(timestamp("2018-01-01 00:00 +0000"), title="Start Date")
end_date = input(timestamp("2069-12-31 00:00 +0000"), title="End Date")

lsmaLength = input.int(20, title="Long SMA Length", minval=1)
lemaLength = input.int(21, title="Long EMA Length", minval=1)
customLongTimeframe = input.timeframe("W", title="Long Timeframe")  // Long Timeframe
ssmaLength = input.int(50, title="Short SMA Length", minval=1)
semaLength = input.int(51, title="Short EMA Length", minval=1)
customShortTimeframe = input.timeframe("D", title="Short Timeframe")  // Short Timeframe

source = close

// Calculate SMA and EMA for the long timeframe
smaLong = ta.sma(source, lsmaLength)
emaLong = ta.ema(source, lemaLength)
outSmaLong = request.security(syminfo.tickerid, customLongTimeframe, smaLong)
outEmaLong = request.security(syminfo.tickerid, customLongTimeframe, emaLong)

// Calculate SMA and EMA for the short timeframe
smaShort = ta.sma(source, ssmaLength)
emaShort = ta.ema(source, semaLength)
outSmaShort = request.security(syminfo.tickerid, customShortTimeframe, smaShort)
outEmaShort = request.security(syminfo.tickerid, customShortTimeframe, emaShort)

// Trading logic
longCondition = (ta.crossover(outEmaLong, outSmaLong) and ta.crossover(outEmaShort, outSmaShort))
shortCondition = (ta.crossunder(outEmaShort, outSmaShort))

if (time >= start_date and time <= end_date)
    if longCondition
        strategy.entry("Long", strategy.long)

    if shortCondition
        strategy.close("Long")

// Exit conditions
if (time > end_date or ta.crossover(outEmaLong, outSmaLong))
    strategy.close("Long")
```

This Pine Script translates the provided trading strategy document into English. The comments and variable names have been translated to maintain clarity and understanding in an English-speaking context.