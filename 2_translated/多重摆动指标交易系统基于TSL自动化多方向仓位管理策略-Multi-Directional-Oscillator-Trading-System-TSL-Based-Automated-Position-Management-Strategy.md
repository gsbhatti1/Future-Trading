#### Overview

The Multi-Directional Oscillator Trading System is a quantitative trading strategy based on technical analysis, primarily relying on the identification of swing highs and lows to determine market trend changes. The strategy tracks the highest high and lowest low over N periods to construct a dynamic Trailing Stop Level (TSL), which serves as a decision boundary for both long and short trades. The system automatically executes buy signals when the price breaks above the TSL and sell signals when the price falls below the TSL, while managing positions to ensure only one directional position is held at any time. This strategy is particularly suitable for volatile market environments, capable of automatically capturing short to medium-term trend changes.

#### Strategy Principles

The core logic of this strategy revolves around the Trailing Stop Level (TSL), implemented as follows:

1. Calculate key price levels within the period:
   - Use `ta.highest(high, no)` to calculate the highest price (res) over the past no periods
   - Use `ta.lowest(low, no)` to calculate the lowest price (sup) over the past no periods

2. Determine price position relative to previous highs and lows:
   - When the closing price is higher than the previous period's highest price, avd is set to 1 (uptrend)
   - When the closing price is lower than the previous period's lowest price, avd is set to -1 (downtrend)
   - In other cases, avd is set to 0 (no clear trend)

3. Construct the Trailing Stop Level (TSL):
   - During an uptrend, TSL is set to the support level (sup) as a stop-loss point
   - During a downtrend, TSL is set to the resistance level (res) as a reversal signal point

4. Generate trading signals:
   - Buy signal (Buy): When the closing price crosses above the TSL
   - Sell signal (Sell): When the closing price crosses below the TSL

5. Execute trading operations:
   - When a buy signal is triggered, close short positions and open long positions
   - When a sell signal is triggered, close long positions and open short positions

The system also includes visualization components, such as markers for buy and sell points, color-changing candlesticks and background, and horizontal lines displaying entry prices in real-time, enhancing the visual experience of the trading process.

#### Strategy Advantages

1. Strong trend capture capability: Through dynamic calculation of the highest and lowest prices, it effectively captures market trend changes and adapts to market fluctuations across different cycles.

2. High degree of automation: The system automatically identifies buy and sell signals and executes trades, reducing human intervention and emotional influence.

3. Bi-directional trading mechanism: Supports both long and short trading, enabling profit opportunities in both rising and falling markets.

4. Built-in risk management: The design of the Trailing Stop Level (TSL) inherently includes a stop-loss function, limiting the maximum loss per trade.

5. Visual trading feedback: The graphical interface clearly displays trading signals and entry prices, facilitating real-time monitoring and assessment of strategy performance.

6. Parameter flexibility: By adjusting the swing period parameter (no), the strategy can adapt to different time cycles, from short-term to medium-term.

7. Clear signal prompts: The system provides both text and visual signal prompts, reducing the likelihood of erroneous operations.

#### Strategy Risks

1. Poor performance in choppy markets: In horizontal consolidation markets, the strategy may generate frequent false signals, leading to consecutive stop-loss events.

2. Slippage and execution delay risks: In live trading, there can be a time difference between signal generation and order execution, causing actual trade prices to deviate from ideal prices.

3. Fixed position management limitations: The current strategy uses a fixed unit (qty=1) for trading, lacking mechanisms to adjust position sizes based on market volatility or account size.

4. Parameter sensitivity: Strategy performance is highly dependent on the setting of the swing period parameter (no), and different market environments may require different parameter values.

5. Weak response to sudden price movements: In fast price movements caused by major news or black swan events, the stop-loss level may not adjust in time, leading to significant losses.

To mitigate these risks, methods such as combining other indicators for signal confirmation, implementing dynamic position management, setting maximum stop-loss limits, adjusting parameters based on volatility, and regularly backtesting and optimizing strategy parameters can be employed.

#### Strategy Optimization Directions

1. Dynamic Position Management: Adjust position sizes based on market volatility or account balance proportions instead of fixed units. The following code can be added to achieve this:
   ```
   volatility = ta.atr(14) / close * 100  // Calculate percentage volatility
   position_size = strategy.equity * 0.01 / volatility  // Adjust position size based on volatility
   ```

2. Signal Filtering Optimization: Introduce additional technical indicators such as RSI, MACD, or ATR as signal filters to reduce false signals. For example:
   ```
   rsi = ta.rsi(close, 14)
   valid_buy = Buy and rsi < 70  // Avoid buying in overbought conditions
   valid_sell = Sell and rsi > 30  // Avoid selling in oversold conditions
   ```

3. Adaptive Parameters: Dynamically adjust the swing period parameter (no) based on market volatility, using smaller values in low-volatility environments and larger values in high-volatility environments.

4. Add Profit Target: Set profit targets based on ATR or support/resistance levels, locking in partial profits when the market moves favorably enough.

5. Time Filters: Add trading time window restrictions to avoid low liquidity or abnormal market volatility periods.

6. Drawdown Control Mechanism: Implement a trading pause mechanism based on percentage drawdown of account equity, pausing trading when consecutive losses reach a preset threshold.

7. Multi-period Confirmation: Combine higher time frame trend directions, only opening positions in the direction consistent with the higher cycle trend to increase the win rate.

These optimization directions can significantly enhance the strategy's stability and adaptability, providing better risk-adjusted returns in different market environments.

#### Summary

The Multi-Directional Oscillator Trading System is a quantitative trading strategy based on technical analysis, designed to dynamically track the Trailing Stop Level (TSL) and execute both long and short trades. This strategy excels in clear trending markets, effectively tracking price movements and automatically managing positions.

The core advantages of the strategy lie in its simple and effective signal generation mechanism and built-in risk management features, making it particularly suitable for medium-term trend trading. However, the strategy may face challenges in volatile markets due to frequent false signals, requiring further optimization to improve its adaptability across various market conditions.

By implementing dynamic position management, multi-indicator signal confirmation, adaptive parameter adjustments, and other optimization measures, the strategy can further enhance its risk-adjusted returns and stability. For quantitative traders, such a system based on clear rules provides a reliable framework to reduce emotional interference and maintain trading discipline.

Ultimately, the successful application of this strategy depends on the trader's fine-tuning of parameters and understanding of market characteristics, with a recommendation to conduct thorough historical backtesting and simulated trading validation before live application.