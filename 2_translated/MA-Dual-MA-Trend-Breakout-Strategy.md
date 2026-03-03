> Name

Dual-MA-Trend-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10eb974855f680c012d.png)

## Overview

The Dual-MA Trend Breakout strategy is a quantitative trading strategy that uses two moving averages of different periods to determine the trend and generate entry signals. It mainly judges the overall trend direction through the slow MA, and uses the fast MA for entry filtering. When the direction of the larger timeframe trend is consistent, it selects reversal bars to enter, in order to pursue higher win rate and profitability.

## Strategy Logic

The strategy consists of the following main parts:

**Trend Judgement:** Calculates the 21-period MA, defined as the slow MA. Its position is relatively stable and can be used to judge the overall trend direction. When prices rise close to this MA, it is an upward trend. When prices fall close to this MA, it is a downward trend.

**Entry Filtering:** Calculates the 5-period MA, defined as the fast MA. Only when the price breaks through both the slow MA and the fast MA simultaneously, a trading signal is triggered. This design mainly further filters out false breakouts.

**Candle Filtering:** The strategy only goes long when the current candle is bearish, or goes short when the current candle is bullish. This considers that using reversal bars for entry can obtain higher success rate. It also combines the fast RSI indicator to avoid entering in overbought or oversold areas.

**Pyramiding Filter:** For the crypto market, the strategy additionally includes a tripling volatility breakout condition to capture oversold opportunities in significant downtrends.

**Stop Loss:** The strategy supports moving stop loss. After opening positions, the stop loss will be updated in real-time based on the set percentage.

## Advantage Analysis

The advantages of this strategy include:

1. The dual MA design is simple and practical, easy to understand and master;
2. Reliable trend judgment by combining fast and slow MAs; 
3. Reversal bar entry improves trading win rate;
4. The overall methodology is conservative and stable, suitable for all timeframes;
5. Supports moving stop loss to control risks;
6. Specially considers the characteristics of the crypto market by adding oversold pyramiding opportunities to obtain excess returns.

## Risk Analysis

The strategy also has some risks:

1. During range-bound dual MA periods, there will be multiple small wins and losses.
2. Reversal bar entry may have low win rate in some timeframes.
3. The crypto market has high volatility and high chance of stop loss being triggered.
4. Oversold pyramiding opportunities are not many, with high return volatility.

To address these risks, optimizations can be made in the following aspects:

1. Add more entry conditions to avoid ineffective whipsaws;
2. Adjust timeframe or add other indicators for filtering; 
3. Optimize stop loss algorithms to track near midline;
4. Evaluate actual performance of oversold pyramiding strategies.

## Optimization Directions

The main aspects to optimize this strategy include:

1. **Parameter Optimization**: Systematically backtest to find optimal fast and slow MA period combinations to improve risk-adjusted returns.
2. **Pattern Recognition**: Add other indicators like KDJ, MACD to identify more reliable reversal signals.  
3. **Stop Loss Optimization**: Develop floating or trailing stop loss algorithms to lower chance of being stopped out.
4. **Machine Learning**: Collect and label more historical data to automatically generate trading rules using ML.
5. **Position Sizing**: Dynamically adjust position sizing based on market conditions.

## Conclusion

The Dual-MA Trend Breakout Strategy is generally a simple and practical trend following strategy. Compared to complex machine learning algorithms, this strategy is easier to interpret and master, with higher reliability. With parameter tuning, feature expansion and ML augmentation, this strategy has great potential for improvement and is a great starting point for quantitative trading.

||

## Source (PineScript)

```pinescript
//@version=5
strategy("Dual-MA-Trend-Breakout-Strategy", overlay=true)
long = v_input_1 == true ? "long" : na
short = v_input_2 == true ? "short" : na
stops = v_input_3 == true ? "stops" : na
stop_percent = v_input_4
use_ohlc4 = v_input_5 == true ? true : false
use_fast_ma_filter = v_input_6 == true ? true : false
fast_ma_period = v_input_7
slow_ma_period = v_input_8
bars_q = v_input_9
need_trend_background = v_input_10 == true ? true : false
need_entry_arrows = v_input_11 == true ? true : false
need_extreme = v_input_12 == true ? true : false

// Trend Judgment
slow_ma = ta.sma(close, slow_ma_period)
fast_ma = use_fast_ma_filter ? ta.sma(close, fast_ma_period) : na

long_condition = not need_trend_background or (ta.crossover(close, slow_ma) and close > fast_ma)
short_condition = not need_trend_background or (ta.crossunder(close, slow_ma) and close < fast_ma)

// Entry Filtering
if use_ohlc4
    open_price = na
else
    open_price = close

long_entry = long_condition and ta.crossover(open_price, fast_ma)
short_entry = short_condition and ta.crossunder(open_price, fast_ma)

// Candle Filtering
bullish_candle = (ta.open > ta.close) ? true : false
bearish_candle = (ta.open < ta.close) ? true : false

long_signal = long_entry and bullish_candle
short_signal = short_entry and bearish_candle

// Pyramiding Filter
if need_extreme and strategy.opentrades == 0
    pyramid_long = long_signal and bars_since(ta.lowest(close, bars_q)) > (bars_q / 2)
    pyramid_short = short_signal and bars_since(ta.highest(close, bars_q)) > (bars_q / 2)

// Stop Loss
stop_loss_percent = stop_percent / 100
initial_stop = na
if long_entry or short_entry
    if initial_stop == na
        initial_stop := open_price - (open_price * stop_loss_percent)
strategy.exit("Exit Long", from_entry="Enter Long", limit=initial_stop, comment="Stop Loss")

// Plotting
plotshape(series=long_signal, title="Long Signal", location=location.belowbar, color=color.green, style=shape.labeldown, text="Buy")
plotshape(series=short_signal, title="Short Signal", location=location.abovebar, color=color.red, style=shape.labelup, text="Sell")

// Optional Entry Arrows
if need_entry_arrows and long_entry or short_entry
    plotarrow(series=(long_entry ? 1 : 0), title="Long Arrow", colorup=color.green)
    plotarrow(series=(short_entry ? 1 : 0), title="Short Arrow", colordown=color.red)

```