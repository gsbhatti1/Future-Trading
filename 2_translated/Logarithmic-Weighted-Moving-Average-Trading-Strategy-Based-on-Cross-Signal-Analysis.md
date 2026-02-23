> Name

Logarithmic-Weighted-Moving-Average-Trading-Strategy-Based-on-Cross-Signal-Analysis-基于对数加权移动平均交叉信号的量化交易策略

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c30feb4411a822738c.png)

[trans]
#### Overview
This strategy is a quantitative trading system based on logarithmic transformation and Weighted Moving Average (WMA) crossovers. It reduces market noise by applying logarithmic transformation to price data and generates trading signals through the intersection of short-term and long-term WMAs. The core concept is to smooth price fluctuations in logarithmic space for more stable trend identification.

#### Strategy Principle
The strategy first applies logarithmic transformation to closing prices to minimize the impact of extreme price movements. It then calculates short-term (5-period) and long-term (20-period) weighted moving averages. The system generates long signals when the short-term WMA crosses above the long-term WMA, and short signals when the short-term WMA crosses below the long-term WMA. Trend transition points are identified through moving average crossovers in logarithmic space, enabling effective trend following.

#### Strategy Advantages
1. Logarithmic transformation effectively reduces the impact of extreme price movements, leading to more stable trend identification.
2. Weighted moving averages respond more quickly to price changes compared to simple moving averages.
3. Dual moving average crossovers provide clear signals, avoiding false signals that might occur with single indicators.
4. Automated trading execution reduces delays and emotional impacts from manual operations.
5. Real-time alert system ensures no important trading opportunities are missed.

#### Strategy Risks
1. May generate excessive false signals in ranging markets, leading to increased trading costs.
2. Logarithmic transformation might delay signal generation in extreme market conditions.
3. Fixed moving average periods may not be suitable for all market environments.
Risk management through stop-loss conditions and position sizing is recommended, along with signal confirmation using additional technical indicators.

#### Strategy Optimization
1. Introduce adaptive moving average periods that dynamically adjust based on market volatility.
2. Add volume and other auxiliary indicators for signal confirmation.
3. Implement trend strength filters to avoid trading in weak trend environments.
4. Optimize stop-loss and take-profit conditions for better capital efficiency.
5. Consider adding drawdown control mechanisms to prevent significant losses.

#### Summary
This is a trend-following strategy combining logarithmic transformation and weighted moving averages. It reduces price volatility impact through logarithmic transformation and captures trend transition points using dual moving average crossovers. The strategy has clear logic and good operability but requires careful risk management in ranging markets. Through parameter optimization and additional indicator integration, this strategy has potential for improved performance.

||

#### Overview
This strategy is a quantitative trading system based on logarithmic transformation and Weighted Moving Average (WMA) crossovers. It reduces market noise by applying logarithmic transformation to price data and generates trading signals through the intersection of short-term and long-term WMAs. The core concept is to smooth price fluctuations in logarithmic space for more stable trend identification.

#### Strategy Principle
The strategy first applies logarithmic transformation to closing prices to minimize the impact of extreme price movements. It then calculates short-term (5-period) and long-term (20-period) weighted moving averages. The system generates long signals when the short-term WMA crosses above the long-term WMA, and short signals when the short-term WMA crosses below the long-term WMA. Trend transition points are identified through moving average crossovers in logarithmic space, enabling effective trend following.

#### Strategy Advantages
1. Logarithmic transformation effectively reduces the impact of extreme price movements, leading to more stable trend identification.
2. Weighted moving averages respond more quickly to price changes compared to simple moving averages.
3. Dual moving average crossovers provide clear signals, avoiding false signals that might occur with single indicators.
4. Automated trading execution reduces delays and emotional impacts from manual operations.
5. Real-time alert system ensures no important trading opportunities are missed.

#### Strategy Risks
1. May generate excessive false signals in ranging markets, leading to increased trading costs.
2. Logarithmic transformation might delay signal generation in extreme market conditions.
3. Fixed moving average periods may not be suitable for all market environments.
Risk management through stop-loss conditions and position sizing is recommended, along with signal confirmation using additional technical indicators.

#### Strategy Optimization
1. Introduce adaptive moving average periods that dynamically adjust based on market volatility.
2. Add volume and other auxiliary indicators for signal confirmation.
3. Implement trend strength filters to avoid trading in weak trend environments.
4. Optimize stop-loss and take-profit conditions for better capital efficiency.
5. Consider adding drawdown control mechanisms to prevent significant losses.

#### Summary
This is a trend-following strategy combining logarithmic transformation and weighted moving averages. It reduces price volatility impact through logarithmic transformation and captures trend transition points using dual moving average crossovers. The strategy has clear logic and good operability but requires careful risk management in ranging markets. Through parameter optimization and additional indicator integration, this strategy has potential for improved performance.

||

> Source (PineScript)

```pinescript
/*backtest
start: 2022-02-09 00:00:00
end: 2025-02-06 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=6
strategy("Logarithmic WMA Trading Strategy", overlay=true)

// Parameters
shortWMA_length = input.int(5, title="Short WMA (5)")
longWMA_length = input.int(20, title="Long WMA (20)")

// Logarithm Calculation for Prices
log_close = math.log(close)  // Calculate log of closing prices

// Calculation of Logarithmic WMAs
log_shortWMA = ta.wma(log_close, shortWMA_length)  // Short-term WMA (Log)
log_longWMA = ta.wma(log_close, longWMA_length)    // Long-term WMA (Log)

// Reverting to Normal Scale for WMAs
shortWMA = math.exp(log_shortWMA)  // Reverted short-term WMA from log scale
longWMA = math.exp(log_longWMA)    // Reverted long-term WMA from log scale

// Entry Conditions for Trading
longCondition = ta.crossover(shortWMA, longWMA)  // Long signal when short-term WMA crosses above long-term WMA
shortCondition = ta.crossunder(shortWMA, longWMA)  // Short signal when short-term WMA crosses below long-term WMA

// Plotting WMAs
plot(shortWMA, color=color.green, title="Short WMA (Log)", linewidth=2, style=plot.style_line)
plot(longWMA, color=color.red, title="Long WMA (Log)", linewidth=2, style=plot.style_line)

// Trading Entry Logic
if (longCondition)
    strategy.entry("Buy", strategy.long)

if (shortCondition)
    strategy.entry("Sell", strategy.short)

// Alert Function for Trading Signals
if (longCondition)
    alert("Buy Signal: Short WMA (Log) crosses above Long WMA (Log)", alert.freq_once_per_bar_close)

if (shortCondition)
    alert("Sell Signal: Short WMA (Log) crosses below Long WMA (Log)", alert.freq_once_per_bar_close)
```

> Detail

https://www.fmz.com/strategy/481094

> Last Modified

2025-02-08 14:53:53