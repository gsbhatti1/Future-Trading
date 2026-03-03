> Name

SR-突破策略-SR-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11747ab4f0b0f935ba8.png)

[trans]
#### Overview
The SR Breakout Strategy is a trading strategy developed based on the breakout finder indicator by LonesomeTheBlue. The main idea of this strategy is to generate long or short signals by determining whether the closing price breaks through support or resistance levels. The default settings are based on 8-hour candlesticks, but better parameters exist for the 4-hour chart. This strategy uses pivothigh and pivotlow functions to identify support and resistance levels and employs high and low prices to determine breakouts. Additionally, this strategy includes stop loss and take profit mechanisms.

#### Strategy Principle
1. Use the pivothigh and pivotlow functions to calculate the highest and lowest points over a specific period and store them in arrays.
2. Determine if the current closing price is higher than the resistance level; if so, it's considered a bullish breakout, generating a long signal.
3. Determine if the current closing price is lower than the support level; if so, it's considered a bearish breakout, generating a short signal.
4. After generating a trading signal, calculate stop loss and take profit prices based on predefined ratios, setting corresponding orders for both stop loss and take profit.
5. Plot the breakout range according to the direction of the breakout.

#### Strategy Advantages
1. Support and resistance breakouts are classic strategies with proven practical applications.
2. Using pivothigh and pivotlow functions allows relatively accurate identification of breakout opportunities.
3. The code structure is clear, making it easy for backtesting and optimization by storing highs and lows in arrays.
4. Stop loss and take profit mechanisms help manage risks effectively.

#### Strategy Risks
1. Support and resistance breakouts perform poorly in choppy markets, often leading to frequent false breakouts.
2. Fixed stop loss and take profit ratios may not suit all market conditions, potentially skewing risk-reward ratios.
3. This strategy focuses only on price factors without considering other important indicators like volume, possibly missing significant signals.

#### Strategy Optimization Directions
1. Introduce additional technical indicators such as volume or MACD to enhance signal accuracy and reliability.
2. Use trailing stop losses or dynamic stop loss and take profit percentages for better adaptability to market conditions.
3. Implement filtering criteria like trend filters or volatility filters to reduce false breakouts in choppy markets.
4. Optimize support and resistance levels by using adaptive periods, Fibonacci levels, etc.

#### Summary
The SR Breakout Strategy is based on the classical idea of support and resistance breakout. By employing pivothigh and pivotlow functions to identify these levels and generate trading signals when prices break through them. The advantage lies in its clear structure and ease of implementation and optimization; however, it faces challenges like poor performance in choppy markets and fixed stop loss/take profit ratios that may not suit all scenarios. Future improvements can be made by incorporating technical indicators, flexible stop losses/takes profits, filtering criteria, and better support/resistance optimizations to enhance stability and profitability.

||

#### Overview
The SR Breakout Strategy is a trading strategy developed based on the breakout finder indicator by LonesomeTheBlue. The main idea of this strategy is to generate long or short signals by determining whether the closing price breaks through support or resistance levels. Default settings are based on 8-hour candlesticks, but better parameters exist for the 4-hour chart. This strategy uses pivothigh and pivotlow functions to identify support and resistance levels and employs high and low prices to determine breakouts. Additionally, this strategy includes stop loss and take profit mechanisms.

#### Strategy Principle
1. Use the `pivothigh` and `pivotlow` functions to calculate the highest and lowest points over a specific period and store them in arrays.
2. Determine if the current closing price is higher than the resistance level; if so, it's considered a bullish breakout, generating a long signal.
3. Determine if the current closing price is lower than the support level; if so, it's considered a bearish breakout, generating a short signal.
4. After generating a trading signal, calculate stop loss and take profit prices based on predefined ratios, setting corresponding orders for both stop loss and take profit.
5. Plot the breakout range according to the direction of the breakout.

#### Strategy Advantages
1. Support and resistance breakouts are classic strategies with proven practical applications.
2. Using `pivothigh` and `pivotlow` functions allows relatively accurate identification of breakout opportunities.
3. The code structure is clear, making it easy for backtesting and optimization by storing highs and lows in arrays.
4. Stop loss and take profit mechanisms help manage risks effectively.

#### Strategy Risks
1. Support and resistance breakouts perform poorly in choppy markets, often leading to frequent false breakouts.
2. Fixed stop loss and take profit ratios may not suit all market conditions, potentially skewing risk-reward ratios.
3. This strategy focuses only on price factors without considering other important indicators like volume, possibly missing significant signals.

#### Strategy Optimization Directions
1. Introduce additional technical indicators such as volume or MACD to enhance signal accuracy and reliability.
2. Use trailing stop losses or dynamic stop loss and take profit percentages for better adaptability to market conditions.
3. Implement filtering criteria like trend filters or volatility filters to reduce false breakouts in choppy markets.
4. Optimize support and resistance levels by using adaptive periods, Fibonacci levels, etc.

#### Summary
The SR Breakout Strategy is based on the classical idea of support and resistance breakout. By employing `pivothigh` and `pivotlow` functions to identify these levels and generate trading signals when prices break through them. The advantage lies in its clear structure and ease of implementation and optimization; however, it faces challenges like poor performance in choppy markets and fixed stop loss/take profit ratios that may not suit all scenarios. Future improvements can be made by incorporating technical indicators, flexible stop losses/takes profits, filtering criteria, and better support/resistance optimizations to enhance stability and profitability.

``` pinescript
/*backtest
start: 2024-05-07 00:00:00
end: 2024-05-14 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © LonesomeTheBlue © chanu_lev10k

//@version=5
strategy('SR Breakout Strategy', overlay=true, max_bars_back=500, max_lines_count=400)
prd = input.int(defval=5, title='Period', minval=2)
bo_len = input.int(defval=71, title='Max Breakout Length', minval=30, maxval=300)
cwidthu = input.float(defval=3., title='Threshold Rate %', minval=1., maxval=10) / 100
mintest = input.int(defval=2, title='Minimum Number of Tests', minval=1)
bocolorup = input.color(defval=color.blue, title='Breakout Colors')
```