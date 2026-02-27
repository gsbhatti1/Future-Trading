> Name

Three-Week-High-Low-Momentum-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/f10c35ac3048ee6abd.png)

[trans]

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
3. Dynamic Stop-Loss Mechanism: Implement adaptive stop-loss strategies, such as trailing stops or ATR-based stop losses, to better manage risk.
4. Signal Filter: Add additional technical indicators or market sentiment indicators, like RSI or MACD, to reduce false signals.
5. Entry Optimization: Consider using limit orders or observing ranges instead of direct market entry orders to achieve better execution prices.
6. Position Sizing Management: Develop dynamic position sizing strategies based on market volatility and account risk tolerance to adjust the size of each trade.
7. Market State Identification: Incorporate logic for identifying different market states (trends, consolidations, high volatility) to use appropriate trading parameters in different environments.

#### Summary

The three-week high-low momentum trading strategy is a simple yet effective method for medium-term trend tracking. By comparing the latest high, latest closing price, and the closing price from three weeks ago, the strategy can capture price breakouts and momentum changes. Its advantages include filtering short-term noise, capturing medium-term trends, and having an intuitive logic that is easy to understand and implement. However, it also faces challenges such as false breakouts, signal lagging, and inadequate risk management.

Future optimization directions should focus on multi-time frame analysis, volume confirmation, dynamic risk management, and market state identification. Through these improvements, the strategy can perform more robustly across different market environments and provide reliable decision support for traders.

In summary, this strategy serves as a good starting point for quantitative trading. By continuous optimization and improvement, it has the potential to become a powerful trading tool. However, investors should exercise caution when applying it, fully understanding market risks and aligning their risk tolerance with investment goals.