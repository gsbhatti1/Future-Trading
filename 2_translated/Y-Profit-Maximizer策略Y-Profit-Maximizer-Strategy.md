> Name

Y-Profit-Maximizer Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/bf57dac26ee6be0d40.png)

[trans]


## Overview

The core idea of this strategy is to maximize profits by using moving stop loss tracking, and optimize entry by using filters and take profit methods. The Y shape in the strategy name represents the crossover pattern of the buy and sell signal lines.

## Strategy Logic

This strategy is mainly based on KivancOzbilgic's PMax Explorer strategy with some modifications.  

1. Calculate PMax based on ATR and Moving Average. Generate buy signal when price crosses over PMax.
2. Add T3 indicator and price as filters to ensure entering during an upward trend.
3. Set take profit methods: First use double BAND strategy to determine the first take profit; then use Dice strategy to determine subsequent take profits and stop losses.
4. MOST indicator assists in determining trends, reducing unnecessary reverse operations.

## Advantage Analysis  

1. The PMax strategy itself has the advantage of avoiding chasing high stops, and the moving stop mechanism further helps reduce drawdowns (DD).
2. The double filter ensures that we only enter on upward trends, avoiding false breakouts.
3. Multiple take profit points make profits more flexible.
4. MOST indicator ensures long-only operations, avoiding reverse trading.

## Risk Analysis  

1. PMax itself has some lag, easily missing the first breakout.
2. Too many filter settings could also miss the golden entry point.
3. Overly optimistic take profit settings will prevent orders from fully filling.
4. Doing long-only trading can make it difficult to profit in products with high volatility.

## Optimization Direction  

1. Can test adding MACD-like indicators to determine short-term divergences for better entry timing.
2. Can test simplifying filters, keeping only one filter indicator.
3. Can add auto-adjust take profit mechanism, dynamically adjusting subsequent take profit points based on volatility and return rate.
4. Can test allowing short positions, adjusting position proportions based on filters.

## Summary  

The overall strategy is centered around using PMax for entry judgment, and designed multiple filters and take profit methods for optimization, which can yield good returns in trending products. Afterwards, by simplifying filters, optimizing take profit settings, appropriately adjusting position management, the strategy can be optimized to suit more products, achieving even better performance in live trading.

||

## Overview  

The core idea of this strategy is to maximize profits by using moving stop loss tracking, and optimize entry by using filters and take profit methods. The Y shape in the strategy name represents the crossover pattern of the buy and sell signal lines.

## Strategy Logic

This strategy is mainly based on KivancOzbilgic's PMax Explorer strategy with some modifications.  

1. Calculate PMax based on ATR and Moving Average. Generate buy signal when price crosses over PMax.
2. Add T3 indicator and price as filters to ensure entering during an upward trend.
3. Set take profit methods: First use double BAND strategy to determine the first take profit; then use Dice strategy to determine subsequent take profits and stop losses.
4. Use MOST indicator to assist in determining trends, reducing unnecessary reverse operations.

## Advantage Analysis  

1. The PMax strategy itself has the advantage of avoiding chasing high stops, and the moving stop mechanism further helps reduce drawdowns (DD).
2. The double filter ensures that we only enter on upward trends, avoiding false breakouts.
3. Multiple take profit points make profits more flexible.
4. MOST indicator ensures long-only operations, avoiding reverse trading.

## Risk Analysis  

1. PMax itself has some lag, easily missing the first breakout.
2. Too many filter settings could also miss the golden entry point.
3. Overly optimistic take profit settings will prevent orders from fully filling.
4. Doing long-only trading can make it difficult to profit in products with high volatility.

## Optimization Direction  

1. Can test adding MACD-like indicators to determine short-term divergences for better entry timing.
2. Can test simplifying filters, keeping only one filter indicator.
3. Can add auto-adjust take profit mechanism, dynamically adjusting subsequent take profit points based on volatility and return rate.
4. Can test allowing short positions, adjusting position proportions based on filters.

## Summary  

The overall strategy is centered around using PMax for entry judgment, and designed multiple filters and take profit methods for optimization, which can yield good returns in trending products. Afterwards, by simplifying filters, optimizing take profit settings, appropriately adjusting position management, the strategy can be optimized to suit more products, achieving even better performance in live trading.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|-------------------- PMax Settings -------------------|
|v_input_2_hl2|0|Source: hl2|high|low|open|close|hlc3|hlcc4|ohlc4|
|v_input_3|10|ATR Length|
|v_input_4|3|ATR Multiplier|
|v_input_5|0|Moving Average Type: VAR|EMA|WMA|TMA|SMA|WWMA|ZLEMA|TSF|
|v_input_6|13|Moving Average Length|
|v_input_7|false|Filters On/Off|
|v_input_8|false|Filter T3/Src (T3 On/Src Off)|
|v_input_9|true|Change ATR Calculation Method?|
|v_input_10|false|Show Moving Average?|
|v_input_11|true|Show Buy Sell Signals?|
|v_input_12|false|Show Price/Pmax Intersection Signals?|
|v_input_13|false|Cloud On/Off?|
|v_input_14|false|-------------------- T3 Settings --------------------|
|v_input_15|89|T3 Length|
|v_input_16|5|T3 Filter Length|
|v_input_17|0.84|T3 Volume Factor|
|v_input_18|5|Fibo T3 Length|
|v_input_19|0.618|T3 Fibonacci Volume Factor|
|v_input_20|false|Show T3?|
|v_input_21|false|Show T3 Filter?|
|v_input_22|false|T3 Fibonacci Ratio Lines?|
|v_input_23|false|---------------- Take Profit Settings ----------------|
|v_input_24|25|Band Width|
|v_input_25|20|Dominant Cycle Band Width|
|v_input_26|8|Fast Center|
|v_input_27|26|Slow Center|
|v_input_28|0.8|Width|
|v_input_29|false|TP Filter avg2/avg4?|
|v_input_30|false|Count TP Levels and Exit Levels On/Off?|
|v_input_31|false|Early TP On/Off|
|v_input_32|false|------------------- MOST Settings ------------------|
|v_input_33_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_34|8|Length|
|v_input_35|2|Percent|
|v_input_36|0|Moving Average Type: ZLEMA|EMA|
|v_input_37|true|Buy Sell Labels|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-12-04 00:00:00
end: 2023-12-10 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © KivancOzbilgic
// developer: @KivancOzbilgic
// author: @enesyetkin

strategy("Y-Profit Maximizer Strategy with Exit Points", shorttitle="Y-PMax Strategy with Exit Points", overlay=true, default_qty_type=strategy.cash, default_qty_value=10000, initial_capital=10000, currency=currency.USD, commission_value=0.1, commission_type=strategy.commission.percent)
baslik1 = input(title="-------------------- PMax Settings -------------------", defval=false)
src = i