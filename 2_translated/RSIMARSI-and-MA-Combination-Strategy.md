> Name

RSI with Customizable MA and StochRSI Alert Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/163ce4ff31fe3cedf6d.png)

[trans]
#### Overview
This strategy combines the RSI indicator with customizable moving averages (MA) and Stochastic RSI alerts to generate trading signals. The RSI is used to determine whether the market is overbought or oversold, while the MA is used to identify price trends. A buy signal is generated when RSI is overbought and the price is above the MA; a sell signal is generated when RSI is oversold or when the MA produces a death cross. Additionally, the strategy introduces the Stochastic RSI indicator (StochRSI) as an auxiliary judgment, and prompts will be marked on the chart when StochRSI generates a signal.

#### Strategy Principle
1. Calculate the RSI indicator value to determine whether the market is overbought (>70) or oversold (<30).
2. Calculate the MA of a custom period, including EMA, SMA, HMA, and WMA types, and decide whether to display them on the chart based on parameter settings.
3. When RSI is overbought and the closing price is higher than the MA, a buy signal is generated; when RSI is oversold or the MA produces a death cross, a sell signal is generated.
4. Introduce the StochRSI indicator as an auxiliary judgment. When StochRSI is overbought (>70) or oversold (<30), prompts will be marked on the chart, but no actual trading signals are generated.

#### Strategy Advantages
1. The organic combination of the RSI and MA indicators can effectively capture trend movements and overbought/oversold opportunities.
2. The type and parameters of the MA can be freely set with high flexibility, allowing adjustments based on different market characteristics.
3. The introduction of the StochRSI indicator as an auxiliary judgment provides more reference for trading decisions.
4. The code logic is clear and readable, making it easy to understand and support further development.

#### Strategy Risks
1. Both RSI and MA are lagging indicators and may generate misleading signals during the early stages of trend reversal.
2. Improper parameter settings may result in signals being generated too early or too late, affecting overall returns.
3. Lack of stop-loss and position management mechanisms may lead to greater risks when market fluctuations are significant.

#### Strategy Optimization Directions
1. Introduce more leading indicators such as volatility to predict trend changes in advance.
2. Filter buy and sell signals, requiring both RSI and MA to meet certain conditions simultaneously before generating a signal, to improve signal accuracy.
3. Add stop-loss and position management modules to the strategy to control single transaction risk and overall risk.
4. Perform parameter optimization on the strategy to find the best parameter combination.
5. Consider adding different cycles or multiple varieties to fully utilize the联动 relationship between different cycles or varieties.

#### Summary
By combining the RSI and MA indicators, this strategy can effectively capture trend movements and overbought/oversold opportunities. Additionally, it introduces the StochRSI indicator as an auxiliary judgment, making the overall approach simple and clear. However, the strategy also has some limitations, such as the lack of risk control measures and potential signal inaccuracies. Future improvements could include adding more indicators, optimizing signal rules, and incorporating risk management modules to achieve more stable returns.
[/trans]

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

// Set RSI levels for buy and sell signals
rsiOverbought = input(70, title="RSI Overbought Level")
rsiOversold = input(30, title="RSI Oversold Level")

// Choose the type of moving average
maType = input.string("EMA", title="MA Type", options=["EMA", "SMA", "HMA", "WMA"])

// Set MA lengths
maShortLength = input(12, title="MA Short Length")
maLongLength = input(26, title="MA Long Length")

// Decide whether to show the short and long MAs on the chart
showShortMA = input(true, title="Show Short Moving Average")
showLongMA = input(true, title="Show Long Moving Average")

// Function for choosing the type of moving average
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
buySignal = rsiValue > rsiOverbought and close > maShort
sellSignal = rsiValue < rsiOversold or crossover(maLong, maShort)
```