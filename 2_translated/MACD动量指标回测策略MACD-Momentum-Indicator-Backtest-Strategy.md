> Name

MACD-Momentum-Indicator-Backtest-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy combines the MACD momentum indicator with the RSI overbought/oversold indicator. When MACD crossovers occur, it checks if RSI also completed corresponding bottoming or topping reversals during a lookback period to generate more reliable trading signals. It follows typical short-term mean reversion strategy logic.

## Strategy Logic

1. Calculate MACD DIFF, DEA, and histogram. Crossover of DIFF above DEA gives a bullish crossover signal; crossover below gives a bearish crossover signal.
2. Calculate RSI to identify oversold bounces and overbought selloffs. A lookback window checks if recent bottoming or topping has occurred.
3. When MACD bullish crossover happens, if RSI has bounced off oversold within the lookback window, a long signal is generated. On MACD bearish crossover, a short signal is generated if RSI topped over the lookback window.
4. Set stop loss after entry to control risk.

## Advantages

1. MACD sensitively identifies trend changes while RSI effectively judges overbought/oversold levels.
2. Requiring both MACD and RSI signals filters out false signals.
3. The lookback window improves signal reliability.
4. Stop loss aids in risk management.

## Risks

1. Lag of MACD and RSI may cause missed optimal entries.
2. Lower probability of dual-indicator signals means fewer trades.
3. No consideration of larger trend direction risks being trapped.
4. Poor stop loss tuning may be too wide or too tight.

Possible Solutions:

1. Adjust MACD and RSI parameters to reduce lag.
2. Widen indicator threshold ranges to provide more signals.
3. Add trend filter to avoid counter-trend entries.
4. Test different stop loss parameters for optimal levels.

## Optimization Directions

1. Test SMA and other moving averages.
2. Add trailing stop loss for flexible stops.
3. Incorporate trend strength to judge entry quality.
4. Use machine learning to predict indicator movements.
5. Combine more factors to optimize entry timing.

## Summary

This strategy filters for reliable reversal signals using coordinated MACD and RSI. The logic is clear, and parameters are flexible for enhancements like indicator selection, trend filtering, stop loss techniques, etc., to acquire more trades while maintaining stability, but over-optimization risks need to be avoided.

---

## Overview 

This strategy combines the MACD momentum indicator with the RSI overbought/oversold indicator. When MACD crossovers occur, it checks if RSI also completed corresponding bottoming or topping reversals during a lookback period to generate more reliable trading signals. Typical short-term mean reversion strategy logic.

## Strategy Logic

1. Calculate MACD DIFF, DEA, and histogram. Crossover of DIFF above DEA gives a bullish crossover signal; crossover below gives a bearish crossover signal.
2. Calculate RSI to identify oversold bounces and overbought selloffs. A lookback window checks if recent bottoming or topping has occurred.
3. When MACD bullish crossover happens, if RSI has bounced off oversold within the lookback window, a long signal is generated. On MACD bearish crossover, a short signal is generated if RSI topped over the lookback window.
4. Set stop loss after entry to control risk.

## Advantages

1. MACD sensitively identifies trend changes while RSI effectively judges overbought/oversold levels.
2. Requiring both MACD and RSI signals filters out false signals.
3. The lookback window improves signal reliability.
4. Stop loss aids in risk management.

## Risks

1. Lag of MACD and RSI may cause missed optimal entries.
2. Lower probability of dual-indicator signals means fewer trades.
3. No consideration of larger trend direction risks being trapped.
4. Poor stop loss tuning may be too wide or too tight.

Possible Solutions:

1. Adjust MACD and RSI parameters to reduce lag.
2. Widen indicator threshold ranges to provide more signals.
3. Add trend filter to avoid counter-trend entries.
4. Test different stop loss parameters for optimal levels.

## Optimization Directions

1. Test SMA and other moving averages.
2. Add trailing stop loss for flexible stops.
3. Incorporate trend strength to judge entry quality.
4. Use machine learning to predict indicator movements.
5. Combine more factors to optimize entry timing.

## Summary

This strategy filters for reliable reversal signals using coordinated MACD and RSI. The logic is clear, and parameters are flexible for enhancements like indicator selection, trend filtering, stop loss techniques, etc., to acquire more trades while maintaining stability, but over-optimization risks need to be avoided.

---

```pinescript
/*backtest
start: 2023-08-24 00:00:00
end: 2023-09-23 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
//based on Range Strat - MACD/RSI 
strategy("MACD/RSI - edited", 
      overlay=true,
      default_qty_type=strategy.percent_of_equity,
      default_qty_value=10, precision=2, initial_capital=100000,
      pyramiding=2,
      commission_value=0.05)

//Backtest date range
StartDate = input(timestamp("13 Jun 2022"), title="Start Date")
EndDate = input(timestamp("13 Jun 2024"), title="End Date")
inDateRange = true

// RSI Input Settings
rsisrc = input(title="RSI Source", defval=close, group="RSI Settings")
length = input(title="Length", defval=14, group="RSI Settings" )
overSold = input(title="Over Sold Threshold", defval=30, group="RSI Settings" )
overBought = input(title="Over Bought Threshold", defval=70, group="RSI Settings" )
rsi_lookback = input(title="RSI cross lookback period", defval=7, group="RSI Settings")

// Calculating RSI
vrsi = ta.rsi(rsisrc, length)
co = ta.crossover(vrsi, overSold)
cu = ta.crossunder(vrsi, overBought)

// Function looking for a happened condition during lookback period
f_somethingHappened(_cond, _lookback) =>
    bool _crossed = false
    for i = 1 to _lookback
        if _cond[i]
            _crossed := true
    _crossed

coCheck = f_somethingHappened(co, rsi_lookback)
cuCheck = f_somethingHappened(cu, rsi_lookback)

// MACD Input Settings
macdsrc = input(title="MACD Source", defval=close, group="MACD Settings")
fast_length = input(title="Fast Length", defval=12, group="MACD Settings")
slow_length = input(title="Slow Length", defval=26, group="MACD Settings")
signal_length = input.int(title="Signal Smoothing",  minval = 1, maxval = 50, defval = 9, group="MACD Settings")
sma_source = input.string(title="Oscillator MA Type: EMA|SMA", defval="EMA", group="MACD Settings")
```