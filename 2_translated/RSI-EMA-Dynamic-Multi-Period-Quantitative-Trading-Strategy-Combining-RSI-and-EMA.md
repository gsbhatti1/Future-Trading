> Name

RSI and EMA Combined Dynamic Multi-Period Quantitative Trading Strategy - Combining RSI and EMA

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/8e489a910e6866981e.png)

[trans]
#### Overview
This strategy is a quantitative trading system based on RSI and EMA, combining Relative Strength Index (RSI) overbought/oversold signals with trend confirmation from Exponential Moving Average (EMA). The strategy includes a risk management module that controls risk through Stop-Loss and Take-Profit settings. According to backtest data, about 70% of trading instruments achieved profitability when tested on 15-minute timeframes.

#### Strategy Principles
The core logic of the strategy is based on the following key elements:
1. RSI Crossing Signals: Short signals are triggered when RSI crosses down from overbought zone, while long signals are triggered when crossing up from oversold zone
2. EMA Trend Confirmation: Using 400-period EMA as trend filter, only allowing long positions above EMA and short positions below EMA
3. Risk Control: Setting 1% stop-loss and take-profit levels for each trade for precise risk control
4. Signal Visualization: Clearly displaying buy/sell signals through shape markers on the chart

#### Strategy Advantages
1. Multiple Signal Confirmation: Combining RSI and EMA indicators effectively reduces false signals
2. Flexible Parameter Settings: Users can adjust RSI period, overbought/oversold thresholds, and EMA period based on different market conditions
3. Complete Risk Management: Protects capital safety through stop-loss and take-profit mechanisms
4. Visualized Trading Signals: Intuitive graphical interface aids strategy monitoring and verification
5. High Adaptability: Shows good profitability across multiple trading instruments

#### Strategy Risks
1. Sideways Market Risk: May generate frequent false signals in ranging markets
2. Slippage Risk: Actual execution prices may deviate from signal prices in markets with insufficient liquidity
3. Trend Reversal Risk: Fixed stop-loss levels may not be sufficient to avoid large price swings during strong trend reversals
4. Parameter Sensitivity: Different parameter combinations may lead to significant variations in strategy performance

#### Strategy Optimization Directions
1. Dynamic Stop-Loss: Consider adjusting stop-loss positions dynamically based on market volatility
2. Multi-Timeframe Analysis: Add signal confirmation mechanisms across multiple timeframes
3. Volatility Filtering: Introduce ATR indicator to filter trading signals in low volatility environments
4. Position Management: Add risk-based position management system
5. Market Environment Recognition: Add market condition judgment module to use different parameter settings under different market conditions

#### Summary
This is a well-structured quantitative trading strategy with clear logic, achieving reliable trading signal generation through the combination of RSI and EMA. The strategy's risk management mechanism and parameter flexibility make it highly practical. Although there are some potential risks, the suggested optimization directions can further enhance the strategy's stability and profitability. It is suitable as a foundation framework for medium to long-term quantitative trading systems, and better trading results can be achieved through continuous optimization and adjustment.[/trans]

#### Source (PineScript)

```pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-27 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI BUY/SELL + EMA + SLTP by rcpislr", overlay=true)

// User Parameters
rsi_period = input(14, title="RSI Period")
rsi_overbought = input(70, title="RSI Overbought Level")
rsi_oversold = input(30, title="RSI Oversold Level")
ema_period = input(400, title="EMA Period")
use_ema = input(true, title="Use EMA Condition")
sl_pct = input(1, title="Stop-Loss (%)") / 100
tp_pct = input(1, title="Take-Profit (%)") / 100

// RSI and EMA Calculations for the Given Timeframe
rsi = ta.rsi(close, rsi_period)
ema = ta.ema(close, ema_period)

// Long and Short Signals
long_signal = rsi[2] > rsi_overbought and rsi < rsi_overbought  and (close > ema or not use_ema)
short_signal = rsi[2] < rsi_oversold and rsi > rsi_oversold and (close < ema or not use_ema)

// Trade Execution
if long_signal
    strategy.entry("Long", strategy.long)

if short_signal
    strategy.entry("Short", strategy.short)

// Stop-Loss and Take-Profit Implementation
if strategy.position_size > 0
    long_stop_loss = close * (1 - sl_pct)
    long_take_profit = close * (1 + tp_pct)
    strategy.exit("Long Exit", from_entry="Long", stop=long_stop_loss, limit=long_take_profit)

if strategy.position_size < 0
    short_stop_loss = close * (1 + sl_pct)
    short_take_profit = close * (1 - tp_pct)
    strategy.exit("Short Exit", from_entry="Short", stop=short_stop_loss, limit=short_take_profit)
```