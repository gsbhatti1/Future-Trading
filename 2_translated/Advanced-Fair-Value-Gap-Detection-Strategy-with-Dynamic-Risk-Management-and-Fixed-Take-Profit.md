<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

Advanced-Fair-Value-Gap-Detection-Strategy-with-Dynamic-Risk-Management-and-Fixed-Take-Profit

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13e6bfcba3ff6117aab.png)

[trans]
#### Overview
This is a trading strategy based on Fair Value Gap (FVG) detection, combined with dynamic risk management and fixed take-profit targets. The strategy operates on a 15-minute timeframe, identifying potential trading opportunities by capturing price gaps in the market. According to backtesting data from November 2023 to August 2024, the strategy achieved a net return of 284.40%, completed a total of 153 trades, with a win rate of 71.24% and a profit factor of 2.422.

#### Strategy Principle
The core of the strategy involves monitoring price relationships among three consecutive candles to identify fair value gaps. Specifically:
1. Bullish FVG formation condition: The high of the current candle is lower than the low of the previous two candles.
2. Bearish FVG formation condition: The low of the current candle is higher than the high of the previous two candles.
3. Entry signals are controlled by an FVG threshold parameter; only gaps exceeding a certain percentage of price will trigger entries.
4. Risk control employs a fixed percentage (1%) of account equity as the stop-loss standard.
5. Profit targets use fixed points (50 points).

#### Strategy Advantages
1. Scientific and reasonable risk management: Using account equity percentage for stop-loss allows dynamic risk control.
2. Clear trading rules: Fixed profit targets avoid subjective judgment.
3. Excellent performance: High win rate and profit factor indicate good strategy stability.
4. Simple implementation: Clear code logic makes it easy to understand and maintain.
5. Strong adaptability: Adjustable parameters allow adaptation to different market environments.

#### Strategy Risks
1. Market volatility risk: Fixed-point profit targets may lack flexibility during high-volatility periods.
2. Slippage risk: Frequent trading could lead to higher slippage costs.
3. Parameter dependence: Strategy performance heavily depends on the FVG threshold setting.
4. False breakout risk: Some FVG signals might be false breakouts requiring additional confirmation indicators.
5. Fund management risk: Fixed percentage stop-loss can rapidly erode capital during consecutive losses.

#### Strategy Optimization Directions
1. Introduce market volatility indicators to dynamically adjust profit targets.
2. Add trend filters to avoid trading during sideways markets.
3. Develop multi-timeframe confirmation mechanisms.
4. Optimize position management algorithms by introducing floating position systems.
5. Add trading time filters to avoid high-volatility periods.
6. Develop signal strength scoring systems to filter high-quality trading opportunities.

#### Summary
By integrating Fair Value Gap theory with scientific risk management methods, this strategy demonstrates excellent trading performance. Its high win rate and stable profit factor indicate practical value. There's room for further improvement through the suggested optimizations. It is recommended that traders conduct sufficient parameter optimization and backtesting validation before using it in live trading. ||

#### Overview
This is a trading strategy based on Fair Value Gap (FVG) detection, combining dynamic risk management with fixed take profit targets. Operating on a 15-minute timeframe, the strategy identifies potential trading opportunities by detecting price gaps in the market. According to backtest data from November 2023 to August 2024, the strategy achieved a net profit of 284.40% with 153 total trades, maintaining a win rate of 71.24% and a profit factor of 2.422.

#### Strategy Principle
The core mechanism revolves around detecting Fair Value Gaps by monitoring price relationships across three consecutive candles:
1. Bullish FVG: When the high of the middle candle is below the low of the first candle
2. Bearish FVG: When the low of the middle candle is above the high of the first candle
3. Entry signals are controlled by an FVG threshold parameter
4. Risk control uses a fixed percentage (1%) of account equity as stop loss
5. Take profit is set at a fixed 50 points

#### Strategy Advantages
1. Scientific risk management: Uses account equity percentage for stop loss
2. Clear trading rules: Fixed take profit targets eliminate subjective judgment
3. Excellent performance: High win rate and profit factor indicate strategy stability
4. Simple implementation: Clear code logic, easy to understand and maintain
5. High adaptability: Can be adjusted for different market conditions

#### Strategy Risks
1. Market volatility risk: Fixed point take profit may be inflexible in highly volatile markets
2. Slippage risk: Frequent trading may lead to higher slippage costs
3. Parameter dependency: Performance heavily relies on FVG threshold settings
4. False breakout risk: Some FVG signals might be false breakouts
5. Money management risk: Fixed percentage stop loss might lead to quick drawdowns

#### Optimization Directions
1. Introduce volatility indicators for dynamic take profit adjustment
2. Add trend filters to avoid ranging market trades
3. Develop multiple timeframe confirmation mechanism
4. Optimize position sizing algorithm with floating position system
5. Add trading time filters to avoid high volatility periods
6. Develop signal strength scoring system for high-quality trade selection

#### Summary
This strategy demonstrates impressive results by combining Fair Value Gap theory with scientific risk management. The high win rate and stable profit factor indicate its practical value. Through the suggested optimization directions, there is potential for further improvement. Traders are advised to conduct thorough parameter optimization and backtesting before live implementation.[/trans]

> Source (PineScript)

``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-28 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Fair Value Gap Strategy with % SL and Fixed TP", overlay=true, initial_capital=500, default_qty_type=strategy.fixed, default_qty_value=1)

// Parameters
fvgThreshold = input.float(0.5, "FVG Threshold (%)", minval=0.1, step=0.1)

// Fixed take profit in pips
takeProfitPips = 50

// Function to convert pips to price
pipsToPriceChange(pips) =>
    syminfo.mintick * pips * 10

// Function to detect Fair Value Gap
detectFVG(dir) =>
    gap = 0.0
    if dir > 0  // Bullish FVG
        gap := low[2] - high[1]
    else  // Bearish FVG
        gap := low[1] - high[2]
    math.abs(gap) > (close * fvgThreshold / 100)

// Detect FVGs
bullishFVG = detectFVG(1)
bearishFVG = detectFVG(-1)

// Entry conditions
longCondition = bullishFVG
shortCondition = bearishFVG

// Calculate take profit level
longTakeProfit = strategy.position_avg_price + pipsToPriceChange(takeProfitPips)
shortTakeProfit = strategy.position_avg_price - pipsToPriceChange(takeProfitPips)

// Calculate stop loss amount (5% of capital)
stopLossAmount = strategy.equity * 0.01

// Execute trades
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Set exit conditions
if (strategy.position_size > 0)
    strategy.exit("Long TP", "Long", limit=longTakeProfit)
    strategy.close("Long SL", when=strategy.openprofit < -stopLossAmount)
else if (strategy.position_size < 0)
    strategy.exit("Short TP", "Short", limit=shortTakeProfit)
    strategy.close("Short SL", when=strategy.openprofit < -stopLossAmount)

// Plot signals
plotshape(longCondition, "Buy Signal", location = location.belowbar, color = color.green, style = shape.triangleup, size = size.small)
plotshape(shortCondition, "Sell Signal", location = location.abovebar, color = color.red, style = shape.triangledown, size = size.small)
```

> Detail

https://www.fmz.com/strategy/473391

> Last Modified

2024-11-29 16:22:10