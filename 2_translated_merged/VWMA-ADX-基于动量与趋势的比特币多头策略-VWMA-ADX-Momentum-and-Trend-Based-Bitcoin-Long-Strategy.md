> Name

VWMA-ADX-基于动量与趋势的比特币多头策略-VWMA-ADX-Momentum-and-Trend-Based-Bitcoin-Long-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/104c7b79ea2771e1315.png)
[trans]
#### Overview
This strategy utilizes multiple moving averages (VWMA), the Average Directional Index (ADX), and the Directional Movement Indicator (DMI) to capture long opportunities in the Bitcoin market. By combining price momentum, trend direction, and trading volume, the strategy aims to find entry points with strong upward trends and sufficient momentum while strictly controlling risk.

#### Strategy Principles
1. Use the 9-day and 14-day VWMA to determine the long trend. A bullish signal is generated when the short-term moving average crosses above the long-term moving average.
2. Introduce an adaptive moving average constructed from the 89-day highest and lowest price VWMA as a trend filter. Only consider opening a position when the closing price or opening price is above this moving average.
3. Confirm trend strength using the ADX and DMI indicators. The trend is considered strong enough only when the ADX is greater than 18 and the difference between +DI and -DI is greater than 15.
4. Filter out bars with trading volume between the 60% and 95% percentiles using the volume percentile function to avoid periods with low trading volume.
5. Set the stop-loss level at 0.96 to 0.99 times the previous candle's high, decreasing as the time frame increases to control risk.
6. Close the position when the predefined holding time is reached or the price falls below the adaptive moving average.

#### Advantage Analysis
1. By combining multiple technical indicators, the strategy evaluates market conditions from various dimensions such as trend, momentum, and trading volume, making the signals more reliable.
2. The adaptive moving average and trading volume filtering mechanism effectively filter out false signals and reduce invalid trades.
3. Strict stop-loss settings and holding time limits greatly reduce the strategy's risk exposure.
4. The modular design of the code enhances readability and maintainability, facilitating further optimization and expansion.

#### Risk Analysis
1. When the market is fluctuating or the trend is unclear, the strategy may generate more false signals.
2. The stop-loss level is relatively tight, which may trigger premature stop-outs and lead to increased losses during large market fluctuations.
3. The strategy lacks consideration of macroeconomic conditions and significant events, and may fail in the face of "black swan" events.
4. The parameter settings are relatively fixed and lack adaptability, which may result in unstable performance in different market environments.

#### Optimization Directions
1. Introduce more indicators that can capture market conditions, such as the Relative Strength Index (RSI) and Bollinger Bands, to improve signal reliability.
2. Dynamically optimize the stop-loss level, for example, by using Average True Range (ATR) or percentage-based stop-loss, to adapt to different market volatility conditions.
3. Enhance the strategy's risk control module by incorporating macroeconomic data and sentiment analysis.
4. Utilize machine learning algorithms to automatically optimize parameters, improving the strategy's adaptability and stability.

#### Summary
The VWMA-ADX Bitcoin Long Strategy effectively captures upward opportunities in the Bitcoin market by comprehensively considering price trends, momentum, trading volume, and other technical indicators. At the same time, strict risk control measures and clear exit conditions ensure that the strategy's risk is well-controlled. However, the strategy also has some limitations, such as insufficient adaptability to changing market environments and the need for optimized stop-loss strategies. In the future, improvements can be made in terms of signal reliability, risk control, and parameter optimization to further enhance the strategy's robustness and profitability. Overall, the VWMA-ADX Bitcoin Long Strategy provides investors with a systematic trading approach based on momentum and trend, which is worth further exploration and refinement.

||

#### Overview
This strategy utilizes multiple moving averages (VWMA), the Average Directional Index (ADX), and the Directional Movement Indicator (DMI) to capture long opportunities in the Bitcoin market. By combining price momentum, trend direction, and trading volume, the strategy aims to find entry points with strong upward trends and sufficient momentum while strictly controlling risk.

#### Strategy Principles
1. Use the 9-day and 14-day VWMA to determine the long trend. A bullish signal is generated when the short-term moving average crosses above the long-term moving average.
2. Introduce an adaptive moving average constructed from the 89-day highest and lowest price VWMA as a trend filter. Only consider opening a position when the closing price or opening price is above this moving average.
3. Confirm trend strength using the ADX and DMI indicators. The trend is considered strong enough only when the ADX is greater than 18 and the difference between +DI and -DI is greater than 15.
4. Filter out bars with trading volume between the 60% and 95% percentiles using the volume percentile function to avoid periods with low trading volume.
5. Set the stop-loss level at 0.96 to 0.99 times the previous candle's high, decreasing as the time frame increases to control risk.
6. Close the position when the predefined holding time is reached or the price falls below the adaptive moving average.

#### Advantage Analysis
1. By combining multiple technical indicators, the strategy evaluates market conditions from various dimensions such as trend, momentum, and trading volume, making the signals more reliable.
2. The adaptive moving average and trading volume filtering mechanism effectively filter out false signals and reduce invalid trades.
3. Strict stop-loss settings and holding time limits greatly reduce the strategy's risk exposure.
4. The modular design of the code enhances readability and maintainability, facilitating further optimization and expansion.

#### Risk Analysis
1. When the market is fluctuating or the trend is unclear, the strategy may generate more false signals.
2. The stop-loss level is relatively tight, which may trigger premature stop-outs and lead to increased losses during large market fluctuations.
3. The strategy lacks consideration of macroeconomic conditions and significant events, and may fail in the face of "black swan" events.
4. The parameter settings are relatively fixed and lack adaptability, which may result in unstable performance in different market environments.

#### Optimization Directions
1. Introduce more indicators that can capture market conditions, such as the Relative Strength Index (RSI) and Bollinger Bands, to improve signal reliability.
2. Dynamically optimize the stop-loss level, for example, by using Average True Range (ATR) or percentage-based stop-loss, to adapt to different market volatility conditions.
3. Enhance the strategy's risk control module by incorporating macroeconomic data and sentiment analysis.
4. Utilize machine learning algorithms to automatically optimize parameters, improving the strategy's adaptability and stability.

#### Summary
The VWMA-ADX Bitcoin Long Strategy effectively captures upward opportunities in the Bitcoin market by comprehensively considering price trends, momentum, trading volume, and other technical indicators. At the same time, strict risk control measures and clear exit conditions ensure that the strategy's risk is well-controlled. However, the strategy also has some limitations, such as insufficient adaptability to changing market environments and the need for optimized stop-loss strategies. In the future, improvements can be made in terms of signal reliability, risk control, and parameter optimization to further enhance the strategy's robustness and profitability. Overall, the VWMA-ADX Bitcoin Long Strategy provides investors with a systematic trading approach based on momentum and trend, which is worth further exploration and refinement.

||

``` pinescript
//@version=5
strategy("Long BTC Strategy", overlay=true, 
     default_qty_type = strategy.percent_of_equity, 
     default_qty_value = 100, initial_capital = 1000, currency = currency.USD)

Volume_Q