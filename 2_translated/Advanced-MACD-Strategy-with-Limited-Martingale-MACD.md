> Name

Advanced-MACD-Strategy-with-Limited-Martingale

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19d896963817e1d58ec.png)
[trans]
#### Overview
This strategy combines the MACD indicator with a limited Martingale money management approach to capture trading opportunities during market trend changes. It generates buy signals when the MACD fast line crosses above the slow line (golden cross), and sell signals when the fast line crosses below the slow line (death cross). Meanwhile, the strategy employs a limited Martingale method to control drawdown, allowing up to 3 additional positions. Each trade has a fixed take-profit and stop-loss set at 1%.

#### Strategy Principle
1. Calculate the fast line, slow line, and signal line of the MACD indicator.
2. Judge the crossover situation between the fast and slow lines: go long on golden crosses, and go short on death crosses.
3. Set a fixed lot size per trade (0.01).
4. Record the net profit from the previous trade.
5. If the current net profit is less than the previous trade's profit and the number of additional trades is less than 3, double the next trade's volume and increment the additional trade count by one; otherwise, reset the trade volume and additional trade count.
6. For each long trade, take profit when the price rises by 1%, and stop loss when it drops by 1%; conversely for short trades.
7. Mark buy and sell points on the chart.

#### Strategy Advantages
1. Combines the trend-following indicator MACD with Martingale money management, effectively capturing trending market movements.
2. Implements fixed take-profit and stop-loss settings to control single-trade risk.
3. Utilizes limited Martingale scaling-in to achieve higher profits during trend continuation.
4. Caps additional trades at three times, preventing over-scaling that could lead to account blowout.
5. Charts buy and sell signal markers for convenient observation of strategy effectiveness.

#### Strategy Risks
1. The MACD indicator might produce divergent signals compared to price action, leading to incorrect judgments.
2. Fixed take-profit and stop-loss percentages may either miss larger profit potential or incur greater losses.
3. Although Martingale scaling is capped at three times, consecutive losses in range-bound markets still pose a blowout risk.
4. The strategy does not account for abnormal market volatility such as sudden gaps, potentially causing execution issues.

#### Strategy Optimization Directions
1. Introduce trend confirmation indicators like MA to filter MACD signals.
2. Optimize take-profit and stop-loss configurations using dynamic methods such as ATR or percentage-based stops.
3. Fine-tune the frequency and scale of additional trades to manage drawdown risk.
4. Implement contingency plans for abnormal market conditions, such as pausing trades during price gaps.
5. Incorporate position sizing strategies that dynamically adjust positions based on market volatility.

#### Summary
This strategy captures trends via the MACD indicator while employing a limited Martingale approach to control drawdowns, performing well in trending markets. However, it carries inherent risks such as false signals and fixed stop-losses. Enhancing robustness and profitability can be achieved through incorporating additional indicators, optimizing parameters, and implementing advanced position sizing techniques.

[/trans]

> Source (PineScript)

``` pinescript
/*backtest
start: 2024-04-01 00:00:00
end: 2024-04-30 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Advanced MACD Strategy with Limited Martingale", overlay=true, initial_capital=100)

// MACD settings
fastLength = 15
slowLength = 30
signalSmoothing = 9
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// Contract size and record of previous trade results
var float contractSize = 0.01
var int martingaleCount = 0 // Martingale count
var float lastTradeResult = 0

// Buy and sell conditions
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// Long signal
if (longCondition)
    strategy.entry("Long", strategy.long, qty=contractSize)
    lastTradeResult := strategy.netprofit

// Short signal
if (shortCondition)
    strategy.entry("Short", strategy.short, qty=contractSize)
    lastTradeResult := strategy.netprofit

// Take-profit and stop-loss conditions
strategy.close("Long", when=(close / strategy.position_avg_price >= 1.01))
strategy.close("Short", when=(strategy.position_avg_price / close >= 1.01))
strategy.close("Long", when=(close / strategy.position_avg_price <= 0.99))
strategy.close("Short", when=(strategy.position_avg_price / close <= 0.99))

// Apply Martingale strategy
if (strategy.netprofit < lastTradeResult)
    if (martingaleCount < 3)
        contractSize := contractSize * 2
        martingaleCount := martingaleCount + 1
    else
        contractSize := 0.01
        martingaleCount := 0
else
    contractSize := 0.01
    martingaleCount := 0

// Mark buy and sell points with arrows
plotshape(series=longCondition, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")
```

> Detail

https://www.fmz.com/strategy/451072

> Last Modified

2024-05-11 17:24:43