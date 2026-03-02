> Name

Dynamic Dual Exponential Moving Average Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c76acb0f5e9b040035.png)
[trans]
### Overview

This strategy is named "Dynamic Dual Exponential Moving Average Trading Strategy," and it is a quantitative trading strategy based on the dual exponential moving average (DEMA). The strategy calculates the price change rate of stocks, then performs dual exponential smoothing on both its absolute value and non-absolute value to obtain the True Strength Index (TSI). The strategy generates buy and sell signals based on the golden/dead cross of the TSI value and its signal line.

### Strategy Principle

The core indicator of this strategy is the True Strength Index (TSI). The calculation formula of TSI is:

\[ \text{TSI} = 100 \times \left( \frac{\text{PC1}}{\text{PC2}} \right) \]

Where PC1 and PC2 are the dual exponential moving averages of the price change rate and the absolute value of the price change rate, respectively. The dual exponential moving average is calculated by first applying an exponential moving average with one length to the price change rate, and then applying another shorter exponential moving average to the obtained moving average. This dual smoothing can better eliminate the randomness in the price change rate and improve the stability of the TSI indicator.

After calculating the TSI value, the strategy also calculates a signal line for the TSI value. The signal line is defined as an exponential moving average of the TSI value over a certain period. In actual trading, the strategy judges market trends and generates trading signals by observing the relationship between the TSI value and its signal line. When the TSI value crosses above the signal line, it is a buy signal. When the TSI value crosses below the signal line, it is a sell signal.

Another feature of this strategy is that the trade size is dynamically adjusted. The strategy code sets an initial capital and a risk exposure ratio as input parameters. These two parameters combine with the current price of the stock to dynamically calculate the number of contracts traded or risk exposure. This can better control the overall risk of the entire strategy.

### Advantage Analysis

The dynamic dual exponential moving average trading strategy comes with several advantages:

1. It utilizes the TSI indicator which applies dual exponential smoothing, making it less sensitive to market noise and able to generate more accurate signals.
2. It builds upon the proven principle of crossing of an indicator and its signal line to generate trading signals. This eliminates many false signals.
3. The strategy dynamically adjusts position sizing based on the risk budget. This helps prevent overtrading and emotions.
4. It works on daily and weekly timeframes, suitable for both swing trading and positional trading.
5. It is easy to implement in bots and other trading systems due to the simple entry/exit logic.
6. There are not too many parameters to tune, making the system easy to optimize.

These advantages combined make it a robust and versatile trading strategy for stock traders. The careful smoothing and position sizing help prevent false signals and large losses.

### Risk Analysis

While the dynamic dual exponential moving average trading strategy has many advantages, it also has some inherent risks like most stock strategies:

1. Since the TSI and signal line are based on historical price data, there is always the risk of incorrect signals especially during volatile market conditions.
2. Whipsaws may occur if the market oscillates around the zero line of the TSI indicator. This can lead to losses.
3. Large gap moves may result in the strategy closing at a loss since it was not able to exit in time.
4. If the market continues in a strong trend, the TSI may prematurely reverse the trend resulting in missed profits.
5. Due to the leverage effect, larger losses than the limit set by the risk parameter can be generated.

However, these risks can be mitigated through the application of position sizing, stop-losses, and other risk management techniques. Additionally, parameters and filters can further optimize performance across different market conditions.

### Optimization Directions

Some ideas for optimizing this strategy include:

1. Testing different combinations of dual smoothing parameters to find those that produce more accurate trading signals. Adjusting the long and short-term parameters can optimize.
2. Adding filters based on volatility, volume or other indicators to reduce unnecessary trade signals. This can lower the frequency of trades while increasing profitability per trade.
3. Including stop-loss logic. For example, setting a stop-loss when the TSI value crosses the zero axis. This can limit unnecessary losses.
4. Evaluating different asset classes such as indices and commodities under this strategy to focus on the best-performing assets.
5. Applying selection filters for the traded assets. For instance, assessing liquidity, volatility indicators, and selecting assets with higher parameter rankings.
6. Utilizing machine learning methods for forward analysis to select optimal parameter combinations. This can reduce bias in manual selection and obtain superior parameters.

7. Using multiple sets of parameters based on different market environments and dynamically switching between them. For example, using more aggressive parameter combinations during bull markets and more conservative ones during bear markets.

By testing and optimizing the above aspects, further improvements in stability and returns can be expected.

### Summary

In summary, this strategy is designed around the dual exponential smoothing characteristic of the TSI indicator to create a relatively stable and reliable stock trading strategy. By dynamically adjusting position sizes, it effectively controls overall risk levels. The strategy also balances well for both short-term and long-term trading.

Of course, like most quantitative trading strategies, this one has certain limitations, mainly being susceptible to significant market volatility. Additionally, parameter selection and filtering conditions need further testing and optimization to achieve stronger adaptability and profitability in a complex and ever-changing market.