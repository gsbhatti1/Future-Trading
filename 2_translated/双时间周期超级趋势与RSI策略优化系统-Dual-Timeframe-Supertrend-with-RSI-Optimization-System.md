> Name

Dual-Timeframe SuperTrend with RSI Optimization System

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/12f6b3f0d57f84c529c.png)

#### Overview
This strategy is a dual-timeframe trading system based on the SuperTrend indicator and RSI. It combines technical analysis indicators from 120-minute and 15-minute timeframes, using SuperTrend to capture medium-term trend direction while utilizing RSI for profit-taking. The strategy implements position sizing through percentage allocation and includes percentage-based take-profit conditions.

#### Strategy Principles
The core logic is built on several key elements:
1. Uses 120-minute timeframe SuperTrend indicator as the main trend determination tool, with ATR period of 14 and factor of 3.42
2. Generates trading signals through price crossovers with SuperTrend line - upward crosses for long entries and downward crosses for short entries
3. Employs 15-minute timeframe RSI indicator with period 5 as a supplementary tool for market overbought/oversold conditions
4. Closes long positions when RSI reaches overbought zone (95) and short positions at oversold zone (5)
5. Sets 30% take-profit level calculated relative to entry average price

#### Strategy Advantages
1. Multiple timeframe combination improves signal reliability and reduces false signals
2. Optimized SuperTrend parameters balance trend sensitivity while avoiding excessive trading
3. Strict RSI extreme values (5 and 95) ensure position closing only in extreme conditions
4. Position sizing uses fixed percentage of equity (35%), effectively controlling risk while maintaining profit potential
5. Automatically closes reverse positions before opening new ones, avoiding simultaneous long and short exposure

#### Strategy Risks
1. Dual timeframe approach may create lag in ranging markets, requiring drawdown management
2. Strict RSI extreme values might cause missed profit-taking opportunities
3. 30% take-profit level is aggressive, potentially leading to early exits in volatile markets
4. Lack of stop-loss conditions could result in significant losses during sudden trend reversals
5. 35% position sizing is relatively aggressive, creating high risk during extreme volatility

#### Optimization Directions
1. Recommend adding dynamic stop-loss mechanism, considering ATR-based trailing stops
2. RSI overbought/oversold thresholds could be adjusted to 10 and 90 for better adaptability
3. Volume indicators could be added for signal confirmation
4. Consider dynamic position sizing based on market volatility using ATR or volatility indicators
5. Suggest adding trend strength filters like DMI or ADX to filter weak trends

#### Summary
This is a well-structured trend-following strategy with clear logic. It combines different timeframe technical indicators to capture trends while maintaining risk control. While there's room for optimization, the overall design aligns with quantitative trading principles. Traders should backtest and optimize parameters before live trading and adjust position sizing according to their risk tolerance.

#### Source (PineScript)

```pinescript
//@version=5
strategy("Supertrend Strategy", overlay=true)

// Function for Supertrend
supertrend(_factor, _atrPeriod) =>
    [out, _] = ta.supertrend(_factor, _atrPeriod)
    out

// Supertrend Settings
factor = input.float(3.42, title="Supertrend Factor")
atrPeriod = input.int(14, title="ATR Period")
tf2 = input.timeframe("120", title="Supertrend Timeframe")

// RSI Settings
rsi_tf = input.timeframe("15", title="RSI Timeframe")
rsiLength = input.int(5, title="RSI Length")
rsiUpper = input.int(95, title="RSI Upper Limit")  
rsiLower = input.int(5, title="RSI Lower Limit")

// RSI Timeframe
rsi_tf_value = request.security(syminfo.tickerid, rsi_tf, ta.rsi(close, rsiLength), lookahead=barmerge.lookahead_off, gaps=barmerge.gaps_off)

// Supertrend Timeframe
supertrend_tf2 = request.security(syminfo.tickerid, tf2, supertrend(factor, atrPeriod), lookahead=barmerge.lookahead_off, gaps=barmerge.gaps_off)

// Take Profit Settings (Percentage in relation to the average price)
takeProfitPercent = input.float(30, title="Take Profit", step=0.1) / 100

// Entry conditions based on price crossover with Supertrend Timeframe
longCondition = ta.crossover(close, supertrend_tf2) and barstate.isconfirmed
shortCondition = ta.crossunder(close, supertrend_tf2) and barstate.isconfirmed

// Execution of reversal
```