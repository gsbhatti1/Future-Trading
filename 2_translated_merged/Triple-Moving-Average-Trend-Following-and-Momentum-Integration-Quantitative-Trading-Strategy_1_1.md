> Name

Triple Moving Average Trend Following and Momentum Integration Quantitative Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1184187f636090839af.png)

[trans]
#### Overview
This is a quantitative trading strategy combining trend following and momentum analysis. It uses Triple Exponential Moving Average (TEMA), multiple moving average crossovers, and a MACD variant indicator to identify market trends and entry timing. The strategy incorporates strict risk control mechanisms including fixed stop-loss, profit targets, and trailing stop-loss to achieve optimal risk-reward balance.

#### Strategy Principle  
The strategy determines trading signals mainly through three core technical indicator systems:
1. The Triple Exponential Moving Average (TEMA) system confirms the overall trend direction. By calculating three layers of EMA combined with their dynamic changes, it judges the trend strength.
2. The fast/slow moving average crossover system uses 9-period and 15-period EMAs to capture turning points of medium-term trends.
3. The price crossover with the 5-period EMA serves as the final confirmation signal to precisely grasp entry timing.

Trading signals are triggered only when all the following conditions are met:
- MACD indicator forms a golden cross with its signal line and TEMA trend is upward
- Short-term EMA crosses above long-term EMA  
- Price crosses above the 5-period EMA

#### Strategy Advantages
1. The multi-confirmation mechanism greatly reduces the impact of false signals and improves trading accuracy.
2. Combining trend following and momentum analysis enables capturing both major trends and short-term opportunities.
3. Comprehensive stop-loss mechanisms including fixed stop-loss levels and dynamic trailing stop-loss effectively control risk.
4. Strong parameter adjustability adapts to different market environments.
5. Clear entry logic is easy to understand and execute.

#### Strategy Risks
1. The multi-confirmation mechanism may cause slower entry timing, missing some opportunities in fast-moving markets.
2. Fixed stop-loss levels need adjustment according to different market volatilities; otherwise, premature stop-outs may occur.
3. Frequent false signals may be generated in range-bound oscillating markets.
4. Trailing stop-loss may exit quality trends prematurely during violent market fluctuations.

#### Strategy Optimization Directions
1. Introduce volatility indicators to dynamically adjust stop-loss and profit targets to better match market conditions.
2. Add volume indicators as auxiliary confirmation to enhance signal reliability.
3. Incorporate market regime identification mechanisms to use different parameter sets under varying market conditions.
4. Develop contrarian pyramiding mechanisms for moderate position building during pullbacks to enhance returns.
5. Optimize the trailing stop-loss algorithm for better adaptation to market volatility.

#### Summary
This strategy constructs a robust trading system by integrating multiple technical indicator systems. Its core advantage lies in the multi-confirmation mechanism and comprehensive risk control framework. Although there are certain lag risks, the strategy still has significant room for improvement through parameter optimization and functionality enhancements. It is suitable for traders pursuing steady returns.
[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2024-10-01 00:00:00
end: 2024-10-31 23:59:59
period: 2h
basePeriod: 2h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("ITG Scalper Strategy", shorttitle="lokesh_ITG_Scalper_Strategy", overlay=true)

// General inputs
len = input(14, title="TEMA period")
FfastLength = input.int(13, title="Filter fast length")
FslowLength = input.int(18, title="Filter slow length")
FsignalLength = input.int(14, title="Filter signal length")
sl_points = 7 // 5 points stop loss
tp_points = 100 // 100 points target profit
trail_points = 15 // Trailing stop loss every 10 points

// Validate input
if FfastLength < 1
    FfastLength := 1
if FslowLength < 1
    FslowLength := 1
if FsignalLength < 1
    FsignalLength := 1

// Get real close price
realC = close

// Triple EMA definition
ema1 = ta.ema(realC, len)
ema2 = ta.ema(ema1, len)
ema3 = ta.ema(ema2, len)

// Triple EMA trend calculation
avg = 3 * (ema1 - ema2) + ema3

// Filter formula
Fsource = close
FfastMA = ta.ema(Fsource, FfastLength)
FslowMA = ta.ema(Fsource, FslowLength)
Fmacd = FfastMA - FslowMA
Fsignal = ta.sma(Fmacd, FsignalLength)

// Plot EMAs for visual reference
shortema = ta.ema(close, 9)
longema = ta.ema(close, 15)
yma = ta.ema(close, 5)
plot(shortema, color=color.green)
plot(longema, color=color.red)
plot(yma, color=#e9f72c)

// Entry conditions
firstCrossover = ta.crossover(Fmacd, Fsignal) and avg > avg[1]
secondCrossover = ta.crossover(shortema, longema)  // Assuming you meant to cross shortema with longema
thirdCrossover = ta.crossover(close, yma)

var bool entryConditionMet = false

if (firstCrossover)
    entryConditionMet := true

longSignal = entryConditionMet and secondCrossover and thirdCrossover

// Strategy execution
if (longSignal)
    strategy.entry("Long", strategy.long)
    entryConditionMet := false  // Reset the entry condition after taking a trade

// Calculate stop loss and take profit prices
var float long_sl = na
var float long_tp = na

if strategy.position_size > 0  // Long position
    long_sl := close - sl_points
    long_tp := close + tp_points
    
    // Adjust stop loss with trailing logic
    if (close - long_sl > trail_points)
        long_sl := close - trail_points
        
    strategy.exit("Exit Long", "Long", stop=long_sl, limit=long_tp)

// Plotting Buy signals
plotshape(series=longSignal, style=shape.triangleup, location=location.belowbar, color=color.green, size=size.small, title="Buy Signal")

// Alerts
alertcondition(longSignal, title="Buy Signal", message="Buy Signal")
```

> Detail

https://www.fmz.com/strategy/473145

> Last Modified

2024-11-27 16:08:16