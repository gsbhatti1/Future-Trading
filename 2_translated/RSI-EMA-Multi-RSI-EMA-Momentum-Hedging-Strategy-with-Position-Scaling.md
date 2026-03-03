> Name

Multi-RSI-EMA Momentum Hedging Strategy with Position Scaling

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/14edc3c85ba62e7d24a.png)

[trans]
#### Overview
This is a trading strategy based on RSI indicators and EMA moving averages. The strategy utilizes dual RSI time periods (RSI-14 and RSI-2) combined with triple EMA lines (50, 100, 200) to capture market trend reversal opportunities, implementing hedging through dynamic position management. The core feature of the strategy is to gradually increase positions when entry conditions are met, with profit-taking conditions based on RSI overbought/oversold levels.

#### Strategy Principles
The strategy employs RSI-14 and RSI-2 with different periods, along with EMA-50, EMA-100, and EMA-200 to determine trading signals. Long conditions require RSI-14 below 31 and RSI-2 crossing above 10, while EMAs must be in bearish alignment (EMA-50 < EMA-100 < EMA-200). Short conditions are opposite, requiring RSI-14 above 69 and RSI-2 crossing below 90, with EMAs in bullish alignment (EMA-50 > EMA-100 > EMA-200). The strategy uses 20x leverage and dynamically calculates trade quantities based on current equity. New positions are opened with twice the current position size when conditions are met. Take-profit conditions are set based on RSI indicator reverse breakouts.

#### Strategy Advantages
1. Multiple technical indicator cross-validation improves signal reliability
2. Dynamic position management allows flexible portfolio adjustment
3. Bi-directional trading mechanism enables profit from both directions
4. Adaptive take-profit conditions prevent premature exits
5. Clear graphical interface showing trading signals and market conditions
6. Hedging mechanism reduces directional risk exposure
7. Equity-based dynamic position calculation for better risk control

#### Strategy Risks
1. High leverage (20x) may lead to significant liquidation risks
2. Incremental positioning could cause severe losses during market volatility
3. Absence of stop-loss conditions may face continuous drawdown risks
4. RSI indicators may generate false signals in ranging markets
5. Multiple technical indicator combination may reduce trading opportunities
6. Position management method may accumulate excessive risk during consecutive trades

#### Strategy Optimization Directions
1. Introduce adaptive stop-loss mechanism based on ATR or volatility
2. Optimize leverage multiplier with dynamic adjustment based on market volatility
3. Add time filters to avoid trading during low volatility periods
4. Incorporate volume indicators to improve signal reliability
5. Optimize position increment multiplier with maximum position limits
6. Add trend strength filters to avoid trading in weak trends
7. Enhance risk management with daily maximum loss limits

#### Summary
This comprehensive strategy combines momentum and trend following, using multiple technical indicators to improve trading accuracy. The strategy innovates through dynamic position management and hedging mechanisms, though it carries significant risks. Through optimization of risk control mechanisms and introduction of additional filters, this strategy has potential for better performance in live trading. Thorough backtesting and parameter optimization are recommended before live implementation.[/trans]


> Source (PineScript)

```pinescript
//@version=5
strategy("Custom RSI EMA Strategy Hedge", overlay=true, default_qty_type=strategy.fixed, default_qty_value=1)

// Defining entry conditions
rsi_14 = ta.rsi(close, 14)
rsi_2 = ta.rsi(close, 2)
ema_50 = ta.ema(close, 50)
ema_100 = ta.ema(close, 100)
ema_200 = ta.ema(close, 200)

// Leverage effect
leverage = 20

// Conditions for long position
longCondition = (rsi_14[1] < 31) and ta.crossover(rsi_2, 10) and (ema_50 < ema_100) and (ema_100 < ema_200)

// Conditions for short position
shortCondition = (rsi_14[1] > 69) and ta.crossunder(rsi_2, 90) and (ema_50 > ema_100) and (ema_100 > ema_200)

// Position identifiers
long_id = "Long"
short_id = "Short"

// Defining average position price for long and short
var float long_avg_price = na
var float short_avg_price = na

// Tracking changes in position size
var float last_long_position_size = na
var float last_short_position_size = na

// Breaking average position price when position size changes
if (last_long_position_size != strategy.position_size and strategy.position_size > 0)
    long_avg_price := na
if (last_short_position_size != strategy.position_size and strategy.position_size < 0)
    short_avg_price := na

// Updating average position price
if (strategy.position_size > 0)
    long_avg_price := (long_avg_price * strategy.position_size + close) / strategy.position_size

if (strategy.position_size < 0)
    short_avg_price := (short_avg_price * strategy.position_size + close) / strategy.position_size

// ...
```