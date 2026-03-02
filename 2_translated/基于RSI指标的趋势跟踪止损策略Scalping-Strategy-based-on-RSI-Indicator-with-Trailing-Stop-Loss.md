> Name

Scalping Strategy based on RSI Indicator with Trailing Stop Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b398270b341c2162f3.png)
[trans]

## Overview

This strategy is named "Scalping Strategy based on RSI Indicator with Trailing Stop Loss." It utilizes the RSI indicator to determine overbought and oversold conditions, combines fast and slow Moving Averages (MA) to identify trend direction, and sets entry criteria. Additionally, it uses a percentage trailing stop loss mechanism for exit.

## Strategy Logic

The entry signals of this strategy are primarily determined by the RSI indicator and MA crossovers. The RSI parameter is set to 2 periods to quickly capture overbought and oversold situations for reversal opportunities. The fast MA and slow MA are set to 50 and 200 periods, respectively, to identify trend direction. Specifically, the entry logic is:

- Long entry: Fast MA crosses above slow MA, price is above slow MA, and RSI is below oversold level (default 10%).
- Short entry: Fast MA crosses below slow MA, price is below slow MA, and RSI is above overbought level (default 90%).

In addition, there is an optional volatility filter in the strategy. It calculates the difference between the slopes of fast and slow MAs. Positions will only be opened when the difference exceeds a threshold. The purpose is to avoid opening positions during market fluctuations with no clear direction.

On the exit side, the strategy uses percentage trailing stop loss. Based on the input percentage, it calculates the stop loss price combined with the tick size, to dynamically adjust the stop loss.

## Advantage Analysis

The main advantages of this strategy are:

1. RSI set to 2 periods can quickly capture overbought and oversold situations for reversal opportunities.
2. Fast and slow MAs can effectively identify trend direction and turning points.
3. Combining RSI and MA dual indicators avoids false breakouts.
4. Volatility filter helps avoid opening positions during market fluctuations with no clear direction.
5. Percentage trailing stop loss allows adjusting the stop loss level based on market volatility to effectively control risks.

## Risk Analysis

There are also some risks in this strategy:

1. RSI and MA indicators have some lagging effect, which may miss some reversal opportunities.
2. Percentage stop loss is likely to be triggered during low volume declines.
3. Significant overnight and pre-market price swings are not handled effectively.

The optimization directions for the risks are:

1. Adjusting the RSI parameter to 1 period can reduce the lagging effect.
2. Optimizing MA periods based on symbol characteristics.
3. Adjusting the percentage stop loss level to balance between stop loss and fluctuation tolerance.

## Optimization Directions

The optimization directions for this strategy include:

1. Adding other indicators, such as volume, to avoid false breakout signals.
2. Incorporating machine learning model predictions to assist in decision making.
3. Optimizing pyramiding times and position sizing to further improve returns.
4. Setting up filters for overnight and pre-market price swings to determine whether to participate in the next trading day based on fluctuation.

## Conclusion

In general, this is a relatively stable trend-following strategy. By combining dual RSI and MA indicators, it ensures certain stability while capturing clearer trend reversal opportunities. The volatility filter avoids some risks, and percentage stop loss effectively controls single trade losses. This strategy can be used as a multi-symbol generic strategy or optimized for specific symbols to achieve better results.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|def_start_date|Start date|
|v_input_2|def_end_date|End date|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|2|RSI Length|
|v_input_5|90|Overbought threshold|
|v_input_6|10|Oversold threshold|
|v_input_7|200|Slow MA length|
|v_input_8|50|Fast MA length|
|v_input_9|0|MA choice: EMA|SMA|
|v_input_10|0.5|Ticker size|
|v_input_11|true|Trend Filter|
|v_input_12|true|Trailing Stop %|


> Source (PineScript)

```pinescript
// Scalping strategy
// © Lukescream and Ninorigo
// (original version by Lukescream - latest versions by Ninorigo) - v1.3

//@version=4
strategy(title="Scalping using RSI 2 indicator", shorttitle="RSI 2 Strategy", overlay=true, pyramiding=0, process_orders_on_close=false)

var bool ConditionEntryL = false
var bool ConditionEntryS = false


//***********
```