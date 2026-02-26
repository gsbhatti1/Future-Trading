> Name

Ichimoku-Backtester-with-TP-SL-and-Cloud-Confirmation

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c483369670e6628319.png)
[trans]

### Overview

This is a trend-following strategy based on the Ichimoku cloud. It combines moving averages, the Ichimoku cloud, and precise entry/exit mechanisms to improve profitability.

### Strategy Principle

The core of this strategy involves constructing the Ichimoku components using user-defined input parameters—Tenkan-Sen, Kijun-Sen, Senkou Span A & B, and Chikou Span. It identifies bullish (long) signals when price breaks above these equilibrium lines and bearish (short) signals when it breaks below them. Stop loss and take profit levels are set to manage risk and reward.

Additionally, this strategy includes a cloud confirmation mechanism based on the color of the Ichimoku cloud. Only long positions are taken when the Ichimoku cloud is green, and only short positions when it is red. This can help filter out false signals and improve the probability of profitable trades.

### Advantages

The main advantage of this strategy lies in combining the benefits of moving averages and the Ichimoku cloud. It considers both the overall trend from price averages and the recent changes in closing prices for the last trading session. The cloud confirmation mechanism also helps avoid false signals, thereby increasing the stability of the strategy.

In terms of parameter optimization, the stop loss and take profit settings make this strategy risk-manageable. Furthermore, as a relatively new technical indicator, its familiarity is low among traders, giving it an early adoption advantage.

### Risks

However, there are also key risks to consider:

1. The Ichimoku cloud can be volatile in range-bound markets without clear trends, leading to frequent stop loss hits.
2. The cloud acts as a lagging indicator; by the time confirmation occurs, much of the move may have already happened.
3. Optimizing stop loss and take profit levels is challenging and sensitive, with suboptimal parameters potentially resulting in more losses.

### Optimization Directions

This strategy can be further optimized through the following methods:

1. Optimize the length parameter for Tenkan-Sen to find the best balance point.
2. Test different combinations of stop loss and take profit settings to determine the optimal parameters.
3. Integrate additional technical indicators such as MACD or RSI for consensus-based entry decisions.
4. Backtest across different asset classes and timeframes to identify the best setup scenarios.
5. Consider incorporating machine learning models to dynamically optimize parameters and adapt the strategy.

### Conclusion

This strategy integrates the advantages of moving averages and Ichimoku clouds, setting reasonable stop loss and take profit levels while adding a cloud confirmation mechanism to effectively track trends and control risks. It can be widely applied to indices, foreign exchange, commodities, and cryptocurrencies, making it a recommended quant trading strategy.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|9|Tenkan-Sen Bars|
|v_input_2|26|Kijun-Sen Bars|
|v_input_3|52|Senkou-Span B Bars|
|v_input_4|26|Chikou-Span Offset|
|v_input_5|26|Senkou-Span Offset|
|v_input_6|true|Long Entry|
|v_input_7|true|Short Entry|
|v_input_8|true|Wait for Cloud Confirmation|
|v_input_9|true|Use Short Stop Loss|
|v_input_10|5|Short Stop Loss (%)|
|v_input_11|true|Use Long Stop Loss|
|v_input_12|5|Long Stop Loss (%)|
|v_input_13|true|Use Short Take Profit|
|v_input_14|20|Short Take Profit (%)|
|v_input_15|true|Use Long Take Profit|
|v_input_16|20|Long Take Profit (%)|
|v_input_17|false|Show Date Range|
|v_input_18|true|From Month|
|v_input_19|true|From Day|
|v_input_20|2020|From Year|
|v_input_21|true|Thru Month|
|v_input_22|true|Thru Day|
|v_input_23|2112|Thru Year|

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-17 00:00:00
end: 2023-11-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

strategy("Ichimoku Backtester with TP and SL", overlay=true, 
     currency = currency.USD, default_qty_type = strategy.percent_of_equity, 
     default_qty_value = 95)
//@version=4

//Inputs
ts_bars = input(9, minval=1, title="Tenkan-Sen Bars")
ks_bars = input(26, minval=1, title="Kijun-Sen Bars")
ssb_bars = input(52, minval=1, title="Senkou-Span B Bars")
cs_offset = input(26, minval=1, title="Chikou-Span Offset")
ss_offset = input(26, minval=1, title="Senkou-Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

wait_for_cloud = input(true, title="Wait for Cloud Confirmation")

use_short_stop_loss = input(true, title="Use Short Stop Loss")
short_stop_loss = input(title="Short Stop Loss (%)", type=input.float, minval=0.0, step=0.1, 
     defval=5) * 0.01
use_long_stop_loss = input(true, title="Use Long Stop Loss")
long_stop_loss = input(title="Long Stop Loss (%)", type=input.float, minval=0.0, step=0.1, 
     defval=5) * 0.01
     
use_short_take_profit = input(true, title="Use Short Take Profit")
short_take_profit = input(title="Short Take Profit (%)", type=input.float, minval=0.0, step=0.1,
     defval = 20) * .01
use_long_take_profit = input(true, title="Use Long Take Profit")
long_take_profit = input(title="Long Take Profit (%)", type=input.float, minval=0.0, step=0.1,
     defval = 20) * .01

// === INPUTS END ===
```