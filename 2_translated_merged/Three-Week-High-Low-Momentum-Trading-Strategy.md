> Name

Three-Week-High-Low-Momentum-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/f10c35ac3048ee6abd.png)

[trans]

#### Overview

This strategy is a momentum trading approach based on three-period high and low points. It uses price data from the recent three weeks to identify potential buy and sell opportunities. The strategy mainly focuses on the relationship between the latest high, latest closing price, and the closing price from three weeks ago, generating trading signals by comparing these price levels. This approach aims to capture mid-term price trends while avoiding the influence of short-term market noise.

#### Strategy Principle

The core principles of this strategy include the following key elements:

1. Indicator Calculation:
   - Latest High: Use ta.highest() function to calculate the highest price over the last 30 trading days (about 4 weeks).
   - Latest Close: Use close[1] to get the previous day's closing price.
   - Closing Price from Three Weeks Ago: Use close[30] to get the closing price from 30 trading days ago.

2. Buy Conditions:
   - Condition 1: Latest high is greater than or equal to the closing price from three weeks ago.
   - Condition 2: Latest closing price is greater than the closing price from three weeks ago.

3. Sell Conditions:
   - Trigger sell signal when the latest closing price is greater than the closing price from three weeks ago.

4. Trade Execution:
   - When buy signal triggers, enter long position.
   - When sell signal triggers, close current long position.

5. Visualization:
   - Use plotshape() function to mark buy and sell signals on chart.

This design aims to capture upward momentum when price breaks through the level from three weeks ago, while timely closing positions to protect profits when price retreats.

#### Strategy Advantages

1. Mid-term Trend Capture: By comparing current price with price level from three weeks ago, strategy can effectively identify formation and continuation of mid-term trends.

2. Noise Filtering: Using three-period timeframe helps filter out short-term market fluctuations, improving signal reliability.

3. Dynamic Adaptation: Strategy continuously updates judgment criteria based on latest price data, able to dynamically adapt to market changes.

4. Risk Management: By setting clear sell conditions, strategy can timely close positions when market turns, effectively controlling risk.

5. Simple and Understandable: Strategy logic is intuitive, easy to understand and implement, suitable for both beginners and experienced traders.

6. Visualization Support: Buy and sell signals clearly marked on chart, convenient for traders to intuitively judge and backtest analysis.

#### Strategy Risks

1. False Breakout Risk: In range-bound market, frequent false breakouts may occur, leading to excessive trading and unnecessary commission losses.

2. Lagging Nature: Using three-period historical data may cause signal lag, missing best entry timing in fast-changing market.

3. Single Timeframe Limitation: Relying solely on three-period data may overlook important market information from other timeframes.

4. Lack of Stop-loss Mechanism: Current strategy has no explicit stop-loss mechanism, may face large losses during violent market fluctuations.

5. Over-reliance on Closing Price: Strategy mainly judges based on closing price, may ignore important intraday price movements.

6. Lack of Volume Confirmation: Not considering volume factor may generate false signals during low-volume periods.

#### Strategy Optimization Directions

1. Multi-timeframe Analysis: Integrate data from multiple timeframes, such as daily, weekly and monthly, to provide more comprehensive market perspective.

2. Introduce Volume Indicators: Combine volume analysis to improve signal reliability, especially in breakout confirmation.

3. Dynamic Stop-loss Mechanism: Implement adaptive stop-loss strategy, such as trailing stop or ATR-based stop, to better manage risk.

4. Signal Filter: Add additional technical indicators or market sentiment indicators, such as RSI or MACD, to reduce false signals.

5. Entry Optimization: Consider using limit order or observation zone instead of direct market order entry, to get better execution price.

6. Position Management: Implement dynamic position sizing strategy, adjust position size for each trade based on market volatility and account risk.

7. Market State Recognition: Add market state (trend, consolidation, high volatility) identification logic, use different trading parameters in different market environments.

8. Backtesting and Optimization: Conduct extensive historical data backtesting, optimize strategy parameters, such as time period, condition thresholds, etc.

#### Summary

Three-period high-low momentum trading strategy is a simple yet effective mid-term trend-following method. By comparing latest high, latest closing price with closing price from three weeks ago, strategy can capture price breakouts and momentum changes. Its advantages lie in filtering short-term noise, capturing mid-term trends, and having intuitive and easily understandable logic. However, strategy also faces challenges such as false breakouts, signal lag, and insufficient risk management.

Future optimization directions should focus on multi-timeframe analysis, volume confirmation, dynamic risk management, and market state recognition. Through these improvements, strategy has potential to perform more stably in different market environments, providing traders with more reliable decision support.

Overall, this strategy provides a good starting point for quantitative trading. Through continuous optimization and improvement, it has potential to become a powerful trading tool. However, investors should be cautious when actually applying it, fully recognize market risks, and use strategy in combination with their own risk tolerance and investment objectives.

[/trans]

> Source (PineScript)

``` pinescript
/*backtest
start: 2024-06-28 00:00:00
end: 2024-07-28 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Buy and Sell Strategy", overlay=true)

// Calculate the latest high, close, and volume
latestHigh = ta.highest(high, 30) // 4 weeks = 30 trading days
latestClose = close[1]


// Calculate the high, close, 
threeWeeksAgoClose = close[30] // 4 weeks = 30 trading days + 1 current day


// Condition 1: Buy if latest high >= 4 weeks ago close
condition1 = latestHigh >= threeWeeksAgoClose

// Condition 2: Buy if latest close > 4 weeks ago close
condition2 = latestClose > threeWeeksAgoClose



// Generate buy and sell signals
buySignal = condition1  
sellSignal = condition2

// Entry and exit logic using if statements
if buySignal
    strategy.entry("Buy", strategy.long)
    
if sellSignal
    strategy.close("Buy")

// Plotting buy and sell signals on the chart
plotshape(buySignal, color=color.green, style=shape.labelup, location=location.belowbar, text="Buy")
plotshape(sellSignal, color=color.red, style=shape.labeldown, location=location.abovebar, text="Sell")


```

> Detail

https://www.fmz.com/strategy/458128

> Last Modified

2024-07-30 10:44:11