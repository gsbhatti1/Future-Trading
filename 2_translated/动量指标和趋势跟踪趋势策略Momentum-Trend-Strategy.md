### Overview  

This strategy incorporates momentum indicators and trend tracking to identify the mid-term uptrend or downtrend of stock prices and take positions at the beginning stage of trends. The strategy firstly computes the 20-day momentum indicator of price, then processes it into a normalized momentum value ranging from 0 to 1. Meanwhile, the 20-day simple moving average is calculated as a representative of the mid-term trend. When the normalized momentum is larger than 0.5 and the price is above the mid-term trendline, go long. When the normalized momentum is less than 0.5 and the price is below the mid-term trendline, go short.

### Strategy Logic  

The core indicator of this strategy is the 20-day momentum difference of price. The momentum difference is defined as: (today's close – close 20 days ago) / close 20 days ago. This metric reflects the percentage increase or decrease of price over the last 20 days. To solve the issue of vastly different price ranges across stocks, the raw momentum difference is normalized to a 0 to 1 scale by the following process: first find the maximum and minimum values of momentum difference in the past 100 days, then calculate the percentage position of current difference within this range, resulting in a normalized momentum score between 0 and 1. The normalization can better capture the magnitude of price movement.

In addition, the 20-day simple moving average is included to determine the mid-term trend direction. Moving averages are visually intuitive tools for trend analysis. When the price is above the moving average line, it signals an uptrend. When below the line, it indicates a downtrend.   

By combining the normalized momentum indicator and mid-term trend judgment, this strategy aims to capture significant bullish and bearish stages in the mid-term horizon. The logic is: if normalized momentum is larger than 0.5, it means the price is accelerating with an uptrend recently. Meanwhile, if the price stays above 20-day MA, then the mid-term is still an uptrend. Under this condition, go long. On the contrary, if normalized momentum drops below 0.5, it signals an accelerating downtrend recently. Also, with the price below 20-day MA, the mid-term is bearish. Then we should go short.  

The above describes the core decision logic. For entries, the strategy simply enters the market when observing aligned momentum and trend signals. For stop loss, a fixed stop is set at the highest price + minimum tick size for longs, and lowest price - minimum tick size for shorts, in order to prevent inefficient floating losses.

### Advantage Analysis  

The biggest advantage of this strategy is utilizing two indicators for confirmation, which can effectively filter out some false entries in whipsaws. Relying solely on momentum signals tends to produce fake signals occasionally. By adding the condition of mid-term trend, the validity of momentum signals can be verified to avoid being trapped in ranging markets. Similarly, just following the trend may miss some opportunities at the beginning of trend accelerations, while combining momentum can capture such turns in a timely fashion. So the two indicators complement each other to form more robust decisions.

Another advantage is the choice of 20-day period. This mid-term parameter helps reduce trading frequency compared to faster frequencies, allowing the strategy to capture larger swings over the medium-long term. Meanwhile, it can also filter out short-term market noises.

### Risk Analysis  

The major risk of this strategy lies in the divergence between momentum and trend. Misalignments may lead to incorrect signals. For instance, during a downtrend, short-term bounces could push momentum upwards temporarily. If going straight long, it may encounter losses.

In addition, the stop-loss mechanism is relatively simple and may fail to fully contain risks. In case of huge price gaps, the fixed loss size could be gapped through directly, proving inadequate reaction.

### Optimization Directions  

Here are some major optimization directions for this strategy:

1. Introduce more indicators for comprehensive judgment. For example, MACD, KD, Bollinger Bands can be used to validate momentum signals and avoid misleading signals.
2. Dynamically adjust the stop-loss position. Based on ATR values or using options pricing theory to calculate reasonable stop-loss lines can reduce the probability of being trapped by the stop loss.
3. Optimize parameter periods. The current strategy uses a 20-day period for calculations. Testing different combinations of parameters can help find the best cycle length.
4. Distinguish between buy and sell momentum differences in judgment criteria. Currently, the same 0.5 standard is used. Separate tests for optimal parameters for buying and selling should be conducted.
5. Incorporate trading volume filtering. For instance, signals are only issued when there is significant volume amplification. This can avoid false breakouts due to inadequate liquidity.

### Summary  

This strategy integrates trend analysis with momentum indicators to capture price momentum changes over medium to long-term horizons. Compared to a single indicator, using multiple indicators can enhance the accuracy of judgments and increase profitability. The stop-loss rules are straightforward and allow quick risk management. With further optimization in indicator settings, stop-loss methods, and additional supporting judgment conditions, this strategy can become more flexible and adaptable to different market conditions. Overall, it is a promising and expandable quantitative trading idea.