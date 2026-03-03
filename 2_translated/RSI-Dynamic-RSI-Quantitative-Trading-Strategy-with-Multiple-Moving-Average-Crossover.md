> Name

Dynamic-RSI-Quantitative-Trading-Strategy-with-Multiple-Moving-Average-Crossover

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fc341e6f1e099965a0.png)

#### Overview
This is a quantitative trading strategy that combines the Relative Strength Index (RSI) with multiple moving averages. The strategy primarily identifies market trends by monitoring crossover signals between different types of moving averages (including SMA, EMA, WMA, and SMMA) on the RSI indicator, while using RSI's overbought and oversold zones as supplementary decision criteria.

#### Strategy Principles
The strategy includes several key calculation steps:
1. Calculate 14-period RSI with an overbought level at 70 and an oversold level at 30.
2. Calculate three different moving averages on the RSI curve:
   - MA1: 20-period, choice of SMA/EMA/WMA/SMMA
   - MA2: 50-period, choice of SMA/EMA/WMA/SMMA  
   - MA3: 100-period, choice of SMA/EMA/WMA/SMMA
3. Trading signal generation rules:
   - Buy signal: When MA2 crosses above MA3.
   - Sell signal: When MA2 crosses below MA3.
4. Simultaneously detect RSI divergences for additional reference.

#### Strategy Advantages
1. Multiple technical indicator cross-validation improves signal reliability.
2. Flexible moving average types and parameters.
3. RSI divergence detection helps identify market turning points early.
4. Percentage-based position management for effective risk control.
5. Excellent visualization for analysis and backtesting.

#### Strategy Risks
1. Moving average crossovers may have lag effects.
2. False signals may occur in ranging markets.
3. RSI distortion under certain market conditions.
4. Improper parameter selection may lead to excessive or insufficient trading signals.

Risk mitigation:
- Recommend cross-validation with market trends and volume.
- Optimize trading frequency through moving average parameter adjustment.
- Set stop-loss and take-profit levels for risk control.

#### Strategy Optimization Directions
1. Signal filtering optimization:
   - Add trend confirmation indicators.
   - Incorporate volume analysis.
2. Parameter dynamic optimization:
   - Automatically adjust RSI and MA parameters based on market volatility.
   - Introduce adaptive period calculation methods.
3. Risk control optimization:
   - Develop dynamic stop-loss and take-profit mechanisms.
   - Design dynamic position management system.

#### Summary
The strategy builds an adaptive trading system by combining RSI and multiple moving averages. Its core advantages lie in the cross-validation of multiple technical indicators and flexible parameter configuration, while attention must be paid to moving average lag and market condition impacts on strategy performance. Through continuous optimization and risk control, this strategy shows promise for stable performance in actual trading.

||

#### Overview
This is a quantitative trading strategy that combines the Relative Strength Index (RSI) with multiple moving averages. The strategy primarily identifies market trends by monitoring crossover signals between different types of moving averages (including SMA, EMA, WMA, and SMMA) on the RSI indicator, while using RSI's overbought and oversold zones as supplementary decision criteria.

#### Strategy Principles
The strategy includes several key calculation steps:
1. Calculate 14-period RSI with an overbought level at 70 and an oversold level at 30.
2. Calculate three different moving averages on the RSI curve:
   - MA1: 20-period, choice of SMA/EMA/WMA/SMMA
   - MA2: 50-period, choice of SMA/EMA/WMA/SMMA  
   - MA3: 100-period, choice of SMA/EMA/WMA/SMMA
3. Trading signal generation rules:
   - Buy signal: When MA2 crosses above MA3.
   - Sell signal: When MA2 crosses below MA3.
4. Simultaneously detect RSI divergences for additional reference.

#### Strategy Advantages
1. Multiple technical indicator cross-validation improves signal reliability.
2. Flexible moving average types and parameters.
3. RSI divergence detection helps identify market turning points early.
4. Percentage-based position management for effective risk control.
5. Excellent visualization for analysis and backtesting.

#### Strategy Risks
1. Moving average crossovers may have lag effects.
2. False signals may occur in ranging markets.
3. RSI distortion under certain market conditions.
4. Improper parameter selection may lead to excessive or insufficient trading signals.

Risk mitigation:
- Recommend cross-validation with market trends and volume.
- Optimize trading frequency through moving average parameter adjustment.
- Set stop-loss and take-profit levels for risk control.

#### Strategy Optimization Directions
1. Signal filtering optimization:
   - Add trend confirmation indicators.
   - Incorporate volume analysis.
2. Parameter dynamic optimization:
   - Automatically adjust RSI and MA parameters based on market volatility.
   - Introduce adaptive period calculation methods.
3. Risk control optimization:
   - Develop dynamic stop-loss and take-profit mechanisms.
   - Design dynamic position management system.

#### Summary
The strategy builds an adaptive trading system by combining RSI and multiple moving averages. Its core advantages lie in the cross-validation of multiple technical indicators and flexible parameter configuration, while attention must be paid to moving average lag and market condition impacts on strategy performance. Through continuous optimization and risk control, this strategy shows promise for stable performance in actual trading.

||

```pinescript
//@version=6
strategy(title="Relative Strength Index with MA Strategy", shorttitle="RSI-MA Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=200)

// RSI Inputs
rsiLengthInput = input.int(14, minval=1, title="RSI Length", group="RSI Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")
calculateDivergence = input.bool(false, title="Calculate Divergence", group="RSI Settings", tooltip="Calculating divergences is needed in order for divergence alerts to fire.")

// RSI Calculation
change_rsi = ta.change(rsiSourceInput)
up = ta.rma(math.max(change_rsi, 0), rsiLengthInput)
down = ta.rma(-math.min(change_rsi, 0), rsiLengthInput)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))

// RSI Plot
plot(rsi, "RSI", color=#7E57C2)
hline(70, "RSI Upper Band", color=#787B86)
hline(50, "RSI Middle Band", color=color.new(#787B86, 50))
hline(30, "RSI Lower Band", color=#787B86)
fill(hline(70), hline(30), color=color.rgb(126, 87, 194, 90), title="RSI Background Fill")

// RSI-based MA Inputs
grpRSIMovingAverages = "RSI Moving Averages"
ma1Length = input.int(20, title="MA1 Length", group=grpRSIMovingAverages)
ma2Length = input.int(50, title="MA2 Length", group=grpRSIMovingAverages)
ma3Length = input.int(100, title="MA3 Length", group=grpRSIMovingAverages)
ma1Type = input.string("SMA", title="MA1 Type", options=["SMA", "EMA", "WMA", "SMMA"], group=grpRSIMovingAverages)
ma2Type = input.string("EMA", title="MA2 Type", options=["SMA", "EMA", "WMA", "SMMA"], group=grpRSIMovingAverages)
ma3Type = input.string("WMA", title="MA3 Type", options=["SMA", "EMA", "WMA", "SMMA"], group=grpRSIMovingAverages)

// MA Calculation Function
calcMA(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
```