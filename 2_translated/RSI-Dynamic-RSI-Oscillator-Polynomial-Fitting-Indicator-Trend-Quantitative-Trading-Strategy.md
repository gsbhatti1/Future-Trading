> Name

Dynamic RSI Oscillator Polynomial Fitting Indicator Trend Quantitative Trading Strategy - Dynamic-RSI-Oscillator-Polynomial-Fitting-Indicator-Trend-Quantitative-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/113c46ea585baf8fb27.png)

[trans]
This is a quantitative trading system based on the RSI dynamic oscillator. By performing polynomial fitting and time series analysis on the RSI indicator, it calculates the rate of change of RSI to capture market momentum. The strategy uses advanced mathematical methods such as QR decomposition for signal processing and combines with moving average systems for trading decisions.

#### Strategy Principle
The core of the strategy is the Delta-RSI oscillator, which is implemented through the following steps:
1. First calculate traditional RSI indicator as basic data.
2. Use polynomial fitting to smooth RSI and reduce noise.
3. Calculate time derivative of RSI to get Delta-RSI, reflecting the rate of change of RSI.
4. Compare Delta-RSI with its moving average to generate trading signals.
5. Use root mean square error (RMSE) to evaluate and filter fitting quality.

Trading signals can be generated in three ways:
- Zero-line crossing: Long when Delta-RSI turns positive from negative, short when it turns negative from positive.
- Signal line crossing: Long/short when Delta-RSI crosses above/below its moving average.
- Direction change: Long when Delta-RSI starts rising in the negative territory, short when it starts falling in the positive territory.

#### Strategy Advantages
1. Solid mathematical foundation: Uses advanced mathematical methods like QR decomposition for signal processing.
2. Signal smoothing: Polynomial fitting can effectively filter market noise and improve signal quality.
3. High flexibility: Provides multiple signal generation methods and parameter choices to adapt to different market conditions.
4. Controllable risk: Includes RMSE filtering mechanism to screen out more reliable signals.
5. Computational efficiency: Matrix operations use optimized algorithms for high running efficiency.

#### Strategy Risks
1. Parameter sensitivity: Multiple key parameters need careful adjustment; poor parameter selection seriously affects strategy performance.
2. Lag: Signal smoothing introduces some delay, which may miss rapid market moves.
3. False breakouts: May generate false signals in oscillating markets, increasing trading costs.
4. Computational complexity: Involves many matrix operations, potentially causing performance bottlenecks in high-frequency trading.
5. Overfitting: Need to avoid overfitting historical data when optimizing parameters.

#### Strategy Optimization Directions
1. Adaptive parameters: Dynamically adjust RSI period and fitting order based on market volatility.
2. Multiple timeframes: Incorporate signals from more timeframes for cross-validation.
3. Volatility filtering: Add volatility indicators like ATR for signal filtering.
4. Market classification: Use different signal generation rules for different market states (trend/oscillation).
5. Stop-loss optimization: Add smarter stop-loss mechanisms, such as dynamic stops based on support/resistance levels.

#### Summary
This is a complete quantitative trading strategy with a solid theoretical foundation. Through analysis of RSI's dynamic characteristics combined with modern mathematical methods for signal processing, it can effectively capture market trends. While there are some issues with parameter sensitivity and computational complexity, the strategy has good practical value through proper parameter selection and optimization improvements. When applying to live trading, it is recommended to pay attention to risk control, set reasonable position sizes, and continuously monitor strategy performance.

> Source (PineScript)

```pinescript
/*backtest
start: 2024-11-10 00:00:00
end: 2024-12-09 08:00:00
period: 4h
basePeriod: 4h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © tbiktag
//
// Delta-RSI Oscillator Strategy
//
// A strategy that uses Delta-RSI Oscillator (© tbiktag) as a stand-alone indicator:
// https://www.tradingview.com/script/OXQVFTQD-Delta-RSI-Oscillator/
//
// Delta-RSI is a smoothed time derivative of the RSI, plotted as a histogram 
// and serving as a momentum indicator.
//
// Input parameters:
// RSI Length: The timeframe of the RSI that serves as an input to D-RSI.
// Length: The length of the lookback frame used for local regression.
// Polynomial Order: The order of the local polynomial function used to interpolate the RSI.
// Signal Length: The length of a EMA of the D-RSI series that is used as a signal line.
// Trade signals are generated based on three optional conditions:
// - Zero-crossing: bullish when D-RSI crosses