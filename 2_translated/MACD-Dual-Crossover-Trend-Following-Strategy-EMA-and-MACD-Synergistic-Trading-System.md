> Name

Dual-Crossover-Trend-Following-Strategy-EMA-and-MACD-Synergistic-Trading-System

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b8ce3a649a9104dfc2.png)

[trans]
#### Overview
This strategy is a trend-following trading system that combines EMA and MACD dual technical indicators. It captures market trends through the crossover of EMA9 with price and the crossover of MACD fast line (DIF) with slow line (DEA). The strategy employs an adaptive stop-loss based on the past 5 candles and uses a 3.5:1 reward-risk ratio for profit targets, forming a complete trading system.

#### Strategy Principle
The core logic is divided into long and short directions:
1. Long conditions: When the closing price breaks above EMA9 from below, and MACD's DIF line crosses above the DEA line, the system generates a long signal.
2. Short conditions: When the closing price breaks below EMA9 from above, and MACD's DIF line crosses below the DEA line, the system generates a short signal.
3. Risk management:
   - Long position stop-loss is set below the lowest point of the previous 5 candles
   - Short position stop-loss is set above the highest point of the previous 5 candles
   - Profit target is set at 3.5 times the stop-loss distance

#### Strategy Advantages
1. Dual confirmation mechanism: Through the synergy of EMA and MACD, effectively filters false signals and improves trading accuracy.
2. Adaptive stop-loss: Stop-loss positions based on recent price volatility automatically adjust according to market volatility.
3. Clear risk-reward ratio: Fixed 3.5:1 risk-reward setting helps achieve long-term stable profits.
4. Clear strategy logic: Entry and exit conditions are explicit, easy to understand and execute.
5. High adaptability: Parameters can be adjusted according to different market conditions.

#### Strategy Risks
1. Choppy market risk: Frequent false breakouts may occur in sideways markets, leading to consecutive stop-losses.
2. Slippage risk: In fast-moving markets, actual stop-loss and profit prices may deviate from expectations.
3. Parameter sensitivity: EMA and MACD period settings have significant impact on strategy performance.
4. Trend dependency: Strategy may not perform well in markets without clear trends.

#### Strategy Optimization Directions
1. Add trend filter: Introduce longer-period trend indicators to only trade in the main trend direction.
2. Dynamic risk multiplier: Automatically adjust risk-reward ratio based on market volatility.
3. Time filtering: Add trading time filters to avoid low liquidity periods.
4. Position management optimization: Dynamically adjust position size based on signal strength.
5. Introduce volatility indicators: For dynamic adjustment of stop-loss distances.

#### Summary
This strategy constructs a complete trend-following trading system through technical indicator dual confirmation and strict risk management. Although there is some market environment dependency, the strategy shows good adaptability and stability through reasonable parameter optimization and risk management. Future optimization directions mainly focus on improving trend identification accuracy and risk management dynamics to enhance overall strategy performance.

||

#### Source (PineScript)

```pinescript
/*backtest
start: 2024-01-17 00:00:00
end: 2025-01-16 00:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT","balance":49999}]
*/

// =======================
// @version=6
strategy(title="MACD + EMA9 3 h",
         shorttitle="MACD+EMA9+StopTP_5candles",
         overlay=true,
         initial_capital=100000,    // Adjust as desired
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=200)      // Risk percentage or quantity

// ----- Inputs -----
emaLen          = input.int(9,     "EMA 9 Period", minval=1)
macdFastLen     = input.int(12,    "MACD Fast Period", minval=1)
macdSlowLen     = input.int(26,    "MACD Slow Period", minval=1)
macdSignalLen   = input.int(9,     "MACD Signal Period", minval=1)
riskMultiplier  = input.float(3.5, "Risk Multiplier (TP)")
lookbackCandles = input.int(5,     "Number of Candles for Stop", minval=1)

// ----- EMA Calculation -----
ema9 = ta.ema(close, emaLen)

// ----- MACD Calculation -----
[macdLine, signalLine, histLine] = ta.macd(close, macdFastLen, macdSlowLen, macdSignalLen)
// DIF crosses DEA up or down
macdCrossover   = ta.crossover(macdLine, signalLine)   // DIF crosses DEA up
macdCrossunder  = ta.crossunder(macdLine, signalLine)  // DIF crosses DEA down

// ----- Entry/Exit Conditions -----

// Buy when:
// 1) Price crosses EMA9 from below
// 2) MACD's DIF line crosses above the DEA line
buySignal = ta.crossover(close, ema9) and macdCrossover

// Sell when:
// 1) Price crosses EMA9 from above
// 2) MACD's DIF line crosses below the DEA line
sellSignal = ta.crossunder(close, ema9) and macdCrossunder

// ----- Risk Management -----

stopLossLong   = low[lookbackCandles]
takeProfitLong = stopLossLong * (1 + riskMultiplier)

stopLossShort  = high[lookbackCandles]
takeProfitShort = stopLossShort * (1 - riskMultiplier)

// ----- Execution of Trades -----
if (buySignal)
    strategy.entry("Buy", strategy.long, when=buySignal)
    strategy.exit("Take Profit/Stop Loss", "Buy", limit=takeProfitLong, stop=stopLossLong)

if (sellSignal)
    strategy.entry("Sell", strategy.short, when=sellSignal)
    strategy.exit("Take Profit/Stop Loss", "Sell", limit=takeProfitShort, stop=stopLossShort)
```

This PineScript code defines the trading logic based on the described strategy. Adjustments can be made to the inputs and other parameters as needed for specific market conditions or preferences.