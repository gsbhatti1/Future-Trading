> Name

Supertrend Combined with RSI Quantitative Trading Strategy [Supertrend-Combined-with-RSI-Quantitative-Trading-Strategy]

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/823226b94aea93a628.png)
[trans]
### Overview

This strategy is named the "Dual-drive Strategy." The main idea behind it is to combine Supertrend and RSI, two powerful technical indicators, to leverage their respective strengths and achieve superior quantitative trading performance.

### Strategy Logic  

The core of this strategy uses the `Change` function to determine the direction change of the Supertrend indicator in order to generate trading signals. A buy signal is generated when the Supertrend changes from up to down, and a sell signal is generated when Supertrend turns from down to up.

Additionally, the RSI indicator is introduced to assist in determining when positions should be closed. Long positions are closed when the RSI breaks through the set overbought line, and short positions are closed when the RSI breaches the set oversold line. This way, the RSI helps determine reasonable stop loss points to lock in profits.

### Advantage Analysis  

The major advantages of this strategy include:

1. Supertrend excels at identifying market trend changes for precise long and short entries.
2. RSI is adept at pinpointing overextended turning points to assist with reasonable profit-taking and stop-loss determination.
3. The complementary strengths of the two indicators enable better opportunity capture and more stable gains.
4. The strategy logic is straightforward and easy to understand, making it accessible even for less experienced investors.
5. Robust implementation with controlled drawdowns and stable profitability.

### Risk Analysis  

Despite its merits, there are some risks associated with the Dual-drive Strategy:

1. Incorrect signals from Supertrend or RSI can lead to unnecessary losses; parameters should be fine-tuned or additional indicators used for verification.
2. Two-way trading poses higher risks, requiring stricter money management and risk control protocols.
3. Stop loss mechanisms may fail during abnormal price swings; backup strategies are needed to manage risks.
4. Supertrend is sensitive to parameter changes, necessitating adjustments for different markets.

### Optimization Directions  

To address these risks, the strategy can be optimized in several ways:

1. Incorporating Volume and MACD indicators to filter false signals and achieve more accurate entry points.
2. Setting up dynamic stop losses to react to market anomalies.
3. Optimizing Supertrend and RSI parameters for better fit with different markets.
4. Introducing machine learning algorithms to assist in indicator effectiveness and parameter selection.
5. Using derivatives like futures or options for hedging risks.
6. Varying position sizing rules to limit single trade losses and maximum drawdowns.

### Summary  

The Dual-drive Strategy effectively combines Supertrend and RSI for efficient trend identification and profit-taking. Compared to strategies relying on a single indicator, this strategy provides more reliable signals and controlled drawdowns, making it an implementable and stable algorithmic trading approach. Further optimizations in parameter tuning, signal filtering, and risk management could lead to even better performance.

||

### Overview  

The strategy is named “Dual-drive Strategy.” The main idea behind it is to integrate Supertrend and RSI, two powerful technical indicators, leveraging their respective strengths to achieve superior quantitative trading outcomes.

### Strategy Logic  

The core of the strategy employs the `Change` function to detect changes in the direction of the Supertrend indicator for generating trading signals. A buy signal is triggered when Supertrend transitions from an upward trend to a downward one; conversely, a sell signal is generated when Supertrend shifts from a downward to an upward trend.

Additionally, the RSI indicator is incorporated to assist in determining appropriate exit points. Long positions are liquidated when the RSI breaches the overbought threshold, while short positions are closed when the RSI falls below the oversold level. This approach ensures that RSI aids in setting realistic stop-loss levels for locking in profits.

### Advantage Analysis  

The primary strengths of this strategy include:

1. Supertrend is adept at identifying market trend shifts to achieve precise entry and exit points.
2. RSI excels at pinpointing overbought or oversold conditions, aiding in strategic profit-taking and risk management.
3. The combination of both indicators enhances the potential for capturing market opportunities while maintaining stability.
4. The straightforward logic ensures easy understanding and tracking, making it suitable for investors of varying experience levels.
5. Robust implementation with controlled drawdowns guarantees stable returns.

### Risk Analysis  

While this strategy offers significant advantages, certain risks must be considered:

1. Incorrect signals from Supertrend or RSI can result in unnecessary losses; parameter adjustments or additional indicators may mitigate these risks.
2. The dual-nature of the trading approach increases risk exposure, necessitating strict money management and risk control measures.
3. Abnormal market fluctuations may bypass stop-loss mechanisms; backup strategies are essential to manage such risks.
4. Supertrend’s sensitivity to parameters requires market-specific adjustments.

### Optimization Directions  

To mitigate these risks, the following optimizations can be implemented:

1. Incorporating Volume and MACD indicators for enhanced signal filtering and precise entry points.
2. Setting up dynamic stop losses to react to unusual market conditions.
3. Optimizing Supertrend and RSI parameters for better fit with various markets.
4. Utilizing machine learning algorithms to enhance indicator performance and parameter selection.
5. Employing derivatives such as futures or options for risk hedging purposes.
6. Varying position sizing strategies to limit single trade losses and overall drawdowns.

### Summary  

The Dual-drive Strategy effectively combines the strengths of Supertrend and RSI to achieve efficient trend identification and profit-taking. Compared to single-indicator approaches, this strategy offers more reliable signals and controlled risk exposure, making it a practical and profitable algorithmic trading approach. Further refinements in parameter tuning, signal filtering, and risk management could significantly enhance its performance.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|10|(?Supertrend)ATR Length|
|v_input_float_1|3|Factor|
|v_input_2_close|0|(?RSI)Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|14|Length|
|v_input_bool_1|true|(?Strategy)Long entries|
|v_input_bool_2|false|Short entries|
|v_input_int_2|72|Exit Long|
|v_input_int_3|28|Exit Short|


> Source (PineScript)

``` pinescript
/*backtest
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
RSIoversold = input.int(28, title='Exit Short', minval=1, group=stratGroup, tooltip='The trade will close when the RSI crosses below this p