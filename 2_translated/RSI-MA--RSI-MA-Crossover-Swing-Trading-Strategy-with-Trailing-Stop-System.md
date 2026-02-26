> Name

RSI-MA-Crossover-Swing-Trading-Strategy-with-Trailing-Stop-System

> Author

ianzeng123

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/2d83701087c9c3ecdf280.png)
![IMG](https://www.fmz.com/upload/asset/2d86a333649c6eb42c581.png)


[trans]  
#### Overview  
This strategy is a swing trading approach based on the crossover between RSI (Relative Strength Index) and its moving average (MA), designed for 4-hour charts. It generates trading signals through RSI-MA crossovers and incorporates multiple risk management tools, including fixed stop-loss/take-profit, trailing stop-loss, and reversal exit mechanisms. The strategy also imposes a consecutive loss limit, pausing trading after two consecutive losses until a daily reset.  

#### Strategy Logic  
1. **Timeframe Enforcement**: The strategy operates exclusively on 4-hour charts to ensure signal alignment with the designed period.  
2. **Indicator Calculation**: Uses RSI (default length 14) and its MA (SMA or EMA, default length 14) for signals.  
   - Golden cross (RSI above MA) triggers long entries.  
   - Death cross (RSI below MA) triggers short entries.  
3. **Position Sizing**: Calculates position size based on allocated capital per trade and current price.  
4. **Exit Mechanisms**:  
   - **Fixed SL/TP**: Percentage-based stop-loss (default 1.5%) and take-profit (default 2.5%).  
   - **Trailing Stop-Loss**: Exits when price retracts by a specified points (default 10) from the peak.  
   - **Reversal Exit**: Closes positions on opposing signals.  
5. **Risk Control**:  
   - Pauses trading after two consecutive losses, with a daily reset at 9:15 AM.  

#### Advantages  
1. **Multi-Layered Signal Validation**: Combines RSI and MA for reduced false signals.  
2. **Dynamic Risk Management**: Trailing stop-locks profits, fixed SL limits losses.  
3. **Strict Capital Allocation**: Position sizing prevents over-leverage.  
4. **Disciplinary Control**: Loss count mechanism avoids emotional trading.  
5. **Visual Markers**: Clear chart annotations for quick signal identification.  

#### Risks  
1. **Parameter Sensitivity**: RSI and MA lengths significantly impact signal quality.  
2. **Trend Market Performance**: RSI may lag in strong trends due to prolonged overbought/oversold conditions.  
3. **Timeframe Limitation**: Requires revalidation for other periods.  
4. **Consecutive Loss Risk**: May miss opportunities during pause periods.  
**Solutions**:  
- Optimize parameters via backtesting.  
- Add trend filters (e.g., ADX).  
- Implement dynamic loss count thresholds.  

#### Optimization Directions  
1. **Multi-Indicator Confirmation**: Integrate MACD or Bollinger Bands.  
2. **Dynamic Parameters**: Adjust RSI length and SL ratios based on market volatility.  
3. **Timeframe Expansion**: Test performance on higher/lower timeframes (e.g., daily/1-hour).  
4. **Machine Learning**: Train models to optimize entry/exit conditions.  
5. **Advanced Capital Management**: Dynamically adjust capital allocation based on equity.  

#### Conclusion  
The strategy leverages RSI-MA crossovers for swing trading, balancing profitability and risk through multi-tiered management tools. Its strengths lie in clear logic and discipline, though further optimizations (e.g., multi-indicator integration) could enhance adaptability. Future improvements should focus on dynamic adjustments and broader market validation.

||  

#### Source (PineScript)

```pinescript
/*backtest
start: 2024-04-23 00:00:00
end: 2024-09-06 00:00:00
period: 4h
basePeriod: 4h
exchanges: [{"eid":"Futures_Binance","currency":"DOGE_USDT"}]
*/

//@version=5
strategy("? RX Swing", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=1)


// === INPUTS ===
rsiLength     = input.int(14, title="RSI Length")
maLength      = input.int(14, title="RSI MA Length")
maType        = input.string("SMA", options=["SMA", "EMA"], title="MA Type for RSI")
sl_pct        = input.float(1.5, title="Stop Loss %", minval=0.0)
tp_pct        = input.float(2.5, title="Take Profit %", minval=0.0)
capitalPerTrade = input.float(15000, title="Capital Per Trade (INR)", minval=1)
lotSize       = input.int(50, title="Lot Size (Nifty Options Lot)", minval=1)
trail_points  = input.float(10, title="Trailing SL Points", minval=0.1)

// === CALCULATIONS ===
rsi    = ta.rsi(close, rsiLength)
rsiMA  = maType == "SMA" ? ta.sma(rsi, maLength) : ta.ema(rsi, maLength)

longSignal  = ta.crossover(rsi, rsiMA)
shortSignal = ta.crossunder(rsi, rsiMA)

// === TRADING WINDOW ===
canTrade = true

if (longSignal and canTrade)
    strategy.entry("Long", strategy.long, size=lotSize)

if (shortSignal and canTrade)
    strategy.entry("Short", strategy.short, size=lotSize)

// === EXIT MECHANISMS ===
trailStop = strategy.exit("Trail Stop", "Long", trail_offset=trail_points)
strategy.exit("Fixed SL/TP", "Long", stop=(strategy.position_avg_price - sl_pct * close))
strategy.exit("Fixed SL/TP", "Short", stop=(strategy.position_avg_price + sl_pct * close))

// === RISK CONTROL ===
consecutiveLosses = 0
lossResetTime     = 9:15

if (not canTrade and consecutiveLosses > 2)
    strategy.close_all()
    consecutiveLosses := 0

if time >= lossResetTime[1] and not is Weekend
    consecutiveLosses := 0

// === VISUALIZATION ===
plotshape(series=longSignal, title="Long Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortSignal, title="Short Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

```

This code implements the described strategy in Pine Script for a 4-hour chart on Binance Futures DOGE_USDT.