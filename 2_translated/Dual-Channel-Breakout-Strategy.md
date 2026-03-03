---

### Name

Dual-Channel-Breakout-Strategy

### Author

ChaoZhang

### Strategy Description

![IMG](https://www.fmz.com/upload/asset/a656fe906fed023b28.png)
[trans]

This strategy name derives from its use of Bollinger Bands and Keltner Channels as two indicators to generate trading signals. It monitors price breakouts beyond channel boundaries, going long on downside breakouts and short on upside breakouts.

#### Strategy Logic

The strategy combines the use of Bollinger Bands and Keltner Channels. Bollinger Bands are adaptive channels plotted at a moving average line plus/minus standard deviations. Keltner Channels use true range to compute channel width.

The trading logic is to go long when the closing price falls below the lower Bollinger Band and lower Keltner Channel, anticipating a reversal. It goes short when the closing price rises above the upper Bollinger and Keltner Channel boundaries. Stops and take profits are set after entry.

#### Strengths

By combining two channels, the strategy effectively identifies abnormal price swings. The dual channel filters help avoid false signals. The stops and take profits also aid in risk control.

Compared to using just Bollinger Bands or Keltner Channels, this strategy filters out more noise for higher-quality signals. Dual-channel breakouts allow timely entries aiming to capture reversals.

#### Risk Analysis

A key risk is the lagging nature of channel indicators. Prices could start reversing before hitting the channel boundaries that trigger signals. This may result in late entries or being caught in pullbacks.

Overly tight stops and excessively wide take profits are other risks. These need to be adjusted per market conditions.

#### Enhancement Opportunities

The strategy can be optimized by adding auxiliary filters like momentum oscillators. Parameter tuning to discover optimal combinations may also help.

Incorporating adaptive stops and take profits is another enhancement route, helping the strategy better adapt to evolving markets.

#### Conclusion

This dual channel breakout strategy combines the strengths of Bollinger Bands and Keltner Channels to effectively identify reversal opportunities, while controlling risks via dual channel filters and stop/take profit settings. It is a quality, risk-managed quantitative trading strategy.

[/trans]

### Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Bollinger Bands Length|
|v_input_2|2|Bollinger Bands Deviation|
|v_input_3|20|Keltner Channels Length|
|v_input_4|1.5|Keltner Channels ATR Multiplier|
|v_input_5|10|Take Profit (in $)|
|v_input_6|20|Stop Loss (in $)|


### Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-31 00:00:00
end: 2024-01-31 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Bollinger Bands and Keltner Channels Breakout Strategy", overlay=true)

// Bollinger Bands Parameters
bollinger_length = input(20, title="Bollinger Bands Length", minval=1)
bollinger_deviation = input(2.0, title="Bollinger Bands Deviation", minval=0.1)

// Keltner Channels Parameters
keltner_length = input(20, title="Keltner Channels Length", minval=1)
atr_multiplier = input(1.5, title="Keltner Channels ATR Multiplier", minval=0.1)

// Take Profit and Stop Loss in financial terms
take_profit = input(10.0, title="Take Profit (in $)", step=1)
stop_loss = input(20.0, title="Stop Loss (in $)", step=1)

// Calculations for Bollinger Bands
basis_bb = sma(close, bollinger_length)
dev_bb = sma(stdev(close, bollinger_length), bollinger_length)
upper_bb = basis_bb + dev_bb * bollinger_deviation
lower_bb = basis_bb - dev_bb * bollinger_deviation

// Calculations for Keltner Channels
basis_kc = sma(close, keltner_length)
atr_kc = sma(atr(keltner_length), keltner_length)
upper_kc = basis_kc + atr_multiplier * atr_kc
lower_kc = basis_kc - atr_multiplier * atr_kc

// Buy Condition
buy_condition = close < lower_bb and close < lower_kc

// Sell Condition
sell_condition = close > upper_bb and close > upper_kc

// Long/Short Strategy with TP and SL
if (buy_condition)
    strategy.entry("Buy", strategy.long)
    strategy.exit("Take Profit/Stop Loss", from_entry="Buy", profit=take_profit, loss=stop_loss)
if (sell_condition)
    strategy.entry("Sell", strategy.short)
    strategy.exit("Take Profit/Stop Loss", from_entry="Sell", profit=take_profit, loss=stop_loss)

// Plot Bollinger Bands and Keltner Channels
plot(upper_bb, color=color.rgb(47, 33, 243), title="Upper Bollinger Band")
plot(lower_bb, color=color.rgb(89, 33, 243), title="Lower Bollinger Band")
plot(upper_kc, color=color.rgb(200, 255, 0), title="Keltner Channel Upper")
plot(lower_kc, color=color.rgb(225, 255, 0), title="Keltner Channel Lower")

```

### Detail

https://www.fmz.com/strategy/440717

### Last Modified

2024-02-01 14:43:07