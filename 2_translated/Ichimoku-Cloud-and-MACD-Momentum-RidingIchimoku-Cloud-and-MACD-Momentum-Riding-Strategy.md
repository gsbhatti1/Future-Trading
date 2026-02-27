> Name

Ichimoku-Cloud-and-MACD-Momentum-Riding-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/148fc7accad9c45cf24.png)

[trans]

## Overview

Ichimoku Cloud and MACD Momentum Riding is a trend-following strategy that combines the Ichimoku Cloud indicator and the MACD momentum indicator. The strategy leverages the Ichimoku Cloud to determine trend direction and support/resistance levels, as well as the MACD to detect momentum reversals, enabling timely entry into the market during trends. Additionally, the strategy employs a trailing stop loss to lock in profits and reduce drawdowns.

## Strategy Logic

### Ichimoku Cloud

The Ichimoku Cloud consists of the Turning Line (Tenkan-Sen), Base Line (Kijun-Sen), Leading Span A (Senkou-Span A), Leading Span B (Senkou-Span B), and Confirmation Line (Chikou-Span). The strategy uses the following signals to determine trend direction and support/resistance:

- Price above Cloud - Uptrend
- Price below Cloud - Downtrend
- Turning Line crosses above Base Line - Bullish signal
- Turning Line crosses below Base Line - Bearish signal

### MACD Indicator

The Moving Average Convergence Divergence (MACD) is a momentum indicator. In this strategy, when the fast line of MACD crosses above the slow line it's a buy signal, and when the fast line crosses below the slow line it's a sell signal.

### Entries and Exits

When the Turning Line crosses above the Base Line, the Confirmation Line crosses above the close price of 26 bars ago, the close price breaks above the top band of Cloud, and MACD's fast line has a bullish crossover over the slow line, go long.

When the price rises by 3%, the strategy will move the stop loss to 97% of the current price to lock in profits and trail the upside move. If the drawdown exceeds 3%, exit with a loss.

When the Turning Line crosses below the Base Line, the Confirmation Line crosses below the close price of 26 bars ago, the close price breaks below the bottom band of Cloud, and MACD's fast line has a bearish crossover below the slow line, go short.

When the price falls by 3%, the strategy will move the stop loss to 103% of the current price to lock in profits and trail the downside move. If the recovery exceeds 3%, exit with a loss.


## Advantage Analysis

This strategy combines trend identification and entry timing, which can achieve good returns during trending markets.

1. The Ichimoku Cloud clearly identifies trend direction. The strategy only enters when aligned with the Cloud's direction, avoiding counter-trend trades.
2. MACD effectively detects short-term momentum reversals. Combining with the Cloud improves entry accuracy.
3. Trailing stop loss allows the strategy to keep running during a trend. Proper position sizing ensures controlled risk per trade.


## Risk Analysis

There are also certain risks associated with this strategy:

1. The Ichimoku Cloud requires relatively long lookback periods and may give inaccurate signals in the short term.
2. MACD oscillates with price and can generate false signals. More filters are needed to confirm signals.
3. Trailing stop loss only suits trending markets. Stop loss percentage needs to be adjusted accordingly, otherwise whipsaws may stop out too frequently during ranging markets.
4. The strategy itself does not manage risk. Users need to implement external risk management techniques to control losses.


## Optimization Directions

For the Ichimoku Cloud and MACD Momentum Riding strategy, optimizations can include:

1. Parameter tuning - Adjust Turning Line and Base Line lookback periods, optimize MACD parameters for clearer signals.
2. Add filtration - Use other indicators like RSI, Bollinger Bands to filter out bad signals, reducing false signals.
3. Dynamic stops - Base stop loss percentage on market volatility and risk preference.
4. Incorporate position sizing - Limit max loss per trade to control overall drawdown.
5. Auto selecting contracts & rebalancing - Expand adaptability to more markets.


## Conclusion

The Ichimoku Cloud and MACD Momentum Riding strategy considers both trend identification and timing, which can achieve good returns when parameters are properly tuned and risk controls are in place. It suits investors with some programming skills as a trend-following strategy, and serves as a reference for quant trading beginners to learn technical indicators and strategy development.

[/trans]

> Strategy Arguments

|Argument Name| Default Value| Description|
|---|---|---|
|||