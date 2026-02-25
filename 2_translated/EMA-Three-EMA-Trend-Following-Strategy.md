> Name

Three-EMA-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/b940064ababd737a51.png)
[trans]

## Overview

The Three-EMA Trend Following Strategy tracks the overall price trend by calculating EMA lines of different periods and follows the identified trend. This strategy is simple to implement, effective in trending markets, and suitable for beginners.

## Strategy Logic

This strategy calculates three EMA lines with specific periods: 10-period, 20-period, and 30-period EMAs. The `ema` function in the code generates these EMA lines.

The core logic involves judging the direction of the three EMA lines. If all three EMA lines are rising together, a long signal is generated; if they are falling together, a short signal is generated.

Specifically:
- If `ema1`, `ema2`, and `ema3` have all risen in the last bar, `enter_long` becomes true, generating a long signal.
- If `ema1`, `ema2`, and `ema3` have all fallen in the last bar, `enter_short` becomes true, generating a short signal.

Based on these signals, the strategy opens corresponding long or short positions. The exit logic is opposite to the entry signals:
- If `ema1`, `ema2`, and `ema3` do not rise together in the current bar, `exit_long` becomes true, closing the long position.
- If they do not fall together, `exit_short` becomes true, closing the short position.

By judging the direction consistency of the three EMA lines, the overall trend can be determined and followed.

## Advantages

- Using three EMA lines provides a more reliable way to judge trend direction compared to a single line. The probability of wrong signals is lower.
- EMA is more sensitive to price changes and can reflect trend reversals in real time. It is better suited for trend judgment compared to SMA, etc.
- Combining different period EMAs takes both short-term and medium-to-long term trends into account. `10-period` EMA for short-term, `20` and `30-period` EMAs for medium-to-long term trends.
- The strategy logic is simple and easy to understand, making it suitable for beginners. There is also a large space for parameter optimization tailored to different instruments.
- The strategy operates solely on EMA lines, requiring fewer resources and being suitable for high concurrency.

## Risks

- Directional consistency of the three EMAs is necessary but not sufficient for trend judgment. False signals can occur during false breakouts by EMAs.
- EMAs lag in reflecting trend reversals; they may fail to reflect turning points in time, potentially leading to losses.
- EMA's sensitivity to price changes means that frequent long-short position flips can increase transaction costs.
- The strategy performs poorly in volatile markets where EMA lines frequently change direction.

- Can optimize the period difference between three EMAs to reduce false signals. Or add other indicators to filter out fake breakouts.

- Add momentum indicators to confirm real trends and identify turning points, reducing losses. Also, consider loosening stop loss levels.

- Increase the periods of the EMA to decrease position flip frequency. Or use alternative MA indicators.

- Suspend the strategy when identifying a ranging market to avoid unnecessary trades.

## Optimization

- Period Tuning: Adjust the EMA periods to adapt to different instruments.
- Add Filters: Incorporate additional indicators such as MA, BOLL, etc., to filter out false breakouts.
- Stop Loss Strategy: Use trailing stop to lock in profits.
- Risk Management: Optimize position sizing to limit single loss impact.
- Market Regime: Utilize volatility metrics to gauge market oscillation and control strategy engagement.
- Adaptive Parameters: Automatically optimize EMA periods based on market changes to enhance the robustness of the strategy.

## Conclusion

The Three-EMA Trend Following Strategy trades by identifying trend direction via EMA lines, making it simple and practical with substantial optimization potential. Risks such as false breakouts and volatility should be considered. Continuous optimizations can make this strategy a reliable solution for trend following.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|10|EMA1 Period|
|v_input_2|20|EMA2 Period|
|v_input_3|30|EMA3 Period|
|v_input_4|false|Long Only|
|v_input_5|5|Stop-loss (%)|
|v_input_6|false|Use Stop-Loss|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-10-10 00:00:00
end: 2023-11-09 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
```