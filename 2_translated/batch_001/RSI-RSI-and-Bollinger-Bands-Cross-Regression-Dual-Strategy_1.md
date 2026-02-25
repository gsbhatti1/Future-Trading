> Name

RSI with Bollinger Bands Cross-Regression Dual Strategy - RSI-and-Bollinger-Bands-Cross-Regression-Dual-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1835fb0142a655c96fc.png)

[trans]
#### Overview
This strategy is a dual technical analysis trading system based on the Relative Strength Index (RSI) and Bollinger Bands. By combining RSI's overbought/oversold signals with Bollinger Bands' price channel breakout signals, it constructs a complete trading decision framework. This strategy is particularly suitable for markets with high volatility, achieving risk-controlled trading through strict entry and exit conditions.

#### Strategy Principle
The core logic of the strategy is built on the synergy of two main technical indicators:
1. RSI uses a 6-period calculation cycle with 50 as the overbought/oversold threshold.
2. Bollinger Bands use a 200-period moving average as the middle band with a standard deviation multiplier of 2.0, forming upper and lower tracks.
3. Long condition: Triggered when RSI breaks above the oversold level (50) while price breaks above the lower Bollinger Band.
4. Short condition: Triggered when RSI breaks below the overbought level (50) while price breaks below the upper Bollinger Band.
5. The strategy employs OCA (One-Cancels-All) order management to ensure only one active trade at a time.

#### Strategy Advantages
1. Dual confirmation mechanism: Reduces false signals through RSI and Bollinger Bands confirmation.
2. Robust risk control using Bollinger Bands as stop-loss levels.
3. Strong adaptability with Bollinger Bands automatically adjusting to market volatility.
4. Optimized order management through OCA mechanism improves capital efficiency.
5. High parameter adaptability allows optimization for different market characteristics.

#### Strategy Risks
1. Sideways market risk: Frequent false breakouts in range-bound markets.
2. Lag risk: Some inherent delay due to moving average calculations.
3. Parameter sensitivity: Strategy performance heavily depends on RSI and Bollinger Bands parameters.
4. Market environment dependence: Better performance in trending markets, potential underperformance in ranging markets.

#### Optimization Directions
1. Dynamic parameter adjustment: Adapt RSI thresholds based on market volatility.
2. Market environment filtering: Add trend indicators for different parameter sets in various market conditions.
3. Take-profit optimization: Implement dynamic ATR-based take-profit mechanisms.
4. Position management optimization: Adjust position size based on signal strength and market volatility.
5. Time filtering: Add trading time window restrictions to avoid unfavorable periods.

#### Summary
This strategy constructs a relatively complete trading system through the synergy of RSI and Bollinger Bands. Its main advantages lie in the dual confirmation mechanism and comprehensive risk control, while attention must be paid to market environment impacts. The proposed optimization directions can further enhance strategy stability and profitability.[/trans]

#### Source (PineScript)

```pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-28 00:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI with Bollinger Bands Dual Strategy (by ChartArt) v2.2", shorttitle="CA_RSI_BB_2.2", overlay=true)

// ChartArt's RSI + Bollinger Bands dual strategy - Simplified version
//
// Chinese Version 3, BY Henry
// Original idea by ChartArt, January 18, 2015
// Updated to Pine Script v5, removed background color, candlestick colors, and P&L drawing functions
//
// Strategy description:
// The strategy combines the use of RSI and Bollinger Bands.
// Sell when price is above upper band and RSI is overbought,
// Buy when price is below lower band and RSI is oversold.
//
// This strategy only triggers when both RSI and Bollinger Bands are
// in an overbought or oversold state.

// === Input parameters ===

// RSI parameters
RSIlength = input.int(6, title="RSI周期长度", minval=1) 
RSIoverSold = input.int(50, title="RSI超卖阈值", minval=0, maxval=100)
RSIoverBought = input.int(50, title="RSI超买阈值", minval=0, maxval=100)

// Bollinger Bands parameters
BBlength = input.int(200, title="布林带周期长度", minval=1)
BBmult = input.float(2.0, title="布林带标准差倍数", minval=0.001, maxval=50)

// === Calculations ===

price = close
vrsi = ta.rsi(price, RSIlength)

// Bollinger Bands calculation
BBbasis = ta.sma(price, BBlength)
BBdev = BBmult * ta.stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev

// === Plotting ===

plot(BBbasis, color=color.new(color.aqua, 0), title="布林带中线(SMA)")
p1 = plot(BBupper, color=color.new(color.silver, 0), title="布林带上轨")
p2 = plot(BBlower, color=color.new(color.silver, 0), title="布林带下轨")
fill(p1, p2, color=color.new(color.silver, 90))

// === Strategy logic ===

if (not na(vrsi))
    longCondition = ta.crossover(vrsi, RSIoverSold) and ta.crossover(price, BBlower)
    if (longCondition)
        strategy.entry("RSI_BB_做多", strategy.long, stop=BBlower, oca_name="RSI_BB", comment="RSI_BB_做多")
    else
        strategy.cancel("RSI_BB_做多")

    shortCondition = ta.crossunder(vrsi, RSIoverBought) and ta.crossunder(price, BBupper)
    if (shortCondition)
        strategy.entry("RSI_BB_做空", strategy.short, stop=BBupper, oca_name="RSI_BB", commen
```