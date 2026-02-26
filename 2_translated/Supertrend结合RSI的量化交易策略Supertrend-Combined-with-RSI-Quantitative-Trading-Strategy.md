> Name

Supertrend combined with RSI Quantitative Trading Strategy [Alose]

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/823226b94aea93a628.png)
[trans]
### Overview

The strategy is named "Dual-drive Strategy." The main idea of this strategy is to combine Supertrend and RSI, two powerful technical indicators, to fully leverage their respective strengths for better quantitative trading performance.

### Strategy Logic

The core of the strategy uses the `Change` function to determine the direction change of the Supertrend indicator, thereby generating trading signals. A buy signal is generated when Supertrend changes from up to down, and a sell signal is generated when Supertrend turns from down to up.

At the same time, the RSI indicator is introduced to help determine when to close positions. When the RSI breaks through the set overbought line, long positions will be closed; when the RSI breaks through the set oversold line, short positions will be closed. This way, the RSI helps determine reasonable stop loss points to lock in profits.

### Advantage Analysis

The major advantages of this strategy are:

1. Supertrend is good at identifying market trend changes for precise long and short entries.
2. RSI excels at locating overextended turning points to assist with profit taking and stop losses.
3. The two indicators complement each other, making it easier to capture trading opportunities and achieve more stable gains.
4. The strategy logic is simple and straightforward, easy to understand and track for investors of varying skill levels.
5. Robust implementation with controlled drawdowns and stable profitability.

### Risk Analysis

Despite its merits, the Dual-drive Strategy still has some risks that need attention:

1. Wrong signals may occur with Supertrend and RSI leading to unnecessary losses. Parameters can be tuned or additional indicators introduced for verification.
2. Two-way trading carries higher risks, requiring stricter money management rules and risk control.
3. Stop loss may fail during abnormal price swings; backups should be used to manage risks.
4. Supertrend is sensitive to parameters and requires adjustments for different markets.

### Optimization Directions

Considering the risks, optimizations can be made in the following aspects:

1. Adding Volume and MACD indicators for additional signal filtering to achieve more accurate entries.
2. Setting up dynamic stop loss mechanisms to react to risk events.
3. Optimizing Supertrend and RSI parameters to better fit different markets.
4. Introducing machine learning algorithms to assist with parameter selection and indicator performance evaluation.
5. Using derivatives like futures and options for hedging risks.
6. Varying position sizing rules to limit losses and maximum drawdowns.

### Summary

The Dual-drive Strategy effectively combines Supertrend and RSI for efficient trend capturing and profit taking. Compared to single-indicator strategies, it provides more reliable signals, smaller drawdowns, and stable algorithmic trading performance. Further optimizations on parameter tuning, signal filtering, and risk management will lead to even better results.

||

### Overview

The strategy is named "Dual-drive Strategy." The main idea of this strategy is to combine Supertrend and RSI, which are two powerful technical indicators, in order to give full play to their respective advantages for achieving excellent quantitative trading performance.

### Strategy Logic

The core of the strategy uses the `Change` function to determine the direction change of the Supertrend indicator, thereby generating trading signals. A buy signal is generated when Supertrend changes from up to down, and a sell signal is generated when Supertrend turns from down to up.

At the same time, the RSI indicator is introduced to help determine when to close positions. When the RSI breaks through the set overbought line, long positions will be closed; when the RSI breaks through the set oversold line, short positions will be closed. This way, the RSI helps determine reasonable stop loss points to lock in profits.

### Advantage Analysis

The major advantages of this strategy are:

1. Supertrend is good at identifying market trend changes for precise long and short entries.
2. RSI excels at locating overextended turning points to assist with profit taking and stop losses.
3. The two indicators complement each other, making it easier to capture trading opportunities and achieve more stable gains.
4. The strategy logic is simple and straightforward, easy to understand and track for investors of varying skill levels.
5. Robust implementation with controlled drawdowns and stable profitability.

### Risk Analysis

Despite its merits, the Dual-drive Strategy still has some risks that need attention:

1. Wrong signals may occur with Supertrend and RSI leading to unnecessary losses. Parameters can be tuned or additional indicators introduced for verification.
2. Two-way trading carries higher risks, requiring stricter money management rules and risk control.
3. Stop loss may fail during abnormal price swings; backups should be used to manage risks.
4. Supertrend is sensitive to parameters and requires adjustments for different markets.

### Optimization Directions

Considering the risks, optimizations can be made in the following aspects:

1. Adding Volume and MACD indicators for additional signal filtering to achieve more accurate entries.
2. Setting up dynamic stop loss mechanisms to react to risk events.
3. Optimizing Supertrend and RSI parameters to better fit different markets.
4. Introducing machine learning algorithms to assist with parameter selection and indicator performance evaluation.
5. Using derivatives like futures and options for hedging risks.
6. Varying position sizing rules to limit losses and maximum drawdowns.

### Summary

The Dual-drive Strategy effectively combines Supertrend and RSI for efficient trend capturing and profit taking. Compared to single-indicator strategies, it provides more reliable signals, smaller drawdowns, and stable algorithmic trading performance. Further optimizations on parameter tuning, signal filtering, and risk management will lead to even better results.

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 10 | (Supertrend) ATR Length |
| v_input_float_1 | 3 | Factor |
| v_input_2_close | 0 | (RSI) Source: close/high/low/open/hl2/hlc3/hlcc4/ohlc4 |
| v_input_int_1 | 14 | Length |
| v_input_bool_1 | true | (Strategy) Long entries |
| v_input_bool_2 | false | Short entries |
| v_input_int_2 | 72 | Exit Long |
| v_input_int_3 | 28 | Exit Short |

### Source (PineScript)

```pinescript
/* backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © alorse

//@version=5
strategy("Supertrend + RSI Strategy [Alose]", overlay=true )

stGroup = 'Supertrend'
atrPeriod = input(10, "ATR Length", group=stGroup)
factor = input.float(3.0, "Factor", step = 0.01, group=stGroup)

[_, direction] = ta.supertrend(factor, atrPeriod)

// RSI
rsiGroup = 'RSI'
src = input(title='Source', defval=close, group=rsiGroup)
lenRSI = input.int(14, title='Length', minval=1, group=rsiGroup)
RSI = ta.rsi(src, lenRSI)

// Strategy Conditions
stratGroup = 'Strategy'
showLong = input.bool(true, title='Long entries', group=stratGroup)
showShort = input.bool(false, title='Short entries', group=stratGroup)
RSIoverbought = input.int(72, title='Exit Long', minval=1, group=stratGroup, tooltip='The trade will close when the RSI crosses up this point.')
RSIoversold = input.int(28, title='Exit Short', minval=1, group=stratGroup, tooltip='The trade will close when the RSI crosses below this point.')

// Entry and Exit Logic
longCondition = direction < 0 and showLong
shortCondition = direction > 0 and showShort

if (longCondition)
    strategy.entry("Buy", strategy.long)

if (shortCondition)
    strategy.entry("Sell", strategy.short)

if (RSI > RSIoverbought)
    if (position.size > 0)
        strategy.close("Buy")

if (RSI < RSIoversold)
    if (position.size < 0)
        strategy.close("Sell")
```

This script defines the Dual-drive Strategy combining Supertrend and RSI to achieve better trading performance.