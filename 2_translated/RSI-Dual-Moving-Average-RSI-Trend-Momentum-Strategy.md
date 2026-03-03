> Name

Dual-Moving-Average-RSI-Trend-Momentum-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/db22dda680df8f0891.png)

[trans]
#### Overview
This strategy is a trend-following trading system that combines dual moving averages with the RSI indicator. It determines market trend direction through crossovers of short-term and long-term moving averages while utilizing RSI for optimal entry points in overbought and oversold areas, achieving a perfect combination of trend following and momentum reversal. The strategy employs percentage-based money management, investing 10% of the total account balance per trade to effectively control risk.

#### Strategy Principles
The strategy uses 10-period and 50-period Simple Moving Averages (SMA) to identify trends. Buy signals are generated when the short-term MA crosses above the long-term MA and RSI is below 30, while sell signals occur when the short-term MA crosses below the long-term MA and RSI is above 70. For position closing, long positions are closed when RSI exceeds 70, and short positions are closed when RSI falls below 30. This design ensures both trend direction accuracy and timely profit-taking at price extremes.

#### Strategy Advantages
1. Combines trend and momentum confirmation to improve trade success rate
2. Implements percentage-based money management for effective risk control
3. Sets clear entry and exit conditions to avoid subjective judgment
4. Fully utilizes RSI indicator's overbought and oversold characteristics
5. Clear strategy logic that is easy to understand and execute
6. Adaptable to different market environments with strong versatility

#### Strategy Risks
1. May generate excessive false signals in ranging markets
2. RSI may remain in overbought/oversold zones during strong trends
3. Dual MA system has inherent lag
4. Fixed parameters may not suit all market conditions
Risk management recommendations:
- Set stop-loss levels
- Dynamically adjust parameters
- Add trend confirmation indicators
- Control single trade size

#### Optimization Directions
1. Introduce adaptive parameter mechanism to dynamically adjust MA periods based on market volatility
2. Add trend strength filter to avoid trading in weak trends
3. Optimize money management system to adjust position size based on market volatility
4. Incorporate additional technical indicators for trade confirmation
5. Develop dynamic stop-loss mechanism to improve capital efficiency

#### Summary
This is a quantitative trading strategy that perfectly combines trend following with momentum reversal. It uses dual moving averages to determine trend direction and RSI to find optimal entry points, ensuring both directional accuracy and timely profit-taking at price extremes. The key to strategy success lies in reasonable parameter settings and effective risk control. Through continuous optimization and improvement, the strategy has the potential to achieve stable returns across different market environments.

||

#### Overview
This strategy is a trend-following trading system that combines dual moving averages with the RSI indicator. It determines market trend direction through crossovers of short-term and long-term moving averages while utilizing RSI for optimal entry points in overbought and oversold areas, achieving a perfect combination of trend following and momentum reversal. The strategy employs percentage-based money management, investing 10% of the total account balance per trade to effectively control risk.

#### Strategy Principles
The strategy uses 10-period and 50-period Simple Moving Averages (SMA) to identify trends. Buy signals are generated when the short-term MA crosses above the long-term MA and RSI is below 30, while sell signals occur when the short-term MA crosses below the long-term MA and RSI is above 70. For position closing, long positions are closed when RSI exceeds 70, and short positions are closed when RSI falls below 30. This design ensures both trend direction accuracy and timely profit-taking at price extremes.

#### Strategy Advantages
1. Combines trend and momentum confirmation to improve trade success rate
2. Implements percentage-based money management for effective risk control
3. Sets clear entry and exit conditions to avoid subjective judgment
4. Fully utilizes RSI indicator's overbought and oversold characteristics
5. Clear strategy logic that is easy to understand and execute
6. Adaptable to different market environments with strong versatility

#### Strategy Risks
1. May generate excessive false signals in ranging markets
2. RSI may remain in overbought/oversold zones during strong trends
3. Dual MA system has inherent lag
4. Fixed parameters may not suit all market conditions
Risk management recommendations:
- Set stop-loss levels
- Dynamically adjust parameters
- Add trend confirmation indicators
- Control single trade size

#### Optimization Directions
1. Introduce adaptive parameter mechanism to dynamically adjust MA periods based on market volatility
2. Add trend strength filter to avoid trading in weak trends
3. Optimize money management system to adjust position size based on market volatility
4. Incorporate additional technical indicators for trade confirmation
5. Develop dynamic stop-loss mechanism to improve capital efficiency

#### Summary
This is a quantitative trading strategy that perfectly combines trend following with momentum reversal. It uses dual moving averages to determine trend direction and RSI to find optimal entry points, ensuring both directional accuracy and timely profit-taking at price extremes. The key to strategy success lies in reasonable parameter settings and effective risk control. Through continuous optimization and improvement, the strategy has the potential to achieve stable returns across different market environments.

||

> Source (PineScript)

```pinescript
/*backtest
start: 2024-10-12 00:00:00
end: 2024-11-11 00:00:00
period: 5m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Super Advanced Strategy", overlay=true)

// Parameter Configuration
shortMAPeriod = input.int(10, title="Short MA Period", minval=1)
longMAPeriod = input.int(50, title="Long MA Period", minval=1)
rsiPeriod = input.int(14, title="RSI Period", minval=1)

// Calculation of Moving Averages
shortMA = ta.sma(close, shortMAPeriod)
longMA = ta.sma(close, longMAPeriod)

// Calculation of RSI
rsi = ta.rsi(close, rsiPeriod)

// Plotting the Moving Averages
plot(shortMA, title="Short MA", color=color.blue, linewidth=2)
plot(longMA, title="Long MA", color=color.red, linewidth=2)

// Adding horizontal lines for overbought and oversold levels
hline(70, "Overbought", color=color.red, linestyle=hline.style_dashed)
hline(30, "Oversold", color=color.green, linestyle=hline.style_dashed)

// Entry Conditions
buyCondition = (shortMA > longMA) and (rsi < 30)
sellCondition = (shortMA < longMA) and (rsi > 70)

// Placing Orders for Buy
if (buyCondition)
    strategy.entry("Buy", strategy.long)

// Placing Orders for Sell
if (sellCondition)
    strategy.entry("Sell", strategy.short)

// Closing Positions
if (rsi > 70)
    strategy.close("Buy")

if (rsi < 30)
    strategy.close("Sell")

// Displaying Buy and Sell signals on the chart
plotshape(buyCondition, style=shape.labelup, location=location.belowbar, color=color.green, size=size.small, title="Buy Signal", text="BUY")
plotshape(sellCondition, style=shape.labeldown, location=location.abovebar, color=color.red, size=size.small, title="Sell Signal", text="SELL")

```

> Detail

https://www.fmz.com/strategy/471688

> Last Modified

2024-11-12 14:34:17