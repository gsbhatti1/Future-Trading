> Name

SMK-ULTRA-TREND-Dual-Moving-Average-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a9f15710e17d02f890.png)

[trans]
#### Overview
The SMK ULTRA TREND Dual Moving Average Crossover Strategy is a quantitative trading strategy that generates trading signals based on the crossover signals between the 5-day Exponential Moving Average (EMA5) and the 20-day Exponential Moving Average (EMA20). The core idea of this strategy is to capture changes in market trends by using the crossover of short-term and medium-term moving averages. A buy signal is generated when EMA5 crosses above EMA20, and a sell signal is generated when EMA5 crosses below EMA20. Additionally, this strategy incorporates the concepts of support and resistance levels, assisting in judging trend direction and strength by drawing support and resistance lines on the chart.

#### Strategy Principle
The principle of the SMK ULTRA TREND Dual Moving Average Crossover Strategy can be summarized in the following steps:
1. Calculate the 5-day EMA and 20-day EMA. Compared to the Simple Moving Average (SMA), EMA reacts more quickly to price changes, making it more suitable for capturing short-term trends.
2. Determine the crossover situation between EMA5 and EMA20. A buy signal is generated when EMA5 crosses above EMA20, and a sell signal is generated when EMA5 crosses below EMA20.
3. Calculate support and resistance levels. Support and resistance levels are determined by identifying the lowest low and highest high prices over the past 5 trading days.
4. Plot EMA5, EMA20, support lines, and resistance lines on the chart to visually present strategy signals and key price levels.
5. Execute trades according to crossover signals. Open a long position when a buy signal occurs, and close the position when a sell signal occurs.

#### Strategy Advantages
1. Simple and Easy to Use: This strategy features clear logic, uses simple indicators, and has calculation methods that are easy to understand and implement, making it suitable for beginners learning quantitative trading.
2. Strong Adaptability: The dual moving average crossover strategy can be applied to various trading instruments and multiple timeframes. By adjusting the moving average period parameters, it can flexibly adapt to different market characteristics and trading styles.
3. Trend Following: EMA indicators place greater emphasis on recent price changes compared to SMA, enabling timely reflection of price trend changes and facilitating trend-following strategies.
4. Support and Resistance Assistance: Incorporating support and resistance lines helps better grasp trend strength and potential reversal timing, providing additional references for trading decisions.

#### Strategy Risks
1. Frequent Trading: This strategy generates signals based on short-term moving average crossovers, which may lead to frequent trading in ranging markets, increasing transaction costs and drawdown risks.
2. Lag: As a trend-following strategy, the dual moving average crossover strategy inevitably exhibits some lag, potentially missing the best timing for trend initiation or delaying exits during trend reversals.
3. False Signals: In markets with significant noise, moving average crossovers may produce false signals, resulting in poor strategy performance.

#### Strategy Optimization Directions
1. Signal Filtering: Introduce additional technical indicators such as RSI and MACD alongside moving average crossovers to provide secondary confirmation of trading signals, thereby enhancing signal reliability.
2. Dynamic Parameter Optimization: Dynamically adjust moving average period parameters based on market conditions and instrument characteristics to enable the strategy to better adapt to changing market rhythms.
3. Position Management: Dynamically adjust positions based on indicators such as trend strength and volatility—increasing position size during strong trends and reducing position size during unclear trends or increased risk.
4. Stop Loss and Take Profit: Set reasonable stop loss levels and profit targets to control the risk exposure of individual trades and improve the strategy's risk-reward ratio.

#### Summary
The SMK ULTRA TREND Dual Moving Average Crossover Strategy is a simple and practical quantitative trading strategy that captures market trends through crossover signals from EMA5 and EMA20, while also incorporating auxiliary tools like support and resistance lines to aid trading decisions. The advantages of this strategy include clear logic, strong adaptability, and ease of implementation and optimization. However, it may suffer from frequent trading and false signals in ranging markets. These issues can be addressed through signal filtering, parameter optimization, position management, and stop-loss/take-profit mechanisms to improve the strategy's robustness and profitability.

|| 

[/trans]



> Source (PineScript)

``` pinescript
/*backtest
start: 2023-05-17 00:00:00
end: 2024-05-22 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("SMK ULTRA TREND STRATEGY", overlay=true)

// Define the length for EMAs
ema5_length = 5
ema20_length = 20

// Calculate EMAs
ema5 = ta.ema(close, ema5_length)
ema20 = ta.ema(close, ema20_length)

// Plot EMAs
plot(ema5, title="EMA 5", color=color.red )
plot(ema20, title="EMA 20", color=color.blue)

// Generate buy and sell signals
buySignal = ta.crossover(ema5, ema20)
sellSignal = ta.crossunder(ema5, ema20)

// Plot buy and sell signals
plotshape(series=buySignal, location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")
plotshape(series=sellSignal, location=location.abovebar, color=color.red, style=shape.labeldown, text="SELL")

// Execute buy and sell orders
if (buySignal)
    strategy.entry("Buy", strategy.long)
if (sellSignal)
    strategy.close("sell")

// Define support and resistance lengths
pivotLen = 5

// Calculate support and resistance levels
var float supportLevel = na
var float resistanceLevel = na

if (ta.pivotlow(low, pivotLen, pivotLen))
    supportLevel := low[pivotLen]

if (ta.pivothigh(high, pivotLen, pivotLen))
    resistanceLevel := high[pivotLen]

// Plot support and resistance levels
plot(supportLevel, title="Support Level", color=color.green, linewidth=2, style=plot.style_linebr)
plot(resistanceLevel, title="Resistance Level", color=color.red, linewidth=2, style=plot.style_linebr)

```

> Detail

https://www.fmz.com/strategy/452282

> Last Modified

2024-05-23 18:17:07