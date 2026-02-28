> Name

Dual-Hull-Moving-Average-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/135c02e99fd30d3e94d.png)

[trans]

## Overview

The Dual Hull Moving Average Trading Strategy is a quantitative trading strategy that uses the Dual Hull Moving Average as trading signals. It draws on the traditional technical analysis approach of using a single moving average line and replaces it with the Dual Hull Moving Average to make long and short decisions at crossover points.

## Principles  

At the core of the Dual Hull Moving Average Trading Strategy is the Dual Hull Moving Average (DHMA). The DHMA consists of three lines: middle, upper, and lower rails, representing different average price values. The formulas are:

Middle Rail: Mode(modeSwitch, src, len)  
Upper Rail: HULL[0]
Lower Rail: HULL[2]  

Here the Mode function can choose between different Hull MA variants like HMA, EHMA or THMA. Src stands for the price source, and len is the period parameter.

The strategy uses the middle rail of the DHMA as reference to determine the price relationship and generate trading signals:

- When price crosses above middle rail, go long.
- When price crosses below middle rail, close position.

In other words, if the closing price of the current bar is above the middle rail value, go long on the next bar; if the closing price is below, close long position on the next bar.

## Advantages

The Dual Hull Moving Average Trading Strategy has the following advantages:

1. Uses a triple bands mechanism instead of a single moving average line for better support/resistance effects and trend tracking.
2. Compared to common MAs, The Hull Moving Averages have less lag and respond better to price changes.
3. Adopts traditional technical analysis techniques for easy understanding, suitable for algo trading.
4. The logic is simple and clear, easy to implement, fitting high frequency algorithmic trading.
5. Customizable Hull MA types and parameters for optimization across different products and time frames.

## Risks

While having many merits, the strategy also poses some risks to note:

1. More whipsaws may occur during choppy sideways markets. Fine tune parameters to filter out some noise trades.
2. The strategy mainly follows trends, less effective during flat periods. Additional filters for trend strength may help.
3. Hull MAs still have some degree of lag, especially for short terms. Parameter optimization and combo indicators could alleviate this.
4. Frequent signals may lead to over-trading. Manage position sizing and trade frequency.

## Optimization Directions

Here are some major aspects to optimize for the strategy:

1. Optimize Hull MA types and parameters to fine tune middle rail sensitivity for different products.
2. Add stop loss mechanisms like trailing stop or incremental stop loss to control single trade loss amount.
3. Combine with other indicators to determine trend direction and strength, avoiding traps. E.g. MACD, KD etc.
4. Add strategy activation conditions based on number of trades or profit ratio to control cycle closure counts, reducing exits.
5. Multi-timeframe combination. Use higher TFs to decide overall trend to avoid noise.
6. Refine entry logic. Confirm entries with candle patterns to improve entry certainties.

## Conclusion

In summary, the Dual Hull Moving Average Trading Strategy is a quantitative approach utilizing the fast responding, trend following Hull Moving Averages to construct trading signals. Compared to traditional MAs, it has quicker response and better tracking abilities. The strategy logic is simple and clear, easy to automate for algorithmic trading. There are still risks of noises and trend following limitations. Techniques like parameter tuning, stop loss, and combining other indicators can enhance its practical performance.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2016|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2030|Backtest Stop Year|
|v_input_5|12|Backtest Stop Month|
|v_input_6|30|Backtest Stop Day|
|v_input_7_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_8|0|Hull Variation: Hma|Thma|Ehma|
|v_input_9|55|Length(180-200 for floating S/R , 55 for swing entry)|
|v_input_10|true|Color Hull according to trend?|
|v_input_11|false|Color candles based on Hull's Trend?|
|v_input_12|true|Show as a Band?|
|v_input_13|true|Line Thickness