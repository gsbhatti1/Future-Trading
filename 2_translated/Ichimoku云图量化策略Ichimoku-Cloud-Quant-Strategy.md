``` pinescript
/*backtest
start: 2022-11-17 00:00:00
end: 2023-11-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title="Ichimoku only Long Strategy", shorttitle="Ichimoku only Long", overlay = true, pyramiding = 0, calc_on_order_fills = false, commission_type = strategy.commission.percent, commission_value = 0, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, initial_capital=10000, currency=currency.USD)

// Time Range
FromMonth=input(defval=1,title="FromMonth",minval=1,maxval=12)
FromDay=input(defval=1,title="FromDay",minval=1,maxval=31)
FromYear=input(defval=2017,title="FromYear",minval=2017)
ToMonth=input(defval=1,title="ToMonth",minval=1,maxval=12)
ToDay=input(defval=1,title="ToDay",minval=1,maxval=31)
ToYear=input(defval=9999,title="ToYear",minval=2017)
start=timestamp(FromYear,FromMonth,FromDay,00,00)
finish=timestamp(ToYear,ToMonth,ToDay,23,59)
window()=>true
// See if this bar's time happened on/after start date
afterStartDate = time >= start and time<=finish?true:false

// Enable RSI
enableema = input(true, title="Enable EMA?")
enablestochrsi = input(false, title="Enable Stochastic RSI?")
emaperiod1 = input(24, title="EMA 1")
emaperiod2 = input(90, title="EMA 2")
rsik = input(3, title="%K Line")
rsid = input(3, title="%D Line")
rsilen = input(14, title="RSI Length")
stochlen = input(14, title="Stochastic Length")
src = input(close, title="RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4", type=input.source)
ichikonvline = input(9, title="Ichi Conversion Line Length")
ichibase = input(26, title="Ichi Base Line Length")
ichilag2 = input(52, title="Ichi Lagging Span 2 Length")
displace = input(true, title="Ichi Displacement")

// Ichimoku Cloud
conversionline = ta.ichimoku(ichikonvline, ichibase, ichilag2)
base_line = conversionline[displace]
tenkan_sen = conversionline[1 - displace]
kijun_sen = conversionline[2 * displace]
senkou_span_a = (tenkan_sen + kijun_sen) / 2
senkou_span_b = ta.ichimoku(ichikonvline, ichibase, ichilag2)[displace + 10]

// EMA
ema1 = ta.ema(close, emaperiod1)
ema2 = ta.sma(close, emaperiod2)

// Stochastic RSI
rsi = ta.rsi(src, rsilen)
stochk = ta.stoch(rsi, rsi, rsik)
stochd = ta.stoch(rsi, rsi, rsid)

// Entry Conditions
long_condition = afterStartDate and not na(tenkansen) and ta.crossover(close, base_line) and barcolor(green) and (not enableema or ta.crossover(ema1, ema2)) and (not enablestochrsi or ta.crossabove(stochk, stochd))

// Exit Condition
exit_condition = not afterStartDate or ta.crossover(senkou_span_b, close)

if long_condition
    strategy.entry("Long", strategy.long)

if exit_condition
    strategy.close("Long")

```

This script integrates the given parameters and logic into a Pine Script for backtesting on TradingView. It includes Ichimoku Cloud, EMA (when enabled), Stochastic RSI (when enabled) as well as entry and exit conditions based on the specified criteria.