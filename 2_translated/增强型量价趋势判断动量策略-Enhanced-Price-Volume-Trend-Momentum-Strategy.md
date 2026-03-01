> Name

Enhanced-Price-Volume-Trend-Momentum-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/e02be2412bcfe8378d.png)

[trans]
#### Overview
This strategy is a trading system based on the MACD indicator and price-volume relationship, which identifies market trend reversal points by observing changes in MACD histogram patterns. The strategy employs a dynamic profit-taking and stop-loss mechanism using the ATR indicator to adapt to market volatility and effectively control risk.

#### Strategy Principle
The core logic of the strategy is built on the color changes of the MACD histogram, combined with dual EMA and SMA moving average systems. When the MACD histogram transitions from dark to light color, it indicates a momentum shift, triggering the system to execute trades. Specifically:
1. Calculate MACD values using fast(12) and slow(26) moving averages
2. Smooth MACD with a 9-period signal line
3. Monitor color depth changes in MACD histogram
4. Set dynamic profit targets and stop losses using 14-period ATR

#### Strategy Advantages
1. Scientific combination of indicators, with MACD effectively capturing trends and ATR adapting to volatility
2. Flexible profit-taking and stop-loss settings adjustable through multiplier parameters for different market characteristics
3. Clear trading signals with intuitive entry timing based on histogram color changes
4. Accommodates both long and short trading, increasing strategy versatility and profit opportunities

#### Strategy Risks
1. MACD as a lagging indicator may miss optimal entry points in rapid market movements
2. May generate false signals in ranging markets, leading to frequent trading
3. Improper ATR multiplier settings can result in stops being too loose or too tight
4. Requires proper money management to avoid excessive single-trade losses

#### Strategy Optimization Directions
1. Incorporate volume confirmation signals to improve signal reliability
2. Add trend filters to reduce false signals in ranging markets
3. Optimize profit-taking and stop-loss multipliers with dynamic adjustment based on different timeframes
4. Include volatility filtering to reduce trading frequency during highly volatile periods
5. Consider implementing time filters to avoid trading during unfavorable periods

#### Summary
This is a comprehensive strategy combining classic technical analysis indicator MACD with modern risk control methods. It captures market momentum shifts by observing MACD histogram pattern changes while using ATR for dynamic risk control. The strategy is well-designed with clear operational logic and practical value. Through continuous optimization and improvement, this strategy shows promise for better performance in real trading conditions.

#### Source (PineScript)

```pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2025-01-08 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT","balance":49999}]
*/

//@version=5
strategy(title="Enhanced MACD with Hollow Volume Insufficiency Strategy", shorttitle="Enhanced MACD with Hollow Volume Insufficiency Strategy", overlay=true)

//=== 1) Parameters ===//
fast_length   = input.int(title="Fast Length",        defval=12)
slow_length   = input.int(title="Slow Length",        defval=26)
src           = input.source(title="MACD Source",     defval=close)
signal_length = input.int(title="Signal Smoothing",   defval=9,  minval=1, maxval=50)
sma_source    = input.string(title="Oscillator MA Type", defval="EMA", options=["SMA","EMA"])
sma_signal    = input.string(title="Signal MA Type",     defval="EMA", options=["SMA","EMA"])

// Enable Long / Short
useLong       = input.bool(title="Enable Long Position? (Red at the Bottom)", defval=true)
useShort      = input.bool(title="Enable Short Position? (Green at the Top)", defval=true)

// Profit-taking ATR multiple (1~10x ATR)
tpATRmult     = input.int(title="Profit-taking ATR Multiple (1~10)", defval=10, minval=1, maxval=500)
// Stop-loss ATR multiple (1~10x ATR)
slATRmult     = input.int(title="Stop-loss ATR Multiple (1~10)", defval=3, minval=1, maxval=500)

//=== 2) MACD Calculation ===//
fast_ma  = sma_source == "SMA" ? ta.sma(src, fast_length) : ta.ema(src, fast_length)
slow_ma  = sma_source == "SMA" ? ta.sma(src, slow_length) : ta.ema(src, slow_length)
macd     = fast_ma - slow_ma
signal   = sma_signal == "SMA" ? ta.sma(macd, signal_length) : ta.ema(macd, signal_length)
hist     = macd - signal

//=== 3) Determine Dark/Light (Used for change signals) ===//
darkGreen  = hist >= 0 and hist <= hist[1]   // Above, bar shrinks or remains the same
lightGreen = hist >= 0 and hist >  hist[1]   // Above, bar increases in size
darkRed    = hist <  0 and hist <= hist[1]   // Below, absolute value of bar increases or remains the same
lightRed   = hist <  0 and hist >  hist[1]   // Below, absolute value of bar decreases

// Did a 'Dark to Light' change happen in the previous candle?
colorChangeToLightGreen = darkGreen[1] and lightGreen
colorChangeToLightRed   = darkRed[1]   and lightRed

//=== 4) ATR Calculation (Used for profit-taking and stop-loss) ===//
atrPeriod  = 14
atrValue   = ta.atr(atrPeriod)

//=== 5) Long Position Strategy: Dark Red → Light Red (Red at the Bottom) ===//
if useLong and colorChangeToLightRed
    // Set long stop loss based on current low - ATR multiple
    longStopLoss   = low - (slATRmult * atrValue)
    // Set long take profit based on current close + ATR multiple
    longTakeProfit = close + (tpATRmult * atrValue)

    // Enter long position
    strategy.entry("Long Entry", strategy.long, comment="Long")
    strategy.exit("Close Long", "Long", limit=longTakeProfit, stop=longStopLoss)
```

[/trans]