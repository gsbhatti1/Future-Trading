> Name

SMA-RSI-MACD Multi-Indicator Dynamic Limit Order Trading Strategy-SMA-RSI-MACD-Multi-Indicator-Dynamic-Limit-Order-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1947a3f1a718f6364f2.png)

[trans]
#### Overview
This strategy is a multi-technical indicator trading system that primarily uses EMA crossover, RSI oversold conditions, and MACD golden cross for trade confirmation. It employs dynamic limit orders for entry and multiple exit mechanisms for risk management. The strategy uses 9-period and 21-period Exponential Moving Averages (EMA) as primary trend indicators, combined with Relative Strength Index (RSI) and Moving Average Convergence Divergence (MACD) to filter trading signals.

#### Strategy Principles
The core trading logic includes the following key components:
1. Entry signals are triggered when 9-period EMA crosses above 21-period EMA.
2. Entry price is set as a limit order below the 9-period EMA at a specified offset.
3. Trade confirmation requires RSI below threshold and MACD golden cross.
4. Exit signals include MACD death cross, fixed profit/loss points, and forced closing at market end.
5. Trading time is restricted between 9:30 AM and 3:10 PM.

The strategy uses limit orders for entry to achieve better entry prices and combines multiple technical indicators to improve trading accuracy.

#### Strategy Advantages
1. Multiple signal confirmation mechanism improves trade reliability.
2. Limit order entries provide better execution prices.
3. Fixed profit/loss points facilitate risk control.
4. Forced closing at market end eliminates overnight risk.
5. Trading time restrictions avoid opening volatility.
6. EMA indicators provide faster trend response.
7. RSI and MACD combination helps filter false signals.

#### Strategy Risks
1. Multiple signal confirmation may cause missed opportunities.
2. Limit orders might not execute in rapid price movements.
3. Fixed point stops may result in larger losses during high volatility.
4. MACD signals may lag behind price action.
5. The strategy doesn't account for changes in market volatility.
6. Parameter optimization may lead to overfitting.

#### Strategy Optimization Directions
1. Introduce adaptive stop-loss and take-profit points based on market volatility.
2. Add volume indicators as additional confirmation signals.
3. Consider adding trend strength filters.
4. Optimize limit order offset calculation using ATR.
5. Include market sentiment indicators to filter unfavorable conditions.
6. Add position sizing mechanism based on signal strength.

#### Summary
This is a well-structured multi-indicator trading strategy that identifies trends using moving averages, filters signals with RSI and MACD, and controls risk through limit orders and multiple stop mechanisms. The strategy's strengths lie in its signal reliability and comprehensive risk control, though it faces challenges with signal lag and parameter optimization. There is significant room for improvement through dynamic parameter adjustment and additional auxiliary indicators. It is suitable for conservative investors in trending market conditions.

||

#### Source (PineScript)

```pinescript
//@version=5
strategy("SMA 9 & 21 with RSI and MACD Buy Strategy", overlay=true)

// Inputs for Simple Moving Averages
sma_short = ta.ema(close, 9)
sma_long = ta.ema(close, 21)

// Plotting SMA
plot(sma_short, color=color.green, title="SMA 9")
plot(sma_long, color=color.red, title="SMA 21")

// RSI Calculation
rsi_length = input.int(14, title="RSI Length")
rsi_threshold = input.int(70, title="RSI Threshold")
rsi = ta.rsi(close, rsi_length)

// MACD Calculation
macd_fast = input.int(8, title="MACD Fast Length")
macd_slow = input.int(18, title="MACD Slow Length")
macd_signal = input.int(6, title="MACD Signal Length")
[macd_line, signal_line, _] = ta.macd(close, macd_fast, macd_slow, macd_signal)

// Inputs for Limit Order Offset
limit_offset = input.int(50, title="Limit Order Offset", minval=1)  // 50 points below 9 EMA

// User input for specific date
simulationStartDate = input(timestamp("2024-12-01 00:00"), title="Simulation Start Date", group = "Simulation Dates")
simulationEndDate = input(timestamp("2024-12-30 00:00"), title="Simulation End Date", group = "Simulation Dates")

// Declare limit_price as float
var float limit_price = na

// Calculate Limit Order Price
if (sma_short[1] < sma_long[1] and sma_short > sma_long)  // 9 EMA crosses above 21 EMA
    limit_price := sma_short - limit_offset

// Buy Signal Condition (only on the specified date)
buy_condition = not na(limit_price) and rsi < rsi_threshold and ta.crossover(macd_line, signal_line)

// Sell Signal Condition (MACD crossover down)
sell_condition = ta.crossunder(macd_line, signal_line)

// Track Entry Price
```

This PineScript code defines the trading strategy with the specified inputs and logic for entry and exit conditions based on EMA crossovers, RSI levels, MACD signals, and dynamic limit orders.