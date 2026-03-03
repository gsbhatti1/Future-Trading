> Name

Dynamic RSI Low-High Point Divergence Trend Strategy - Dynamic-RSI-Low-High-Point-Divergence-Trend-Strategy

> Author

ianzeng123

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/2d8d8b0a248a1a68fa372.png)
![IMG](https://www.fmz.com/upload/asset/2d8e4668d70229a0ffdc8.png)

#### Overview

This article elaborates on a trading strategy based on the Relative Strength Index (RSI) low-high point divergence. The strategy identifies potential trend reversals by detecting divergences between price and RSI indicators, providing traders with precise entry and exit signals. By combining visual signals and technical analysis, this strategy aims to enhance the accuracy and timeliness of trading decisions.

#### Strategy Principles

The core principle is based on the RSI low-high point divergence theory. Key implementation steps include:

1. **RSI Calculation**: Using a 14-period RSI length to assess market overbought and oversold conditions.
2. **Price Extreme Identification**: Determining low and high points through a lookback period.
3. **Divergence Judgment Mechanism**:
   - **Bullish Divergence**: Price makes a new low, but the RSI does not synchronously decline.
   - **Bearish Divergence**: Price makes a new high, but the RSI does not synchronously rise.
4. **Signal Generation**:
   - Bullish divergence in an oversold zone (below 30).
   - Bearish divergence in an overbought zone (above 70).

#### Strategy Advantages

1. **High Precision Signal Identification**: Reduces false signals through strict divergence conditions.
2. **Visualized Signals**: Large triangular markers and background highlighting enhance signal readability.
3. **Flexibility**: Adjustable RSI parameters, lookback periods, and overbought/oversold thresholds.
4. **Multi-Timeframe Adaptability**: Best performance on 1-hour to 4-hour timeframes.
5. **Debugging Functionality**: Built-in debug table for verifying key indicators.

#### Strategy Risks

1. **Misjudgment Risk**: Divergence signals are not always accurate, and there is a risk of false signals.
2. **Market Volatility**: The strategy may underperform in strongly trending markets.
3. **Parameter Sensitivity**: Improperly set RSI parameters and lookback periods can reduce the effectiveness of the strategy.
4. **Transaction Costs**: Frequent trading can lead to higher commission and slippage expenses.

#### Strategy Optimization Directions

1. **Multi-Indicator Confirmation**: Incorporate moving averages, MACD to improve signal accuracy.
2. **Dynamic Parameter Adjustment**: Adjust RSI parameters intelligently based on market volatility.
3. **Stop-Loss Mechanism**: Introduce an ATR-based dynamic stop-loss strategy.
4. **Machine Learning Optimization**: Use machine learning algorithms to optimize entry and exit points.
5. **Risk Management**: Adjust position sizes based on market volatility.

#### Summary

The Dynamic RSI Low-High Point Divergence Trend Strategy provides traders with a relatively efficient trend trading method through precise technical indicator analysis and visual signals. Continuous optimization and risk management can help maintain stable performance across different market environments.

|| 

#### Source (PineScript)

```pinescript
// backtest
// start: 2024-03-31 00:00:00
// end: 2025-03-29 08:00:00
// period: 1d
// basePeriod: 1d
// exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]

//@version=6
strategy("RSI Divergence Strategy - Visible Signals", overlay=true)

// 1. Basic Inputs (Keep it simple)
rsiLength = input.int(14, "RSI Length")
lookback = input.int(10, "Lookback Period", minval=5)
oversold = input.int(30, "Oversold Level")
overbought = input.int(70, "Overbought Level")

// 2. Calculate Indicators
rsi = ta.rsi(close, rsiLength)
priceLow = ta.lowest(low, lookback)
priceHigh = ta.highest(high, lookback)
rsiLow = ta.lowest(rsi, lookback)
rsiHigh = ta.highest(rsi, lookback)

// 3. Simple Divergence Detection
bullishDiv = low == priceLow and rsi > rsiLow and rsi < oversold
bearishDiv = high == priceHigh and rsi < rsiHigh and rsi > overbought

// 4. Visual Signals (Large and Clear)
plotshape(bullishDiv, "Buy", shape.triangleup, location.belowbar,
          color=color.new(color.green, 0), size=size.large)
plotshape(bearishDiv, "Sell", shape.triangledown, location.abovebar,
          color=color.new(color.red, 0), size=size.large)

// 5. Optional: Add Background for Better Visibility
bgcolor(bullishDiv ? color.new(color.green, 90) : bearishDiv ? color.new(color.red, 90) : na)

// 6. Basic Strategy Execution
if bullishDiv
    strategy.entry("Long", strategy.long)
    
if bearishDiv
    strategy.entry("Short", strategy.short)

// 7. Debugging Table (To verify values)
var table debugTable = table.new(position.top_right, 4, 1)
if barstate.islast
    table.cell(debugTable, 0, 0, "RSI: " + str.tostring(rsi))
    table.cell(debugTable, 1, 0, "Price Low: " + str.tostring(priceLow))
    table.cell(debugTable, 2, 0, "RSI Low: " + str.tostring(rsiLow))
    table.cell(debugTable, 3, 0, "Signal: " + (bullishDiv ? "BUY" : bearishDiv ? "SELL" : "NONE"))
    // Test Settings (paste these above the strategy call)
//rsiLength := 5
```