#### Overview

The RSI and MACD Cross-Period Dynamic Trading Strategy is a quantitative trading system that combines the Relative Strength Index (RSI) and Moving Average Convergence Divergence (MACD) indicators, specifically designed for 15-minute chart intervals. This strategy monitors market overbought/oversold conditions (RSI) and price momentum trends (MACD), triggering trading signals when both indicators simultaneously meet specific criteria. Specifically, when the RSI value falls below 30 (oversold) and the MACD fast line crosses above the signal line, the system generates a buy signal; when the RSI value rises above 70 (overbought) and the MACD fast line crosses below the signal line, the system generates a sell signal. Each trade is configured with percentage-based take profit (5%) and stop loss (2%) mechanisms, effectively maintaining a favorable risk-reward ratio of 2.5:1.

#### Strategy Principles

The core of this strategy lies in combining signals from two classic technical indicators to enhance the reliability of trading decisions:

1. **RSI Application**: Uses the default 14-period RSI to identify market overbought and oversold conditions. The traditional view considers RSI below 30 as oversold (potential bounce) and above 70 as overbought (potential reversal). The code calculates RSI values using `ta.rsi(close, rsiLength)`.

2. **MACD Application**: Employs standard parameters with a fast period of 12, slow period of 26, and signal smoothing factor of 9. MACD is calculated through the `ta.macd(close, macdFast, macdSlow, macdSignal)` function, yielding the MACD line and signal line. Key trading signals derive from crossovers between the MACD line and signal line, captured by the `ta.crossover` and `ta.crossunder` functions.

3. **Combined Signal Logic**:
   - Long entry condition: RSI < 30 (oversold) AND MACD fast line crosses above the signal line
   - Short entry condition: RSI > 70 (overbought) AND MACD fast line crosses below the signal line

4. **Capital Management**: The strategy employs account equity percentage for position sizing (`default_qty_type=strategy.percent_of_equity, default_qty_value=100`), investing 100% of total funds in each trade.

5. **Risk Control**: Each trade automatically sets take-profit levels (±5% of entry price) and stop-loss levels (±2% of entry price), implemented through the `strategy.exit` function.

#### Strategy Advantages

1. **Indicator Confirmation Synergy**: By combining RSI and MACD indicators, the strategy requires dual confirmation to issue trading signals, effectively reducing false breakouts and misleading signals, thus improving trade quality.

2. **Balanced Entry and Exit Mechanism**: Entries are based on objective technical indicator assessments, while exits rely on preset take-profit and stop-loss levels, forming a complete trading cycle that minimizes subjective interference.

3. **Good Risk-Reward Ratio**: The take-profit ratio (5%) is 2.5 times the stop-loss ratio (2%), adhering to professional trading risk management principles. As long as the win rate exceeds 30%, long-term profitability can be achieved.

4. **Adaptability to Market Pacing**: A 15-minute timeframe suits intraday traders, allowing them to capture short-term fluctuations without excessive trading, balancing trade frequency and signal quality.

5. **Visual Feedback Mechanism**: The strategy visualizes the RSI indicator lines along with overbought/oversold levels, providing a clear visual reference for traders to monitor market conditions in real-time.

#### Strategy Risks

1. **Risk of Range Trading Markets**: In sideways markets where RSI frequently oscillates between overbought and oversold levels, and MACD generates frequent crossovers, it may lead to excessive trading and consecutive losses. Solutions include adding additional trend filters like moving averages or ADX indicators.

2. **Parameter Sensitivity**: The strategy's performance is sensitive to the settings of RSI and MACD parameters; the current default parameters might not be suitable for all market environments. It is recommended to optimize parameters based on specific trading instruments and market characteristics.

3. **Fixed Take-Profit and Stop-Loss Limits**: Using fixed percentage take-profit and stop-loss limits may not adapt well to different market volatility patterns. High-volatility markets could result in frequent stops, while low-volatility markets might struggle to reach the profit targets.

4. **Lack of Time Control Mechanism**: The current strategy does not set time filters; it could generate unfavorable signals during times with poor liquidity or abnormal volatility.

5. **No Counter-Trend Mechanism**: The long and short signals are triggered independently without an effective counter-trend mechanism, which can result in significant losses when trading against strong trends.

#### Strategy Optimization Directions

1. **Dynamic Parameter Adjustment**: Consider dynamically adjusting the RSI overbought/oversold thresholds and MACD parameters based on market volatility (e.g., using ATR). Implementation example:
   ```python
   atrValue = ta.atr(14)
   dynamicRsiOversold = 30 - (atrValue / close * 100)
   dynamicRsiOverbought = 70 + (atrValue / close * 100)
   ```

2. **Increase Trend Filters**: Introduce additional trend confirmation indicators, such as adding the ADX indicator, only executing trades when ADX > 25 (indicating a clear trend), to avoid frequent trading in range-bound markets:
   ```python
   adxValue = ta.adx(14)
   adxFilter = adxValue > 25
   longCondition = (rsi < rsiOversold) and macdCrossUp and adxFilter
   ```

3. **Optimize Capital Management**: Replace the fixed 100% of funds for position sizing with a volatility-based approach, where larger positions are taken in low-volatility markets:
   ```python
   positionSize = 100 / (ta.atr(14) / close * 100)
   ```

4. **Add Time Filters**: Include trading time windows to avoid periods of poor liquidity and abnormal volatility, such as the market opening and closing hours:
   ```python
   timeFilter = (time >= timestamp("00:30:00")) and (time <= timestamp("23:00:00"))
   ```

5. **Enhance Take-Profit and Stop-Loss Mechanisms**: Use level-based take-profit and stop-loss mechanisms, such as previous highs/lows, support/resistance levels, or ATR multiples instead of fixed percentages:
   ```python
   atrValue = ta.atr(14)
   dynamicStopLoss = atrValue * 1.5
   ```

#### Conclusion

The RSI and MACD Cross-Period Dynamic Trading Strategy is a clear and logical quantitative trading system that integrates the advantages of overbought/oversold indicators (RSI) and momentum trend indicators (MACD), providing relatively reliable trading signals. This strategy is particularly suitable for 15-minute chart intervals, with core strengths in dual indicator confirmation mechanisms and explicit risk management rules.

While the design of the strategy is reasonable, it still faces challenges related to parameter sensitivity and market adaptability. Through incorporating dynamic parameter adjustments, trend filters, optimized capital management, time filters, and improved take-profit/stop-loss mechanisms, the robustness and adaptability of the strategy can be further enhanced.

Any quantitative strategy requires comprehensive backtesting and forward validation, as well as personalization based on specific market conditions and trader risk preferences. This strategy provides a solid framework for quantitative trading, allowing traders to build upon it through secondary development and optimization to create more sophisticated trading systems.