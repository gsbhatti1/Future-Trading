> Name

Williams-R-Dynamic-TP-SL-Adjustment-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/693ea875fea3e9b203.png)
[trans]
#### Overview
This strategy is based on the Williams %R indicator and optimizes trading performance by dynamically adjusting take profit and stop loss levels. Buy signals are generated when the Williams %R crosses above the oversold area (-80), and sell signals are generated when it crosses below the overbought area (-20). An Exponential Moving Average (EMA) is used to smooth the Williams %R values and reduce noise. The strategy offers flexible parameter settings, including indicator periods, take profit/stop loss (TP/SL) levels, trading hours, and trade direction choices, to adapt to different market conditions and trader preferences.

#### Strategy Principles
1. Calculate the Williams %R indicator value for a given period.
2. Calculate the Exponential Moving Average (EMA) of the Williams %R.
3. When the Williams %R crosses above the -80 level from below, it triggers a buy signal; when it crosses below the -20 level from above, it triggers a sell signal.
4. After a buy entry, set take profit and stop loss levels. The trade is closed when the TP/SL price levels are reached or when the Williams %R triggers a reverse signal.
5. After a sell entry, set take profit and stop loss levels. The trade is closed when the TP/SL price levels are reached or when the Williams %R triggers a reverse signal.
6. Optionally, trade within a specified time range (e.g., 9:00-11:00) and choose whether to trade near the top of the hour (X minutes before to Y minutes after).
7. Optionally, choose the trade direction as long only, short only, or both.

#### Advantages Analysis
1. Dynamic TP/SL: Dynamically adjust take profit and stop loss levels based on user settings, which can better protect profits and control risks.
2. Flexible parameters: Users can set various parameters according to their preferences, such as indicator periods, TP/SL levels, trading hours, etc., to adapt to different market conditions.
3. Smoothed indicator: Introducing EMA to smooth Williams %R values can effectively reduce indicator noise and improve signal reliability.
4. Restricted trading time: Optionally trade within a specific time range to avoid highly volatile market periods and reduce risk.
5. Customizable trade direction: Choose to go long only, short only, or trade in both directions based on market trends and personal judgment.

#### Risk Analysis
1. Improper parameter settings: If the TP/SL settings are too loose or too strict, it may lead to profit loss or frequent stop-outs.
2. Trend identification errors: The Williams %R indicator performs poorly in choppy markets and may generate false signals.
3. Limited effect of time restrictions: Limiting trading time may cause the strategy to miss some good trading opportunities.
4. Over-optimization: Over-optimizing parameters may lead to poor strategy performance in future actual trading.

#### Optimization Directions
1. Combine with other indicators: Such as trend indicators, volatility indicators, etc., to improve the accuracy of signal confirmation.
2. Dynamic parameter optimization: Adjust parameters in real-time according to market conditions, such as using different parameter settings in trending and ranging markets.
3. Improve TP/SL methods: Such as using trailing stop loss, partial profit-taking, etc., to better protect profits and control risks.
4. Incorporate money management: Dynamically adjust the position size of each trade based on account balance and risk preferences.

#### Summary
The Williams %R Dynamic TP/SL Adjustment Strategy captures overbought and oversold price conditions in a simple and effective way while providing flexible parameter settings to adapt to different market environments and trading styles. The strategy dynamically adjusts take profit and stop loss levels, which can better control risks and protect profits. However, when applying the strategy in practice, attention should still be paid to factors such as parameter settings, signal confirmation, and trading time selection to further improve the robustness and profitability of the strategy.

||

#### Source (PineScript)

```pinescript
// backtest
// start: 2024-05-01 00:00:00
// end: 2024-05-31 23:59:59
// period: 4h
// basePeriod: 15m
// exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]

//@version=5
strategy("Williams %R Strategy defined buy/sell criteria with TP / SL", overlay=true)

// User inputs for TP and SL levels
tp_level = input.int(defval=60, title="Take Profit")
sl_level = input.int(defval=20, title="Stop Loss")
period = input.int(defval=14, title="Williams %R Period")
time_range_start = input.time([9*60*60], title="Start Time (UTC)", confirm=false)
time_range_end = input.time([11*60*60], title="End Time (UTC)", confirm=false)

// Calculate Williams %R
williams_r = ta.willr(period)
ema_williams_r = ta.ema(williams_r, 9)

// Buy and Sell Logic
if time >= time_range_start and time <= time_range_end
    if ema_williams_r > -80 and ta.crossover(ema_williams_r, -80) 
        strategy.entry("Buy", strategy.long)
    if ema_williams_r < -20 and ta.crossunder(ema_williams_r, -20) 
        strategy.close("Buy")

    // Set Take Profit and Stop Loss
    tp_price = strategy.position_avg_cost + (strategy.position_avg_price * tp_level / 100)
    sl_price = strategy.position_avg_cost - (strategy.position_avg_price * sl_level / 100)

    if ta.crossover(ema_williams_r, -80) 
        strategy.exit("TP/SL", "Buy", limit=tp_price, stop=sl_price)

// Additional Settings
if time < time_range_start or time > time_range_end
    strategy.close("Buy")
```
[/trans]