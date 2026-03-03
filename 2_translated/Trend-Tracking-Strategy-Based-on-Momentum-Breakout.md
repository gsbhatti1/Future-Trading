> Name

Momentum Breakout Trend-Tracking Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c485416b0d6677f217.png)

[trans]

## Overview

This strategy combines multiple technical indicators to identify trend direction and track the momentum when breakout happens, aiming for excess return.

## Strategy Logic

1. Use Donchian Channel to determine overall trend direction. A breakout of the channel confirms trend reversal.
2. Hull Moving Average assists in judging trend direction. It is sensitive to price changes and can early detect trend reversals.
3. Halftrend system generates buy and sell signals based on price channels and ATR range. It avoids false breakouts.
4. When Donchian, Hull, and Halftrend signals align, it confirms a strong momentum breakout, triggering entry into the market.
5. Exit when above indicators give reverse signals, indicating trend reversal.

## Advantage Analysis

- More robust signal with multiple indicators. Donchian for fundamentals, Hull and Halftrend for details, accurately catching trend turning points.
- Pursuit of excess return by momentum breakout. Only enter on strong breakouts to avoid getting trapped in consolidations.
- Strict stop loss to ensure capital safety. Cut losses immediately when reverse signals appear.
- Flexible parameter tuning for different markets. Channel length, ATR range, etc., can be adjusted and optimized.
- Easy to understand and implement. Indicator combination is simple and clear, easy to code.

## Risk Analysis

- Miss early trend opportunity. Entry timing is relatively late; early rally cannot be captured.
- Loss from failed breakout and reversal. Drawdown may occur after entry.
- False signal from poorly tuned parameters. Indicators may fail due to improper tuning.
- Limited trade frequency. Only clear breakouts are traded, resulting in low annual trade numbers.

## Optimization Directions

- Optimize parameter combinations by testing different setups to find the best fit.
- Add trailing stop loss conditions to avoid premature exits and miss potential trends.
- Introduce additional filters like MACD and KDJ to reduce false signals.
- Optimize parameters for different trading sessions. Separate tuning for different times of day.
- Improve capital efficiency through leverage, dollar-cost averaging (DCA), etc.

## Summary

This strategy combines multiple indicators to identify momentum breakout of established trends and profit from trend tracking. A strict stop loss mechanism controls risk, while flexible parameter tuning adapts to various market environments. Despite low trade frequency, each trade aims for high profitability. The strategy can be continuously improved through parameter optimization and additional filter introduction.

||

# Overview

This strategy combines multiple technical indicators to identify trend direction and track the momentum when breakout happens, aiming for excess return.

# Strategy Logic

1. Use Donchian Channel to determine overall trend. A breakout confirms trend reversal.
2. Hull Moving Average assists in judging trend direction. It is sensitive to price changes and can detect trends early.
3. Halftrend system generates buy and sell signals based on price channel and ATR range, avoiding false breakouts.
4. When Donchian, Hull, and Halftrend signals align, it confirms a strong momentum breakout and triggers entry into the market.
5. Exit when above indicators give reverse signals, indicating trend reversal.

# Advantage Analysis

- More robust signal with multiple indicators. Donchian for fundamentals, Hull and Halftrend for details, catching accurate turning points of trends.
- Pursue excess return by momentum breakout. Only enter on strong breakouts to avoid being trapped in consolidations.
- Strict stop loss ensures capital safety. Cut losses immediately when reverse signals show up.
- Flexible parameter tuning adapts to different markets. Channel length and ATR range can be adjusted for optimization.
- Easy to understand and implement. Indicator combination is simple and clear, easy to code.

# Risk Analysis

- Miss early trend opportunity. Entry is relatively late; initial rally cannot be captured.
- Loss from failed breakout and reversal. Drawdown may occur after entry.
- False signal due to bad parameter settings. Indicators may fail due to improper tuning.
- Limited trade frequency. Only clear breakouts are traded, resulting in low annual trade numbers.

# Optimization Directions

- Optimize parameter combinations by testing different setups to find the best fit.
- Add trailing stop loss conditions to avoid premature exits and missing potential trends.
- Introduce additional filters like MACD and KDJ to reduce false signals.
- Optimize parameters for different trading sessions. Separate tuning for different times of day.
- Improve capital efficiency through leverage, dollar-cost averaging (DCA), etc.

# Summary

This strategy combines multiple indicators to identify momentum breakout of established trends and profit from trend tracking. A strict stop loss mechanism controls risk while flexible parameter tuning adapts to various market environments. Although trade frequency is low, each trade aims for high profitability. The strategy can be continuously improved through parameter optimization and additional filter introduction.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|30|dlen|
|v_input_1_hlc3|0|Source: hlc3, high, low, open, hl2, close, hlcc4, ohlc4|
|v_input_string_1|0|Hull Variation: Hma, Thma, Ehma|
|v_input_2|55|Length|
|v_input_3|true|Length multiplier |
|v_input_4|2|Amplitude|
|v_input_5|2|Channel Deviation|
|v_input_int_2|7|atr_length|
|v_input_int_3|50|atr_rsi_length|

> Source (PineScript)

```pinescript
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © kgynofomo

// @version=5
strategy(title="[Salavi] | Andy Super Pro Strategy", overlay=true)

// Donchian Trend Ribbon
dlen = input.int(defval=30, minval=10)

dchannel(len) =>
    float hh = ta.highest(len)
    float ll = ta.lowest(len)

    int trend = 0
    trend := close > hh[1] ? 1 : close < ll[1] ? -1 : nz(trend[1])
    trend

dchannelalt(len, maintrend) =>
    float hh = ta.highest(len)
    float ll = ta.lowest(len)

    int trend = 0
    trend := close > hh[1] ? 1 : close < ll[1] ? -1 : nz(trend[1])
    maintrend == 1 ? trend == 1 ? #00FF00ff : #00FF009f : maintrend == -1 ? trend == -1 ? #FF0000ff : #FF00009f : na

maintrend = dchannel(dlen)
donchian_bull = maintrend==1
donchian_bear = maintrend==-1


// Hulls
src = input(hlc3, title='Source')
modeSwitch = input.string('Hma', title='Hull Variation', options=['Hma', 'Thma', 'Ehma'])
length = input(55, title='Length')
lengthMult = input(1.0, title='Length multiplier ')

useHtf = false
htf = '240'

switchColor = true
candleCol = false
visualSwitch = true
thicknesSwitch = 1
transpSwitch = 40

// FUNCTIONS
// HMA
HMA(_src, _length) =>
    ta.wma(2 * ta.wma(_src, _length / 2) - ta.wma(_src, _length), math.round(math.sqrt(_length)))
// EHMA    
EHMA(_src, _length) =>
    ta.ema(2 * ta.ema(_src, _length / 2) - ta.ema(_src, _length), math.round(math.sqrt(_length)))
// THMA    
THMA(_src, _length) =>
    ta.wma(ta.wma(_src, _length / 3) * 3 - ta.wma(_src, _length / 2) - ta.wma(_src, _length), _length)

// SWITCH
Mode(modeSwitch, src, len) =>
    modeSwitch == 'Hma' ? HMA(src, len) : modeSwitch == 'Ehma' ? EHMA(src, len) : modeSwitch
```