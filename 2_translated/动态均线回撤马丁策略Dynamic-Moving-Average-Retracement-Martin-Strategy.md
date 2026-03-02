> Name

Dynamic Moving Average Retracement Martin Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/f353fcad2ccf4c6578.png)
[trans]

### Overview

The Dynamic Moving Average Retracement Martin strategy is a frequent trading strategy that combines moving average crossovers and bottom divergence signals to generate entry and exit signals. The strategy utilizes the crossover and divergence of 3-day and 8-day simple moving averages to capture short-term trends, and adopts stop-loss and take-profit mechanisms to control risks. This strategy allows for choosing trading directions based on different market conditions.

### Strategy Logic

The strategy uses 3-day and 8-day simple moving averages along with their crossover signals. A long signal is generated when the 3-day MA crosses above the 8-day MA, and a short signal is generated when the 3-day MA crosses below the 8-day MA. Long signals will trigger long entries, and short signals will trigger short entries.

If there are no existing positions, the strategy determines entry based on crossover signals. After entry, stop-loss and take-profit prices will be calculated based on the latest close price, stop-loss percentage, and take-profit percentage. For example, when holding a long position, the stop loss price is set as the latest close price minus the stop-loss percentage times the 8-day MA; the take profit price is set as the latest close price plus the take-profit percentage times the 8-day MA.

If there are existing long positions, when the price triggers the stop-loss or take-profit levels, if an 8-day MA bottom divergence signal occurs, the position will be closed. At this time, the stop loss and take profit prices will be reset to zero. The logic for handling short positions is similar.

The strategy also plots entry and exit points on the chart, such as using upward triangles for long entries and downward triangles for long exits, which helps in visually determining entry and exit points.

### Advantage Analysis

The advantages of this strategy include:

1. Captures short-term trends using moving average crossovers, allowing frequent trading.
2. Stop-loss mechanisms can control single losses.
3. Take-profit settings can lock in partial profits.
4. Trading directions can be selected to suit different market stages.
5. Visualizes entry and exit points on the chart for clarity.

### Risk Analysis

The main risks of this strategy include:

1. Short-term MA strategies may get whipsawed easily.
2. The possibility of lagging signals from moving averages.
3. Consecutive losses can lead to increased overall losses.
4. Incorrectly set stop-loss percentages may be too loose or too tight.

Risk reduction can be achieved by reasonably widening the stop-loss percentage, optimizing moving average parameters, introducing additional filter conditions, etc. Correctly assessing personal risk tolerance and avoiding overtrading is also important.

### Optimization Directions

This strategy can be optimized in the following ways:

1. Test more MA combinations to find optimal parameters.
2. Add other indicators like RSI, KD, etc., to improve signal quality.
3. Adjust stop-loss percentages according to different products and timeframes.
4. Introduce position sizing controls such as fixed quantity or fixed capital.
5. Implement entry order rules.
6. Optimize and evaluate stop-loss or take-profit levels.

### Summary

The Dynamic Moving Average Retracement Martin strategy is a short-term trading strategy that captures short-term trends formed by moving average crossovers and manages risks with appropriate stop-loss and take-profit mechanisms. Its frequent trading nature provides both profit opportunities and inherent risks. By optimizing parameters, filtering signals, and managing risks, this strategy can be further improved for greater reliability.

||

### Overview  

The Dynamic Moving Average Retracement Martin strategy is a frequent trading strategy that combines moving average crossovers and bottom divergence signals to generate entry and exit signals. The strategy utilizes the crossover and divergence of 3-day and 8-day simple moving averages to capture short-term trends, and adopts stop-loss and take-profit mechanisms to control risks. This strategy allows for choosing trading directions based on different market conditions.

### Strategy Logic

The strategy uses 3-day and 8-day simple moving averages along with their crossover signals. A long signal is generated when the 3-day MA crosses above the 8-day MA, and a short signal is generated when the 3-day MA crosses below the 8-day MA. Long signals will trigger long entries, and short signals will trigger short entries.

If there are no existing positions, the strategy determines entry based on crossover signals. After entry, stop-loss and take-profit prices will be calculated based on the latest close price, stop-loss percentage, and take-profit percentage. For example, when holding a long position, the stop loss price is set as the latest close price minus the stop-loss percentage times the 8-day MA; the take profit price is set as the latest close price plus the take-profit percentage times the 8-day MA.

If there are existing long positions, when the price triggers the stop-loss or take-profit levels, if an 8-day MA bottom divergence signal occurs, the position will be closed. At this time, the stop loss and take profit prices will be reset to zero. The logic for handling short positions is similar.

The strategy also plots entry and exit points on the chart, such as using upward triangles for long entries and downward triangles for long exits, which helps in visually determining entry and exit points.

### Advantage Analysis

The advantages of this strategy include:

1. Captures short-term trends using moving average crossovers, allowing frequent trading.
2. Stop-loss mechanisms can control single losses.
3. Take-profit settings can lock in partial profits.
4. Trading directions can be selected to suit different market stages.
5. Visualizes entry and exit points on the chart for clarity.

### Risk Analysis

The main risks of this strategy include:

1. Short-term MA strategies may get whipsawed easily.
2. The possibility of lagging signals from moving averages.
3. Consecutive losses can lead to increased overall losses.
4. Incorrectly set stop-loss percentages may be too loose or too tight.

Risk reduction can be achieved by reasonably widening the stop-loss percentage, optimizing moving average parameters, introducing additional filter conditions, etc. Correctly assessing personal risk tolerance and avoiding overtrading is also important.

### Optimization Directions

This strategy can be optimized in the following ways:

1. Test more MA combinations to find optimal parameters.
2. Add other indicators like RSI, KD, etc., to improve signal quality.
3. Adjust stop-loss percentages according to different products and timeframes.
4. Introduce position sizing controls such as fixed quantity or fixed capital.
5. Implement entry order rules.
6. Optimize and evaluate stop-loss or take-profit levels.

### Summary

The Dynamic Moving Average Retracement Martin strategy is a short-term trading strategy that captures short-term trends formed by moving average crossovers, and manages risks with appropriate stop-loss and take-profit mechanisms. Its frequent trading nature provides both profit opportunities as well as inherent risks. By optimizing parameters, filtering signals, and managing risks, this strategy can be further improved for greater reliability.

|---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|1.03|Take Profit|
|v_input_2|0.95|Stop Loss|
|v_input_string_1|0|Trading Mode: Long|Short|BiDir|

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-17 00:00:00
end: 2023-11-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

    // ____  __    ___   ________ ___________  ___________ __  ____ ___ 
   // / __ )/ /   /   | / ____/ //_/ ____/   |/_  __<  / // / / __ |__ \
  // / __  / /   / /| |/ /   / ,< / /   / /| | / /  / / // /_/ / / __/ /
 // / /_/ / /___/ ___ / /___/ /| / /___/ ___ |/ /  / /__  __/ /_/ / __/ 
// /_____/_____/_/  |_\____/_/ |_\____/_/  |_/_/  /_/  /_/  \____/____/                                              

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © blackcat1402
//@version=5
strategy('[blackcat] L1 MartinGale Scalping Strategy', overlay=true, pyramiding = 5)

// Define input variables
```