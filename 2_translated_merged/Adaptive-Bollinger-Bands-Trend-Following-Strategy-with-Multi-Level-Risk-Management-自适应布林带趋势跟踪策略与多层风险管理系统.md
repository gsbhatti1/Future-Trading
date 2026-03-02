> Name

Adaptive-Bollinger-Bands-Trend-Following-Strategy-with-Multi-Level-Risk-Management-自适应布林带趋势跟踪策略与多层风险管理系统

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1755a2f0b908a58b2f3.png)

[trans]
#### Overview
This strategy is a trend-following system that combines Bollinger Bands and EMA indicators with a multi-layer risk control mechanism to optimize trading performance. The core strategy utilizes Bollinger Bands breakout-reversion patterns to capture market trends while incorporating an EMA trend filter to enhance trading accuracy. The system includes a comprehensive risk management framework with trailing stops, fixed stop losses, profit targets, and time-based position closure.

#### Strategy Principles
The trading logic is based on the following core elements:
1. Uses Bollinger Bands with 1.5 standard deviation and 14-period length as the primary trading signal indicator
2. Triggers short signals when the previous candle closes above the upper band and current candle reverses
3. Triggers long signals when the previous candle closes below the lower band and current candle turns bullish
4. Optionally applies an 80-period EMA as a trend filter, only entering positions when trend direction aligns
5. Activates trailing stops when price crosses the Bollinger Bands middle line
6. Allows setting fixed stop loss and take profit amounts
7. Supports automatic position closure based on bar count

#### Strategy Advantages
1. Combines trend-following and reversal trading characteristics for stable performance across different market conditions
2. Multi-layered risk control system provides comprehensive money management
3. Flexible parameter settings allow strategy adaptation to different market conditions
4. EMA filter effectively reduces false breakout risks
5. Trailing stop mechanism effectively locks in profits
6. Time-dimensional closure mechanism prevents long-term position trapping

#### Strategy Risks
1. May generate frequent false breakout signals in ranging markets
2. Fixed monetary stop losses may not suit all market conditions
3. EMA filtering might cause missing important trading opportunities
4. Trailing stops may close positions prematurely in highly volatile markets
5. Parameter optimization may lead to overfitting historical data

#### Strategy Optimization Directions
1. Introduce adaptive Bollinger Bands periods based on market volatility
2. Develop dynamic stop-loss system based on money management
3. Add volume analysis to confirm breakout validity
4. Implement intelligent parameter optimization system
5. Add market environment recognition module for different parameter settings in different market conditions

#### Summary
This is a well-designed trend-following system that provides reliable trading signals through the combination of Bollinger Bands and EMA, while ensuring trading safety through multi-layered risk control. The strategy offers strong configurability to adapt to different trading styles and market environments. While there are some inherent risks, the suggested optimization directions can further enhance the strategy's stability and profitability.

``` pinescript
/*backtest
start: 2025-01-10 00:00:00
end: 2025-02-08 08:00:00
period: 2h
basePeriod: 2h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("AI Bollinger Bands Strategy with SL, TP, and Bars Till Close", overlay=true)

// Input parameters
bb_length           = input.int(14, title="Bollinger Bands Length", minval=1)
bb_stddev           = input.float(1.5, title="Bollinger Bands Standard Deviation", minval=0.1)
use_ema             = input.bool(true, title="Use EMA Filter")
ema_length          = input.int(80, title="EMA Length", minval=1)
use_trailing_stop   = input.bool(true, title="Use Trailing Stop")
use_sl              = input.bool(true, title="Use Stop Loss")
use_tp              = input.bool(false, title="Use Take Profit")
sl_dollars          = input.float(300.0, title="Stop Loss (\$)", minval=0.0)
tp_dollars          = input.float(1000.0, title="Take Profit (\$)", minval=0.0)
use_bars_till_close = input.bool(true, title="Use Bars Till Close")
bars_till_close     = input.int(10, title="Bars Till Close", minval=1)
// New input to toggle indicator plotting
plot_indicators     = input.bool(true, title="Plot Bollinger Bands and EMA on Chart")

// Calculate Bollinger Bands and EMA
basis      = ta.sma(close, bb_length)
upper_band = basis + bb_stddev * ta.stdev(close, bb_length)
lower_band = basis - bb_stddev * ta.stdev(close, bb_length)
ema        = ta.ema(close, ema_length)

// Plot Bollinger Bands and EMA conditionally
plot(plot_indicators  ? basis : na, color=color.blue, linewidth=2, title="Basis (SMA)")
plot(plot_indicators ? upper_band : na, color=color.red, linewidth=2, title="Upper Band")
plot(plot_indicators  ? lower_band : na, color=color.green, linewidth=2, title="Lower Band")
plot(plot_indicators ? ema : na, color=color.orange, linewidth=2, title="EMA")

// Trading logic
short_signal = ta.crossover(close[1], upper_band) and not ta.is_empty(ta.crossover(close, lower_band))
long_signal  = ta.crossunder(close[1], lower_band) and not ta.is_empty(ta.crossunder(close, upper_band))

if (use_ema)
    if (ta.trend.up(basis, ema_length))
        short_signal := false
    elif (ta.trend.down(basis, ema_length))
        long_signal := false

// Trailing stop mechanism
trail_price = na
if (strategy.opentrades > 0 and use_trailing_stop)
    if strategy.position_avg_price < close
        trail_price := math.min(trail_price, close - sl_dollars * (1 + ta.rma(close / strategy.position_avg_price, 2)))
    else
        trail_price := math.max(trail_price, close + sl_dollars * (1 + ta.rma(strategy.position_avg_price / close, 2)))

if not na(trail_price)
    if use_sl and (strategy.opentrades > 0) and (strategy.position_avg_price - close < -sl_dollars)
        strategy.close_all()
    else
        strategy.exit("Trailing Stop", from_entry="Enter Long/Short", limit=trail_price)

// Optional take profit implementation
if (use_tp and use_sl and (strategy.opentrades > 0))
    if (strategy.position_avg_price + tp_dollars < close)
        strategy.close_all()

// Automatic position closure based on bar count
if use_bars_till_close
    for i = 1 to bars_till_close
        if i == ta.barssince(ta.crossover(close, upper_band)) or i == ta.barssince(ta.crossunder(close, lower_band))
            strategy.close("Bars Till Close")

```