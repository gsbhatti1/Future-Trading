#### Overview  
The RSI Dual-Pivot Divergence Quantification Strategy is an advanced trading methodology that identifies potential reversal opportunities by detecting regular bullish and bearish divergences between price action and the Relative Strength Index (RSI). This strategy employs an automated pivot detection algorithm combined with two distinct stop-loss/take-profit management approaches to automatically establish positions when divergence signals are confirmed. The core innovation lies in its precise mathematical validation of price-RSI divergence phenomena and dynamic risk management mechanisms that ensure each trade adheres to predetermined risk-reward ratios.

#### Strategy Logic  
1. RSI Calculation Module: Utilizes Wilder's smoothing method to compute 14-period (adjustable) RSI values with close price as default input (configurable).  
2. Pivot Detection:  
   - Employs sliding windows of 5 periods (adjustable) on both sides to identify local RSI highs and lows  
   - Uses `ta.barssince` function to ensure 5-60 bar intervals (adjustable range) between pivots  
3. Divergence Confirmation:  
   - Bullish divergence: Price makes lower low while RSI forms higher low  
   - Bearish divergence: Price makes higher high while RSI forms lower high  
4. Trade Execution System:  
   - Dual-mode stop-loss: Based on recent 20-period (adjustable) swing points or ATR volatility  
   - Dynamic take-profit: Calculated as risk amount multiplied by preset reward-risk ratio (default 2:1)  
5. Visualization System: Marks all valid divergence signals on chart and displays real-time stop-loss (red) and take-profit (green) levels for open positions.

#### Advantages  
1. Multi-dimensional Validation: Requires both price and RSI to meet specific patterns within preset time ranges, significantly reducing false signals.  
2. Adaptive Risk Management:  
   - Swing mode suits trending markets for capturing wave movements  
   - ATR mode adapts to ranging markets with volatility-based stops  
3. High Customizability: All critical parameters (RSI period, pivot range, risk-reward ratio etc.) adjustable for market conditions.  
4. Scientific Position Sizing: Default 10% capital allocation prevents overexposure in single trades.  
5. Visual Feedback: Real-time chart markings and dynamic stop/take-profit lines provide intuitive decision support.

#### Risks  
1. Lag Risk: RSI as a lagging indicator may generate delayed signals during strong trends. Mitigation: Add trend filters or shorten RSI period.  
2. Whipsaw Risk: May produce consecutive false signals in choppy markets. Mitigation: Use ATR mode with higher multipliers or add volatility filters.  
3. Overfitting Risk: Parameter sets may perform well historically but fail live. Mitigation: Conduct multi-period multi-asset stress tests.  
4. Gap Risk: Price gaps may bypass stops. Mitigation: Avoid trading around major economic events or use options hedging.  
5. Timeframe Dependency: Performance varies across timeframes. Mitigation: Thorough backtesting on target timeframe.

#### Optimization Directions  
1. Composite Verification: Add MACD or volume indicators for secondary confirmation.  
2. Dynamic Parameters: Auto-adjust RSI period and ATR multiplier based on market volatility.  
3. Machine Learning: Apply genetic algorithms to optimize parameter combinations.  
4. Multi-Timeframe Analysis: Incorporate higher timeframe trend filters.  
5. Dynamic Position Sizing: Adjust trade size based on volatility for risk parity.  
6. Event Filters: Integrate economic calendar data to avoid trading around major news events.

#### Conclusion  
The RSI Dual-Pivot Divergence Quantification Strategy provides a structured approach to reversal trading through systematic divergence identification and rigorous risk management. Its core value lies in transforming traditional technical analysis concepts into quantifiable trading rules with dual-mode stop mechanisms adaptable to varying market conditions. Strategy excellence requires three key elements: appropriate parameter optimization, strict risk control, and consistent execution discipline. This strategy is particularly suitable for markets with moderate volatility but non-extreme trends, making it an excellent template for intermediate traders transitioning towards quantitative trading.