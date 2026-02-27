> Source (PineScript)

``` pinescript
/*backtest
start: 2023-05-22 00:00:00
end: 2024-05-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI Strategy with Customizable MA and StochRSI Alert", overlay=true)

// Define RSI levels for buy and sell signals
rsiOverbought = input(70, title="RSI Overbought Level")
rsiOversold = input(30, title="RSI Oversold Level")

// Select the type of moving average
maType = input.string("EMA", title="MA Type", options=["EMA", "SMA", "HMA", "WMA"])

// Define the length of the moving averages
maShortLength = input(12, title="MA Short Length")
maLongLength = input(26, title="MA Long Length")

// Determine whether to display the moving averages
showShortMA = input(true, title="Show Short Moving Average")
showLongMA = input(true, title="Show Long Moving Average")

// Function to select the type of moving average
f_ma(src, length, type) =>
    switch type
        "SMA" => ta.sma(src, length)
        "EMA" => ta.ema(src, length)
        "HMA" => ta.hma(src, length)
        "WMA" => ta.wma(src, length)

// Calculate the moving averages
maShort = showShortMA ? f_ma(close, maShortLength, maType) : na
maLong = showLongMA ? f_ma(close, maLongLength, maType) : na

// Calculate RSI value
rsiValue = ta.rsi(close, 14)

// Generate buy and sell signals
buySignal = (rsiValue > rsiOverbought and close > maShort)
sellSignal = (rsiValue < rsiOversold or ta.crossunder(maLong, maShort))

// Plot indicators on the chart
plot(rsiValue, title="RSI", color=color.red, style=plot.style_histogram)
hline(rsiOverbought, "RSI Overbought Level", color=color.red)
hline(rsiOversold, "RSI Oversold Level", color=color.green)

// Plot moving averages on the chart
if showShortMA
    plot(maShort, title="Short MA", color=color.blue)
if showLongMA
    plot(maLong, title="Long MA", color=color.orange)

// Place buy and sell orders based on signals
strategy.entry("Buy", strategy.long, when=buySignal)
strategy.exit("Close Long Position", "Buy", trailpercent=10)
strategy.close("Sell", when=sellSignal)
```

This Pine Script defines a trading strategy that uses RSI combined with customizable moving averages (MA) and StochRSI for generating buy and sell signals. The script includes input parameters for setting the RSI levels, MA types and lengths, and whether to display these indicators on the chart. It also provides functions to calculate the moving averages and RSI values, and generates trading signals based on these calculations.