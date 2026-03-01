> Name

Dual-Breakthrough-Strategy Based on Candlesticks

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/133e58ba984f14c0c26.png)
[trans]

## Overview
This is a dual-breakthrough trading strategy based on candlesticks. It generates trading signals when the closing price of the current candlestick breaks through both the highest and lowest prices of the previous two candlesticks.

## Strategy Principle  
The basic logic of the strategy is:  

1. Define bull signal: `bull = close > open and close > math.max(close[2], open[2]) and low[1] < low[2] and high[1] < high[2]`. That is, the closing price of the current candlestick is greater than the opening price, and greater than the highest price of the previous two candlesticks, while the lowest price of the current candlestick is lower than the lowest price of the previous candlestick.  

2. Define bear signal: `bear = close < open and close < math.min(close[2], open[2]) and low[1] > low[2] and high[1] > high[2]`. That is, the closing price of the current candlestick is less than the opening price, and less than the lowest price of the previous two candlesticks, while the highest price of the current candlestick is higher than the highest price of the previous candlestick.  

3. When a bull signal is triggered, go long; when a bear signal is triggered, go short.  

4. Stop loss and take profit can be set.

The strategy utilizes the characteristics of dual breakthroughs to judge changes in trends through breaches of key price zones, thereby generating trading signals.

## Advantage Analysis
This is a relatively simple and intuitive breakout strategy with the following advantages:  

1. The logic is clear and easy to understand and implement, with a low barrier to entry.  

2. Breakouts are common trading signals that tend to form trends easily.  

3. Going both long and short allows for dual directional trading, increasing profit opportunities.  

4. Flexible stop loss and take profit settings help control risk.

## Risk Analysis 
The strategy also carries some risks:

1. Dual directional trading carries higher risks and requires close monitoring.  

2. Breakouts can be vulnerable to traps, potentially forming false signals.  

3. Improper parameter settings may lead to overtrading. 

4. Improper stop loss and take profit settings can also affect profit potential.

Risks can be reduced by optimizing parameters and appropriately filtering products.

## Optimization Directions
The strategy can be optimized in the following aspects:  

1. Optimize parameters like breakout cycle, stop loss/take profit range etc.  

2. Add filtering conditions to avoid errors from arbitrage, sideways movements etc.  

3. Incorporate trend indicators to avoid consolidation ranges. 
  
4. Optimize capital management, improve position algorithms.
  
5. Different parameters for different products, test and optimize separately.

## Summary  
This is a simple strategy based on the dual breakout concept. It has the advantage of clear logic and easy implementation, but also carries certain monitoring risks. Better strategy results can be expected through parameter and condition optimization.

||

## Overview
This is a dual breakthrough trading strategy based on candlesticks. It will generate trading signals when the closing price of the current K-line has a breakthrough relative to the highest and lowest prices of the previous two K-lines.

## Strategy Principle  
The basic logic of the strategy is:  

1. Define bull signal: `bull = close > open and close > math.max(close[2], open[2]) and low[1] < low[2] and high[1] < high[2]`. That is, the closing price of the current K-line is greater than the opening price, and greater than the highest price of the previous two K-lines, while the lowest price of the current K-line is lower than the lowest price of the previous K-line.  

2. Define bear signal: `bear = close < open and close < math.min(close[2], open[2]) and low[1] > low[2] and high[1] > high[2]`. That is, the closing price of the current K-line is less than the opening price, and less than the lowest price of the previous two K-lines, while the highest price of the current K-line is higher than the highest price of the previous K-line.  

3. When a bull signal is triggered, go long; when a bear signal is triggered, go short.  

4. Stop loss and take profit can be set.

The strategy utilizes the characteristics of dual breakthroughs to judge changes in trends through breaches of key price zones, thereby generating trading signals.

## Advantage Analysis
This is a relatively simple and intuitive breakout strategy with the following advantages:  

1. The logic is clear and easy to understand and implement, with a low barrier to entry.  

2. Breakouts are common trading signals that tend to form trends easily.  

3. Going both long and short allows for dual directional trading, increasing profit opportunities.  

4. Flexible stop loss and take profit settings help control risk.

## Risk Analysis 
The strategy also carries some risks:

1. Dual directional trading carries higher risks and requires close monitoring.  

2. Breakouts can be vulnerable to traps, potentially forming false signals.  

3. Improper parameter settings may lead to overtrading. 

4. Improper stop loss and take profit settings can also affect profit potential.

Risks can be reduced by optimizing parameters and appropriately filtering products.

## Optimization Directions
The strategy can be optimized in the following aspects:  

1. Optimize parameters like breakout cycle, stop loss/take profit range etc.  

2. Add filtering conditions to avoid errors from arbitrage, sideways movements etc.  

3. Incorporate trend indicators to avoid consolidation ranges. 
  
4. Optimize capital management, improve position algorithms.
  
5. Different parameters for different products, test and optimize separately.

## Summary  
This is a simple strategy based on the dual breakout concept. It has the advantage of clear logic and easy implementation, but also carries certain monitoring risks. Better strategy results can be expected through parameter and condition optimization.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|true|(?Debug)Show Alerts Debug Label?|
|v_input_string_1|0|(?Automation)Use Demo or Live Broker: DEMO|LIVE|
|v_input_string_2|0|Broker Name: Tradovate|AscendEX|Binance|Binance Futures|Binance US|Binance Delivery|Kraken|Deribit|Poloniex|Okcoin|Bitfinex|Oanda|Kucoin|Okex|Bybit|FTX|Bitmex|Alpaca|Gemini|
|v_input_bool_2|true|Enable trades?|
|v_input_string_3|*|Account Name|
|v_input_string_4|btcusd_perp|Symbol Name|
|v_input_int_1|2|Nb Contracts|
|v_input_bool_3|false|Use Delay between orders|
|v_input_int_2|true|Delay in seconds|
|v_input_bool_4|false|(?Binance Automation)Use Borrow/Repay Mode?|
|v_input_string_5|BTC|Asset to Borrow/Repay|
|v_input_float_1|true|Quantity of assets to borrow?|
|v_input_1|false|(?Date)Date Range Filtering|
|v_input_2|timestamp(01 Jan 2019 13:30 +0000)|Start Time|
|v_input_3|timestamp(30 Dec 2021 23:30 +0000)|End Time|
|v_input_string_6|0|(?Stop Loss)Select Stop Loss Mode: None|Percent|Price|
|v_input_float_2|3|(?Stop Loss %)Stop Loss (%)|
|v_input_float_3|30|(?Stop Loss USD)Stop Loss (USD)|
|v_input_string_7|0|(?Take Profit)Select Take Profit Mode: None|Percent|Price|
|v_input_float_4|3|(?Take Profit %)Take Profit (%)|
|v_input_float_5|30|(?Take Profit USD)Take Profit (USD)|

> Source (PineScript)

```pinescript
//@version=5
// # ========================================================================= #
// #                   |   Strategy  |
// # ========================================================================= #

SystemName = "Strategy Temp"
```