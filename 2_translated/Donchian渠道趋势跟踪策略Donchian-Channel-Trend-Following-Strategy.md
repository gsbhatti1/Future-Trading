> Name

Donchian Channel Trend Following Strategy Donchian-Channel-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/9553e0221d1519141a.png)
 [trans]
## Overview

The Donchian Channel trend following strategy is a trend-following strategy based on the Donchian Channel indicator. It uses different lengths of Donchian Channels to identify price trends and generates trading signals when prices break out of these channels.

The main idea of this strategy is to use a long-term Donchian Channel to determine the major trend direction, and a short-term Donchian Channel as the signal for entry and stop loss. It aims to capture medium-to-long term price trends without being misled by short-term market fluctuations.

## Strategy Logic  

1. Calculate the highest closing price and lowest closing price over a long period (e.g., 50 days) to build the Donchian Channel. A breakout above the upper band indicates an uptrend, while a breakout below the lower band indicates a downtrend. This determines the major trend direction.

2. Use the highest closing price and lowest closing price over a short period (e.g., 20 days) as the criteria for entry and stop loss. When the price breaks out of the long-term channel, if the closing price also breaks the short-term channel, take a long or short position accordingly.

3. When holding a long position, if the price falls below the short-term lower band, exit at a loss. When holding a short position, if the price breaks above the short-term upper band, exit at a loss.

4. The stop-loss point is set at N times ATR. This automatically adjusts based on market volatility to reduce the likelihood of the stop-loss being triggered.

5. There is an option to close positions before the trading session ends or hold them until hit stop-loss. This is controlled by an input parameter.

The strategy considers both trend identification and profit stop loss, making it capable of capturing price trends while controlling risks. It is suitable for medium-to-long term operations.

## Advantage Analysis  

1. Effectively identifies medium-to-long term trends without being interfered by short-term market noises.

2. Automatic stop-loss mechanism limits per trade losses.

3. ATR-based stop-loss adjusts the stop distance based on market volatility, reducing the risk of the stop-loss being triggered.

4. Automatically closes positions when trading is not possible to manage risks.

5. Simple and clear strategy logic that is easy to understand.

## Risk Analysis  

1. In non-trending markets, the strategy may generate more trades, increasing trading costs and chances of loss.

2. Although having a stop-loss mechanism, price gaps in volatile conditions may directly penetrate the stop-loss point causing significant losses.

3. ATR calculation is solely based on historical data and cannot precisely predict future price movements and volatility. Actual stop distances might be too wide or too narrow.

4. Stop-loss orders may not always get filled in live trading; they could be skipped in extreme volatile conditions, leading to losses.

## Optimization Directions  

1. Adjust Donchian Channel parameters to optimize trend identification performance.

2. Incorporate other indicators like MACD, KDJ to confirm trading signals and improve strategy stability.

3. Add a trailing stop-loss mechanism to move the stop loss point along with price movements, further limiting potential losses.

4. Test different holding periods to find the optimal overall results.

5. Consider dynamically adjusting position sizes, increasing positions in trending conditions.

## Summary  

The Donchian Channel trend following strategy integrates trend identification and risk control. It aims to generate excess returns by identifying trends while controlling tail risks with stop-loss mechanisms. This strategy is suitable for identifying and capturing medium-to-long term price trends. With parameter optimization and mechanism enhancements, it can achieve steady positive results.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_string_1|0|Length: 20/10 |50/20 |50/50 |20/20 |100/100|
|v_input_bool_1|true|Permit long|
|v_input_bool_2|true|Permit short|
|v_input_float_1|0.5|Position Risk %|
|v_input_float_2|2|ATR multiple|
|v_input_int_1|20|ATR Length|
|v_input_bool_3|true|Close in end|
|v_input_bool_4|true|Permit stop|


> Source (PineScript)

```pinescript
//@version=5
strategy(title="Donchian", overlay=true, calc_on_every_tick=true)

// =============================================================================
// VARIABLES
// ===============================
```