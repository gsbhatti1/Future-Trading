``` pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-04-15 00:00:00
period: 8h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("I11L Hypertrend", overlay=false, initial_capital=500000)
tradingMode = input.string("Oversold or Trend", "Trading Mode", ["Oversold or Trend", "Always Buy"], tooltip="Choose the Trading Mode by trying Both in your Backtesting. I use it if one is far better then the other one.")

invertStrategy = tradingMode == "Trend" ? true : false
compoundingMode = input.bool(false, "Work with the total equity")
useTSL = input.bool(true, "Use a trailing SL")
useTP = input.bool(true, "Use a TP")
scoreLookbackDistance = input.int(20, step=1, title="Lookbackdistance for the Score")
scoreLoopCountTo = 20
leverage = input.float(1.0, "Leverage (x)", [20, 10, 5, 2, 1])
SL_Factor = 1 - input.float(3.0, "Risk Capital per Trade unleveraged (%)", minval=0.1, maxval=100, step=0.25) / 100 / leverage
TPFactor = input.float(1.2, step=0.1)

chooseDate = input.string(title="Select Date", defval="All available Records", options=["Start-2012", "2012-Now", "All available Records"], tooltip="Separation works best for 8hr CFD markets; you might want to fine-tune your settings in the past and see if the future results (2010 to now) are better than random.")
dateFrom = chooseDate == "Start-2012" ? timestamp("01 Jan 1970 00:00") : chooseDate == "2012-Now" ? timestamp("01 Jan 2012 00:00") : timestamp("01 Jan 1970 00:00")
dateTo = chooseDate == "Start-2012" ? timestamp("31 Dec 2011 23:59") : chooseDate == "2012-Now" ? timestamp("31 Dec 2170 23:59") : timestamp("31 Dec 2170 23:59")
inDateRange = (time >= dateFrom) and (time < dateTo)

var disableAdditionalBuysThisDay = false
var minuteOfLastSell = 0

if(dayofmonth != dayofmonth[1])
    disableAdditionalBuysThisDay := false

longStopPrice = 0.0
longStopPrice := if (strategy.position_size > 0)
    if(useTSL)
        math.max(high * SL_Factor, longStopPrice[1])
    else
        strategy.position_avg_price * SL_Factor
else
    0

if(strategy.position_size != strategy.position_size[1])
    disableAdditionalBuysThisDay := true

//Trade Logic
SCORE = 0
loopCount = 1
for i=0 to scoreLoopCountTo
    trendLengthAdjusted = loopCount
    loopCount := loopCount + 1 
    if(ta.ema(close, trendLengthAdjusted) / ta.sma(close, trendLengthAdjusted) > 1)
        SCORE := SCORE + 1

SCORE_ema50 = ta.ema(SCORE, scoreLookbackDistance)
SCORE_sma50 = ta.sma(SCORE, scoreLookbackDistance)
isOversold = ta.crossover(SCORE_sma50 / SCORE_ema50, 1.0)
isTrend = ta.crossover(SCORE_ema50 / SCORE_sma50, 1.0)

isBuy = isTrend or isOversold or tradingMode == "Always Buy"

if(isBuy and not(disableAdditionalBuysThisDay) and inDateRange)
    if(compoundingMode)
        strategy.entry("Buy", strategy.long, (strategy.equity / close) * leverage)
    else
        strategy.entry("Buy", strategy.long, (strategy.initial_capital / close) * leverage)

if(strategy.position_size > 0)
```

This translation preserves the original formatting and code while translating the human-readable text from Chinese to English.