> Name

MACD动量缠绕DMI突破短线套利策略Inverse-MACD-Momentum-Entangled-with-DMI-Breakout-Short-Term-Scalping-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10f9c64555169d84b4b.png)
[trans]


## Overview

This strategy focuses on short selling during bear market conditions by utilizing two strength-based indicators to provide confluence that the start of a short-term downtrend has occurred - catching the shorting opportunity as soon as possible.

The strategy works well on coins you plan to hold long-term and performs especially well when using an automated trading bot to execute trades for you. It allows you to hedge your investment by allocating a percentage of your holdings to trade with, without risking your entire position. This mitigates unrealized losses from holding as it provides additional cash from the profits made. You can then choose to hold this cash or use it to reinvest when the market reaches attractive buying levels.

Alternatively, if you are trading futures contracts, you can short the underlying asset directly without owning it first.

## Strategy Logic

The trading system uses the Momentum Average Convergence Divergence (MACD) indicator and the Directional Movement Index (DMI) indicator to confirm when the best time is for selling. Combining these two indicators prevents trading during uptrends and reduces the likelihood of getting stuck in a market with low volatility.

The MACD is a trend-following momentum indicator that identifies short-term trend direction. In this variation, it utilizes the 12-period as the fast and 26-period as the slow length EMAs, with signal smoothing set at 9.

The DMI indicates price trends by comparing prior lows and highs, drawing two lines between them - the positive directional movement line (+DI) and the negative directional movement line (-DI). Trends can be interpreted by comparing the two lines and which one is greater. When the negative DMI is greater than the positive DMI, there are more chances that the asset is trading in a sustained downtrend, and vice versa.

The system will enter trades when two conditions are met:

1. The MACD histogram turns bearish.
2. When the negative DMI is greater than the positive DMI.

The strategy comes with a fixed take profit combined with a volatility stop, which acts as a trailing stop to adapt to the trend's strength. Depending on your long-term confidence in the asset, you can edit the fixed take profit to be more conservative or aggressive.

The position is closed when:

Take-Profit Exit: +8% price decrease from entry price.
OR
Stop-Loss Exit: Price crosses above the volatility stop.

In general, this approach suits medium to long term strategies. The backtesting for this strategy begins on April 1, 2022, to July 18, 2022, in order to demonstrate its results in a bear market. Further backtesting from early 2022 also produces good returns.

Pairs that produce very strong results include SOLUSDT on the 45-minute timeframe, MATICUSDT on the 2-hour timeframe, and AVAUSDT on the 1-hour timeframe. Generally, back testing suggests it works best on the 45-minute/1-hour timeframe across most pairs.

A trading fee of 0.1% is also taken into account and is aligned to the base fee applied on Binance.

## Advantage Analysis

The advantages of this strategy include:

- Utilizes the strengths of both MACD and DMI indicators to improve the accuracy of entry signals and avoid false breakouts.
- Employs a combination of fixed take profit and volatility trailing stop exit mechanisms to ensure higher take profits while controlling risk.
- Suitable for bear market downtrends to capture substantial short-term scalping profits.
- Can be used to hedge long positions to gain additional income. Or directly short futures contracts for scalping.
- Strong backtest results, especially on 1-hour and 45-minute timeframes suitable for high-frequency trading.

## Risk Analysis

The risks of this strategy include:

- DMI and MACD as lagging indicators have a higher probability of generating erroneous signals around trend reversals. Close attention to stop losses is required.
- Fixed take profit settings may be too conservative or aggressive, depending on the volatility of different assets. Adjustments should be made accordingly.
- Volatility trailing stops can be broken during periods of high market volatility. It’s recommended to combine with additional stop loss mechanisms.
- Backtesting period selection can lead to overly optimistic results. Longer-term backtests and testing across different market phases are advised.
- Real trading performance may differ from backtests due to transaction fees, market slippage, etc.

## Optimization Directions

This strategy can be further optimized in the following ways:

- Utilize machine learning methods to automatically optimize MACD and DMI parameters for different timeframes and assets.
- Add a dynamic take profit based on volatility, adjusting profits based on market volatility.
- Include other indicators in judgment to form a multi-factor model, enhancing filtering effectiveness. For example, using BVN and OBV indicators.
- Introduce trend judgment through machine learning models to assist MACD and DMI signals.
- Use limit orders instead of market orders to reduce the impact of market slippage.
- Test on different assets separately to find optimal cycle parameter combinations.

## Conclusion

In summary, this short-term bearish arbitrage strategy uses a robust combination of MACD and DMI indicators to determine when to short-sell, achieving high quantitative gains. It can be used to hedge long positions or directly short futures contracts for scalping profits. Optimizing the stop loss strategy and parameter adjustments can further increase the success rate. This strategy is worth active application by bear market traders.

||