```markdown
#### Overview

This strategy is a momentum trading approach based on three-week high and low points. It utilizes price data from the recent three weeks to identify potential buying and selling opportunities. The strategy primarily focuses on the relationship between the latest high, the latest closing price, and the closing price from three weeks ago, generating trading signals by comparing these price levels. This method aims to capture medium-term price trends while avoiding the impact of short-term market noise.

#### Strategy Principle

The core principles of this strategy include the following key elements:

1. Indicator Calculations:
   - Latest High: Uses the `ta.highest()` function to calculate the highest price over the last 30 trading days (approximately 4 weeks).
   - Latest Close: Uses `close[1]` to get the closing price of the previous day.
   - Three Weeks Ago Close: Uses `close[30]` to get the closing price from 30 trading days ago.

2. Buy Conditions:
   - Condition 1: The latest high is greater than or equal to the closing price from three weeks ago.
   - Condition 2: The latest closing price is greater than the closing price from three weeks ago.

3. Sell Condition:
   - Triggers a sell signal when the latest closing price is greater than the closing price from three weeks ago.

4. Trade Execution:
   - Enters a long position when the buy signal is triggered.
   - Closes the current long position when the sell signal is triggered.

5. Visualization:
   - Uses the `plotshape()` function to mark buy and sell signals on the chart.

This design aims to capture upward momentum when the price breaks above the level from three weeks ago, while promptly closing positions to protect profits when the price falls back.

#### Strategy Advantages

1. Medium-Term Trend Capture: By comparing current prices with levels from three weeks ago, the strategy effectively identifies the formation and continuation of medium-term trends.
2. Noise Filtering: Using a three-week time frame helps filter out short-term market fluctuations, improving the reliability of signals.
3. Dynamic Adaptation: The strategy continuously updates its decision criteria based on the latest price data, allowing it to dynamically adapt to market changes.
4. Risk Management: Through clear sell conditions, the strategy can close positions promptly when the market turns, effectively controlling risk.
5. Simple and Understandable: The strategy logic is intuitive, easy to understand and implement, suitable for both novice and experienced traders.
6. Visual Support: Buy and sell signals are clearly marked on the chart, facilitating intuitive judgment and backtesting analysis for traders.

#### Strategy Risks

1. False Breakout Risk: In sideways markets, frequent false breakouts may occur, leading to excessive trading and unnecessary transaction fee losses.
2. Lagging Nature: Using historical data from three weeks may result in lagging signals, potentially missing optimal entry points in rapidly changing markets.
3. Single Time Frame Limitation: Relying solely on three-week data may overlook important market information from other time frames.
4. Lack of Stop-Loss Mechanism: The current strategy lacks a clear stop-loss mechanism, potentially facing significant losses during severe market fluctuations.
5. Over-reliance on Closing Prices: The strategy mainly bases its judgments on closing prices, potentially ignoring important intraday price movements.
6. Lack of Volume Confirmation: Not considering volume factors may lead to false signals during periods of low trading volume.

#### Strategy Optimization Directions

1. Multi-Time Frame Analysis: Integrate data from multiple time frames, such as daily, weekly, and monthly, to provide a more comprehensive market perspective.
2. Incorporate Volume Indicators: Combining volume analysis can improve signal reliability, especially in breakout confirmation.
3. Dynamic Stop-Loss Mechanism: Implement adaptive stop-loss strategies like trailing stops or ATR-based stop-losses to better manage risk.
4. Signal Filter: Add additional technical indicators or market sentiment indicators, such as RSI or MACD, to reduce false signals.
5. Optimize Entry Points: Consider using limit orders or observing price ranges before entering positions to achieve better entry prices.
6. Position Sizing: Develop dynamic position sizing strategies based on market volatility and account risk tolerance to adjust trade sizes accordingly.
7. Market Condition Identification: Incorporate logic for identifying different market conditions (trends, consolidation, high volatility) and apply appropriate trading parameters in each condition.

#### Conclusion

The three-week high-low momentum trading strategy is a simple yet effective method for tracking medium-term trends. By comparing the latest high, latest closing price, and the closing price from three weeks ago, this strategy can capture price breaks and momentum changes. Its advantages include filtering short-term noise, capturing medium-term trends, and having an intuitive and easy-to-understand logic. However, it faces challenges such as false breakouts, lagging signals, and insufficient risk management.

Future optimization directions should focus on multi-time frame analysis, incorporating volume confirmation, implementing dynamic risk management, and identifying market conditions. These improvements can help the strategy perform more robustly across different market environments, providing reliable decision support for traders.

In summary, this strategy serves as a good starting point for quantitative trading, with potential to become a powerful tool through continuous optimization and improvement. However, investors should exercise caution when applying it, fully understanding market risks and aligning their risk tolerance and investment goals with the use of this strategy.
```