> Name

Amazing-Price-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13d90740841c52b4a85.png)
[trans]
Overview: This strategy utilizes Bollinger Bands, KDJ indicators, and trend following for price breakout operations. It can make long and short entries at breakout points and set stop loss to control risks.

Strategy Logic:

1. Calculate the 15-day and 30-day simple moving averages to determine the price trend.
2. Calculate the upper and lower rails of the Bollinger Band, and combine candlestick breakout of BB rails to determine entries and exits.
3. Use the RSI indicator to judge overbought and oversold conditions. An RSI greater than 50 indicates an overbought signal, and an RSI less than 50 indicates an oversold signal.
4. When the price breaks above the Bollinger Band upper rail with RSI greater than 50, a buy signal is generated; when the price falls below the lower Bollinger Band rail with RSI less than 50, a sell signal is generated.
5. Set ATR stop loss to control risks.

Advantages:

1. This strategy combines multiple indicators such as Bollinger Bands and RSI to determine trading signals, effectively avoiding errors caused by a single indicator.
2. With trend filtering, it can prevent wrong signals during consolidation and reversal phases.
3. ATR stop loss controls the risk of each trade.
4. The strategy logic is clear and simple, making it easy to understand and implement.

Risks and Improvements:

1. As an envelope indicator, the Bollinger Band's upper and lower rails are not absolute support and resistance levels. After the price breaks through these rails, the stop loss may be breached. You can set a looser stop loss point or use other stop loss strategies such as time stop loss.
2. The RSI indicator may fail in certain markets. You can consider combining other indicators such as KDJ, MACD, etc., to achieve more reliable overbought and oversold judgments.
3. In reversal and consolidation markets, it is easy to generate wrong signals. You can consider adding trend filtering and only participate in operations when the trend is obvious.

Optimization Suggestions:

1. Test and optimize the period number and standard deviation parameters of Bollinger Bands to make them more consistent with the characteristics of different varieties.
2. Test and optimize the period parameters of RSI.
3. Test other stop loss strategies, such as trailing stop loss, time stop loss, etc.
4. Combine more trend judgment indicators and signal indicators to build a multi-factor model.

Summary:

This strategy comprehensively uses multiple indicators such as Bollinger Bands and RSI to determine the timing of buying and selling. While ensuring the accuracy of certain trading signals, it also sets stop losses to control risks. However, parameter optimization still needs to be carried out for specific varieties to make the signal more accurate and reliable. Additionally, you can consider adding more factors to build a multi-factor model. Overall, this strategy provides a relatively simple and practical idea for price breakout operations, which is worthy of further research and optimization.

||

Overview: This strategy utilizes Bollinger Bands, KDJ indicator, and trend following for price breakout operations. It can make long and short entries at breakout points and set stop loss to control risks.

Strategy Logic:

1. Calculate the 15-day and 30-day simple moving averages to determine the price trend.
2. Calculate the upper and lower rails of the Bollinger Band, and combine candlestick breakout of BB rails to determine entries and exits.
3. Use the RSI indicator to judge overbought and oversold conditions. An RSI greater than 50 indicates an overbought signal, and an RSI less than 50 indicates an oversold signal.
4. When the price breaks above the Bollinger Band upper rail with RSI greater than 50, a buy signal is generated; when the price falls below the lower Bollinger Band rail with RSI less than 50, a sell signal is generated.
5. Set ATR stop loss to control risks.

Advantages:

1. The strategy combines multiple indicators like Bollinger Bands and RSI to determine trading signals, effectively avoiding errors caused by single indicator.
2. With trend filtering, it can prevent wrong signals during consolidation and reversal phases.
3. ATR stop loss controls the risk of each trade.
4. The strategy logic is simple and easy to understand.

Risks & Improvements:

1. As an envelope indicator, the Bollinger Band's upper and lower rails are not absolute support and resistance levels. Prices may break the rails and hit stop loss. Can set wider stop loss or use other stop loss methods like time exit.
2. RSI may fail in some markets. Can consider combining other indicators like KDJ and MACD for more reliable overbought/oversold judgment.
3. Wrong signals may occur during reversals and consolidations. Can add trend filter to only trade along the major trend.

Enhancement Suggestions:

1. Test and optimize Bollinger Bands period and standard deviation parameters for different products.
2. Test and optimize RSI period parameter.
3. Test other stop loss methods like trailing stop loss, time exit.
4. Add more trend indicators and signal indicators to build multifactor models.

Conclusion:

The strategy combines Bollinger Bands, RSI, and other indicators for entry and exit signals. It controls risks while ensuring signal accuracy. More optimization can be done on parameters and enhancements like multifactor models. Overall it provides a simple and practical idea on price breakout strategies.

[/trans]

> Source (PineScript)

```pinescript
//@version=4
strategy("Custom Strategy", overlay=true)

length = 15
mult =
```