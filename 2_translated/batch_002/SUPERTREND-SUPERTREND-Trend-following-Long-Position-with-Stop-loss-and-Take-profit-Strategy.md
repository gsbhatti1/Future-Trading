> Name

SUPERTREND-Trend-following-Long-Position-with-Stop-loss-and-Take-profit-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19dd3f1c70e2138d7a2.png)

[trans]
#### Overview
This strategy uses the Supertrend indicator to determine entry and exit points for trades. Supertrend is a trend-following indicator that combines the concepts of dynamic support/resistance and price breakouts. The strategy aims to capture strong uptrends while strictly controlling risk, and trades with a 1:5 risk-reward ratio. When price breaks above the Supertrend upper band, it enters a long position and sets stop-loss and take-profit prices based on the predefined risk-reward ratio. Once price falls below the Supertrend lower band, the strategy will close the long position.

#### Strategy Principles  
1. Calculate the upper and lower bands of the Supertrend indicator. Supertrend uses ATR (Average True Range) and a factor to calculate dynamic support and resistance levels.
2. Check long entry conditions: When closing price breaks above the Supertrend upper band, enter a long position.  
3. Calculate stop-loss and take-profit prices: Based on current closing price and predefined risk-reward ratio (such as 1:5), calculate stop-loss and take-profit prices.
4. Submit long order: Enter long position with calculated stop-loss and take-profit prices.
5. Check long exit conditions: When closing price falls below the Supertrend lower band, close the long position.

#### Advantage Analysis
1. Trend following: The Supertrend indicator can effectively capture strong trends, helping the strategy profit from rising trends.
2. Dynamic stop-loss: By using ATR to calculate dynamic support and resistance levels, Supertrend provides the strategy with dynamic stop-loss levels to control risk.
3. Risk-reward control: This strategy allows users to preset risk-reward ratios (such as 1:5) to control risk and potential returns for each trade.
4. Simple and easy to use: The strategy logic is clear and easy to understand and implement.

#### Risk Analysis  
1. Trend reversal: During sudden trend reversals, this strategy may incur losses as it relies on trend persistence.
2. Parameter sensitivity: Strategy performance may be sensitive to Supertrend parameters (such as ATR factor and ATR length). Improper parameters may cause false signals.
3. Lack of volatility: In low volatility market environments, this strategy may perform poorly as price may fluctuate between upper and lower bands, causing frequent trades and commission losses.

#### Optimization Directions
1. Dynamic parameter optimization: Implement parameter optimization procedures to dynamically adjust Supertrend parameters based on different market conditions. This can improve strategy adaptability and robustness.
2. Combine with other indicators: Combine with other technical indicators such as RSI or MACD to confirm trend strength and filter false signals.
3. Market environment adaptation: Develop logic to identify different market conditions (such as trending, ranging) and adjust strategy parameters or disable the strategy accordingly.
4. Money management optimization: Optimize position sizing and risk management rules to improve the strategy's risk-adjusted returns.

#### Summary
This strategy uses the Supertrend indicator to capture strong uptrends while strictly controlling risk. It provides a simple and effective framework for capturing trending opportunities. However, the strategy may face risks such as trend reversal and parameter sensitivity. Through dynamic parameter optimization, combining with other indicators, adapting to market environments, and optimizing money management, the strategy can be further improved. Overall, this Supertrend strategy provides a solid foundation for trend-following trading.

[/trans]

> Source (PineScript)

``` pinescript
/*backtest
start: 2024-05-01 00:00:00
end: 2024-05-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Supertrend Strategy with 1:5 Risk Reward", overlay=true)

// Supertrend Indicator
factor = input(3.0, title="ATR Factor")
atrLength = input(10, title="ATR Length")

[supertrendUp, supertrendDown] = ta.supertrend(factor, atrLength)

supertrend = ta.crossover(ta.lowest(close, 1), supertrendDown) ? supertrendDown : supertrendUp

plot(supertrend, title="Supertrend", color=supertrend == supertrendUp ? color.green : color.red, linewidth=2, style=plot.style_line)

// Strategy parameters
risk = input(1.0, title="Risk in %")
reward = input(5.0, title="Reward in %")
riskRewardRatio = reward / risk

// Entry and exit conditions
longCondition = ta.crossover(close, supertrendUp)
if (longCondition)
    // Calculate stop loss and take profit levels
    stopLossPrice = close * (1 - (risk / 100))
    takeProfitPrice = close * (1 + (reward / 100))
    
    // Submit long order
    strategy.entry("Long", strategy.long, stop=stopLossPrice, limit=takeProfitPrice)

// Exit conditions
shortCondition = ta.crossunder(close, supertrendDown)
if (shortCondition)
    strategy.close("Long")

```