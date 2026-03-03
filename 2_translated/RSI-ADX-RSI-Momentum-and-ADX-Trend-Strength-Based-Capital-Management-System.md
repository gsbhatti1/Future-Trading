> Name

RSI-Momentum-and-ADX-Trend-Strength-Based-Capital-Management-System

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d727085206ec4fcf88.png)

#### Overview
This strategy is a hybrid system combining trend following and swing trading, achieving stable trading through multiple technical indicator screening and strict capital management. The strategy adopts a stepped take-profit approach to lock in profits while setting maximum drawdown control to manage risk while ensuring returns. The system uses RSI momentum indicator and ADX trend strength indicator as the main trading signal triggers, combined with volume, ATR, and EMA multiple filters to ensure trading effectiveness.

#### Strategy Principle
The core logic of the strategy includes the following key elements:
1. Entry conditions require simultaneous satisfaction: trading volume greater than 1M, ADX greater than 25 indicating a clear trend, RSI greater than 60 showing strong momentum, ATR greater than 2 ensuring sufficient volatility range, price above 200-day moving average maintaining an uptrend.
2. Stepped take-profit design: first take-profit at 15%, closing 50% position; second take-profit at 30%, closing remaining position. This design both locks in partial profits early and doesn’t miss big trends.
3. Stop-loss control: setting a 15% stop-loss to protect capital, while exiting when RSI falls below 50 or price breaks below the 200-day moving average.
4. Drawdown management: real-time tracking of strategy equity, triggering systemic risk control and clearing all positions when drawdown exceeds 30%.

#### Strategy Advantages
1. Multiple technical indicators cross-validation improves trading signal reliability
2. Stepped take-profit design balances short-term profit and capturing major trends
3. Complete risk control system, including individual stock stop-loss and systemic risk control
4. Strict trading conditions effectively filter false signals
5. Clear strategy logic, easy to adjust parameters based on market conditions

#### Strategy Risks
1. Multiple indicator filtering may miss some trading opportunities
2. Frequent stop-losses may be triggered in oscillating markets
3. Fixed percentage stop-loss and take-profit settings may not suit all market environments
4. Strategy relies on technical indicators, may have insufficient response to fundamental sudden events
5. Requires larger capital scale to meet trading volume requirements

#### Strategy Optimization Directions
1. Introduce adaptive stop-loss and take-profit mechanisms, dynamically adjusting based on market volatility
2. Add a market environment judgment module, using different parameter settings under different market conditions
3. Optimize ADX calculation method, consider using adaptive periods
4. Include transaction cost considerations, optimizing the position management system
5. Develop a machine learning-based signal filtering mechanism

#### Summary
This strategy is a comprehensive trading system achieving stable trading through multiple technical indicators and strict capital management. The core advantages of the strategy lie in its complete risk control system and stepped take-profit mechanism, but attention needs to be paid to timely parameter adjustments based on market conditions in practical application. The strategy's further optimization space mainly lies in parameter dynamic adaptation and signal filtering mechanism improvement.

#### Source (PineScript)

```pinescript
/*backtest
start: 2023-12-20 00:00:00
end: 2024-12-18 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title="Swing Strategy (<30% DD)", shorttitle="SwingStratDD", overlay=true)

//-----------------------------------------------------
// Example Indicators and Logic
//-----------------------------------------------------
emaLen   = input.int(200, "EMA Length", minval=1)
emaValue = ta.ema(close, emaLen)

plot(emaValue, color=color.yellow, linewidth=2, title="EMA 200")


//-----------------------------------------------------
// User Inputs
//-----------------------------------------------------
adxLen           = input.int(14,  "ADX Length",      minval=1)
rsiLen           = input.int(14,  "RSI Length",      minval=1)
atrLen           = input.int(14,  "ATR Length",      minval=1)

rsiBuyThresh     = input.float(60, "RSI Buy Threshold",     minval=1, maxval=100)
adxThresh        = input.float(25, "ADX Threshold (Trend)", minval=1, maxval=100)
minVolume        = input.float(1e6,"Minimum Volume",         minval=1)
minATR           = input.float(2,  "Minimum ATR(14)",        minval=0.1, step=0.1)

stopLossPerc     = input.float(15, "Stop-Loss %",            minval=0.1, step=0.1)
// We’ll do two partial take-profit levels to aim for consistent cashflow:
takeProfit1Perc  = input.float(15, "Take-Profit1 %",         minval=1, maxval=30)
```