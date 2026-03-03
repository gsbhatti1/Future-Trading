This strategy is a quantitative trading strategy based on the Relative Strength Index (RSI) indicator. The strategy uses the RSI indicator to determine overbought and oversold conditions in the market and executes buy and sell orders at appropriate times. Additionally, the strategy introduces the concept of the Martingale system, increasing the trading position size when certain conditions are met.

The main ideas of this strategy are as follows:
1. Calculate the value of the RSI indicator.
2. Execute a buy order when the RSI indicator crosses above the oversold level, and execute a sell order when the RSI indicator crosses below the overbought level.
3. Set take profit and stop loss levels, and close the position when the price reaches these levels.
4. Introduce the Martingale system, multiplying the position size of the next trade by a factor when the previous trade results in a loss.

#### Strategy Principle
1. Calculation of the RSI indicator: Use the `ta.rsi` function to calculate the value of the RSI indicator, requiring the setting of the RSI period (default is 14).
2. Buy condition: Execute a buy order when the RSI indicator crosses above the oversold level (default is 30).
3. Sell condition: Execute a sell order when the RSI indicator crosses below the overbought level (default is 70).
4. Take profit and stop loss: Set the percentage for take profit and stop loss (both default to 0%), and close the position when the price reaches these levels.
5. Martingale system: Set the initial position size (default is 1) and the Martingale multiplier (default is 2). When the previous trade results in a loss, multiply the position size of the next trade by the Martingale multiplier.

#### Strategy Advantages
1. The RSI indicator is a widely used technical indicator that can effectively determine overbought and oversold conditions in the market, providing a basis for trading decisions.
2. The strategy logic is clear and easy to understand and implement.
3. The introduction of the Martingale system can increase the profitability of the strategy to a certain extent. When the market experiences consecutive losses, the strategy seeks greater profits by increasing the position size.
4. The strategy can be flexibly adjusted according to market characteristics and personal risk preferences, such as the RSI period, overbought/oversold levels, take profit and stop loss percentages, etc.

#### Strategy Risks
1. The RSI indicator may sometimes fail to provide effective signals, especially when the market trend is strong. In such cases, the RSI indicator may remain in the overbought or oversold state for a long time, while the market price continues to rise or fall.
2. Although the Martingale system can increase the profitability of the strategy, it also amplifies the risk of the strategy. When the market experiences consecutive losses, the position size of the strategy will increase sharply, potentially leading to the risk of liquidation.
3. The strategy does not set take profit and stop loss percentages (both are 0%), which means that the strategy will not actively take profit or stop loss after opening a position. This may cause the strategy to bear greater risk when the market fluctuates dramatically.

#### Strategy Optimization Directions
1. Consider introducing other technical indicators, such as Moving Averages (MA), Bollinger Bands, etc., to improve the signal quality and reliability of the strategy. These indicators can be used in combination with the RSI indicator to form more complex trading conditions.
2. Optimize the Martingale system. A maximum position size can be set to avoid unlimited position increases. Alternatively, the use of the Martingale system can be suspended after a certain number of consecutive losses to control risk.
3. Set reasonable take profit and stop loss percentages. Stop loss can help the strategy stop losses in a timely manner and avoid excessive losses, while take profit can help the strategy lock in profits in a timely manner and avoid profit retracements.
4. Optimize the parameters of the RSI indicator. Through backtesting and parameter optimization, the most suitable RSI period, overbought/oversold levels, and other parameters for the current market and underlying asset can be found.

#### Summary
This strategy is an RSI-based quantitative trading strategy that introduces the Martingale system. The advantages of this strategy lie in the effectiveness of the RSI indicator and the clarity of its logic. However, it also has certain risks such as signal failure from the RSI indicator and amplified risk from the Martingale system. Future optimization could include introducing additional technical indicators, optimizing the Martingale system, setting take profit and stop loss percentages, and optimizing RSI parameters. Overall, this strategy requires continuous improvement and adaptation to changing market conditions.

---

**Note:** The code block for the `ta.rsi` function has been kept as is.