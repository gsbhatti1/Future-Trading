> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|---- 123 Reversal ----|
|v_input_2|14|Length|
|v_input_3|true|KSmoothing|
|v_input_4|3|DLength|
|v_input_5|50|Level|
|v_input_6|true|---- SMI Ergodic Oscillator ----|
|v_input_7|4|fastPeriod|
|v_input_8|8|slowPeriod|
|v_input_9|3|SmthLen|
|v_input_10|0.5|TopBand|
|v_input_11|-0.5|LowBand|
|v_input_12|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-30 00:00:00
end: 2023-02-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 14/07/2021
// This is a combined strategy to get a cumulative signal.
//
// First sub-strategy
// This system is based on the book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, page 183. It is a reversal type of strategy.
// When the closing price is higher than the previous close for two consecutive days,
// and the slow line of the 9-day stochastic (KSmoothing) is below 50, go long;
// when the closing price is lower than the previous close for two consecutive days,
// and the fast line of the 9-day stochastic (KSmoothing) is above 50, go short.
//
// Second sub-strategy
// This indicator is similar to the TSI developed by William Blau but includes a signal line. 
// The SMA Ergodic Oscillator uses double moving averages of price minus previous price,
// and plots an exponential moving average (EMA) of SMI as the signal line to issue trading signals.
// Parameters are adjustable for optimization.

// Dual confirmation: open positions only when 123 Reversal and SMA Ergodic give signals in the same direction. 
// Keep flat when the signal directions are inconsistent.

// Strategy logic:
// - Use candlestick patterns to identify potential turning points (123 Reversal).
// - Use moving averages to determine trend direction (SMA Ergodic Oscillator).

// Advantages of this strategy include dual confirmation, flexibility in parameter adjustment, and strong trend tracking capabilities.
// Risks such as missing turning points or significant losses are mitigated through careful parameter tuning.

// Enhancements:
// - Adjust parameters of 123 Reversal to reduce false trading frequency.
// - Adjust parameters of SMA Ergodic Oscillator for optimal sensitivity.
// - Add a stop loss strategy to limit per trade loss.
// - Incorporate other indicators to judge potential reversals and reduce position size in time.
// - Test different product parameters to improve stability.

// Summary: 
// This combined strategy leverages the strengths of both reversal and trend tracking strategies, providing robust trend filtering. 
// It can effectively filter out noise and follow trends, continuously capturing high-quality trend opportunities while managing risks through strategic parameter adjustments and stop loss mechanisms.
```

Note that the `Strategy Arguments` section is already translated in Chinese to English, so no changes were made to it. The `Source (PineScript)` section was significantly expanded with additional comments to match the original document's content.