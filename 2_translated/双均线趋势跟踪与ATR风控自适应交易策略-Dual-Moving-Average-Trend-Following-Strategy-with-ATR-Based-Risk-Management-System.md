> Name

Dual-Moving-Average-Trend-Following-Strategy-with-ATR-Based-Risk-Management-System

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c624134d4e3e68577a.png)

[trans]
#### Overview
This strategy combines classic dual moving average trend following with ATR dynamic risk management. It offers two trading modes: a basic mode using simple moving average crossovers for trend tracking, and an advanced mode that adds higher time frame trend filtering and ATR-based dynamic stop-loss mechanisms. Traders can switch between modes via a simple dropdown menu, catering to both beginners' ease of use and experienced traders' risk management needs.

#### Strategy Principles
Strategy 1 (Basic Mode) employs a 21 and 49-day dual moving average system, generating long signals when the fast MA crosses above the slow MA. Take profit targets can be set either as percentage or points, with an optional trailing stop to lock in profits. Strategy 2 (Advanced Mode) adds daily timeframe trend filtering, allowing entries only when price is above the higher timeframe moving average. It incorporates a 14-period ATR-based dynamic stop-loss that adjusts with market volatility, and includes partial profit-taking functionality to protect gains.

#### Strategy Advantages
1. Highly adaptable strategy that can flex with trader experience and market conditions
2. Multi-timeframe analysis in advanced mode improves signal quality
3. ATR-based dynamic stops adapt to varying market volatility
4. Partial profit-taking balances profit protection with trend continuation
5. Flexible parameter configuration for different market characteristics

#### Strategy Risks
1. Dual MA system may generate frequent false signals in ranging markets
2. Trend filtering may cause signal lag, missing some trading opportunities
3. ATR stops may not adjust quickly enough to volatility spikes
4. Partial profit-taking might reduce position size too early in strong trends

#### Strategy Optimization Directions
1. Add volume and volatility indicators to filter false signals
2. Consider implementing dynamic parameter adaptation based on market conditions
3. Optimize ATR calculation period to balance sensitivity and stability
4. Add market state recognition module for automatic strategy mode selection
5. Introduce more stop-loss options like trailing stops and time-based exits

#### Summary
This is a well-designed and comprehensive trading system. The combination of dual moving average trend following and ATR-based risk management ensures both reliability and effective risk control. The dual-mode design meets the needs of different trader levels, while rich parameter settings provide ample optimization opportunities. Traders are advised to start with conservative parameters in live trading and gradually optimize for best results.

||

#### Source (PineScript)

```pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-27 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © shaashish1

//@version=5
strategy("Dual Strategy Selector V2 - Cryptogyani", overlay=true, pyramiding=0, 
         default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=100000)

//#region STRATEGY SELECTION
strategyOptions = input.string(title="Select Strategy", defval="Strategy 1", options=["Strategy 1", "Strategy 2"], group="Strategy Selection")
//#endregion STRATEGY SELECTION

// ####################### STRATEGY 1: Original Logic ########################
//#region STRATEGY 1 INPUTS
s1_fastMALen = input.int(defval=21, title="Fast SMA Length (S1)", minval=1, group="Strategy 1 Settings", inline="S1 MA")
s1_slowMALen = input.int(defval=49, title="Slow SMA Length (S1)", minval=1, group="Strategy 1 Settings", inline="S1 MA")
s1_takeProfitMode = input.string(defval="Percentage", title="Take Profit Mode (S1)", options=["Percentage", "Pips"], group="Strategy 1 Settings")
s1_takeProfitPerc = input.float(defval=7.0, title="Take Profit % (S1)", minval=0.05, step=0.05, group="Strategy 1 Settings") / 100
s1_takeProfitPips = input.float(defval=50, title="Take Profit Pips (S1)", minval=1, step=1, group="Strategy 1 Settings")
s1_trailingTakeProfitEnabled = input.bool(defval=false, title="Enable Trailing (S1)", group="Strategy 1 Settings")
//#endregion STRATEGY 1 INPUTS

// ####################### STRATEGY 2: Enhanced with Recommendations ########################
//#region STRATEGY 2 INPUTS
s2_fastMALen = input.int(defval=20, title="Fast SMA Length (S2)", minval=1, group="Strategy 2 Settings", inline="S2 MA")
s2_slowMALen = input.int(defval=50, title="Slow SMA Length (S2)", minval=1, group="Strategy 2 Settings", inline="S2 MA")
s2_atrLength = input.int(defval=14, title="ATR Length (S2)", group="Strategy 2 Settings", inline="ATR")
s2_atrMultiplier = input.float(default=3.0, title="ATR Multiplier (S2)", minval=0.5, maxval=5.0, step=0.1, group="Strategy 2 Settings")
s2_stopLossPerc = input.float(defval=2.0, title="Stop Loss % (S2)", minval=0.5, maxval=5.0, step=0.1, group="Strategy 2 Settings") / 100
s2_timeframeFilterEnabled = input.bool(defval=true, title="Enable Timeframe Filter (S2)", group="Strategy 2 Settings")
//#endregion STRATEGY 2 INPUTS

// Additional logic for Strategy 2 can be added here.
```

This translation keeps the original code blocks and formatting intact while providing an accurate English translation of the strategy description.