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

2. **Balanced Entry and Exit Mechanism**: Entries are based on objective technical indicator assessments, while exits rely on preset take-profit and stop-loss levels, forming a complete trading cycle, thereby minimizing subjective interference.

3. **Good Risk-Reward Ratio**: The take-profit ratio (5%) is 2.5 times the stop-loss ratio (2%), aligning with professional trading risk management principles. As long as the win rate exceeds 30%, this strategy can achieve long-term profitability.

4. **Adaptability to Market Rhythm**: A 15-minute period suits day traders, allowing for both short-term volatility capture and avoiding excessive trading while balancing trade frequency and signal quality.

5. **Visual Feedback Mechanism**: The strategy provides visual feedback through the drawing of RSI indicator lines and overbought/oversold level lines, offering traders a clear reference point to monitor market conditions in real-time.

#### Strategy Risks

1. **Volatility Risk in Range-Bound Markets**: In range-bound markets, RSI may frequently oscillate between overbought and oversold levels, while MACD may generate multiple crossovers, leading to excessive trading and consecutive losses. Solutions include adding additional trend filters such as moving averages or ADX indicators.

2. **Parameter Sensitivity**: The performance of the strategy is sensitive to the parameters set for RSI and MACD. Current use of traditional default settings may not be suitable for all market environments. It is recommended to optimize parameters based on specific trading instruments and market characteristics.

3. **Fixed Take-Profit/Stop-Loss Limits**: Fixed percentage take-profit/stop-loss levels may not adapt well to different market volatility characteristics. High-volatility markets can result in frequent stop-loss triggers, while low-volatility markets may struggle to meet the target for take-profits.

4. **Lack of Time Control Mechanism**: The current strategy does not set time filters, potentially generating unfavorable signals during periods of low liquidity or abnormal market volatility.

5. **No Counter-Position Mechanism**: Multi-directional trading signals trigger independently in the strategy without an effective counter-position mechanism, posing significant risks to traders holding positions against strong trends.

#### Strategy Optimization Directions

1. **Dynamic Parameter Adjustment**: Consider dynamically adjusting RSI overbought/oversold thresholds and MACD parameters based on market volatility (e.g., using ATR), to adapt to different market environments:
   ```
   atrValue = ta.atr(14)
   dynamicRsiOversold = 30 - (atrValue / close * 100)
   dynamicRsiOverbought = 70 + (atrValue / close * 100)
   ```

2. **Increase Trend Filters**: Introduce additional trend confirmation indicators, such as adding the ADX indicator, to execute trades only when ADX > 25 (indicating a clear trend), thus avoiding frequent trading in range-bound markets:
   ```
   adxValue = ta.adx(14)
   adxFilter = adxValue > 25
   longCondition = (rsi < rsiOversold) and macdCrossUp and adxFilter
   ```

3. **Optimize Capital Management**: Replace the fixed 100% equity allocation with a volatility-based position sizing approach, where larger positions are taken in low-volatility markets:
   ```
   positionSize = 100 / (ta.atr(14) / close * 100)
   ```

4. **Introduce Time Filters**: Add trading time window controls to avoid periods of low liquidity or abnormal market volatility, such as market opening and closing times:
   ```
   timeFilter = (time >= timestamp("00:30:00")) and (time <= timestamp("23:00:00"))
   ```

5. **Enhance Take-Profit/Stop-Loss Mechanisms**: Use technical levels, such as previous highs/lows or support/resistance areas, to set dynamic stop-loss points instead of fixed percentages:
   ```
   atrValue = ta.atr(14)
   dynamicStopLoss = atrValue * 1.5
   ```

#### Conclusion

The RSI and MACD Cross-Period Dynamic Trading Strategy is a clear and logically structured quantitative trading system that integrates the strengths of overbought/oversold indicators (RSI) and momentum trend indicators (MACD), providing relatively reliable trading signals. This strategy, particularly suitable for 15-minute intervals in short-term trading, highlights its core advantages through dual indicator confirmation mechanisms and explicit risk management rules.

While the design is sound, it still faces challenges related to parameter sensitivity and market adaptability. By introducing dynamic parameter adjustments, trend filters, optimized capital management, time filters, and enhanced take-profit/stop-loss mechanisms, this strategy can be further refined for greater robustness and adaptability.

Any quantitative trading system requires comprehensive backtesting and forward validation, tailored to specific market conditions and trader risk preferences. This strategy provides a solid framework for traders to build upon through secondary development and optimization, creating more complete trading systems.