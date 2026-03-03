``` pinescript
/*backtest
start: 2024-09-01 00:00:00
end: 2025-02-18 08:00:00
period: 5d
basePeriod: 5d
exchanges: [{"eid":"Binance","currency":"BTC_USDT"}]
*/

// This code is released under the Mozilla Public License 2.0
// More details at: https://mozilla.org/MPL/2.0/
// © LonesomeTheBlue

//@version=5
strategy("Consolidation Zones - Live [Strategy]", overlay=true, max_bars_back=1100)

//-----------------------------------------------------------------------//
//                        Input Variables
//-----------------------------------------------------------------------//
prd       = input.int(defval=10, title="Loopback Period", minval=2, maxval=50)
conslen   = input.int(defval=5,  title="Min. Consolidation Length", minval=2, maxval=20)
paintcons = input.bool(defval=true, title="Color Consolidation Zone?")
zonecol   = input.color(defval=color.new(color.blue, 70), title="Zone Color")

//-----------------------------------------------------------------------//
//                  Variables and Calculations for ZZ (ZigZag) Detection
//-----------------------------------------------------------------------//

// Check if the bar has the highest High or lowest Low in the last prd bars
float hb_ = ta.highestbars(prd) == 0 ? high : na
float lb_ = ta.lowestbars(prd)  == 0 ? low  : na

// Convert to bool to check if hb_ and lb_ are valid (not na)
bool hasHb = not na(hb_)
bool hasLb = not na(lb_)

// Direction variable to determine the trend, based on the last high or low pivot
var int dir = 0

// ZigZag value and last pivot
float zz = na
float pp = na

// 1) Determine direction based on whether a high or low pivot occurred
dir := if hasHb and not hasLb
    1
else if hasLb and not hasHb
    -1
else
    dir  // unchanged
```