#### Overview

The BTST High-Probability Breakout Strategy with Selective Stock Screening System is a quantitative approach designed for intraday and overnight trading, aimed at identifying and capturing short-term price momentum breakthrough opportunities. This strategy combines time-specific price movement screening, classic technical pattern confirmation, and dynamic resistance breakout analysis to construct a multi-layered trading decision system. The core of the strategy lies in precisely filtering targets with a 2-3% gain at 3 PM, further confirming bullish signals through candlestick pattern analysis, and setting reasonable entry and exit mechanisms to avoid overextension risks, thereby achieving high-probability short-term trading opportunities.

#### Strategy Principles

The operational principles of this strategy are based on multi-condition progressive filtering and confirmation:

1. **Initial Screening (3 PM)**: The strategy first screens for instruments with a daily gain of 2-3% at precisely 3 PM. This specific time window selection is based on the assumption that market momentum may continue to develop into the close.

2. **Daily Candlestick Pattern Analysis**: The strategy incorporates three classic bullish pattern assessments:
   - Bullish Engulfing Pattern: When the current day's candlestick completely engulfs the previous day's candlestick, and the current day's closing price is higher than its opening price.
   - Morning Star Pattern: Composed of three candlesticks, showing a transition from bearish to bullish sentiment.
   - Three White Soldiers Pattern: Three consecutive positive candlesticks with each closing price higher than the previous candlestick's closing price.

3. **30-Minute Resistance Breakout**: The strategy dynamically sets resistance levels every 30 minutes (the highest point of the current 30-minute period) and determines whether the price breaks through this resistance level, serving as a potential signal for continued upward movement or profit-taking.

4. **Avoiding Overextension**: The strategy calculates intraday gains to avoid instruments that have already risen more than 5% or fallen more than 10%, mitigating potential pullback risks.

5. **Next-Day Watchlist**: Combining the above conditions, instruments that meet the initial screening, bullish pattern confirmation, and are not overextended are added to the next-day watchlist.

6. **Exit Strategy**: Simulating pre-market and opening observations, if an instrument gaps up by more than 2% and the price remains above the previous day's low, positions are maintained for at least 15 minutes, awaiting potential further upside.

7. **Buy and Sell Triggers**: Buy signals are based on a combination of bullish patterns, initial screening conditions, and non-overextension assessment; sell signals rely on resistance level breakout conditions and non-overextension status.

#### Strategy Advantages

1. **Temporal Precision**: The strategy screens at the specific time point of 3 PM, effectively capturing a critical stage of intraday momentum development, providing early warning for potential continuation moves the next day.

2. **Multiple Confirmation Mechanism**: By combining pe