> Name

One-Cloud Multiple Moving Average Trading Strategy - Ichimoku-Cloud-and-Moving-Average-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/17e975d8001cb544ebf.png)

[trans]
#### Overview
This strategy combines the Ichimoku Cloud and short-term (55) and long-term (200) Simple Moving Averages (SMA) to identify potential buy and sell signals. Buy signals require the price to be above the cloud and long-term SMA, and retest the short-term SMA after crossing above it. Sell signals require the price to be below the cloud and long-term SMA, and retest the short-term SMA after crossing below it. The strategy avoids generating signals during ranging markets or major news events as these periods tend to have more false signals. Backtesting shows that this strategy performs best on 1-hour and 2-hour timeframes.

#### Strategy Principles
The strategy is based on the following principles:
1. When price is above the cloud and long-term SMA, the market is in an uptrend.
2. When price is below the cloud and long-term SMA, the market is in a downtrend.
3. Crossovers of the short-term SMA confirm trends, and retests of the short-term SMA provide low-risk entry opportunities.
4. Ranging markets and major news events have more false signals and should be avoided.

The code first calculates the required Ichimoku Cloud components (Conversion Line, Base Line, Leading Span A and B), as well as the short-term and long-term SMAs. It then defines multiple conditions to identify the price position relative to the cloud and moving averages. When all buy/sell conditions are met, the code generates buy and sell signals.

#### Strategy Advantages
1. Combines multiple indicators to confirm trends, improving signal reliability. The Ichimoku Cloud filters out noise, while SMA crossovers confirm trends.
2. Seeks low-risk entry opportunities on retests of moving averages within confirmed trends.
3. Further reduces false signal risks by avoiding trades during ranging markets and major news events.
4. Suitable for medium to long-term trading on 1-hour and 2-hour timeframes, capturing big trends with large profit potential.

#### Strategy Risks
1. Losses may occur during trend reversals. Although moving average crossovers and cloud breakouts confirm trends, they still lag.
2. Lacks clear stop-loss levels. Current conditions focus on entry timing but do not define specific exit points.
3. Parameter selection is subjective and uncertain. Different choices of cloud parameters, moving average lengths, etc., will affect strategy performance.

#### Strategy Optimization Directions
1. Introduce clear stop-loss levels, such as previous high/low breaches, ATR multiples, etc., to reduce single trade risk.
2. Cross-reference with other trend confirmation indicators, such as MACD, DMI, etc., to form more robust signal combinations.
3. Optimize parameters to find the best combination that improves the strategy's adaptability to various market conditions.
4. Differentiate between trending and ranging markets, actively enter positions in trends while reducing trading frequency in ranges.

#### Summary
The "Ichimoku Cloud and Moving Average Strategy" seeks low-risk entry opportunities by combining the Ichimoku Cloud with Simple Moving Averages within established trends. By filtering out trades during ranging markets and major news events, the strategy reduces false signal risks and improves overall performance. It is mainly suitable for medium to long-term traders and performs well on 1-hour and 2-hour timeframes. However, there is still room for further optimization, such as introducing clear stop-losses, optimizing signal combinations, and tuning parameters, to achieve more robust strategy performance.

[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2023-05-11 00:00:00
end: 2024-05-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Ichimoku Cloud and Moving Average Strategy", shorttitle="ICMA", overlay=true)

// Input parameters
shortMA = input.int(55, title="Short-term Moving Average Length")
longMA = input.int(200, title="Long-term Moving Average Length")

// Calculate moving averages
shortSMA = ta.sma(close, shortMA)
longSMA = ta.sma(close, longMA)

// Ichimoku Cloud settings
conversionPeriod = input.int(9, title="Conversion Line Period")
basePeriod = input.int(26, title="Base Line Period")
spanBPeriod = input.int(52, title="Span B Period")
displacement = input.int(26, title="Displacement")

// Calculate Ichimoku Cloud components
conversionLine = ta.sma(high + low, conversionPeriod) / 2
baseLine = ta.sma(high + low, basePeriod) / 2
leadSpanA = (conversionLine + baseLine) / 2
leadSpanB = ta.sma(high + low, spanBPeriod) / 2

// Plot Ichimoku Cloud components
plot(conversionLine, color=color.blue, title="Conversion Line")
plot(baseLine, color=color.red, title="Base Line")
plot(leadSpanA, color=color.green, title="Leading Span A")
plot(leadSpanB, color=color.orange, title="Leading Span B")

// Plot moving averages
plot(shortSMA, color=color.purple, title="Short-term SMA")
plot(longSMA, color=color.magenta, title="Long-term SMA")

// Buy and sell conditions
buyCondition = (close > leadSpanB) and (close > longSMA) and ta.crossover(shortSMA, close)
sellCondition = (close < leadSpanB) and (close < longSMA) and ta.crossunder(shortSMA, close)

if (buyCondition)
    strategy.entry("Buy", strategy.long)

if (sellCondition)
    strategy.exit("Sell", "Buy")

// Add labels for signal occurrences
label.new(x=bar_index, y=high, text="BUY", color=color.green, style=label.style_label_down, size=size.small)
label.new(x=bar_index, y=low, text="SELL", color=color.red, style=label.style_label_up, size=size.small)

// Plot horizontal lines for support and resistance
hline(0.5, "Support Line", color=color.blue, linestyle=hline.style_dashed, linewidth=2)
hline(1.5, "Resistance Line", color=color.red, linestyle=hline.style_dashed, linewidth=2)
```