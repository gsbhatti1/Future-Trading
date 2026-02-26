> Name

Ichimoku-Trading-Strategy-With-Money-Management

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/14ae8911455f5025f3a.png)
[trans]

### Overview

This is a long-only stock trading strategy based on the Ichimoku Kinko Hyo indicator. The strategy utilizes the basic principles of Ichimoku to determine entry and exit opportunities.

### Strategy Logic

The strategy first calculates the components of Ichimoku, including Tenkan-Sen, Kijun-Sen, Senkou Span A, and Senkou Span B.

Long entry if the following conditions are met:
- Tenkan crosses above Kijun, indicating a short-term MA cross above a long-term MA, which is a golden cross signal
- Price is above the cloud (Kumo), indicating support for the price and a potential upward trend
- Future cloud is red, indicating an upward future trend
- Price distance from Tenkan < 2 x ATR, indicating that the price is not overextended for a chase strategy
- Price distance from Kijun < 3 x ATR, indicating that the price is not overextended for a chase strategy
- Both Tenkan and Kijun are above the cloud, indicating an upward Ichimoku trend

Exit if the following conditions are met:
- Tenkan crosses below Kijun, indicating a dead cross
- Price breaks below the cloud, indicating loss of support
- Profit > 30%, implementing a profit-taking strategy
- Loss > 3%, implementing a stop-loss strategy

### Advantage Analysis

- Utilizing Ichimoku to determine price trends with high accuracy
- Incorporating ATR to control chasing and avoid overbought or oversold conditions
- Filtering signals through multiple confirmations, avoiding false signals
- Adding-on strategies can accelerate profits

### Risk Analysis

- Ichimoku signals may be lagging, requiring confirmation from other indicators
- Incorrect ATR parameter settings can lead to overbought or oversold conditions
- Add-on strategies may increase the risk of losses
- Manual tuning of parameters is required for different stocks

### Optimization Directions

- Incorporating other indicators like MACD and KDJ for signal confirmation
- Increasing profit-taking levels while decreasing stop-loss levels
- Automatically optimizing ATR parameters based on historical data
- Researching parameter differences for various sectors to build a parameter pool

### Summary

This is a highly practical stock trading strategy that uses Ichimoku to determine trends, ATR to manage risks, and a chasing-stop loss method to generate profits. The advantages are clear, and further optimizations in parameters and combining indicators will make it even better for live trading.

||

### Overview

This is an Ichimoku Kinko Hyo indicator-based long-only stock trading strategy. The strategy utilizes the basic principles of Ichimoku to determine entries and exits.

### Strategy Logic

The strategy first calculates the components of Ichimoku, including Tenkan-Sen, Kijun-Sen, Senkou Span A, and Senkou Span B.

Long entry if the following conditions are met:
- Tenkan crosses above Kijun, indicating a short-term MA cross above a long-term MA, which is a golden cross signal
- Price is above the cloud (Kumo), indicating support for the price and a potential upward trend
- Future cloud is red, indicating an upward future trend
- Price distance from Tenkan < 2 x ATR, indicating that the price is not overextended for a chase strategy
- Price distance from Kijun < 3 x ATR, indicating that the price is not overextended for a chase strategy
- Both Tenkan and Kijun are above the cloud, indicating an upward Ichimoku trend

Exit if the following conditions are met:
- Tenkan crosses below Kijun, indicating a dead cross
- Price breaks below the cloud, indicating loss of support
- Profit > 30%, implementing a profit-taking strategy
- Loss > 3%, implementing a stop-loss strategy

### Advantage Analysis 

- Utilize Ichimoku to determine price trend with high accuracy
- Incorporate ATR to control chasing and avoid overbought or oversold conditions
- Filter signals with multiple confirmations, avoiding false signals
- Add-on strategy could accelerate profit

### Risk Analysis

- Ichimoku signals could lag, requiring confirmations from other indicators
- Wrong ATR parameters could lead to overbought or oversold conditions
- Add-on strategy could increase loss risk  
- Parameters need to be tuned manually for different stocks

### Optimization Directions

- Incorporate other indicators like MACD, KDJ for signal confirmation
- Increase profit-taking level, decrease stop-loss level
- Auto tune ATR parameters based on historical data
- Research parameter differences for various sectors, build parameter pool

### Summary

This is a very practical stock trading strategy that utilizes Ichimoku to determine trends and ATR to manage risks. The strategy profits from chasing while having a stop-loss mechanism in place. Its advantages are evident, and further optimizations on parameters and combining indicators would make it even better for live trading.

||

> Strategy Arguments


| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_int_1 | 9 | Tenkan-Sen Period |
| v_input_int_2 | 26 | Kijun-Sen Period |
| v_input_int_3 | 52 | Senkou-Span B Period |
| v_input_int_4 | 26 | Chikou-Span Offset |
| v_input_int_5 | 26 | Senkou-Span Offset |
| v_input_int_6 | true | Start Date |
| v_input_int_7 | true | Start Month |
| v_input_int_8 | 1980 | Start Year |
| v_input_int_9 | true | En Date |
| v_input_int_10 | true | End Month |
| v_input_int_11 | 2100 | End Year |

> Source (PineScript)

```pinescript
/*backtest
start: 2022-12-05 00:00:00
end: 2023-12-11 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Author Obarut
//@version=5
strategy("İchimoku Strategy With Money Management",overlay=true)

//Inputs
ts_period = input.int(9, minval=1, title="Tenkan-Sen Period")
ks_period = input.int(26, minval=1, title="Kijun-Sen Period")
ssb_period = input.int(52, minval=1, title="Senkou-Span B Period")
cs_offset = input.int(26, minval=1, title="Chikou-Span Offset")
ss_offset = input.int(26, minval=1, title="Senkou-Span Offset")


// Back Testing Period

fromday = input.int(defval=1,title="Start Date",minval=1,maxval=31) 
frommonth = input.int(defval=1,title="Start Month",minval=1,maxval=12)
fromyear = input.int(defval=1980,title="Start Year",minval=1800, maxval=2100)
today = input.int(defval=1,title="En Date",minval=1,maxval=31)
tomonth = input.int(defval=1,title="End Month",minval=1,maxval=12)
toyear =input.int(defval=2100,title="End Year",minval=1800,maxval=2200)


start=timestamp(fromyear,frommonth,fromday,00,00)
finish=timestamp(toyear,tomonth,today,00,00)
timewindow= time>=start and time<=finish

middle(len) => math.avg(ta.lowest(len), ta.highest(len))

// Ichimoku Components

tenkan = middle(ts_period)
kijun = middle(ks_period)
senkouA = math.avg(tenkan, kijun)
senkouB = middle(ssb_period)


atr = ta.atr(14)
ss_above = math.max(senkouA[ss_offset-1], senkouB[ss_offset-1])
ss_below = math.min(senkouA[ss_offset-1], senkouB[ss_offset-1])

// Price Distance From Tenkan

distance = close - tenkan

// Price Distance from Kijun

distancek = close - kijun

// Entry/Exit Signals

tk_cross_kijun_bull = tenkan >= kijun
tk_cross_kijun_bear = tenkan <= kijun
cs_cross_bull = ta.mom(close, cs_offset-1) > 0
cs_cross_bear = ta.mom(close, cs_offset-1) < 0
future_kumo_bull = senkouA > senkouB
future_kumo_bear = senkouA < senkouB

// Price Distance From Tenkan
disbull = distance < 2*atr
//Price Distance From Kijun
disbullk = distancek < 3*atr
//Price A