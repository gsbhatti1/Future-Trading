> Name

Crossover-Strategy-between-Multiple-Moving-Averages

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/168629d3c50cb9f04de.png)
[trans]

## Overview

This strategy uses the calculation of multiple moving averages with different time periods to determine trends across various timeframes. When the price breaks through the moving averages of different periods, corresponding buy or sell operations are performed. At the same time, combining stop loss and take profit methods, it achieves a balance between risk and reward.

## Strategy Principles

The strategy is mainly based on the following points:

1. Calculate simple moving averages for 21-day, 50-day, 100-day, and 200-day periods.
2. Buy when the price crosses above any of the moving averages; sell when the price crosses below.
3. Set the stop loss near the lowest price of the previous bar after going long, and near the highest price after going short.
4. Set the take profit targets within a certain range below the lowest price for long positions and above the highest price for short positions.
5. Close positions when the price touches the stop loss or take profit levels.

This multi-timeframe approach can improve the reliability of trading signals and follow trends when they are clear. The stop loss and take profit settings control risks by exiting positions when losses expand or profits reach a certain level.

## Advantages

This strategy mainly has the following advantages:

1. Improved signal reliability through multi-timeframe analysis. Different moving average crossovers help filter out some false signals and allow us to trade during clearer trend moments.
2. Dynamic stop loss and take profit mechanisms facilitate risk control. Calculating stop loss and take profit levels based on price action provides reasonable ranges to limit maximum loss per trade.
3. Clear and simple code structure. The Pine script syntax offers readable structures to easily adjust parameters and optimize.
4. Easy practical application. Moving average crossovers are a classic strategy idea that can be easily implemented in live trading with proper parameter tuning.

## Risks

This strategy also has some risks, mainly including:

1. Inaccurate trend judgment. Moving averages can produce mixed signals and lag, leading to improper trade signals.
2. Large losses in volatile markets. Stop losses may get triggered easily in huge price gaps or reversals, incurring significant losses.
3. Improper parameter settings can increase losses. Overly wide stop loss or tight take profit levels can increase the maximum loss per trade.
4. Long holding risks. This trend-following strategy does not consider long-term profitability and can consume substantial capital over time.
5. Real trading differences. Trading costs, slippage, etc., can affect returns when applied in actual trading platforms.

Solutions:

1. Add signal confirmation with other indicators like KDJ, MACD, etc.
2. Adjust stop loss based on market conditions to avoid premature triggering.
3. Optimize parameters and evaluate long-term returns and drawdowns. Obtain the best parameter combinations through rigorous backtesting.
4. Thoroughly test strategies in paper trading and add manual stops.

## Enhancement Opportunities

There is room for further improvements:

1. Add quantitative entry and exit rules. For example, check for new highs and lows to ensure trading at clearer trends.
2. Incorporate position sizing and risk management. Dynamically size positions based on account size and market conditions.
3. Enhance trend validation. Use indicators like PRZ, ATR, DMI, etc., to filter and select appropriate trends.
4. Set trailing stops on profits to lock in gains.
5. Construct stock pool using factor investing models. Score and filter stocks on various factors.
6. Add machine learning for risk control. Use LSTM, RNN, etc., to assist in judgment and prevent human errors.

## Conclusion

This simple moving average crossover strategy offers easy implementation for trend following. The dynamic stop loss and take profit mechanisms help control risks. However, some signal inaccuracies and whipsaw risks exist. Further optimizations on parameters and additional techniques can lead to more robust performance.

[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-04 00:00:00
end: 2024-02-03 00:00:00
period: 4h
basePeriod: 15m
exchanges: [
   交易所名称
]
```

Please replace `"交易所名称"` with the actual name of the exchange you want to use.