> Name

JMA Indicator Crossing RSI Trading Strategy JMA-Crossing-RSI-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


## Overview

This strategy generates trading signals by crossing the Jurik Moving Average (JMA) and RSI indicators. It goes long when JMA crosses above RSI and goes short when it crosses below. The strategy attempts to filter false signals by combining two indicators and trades when a clear trend is present.

## Principles

The strategy mainly utilizes two types of indicators:

1. **JMA Indicator**: A smoothed moving average using power multipliers, with lower lag and quicker in capturing price changes.
2. **RSI Indicator**: A common strength indicator reflecting buying/selling momentum.

When JMA crosses above RSI, it indicates a stronger short-term uptrend over the long term trend and generates a buy signal. When crossing below RSI, it prompts a sell signal.

Upon receiving a crossover signal, the strategy enters trade in the corresponding direction. Exits occur when the price reaches a predetermined profit target ratio or the indicators cross in the opposite direction.

## Advantages

1. Adjustable JMA parameters adaptable to different periods.
2. RSI filters false breakouts.
3. Dual indicator combination reduces false signals.
4. Built-in stop loss controls risk.
5. Customizable profit target for profit targeting.

## Risks and Mitigations

1. Dual indicators combo may generate too few signals. Can tweak parameters for sensitivity.
2. JMA still has lag, may miss turning points. Can optimize with leading indicators.
3. Improper stop loss placement may be hit for greater losses. Should backtest for suitable placement.
4. Overreliance on indicators can produce false signals. Can add volume or volatility filters.

## Optimization Opportunities

1. Test JMA parameters to find optimal settings.
2. Try different RSI parameters for better performance.
3. Add trailing stop mechanism for adaptive stops.
4. Optimize entry position sizing like adding to winning trades.
5. Research additional filters like KD, MACD.

## Summary

The strategy enables trend following with JMA and RSI crossovers and limits risk via stops. But false signals remain probable, requiring further optimization on parameters and filters. Stop loss also needs backtest validation. It provides a basic framework for dual indicator crossing system with room for improvements.

||

## Overview

This strategy generates trading signals by the crossover of Jurik Moving Average (JMA) and RSI indicators. The strategy goes long when JMA crosses above RSI, and goes short when it crosses below. The strategy attempts to filter false signals by combining two indicators, and trades when a clear trend is more apparent.

## Principles

The strategy mainly utilizes the following two types of indicators:

1. **JMA Indicator**: A smoothed moving average using power multipliers with lower lag and quicker in capturing price changes.
2. **RSI Indicator**: A common strength indicator reflecting buying/selling momentum.

When JMA crosses above RSI, it indicates a stronger short-term uptrend over the long term trend and generates a buy signal. When crossing below RSI, it prompts a sell signal.

Upon receiving a crossover signal, the strategy enters trade in the corresponding direction. Exits occur when price reaches a predetermined profit target ratio or indicators cross in the opposite direction.

## Advantages

1. Adjustable JMA parameters adaptable to different periods.
2. RSI filters false breakouts.
3. Dual indicator combination reduces false signals.
4. Built-in stop loss controls risk.
5. Customizable profit target for profit targeting.

## Risks and Mitigations

1. Dual indicators combo may generate too few signals. Can tweak parameters for sensitivity.
2. JMA still has lag, may miss turning points. Can optimize with leading indicators.
3. Improper stop loss placement may be hit for greater losses. Should backtest for suitable placement.
4. Overreliance on indicators can produce false signals. Can add volume or volatility filters.

## Optimization Opportunities

1. Test JMA parameters to find optimal settings.
2. Try different RSI parameters for better performance.
3. Add trailing stop mechanism for adaptive stops.
4. Optimize entry position sizing like adding to winning trades.
5. Research additional filters like KD, MACD.

## Summary

The strategy enables trend following with JMA and RSI crossovers and limits risk via stops. But false signals remain probable, requiring further optimization on parameters and filters. Stop loss also needs backtest validation. It provides a basic framework for dual indicator crossing system with room for improvements.

| |

> Strategy Arguments


| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 2019 | Start Year |
| v_input_2 | 6 | Start Month |
| v_input_3 | true | Start Day |
| v_input_4 | false | Start Hour |
| v_input_5 | false | Start Minute |
| v_input_6 | 2019 | End Year |
| v_input_7 | 12 | End Month |
| v_input_8 | true | End Day |
| v_input_9 | false | End Hour |
| v_input_10 | false | End Minute |
| v_input_11 | 14 | Length |
| v_input_12 | 7 | Length |
| v_input_13 | 50 | Phase |
| v_input_14 | 2 | Power |
| v_input_15 | true | Highlight Movements ? |
| v_input_16 | true | Use Initial Stop Loss? |

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-03-15 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// The strategy performs best on a two-day timeframe.
strategy("JMA(7,50,RSI) crossing RSI(14,close)", overlay=false, currency=currency.EUR, default_qty_type=strategy.cash, default_qty_value=5000)

// Strategy Tester Start Time
sYear = input(2019, title="Start Year")
sMonth = input(06, title="Start Month", minval=01, maxval=12)
sDay = input(01, title="Start Day", minval=01, maxval=31)
sHour = input(00, title="Start Hour", minval=00, maxval=23)
sMinute = input(00, title="Start Minute", minval=00, maxval=59)
startTime = true

// Strategy Tester End Time
eYear = input(2019, title="End Year")
eMonth = input(12, title="End Month", minval=01, maxval=12)
eDay = input(01, title="End Day", minval=01, maxval=31)
eHour = input(00, title="End Hour", minval=00, maxval=23)
eMinute = input(00, title="End Minute", minval=00, maxval=59)
endTime = true

// === RSI ===
src = close, len = input(14, minval=1, title="Length")
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
plot(rsi, color=color.purple)
band1 = hline(70)
band0 = hline(30)

// === JMA ===
_length = input(7, title="Length")
_phase = input(50, title="Phase")
_power = input(2, title="Power")
highlightMovements = input(true, title="Highlight Movements ?")

// srcJMA = input(rsi, title="Source")
srcJMA = rsi

phaseRatio = _phase < -100 ? 0.5 : _phase > 100 ? 2.5 : _phase / 100 + 1.5
beta = 0.45 * (_length - 1) / (0.45 * (_length - 1) + 2)
alpha = pow(beta, _power)
jma = 0.0
e0 = 0.0
e0 := (1 - alpha) * srcJMA + e0 * alpha
e1 = 0.0
e1 := (srcJMA - e0) * (1 - beta) + e1 * beta
e2 = 0.0
e2 := (e0 + phaseRatio * e1 - jma) * pow(1 - alpha, 2) + e2 * pow(alpha, 2)
jma := e2 + jma

// === End of JMA def ===

jmaColor = highlightMovements ? (jma > jma[1] ? color.green : color.red) : #6d1e7f
plot(jma, title="JMA switch", linewidth=2, color=jmaColor, transp=0)
```