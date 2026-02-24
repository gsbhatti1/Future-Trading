``` pinescript
/*backtest
start: 2022-04-25 00:00:00
end: 2022-05-24 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Super Trend Daily 2.0 BF", overlay=true, precision=2, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.075)

/////////////// Time Frame ///////////////
_0 = input(false, "════════ Test Period ═══════")
testStartYear = input(2017, "Backtest Start Year") 
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear, testStartMonth, testStartDay, 0, 0)

testStopYear = input(2019, "Backtest Stop Year")
testStopMonth = input(12, "Backtest Stop Month")
testStopDay = input(31, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear, testStopMonth, testStopDay, 0, 0)

testPeriod() => true

///////////// Super Trend Long /////////////
_1 = input(false, "═════ Super Trend L ═════")
lengthl = input(title="ATR Period", type=input.integer, defval=2)
multl = input(title="ATR Multiplier", type=input.float, step=0.1, defval=1.5)

atrl = multl * atr(lengthl)

longStopl = hl2 - atrl
longStopPrevl = nz(longStopl[1], longStopl)
longStopl := close[1] > longStopPrevl ? max(longStopl, longStopPrevl) : longStopl

shortStopl = hl2 + atrl
shortStopPrevl = nz(shortStopl[1], shortStopl)
shortStopl := close[1] < shortStopPrevl ? min(shortStopl, shortStopPrevl) : shortStopl

dirl = 1
dirl := nz(dirl[1], dirl)
dirl := dirl == -1 and close > shortStopPrevl ? 1 : dirl == 1 and close < longStopPrevl ? -1 : dirl

///////////// Super Trend Short /////////////
_2 = input(false, "═════ Super Trend S ═════")
lengths = input(title="ATR Period", type=input.integer, defval=3)
mults = input(title="ATR Multiplier", type=input.float, step=0.1, defval=1.3)

atrs = mults * atr(lengths)

longStops = hl2 - atrs
longStopPrevs = nz(longStops[1], longStops)
longStops := close[1] > longStopPrevs ? max(longStops, longStopPrevs) : longStops

shortStops = hl2 + atrs
shortStopPrevs = nz(shortStops[1], shortStops)
shortStops := close[1] < shortStopPrevs ? min(shortStops, shortStopPrevs) : shortStops

dirs = 1
dirs := nz(dirs[1], dirs)
dirs := dirs == -1 and close > shortStopPrevs ? 1 : dirs == 1 and close < longStopPrevs ? -1 : dirs

///////////// Rate Of Change Long ///////////// 
_3 = input(false, "═════ Rate of Change L ═════")
sourcel = close
roclengthl = input(30, "ROC Length", minval=1)
pcntChangel = input(6, "ROC % Change", minval=1)
rocl = 100 * (sourcel - sourcel[roclengthl]) / sourcel[roclengthl]
emarocl = ema(rocl, roclengthl / 2)
isMovingl() => emarocl > (pcntChangel / 2) or emarocl < (0 - (pcntChangel / 2))

///////////// Rate Of Change Short ///////////// 
_4 = input(false, "═════ Rate of Change S ═════")
sources = close
roclengths = input(76, "ROC Length", minval=1)
pcntChanges = input(6, "ROC % Change", minval=1)
rocs = 100 * (sources - sources[roclengths]) / sources[roclengths]
emarocs = ema(rocs, roclengths / 2)
isMovings() => emarocs > (pcntChanges / 2) or emarocs < (0 - (pcntChanges / 2))

/////////////// Strategy /////////////// 
long = dirl == 1 and dirl[1] == -1 and isMovingl()
short = dirs == -1 and dirs[1] == 1 and isMovings()

last_long = 
```