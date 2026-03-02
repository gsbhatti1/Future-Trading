``` pinescript
/*backtest
start: 2023-11-16 00:00:00
end: 2023-11-23 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy(title="[WAI GUA]", shorttitle="[EOS] 1.0", overlay=false )

//study(title="[WAI GUA]", shorttitle="[EOS] 1.0", overlay=true)



//
// Use Alternate Anchor TF for MAs 
uRenko    = input(true, title="IS This a RENKO Chart")
//
anchor     = input(0,minval=0,maxval=1440,title="Alternate TimeFrame Multiplier (0=none)")
//
src          = close //input(close, title="EMA Source")
showRibbons  = input(false,title="Show Coloured MA Ribbons")
showAvgs     = input(false,title="Show Ribbon Median MA Lines")
fastType     = input("WMA",title="FAST MA Ribbon Type: EMA|SMA|WMA|VWMA|SMMA|DEMA|TEMA|LAGMA|HullMA|ZEMA|TMA|SSMA")
fastLower    = input(5,title="FAST Ribbon Lower MA Length")
fastUpper    = input(25,title="FAST Ribbon Upper Length")
slowType     = input("WMA",title="SLOW MA Ribbon Type: EMA|SMA|WMA|VWMA|SMMA|DEMA|TEMA|LAGMA|HullMA|ZEMA|TMA|SSMA")
slowLower    = input(28,title="SLOW Ribbon Lower MA Length")
slowUpper    = input(72,title="SLOW Ribbon Upper Length")
backtestStartYear  = input(2018, title="Backtest Start Year")
backtestStartMonth = input(true, title="Backtest Start Month")
backtestStartDay   = input(true, title="Backtest Start Day")
startValue        = input(0.02, title="start")
increment         = input(0.02, title="increment")
maxStep           = input(0.2, title="maximum")
reverseTrade      = input(false, title="Use Opposite Trade as a Close Signal")
colorCandles      = input(true, title="Colour Candles to Trade Order state")
orderType         = input("Longs+Shorts", title="What type of Orders: LongsOnly|ShortsOnly|Flip", options=["LongsToShorts","ShortsToLongs","Flip"])
trailStop         = input(true, title="Trailing Stop")
trailPercent      = input(3, title="Trailing Stop (%)")
takeProfit        = input(true, title="Take Profit")
profitPercent     = input(3, title="Take Profit (%)")
trailProfit       = input(true, title="Trailing Profit (%)")
stopLoss          = input(false, title="Stop Loss")
lossPercent       = input(3, title="Stop Loss (%)")
```

Note: The translation has been kept as close to the original code as possible while ensuring it remains coherent. The comments and parameter names have been translated where necessary.