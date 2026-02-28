```markdown
#### Overview
This strategy combines two technical indicators, MACD and RSI, using MACD crossover signals and RSI overbought/oversold signals to determine trading timing. Meanwhile, the strategy also introduces the Weighted Moving Average (WMA) as an auxiliary judgment to improve the reliability of the strategy. The strategy runs on a 1-hour timeframe, opening long positions when MACD forms a golden cross and RSI is above 50, and opening short positions when MACD forms a death cross and RSI is below 50. At the same time, it closes long positions when RSI is above 70 and closes short positions when RSI is below 30. In addition, the strategy sets variables for multiple timeframes to judge trend changes at different time scales.

#### Strategy Principles
The core of this strategy is the combined use of two technical indicators, MACD and RSI. MACD is composed of the difference between the fast line (short-term moving average) and the slow line (long-term moving average), which can reflect market trend changes. When the fast line crosses above the slow line, it forms a golden cross, indicating an upward trend; conversely, it forms a death cross, indicating a downward trend. RSI is an indicator that measures the overbought and oversold state of the market. When RSI is above 70, it indicates that the market is overbought and may face a pullback risk; when RSI is below 30, it indicates that the market is oversold and may usher in a rebound opportunity.

This strategy combines MACD and RSI, using MACD's trend judgment and RSI's overbought/oversold judgment to more accurately grasp trading timing. At the same time, the strategy also introduces the Weighted Moving Average (WMA) as an auxiliary judgment. WMA places more emphasis on recent prices compared to ordinary moving averages, and can more sensitively reflect price changes.

In addition, the strategy sets variables for multiple timeframes (such as 15 minutes, 30 minutes, 1 hour, 2 hours, etc.) to judge trend changes at different time scales. This multi-timeframe analysis method can help the strategy grasp market trends more comprehensively and improve the accuracy of decision-making.

#### Advantage Analysis
1. It combines two effective technical indicators, MACD and RSI, which can better grasp market trends and overbought/oversold conditions, improving the accuracy of trading decisions.
2. It introduces the Weighted Moving Average (WMA) as an auxiliary judgment. WMA places more emphasis on recent prices and can more sensitively reflect price changes, improving the adaptability of the strategy.
3. It sets variables for multiple timeframes, realizing joint analysis of multiple timeframes, which can more comprehensively grasp market trends and improve the reliability of decisions.
4. It runs on a 1-hour timeframe, with a moderate trading frequency, which can better balance trading costs and returns.
5. It sets clear opening and closing conditions, such as MACD golden cross/death cross, RSI overbought/oversold, etc., which are easy to understand and implement.

#### Risk Analysis
1. Both MACD and RSI are lagging indicators. When the market changes rapidly, there may be a disconnect between indicator signals and prices, leading to false signals.
2. The strategy runs on a single timeframe (1 hour), which may not fully capture trend changes at different time scales, and has certain limitations.
3. The strategy lacks risk control measures, such as stop-loss and position management, which may face greater drawdown risks when the market fluctuates violently.
4. The parameter settings of the strategy (such as the fast and slow line periods of MACD, the time period of RSI, etc.) may need to be adjusted according to different market conditions. The selection of parameters has certain subjectivity and uncertainty.

#### Optimization Direction
1. Introduce more technical indicators, such as Bollinger Bands, ATR, etc., to build more robust trading signals and improve the reliability of the strategy.
2. Optimize the selection of the strategy's timeframes, such as adding higher-level timeframes like daily charts, to better capture major trends while setting specific entry points in lower-level timeframes (such as 15 minutes or 5 minutes), enhancing the precision of the strategy.
3. Add risk control measures, such as setting reasonable stop-loss levels and position restrictions, to manage drawdown risks.
4. Optimize strategy parameters by using machine learning methods to automatically find optimal parameter combinations based on historical data, reducing subjective judgment impacts.
5. Consider incorporating other market factors like trading volume and open interest to better grasp the overall market condition and improve adaptability.

#### Conclusion
This strategy through combining MACD and RSI two effective technical indicators, simultaneously introduces WMA as an auxiliary judgment, performs trading decisions in a 1-hour timeframe. The logic of the strategy is clear, easy to understand and implement, can accurately grasp market trends and overbought/oversold conditions, has certain feasibility. However, the strategy also exists some limitations and risks such as lagging nature, single time frame, lack of risk control measures. In the future, we could improve the strategy by introducing more indicators, optimizing timeframes, strengthening risk management, parameter optimization, etc., to enhance its robustness and profitability. Overall, this strategy provides a thinking approach for quantitative trading but still needs continuous optimization and perfection in practice.
```

This translation maintains the original formatting and structure while translating the text from Chinese to English.