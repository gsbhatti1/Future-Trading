> Name

Advanced-MACD-Strategy-with-Limited-Martingale-基于有限马丁格尔的高级MACD策略

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19d896963817e1d58ec.png)
[trans]
#### Overview
This strategy combines the MACD indicator with a limited Martingale money management method to capture trading opportunities when market trends change. A buy signal is generated when the MACD fast line crosses above the slow line, and a sell signal is generated when the fast line crosses below the slow line. At the same time, the strategy uses a limited Martingale method to control drawdowns, with a maximum of 3 additional positions. The strategy sets a fixed take profit and stop loss of 1% for each trade.

#### Strategy Principles
1. Calculate the fast line, slow line, and signal line of the MACD indicator.
2. Determine the crossover of the fast and slow lines, going long on a bullish crossover and short on a bearish crossover.
3. Set a fixed trading volume (0.01) for each trade.
4. Record the net profit of the previous trade.
5. If the current net profit is less than the previous trade and the number of additional positions is less than 3, double the next trading volume and increase the number of additional positions by 1; otherwise, reset the trading volume and number of additional positions.
6. For each long position, take profit when the price rises by 1% and stop loss when it falls by 1%; vice versa for short positions.
7. Mark buy and sell points on the chart.

#### Strategy Advantages
1. Combines the MACD trend-following indicator with Martingale money management, which can better capture trending markets.
2. Sets fixed take profit and stop loss levels to control individual trade risk.
3. Uses limited Martingale position sizing to achieve higher returns when trends continue.
4. Limits the maximum number of additional positions to 3, avoiding the risk of excessive position sizing leading to account blowouts.
5. Marks buy and sell signals on the chart for easy observation of strategy performance.

#### Strategy Risks
1. The MACD indicator may experience divergence between signals and price, leading to misjudgment.
2. Fixed take profit and stop loss ratios may miss out on larger profit opportunities or incur greater losses.
3. Although Martingale position sizing is limited to 3 times, there is still a risk of account blowouts when experiencing consecutive losses in choppy markets.
4. The strategy does not consider abnormal market fluctuations, such as sudden gaps, which may result in inability to execute as expected.

#### Strategy Optimization Directions
1. Consider introducing trend confirmation indicators, such as MA, to filter MACD signals.
2. Optimize the take profit and stop loss settings, such as using ATR or percentages for dynamic stop losses.
3. Optimize the number and ratio of additional positions to control drawdown risk.
4. Set up mechanisms to deal with abnormal market conditions, such as suspending trading when prices gap.
5. Consider introducing position sizing to dynamically adjust positions based on market volatility.

#### Summary
This strategy captures trends through the MACD indicator while using limited Martingale to control drawdowns, which can achieve good results in trending markets. However, the strategy also has certain risks, such as signal failure and fixed stop losses. By introducing other indicators, optimizing parameter settings, position sizing, and other methods, the robustness and profitability of this strategy can be further improved.

[/trans]


> Source (PineScript)

```pinescript
//@version=5
strategy("Advanced MACD Strategy with Limited Martingale", overlay=true, initial_capital=100)

// MACD settings
fastLength = 15
slowLength = 30
signalSmoothing = 9
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// Contract size and previous trade result record
var float contractSize = 0.01
var int martingaleCount = 0 // Martingale count
var float lastTradeResult = 0

// Buy and sell conditions
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// Buy signal
if (longCondition)
    strategy.entry("Long", strategy.long, qty=contractSize)
    lastTradeResult := strategy.netprofit

// Sell signal
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=contractSize)
    lastTradeResult := strategy.netprofit

// Take profit and stop loss conditions
strategy.close("Long", when=(close / strategy.position_avg_price >= 1.01))
strategy.close("Short", when=(strategy.position_avg_price / close >= 1.01))
strategy.close("Long", when=(close / strategy.position_avg_price <= 0.99))
strategy.close("Short", when=(strategy.position_avg_price / close <= 0.99))

// Martingale strategy application
if (strategy.netprofit < lastTradeResult)
    if (martingaleCount < 3)
        contractSize := contractSize * 2
        martingaleCount := martingaleCount + 1
    else
        contractSize := 0.01
        martingaleCount := 0
```

Note: The PineScript code has been formatted and translated to maintain the original structure and functionality.