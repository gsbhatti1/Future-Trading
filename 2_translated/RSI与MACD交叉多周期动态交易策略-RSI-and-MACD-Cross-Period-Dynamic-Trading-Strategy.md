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

2. **Balanced Entry and Exit Mechanism**: Entries are based on objective technical indicator assessments, while exits rely on preset take-profit and stop-loss levels, forming a complete trading cycle, thereby reducing subjective factors' interference.

3. **Good Risk-Reward Ratio**: The take-profit ratio (5%) is 2.5 times the stop-loss ratio (2%), aligning with professional trading risk management principles; as long as the win rate exceeds 30%, the strategy can achieve long-term profitability.

4. **Adaptation to Market Rhythm**: A 15-minute interval is suitable for intraday traders, capable of capturing short-term fluctuations without excessive transactions, balancing trading frequency and signal quality.

5. **Visual Feedback**: The strategy visualizes RSI levels along with overbought/oversold horizontal lines, providing traders with intuitive visual references to monitor market conditions in real time.

#### Strategy Risks

1. **Risk in Range-bound Markets**: In sideways markets, the RSI may frequently hover around overbought and oversold levels, while MACD can generate multiple crossovers, leading to excessive trading and consecutive losses. Solutions include adding additional trend filters such as moving averages or ADX indicators.

2. **Parameter Sensitivity**: Strategy performance is sensitive to the parameters of RSI and MACD; current use of traditional default parameters may not be suitable for all market environments. It is recommended to optimize parameters based on specific trading instruments and market characteristics.

3. **Fixed Stop-Loss/Take-Profit Limits**: Using fixed percentage-based stop-loss/take-profit limits might not adapt well to different market volatility characteristics, potentially leading to frequent false triggers in highly volatile markets and difficulty reaching take-profit targets in low-volatility environments.

4. **Lack of Time Control Mechanism**: The current strategy lacks time filters; it may generate unfavorable signals during periods with poor liquidity or abnormal market fluctuations.

5. **No Reversal Mechanism**: Buy and sell signals are triggered independently within the strategy, lacking effective reversal mechanisms, which could result in significant losses if short-term strong trends occur.

#### Strategy Optimization Directions

1. **Dynamic Parameter Adjustment**: Consider dynamically adjusting RSI overbought/oversold thresholds and MACD parameters based on market volatility (e.g., ATR). Implementation can be as follows:
   ```python
   atrValue = ta.atr(14)
   dynamicRsiOversold = 30 - (atrValue / close * 100)
   dynamicRsiOverbought = 70 + (atrValue / close * 100)
   ```

2. **Add Trend Filters**: Introduce additional trend confirmation indicators, such as ADX, only executing trades when ADX > 25 (indicating a clear trend), avoiding frequent trading in range-bound markets:
   ```python
   adxValue = ta.adx(14)
   adxFilter = adxValue > 25
   longCondition = (rsi < rsiOversold) and macdCrossUp and adxFilter
   ```

3. **Optimize Capital Management**: Replace the fixed 100% capital allocation with a volatility-based position sizing approach, where larger positions are taken in less volatile markets:
   ```python
   positionSize = 100 / (ta.atr(14) / close * 100)
   ```

4. **Add Time Filters**: Introduce trade time windows to avoid trading during low liquidity or abnormal market periods:
   ```python
   timeFilter = (time >= timestamp("00:30:00")) and (time <= timestamp("23:00:00"))
   ```

5. **Enhance Stop-Loss/Take-Profit Mechanisms**: Use technical levels for stop-loss/take-profit, such as previous highs/lows, support/resistance levels, or ATR multiples instead of fixed percentages:
   ```python
   atrValue = ta.atr(14)
   dynamicStopLoss = atrValue * 1.5
   ```

#### Conclusion

The RSI and MACD Cross-Period Dynamic Trading Strategy is a structured and clear quantitative trading system that integrates the advantages of overbought/oversold indicators (RSI) and momentum trend indicators (MACD), providing relatively reliable trading signals. The strategy, particularly suitable for 15-minute intervals in short-term trading, excels with its dual indicator confirmation mechanism and explicit risk management rules.

While the design is rational, it still faces challenges related to parameter sensitivity and market adaptability. By incorporating dynamic parameter adjustments, trend filters, optimized capital management, time filters, and enhanced stop-loss/take-profit mechanisms, the strategy can be further robust and adaptable.

Any quantitative trading strategy requires comprehensive historical backtesting and forward validation, along with personalized adjustments based on specific market conditions and trader risk preferences. This strategy provides a solid framework for traders to build upon and optimize, creating more complete trading systems.