### Overview

This is a trend-following strategy based on the QQE (Qualitative Quantitative Estimation) indicator and moving averages. It determines the trend direction and generates trading signals based on fast QQE crossovers filtered by the direction of moving averages.

The strategy can use three kinds of QQE crossovers to determine the trading signal:  
(1) Smooth RSI crossing 0 line; (2) Smooth RSI crossing fast QQE line; (3) Smooth RSI exiting the RSI threshold channel. By default, it uses the third crossover to open positions and the second crossover to close positions.

The buy and sell signals can choose to add an additional filter by moving averages: the close price should be above (below) the fast MA line, and the fast MA line should be above (below) the slow MA line, to generate a trading signal.

This strategy is suitable for use in automated trading with a signal-to-signal mode.

### Principle

The core indicator of this strategy is QQE. Its calculation formula is as follows:

```
Wilders_Period = RSILen * 2 - 1  

Rsi = rsi(close, RSILen)  
RSIndex = ema(Rsi, SF)  
AtrRsi = abs(RSIndex - RSIndex[1])  
MaAtrRsi = ema(AtrRsi, Wilders_Period)
DeltaFastAtrRsi = ema(MaAtrRsi, Wilders_Period) * QQEfactor

newshortband = RSIndex + DeltaFastAtrRsi 
newlongband = RSIndex - DeltaFastAtrRsi
```

Where `RSILen` is the length period of RSI, and `SF` is the RSI smoothing factor. QQE is essentially a smoothed RSI. It calculates an upper and lower channel based on a fast ATR. When the price crosses over these channels, it identifies buy or sell opportunities.

The strategy uses three kinds of QQE crossovers to identify trading signals:

1. **Smooth RSI crossing 0 line (XZ)**

```
QQEzlong = RSIndex >= 50 ? QQEzlong + 1 : 0
QQEzshort = RSIndex < 50 ? QQEzshort + 1 : 0  
```

2. **Smooth RSI crossing fast QQE line (XQ), similar to an early swing signal**

```
QQExlong = FastAtrRsiTL < RSIndex ? QQExlong + 1 : 0
QQExshort = FastAtrRsiTL > RSIndex ? QQExshort + 1 : 0
```

3. **Smooth RSI exiting the threshold channel (XC), similar to a confirmed swing signal**

```
threshold = 10 
QQEclong = RSIndex > (50 + threshold) ? QQEclong + 1 : 0
QQEcshort = RSIndex < (50 - threshold) ? QQEcshort + 1 : 0
```

One or multiple of the above three crossovers can be selected to identify buy/sell signals and close positions.

The buy and sell signals can choose to add an additional filter by moving averages:

```  
// Filter condition   
QQEflong = close > ma_medium AND  
            ma_medium > ma_slow AND
            ma_fast > ma_medium
            
QQEfshort = close < ma_medium AND  
            ma_medium < ma_slow AND  
            ma_fast < ma_medium   
```

This helps avoid false signals in sideways markets.

The strategy is suitable for automated trading by using different QQE crossovers for entries and exits:

```
Entry signal = XC OR XQ OR XZ
Exit signal = XQ OR XZ
```

### Advantages

The advantages of this strategy include:

1. Using the QQE indicator to determine trends and crossovers, which inherently smooths out noise, reducing false signals.
2. Adding a moving average filter can further reduce false signals in sideways markets, improving the quality of signals.
3. Different QQE crossovers can be chosen for entries and exits, enabling automated trading.
4. Smooth RSI indicators are lagging, so buy/sell signals will not redraw.
5. Optimization is possible across different time periods to find the best parameter combinations.

### Risks

The strategy also has certain risks:

1. False signals may occur during trend reversals; setting stop-losses can help manage risk.
2. Improper parameter settings can affect performance, necessitating multiple tests and optimizations to find optimal parameters.
3. Parameters for different assets and time periods need individual testing and optimization.
4. Automated trading poses the risk of drawdowns and consecutive losses, which require effective money management.

### Solutions

1. Set stop-losses to exit positions when losses reach a certain level.
2. Test various parameter combinations in detail to find the best settings.
3. Adjust parameters based on the characteristics of different assets and time periods.
4. Implement strict money management, using partial positions and controlling single position size.

### Optimization Directions

This strategy can be optimized from several directions:

1. Optimize QQE parameters, including RSI length, RSI smoothing length, fast ATR length, etc., to find the best parameter combinations.
2. Optimize moving average parameters by adjusting period, type, etc., to form the best match with QQE indicators.
3. Test different QQE crossovers for entries and exits to find the most stable combination.
4. Fine-tune parameters based on different assets and trading periods. Day trading can use shorter periods to increase frequency of parameter adjustments.
5. Add a stop-loss mechanism, exiting positions when losses reach a certain percentage.
6. Adjust position sizes appropriately and test different position management strategies.

### Summary

This strategy integrates QQE indicators for trend determination and crossover signals with moving averages as filters to generate trading signals. In practice, adjusting parameters can optimize signal quality, and strict money management can control risk. This strategy is suitable for use in automated trading with a signal-to-signal mode and can also assist discretionary traders. Parameter optimization and rule refinement can adapt the strategy to various market environments.