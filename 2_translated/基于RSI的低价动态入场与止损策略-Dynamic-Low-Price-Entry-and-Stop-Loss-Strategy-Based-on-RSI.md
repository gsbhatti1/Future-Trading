#### Strategy Optimization Directions

1. Multi-Indicator Combination: Consider introducing other technical indicators such as moving averages, Bollinger Bands, etc., to be used in conjunction with RSI to improve signal reliability.

2. Adaptive Parameters: Develop a mechanism to automatically adjust the RSI calculation period and entry/exit thresholds based on market volatility, making the strategy more adaptive.

3. Dynamic Stop-Loss: Change the fixed percentage stop-loss to a trailing stop-loss or ATR (Average True Range) stop-loss, which may better adapt to different market volatility situations.

4. Position Management Optimization: Consider dynamically adjusting the fund ratio for each trade based on RSI strength or market volatility, rather than fixing it at 10% of the account's total value.

5. Trend Filtering: Introduce a trend judgment mechanism, such as using long-term moving averages, to avoid premature closing during strong upward trends.

6. Time Filters: Add transaction time window restrictions to avoid trading during periods of low market volatility or poor liquidity.

7. Backtesting and Optimization: Conduct extensive parameter optimization and backtesting to find the best parameter combinations under different market conditions.

#### Summary

This RSI-based dynamic low-price entry and stop-loss strategy provides a concise and effective trading method. By leveraging RSI oversold and overbought signals, combined with a dynamic stop-loss mechanism, this strategy aims to capture market lows while controlling risk. The unique aspect of this strategy lies in using the daily low price to calculate RSI, making it more sensitive to market bottoms.

However, the strategy also has some limitations, such as excessive reliance on a single indicator and potential premature exits. To enhance the robustness and adaptability of the strategy, consider incorporating multi-indicator validation, adaptive parameters, dynamic stop-loss mechanisms, etc. Additionally, conducting in-depth backtesting and parameter optimization based on different market characteristics is necessary.

Overall, this strategy provides a good starting point for traders to customize and improve according to their trading style and target market characteristics. In practical application, it is recommended that traders carefully evaluate the performance of the strategy under various market conditions and combine other analytical tools and risk management techniques to enhance its overall effectiveness.