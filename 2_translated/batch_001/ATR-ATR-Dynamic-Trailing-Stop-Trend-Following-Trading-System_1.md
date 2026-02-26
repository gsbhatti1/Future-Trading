#### Overview
This strategy is a trend following system based on ATR (Average True Range) dynamic trailing stop. It combines EMA as a trend filter and controls signal generation through adjustable sensitivity parameters and an ATR period. The system supports both long and short trades with a comprehensive profit management mechanism.

#### Strategy Principle
1. Uses the ATR indicator to calculate price volatility, determining the trailing stop distance based on a set sensitivity coefficient (Key Value).
2. Utilizes EMA to judge market trend direction, opening long positions above EMA and short positions below EMA.
3. Triggers trading signals when the price breaks through the trailing stop line and aligns with the trend direction.
4. The system employs staged profit management:
   - At 20%-50% profit, raises the stop loss to breakeven.
   - At 50%-80% profit, takes partial profits and tightens the stop loss.
   - At 80%-100% profit, further tightens the stop loss to protect profits.
   - Above 100% profit, closes the entire position.

#### Strategy Advantages
1. The dynamic trailing stop effectively follows trends while preventing premature exits.
2. EMA trend filtering effectively reduces false breakout risks.
3. The staged profit mechanism ensures profitable realization while giving trends room to develop.
4. It supports both long and short trading, fully capturing market opportunities.
5. Strong parameter adjustability, adapting to different market environments.

#### Strategy Risks
1. May result in losses from frequent trading in ranging markets.
2. Potentially large drawdowns during trend reversal initiation.
3. Improper parameter settings may affect strategy performance.
Risk control suggestions:
- Recommended use in clear trending markets.
- Careful parameter selection through backtesting.
- Set maximum drawdown limits.
- Consider adding market condition filters.

#### Strategy Optimization Directions
1. Add a market environment recognition mechanism to use different parameters under different market conditions.
2. Introduce volume and other auxiliary indicators to enhance signal reliability.
3. Optimize the profit management mechanism with dynamic profit targets based on volatility.
4. Add time filters to avoid trading during unfavorable periods.
5. Consider adding volatility filters to reduce trading frequency during excessive volatility.

#### Summary
This is a well-structured trend following system with clear logic. Through the combination of ATR dynamic tracking and EMA trend filtering, it captures trends while maintaining good risk control. The staged profit mechanism design reflects mature trading thinking. The strategy has strong practicality and extensibility, with potential for better trading results through continuous optimization and improvement.

#### Source (PineScript)
```pinescript
//@version=5
strategy("Enhanced UT Bot with Long & Short Trades", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Input Parameters
keyvalue = input.float(1.1, title="Key Value (Sensitivity)", step=0.1)
atrperiod = input.int(200, title="ATR Period")
emaPeriod = input.int(50, title="EMA Period")
roi_close = input.float(100, title="Close Trade at ROI (%)", step=1)

// ATR Calculation
src = close
xATR = ta.atr(atrperiod)
nLoss = keyvalue * xATR

// EMA for Trend Filtering
ema = ta.ema(src, emaPeriod)

// Trailing Stop Logic
var float xATRTrailingStop = na
if na(xATRTrailingStop)
    xATRTrailingStop := src - nLoss

if src > nz(xATRTrailingStop[1]) and src[1] > nz(xATRTrailingStop[1])
    xATRTrailingStop := math.max(nz(xATRTrailingStop[1]), src - nLoss)
else if src < nz(xATRTrailingStop[1]) and src[1] < nz(xATRTrailingStop[1])
    xATRTrailingStop := math.min(nz(xATRTrailingStop[1]), src + nLoss)
else
    xATRTrailingStop := src > nz(xATRTrailingStop[1]) ? src - nLoss : src + nLoss

// Buy/Sell Signal with Trend Filter
buySignal = ta.crossover(src, xATRTrailingStop) and src > ema
sellSignal = ta.crossunder(src, xATRTrailingStop) and src < ema

// Strategy Logic: Long Trades
if buySignal and strategy.position_size <= 0
    strategy.entry("Buy", strategy.long)

if sellSignal and strategy.position_size > 0
    strategy.close("Buy")

// Strategy Logic: Short Trades
if sellSignal and strategy.position_size >= 0
    strategy.entry("Sell", strategy.short)

if buySignal and strategy.position_size < 0
    strategy.close("Sell")

// ROI Calculation for Both Long and Short Trades
var float entryPrice = na
var bool isLong = na
if strategy.position_size > 0
    entryPrice := strategy.opentrades.entry_price(0)
    isLong := true
if strategy