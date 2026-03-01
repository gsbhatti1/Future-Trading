``` pinescript
/*backtest
start: 2023-02-19 00:00:00
end: 2024-02-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA Crossover Strategy with Target", shorttitle="EMACross", overlay=true)

// Define input parameters
fastLength = input(3, title="Fast EMA Length")
slowLength = input(30, title="Slow EMA Length")
profitPercentage = input(100.0, title="Profit Percentage")

// Calculate EMAs
emaFast = ta.ema(close, fastLength)
emaSlow = ta.ema(close, slowLength)

// Plot EMAs on the chart
plot(emaFast, color=color.blue, title="Fast EMA")
plot(emaSlow, color=color.red, title="Slow EMA")

// Determine crossover conditions
var float goldenCrossPrice = na
if (crossabove(emaFast, emaSlow))
    strategy.entry("Long", strategy.long)
    goldenCrossPrice := close

var float deathCrossPrice = na
if (crossbelow(emaFast, emaSlow))
    strategy.close("Long")
    deathCrossPrice := close

// Set profit target
profitTarget = goldenCrossPrice * (1 + profitPercentage / 100)

// Exit on profit target or stop loss
if (close > profitTarget)
    strategy.exit("Profit Target", "Long")

// Risk and Solution Analysis
// The dual EMA indicator belongs to the trend tracking strategy, which cannot predict or avoid the risks of major fluctuations or special events. The risk control method is to appropriately shorten the holding period and stop loss in time.
// The EMA indicator is sensitive to parameters. Improper fast and slow line parameter settings may lead to poor strategy performance. The optimal parameters can be found through systematic backtesting optimization methods.

// Optimization Directions
// The following aspects of this strategy can be further optimized:
// 1. Optimize the parameters of the fast and slow EMA lines to find the best parameter combination.
// 2. Increase other indicators to build multi-factor models and improve signal accuracy, such as introducing BOLL derivatives indicators.
// 3. Add stop loss strategies to control single transaction risks, such as introducing trailing stops.
// 4. The optimal parameters may differ across products. Consider factor decomposition to find parameters most suitable for each product.
// 5. Machine learning methods can be tried for time-driven hyperparameter optimization.
// 6. Explore K-line pattern recognition at key technical positions to capture larger degree reversals.

// Conclusion
// In summary, this is a simple and practical dual EMA trend tracking strategy. It automatically adjusts positions by determining market stages through fast and slow EMA crosses. The strategy logic is concise and clear, easy to implement quantitatively. At the same time, there is room for further optimization to improve signal accuracy and control risks to make it a high-quality quantitative strategy for actual trading.
```

This translation keeps all code blocks, numbers, and formatting as specified while translating the human-readable text into English.