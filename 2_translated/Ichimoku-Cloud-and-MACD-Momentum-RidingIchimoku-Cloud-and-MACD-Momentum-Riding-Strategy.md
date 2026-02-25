> Name

Ichimoku-Cloud-and-MACD-Momentum-RidingStrategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/148fc7accad9c45cf24.png)

[trans]

## Overview

The Ichimoku Cloud and MACD Momentum Riding is a trend-following strategy that combines the Ichimoku Cloud indicator with the MACD momentum indicator. The strategy leverages the Ichimoku Cloud to determine trend direction and support/resistance levels, and uses the MACD indicator to detect momentum reversals, timing market entries during trends. Additionally, the strategy employs trailing stop loss to lock in profits and reduce drawdowns.

## Strategy Logic

### Ichimoku Cloud

The Ichimoku Cloud consists of the Tenkan-Sen (Turning Line), Kijun-Sen (Base Line), Senkou Span A (Leading Span A), Senkou Span B (Leading Span B), and Chikou Span (Confirmation Line). The strategy uses the following signals to determine trend direction and support/resistance:

- Price above Cloud - Uptrend
- Price below Cloud - Downtrend
- Tenkan-Sen crosses above Kijun-Sen - Bullish signal
- Tenkan-Sen crosses below Kijun-Sen - Bearish signal

### MACD Indicator  

The Moving Average Convergence Divergence (MACD) is a momentum indicator. In this strategy, when the fast line of MACD crosses above the slow line it's a buy signal, and when the fast line crosses below the slow line it's a sell signal.

### Entries and Exits

When Tenkan-Sen crosses above Kijun-Sen, Senkou Span B crosses above the close price of 26 bars ago, close price breaks above top band of Cloud, and MACD's fast line has bullish crossover over slow line, go long.  

When price rises 3%, the strategy will move stop loss to 97% of current price to lock in profits and trail the upside move. If drawdown exceeds 3%, stop out with loss.  

When Tenkan-Sen crosses below Kijun-Sen, Senkou Span B crosses below the close price of 26 bars ago, close price breaks below bottom band of Cloud, and MACD's fast line has bearish crossover below slow line, go short.  

When price drops 3%, the strategy will move stop loss to 103% of current price to lock in profits and trail the downside move. If rise exceeds 3%, stop out with loss.


## Advantage Analysis

This strategy combines trend identification and entry timing, which can achieve good returns during trending markets.

1. The Ichimoku Cloud can clearly identify trend direction. The strategy only enters when aligning with Cloud direction, avoiding counter-trend trades.
2. MACD is effective in detecting short-term momentum reversals. Combining with the Cloud it improves entry accuracy.
3. Trailing stop loss allows the strategy to keep running during a trend. Proper position sizing ensures controlled risk per trade.


## Risk Analysis

There are also certain risks with this strategy:

1. The Cloud requires relatively long data periods, and may give inaccurate signals in the short term.
2. MACD oscillates with price and can generate false signals. More filters are needed to confirm signals.
3. Trailing stop loss only suits trending markets. Stop loss percentage needs to be adjusted accordingly, otherwise frequent whipsaws may occur during ranging markets.
4. The strategy itself does not manage risk. Users need to implement external risk management techniques to control losses.


## Optimization Directions

For the Ichimoku Cloud and MACD Momentum Riding strategy, optimization can be done in the following ways:

1. Parameter tuning - Adjust Tenkan-Sen, Kijun-Sen lookback periods, optimize MACD parameters for clearer signals.
2. Add filtration - Use other indicators like RSI, Bollinger Bands to filter out bad signals, reducing false signals.
3. Dynamic stops - Base stop loss percentage on market volatility and risk preference.
4. Incorporate position sizing - Limit max loss per trade to control overall drawdown.
5. Auto selecting contracts & rebalancing - Expand adaptability to more markets.


## Conclusion

The Ichimoku Cloud and MACD Momentum Riding strategy considers both trend and timing, which can achieve good returns when parameters are properly tuned and risk controls are in place. It suits investors with some programming skills as a trend-following strategy, and serves as a reference for quant trading beginners to learn technical indicators and strategy development.

[/trans]

> Strategy Arguments


|Ar