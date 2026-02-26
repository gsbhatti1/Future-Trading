<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

TGT Falling Buy Strategy Based on Price Decline

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1436fb3f86ec5b8f2ac.png)
[trans]
#### Overview
The main idea of this strategy is to perform buy operations by monitoring the decline in price. When the price falls more than 5% compared to the previous cycle, a buy signal is triggered, purchasing a certain position at the current closing price. When the price is higher than the buy price, the position is closed to take profit. This strategy leverages market volatility, attempting to capture short-term rebound opportunities for profit.

#### Strategy Principle
1. Calculate the percentage drop of the current closing price compared to the previous cycle's closing price.
2. If the drop exceeds 5%, trigger a buy signal to purchase a certain position at the current closing price. The quantity purchased is calculated based on the current account balance and the buy price.
3. Record the buy price and the quantity purchased.
4. Close the position for profit when the current price is higher than the buy price.
5. Calculate the profit or loss and update the account balance.
6. Mark the K-line where the buy signal occurred with a yellow indicator on the chart.

#### Advantages Analysis
1. Simple and Understandable: The strategy logic is clear, making it easy to understand and implement.
2. Trend Capture: By buying assets that have dropped significantly, it can capture short-term price rebound trends.
3. Risk Control: The purchase quantity is calculated based on the account balance and current price, controlling the risk exposure of each trade.
4. Timely Exit: Closing positions promptly when the price rises above the buy price avoids overexposure, managing risk effectively.
5. Intuitive Representation: Buy signals are marked with a distinct color on the chart, facilitating observation and analysis.

#### Risk Analysis
1. Frequent Trading: Targeting short-term fluctuations may result in high trading frequency; attention should be paid to how transaction costs affect profitability.
2. Deep Drawdowns: If prices continue to drop significantly after purchase, there could be considerable drawdown risk.
3. Price Volatility: Since the strategy relies heavily on price volatility, its effectiveness might diminish in markets with low volatility.
4. Profit-Loss Balance: The strategy lacks explicit control over win rates and payoff ratios, necessitating careful monitoring of overall profitability during live execution.

#### Optimization Directions
1. Stop-Loss Enhancement: Currently, no stop-loss mechanism exists post-purchase. Adding features like fixed percentage stops or ATR-based stops can better manage maximum single-trade losses.
2. Signal Filtering: Enhance signal quality by incorporating additional filters such as moving averages, RSI indicators, price inflection points, or candlestick patterns to increase reliability and success rate.
3. Position Management: Instead of using a fixed capital ratio, consider dynamic models adjusting position sizes based on volatility metrics or equity curve behavior.
4. Multi-Instrument Synergy: Apply this concept across multiple instruments, leveraging correlations and diversified fund allocation strategies potentially leading to improved outcomes.

#### Summary
This strategy triggers buys when short-term price drops exceed a specified threshold, aiming to capitalize on rebounds—a straightforward approach. Its strengths include effective trend catching and risk management; however, issues related to frequent trades, potential drawdowns, and dependency on volatility require vigilance. Future improvements could focus on stop-loss mechanisms, enhanced signal validation techniques, adaptive position sizing methods, and cross-instrument coordination efforts to achieve more stable performance.

|| 

#### Overview
The main idea of this strategy is to perform buy operations by monitoring the decline in price. When the price falls more than 5% compared to the previous cycle, a buy signal is triggered, purchasing a certain position at the current closing price. When the price is higher than the buy price, the position is closed to take profit. This strategy leverages market volatility, attempting to capture short-term rebound opportunities for profit.

#### Strategy Principle
1. Calculate the percentage drop of the current closing price compared to the previous cycle's closing price.
2. If the drop exceeds 5%, trigger a buy signal to purchase a certain position at the current closing price. The quantity purchased is calculated based on the current account balance and the buy price.
3. Record the buy price and the quantity purchased.
4. Close the position for profit when the current price is higher than the buy price.
5. Calculate the profit or loss and update the account balance.
6. Mark the K-line where the buy signal occurred with a yellow indicator on the chart.

#### Advantages Analysis
1. Simple and Understandable: The strategy logic is clear, making it easy to understand and implement.
2. Trend Capture: By buying assets that have dropped significantly, it can capture short-term price rebound trends.
3. Risk Control: The purchase quantity is calculated based on the account balance and current price, controlling the risk exposure of each trade.
4. Timely Exit: Closing positions promptly when the price rises above the buy price avoids overexposure, managing risk effectively.
5. Intuitive Representation: Buy signals are marked with a distinct color on the chart, facilitating observation and analysis.

#### Risk Analysis
1. Frequent Trading: Targeting short-term fluctuations may result in high trading frequency; attention should be paid to how transaction costs affect profitability.
2. Deep Drawdowns: If prices continue to drop significantly after purchase, there could be considerable drawdown risk.
3. Price Volatility: Since the strategy relies heavily on price volatility, its effectiveness might diminish in markets with low volatility.
4. Profit-Loss Balance: The strategy lacks explicit control over win rates and payoff ratios, necessitating careful monitoring of overall profitability during live execution.

#### Optimization Directions
1. Stop-Loss Enhancement: Currently, no stop-loss mechanism exists post-purchase. Adding features like fixed percentage stops or ATR-based stops can better manage maximum single-trade losses.
2. Signal Filtering: Enhance signal quality by incorporating additional filters such as moving averages, RSI indicators, price inflection points, or candlestick patterns to increase reliability and success rate.
3. Position Management: Instead of using a fixed capital ratio, consider dynamic models adjusting position sizes based on volatility metrics or equity curve behavior.
4. Multi-Instrument Synergy: Apply this concept across multiple instruments, leveraging correlations and diversified fund allocation strategies potentially leading to improved outcomes.

#### Summary
This strategy triggers buys when short-term price drops exceed a specified threshold, aiming to capitalize on rebounds—a straightforward approach. Its strengths include effective trend catching and risk management; however, issues related to frequent trades, potential drawdowns, and dependency on volatility require vigilance. Future improvements could focus on stop-loss mechanisms, enhanced signal validation techniques, adaptive position sizing methods, and cross-instrument coordination efforts to achieve more stable performance.
[/trans]



> Source (PineScript)

``` pinescript
/*backtest
start: 2023-06-01 00:00:00
end: 2024-06-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Thgoodtrader

//@version=5
strategy("TGT Falling Buy", overlay=true, margin_long=100, margin_short=100)
var float buy_price = na
var float open_price = na
var float open_weekend = na 
var float close_weekend = na 
var bool trade=false
var float balance = 1000
// Define initial buy price and initial quantity
var float qty = na
// Check if the day of the week is Saturday (6) or Sunday (0)
es_sabado = dayofweek == 1
es_domingo = dayofweek == 7
es_viernes = dayofweek == 6

// Calculate the value of the initial balance
balance_initial = balance

change_percent = ((close - close[1]) / close[1]) * 100
is_last_candle_negative = close < open
is_change_above_threshold = change_percent < -5
// Change the color of the last candle if conditions are met
barcolor(is_last_candle_negative and is_change_above_threshold ? color.yellow : na)
bgcolor(is_last_candle_negative and is_change_above_threshold ? color.yellow : na, transp=80)
// Save the buy price when the 5% condition is met
if is_change_above_threshold 
    // Calculate the quantity based on the buy price and balance
    qty := balance / close
    // Save the buy price
    buy_price := close
    open_price := open
    strategy.entry("Buy Trading",strategy.long,qty)
    alert("Buy BTC", alert.freq_once_per_bar_close)
    trade :=true
//if (((close - strategy.position_avg_price) / strategy.position_avg_price) * 100 ) > 2
if close > strategy.position_avg_price
    // Calculate the profit or loss value
    pnl = (close - strategy.position_avg_price) * qty
    // Update the balance
    balance := balance_initial + pnl
    strategy.close("Buy Trading")
alertcondition(is_change_above_threshold, title = "Buy 5% Discount", message = "Buy Position")
alertcondition(close > strategy.position_avg_price, title = "Close Trade", message = "Close Buy Position")   
```

> Detail

https://www.fmz.com/strategy/453656

> Last Modified

2024-06-07 15:33:26