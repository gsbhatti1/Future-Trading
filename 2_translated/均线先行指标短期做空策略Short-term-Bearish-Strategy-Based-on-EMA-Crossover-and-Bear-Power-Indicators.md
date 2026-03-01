``` pinescript
/*backtest
start: 2023-10-09 00:00:00
end: 2023-10-16 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 19/04/2022
// This is a combined strategy to generate cumulative signals.
//
// First Strategy
// EMA Crossover Indicator: Calculates the 2/20 period exponential moving average (EMA). 
// A sell signal is generated when price is below the EMA, and a buy signal when above.
//
// Second Strategy
// Bear Power Indicator:
// To get more information please see "Bull And Bear Balance Indicator" by Vadim Gimelfarb. 
//
//
// WARNING:
// - For educational purposes only
// - This script changes bar colors.
////////////////////////////////////////////////////////////
EMA20(Length) =>
    pos = 0.0
    xPrice = close
    xXA = ta.ema(xPrice, Length)
    nHH = math.max(high, high[1])
    nLL = math.min(low, low[1])
    nXS = nLL > xXA or nHH < xXA ? nLL : nHH
    iff_1 = nXS < close[1] ? 1 : nz(pos[1], 0)
    pos := nXS > close[1] ? -1 : iff_1
    pos

BP(SellLevel, BuyLevel) =>
    pos = 0.0
    value =  close < open  ?  
                 close[1] > open ?  math.max(close - open, high - low): high - low: 
                     close > open ? 
                         close[1] > open ? math.max(close[1] - low, high - close): math.max(open - low, high - close): 
                             high - close > close - low ?
```