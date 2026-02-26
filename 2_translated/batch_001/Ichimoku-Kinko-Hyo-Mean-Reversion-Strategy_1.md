``` pinescript
/*backtest
start: 2022-09-17 00:00:00
end: 2023-09-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
// Any timeFrame ok but good on 15 minute & 60 minute, Ichimoku + Daily-Candle_cross(DT) + HULL-MA_cross + MacD combination 420 special blend
strategy("Ichimoku + Daily-Candle_X + HULL-MA_X + MacD", shorttitle="٩(̾●̮̮̃̾•̃̾)۶", overlay=true, default_qty_type=strategy.percent_of_equity, max_bars_back=26, default_qty_value=100, calc_on_order_fills= true, calc_on_every_tick=true, pyramiding=0, precision=6)
keh=input(title="Double HullMA", defval=14, minval=1)
dt = input(defval=0.0010, title="Decision Threshold (0.001)", type=float, step=0.0001)
SL = input(defval=-500.00, title="Stop Loss in $", type=float, step=1)
TP = input(defval=25000.00, title="Target Point in $", type=float, step=1)
ot=1
p = input(7, minval=1, title="Length")
pi=3.1415926535
w=2*pi/p
beta = (1 - cos(w))/(pow(1.414,2.0/3) - 1)
alfa = -beta + sqrt(beta*beta + 2*beta)
ret1= pow(alfa,4)*close+4*(1-alfa)*nz(ret1[1])-6*pow(1-alfa,2)*nz(ret1[2])+4*pow(1-alfa,3)*nz(ret1[3])-pow(1-alfa,4)*nz(ret1[4])
ret2= pow(alfa,4)*close[1]+4*(1-alfa)*nz(ret1[1])-6*pow(1-alfa,2)*nz(ret1[2])+4*pow(1-alfa,3)*nz(ret1[3])-pow(1-alfa,4)*nz(ret1[4])
confidence=(security(syminfo.tickerid, 'D', close)-security(syminfo.tickerid, 'D', close[1]))/security(syminfo.tickerid, 'D', close[1])
conversionPeriods = input(9, minval=1, title="Conversion Line Periods")
basePeriods = input(26, minval=1, title="Base Line Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span 2 Periods")
displacement = input(26, minval=1, title="Displacement")
donchian(len) => avg(lowest(len), highest(len))
conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadLine1 = avg(conversionLine, baseLine)
leadLine2 = donchian(laggingSpan2Periods)
LS=close, offset = -displacement
MACD_Length = input(9)
MACD_fastLength = input(12)
MACD_slowLength = input(26)
MACD = ema(close, MACD_fastLength) - ema(close, MACD_slowLength)
aMACD = ema(MACD, MACD_Length)
closelong = ret1<ret2 and close<ret2 and confidence<dt or strategy.openprofit<SL or strategy.openprofit>TP
if (closelong)
    strategy.close("Long")
longCondition = ret1>ret2 and strategy.opentrades<ot and confidence>dt and close>ret2 and leadLine1>leadLine2 and open<LS and MACD>0
strategy.entry("Long", strategy.long, when=longCondition)
```