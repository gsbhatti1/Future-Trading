> Name

Scalping Trading Strategy Based on Double Moving Average

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a2b5b290e11aa667c5.png)
[trans]
## Overview

This is an oscillation trading strategy based on double moving averages. It uses the crossover of fast and slow moving averages as buy and sell signals. When the fast moving average crosses above the slow moving average, a buy signal is generated. When the fast moving average crosses below the slow moving average, a sell signal is generated. This strategy is suitable for range-bound markets and capturing short-term price fluctuations.

## Strategy Logic

The strategy uses a 6-period RMA as the fast moving average and a 4-period HMA as the slow moving average. It judges price trends and generates trading signals based on the crossover between the fast and slow lines. 

When the fast line crosses above the slow line, it indicates a short-term trend change from decline to rise, which is a timing of chip transfer. Hence a buy signal is generated. Conversely, when the fast line crosses below the slow line, a sell signal is generated.

In addition, long-term trend judgments are made to avoid trading against the trend. Actual buy/sell signals are only generated when the long-term trend aligns with the signal.

## Advantages

The advantages of this strategy include:

1. The double moving average crossover effectively identifies short-term reversal points.
2. The fast and slow moving average lengths are reasonably combined to produce accurate signals.
3. Long/short-term trend filtering removes most false signals.
4. Take profit and stop loss logic actively manages risks.
5. It is easy to understand and implement, suitable for beginners.

## Risks and Solutions

There are also some risks:

1. Prone to multiple small profits but one huge loss. Fine tune TP/SL levels.
2. Frequent trading under range-bound markets. Relax trading conditions.
3. Overfitting parameters. Robustness test needed.
4. Underperforms under trending markets. Add trend module or combine with trend strategies.

## Optimization Directions

Some directions to optimize the strategy:

1. Upgrade MAs with adaptive Kalman filters etc.
2. Add ML model to improve signal accuracy.
3. Add capital management module to automate risk control.
4. Combine with high-frequency factors for stronger signals.
5. Cross-market arbitrage across products.

## Conclusion

In conclusion, this double moving average strategy is a typical and practical quant strategy. It has good adaptivity for beginners to learn from, and has great potential to optimize further with more quant techniques for better results.

||

## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|(?⚙ Settings)Bar Color|
|v_input_2|true|Show Alerts|
|v_input_timeframe_1|0|? Timeframe: 60|5|15|30|1|120|240|360|720|D|W|
|v_input_3|true|Show Take Profit/Stop Loss|
|v_input_string_1|0|(?⚙ D-Panel Settings️)⚙ D-Panel Location: Bottom Center|Top Right|Bottom Right|
|v_input_string_2|0|⚙ D-Painel Size: Big|Small|Tiny|
|v_input_float_1|4500|(?⚙ Risk Management)Take Profit:|
|v_input_float_2|2500|Stop Loss:|
|v_input_int_1|20|(?⚙️ Scanner Market Makers Settings)Period Volume|
|v_input_float_3|1.85|Proportion to the mean: (1.25 = 125% of the mean)|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-31 00:00:00
end: 2024-01-07 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © dc_analytics
// https://datacryptoanalytics.com/

//@version=5
strategy("Scalping Trading", overlay=true)

// INPUTS //
bar_color       = input(true, title='Bar Color', group='⚙ Settings', tooltip='Color chart bars.', inline = "1")
mostrar         = input(true, 'Show Alerts', group='⚙ Settings', inline = "1")
tempo           = input.timeframe('60', group='⚙ Settings', title='? Timeframe', options=['1', '5', '15', '30', '60', '120', '240', '360', '720', 'D', 'W'])

i_position      = input.string("Bottom Center", title = "⚙ D-Panel Location", 
 options = ["Top Right", "Bottom Center", "Bottom Right"], group='⚙ D-Panel Settings️',
 tooltip='Choose the location of the information table on the chart.(D-Panel) ')

position        = i_position == "Top Right" ? position.top_right : i_position == "Bottom Center" ? position.bottom_center : position.bottom_right

i_tam           = input.string('Big', title = '⚙ D-Painel Size', 
 options = ["Tiny", "Small", "Big"], group='⚙ D-Panel Settings️', tooltip='Choose the size of the information panel (D-Panel).')

tamanho         = i_tam == "Tiny" ? size.tiny : i_tam == "Small" ? size.small : size.normal

show_tp_sl      = input(true, title='Show Take Profit/Stop Loss', group='⚙ Settings', tooltip='Show Take Profit/Stop Loss.')
TP              = input.float