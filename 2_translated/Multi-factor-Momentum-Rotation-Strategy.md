> Name

Multi-factor-Momentum-Rotation-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b5dcde95f20d6f98b1.png)

[trans]


## Overview

This strategy combines RSI, MACD, Bollinger Bands, and limit up/down factors to implement multi-factor momentum rotation trading. The strategy first judges if multiple technical indicators give buy or sell signals simultaneously. If so, corresponding buy or sell operations will be executed. Meanwhile, the strategy adopts moving stop profit and stop loss to lock in profits and control risks.

## Strategy Logic

The main components of this strategy are:

1. Factor Judgment

   - RSI: Calculate 14-period RSI and judge if it is lower than the buy line or higher than the sell line
   - TD Sequence: Calculate the number of limit up/down days and judge if it meets buy/sell conditions
   - MACD: Calculate MACD and MACD Histogram to judge buy/sell conditions  
   - Bollinger Bands: Calculate 20-period BBs and judge if price touches BBs' upper or lower band

2. Entry and Exit

   - Buy Condition: RSI, MACD, TD Sequence give buy signals together  
   - Sell Condition: RSI, MACD, TD Sequence give sell signals together
   - Stop Profit: Use fixed points or percentage as trailing stop profit
   - Stop Loss: Set maximum tolerated loss points for stop loss

3. Strategy Optimization

   - Adjust RSI Parameters: Optimize RSI period parameter
   - Adjust MA Period: Optimize period parameter of Moving Averages  
   - Adjust Entry Conditions: Add or reduce entry signals
   - Add Other Factors: Incorporate more technical indicators and statistical factors

## Advantage Analysis

- Multiple Factors Improve Entry Accuracy

  The strategy considers multiple factors like RSI and MACD rather than just a single indicator. This reduces false signals and improves entry accuracy.

- Momentum Characteristic Captures Trends

  Indicators like RSI and MACD have obvious momentum characteristics, which capture price trend changes. They are more sensitive than trend-following indicators like moving averages.

- Stop Profit/Stop Loss Mechanism Controls Risks

  Moving stop profit can lock in profits dynamically following the market. Stop loss setting controls single trade loss.

- Simple and Clear Logic

  The strategy combines common technical indicators and has certain universality. Its rules are relatively simple and clear.

## Risk Analysis

- Poor Performance in Bull Market

  The strategy focuses on mean-reversion trading. It may trigger frequent stop loss in a bull market.

- Potentially Too High Trading Frequency

  If parameters are set too sensitively, trading frequency may be too high, increasing costs and slippage.

- Divergence Risk Across Indicators

  The strategy relies on consistent signals across indicators, but sometimes divergences may happen, resulting in wrong signals.

- Stop Loss Being Penetrated

  Fixed stop loss points may be penetrated. Dynamic stop loss or stock change may help avoid this risk.

## Optimization Directions

- Optimize Parameters to Reduce Trading Frequency

  Test RSI parameters and MA periods to find combinations with lower trading frequency.

- Add Statistical Factors to Improve Efficiency

  Incorporate stock-specific stats like volatility and liquidity to set parameters and improve efficiency.

- Combine Market-Level Indicators Like VIX

  Adjust strategy parameters based on market panic indicators like VIX to reduce trading frequency during market-wide crashes.

- Test Different Holding Periods

  Test long-term holding versus short-term rotation to see their impact on strategy performance.

- Optimize and Test Stop Profit/Stop Loss

  Research more advanced dynamic stop profit/stop loss techniques and backtest them.

## Summary

This strategy combines multiple technical indicators and adopts moving stop profit/loss to lock in profits and control risks while ensuring high entry accuracy. The logic is simple and clear. Performance can be further improved through parameter optimization and indicator selection. But the strategy is more suitable for mean-reversion and range-bound markets. It may underperform in persistent uptrends. In summary, this is a typical multi-factor mean-reversion momentum strategy that provides ideas and reference for stock rotation trading.

|||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|-7|RSI Difference|
|v_input_2