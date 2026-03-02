> Name

Fisher Transform Dynamic Threshold Trend Following Strategy - Fisher-Transform-Dynamic-Threshold-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1366f18ebbe18554b9f.png)
[trans]
#### Overview
The Fisher Transform Dynamic Threshold Trend Following Strategy is based on the Fisher Transform indicator to identify changes in price trends. The strategy uses the Fisher Transform to normalize prices into a standard scale, making it easier to detect potential trend reversal points. By dynamically adjusting thresholds, the strategy can adapt to different market conditions and improve the accuracy of trend recognition. When the Fisher Transform value crosses positive or negative thresholds, the strategy generates buy or sell signals to track market trends.

#### Strategy Principle
1. Calculate Fisher Transform Value: Normalize the current price based on historical high and low prices to obtain a Fisher Transform value between -0.999 and 0.999.
2. Dynamic Thresholds: Dynamically adjust the thresholds for buy and sell signals based on the historical volatility of the Fisher Transform value to adapt to different market states.
3. Trend Determination: Determine changes in price trends by comparing the current Fisher Transform value with the values from the previous two periods.
4. Buy and Sell Signals: Generate a buy signal when the Fisher Transform value crosses the negative threshold from below, and generate a sell signal when it crosses the positive threshold from above.

#### Advantage Analysis
1. Dynamic Threshold Adjustment: Adaptively adjust buy and sell thresholds based on market volatility to improve trend judgment accuracy.
2. Trend Tracking: The Fisher Transform indicator's trend determination can effectively capture market trends for trend-following trading.
3. Reduced Price Noise: Normalizing prices with the Fisher Transform helps reduce the impact of price noise on trend judgments.
4. Intuitive Chart Display: The strategy plots the Fisher Transform curve and threshold lines on the chart, allowing traders to visually observe market trends and buy/sell signals.

#### Risk Analysis
1. Parameter Optimization Risk: The performance of the strategy depends on the selection of parameters such as the Fisher Transform period and dynamic threshold calculation methods. Different parameter choices may lead to different trading outcomes.
2. Trend Recognition Lag: The Fisher Transform indicator has a certain lag in identifying price trends, potentially missing some trend movements.
3. Poor Performance in Choppy Markets: Frequent trend changes in choppy market conditions may result in the strategy generating more false signals, leading to suboptimal trading performance.
4. Extreme Market Risk: In extreme market conditions (such as rapid and substantial changes), the Fisher Transform indicator may fail, causing incorrect trading decisions.

#### Optimization Direction
1. Parameter Optimization: Optimize key parameters such as the Fisher Transform period and dynamic threshold calculation methods to improve adaptability in different market states.
2. Signal Filtering: Introduce additional technical indicators or market sentiment indicators for signal confirmation to enhance signal reliability.
3. Stop-Loss and Take-Profit: Set reasonable stop-loss and take-profit rules to control single-trade risk and improve the strategy's risk-reward ratio.
4. Position Management: Dynamically adjust position sizes based on factors such as market trend strength and price volatility to reduce holding risks.

#### Summary
The Fisher Transform Dynamic Threshold Trend Following Strategy uses the Fisher Transform indicator and dynamic thresholds to identify changes in price trends, adapting to different market conditions. The strategy can effectively capture market trends and enable trend-following trading. Its advantages include dynamic threshold adjustment, reduced price noise interference, and intuitive chart display. However, it faces challenges such as parameter optimization risk, trend recognition lag, poor performance in choppy markets, and extreme market risks. Through measures like parameter optimization, signal filtering, stop-loss and take-profit, and position management, the strategy's robustness and profitability can be further enhanced.
[/trans]

> Source (PineScript)

```pinescript
//@version=5
strategy("Fisher Transform Dynamic Threshold Trend Following Strategy", overlay=true)
len = input.int(14, minval=1, title="Fisher Transform Period")
f = ta.fisher(len)
upper = input.float(0.8, title="Upper Threshold")
lower = input.float(-0.8, title="Lower Threshold")

plot(f, title="Fisher Transform", color=color.blue, linewidth=2)

buySignal = f < lower and ta.crossover(f, lower)
sellSignal = f > upper and ta.crossunder(f, upper)

if (buySignal)
    strategy.entry("Buy", strategy.long)

if (sellSignal)
    strategy.exit("Sell", "Buy")

// Plot thresholds
hline(upper, "Upper Threshold", color=color.red, linewidth=1)
hline(lower, "Lower Threshold", color=color.green, linewidth=1)
```
[/trans]