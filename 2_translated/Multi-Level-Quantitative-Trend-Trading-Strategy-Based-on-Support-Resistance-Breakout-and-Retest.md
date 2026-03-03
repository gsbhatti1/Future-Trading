``` pinescript
/*backtest
start: 2024-02-21 00:00:00
end: 2025-02-18 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
*/

//@version=5
strategy("SR Breakout & Retest Strategy (4hr)", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// ===== USER INPUTS =====
leftBars    = input.int(3, "Left Pivot Bars", minval=1)
rightBars   = input.int(3, "Right Pivot Bars", minval=1)
tolerance   = input.float(0.005, "Retest Tolerance (Fraction)", step=0.001)

// ===== PIVOT CALCULATION =====
pLow  = ta.pivotlow(low, leftBars, rightBars)
pHigh = ta.pivothigh(high, leftBars, rightBars)

// ===== STATE VARIABLES FOR CANDIDATE LEVELS =====
var float candidateSupport  = na
var bool  supportBroken     = false
var bool  supportRetested   = false

var float candidateResistance = na
var bool  resistanceBroken    = false
var bool  resistanceRetested  = false

// ===== UPDATE CANDIDATE LEVELS =====
if not na(pLow)
    candidateSupport := pLow
    supportBroken    := false
    supportRetested  := false

if not na(pHigh)
    candidateResistance := pHigh
    resistanceBroken    := false
    resistanceRetested  := false

// ===== CHECK FOR BREAKOUT & RETEST =====
// -- Support: Price breaks below candidate support and then retests it --
if not na(candidateSupport)
    if not supportBroken and low < candidateSupport
        supportBroken := true

    if supportBroken and not supportRetested and close >= candidateSupport and math.abs(low - candidateSupport) <= candidateSupport * tolerance
        supportRetested := true
        label.new(bar_index, candidateSupport, "Support Retest", 
                  style=label.style_label_up, color=color.green, textcolor=color.white, size=size.tiny)
        // Example trading logic: Enter a long position on support retest
        strategy.entry("Long_Support", strategy.long)

// -- Resistance: Price breaks above candidate resistance and then retests it --
if not na(candidateResistance)
    if not resistanceBroken and high > candidateResistance
        resistanceBroken := true

    if resistanceBroken and not resistanceRetested and close <= candidateResistance
        resistanceRetested := true
        label.new(bar_index, candidateResistance, "Resistance Retest", 
                  style=label.style_label_down, color=color.red, textcolor=color.white, size=size.tiny)
        // Example trading logic: Enter a short position on resistance retest
        strategy.entry("Short_Resistence", strategy.short)

```
```