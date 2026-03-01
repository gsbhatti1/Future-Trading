``` pinescript
/*backtest
start: 2023-09-29 00:00:00
end: 2023-10-06 00:00:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 26/06/2019
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9-days Stochastic Slow Oscillator is lower than 50. 
// The strategy sells at market, if close price is lower than the previous close price 
// during 2 days and the meaning of 9-days Stochastic Fast Oscillator is higher than 50.
//
// Second strategy
//    Breakout Range Long Strategy
//
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
Reversal123(Length, KSmoothing, DLength, Level) =>
    vFast = sma(stoch(close, high, low, Length), KSmoothing) 
    vSlow = sma(vFast, DLength)
    pos = 0.0
    pos := iff(close[2] < close[1] and close > close[1] and vFast < vSlow and vFast > Level, 1,
	           iff(close[2] > close[1] and close < close[1] and vFast > vSlow and vFast < Level, -1, nz(pos[1], 0))) 
	pos

BreakoutRangeLong(look_bak) =>
    pos = 0
    xHighest = highest(high, look_bak)
    pos := iff(high > xHighest[1], 1, 0) 
    pos

strategy(title="Combo Backtest 123 Reversal & Breakout Range Long", shorttitle="Combo", overlay = true)
Length = input(14, minval=1)
KSmoothing = input(1, minval=1)
DLength = input(3, minval=1)
Level = input(50, minval=1)
LookBak = input(4, title="Look Back Period", minval=1)
TradeReverse = input(false, title="Trade Reverse")

// Calculate Reversal123
reversalSignal = Reversal123(Length, KSmoothing, DLength, Level)

// Calculate Breakout Range Long
breakoutLongSignal = BreakoutRangeLong(LookBak)

// Determine final trade direction based on signals and settings
if (TradeReverse)
    strategy.entry("Reversal", reversalSignal > 0 ? side.long : side.short)
else
    strategy.entry("Breakout", breakoutLongSignal == 1 ? side.long : side.short, comment="")

strategy.exit("Exit", "Reversal", stop=low - 5 * tr)
strategy.exit("Exit", "Breakout", stop=high + 5 * tr)

```

### Strategy Arguments
| Argument       | Default   | Description                                                                 |
|----------------|-----------|------------------------------------------------------------------------------|
| `v_input_1`     | 14        | Length of Stochastic Oscillator                                             |
| `v_input_2`     | true      | KSmoothing                                                                   |
| `v_input_3`     | 3         | DLength of Stochastic Oscillator                                            |
| `v_input_4`     | 50        | Level for Stochastic Oscillator                                             |
| `v_input_5`     | 4         | Look Back Period                                                             |
| `v_input_6`     | false     | Trade Reverse                                                                |

This Pine Script defines a combined trading strategy that incorporates reversal and breakout elements. It includes two functions: one for the Reversal123 strategy and another for the Breakout Range Long strategy. The main strategy logic determines trade signals based on these two components, with an option to trade in reverse or based solely on the breakout condition.